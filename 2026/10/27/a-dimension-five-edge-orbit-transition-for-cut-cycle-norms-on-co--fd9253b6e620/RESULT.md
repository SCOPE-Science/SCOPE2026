# A dimension-five edge-orbit transition for cut–cycle norms on coned hypercubes

## Finding
Let \(G_n=K_1\vee Q_n\) be the simple unweighted graph obtained by adjoining one universal apex to the binary \(n\)-cube, where \(n\ge2\). Let \(Q\) be the Euclidean-orthogonal projection of its real edge space onto its cut space, and let \(P=I-Q\) be the complementary orthogonal cycle projection. Define
\[
 a_n=2^{-n}\sum_{j=0}^n\binom nj\frac1{2j+1}.
\]
The exact real induced endpoint norms, equal for \(\ell_1\) and \(\ell_\infty\), are
\[
 \boxed{\|Q\|=\frac{6n+14}{15}},\qquad
 \boxed{\|P\|=\begin{cases}
 2+\frac n3-2a_n,&2\le n\le4,\\[2mm]
 \frac{6n+29}{15}-\frac4n(1-a_n),&n\ge5.
 \end{cases}}
\]
The cut norm always occurs on a cube edge, whereas the cycle norm occurs on an apex spoke for dimensions \(2,3,4\) and on a cube edge for every dimension \(n\ge5\); all the indicated inequalities between the two edge orbits are strict.

Compared with the ordinary \(n\)-cube cut projection \(Q^{\rm cube}_n\), whose norm is \((n+1)/2\), coning produces the exact sign reversal
\[
 \boxed{\|Q\|-\|Q^{\rm cube}_n\|=\frac{13-3n}{30}.}
\]
Thus adding all apex spokes **increases** the cut-projection endpoint norm precisely for \(2\le n\le4\), and **decreases** it for all \(n\ge5\). The mean absolute cut-projection column sum is exactly
\[
 \frac{1}{|E(G_n)|}\sum_{e\in E(G_n)}\sum_{f\in E(G_n)}|Q_{fe}|
 =\frac25\left(n+2+\frac1{n+2}\right).
\]
In particular the norms of both projections and the mean current length have linear growth in \(n\), equivalent to logarithmic growth in the number \(2^n+1\) of vertices.

## Assumptions and scope
The cube has vertex set \(\{0,1\}^n\), adjacent words differing in one coordinate, and one additional apex adjacent to every word. Every edge has unit conductance and is given an arbitrary reference orientation. Let \(D\) be the vertex–edge incidence matrix and \(L=DD^{\mathsf T}\) the graph Laplacian. The cut and cycle projectors are
\[
 Q=D^{\mathsf T}L^+D,\qquad P=I-Q,
\]
where \(L^+\) is the Moore–Penrose inverse. Their matrix entries are independent of orientations up to signed row and column changes; hence their absolute column sums do not depend on those choices. Both projectors are real symmetric, so their induced \(\ell_1\) and \(\ell_\infty\) norms coincide. There are exactly two edge orbits: apex spokes and original cube edges.

