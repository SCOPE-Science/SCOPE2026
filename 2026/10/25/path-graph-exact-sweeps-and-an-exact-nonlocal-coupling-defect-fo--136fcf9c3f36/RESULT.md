# Path-graph exact sweeps and an exact nonlocal-coupling defect for coordinate RCGLS

## Finding
For a full-column-rank least-squares design, a prescribed full permutation of singleton coordinate sketches in the exact-arithmetic RCGLS recurrence of Zeng, Cai, Han and Xie (2026) has an exact finite-pass criterion: **generic exact completion in one full sweep holds precisely for tridiagonal normal matrices in sketch order**. Thus an order with generic exact completion exists precisely when the sparsity graph of the normal matrix is a disjoint union of paths. This characterizes when orthogonalization against only the immediately preceding search direction is as effective as full conjugation of the entire coordinate basis.

In dimension three the exact remaining-energy factor of the last update is additionally computable from a single off-band entry. Put
\[
H=\begin{pmatrix}a&b&c\\b&d&e\\c&e&f\end{pmatrix}\succ0,\quad
D=d-\frac{b^2}{a},\quad W=f-\frac{(e-bc/a)^2}{D}.
\]
For any start whose second-step error is nonzero and whose three sketched coefficients are nonzero, the third update obeys
\[
\boxed{\frac{\|x^*-x^{(3)}\|_H}{\|x^*-x^{(2)}\|_H}=
\frac{|c|}{\sqrt{aW}}.}
\]
Since \(aW-c^2>0\), this is strictly less than one. It is zero exactly when \(c=0\). Unlike a mere upper bound, the factor is an **equality for every admitted initial error**.

## Assumptions and scope
Let \(A\in\mathbb R^{m\times d}\), \(m\ge d\ge2\), have full column rank. The normal matrix is \(H=A^\top A\succ0\), and \(x^*\) is the unique least-squares minimizer for a fixed datum \(b\). Permute coordinates once and thereafter use this coordinate order. At update \(j\) choose the singleton sketch \(S_j=e_j/\sqrt{H_{jj}}\); the original RCGLS iteration uses the sketched negative gradient, exact line search, and orthogonalization only against the last search direction. No restarting or reordering occurs during the sweep. Calculations are over exact real arithmetic.

Let \(e^{(j)}=x^*-x^{(j)}\). We call a start **generic for this sweep** if the sketched gradient at each of the \(d\) prescribed stages is nonzero and no earlier stage has already reached \(x^*\). These conditions exclude finitely many proper linear subspaces of the initial error space; the complement is open dense. Special starts that solve early are not failures, but zero sketched coefficients require a separate branch and are not included in the finite-pass equivalence.

All statements describe a deterministic prescribed order, equivalently a conditional event under an IID coordinate sampler that assigns each selected coordinate positive probability. They make no claim that an IID sampler will complete in one arbitrary sweep.

## Proof
**1. Direction recurrence.** Write \(\langle u,v\rangle_H=u^\top Hv\) and \(\|v\|_H^2=\langle v,v\rangle_H\). On a nonzero-sketch branch the direction produced at stage \(j\) is a nonzero scalar multiple of \(w_j\), where
\[
w_1=e_1,\qquad
w_j=e_j-\frac{\langle e_j,w_{j-1}\rangle_H}{\|w_{j-1}\|_H^2}w_{j-1},\quad 2\le j\le d.
\]
Indeed Algorithm 1 takes the raw direction \(S_jS_j^\top A^\top(b-Ax^{(j-1)})\), a scalar multiple of \(e_j\), and subtracts its \(H\)-projection onto the immediately preceding direction. Scalar normalization of the sketch therefore does not affect the line-search trajectory. Every \(w_j\) has coefficient one at coordinate \(j\) and support in coordinates \(1,\ldots,j\). Hence the \(w_j\) are a basis, with \(\langle w_j,w_{j-1}\rangle_H=0\) for \(j\ge2\).

Let \(Q_jz=z-w_j\langle w_j,z\rangle_H/\|w_j\|_H^2\) be the \(H\)-orthogonal projection onto the complement of \(w_j\). The exact error after the full sweep is \(Q_d\cdots Q_1e^{(0)}\).

**2. When a whole sweep vanishes.** A product of \(d\) codimension-one orthogonal projections on a \(d\)-dimensional inner-product space is the zero map if and only if their discarded one-dimensional directions are pairwise orthogonal. For necessity, the rank begins at \(d\) and can fall by at most one at each projection. A zero final map forces one rank drop at every stage. The second projection can decrease the rank of the first projection's range only when its kernel direction lies inside that range, giving orthogonality of the first two directions. Inductively, if the first \(j-1\) directions are orthogonal, the range equals their common orthogonal complement, and rank drops at step \(j\) only if \(w_j\) is orthogonal to all its predecessors. Sufficiency follows because the mutually orthogonal directions form a basis.

This full conjugacy condition holds precisely when \(H\) is tridiagonal in the chosen coordinates. If it holds, then for \(i\le j-2\),
\[
0=\langle w_j,w_i\rangle_H=\langle e_j,w_i\rangle_H,
\]
since \(w_{j-1}\) is already orthogonal to \(w_i\). The directions \(w_1,\ldots,w_{j-2}\) span \(\operatorname{span}\{e_1,\ldots,e_{j-2}}\), so \(H_{j,i}=0\) for every \(i\le j-2\). Conversely, if \(H\) is tridiagonal, \(e_j\) is \(H\)-orthogonal to the support of each \(w_i\) with \(i\le j-2\). The recurrence then preserves all earlier conjugacy by induction.

