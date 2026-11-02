# Sharp coordinatewise sensitivity of four-point Euclidean metric repair

## Finding
For each integer \(n\ge2\), let \(\mathcal M_n\) be the cone of symmetric, zero-diagonal nonnegative dissimilarities satisfying all triangle inequalities on \(n\) labeled points. Let \(Q_n:\mathbb R^{\binom n2}\to\mathcal M_n\) be Euclidean nearest-point projection in undirected-edge coordinates; *only the perturbation/output ratio* is measured in the coordinate maximum norm. Define
\[
L_n=\sup_{u\ne v}\frac{\|Q_n(u)-Q_n(v)\|_\infty}{\|u-v\|_\infty}.
\]
Then the exact sharp constants are
\[
\boxed{L_2=1,\qquad L_3=\frac43,\qquad L_4=\frac85,\qquad L_n\ge\frac85\quad(n\ge4).}
\]
Both finite sharp constants are attained by pairs of distinct **strictly positive** input dissimilarity arrays. For all larger sizes, a four-point witness embeds without changing its Lipschitz quotient. No equality assertion is made for \(n\ge5\).

## Assumptions and scope
Coordinates are indexed by unordered pairs of distinct labeled vertices. For \(n\ge3\), nonnegativity follows already from the three oriented triangle inequalities on any triple; the explicit nonnegativity convention ensures \(\mathcal M_2=[0,\infty)\). The range includes pseudometrics with zero distances between distinct vertices, so \(\mathcal M_n\) is closed and Euclidean projection is uniquely defined. Inputs can be arbitrary real edge vectors, although the sharp witnesses below are strictly positive. These are unweighted Euclidean least-squares repairs, **not** minimizers of an \(\ell_\infty\) nearness objective.

## Proof
**Polyhedral projection reduction.** Write \(\mathcal M_4=\{d:Ad\ge0\}\). In the edge order \((01,02,03,12,13,23)\), \(A\) has the \(12\) rows obtained by choosing each triple and each one of its three possible long sides: a row is \(-e_{ij}+e_{ik}+e_{jk}\). On each full-dimensional affine-linearity cell of Euclidean projection onto a polyhedral cone, its derivative is the orthogonal projector onto the kernel of some active-row submatrix \(B\):
\[
H_B=I-B^{\mathsf T}(BB^{\mathsf T})^\dagger B.
\]
The same statement follows directly from the Karush–Kuhn–Tucker conditions on any cell of fixed linearly independent binding constraints. Taking the maximum induced \(\ell_\infty\) matrix norm over **all** row subsets is therefore an upper bound, whether or not a particular subset is realizable. A segment between inputs meets finitely many projection cells, so integrating the piecewise-linear derivatives makes this a global upper bound. The code below never assumes every subset is realizable.

**Exhaustive exact upper bound.** For \(n=4\), the attached Python verifier enumerates all \(2^{12}=4096\) subsets, uses rational reduced row-echelon form to identify \(466\) distinct row spaces, inverts their exact rational Gram matrices, and computes every row absolute sum. The maximum at each row-space rank is:

| Rank of binding row space | 0 | 1 | 2 | 3 | 4 | 5 | 6 |
|---|---:|---:|---:|---:|---:|---:|---:|
| Maximum absolute row sum | \(1\) | \(4/3\) | \(3/2\) | \(8/5\) | \(3/2\) | \(10/7\) | \(0\) |
| Number of subsets | 1 | 12 | 66 | 238 | 639 | 1345 | 1795 |

These cardinalities total \(4096\). This is a **finite exhaustive proof certificate**, not sampling or a conjectured infinite conclusion. For \(n=3\), the three oriented triangle inequalities give eight subsets; the exact analogous calculation has maximum \(4/3\). For \(n=2\), projection is scalar clipping to the positive half-line, of norm one.

**Four-point sharpness in strictly positive data.** Let \(B\) contain rows numbered \(3,8,11\) of \(A\), numbered from zero in triple-lexicographic order and then long-side pair-lexicographic order:
\[
B=\begin{pmatrix}-1&0&1&0&1&0\\0&1&1&0&0&-1\\0&0&0&1&1&-1\end{pmatrix}.
\]
Set \(m=(2,2,1,2,1,3)/11\). The three selected inequalities are equalities at \(m\); the other nine are strict. Put \(\eta=1/100\), \(\varepsilon=1/10000\), \(v=(1,-1,1,-1,1,1)\), and \(z=m-\eta B^{\mathsf T}(1,1,1)^{\mathsf T}\). All entries of \(z\) and \(z+\varepsilon v\) are strictly positive. Direct rational computation gives
\[
H_Bv=(8,-3,4,-3,4,1)/5.
\]
Both \(m\) and \(m+\varepsilon H_Bv\) satisfy all metric inequalities, with precisely the selected three binding. The normal multipliers for the latter are
\[
(497/50000,\;251/25000,\;251/25000),
\]
which are strictly positive. Thus the projection optimality conditions give
\[
Q_4(z)=m,\qquad Q_4(z+\varepsilon v)=m+\varepsilon H_Bv.
\]
As \(\|v\|_\infty=1\) and \(\|H_Bv\|_\infty=8/5\), the upper bound is attained.

