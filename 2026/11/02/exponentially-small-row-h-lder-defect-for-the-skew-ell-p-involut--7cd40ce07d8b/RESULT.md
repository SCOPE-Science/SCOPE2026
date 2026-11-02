# Exponentially small row-Hölder defect for the skew \(\ell_p\) involution

## Finding
Fix \(0<\tau<1\). On the real two-coordinate space \(\ell_p^2\), put
\[
A_\tau=\begin{pmatrix}1&\tau\\ \tau&-1\end{pmatrix},\qquad
\nu_p(\tau)=\|A_\tau\|_{\ell_p^2\to\ell_p^2},\qquad
q=\frac{p}{p-1},\qquad R_p=(1+\tau^q)^{1/q}.
\]
The quantity \(R_p\) is the sharp Hölder norm of the first row and hence a **lower** bound for \(\nu_p\), not an upper bound. Define
\[
s_{0,p}=\tau^{1/(p-1)},\qquad
\rho=\frac{1-\tau}{1+\tau},\qquad
\rho_p=\frac{s_{0,p}-\tau}{1+\tau s_{0,p}}.
\]
For every sufficiently large real \(p\), there is a unique \(s_p\in(s_{0,p},1)\) satisfying
\[
s_p^{p-1}-\tau=(1+\tau s_p^{p-1})
\left(\frac{s_p-\tau}{1+\tau s_p}\right)^{p-1}.
\]
Exactly the two real projective lines spanned by \((1,s_p)\) and \((s_p,-1)\) attain \(\nu_p\). The maximizer displacement and the norm defect have sharp equivalent forms:
\[
s_p-s_{0,p}\sim
\frac{s_{0,p}(1+\tau^2)}{\tau(p-1)}\rho_p^{p-1},\qquad
\frac{\nu_p}{R_p}-1\sim\frac{\rho_p^p}{p}.
\]
Consequently the exact exponential coefficient is
\[
\boxed{\lim_{p\to\infty}\frac{p(\nu_p-R_p)}{\rho^p}
=(1+\tau)\tau^{(1+\tau^2)/(1-\tau^2)}.}
\]
In particular the row-Hölder lower bound is always strict for all sufficiently large finite \(p\), although the difference is smaller than every power of \(1/p\).

Xu and Liu's exact \(L_p\) relation for the skew Schäffer constant \(S_{L_p,p}(\tau)=(1+\tau^2)/\nu_p\) therefore gives, whenever the real \(L_p\) space has dimension at least two,
\[
\boxed{\lim_{p\to\infty}\frac p{\rho^p}
\left(\frac{1+\tau^2}{R_p}-S_{L_p,p}(\tau)\right)
=\frac{1+\tau^2}{1+\tau}\tau^{(1+\tau^2)/(1-\tau^2)}.}
\]

## Assumptions and scope
All scalars are real. The skew parameter \(\tau\) is fixed strictly between zero and one; limits as \(p\to\infty\) are pointwise in \(\tau\), not uniform near \(\tau=0\) or \(\tau=1\). Exponents \(p\) need not be integers. Every statement about maximizing directions concerns the two-dimensional operator matrix above; the final formula for \(S_{L_p,p}\) uses the previously established identity and requires a real \(L_p\) space of dimension at least two. No assertion is made about complex scalars or a simultaneous scaling of \(p\) and \(\tau\).

One explicit sufficient choice of the phrase “sufficiently large” is any real \(p\ge3\) satisfying all three inequalities
\[
\begin{aligned}
&\tau-\tau^{p-1}-\tau^{p-1}(1+\tau^p)>0,\\
&1-\tau-(1+\tau)\rho^{p-1}>0,\\
&\tau(1-\tau\rho^{p-1})-(1+\tau)(1+\tau^2)\rho^{p-2}>0.
\end{aligned}
\]
For each fixed \(0<\tau<1\), all three hold for every sufficiently large \(p\).