The scalar coefficient at stage \(j\) is a nonzero multiple of the linear functional \(e_j^\top H Q_{j-1}\cdots Q_1e^{(0)}\). This functional cannot vanish identically: by \(H\)-adjointness, identical vanishing would imply \(Q_1\cdots Q_{j-1}e_j=0\), but every projection \(Q_i\) with \(i<j\) only changes coordinates \(1,\ldots,i\), leaving coordinate \(j\) equal to one. Thus the nonzero-coefficient branch is open dense. If \(H\) is not tridiagonal, the full product is a nonzero linear map, whose kernel is a proper subspace. Intersecting its nonkernel with the generic branch yields an open dense family of starts having a nonzero final error.

A symmetric matrix is tridiagonal under some simultaneous row-column permutation exactly when its off-diagonal graph is a subgraph of a single path; this is equivalent to the graph being a vertex-disjoint union of paths. Concatenating component orders proves the converse.

**3. Three-coordinate exact ratio.** For the displayed \(3\times3\) matrix,
\[
w_1=e_1,\quad w_2=e_2-\frac{b}{a}e_1,\quad
w_3=e_3-\frac{e-bc/a}{D}w_2.
\]
Direct multiplication yields \(\|w_2\|_H^2=D\), \(\langle w_3,w_2\rangle_H=0\), \(\langle w_3,e_1\rangle_H=c\), and \(\|w_3\|_H^2=W\). After two exact line searches, the nonzero error is orthogonal to \(w_1,w_2\), so it is proportional to
\[
z=w_3-\frac{c}{a}e_1,
\qquad \|z\|_H^2=W-\frac{c^2}{a}>0.
\]
The last update is the \(H\)-orthogonal projection of this error off \(w_3\). Pythagoras gives the ratio squared as \(1-\|z\|_H^2/W=c^2/(aW)\). Positivity of the Gram determinant gives the strict bound below one.

**4. Order-sensitive sharp family.** For \(0<\rho<1\), let
\[
H_\rho=\begin{pmatrix}1&0&\rho\\0&1&0\\\rho&0&1\end{pmatrix}.
\]
Its eigenvalues are \(1-\rho,1,1+\rho\); therefore it is positive definite and can be realized as \(A^\top A\) by a Cholesky factor. In coordinate order \((1,2,3)\), the formula gives exactly \(R=\rho\), approaching one as \(\rho\uparrow1\). In order \((1,3,2)\), the permuted Gram matrix is tridiagonal, so a generic three-update sweep terminates exactly. For the rational choice \(\rho=9/10\) and initial error \((1,1,1)^\top\), the errors after two and three steps in order \((1,2,3)\) are respectively \((-9/10,0,1)^\top\) and \((-9/10,0,81/100)^\top\), giving exact ratio \(9/10\).

## Verification
The standalone `verification_checker.py` reproduces the projection identity and the three-mode formula. It checks symbolic expressions for \(D\) and \(W\); an exact rational witness; 2,000 SPD three-dimensional matrices with random initial errors, comparing the analytical factor against independent exact-line-search iteration; and 600 tridiagonal SPD examples in dimensions three, four, five and seven. Run with `python verification_checker.py` using Python 3, NumPy and SymPy. All checks succeeded. Finite sampling supports the proof but is not an infinite-domain certificate.

## Relationship to prior work
Zeng, Cai, Han and Xie introduce RCGLS via a one-step conjugacy projection, show expected linear convergence for independent sketches satisfying a positive-definite sampling assumption, and derive an efficient sparse implementation [1]. Their Algorithm 1 and its exact line-search formulas supply the update being specialized here; this result does not claim their recurrence as new. Classical conjugate-direction theory already establishes finite termination for any fully mutually conjugate basis [2, 3]. The additional statement proved here identifies exactly which *coordinate-sketch orders* make the source's local one-step correction fully conjugate, characterizes the allowable normal-matrix sparsity graphs, and computes an exact three-coordinate off-band deficit. The source's full text (algorithm, convergence sections, sparse implementation, examples, conclusion and references) was compared with these specific statements; no such graph classification or exact off-band ratio was located.

## Limitations
This is an exact-arithmetic, full-column-rank, deterministic-sweep statement conditional on generic nonzero sketched gradients, not a rate for IID trajectories or a claim of backward stability in floating point. Graph sparsity concerns \(A^\top A\), which may be denser than \(A\). Near \(\rho=1\), the explicit witness becomes ill-conditioned; this does not establish near-stagnation at uniformly bounded condition number. Special starts with zero sketched gradients may follow a different branch of Algorithm 1. Classical generic conjugate-direction results cover some underlying steps, and overlooked formulations of the precise sparse short-recurrence characterization remain a bibliographic risk.

## References
[1] Y. Zeng, J.-F. Cai, D. Han and J. Xie, *Randomized conjugate gradient least squares*, arXiv:2605.25034, first publicly available 2026-05-24. https://arxiv.org/abs/2605.25034

[2] *Conjugate Directions*, BMVA computer-vision tutorial, University of Edinburgh archive. https://homepages.inf.ed.ac.uk/rbf/CVonline/LOCAL_COPIES/BMVA96Tut/node20.html

[3] D. Drusvyatskiy, *Week 1: Convex Quadratics*, DSC 243 Advanced Optimization notes, section on the conjugate-gradient short recurrence. https://ddrusvyat.github.io/DSC-243/week1.html
