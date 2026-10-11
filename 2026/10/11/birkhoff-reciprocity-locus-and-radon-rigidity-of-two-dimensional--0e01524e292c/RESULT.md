# Birkhoff reciprocity locus and Radon rigidity of two-dimensional Lorentz sequence spaces
## Finding
Let \(1<q<\infty\) and \(0<\omega\le1\), and equip \(\mathbb R^2\) with the two-dimensional Lorentz norm
\[
N_{\omega,q}(x_1,x_2)=\bigl((\max\{|x_1|,|x_2|\})^q+\omega(\min\{|x_1|,|x_2|\})^q\bigr)^{1/q}.
\]
For every \(t\in(0,1)\), put
\[
x_t=(1,t),\qquad y_t=(\omega t^{q-1},-1).
\]
Then \(x_t\perp_B y_t\), while
\[
y_t\perp_B x_t\quad\Longleftrightarrow\quad \omega^q t^{q(q-2)}=1.
\]
Consequently, among this full smooth Lorentz family, Birkhoff--James orthogonality is symmetric, equivalently the plane is a Radon plane, if and only if \((\omega,q)=(1,2)\), the Euclidean case. More precisely, for \(q>2\) no ordered interior smooth direction is reciprocal; for \(1<q<2\) and \(0<\omega<1\) the unique reciprocal parameter in \((0,1)\) is \(t=\omega^{1/(2-q)}\); for \(q=2\), all such directions are reciprocal exactly when \(\omega=1\).

Here \(x\perp_B y\) means Birkhoff--James orthogonality: \(N(x)\le N(x+s y)\) for every real \(s\). A reciprocal pair means that both \(x\perp_B y\) and \(y\perp_B x\) hold.

## Assumptions and scope
The scalar field is real. The parameters satisfy \(1<q<\infty\) and \(0<\omega\le1\). The displayed norm is the standard two-dimensional Lorentz sequence norm \(d^{(2)}(\omega,q)\). The explicit reciprocity formula concerns ordered smooth directions with \(0<t<1\); signed coordinate permutations carry this sector to all smooth directions whose coordinate magnitudes are distinct and nonzero. The Radon conclusion is global because a Radon plane requires Birkhoff--James orthogonality to be symmetric for every pair.

## Proof
On the open sector \(x_1>x_2>0\), the function
\[
F(x_1,x_2)=N_{\omega,q}(x_1,x_2)^q=x_1^q+\omega x_2^q
\]
is differentiable. Since \(q>1\), the norm is smooth there, and the standard supporting-functional criterion gives
\[
x\perp_B y\quad\Longleftrightarrow\quad D F(x)[y]=0.
\]
For \(x_t=(1,t)\),
\[
D F(x_t)=q(1,\omega t^{q-1}).
\]
Hence with
\[
y_t=(\omega t^{q-1},-1)
\]
one has
\[
D F(x_t)[y_t]=q\bigl(\omega t^{q-1}-\omega t^{q-1}\bigr)=0,
\]
so \(x_t\perp_B y_t\).

Set
\[
a=\omega t^{q-1}.
\]
Because \(0<\omega\le1\) and \(0<t<1\), one has \(0<a<1\). Thus \(y_t=(a,-1)\) lies in the smooth sector where the second coordinate has larger absolute value. There
\[
N_{\omega,q}(u,v)^q=|v|^q+\omega|u|^q,
\]
and at \(y_t\) its derivative is proportional to
\[
(\omega a^{q-1},-1).
\]
Therefore
\[
y_t\perp_B x_t
\quad\Longleftrightarrow\quad
\omega a^{q-1}-t=0.
\]
Substituting \(a=\omega t^{q-1}\) gives
\[
t=\omega\bigl(\omega t^{q-1}\bigr)^{q-1}
=\omega^q t^{(q-1)^2}.
\]
Since \(t>0\), this is equivalent to
\[
\omega^q t^{q(q-2)}=1.
\]
This proves the exact reciprocity criterion.

