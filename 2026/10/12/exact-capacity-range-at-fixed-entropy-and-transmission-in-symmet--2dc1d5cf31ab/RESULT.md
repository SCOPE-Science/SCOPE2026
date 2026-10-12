# Exact capacity range at fixed entropy and transmission in symmetric double-brane conformal interfaces
## Finding
Consider the pure-tension double-brane holographic interface family with symmetric outer radii
\[
L_L=L_R=L,
\qquad
L_C=rL,
\qquad
0<r<1,
\]
and common Newton constant \(G_N\). Define the outer-theory central charge \(c=3L/(2G_N)\), the dimensionless brane tensions
\[
x=8\pi G_NL\sigma_L,
\qquad
y=8\pi G_NL\sigma_R,
\]
and the normalized energy-transmission coefficient \(t=c_{LR}/c\).

At fixed entropy coefficient \(c_{\mathrm{eff}}/c=r\) and fixed transmission \(t\), write
\[
d=\frac{x-y}2.
\]
Then the capacity coefficient has the exact one-parameter law
\[
\frac{c_{\mathrm{cap}}}c
=
\frac{r^2}t-r^2td^2.
\]
The Israel junction inequalities imply
\[
\frac{r}{1+2r}<t<r
\]
and
\[
|d|<\Delta(r,t),
\qquad
\Delta(r,t)=1-\left|\frac1t-1-\frac1r\right|.
\]
Consequently the complete feasible capacity range at fixed \(r\) and \(t\) is
\[
\frac{r^2}t-r^2t\Delta(r,t)^2
<
\frac{c_{\mathrm{cap}}}c
\le
\frac{r^2}t.
\]
The upper endpoint is attained uniquely by equal tensions \(x=y\), and therefore
\[
c_{\mathrm{cap,max}}
=
\frac{c_{\mathrm{eff}}^2}{c_{LR}}.
\]
The lower endpoint is an infimum, not a minimum, because the Israel bounds are strict.

For the example in arXiv:2610.02309v1 with \(r=1/2\) and \(t=1/3\), the theorem gives
\[
\frac23<\frac{c_{\mathrm{cap}}}c\le\frac34.
\]
The equal split \((x,y)=(2,2)\) gives \(3/4\), while \((x,y)=(3/2,5/2)\) gives \(35/48\), reproducing the two values displayed in the source and locating every other allowed split between them and the sharp lower infimum.

## Assumptions and scope
The claim is restricted to the pure-tension double-brane family and to symmetric outer radii \(L_L=L_R=L\) with \(L_C=rL\), \(0<r<1\). It uses the classical holographic formulas and strict Israel tension bounds of arXiv:2610.02309v1. It does not claim a universal upper bound on capacity of entanglement for arbitrary conformal interfaces, nor does it identify a minimum on the excluded Israel boundary.

The dimensionless variables are defined above. Fixing \(r\) fixes \(c_{\mathrm{eff}}/c\). Fixing \(t\) fixes the tension sum, so the only remaining real parameter is the tension asymmetry \(d\).

## Proof
The source gives, for the double-brane model,
\[
c_{\mathrm{eff}}=\frac{3L_C}{2G_N},
\]
\[
c_{\mathrm{cap}}
=
\frac{2L_Cc_{\mathrm{eff}}}
{L_L/(1+8\pi G_NL_L\sigma_L)+L_R/(1+8\pi G_NL_R\sigma_R)},
\]
and
\[
c_{LR}
=
\frac3{G_N\bigl(L_L^{-1}+L_R^{-1}+8\pi G_N(\sigma_L+\sigma_R)\bigr)}.
\]
After substituting \(L_L=L_R=L\), \(L_C=rL\), and the definitions of \(c,x,y\), these become
\[
\frac{c_{\mathrm{eff}}}c=r,
\qquad
\frac{c_{LR}}c=\frac2{2+x+y},
\]
and
\[
\frac{c_{\mathrm{cap}}}c
=
\frac{2r^2(1+x)(1+y)}{2+x+y}.
\]
Put \(S=x+y\). Since \(t=2/(S+2)\), one has
\[
\frac S2=\frac1t-1.
\]
Writing \(x=S/2+d\) and \(y=S/2-d\),
\[
(1+x)(1+y)
=
\left(1+\frac S2\right)^2-d^2
=
\frac1{t^2}-d^2.
\]
Substitution gives the exact quadratic identity
\[
\frac{c_{\mathrm{cap}}}c
=r^2t\left(\frac1{t^2}-d^2\right)
=
\frac{r^2}t-r^2td^2.
\]

For each brane, the source's strict Israel inequality is
\[
\frac1{L_C}-\frac1L
<8\pi G_N\sigma_i<
\frac1{L_C}+\frac1L.
\]
Thus
\[
a<x,y<b,
\qquad
a=\frac1r-1,
\qquad b=\frac1r+1.
\]
A fixed sum \(S\) is feasible exactly when \(2a<S<2b\). Using \(S=2/t-2\), this is equivalent to
\[
\frac r{1+2r}<t<r.
\]
The interval \((a,b)\) has center \(1/r\) and half-width \(1\). Because \(S/2=1/t-1\), both tensions lie in this interval exactly when
\[
|d|<1-\left|\frac1t-1-\frac1r\right|=\Delta(r,t).
\]
For every feasible \(t\), \(\Delta(r,t)>0\). The quadratic capacity law is strictly decreasing in \(d^2\), so its unique maximum is at \(d=0\), while its infimum is approached as \(|d|\uparrow\Delta(r,t)\). This proves the full range and the uniqueness of the equal-tension maximizer. Finally,
\[
c\frac{r^2}t
=
\frac{(rc)^2}{tc}
=
\frac{c_{\mathrm{eff}}^2}{c_{LR}},
\]
which gives the invariant form of the maximum.

## Verification
The proof is symbolic and valid for every \(0<r<1\) and every feasible \(t\). The accompanying verification script independently checks the algebraic identities, the strict feasible interval, and the source's two displayed examples. Finite numerical checks are corroborative only and are not used as proof of the quantified statement.

## Relationship to prior work
Kusuki, Suzuyama, and Tang introduce the capacity coefficient for conformal interfaces, give the double-brane formulas above, and emphasize that at fixed radii the energy-transmission coefficient depends only on the sum of the two brane tensions while the capacity coefficient depends on their split. Their Table 1 exhibits two tension splits with the same entropy and transmission data but different capacities. The inspected source does not give the complete range over all allowed splits, the exact quadratic asymmetry law, or the unique equal-tension maximizer.

Baig and Karch developed the underlying double-brane holographic interface model and its transmission/boundary-entropy data before the capacity-of-entanglement coefficient used here was introduced. That earlier work therefore does not state the capacity range proved above.

## Limitations
The result is an exact optimization inside the symmetric-radius pure-tension double-brane model. It does not prove that equal tensions maximize capacity in asymmetric-radius models, interfaces outside the double-brane construction, or non-holographic theories. The lower endpoint is not attained under the strict Israel inequalities. The general equality problem for the interface inequality \(c_{\mathrm{eff}}\le c_{\mathrm{cap}}\), and a general upper bound on \(c_{\mathrm{cap}}\), remain outside this result.

## References
1. Y. Kusuki, K. Suzuyama, and Y. Tang, *Entanglement Requires Fluctuations at Conformal Interfaces*, arXiv:2610.02309v1 (first public 2026-10-01).
2. A. Baig and A. Karch, *Double brane holographic model dual to 2d ICFTs*, arXiv:2206.01752v1; JHEP 10 (2022) 110, doi:10.1007/JHEP10(2022)022.
