# A sharp quartic skew-Schäffer defect and two-ray extremizer rigidity on real \(L^4\)

## Finding
Let \(X=L^4(\Omega,\mu;\mathbb R)\) have dimension at least two, and let \(\tau>0\). Put
\[
E_\tau=\tau\sqrt{(1+2\tau^2)(2+\tau^2)},\quad A_\tau=\tau(1-\tau^2),\quad B_\tau=3\tau^2+E_\tau,
\]
\[
\lambda_\tau=1+3\tau^2+\tau^4-E_\tau>0,\qquad R_\tau^2=B_\tau^2+4A_\tau^2.
\]
For every real \(f,g\in X\) (without normalization), the **exact quartic deficit identity** is
\[
\|f+\tau g\|_4^4+\|\tau f-g\|_4^4-\lambda_\tau(\|f\|_4^4+\|g\|_4^4)
=\frac{2}{B_\tau}\|A_\tau(f^2-g^2)+B_\tau fg\|_2^2.
\tag{1}
\]
In particular, for \(\|f\|_4=\|g\|_4=1\), the skew-Schäffer quartic deficit
\[
D_\tau(f,g)=\frac{\|f+\tau g\|_4^4+\|\tau f-g\|_4^4}{2}-\lambda_\tau
=\frac{\|A_\tau(f^2-g^2)+B_\tau fg\|_2^2}{B_\tau}
\tag{2}
\]
is nonnegative and has a **complete equality classification**. If \(\tau\ne1\), set
\[
\rho_\tau=-\frac{2A_\tau}{B_\tau+\sqrt{B_\tau^2+4A_\tau^2}},\qquad 0<|\rho_\tau|<1.
\]
Then \(D_\tau(f,g)=0\) if and only if almost everywhere \((f,g)\) lies on the two perpendicular real lines \(g=\rho_\tau f\) and \(g=-\rho_\tau^{-1}f\), with their respective \(f^4\)-masses necessarily
\[
\int_{\{g=\rho_\tau f,\ f\ne0\}}|f|^4\,d\mu=\frac{1}{1+\rho_\tau^4},\qquad
\int_{\{g=-\rho_\tau^{-1}f,\ f\ne0\}}|f|^4\,d\mu=\frac{\rho_\tau^4}{1+\rho_\tau^4}.
\tag{3}
\]
Both branches are essential. At \(\tau=1\), the identity reduces to \(D_1(f,g)=6\|fg\|_2^2\), so equality is equivalent to disjoint support.

The same deficit controls the **exactly sharp fourth-power distance to the pointwise two-line cone**. Define \(\mathscr C_\tau=\{(s,t)\in\mathbb R^2:A_\tau(s^2-t^2)+B_\tau st=0\}\) and \(d_\tau(s,t)=\operatorname{dist}_{\ell_2^2}((s,t),\mathscr C_\tau)\). For all unit \(f,g\),
\[
\boxed{\ \int_\Omega d_\tau(f(\omega),g(\omega))^4\,d\mu(\omega)
\ \le\ \frac{B_\tau}{B_\tau^2+4A_\tau^2}\,D_\tau(f,g).\ }
\tag{4}
\]
The coefficient is the smallest possible on **every** real \(L^4\) space of dimension at least two; equality is attained by unit vectors supported on two disjoint nonzero bands.

## Assumptions and scope
The measure space is arbitrary provided that the real \(L^4\) space has dimension at least two (so it contains two normalized disjointly supported nonzero functions). All statements use real scalars. There are no assumptions of finite measure, separability or nonatomicity. Parameter \(\tau\) is any positive real number. Formula (4) measures distance at each point to a cone of two lines, **not** distance to the globally normalized minimizer set. For complex \(L^4\) the displayed real factorization does not apply.

## Proof
Write \(a=\tau\) and \(E=a\sqrt{(1+2a^2)(2+a^2)}\), \(A=a(1-a^2)\), \(B=3a^2+E\), \(\lambda=1+3a^2+a^4-E\). For arbitrary real numbers \(s,t\), direct polynomial expansion gives
\[
(s+at)^4+(as-t)^4-\lambda(s^4+t^4)
=\frac{2}{B}[A(s^2-t^2)+Bst]^2.
\tag{5}
\]
To verify (5) independently, equate the coefficients of \(s^4+t^4\), \(s^3t-st^3\) and \(s^2t^2\). The resulting requirements are \(E-3a^2=2A^2/B\), \(4a(1-a^2)=4A\), and \(12a^2=2B-4A^2/B\). The first and third are equivalent to \(E^2=a^2(1+2a^2)(2+a^2)\), and the middle is the definition of \(A\). Integrating (5) gives (1) since all products belong to \(L^2\) by Hölder. Since \(B>0\), (2) follows. Positivity of \(\lambda\) follows from
\[
(1+3a^2+a^4)^2-E^2=(1+a^2)^4>0.
\]

