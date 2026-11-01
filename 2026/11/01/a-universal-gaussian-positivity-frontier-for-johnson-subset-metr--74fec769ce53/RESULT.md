# A universal Gaussian positivity frontier for Johnson subset metrics

## Finding
For integers \(k\ge3\) and \(n\ge2k\), let \(\mathcal J_{n,k}\) be the set of \(k\)-element subsets of \(\{1,\ldots,n\}\), with shortest-path Johnson distance \(d(S,T)=k-|S\cap T|\). Set \(K_x(S,T)=x^{d(S,T)^2}\) for \(0<x\le1\), and take \(K_0=I\).

Define \(B_k(x)=\sum_{r=0}^{k}(-1)^r\binom{k}{r}x^{r^2}\), and write \(\rho_k\) for its unique zero in \((0,1/(k-1))\). Then, independently of \(n\), the exact **first loss of positive semidefiniteness** is \(\rho_k\):

\[
K_x\succ0\quad (0\le x<\rho_k),\qquad K_{\rho_k}\succeq0,\qquad K_x\not\succeq0\quad (\rho_k<x\le1/(k-1)).
\]

The endpoint nullity and rank are
\[
\operatorname{nullity}K_{\rho_k}=\binom nk-\binom n{k-1},\qquad
\operatorname{rank}K_{\rho_k}=\binom n{k-1}.
\]
For the squared-distance Gaussian \(x=e^{-t}\), the sharp eventual-positivity bandwidth is \(t_k=-\log\rho_k\): every \(t>t_k\) gives strict positive definiteness, the endpoint is semidefinite, and parameters immediately below \(t_k\) give indefinite matrices. No claim is made here about possible further positivity intervals at smaller \(t\). Approximate \(\rho_k\) values for \(k=3,4,5\) are \(0.347969427509\), \(0.256486788955\), and \(0.203423608558\).

## Assumptions and scope
All matrices are real symmetric over \(\mathbb R\), with complex positive semidefiniteness equivalent. The integer restrictions are \(k\ge3\) and \(n\ge2k\). The distance is graph distance on the Johnson graph, **not** binary Hamming distance: the latter equals twice the former on the fixed-weight slice. The result concerns the full family of \(\binom nk\times\binom nk\) matrices. The word “frontier” denotes the first change of sign as \(x\) increases from zero, or equivalently the smallest bandwidth beyond which all larger bandwidths work; it does not assert a global iff statement for every \(0<x<1\).

## Proof
**1. Positive-kernel expansion.** Fix \(x\in(0,1)\). For \(0\le j\le k\), define
\[
c_j(x)=\sum_{r=0}^{j}(-1)^r\binom jr x^{(k-j+r)^2}.
\]
Newton interpolation on the integers \(0,\dots,k\) gives, for \(h=0,\ldots,k\),
\[
x^{(k-h)^2}=\sum_{j=0}^k c_j(x)\binom hj.
\]
Let \(T_j\) be the inclusion matrix with rows indexed by \(k\)-subsets \(S\), columns by \(j\)-subsets \(R\), and entry \(\mathbf1_{\{R\subset S\}}\). Since \((T_jT_j^{\mathsf T})(S,T)=\binom{|S\cap T|}{j}\), the kernel has the **exact identity**
\[
K_x=\sum_{j=0}^k c_j(x)T_jT_j^{\mathsf T},\qquad T_k=I,\qquad c_k(x)=B_k(x).
\]
No limiting operation or numerical approximation enters this decomposition.

**2. Positivity of the lower levels.** Suppose \(0<x\le1/(k-1)\), put \(m=k-1\), and fix \(j<k\) with \(s=k-j\ge1\). Then
\[
\frac{c_j(x)}{x^{s^2}}=\sum_{r=0}^j(-1)^r\binom jr x^{r^2+2sr}.
\]
The even terms after the constant are nonnegative. For every odd \(r\ge1\), \(r^2+2sr\ge3r\). The sum of their magnitudes is bounded above by
\[
(1+x^3)^j-1\le e^{jx^3}-1\le e^{1/m^2}-1\le e^{1/4}-1<1.
\]
Therefore \(c_j(x)>0\) for every \(j<k\) throughout this interval.