## Proof
**1. Projective reduction and sign comparison.** By homogeneity write
\[
f_p(s)=\frac{\bigl(|1+\tau s|^p+|\tau-s|^p\bigr)^{1/p}}
{(1+|s|^p)^{1/p}},\qquad s\in\mathbb R.
\]
The missing projective line is the limiting input \((0,1)\). The signed-coordinate quarter-turn \(J(a,b)=(-b,a)\) satisfies \(A_\tau J=-JA_\tau\), so \(f_p(s)=f_p(-1/s)\) for nonzero \(s\), including the limiting lines. For \(0\le u\le1\), the two output pairs associated with \(f_p(u)\) and \(f_p(-u)\) have the same sum of squares, \((1+\tau^2)(1+u^2)\). The first pair is
\((1+\tau u,|\tau-u|)\), whereas the second is
\((1-\tau u,\tau+u)\). Since
\[
1+\tau u\ge\max\{1-\tau u,\tau+u,|\tau-u|\},
\]
its maximum coordinate is at least that of the second pair. For \(p>2\), the two-variable \(p\)-power sum at a fixed Euclidean sum is strictly increasing with the larger coordinate. Hence \(f_p(u)>f_p(-u)\) for \(0<u<1\) and \(f_p(u)\ge f_p(-u)\) at the endpoints. Combining this with the quarter-turn symmetry reduces the global maximum to \(0\le s\le1\), with precisely the symmetric negative projective direction whenever the unique maximizing positive slope belongs to \((0,1)\).