For \(a\ne1\), the pointwise quadratic \(q(s,t)=A(s^2-t^2)+Bst\) factors as a nonzero scalar times \((t-\rho s)(t+s/\rho)\), where the roots solve \(A(1-r^2)+Br=0\). Their product is \(-1\) and the small root equals the claimed \(\rho\). Thus the zero set of \(q\) is precisely the two stated orthogonal lines. Equality in (2) forces \(q(f,g)=0\) almost everywhere and conversely. The unit constraints, applied to the two pointwise branches, read \(u+v=1\) and \(\rho^4u+\rho^{-4}v=1\), giving (3). Conversely, any partition into these branches with (3) defines a minimizer. When \(a=1\), \(A=0\) and \(B=6\), whence (2) becomes the stated disjoint-support defect. Existence of minimizers in any \(L^4\) of dimension at least two follows by assigning constant normalized coefficients of the two line directions to any two disjoint unit-supported vectors, choosing the coefficients to satisfy (3).

For stability, let \(Q=\begin{psmallmatrix}A&B/2\\B/2&-A\end{psmallmatrix}\), so \(q(s,t)=(s,t)Q(s,t)^\mathsf T\). Since \(Q\) is traceless symmetric with eigenvalues \(\pm R/2\), an orthogonal rotation turns \(q\) into \(Ruv\) (possibly with sign), and its two null lines become the \(u\)- and \(v\)-axes. Hence \(d_\tau(s,t)^4=\min\{|u|^4,|v|^4\}\le u^2v^2=q(s,t)^2/R^2\). Integrate and use (2), proving (4).

To show sharpness on an arbitrary admissible \(X\), take two disjoint nonzero unit \(L^4\) functions \(h_1,h_2\), and choose an orthonormal eigenbasis \(z_1=(c,d)\), \(z_2=(-d,c)\) of \(Q\). Let \(k=(c^4+d^4)^{-1/4}\), and set \(f=k(ch_1-dh_2)\), \(g=k(dh_1+ch_2)\). Both have fourth-power norm \(k^4(c^4+d^4)=1\). Each nonzero pointwise coordinate pair is along an eigenvector of \(Q\), hence equidistant from its two orthogonal null lines: \(|u|=|v|\). Consequently pointwise \(d^4=q^2/R^2\), making (4) an equality with \(D_\tau(f,g)>0\) and demonstrating that its coefficient cannot be lowered.

## Verification
The exact real-polynomial equality (5), the parameter identity for \(\lambda>0\), and finite positive-parameter sharpness witnesses are checked by the standalone `verify.py`, which uses symbolic polynomial arithmetic and real floating-point sanity checks. The analytical proof above, not these finite checks, establishes all-parameter and infinite-dimensional validity. For reproducibility run `python verify.py` with SymPy installed.

## Relationship to prior work
Xu and Liu, *Skew Schäffer Type Constants*, arXiv:2610.03050v1 (publicly posted 2 October 2026), Theorem 3.2 derive the **value** of the skew \(L^p\) fourth-power constant from a two-dimensional operator norm, and their source yields \(\lambda_\tau\) at \(p=4\). This result **does not claim that value as new**. Separately, the published mathematical finding *Exact skew geometric mean constant of* \(\ell_4\) (public mathematical repository, 4 October 2026) evaluates a related two-parameter matrix operator norm, but for an **arithmetic-mean supremum** rather than the quartic infimal deficit. Its generalized-eigenvalue computation supplies related algebra, not the exact nonnegative remainder (1), the complete infimal equality set (3), or the sharp cone-distance estimate (4). The classical \(\tau=1\) formula agrees with the standard quartic Clarkson identity. The new claim is the **structural defect, rigidity and sharp stability** for all positive skew parameters, not the already known norm constant.

## Limitations
The scalar field is real, and the constant is a pointwise two-line **distance** modulus, not a global distance-to-extremizers estimate. The case \(\tau=1\) is a classical boundary case; substantive new content concerns \(\tau\ne1\). A complete literature search is not a proof of absolute priority: an unindexed weighted quartic Clarkson refinement or equivalent two-dimensional spectral-defect identity could overlap. The source's normalization may differ in notation, so compare by the full fourth-power formula rather than parameter names.

## References
1. Y. Xu and Q. Liu, *Skew Schäffer Type Constants*, arXiv:2610.03050v1, 2 October 2026, https://arxiv.org/html/2610.03050v1 .
2. *Exact skew geometric mean constant of* \(\ell_4\), public mathematical finding (4 October 2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-exact-skew-geometric-mean-constant-of-ell-4--7a18ef79086d .
3. J. A. Clarkson, *Uniformly convex spaces*, Transactions of the American Mathematical Society **40** (1936), 396–414 (the classical \(\tau=1\) quartic comparison).