## Proof
**1. Grounded Laplacian and radial resolvent.** Ground the apex at potential zero. On the cube vertices the full graph Laplacian becomes \(I+L_{Q_n}\). Put \(R=(I+L_{Q_n})^{-1}\), and write \(r_j=R_{xy}\) whenever the Hamming distance from \(x\) to \(y\) is \(j\), \(0\le j\le n\). Since \(R=\int_0^\infty e^{-t}e^{-tL_{Q_n}}\,dt\), the tensor-product heat kernel gives
\[
 r_j=2^{-n}\int_0^\infty e^{-t}(1+e^{-2t})^{n-j}(1-e^{-2t})^j\,dt.
\]
For \(0\le j<n\), set \(h_j=r_j-r_{j+1}\). Subtraction yields
\[
 h_j=2^{1-n}\int_0^\infty e^{-3t}(1+e^{-2t})^{n-j-1}(1-e^{-2t})^j\,dt>0.
\]
For \(0\le j<n-1\), similarly
\[
 h_j-h_{j+1}=2^{2-n}\int_0^\infty e^{-5t}(1+e^{-2t})^{n-j-2}(1-e^{-2t})^j\,dt>0.
\]
Consequently the radial potentials are strictly decreasing, and their successive differences are strictly decreasing. Two exact binomial sums, justified by integrating the binomial theorem, are
\[
 S_n=\sum_{j=0}^{n-1}\binom{n-1}{j}h_j=\int_0^\infty e^{-3t}\,dt=\frac13,
\]
\[
 T_n=\sum_{j=0}^{n-2}\binom{n-2}{j}(h_j-h_{j+1})=\int_0^\infty e^{-5t}\,dt=\frac15.
\]
The diagonal resolvent has the separate Walsh expression
\[
 r_0=2^{-n}\sum_{j=0}^{n}\binom nj\frac1{2j+1}=a_n.
\]
At a cube vertex, \((I+L_{Q_n})R\delta_0=\delta_0\) implies \((n+1)r_0-nr_1=1\); hence
\[
 h_0=\frac{1-a_n}{n},\qquad a_n>\frac1{n+1}.
\]

**2. Spoke current.** Inject one unit at cube vertex \(0\) and extract at the apex. Grounding the apex gives cube potential \(f(x)=r_{|x|}\). Its apex currents total \(\sum_x f(x)=1\), since \(\sum_x (I+L_{Q_n})f(x)=\sum_x\delta_0(x)\). Radial strict monotonicity gives cube-edge absolute-current sum
\[
 \sum_{j=0}^{n-1}\binom nj(n-j)h_j=nS_n=\frac n3.
\]
The absolute column sum and the diagonal entry on a spoke therefore are
\[
 q_{\mathrm{sp}}=1+\frac n3,\qquad d_{\mathrm{sp}}=a_n.
\]

**3. Cube-edge current.** Take source \(0\) and sink \(e_1\), the first-coordinate neighbor. Grounding the apex gives \(f(x)=r_{|x|}-r_{|x\oplus e_1|}\). With \(j\) ones among the remaining \(n-1\) coordinates, this equals \(+h_j\) on the side whose first bit is zero and \(-h_j\) on the other. The strict inequalities in step 1 determine every current sign. The spoke-current absolute sum is \(2S_n=2/3\), and the cube edges parallel to the first coordinate contribute another \(2S_n=2/3\). The other cube edges contribute
\[
 2(n-1)\sum_{j=0}^{n-2}\binom{n-2}{j}(h_j-h_{j+1})=\frac{2(n-1)}5.
\]
Thus the cube-edge cut-column sum and diagonal are
\[
 q_{\mathrm{cu}}=\frac43+\frac{2(n-1)}5=\frac{6n+14}{15},
 \qquad d_{\mathrm{cu}}=2h_0=\frac{2(1-a_n)}n.
\]
The source has zero total cube charge, so its cube potentials sum to zero and automatically satisfy the apex Kirchhoff law. Both source constructions are therefore solutions on the full graph, not only on the grounded subsystem.

**4. Complementary columns and sharp phase.** For any real orthogonal projection matrix \(Q\), its diagonal entries are nonnegative and the corresponding column of \(P=I-Q\) has absolute sum \(1+q_e-2Q_{ee}\). Hence
\[
 p_{\mathrm{sp}}=2+\frac n3-2a_n,\qquad
 p_{\mathrm{cu}}=\frac{6n+29}{15}-\frac4n(1-a_n).
\]
The cut-column difference \(q_{\mathrm{cu}}-q_{\mathrm{sp}}=(n-1)/15>0\) for every \(n\ge2\). The cycle-column difference is
\[
 p_{\mathrm{cu}}-p_{\mathrm{sp}}
 =\frac{n-1}{15}-\frac4n+\left(2+\frac4n\right)a_n.
\]
For \(n=2,3,4\) this difference equals respectively \(-1/15,-2/35,-1/105\), whereas for \(n=5\) it is \(28/495>0\). For every \(n\ge6\), the strict bound \(a_n>1/(n+1)\) gives
\[
 p_{\mathrm{cu}}-p_{\mathrm{sp}}>
 \frac{n-1}{15}-\frac2{n+1}>0,
\]
where the final inequality uses \(n^2-1>30\). Edge-orbit symmetry completes the exact norm formulas and the strict phase classification.