**Three-point sharpness.** In edge order \((01,02,12)\), take \(m=(2,1,1)\), the outward constraint normal \(b=(-1,1,1)\), \(z=m-b/100\), and \(v=(1,1,1)\). For \(\varepsilon=1/10000\), the sole binding-constraint projector is \(I-bb^{\mathsf T}/3\) and sends \(v\) to \((4,2,2)/3\). Its multiplier remains positive, and the other two triangle constraints remain strict. This gives an actual positive-input ratio \(4/3\).

**All larger sizes.** Embed either four-point witness in \(n\ge5\) labeled points. Assign every edge incident to a new point length \(1\) in both inputs, leaving the six original coordinates unchanged. The candidate projected outputs embed \(m\) and \(m+\varepsilon H_Bv\) and take all new-incident edges equal to \(1\). Every triangle involving a new vertex is strict: original distances are positive and below \(2\), and a triangle with all equal new-incident lengths is strictly feasible. The four-point normal certificates extend by zeros. Therefore these candidates are precisely the Euclidean projections in \(n\) points, with unchanged input and output maximum-norm differences. Hence \(L_n\ge8/5\) for all \(n\ge4\).

## Verification
Run `python3 verify_metric_cone.py` using only the standard library. It enumerates all \(4096\) four-point active-row subsets, checks each rational projector norm and the rank table, independently enumerates the eight three-point subsets, and verifies both primal/dual rational certificates. The analytic polyhedral-cell reduction proves the global bound; the finite enumeration is complete for the relevant finite-dimensional objects. The larger-point embedding is proved algebraically rather than by computation.

## Relationship to prior work
Metric nearness and its Euclidean projection formulation appear in the earlier work of Dhillon, Sra and Tropp (2004), and Brickell, Dhillon, Sra and Tropp (2008). The latter's quadratic programming formulation uses the same triangle cone, but an \(\ell_\infty\) nearness **objective** there is different from the \(\ell_\infty\) *sensitivity of the Euclidean solution map* here. Their inspected theorems and algorithms do not give the exact \(4/3\) and \(8/5\) operator moduli. Tang, Jiang and Wang (2022) discuss generalized Jacobians of proximal and projection maps within a numerical solver; the inspected statements do not evaluate this particular sharp cross-norm Lipschitz constant. General projection calculus supplies the reduction to face projectors but does not by itself supply the sharp face enumeration and equality certificate.

## Limitations
Only the constants for two, three, and four points are exact; larger-point estimates are lower bounds and need not be optimal. Distinct inputs attaining sharpness are explicitly given for the small cases, but an exhaustive classification of all equality faces is not asserted. The proof is specific to unweighted Euclidean repair of real complete-graph distance arrays and to the coordinate maximum norm; it does not address independently weighted least squares or approximate algorithms. Specialist earlier finite-metric perturbation calculations might give an equivalent result that was not recovered in the inspected sources. A July 2003 technical-report precursor is known at month precision, but its exact public release day was not verified; the metadata date records the earliest *day-verified* primary source used in this comparison.

## References
- I. S. Dhillon, S. Sra, J. A. Tropp, *Triangle Fixing Algorithms for the Metric Nearness Problem*, Advances in Neural Information Processing Systems 17 (2004), https://papers.nips.cc/paper_files/paper/2004/hash/4ebccfb3e317c7789f04f7a558df4537-Abstract.html .
- J. Brickell, I. S. Dhillon, S. Sra, J. A. Tropp, *The Metric Nearness Problem*, SIAM Journal on Matrix Analysis and Applications 30(1) (2008), pp. 375–396; electronically published 2008-04-23, https://doi.org/10.1137/060653391 .
- P. Tang, B. Jiang, C. Wang, *An Efficient Algorithm for the \(\ell_p\)-Norm-Based Metric Nearness Problem*, arXiv:2211.01245 (2022), https://arxiv.org/abs/2211.01245 .
- I. S. Dhillon, S. Sra, J. A. Tropp, *The Metric Nearness Problem with Applications*, UTCS Technical Report TR-03-23 (July 2003; day not verified), as listed on the first author's publications page.