If \(q>2\), then \(q(q-2)>0\), so for every \(0<t<1\),
\[
\omega^q t^{q(q-2)}<1,
\]
and no ordered interior smooth direction is reciprocal. If \(q=2\), the criterion is \(\omega^2=1\), which under \(0<\omega\le1\) holds exactly for \(\omega=1\). If \(1<q<2\), then for \(0<\omega<1\) the criterion has the unique solution
\[
t=\omega^{1/(2-q)}\in(0,1),
\]
while for \(\omega=1\) it has no solution in \((0,1)\).

Thus, unless \((\omega,q)=(1,2)\), there exists a smooth pair with \(x\perp_B y\) but \(y\not\perp_B x\), so the plane is not Radon. At \((\omega,q)=(1,2)\),
\[
N_{1,2}(x_1,x_2)=\sqrt{x_1^2+x_2^2},
\]
and ordinary Euclidean orthogonality is symmetric. Hence the Lorentz plane is Radon exactly in the Euclidean case.

## Verification
The argument does not infer global symmetry from sampling. It constructs, for every non-Euclidean parameter pair, an analytic one-parameter family of Birkhoff-orthogonal pairs and computes the reverse condition exactly. Both vectors lie in smooth sectors, so the supporting functional is unique and the derivative criterion is sufficient and necessary.

The exponent reduction was checked algebraically:
\[
(q-1)^2-1=q(q-2).
\]
For \(1<q<2\), solving \(\omega^q t^{-q(2-q)}=1\) gives exactly \(t=\omega^{1/(2-q)}\). For \(q>2\), strict failure follows from \(0<\omega\le1\) and \(0<t<1\). The boundary case \((\omega,q)=(1,2)\) is exactly Euclidean.

## Relationship to prior work
Kato and Maligranda studied the same two-dimensional Lorentz sequence spaces \(d^{(2)}(\omega,q)\) and computed classical James and Jordan--von Neumann constants in the super-Hilbert range. Suzuki, Yamano, and Kato later wrote the norm explicitly in the max/min form used here and continued the James-constant problem; their paper classifies the subject under MSC 46B20. These works motivate the family but address geometric constants rather than reciprocity of Birkhoff--James orthogonality.

Komuro, Saito, and Tanaka characterize Radon planes abstractly through generalized Day--James constructions, and the general Minkowski-plane literature identifies Radon planes precisely with symmetry of Birkhoff orthogonality. The present calculation instead gives an object-specific reciprocity locus inside the classical Lorentz family and shows directly that its only Radon member is the Euclidean one.

Database searches using the Lorentz notation, Radon-plane terminology, symmetric Birkhoff orthogonality, and the max/min norm formula located no statement of the displayed criterion \(\omega^q t^{q(q-2)}=1\) or the resulting Lorentz-family classification.

## Limitations
The formula is restricted to \(1<q<\infty\), where the chosen off-axis, off-diagonal points are smooth. The nonsmooth endpoints \(q=1\) and \(q=\infty\) are not classified here. The proof identifies the full reciprocity locus only on the smooth ordered sector; this suffices for the global Radon classification but does not enumerate every reciprocal pair involving axes or diagonal nonsmooth points.

The full text of the 2001 same-object Lorentz paper could not be reliably matched by the available lawful retrieval route during this review, so its abstract and bibliographic metadata were used only to establish same-object context, not whole-document noncoverage. Likewise, the 2020 general Radon characterization was compared at the theorem/abstract level; a hidden object-specific Lorentz example remains a residual bibliographic risk.

## References
1. M. Kato and L. Maligranda, “On James and Jordan--von Neumann constants of Lorentz sequence spaces,” *Journal of Mathematical Analysis and Applications* 258 (2001), 457--465, DOI 10.1006/jmaa.2000.7367. Published 15 June 2001.
2. T. Suzuki, A. Yamano, and M. Kato, “The James Constant of 2-Dimensional Lorentz Sequence Spaces,” *Bulletin of the Kyushu Institute of Technology, Pure and Applied Mathematics* 53 (2006), 15--24, hdl:10228/3185. Published 30 March 2006; MSC 46B20.
3. N. Komuro, K.-S. Saito, and R. Tanaka, “A characterization of Radon planes using generalized Day--James spaces,” *Annals of Functional Analysis* 11 (2020), 62--74, DOI 10.1007/s43034-019-00018-z.
