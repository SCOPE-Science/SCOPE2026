# Sharp conductance and placement thresholds for path shortcuts

## Finding

Let \(n\ge4\), and let \(P_n\) be the path on vertices \(0,\ldots,n-1\), with unit conductance on each original edge. One may add exactly one edge joining nonadjacent vertices \(i<j\), with independently prescribed conductance \(w>0\). Write \(\alpha_n(i,j;w)\) for the second-smallest eigenvalue of the augmented combinatorial Laplacian. Put
\[
\theta=\frac{2\pi}{n},\qquad \Lambda_n=2-2\cos\theta.
\]

**Theorem (complete saturation classification).** For every such edge and every \(w>0\),
\[
\alpha_n(i,j;w)\le\Lambda_n.
\]
Equality holds **if and only if**
\[
i+j=n-1,\qquad
\sin((2i+1)\theta)>0,\qquad
w\sin((2i+1)\theta)\ge\sin\theta.
\]
Consequently, the minimum shortcut conductance at which *some* placement attains the universal upper bound is
\[
\boxed{w_{\mathrm{sat}}(n)
=\frac{\sin(2\pi/n)}{\cos((2\pi/n)\delta_n)},\qquad
\delta_n=\operatorname{dist}\!\left(\frac n4,\,2\mathbb Z+1\right).}
\]
At conductance \(w\ge w_{\mathrm{sat}}(n)\), **every** globally optimal shortcut is a centered pair \((i,n-1-i)\) satisfying the displayed sine inequality, and the globally optimal spectral gap is exactly \(\Lambda_n\). When \(w<w_{\mathrm{sat}}(n)\), no placement attains \(\Lambda_n\); the globally optimal locations in this lower-conductance regime are not classified here.

In particular, when the new link also has unit conductance, the complete set of optimal edges is
\[
\boxed{\big\{\{i,n-1-i\}:0\le i<\lfloor n/4\rfloor\big\};}
\]
there are exactly \(\lfloor n/4\rfloor\) such edges. Moreover,
\[
w_{\mathrm{sat}}(n)=\frac{2\pi}{n}+O(n^{-3})\qquad(n\to\infty).
\]

## Assumptions and scope

The original path is connected, finite, undirected, and has equal unit edge conductances. Its new edge must connect two **nonadjacent** distinct path vertices and has nonnegative incremental Laplacian \(w(e_i-e_j)(e_i-e_j)^{\mathsf T}\) for \(w>0\). The objective is the usual, unnormalized combinatorial-Laplacian algebraic connectivity; no degree normalization, reweighting of original path edges, or multiple shortcuts is allowed. The classification holds for every integer \(n\ge4\), all admissible endpoints, and all positive real \(w\). The universal upper bound is the path's third-smallest Laplacian eigenvalue, not its original spectral gap.

## Proof

**1. Rank-one ceiling and necessity of reflection symmetry.** Number the path eigenpairs from zero:
\[
\lambda_k=2-2\cos\!\left(\frac{k\pi}{n}\right),\qquad
u_k(t)=\begin{cases}n^{-1/2},&k=0,\\[2pt]\sqrt{2/n}\cos((t+1/2)k\pi/n),&1\le k<n,\end{cases}
\]
for \(0\le t<n\). Thus \(\lambda_2=\Lambda_n\). With \(b=e_i-e_j\), positive rank-one interlacing gives \(\alpha_n(i,j;w)\le\lambda_2\).

If \(b^{\mathsf T}u_2\ne0\), set \(z=(b^{\mathsf T}u_2)u_1-(b^{\mathsf T}u_1)u_2\). Then \(z\perp\mathbf1\) and \(b^{\mathsf T}z=0\). Its Rayleigh quotient for the augmented Laplacian is strictly less than \(\lambda_2\), because its \(u_1\) coefficient is nonzero and \(\lambda_1<\lambda_2\). Consequently equality forces \(b^{\mathsf T}u_2=0\). The arguments \((t+1/2)2\pi/n\) lie strictly between \(0\) and \(2\pi\), so equality of their cosines for two distinct endpoints occurs exactly when their sum is \(2\pi\). This is precisely \(i+j=n-1\).

**2. Reduction to one shifted antisymmetric inverse.** Fix a centered shortcut \(j=n-1-i\), with \(j-i\ge2\). The path and augmented Laplacian commute with reversal \(t\mapsto n-1-t\). The symmetric sector contains the constant and the path eigenvectors of even mode number; its least positive eigenvalue remains \(\lambda_2=\Lambda_n\), because \(b\) is antisymmetric. On the antisymmetric sector the path eigenvectors have odd mode numbers. Let
\[
A=(L(P_n)-\Lambda_n I)\big|_{\mathrm{antisymmetric}}.
\]
It is nonsingular and has exactly one negative eigenvalue (the mode \(k=1\)); all remaining eigenvalues are positive. The perturbed antisymmetric eigenvalues are at least \(\Lambda_n\) exactly when \(A+wbb^{\mathsf T}\) is positive semidefinite. Here \(b\) belongs to the antisymmetric sector.

For any invertible symmetric \(A\) with exactly one negative eigenvalue and any vector \(b\), write \(g=b^{\mathsf T}A^{-1}b\). Schur-complement inertia, applied to
\[
\begin{pmatrix}A&b\\b^{\mathsf T}&-1/w\end{pmatrix},
\]
shows that \(A+wbb^{\mathsf T}\succeq0\) if and only if \(-1/w-g\ge0\), equivalently \(1+wg\le0\). (Indeed, taking the Schur complement of the upper-left block gives \(-1/w-g\), while taking that of the negative lower-right scalar gives \(A+wbb^{\mathsf T}\); the two inertia counts agree.) The criterion includes equality, when the antisymmetric block acquires a zero eigenvalue.