**3. Unique first zero.** Differentiation yields
\[
B'_k(x)\le-k+\sum_{r=2}^k r^2\binom kr x^{2r-1}
=-k+kx\big((1+x^2)^{k-1}-1\big)+k(k-1)x^3(1+x^2)^{k-2}.
\]
For \(0\le x\le1/m\), each exponential factor is smaller than \(e^{1/m}<2\), so
\[
B'_k(x)<k\big(-1+1/m+2/m^2\big)\le0\qquad(m\ge2).
\]
The inequality is strict also for \(m=2\). Hence \(B_k\) is strictly decreasing on the whole bracket. At its right endpoint, discarding negative terms and bounding positive terms by powers \(x^{2r}\) gives
\[
B_k(1/m)\le(1+m^{-2})^{m+1}-(m+1)^2/m^2<0.
\]
For \(m=2\), the final inequality is \((5/4)^3<9/4\). For \(m\ge3\), take logarithms and use \((m+1)/m^2<2/(m+1)\le2\log(1+1/m)\). Since \(B_k(0)=1\), exactly one simple zero \(\rho_k\in(0,1/m)\) exists.

**4. Sharpness and nullity.** Steps 1–3 imply all \(c_j(x)>0\) for \(0<x<\rho_k\), so \(K_x\succ0\), and \(K_0=I\). At \(x=\rho_k\), \(c_k=0\) and every lower coefficient is positive. The inclusion matrix \(T_{k-1}\) has full column rank for \(n\ge2k\). Indeed, for the Boolean-lattice up and down operators \(U_r\) and \(D_r=U_{r-1}^{\mathsf T}\), direct double-counting gives
\[
D_{r+1}U_r-U_{r-1}D_r=(n-2r)I.
\]
Putting \(r=k-1\) yields \(\|U_{k-1}f\|^2=\|D_{k-1}f\|^2+(n-2k+2)\|f\|^2\), proving injectivity. For \(j<k\), every column of \(T_j\) is a linear combination of columns of \(T_{k-1}\): sum over its \((k-1)\)-set supersets and divide by \(k-j\). Consequently the endpoint matrix has rank exactly \(\binom n{k-1}\). For any nonzero \(v\in\ker(T_{k-1}^{\mathsf T})\), all lower-level terms vanish and \(K_xv=B_k(x)v\). The nullspace has dimension \(\binom nk-\binom n{k-1}>0\). When \(\rho_k<x\le1/m\), its eigenvalue \(B_k(x)<0\), proving indefiniteness and sharpness.

## Verification
Run `python3 check_johnson.py` from the folder containing that supplied standalone artifact. It requires only Python standard-library modules. It verifies 75 rational lower-coefficient signs, 5,300 exact inclusion-kernel matrix entries at orders 3 and 4, and 8,410 exact top-eigenspace matrix components at orders 3–6, plus rational right-endpoint signs and numerical first-root brackets through order 12. This finite checking is corroborative; the preceding inequalities and the up/down commutator establish the universal result.

## Relationship to prior work
The Johnson association-scheme eigenvalues were derived by Krebs and Shaheen (2008); their primary paper studies distance-class adjacency spectra rather than the Gaussian first-loss frontier or the stated endpoint ranks. Feragen, Lauze, and Hauberg (arXiv:1411.0296, first submitted 2014-11-02) explain why geodesic Gaussian positivity must be checked carefully, but give no Johnson-slice bandwidth classification. Prior all-alphabet Hamming-cube Gaussian threshold work involves a different metric space: restricting binary Hamming kernels to a constant-weight slice replaces Hamming distance by twice Johnson distance, so its general positive-definiteness range does not yield the sharp present frontier. The top polynomial \(B_k\) is shared, but the universal sufficiency on Johnson slices and exact endpoint rank require the inclusion-kernel argument above.

## Limitations
The theorem controls the complete first positivity interval and its first failure, and identifies the sharp **eventual** positivity bandwidth. It does not classify every possible disjoint positivity interval in \((1/(k-1),1)\); at \(x=1\) the all-ones matrix is semidefinite. Originality was assessed against the cited accessible sources and public research records; a previously unpublished equivalent Johnson-kernel specialization cannot be excluded. No independent audit has been performed.

## References
1. M. Krebs and A. Shaheen, *On the Spectra of Johnson Graphs*, Electronic Journal of Linear Algebra 17 (2008), 154–167, DOI: 10.13001/1081-3810.1256, available at https://emis.de/ft/34459.
2. A. Feragen, F. Lauze, and S. Hauberg, *Geodesic Exponential Kernels: When Curvature and Linearity Conflict*, arXiv:1411.0296, initial submission 2014-11-02, https://arxiv.org/abs/1411.0296.