**2. Exact derivative and uniqueness.** On \(0\le s<\tau\), set \(a=1+\tau s\) and \(b=\tau-s\). After removing a strictly positive factor, the derivative of \(f_p\) has the sign of
\[
F_<(s)=a^{p-1}(\tau-s^{p-1})-b^{p-1}(1+\tau s^{p-1}).
\]
For sufficiently large \(p\), the sufficient condition in the assumptions gives
\[
F_<(s)\ge \tau-\tau^{p-1}-\tau^{p-1}(1+\tau^p)>0.
\]
On \(\tau\le s\le1\), replace \(b\) by \(s-\tau\). The derivative has the sign of
\[
F_>(s)=a^{p-1}(\tau-s^{p-1})+(s-\tau)^{p-1}(1+\tau s^{p-1}).
\]
Thus the derivative is positive up to \(s=s_{0,p}=\tau^{1/(p-1)}\). For \(s\ge s_{0,p}\), put \(r(s)=(s-\tau)/(1+\tau s)\) and
\[
H_p(s)=s^{p-1}-\tau-(1+\tau s^{p-1})r(s)^{p-1}.
\]
Then \(F_>(s)=-(1+\tau s)^{p-1}H_p(s)\). Observe that \(H_p(s_{0,p})<0\) and
\[
H_p(1)=1-\tau-(1+\tau)\rho^{p-1}>0.
\]
Since \(0<r(s)\le\rho\), \(r'(s)=(1+\tau^2)/(1+\tau s)^2\le1+\tau^2\), and \(s^{p-2}\ge\tau\) on this interval, differentiation gives
\[
\frac{H_p'(s)}{p-1}\ge
\tau(1-\tau\rho^{p-1})
-(1+\tau)(1+\tau^2)\rho^{p-2}>0.
\]
Hence \(H_p\) has exactly one zero \(s_p\in(s_{0,p},1)\) and \(f_p\) increases before that zero and decreases after it. Together with Step 1, this proves the exact two-line maximizing classification.

**3. Exponentially small maximizer displacement.** The critical-point identity implies
\[
0<s_p^{p-1}-\tau
=(1+\tau s_p^{p-1})r(s_p)^{p-1}
\le(1+\tau)\rho^{p-1}.
\]
The mean value theorem on \([s_{0,p},s_p]\), where \(s^{p-2}\ge\tau\), gives
\(s_p-s_{0,p}=O_\tau(\rho^{p-1}/p)\). Since \(r'(s)/r(s)\) stays bounded on this shrinking interval, one has
\[
\frac{r(s_p)^{p-1}}{\rho_p^{p-1}}\longrightarrow1.
\]
Applying the mean value theorem again to the critical-point identity, now with derivative \((p-1)s_{0,p}^{p-2}=(p-1)\tau/s_{0,p}\) to leading order, yields
\[
s_p-s_{0,p}\sim
\frac{s_{0,p}(1+\tau^2)}{\tau(p-1)}\rho_p^{p-1}.
\]

**4. Norm correction and sharp coefficient.** Define the single-row quotient
\[
U_p(s)=\frac{1+\tau s}{(1+s^p)^{1/p}}.
\]
Hölder's equality condition yields \(U_p(s_{0,p})=R_p\), and
\[
\frac{d}{ds}\log U_p(s)
=\frac{\tau-s^{p-1}}{(1+\tau s)(1+s^p)}.
\]
On \([s_{0,p},s_p]\) its second derivative is \(O_\tau(p)\), and the first derivative vanishes at \(s_{0,p}\). Consequently
\[
\log\frac{U_p(s_p)}{R_p}
=O_\tau\bigl(p(s_p-s_{0,p})^2\bigr)
=o_\tau(\rho_p^p/p).
\]
Moreover, \(r(s_p)^p/\rho_p^p\to1\). The exact factorization
\[
\nu_p=U_p(s_p)\bigl(1+r(s_p)^p\bigr)^{1/p}
\]
then implies
\[
\frac{\nu_p}{R_p}-1\sim\frac{\rho_p^p}{p}.
\]
Finally, \(s_{0,p}=\exp((\log\tau)/(p-1))\), and a one-term Taylor expansion at \(s=1\) shows
\[
\lim_{p\to\infty}p\bigl(\log\rho_p-\log\rho\bigr)
=\frac{1+\tau^2}{1-\tau^2}\log\tau.
\]
Hence \(\rho_p^p/\rho^p\to\tau^{(1+\tau^2)/(1-\tau^2)}\), while \(R_p\to1+\tau\). Substitution gives the boxed norm limit. The cited identity for \(S_{L_p,p}\) and the reciprocal expansion give its boxed counterpart.

## Verification
The proof controls all real exponents above an explicit sufficient threshold and every projective input direction. The supplementary `check.py`, using only Python's standard library with 180-digit decimal precision, checks critical-point brackets, sampled global inequalities, scaled norm and displacement coefficients, and the exponential rate conversion for \(\tau=0.2,0.5,0.8\) and finite exponents \(p=12,20,30,50,80\). The checker prints **12,120 passed assertions**. Such sampling is not an infinite-dimensional proof, an exhaustive parameter search, or a publication-priority certificate; the analytical argument above provides the universal quantifiers.

## Relationship to prior work
Xu and Liu derive the exact expression for the skew Schäffer constant on real \(L_p\) via the matrix norm \(\nu_p\) and supply endpoint and interpolation information. Their 2026 preprint does not determine a sharp beyond-all-orders norm defect relative to the exact single-row Hölder bound, or classify maximizing directions in this high-exponent regime. The 2025 skew James work concerns a different extremal convention. A 2026 two-coordinate matrix-norm reduction for a generalized James constant identifies the same type of matrix norm without evaluating intermediate exponents asymptotically. Results on skew constants for a hexagonal plane or the Banaś–Frączek plane concern different norms or a small-skew limit and do not imply this fixed-skew, high-exponent law.

## Limitations
The coefficient is pointwise in the fixed skew parameter; it is not a uniform result as \(\tau\to0\) or \(\tau\to1\). The theorem establishes high-exponent behavior, not an elementary closed form for \(\nu_p\) at every finite exponent. It applies directly to the real two-coordinate matrix norm and transfers to skew Schäffer constants only through Xu and Liu's established identity. No independent mathematical validation or exhaustive historical-priority audit has been performed; an older high-exponent matrix norm estimate phrased without geometric-constant terminology remains a plausible priority risk.

## References
1. Y. Xu and Q. Liu, *Skew Schäffer Type Constants*, arXiv:2610.03050v1 (first public version 2026-10-02), Theorem 3.2 and its \(L_p\) calculations, https://arxiv.org/abs/2610.03050.
2. *The skew James type constant in Banach spaces*, arXiv:2504.00827v1 (2025), https://arxiv.org/abs/2504.00827.
3. X. Yang and C. Yang, *An inequality between \(L_{\mathrm{YJ}}(\lambda,\mu,X)\) constant and generalized James constant*, Mathematical Inequalities & Applications 27 (2024), 571–581, DOI:10.7153/mia-2024-27-39.