**3. Exact inverse computation.** Put \(\phi=(i+1/2)\theta\) and \(A_0=-\sin\phi/\sin\theta\). The antisymmetric solution of \((L(P_n)-\Lambda_n I)y=b\) is obtained, for \(0\le t\le(n-1)/2\), from the piecewise formula
\[
y_t=\begin{cases}
A_0\cos((t+1/2)\theta),&0\le t\le i,\\
A_0\cot\phi\,\sin((t+1/2)\theta),&i<t\le(n-1)/2,
\end{cases}
\qquad y_{n-1-t}=-y_t.
\]
For odd \(n\), the central vertex is fixed by reversal and has \(y_t=0\); the sine expression also gives zero. The two pieces agree at \(t=i\), since \(\cot\phi\sin\phi=\cos\phi\). All homogeneous difference equations and endpoint Neumann conditions follow from \(2\cos\theta=2-\Lambda_n\). At \(t=i\), switching the right neighbor from the cosine continuation to the sine continuation changes the residual by
\[
-A_0\frac{\sin\theta}{\sin\phi}=1,
\]
while reflection gives residual \(-1\) at \(t=j\); elsewhere it is zero. Thus this is the required antisymmetric solution. Its inverse quadratic form is
\[
g=b^{\mathsf T}y=2y_i
=2A_0\cos\phi
=\boxed{-\frac{\sin((2i+1)\theta)}{\sin\theta}}.
\]
Since \(\sin\theta>0\) for \(n\ge4\), the inertia criterion is equivalent to the three displayed endpoint/conductance conditions in the theorem. This proves both their necessity and sufficiency.

**4. Minimax conductance and optimizer count.** In the centered family \(i\ge0\), \(j=n-1-i\), the possible indices \(r=2i+1\) are the positive odd integers with \(r\le n-2\) and the chord span \(j-i\ge2\). A positive sine requires \(r<n/2\). Since
\[
\sin(r\theta)=\cos((r-n/4)\theta),
\]
the largest admissible positive sine occurs at the odd integer closest to \(n/4\), producing the stated \(\delta_n\) formula. That nearest odd integer always has \(1\le r<n/2\) for \(n\ge4\). For \(w=1\), the inequality \(\sin(r\theta)\ge\sin\theta\), on \(0<r\theta<\pi\), is exactly \(1\le r\le n/2-1\). With \(r=2i+1\), this gives \(0\le i<\lfloor n/4\rfloor\). Finally \(0\le\delta_n\le1\); Taylor expansion of sine and cosine yields \(w_{\mathrm{sat}}(n)=2\pi/n+O(n^{-3})\).

## Verification

The standalone `verify.py` constructs the path Laplacian and checks the claimed complete unit-cost optimizer set for every \(4\le n\le33\) and every eligible edge, spectral saturation at and below predicted finite conductance thresholds, and the exact shifted-resolvent identity through \(n=54\). Invoke `python verify.py` with NumPy installed. The output is `VERIFY_OK 6611 numerical eigenvalue, threshold and shifted-resolvent checks`. These finite floating-point checks are illustrative; the proof above is analytical for all orders and all positive real conductances.

## Relationship to prior work

Ghosh and Boyd [1] study algebraic-connectivity improvement by adding edges and develop a greedy Fiedler-vector heuristic and rank-one secular bounds; their full conference paper was inspected. It establishes the general augmentation framework, not this explicit all-order **conductance saturation and endpoint equality classification** for unit paths. Fallat, Kirkland and Pati [2] study the maximum algebraic connectivity among unicyclic graphs with specified girth; their publisher abstract and a detailed secondary discussion in [3] were examined, but the complete [2] text was unavailable. Their optimization varies graph structure without the constraint that it be a one-shortcut augmentation of a fixed unit path and does not visibly parameterize the added edge's positive conductance. Nevertheless an indirect specialized implication cannot be excluded from the inaccessible paper. Shiu, Guo and Li [3] determine **minimum** algebraic connectivity in caterpillar unicyclic graph classes and cite the fixed-girth maximization results. Those objectives and graph families differ from the present exact spectral-cap saturation theorem.

## Limitations

The theorem does not characterize globally best shortcut locations when \(w<w_{\mathrm{sat}}(n)\), nor arbitrary base-edge weights, directed links, or multiple shortcuts. The general rank-one spectral ceiling and classical path spectrum are known; the assessed result is the exact equality and minimum-conductance classification. Complete original text of [2] was inaccessible, creating a residual possibility of unrecognized stronger or equivalent historical coverage. Numerical replay does not constitute independent mathematical validation.

## References

[1] A. Ghosh and S. Boyd, *Growing Well-connected Graphs*, Proceedings of the 45th IEEE Conference on Decision and Control, pp. 6605–6611 (December 2006), DOI 10.1109/CDC.2006.377282. Full text: https://stanford.edu/~boyd/papers/pdf/growing_fast_graphs.pdf . Conference public session FrIP13.1, Friday 15 December 2006.

[2] S. M. Fallat, S. Kirkland, and S. Pati, *Maximizing Algebraic Connectivity Over Unicyclic Graphs*, Linear and Multilinear Algebra 51 (2003), 221–241, DOI 10.1080/0308108031000069182. Publisher abstract: https://www.tandfonline.com/doi/abs/10.1080/0308108031000069182 .

[3] W. C. Shiu, J.-M. Guo, and J. Li, *The Minimum Algebraic Connectivity of Caterpillar Unicyclic Graphs*, Electronic Journal of Linear Algebra 22 (August 2011), 838–848. Full text: https://journals.uwyo.edu/index.php/ela/article/download/957/957/957 .