**5. Comparison and mean.** The ordinary cube norm \((n+1)/2\) is Theorem 45 of Dilworth–Kutzarova–Ostrovskii (2023), which yields the displayed difference upon subtraction. The coned cube has \(n2^{n-1}\) ordinary cube edges and \(2^n\) spokes. Averaging \(q_{\mathrm{cu}}\) and \(q_{\mathrm{sp}}\) in these proportions gives
\[
 \frac{nq_{\mathrm{cu}}+2q_{\mathrm{sp}}}{n+2}
 =\frac25\left(n+2+\frac1{n+2}\right).
\]
Since \(a_n=2^{-n}\int_0^1(1+t^2)^n\,dt\) and \((1+t^2)/2\le\exp[-(1-t)/2]\) for \(0\le t\le1\), we have \(0<a_n\le2/n\). The exact formulas therefore also imply
\[
 \|Q\|=\frac25n+\frac{14}{15},\qquad
 \|P\|=\frac25n+\frac{29}{15}-\frac4n+O(n^{-2}).
\]

## Verification
Run `python coned_cube_exact_checker.py` with Python 3 and SymPy. The independent grounded-Laplacian calculations solve exact rational linear systems for representatives of both edge orbits in dimensions \(2\) through \(6\). Separately, exact Walsh-resolvent and absolute-current combinatorial identities are checked in dimensions \(1\) through \(30\), including the strict orbital comparisons. All finite checks passed. The infinite-dimensional assertions follow from the integral identities and inequalities in the proof rather than from finite enumeration.

## Relationship to prior work
Dilworth, Kutzarova and Ostrovskii (arXiv:2305.12582v1, 21 May 2023, Theorem 45, Section 2.7) calculate the cut-projection endpoint norm of the **ordinary** Hamming cube. The present graph is its join with a universal apex, with two inequivalent edge orbits; the ordinary-cube result does not imply either coned-cube column sum or the dimension-five switch. Schild, Rao and Srivastava (arXiv:1708.01632v1, 4 August 2017, Theorems 1.4–1.5) establish general electrical-flow localization bounds, and Gurel-Gurevich, Nachmias and Sachdeva (arXiv:2605.24130v1, 22 May 2026, Theorems 1.1–1.3) sharpen the universal logarithmic-order bounds. Neither general theorem computes these exact two edge-orbit norms or identifies the phase transition. The coned family also supplies a concrete exact logarithmic-order average electrical-current length. Search comparisons have not established exhaustive bibliographic uniqueness; independently indexed or earlier equivalent formulas may exist.

## Limitations
The result addresses only unweighted graph cones over binary Hamming cubes, canonical Euclidean-orthogonal cut and cycle projections, and real induced endpoint operator norms. It does not assert minimum norm among nonorthogonal projections, cover weighted spoke/cube conductances, or determine intermediate \(\ell_p\) operator norms. The finite computational checks support but do not certify the all-dimensional proof. No independent mathematical validation has been performed.

## References
- S. J. Dilworth, D. Kutzarova and M. I. Ostrovskii, *Cycle spaces: invariant projections and applications to transportation cost*, arXiv:2305.12582v1 (first public release 21 May 2023), especially Theorem 45 and Section 2.7.
- A. Schild, S. Rao and N. Srivastava, *Localization of Electrical Flows*, arXiv:1708.01632v1 (first public release 4 August 2017), Theorems 1.4–1.5.
- O. Gurel-Gurevich, A. Nachmias and S. Sachdeva, *A Tight Bound on Localization of Electrical Flows*, arXiv:2605.24130v1 (first public release 22 May 2026), Theorems 1.1–1.3.
