# Sharp nonorthogonal cut-space projection constants of complete split graphs

## Finding
For integers \(m,n\ge 2\), let \(G_{m,n}=K_m\vee\overline K_n\): its vertices form a clique \(A\) of size \(m\) and an independent set \(B\) of size \(n\), with every edge between the classes present. Give its edge space \(\mathbb R^{E(G_{m,n})}\) the usual coordinate \(\ell_1\) norm. Write \(\mathcal C_{m,n}\) for its cut (gradient) subspace and \(\lambda_1(\mathcal C_{m,n})\) for the infimum of \(\|P\|_{1\to1}\) over **all** linear projections \(P\) of the edge space onto that fixed subspace. Put \(N=m+n\) and
\[
D=m^2+4mn-3m+2n^2-4n+2.
\]
Then the exact projection constant is
\[
\boxed{\lambda_1(\mathcal C_{m,n})=\frac{2(N-1)(m^2+3mn-3m-2n+2)}{mD}.}
\]
The canonical Euclidean-orthogonal cut projection \(Q_0\), regarded as an operator on \(\ell_1(E)\), has norm
\[
\boxed{\|Q_0\|_{1\to1}=\frac{2m^2+3mn-3m-2n+2}{mN},}
\]
with exact excess
\[
\boxed{\|Q_0\|_{1\to1}-\lambda_1(\mathcal C_{m,n})
=\frac{(m-2)(m-1)(n-1)(m+2n-2)}{mND}.}
\]
Thus orthogonality is norm-optimal precisely for \(m=2\), and is strictly suboptimal for every \(m\ge3\). Along \(m=n\to\infty\), the orthogonal and minimum projection norms tend to \(5/2\) and \(16/7\), respectively: their gap tends to \(3/14\).

## Assumptions and scope
All graph edges are unweighted and unordered as graph edges, but oriented to specify coordinates: clique edges run from the smaller to the larger indexed vertex, and cross edges from \(A\) to \(B\). Reversing an edge orientation changes the sign of that coordinate and therefore does not affect any \(\ell_1\) operator norm. The cut space is the range of the transpose of the signed vertex-edge incidence matrix. Its dimension is \(N-1\). A projection means a real linear idempotent with image equal to this cut space; no symmetry or Euclidean self-adjointness is presumed. The parameter range is exactly all integers \(m,n\ge2\). For these parameters \(D>0\).

## Proof
**1. Reduction to one invariant parameter.** The finite automorphism group \(S_m\times S_n\) acts on edge space by signed coordinate permutations and hence by \(\ell_1\) isometries. It preserves the cut space. Averaging any cut projection under these isometries produces another cut projection with no greater operator norm, so a norm-minimizing invariant projection exists.

The oriented clique-edge module is the exterior square of the permutation representation on \(A\); it contains one copy of the mean-zero standard module \(U_m\) and an inequivalent residual module. The cross-edge module decomposes as \(\mathbf1\oplus U_m\oplus U_n\oplus(U_m\otimes U_n)\). Meanwhile the cut space is \(\mathbf1\oplus U_m\oplus U_n\). These are inequivalent real modules and the indicated constituent multiplicities hold at the small endpoints \(m=2\) and \(n=2\) as well. Consequently invariant edge-to-cut maps have four scalar parameters and the condition of being the identity on the cut space leaves exactly one free parameter. One may equivalently derive the four scalar parameters directly from the two edge orbits and their coordinate stabilizers, so no unproved assumption of uniqueness of the orthogonal projection is made.

For a mean-zero vector \(p\in\mathbb R^m\), define edge vectors \(W(p)\) and \(U(p)\) as follows: on a clique edge \((i,j)\), both have coordinate \(p_i-p_j\); on a cross edge \((i,u)\), their coordinates are respectively \(p_i\) and \(-mp_i/n\). The first vector is a gradient. The second is a circulation, because its signed incidence at each clique vertex is \(mp_i-n(mp_i/n)=0\) and at each independent vertex the sum of the \(p_i\) vanishes. They are orthogonal, and
\[
\|U(p)\|_2^2=\frac{mN}{n}\|p\|_2^2.
\]
With adjoints taken in the ordinary Euclidean inner product on edge coordinates, let
\[
Q_t=Q_0+\frac{tn}{mN}WU^*,\qquad t\in\mathbb R.
\]
The operator \(WU^*\) vanishes on the cut space and has range within it. Thus every \(Q_t\) is a projection onto cuts. The invariant-map dimension count above shows these exhaust all invariant projections.

**2. Exact column norms.** There are only two column orbits, clique edges and cross edges. Solving the graph Laplacian for one unit source on an edge gives the exact column-sum functions
\[
F(t)=\frac{2(N-1)}{mN}|m+nt|
\]
for each clique edge, and
\[
H(t)=\frac{(m-1)(m+2n-2)|1-t|+
 |N+m-1-(m-1)t|+(m-1)|N-1+t|}{mN}
\]
for each cross edge. For completeness, the Laplacian solution at a clique edge \((i,j)\) has clique potentials \((e_i-e_j)/N\) and zero independent-set potentials. At a cross edge \((i,u)\), one can take clique potentials \((e_i-\mathbf1/m)/N\), independent potential \(-1/m\) at \(u\), and zero at the other independent vertices. Applying signed differences to these potentials, and adding the displayed \(WU^*\) correction, gives exactly the two formulas.

On \(0\le t\le1\), the two remaining absolute values in \(H\) sum to \(mN\). Hence
\[
F(t)=\frac{2(N-1)(m+nt)}{mN},\qquad
H(t)=1+\frac{(m-1)(m+2n-2)(1-t)}{mN}.
\]
The former is strictly increasing and the latter is strictly decreasing. At \(t=0\), \(H(0)-F(0)=(m-2)(n-1)/(mN)\ge0\). At \(t=1\), \(H(1)=1<F(1)\). They therefore meet at the unique point
\[
\boxed{t_*=\frac{(m-2)(n-1)}{2n(N-1)+(m-1)(m+2n-2)}},\qquad 0\le t_*<1.
\]
For \(t<0\), the triangle inequality in the expression for \(H(t)\) yields \(H(t)\ge H(0)\), which is no better than \(t_*\). For \(t>1\), \(F(t)\ge F(1)\), likewise no better. Thus \(Q_{t_*}\) minimizes \(\max\{F(t),H(t)\}\) over every real \(t\), and by the averaging argument minimizes norm among **all**, not merely invariant, projections onto the cut space.

**3. Closed forms and sharp separation.** Substituting \(t_*\) into \(F(t_*)=H(t_*)\) and simplifying gives the formula for \(\lambda_1\). At \(t=0\), \(H(0)\) dominates \(F(0)\) and yields the stated orthogonal norm. Subtracting yields the displayed nonnegative rational gap. Its numerator vanishes for the allowed parameters exactly when \(m=2\), and is positive for \(m\ge3\). Dividing the three rational expressions by their highest powers of \(m\) when \(m=n\to\infty\) proves the asymptotic values.

## Verification
The included dependency-free `VERIFY.py` reconstructs the grounded Laplacian inverse with `fractions.Fraction`, forms the actual Euclidean cut projector and the stated rank-\((m-1)\) correction, and checks its idempotence, action on the whole cut space, exact \(\ell_1\) column norms, and closed-form identities for all \(16\) integer pairs \(2\le m,n\le5\), covering \(276\) columns. An optional `VERIFY_LP.py` independently minimizes the unrestricted projection norm using a linear program (SciPy required), checking five small pairs numerically. Execute `python VERIFY.py` from the extracted package; optionally execute `python VERIFY_LP.py`. The infinite two-parameter theorem follows from the proof, not the finite tests.

## Relationship to prior work
Dilworth, Kutzarova and Ostrovskii (2023) formulate graph cut/cycle projection questions in \(\ell_1\), including invariant-projection methods, and carry out explicit calculations for discrete tori and Hamming graphs. The theorem above applies that general methodology to a different edge representation, the complete split graph, and demonstrates that the orthogonal cut projection need not be minimal even under substantial vertex-permutation symmetry. Earlier calculations for balanced complete multipartite graphs concern equal independent vertex classes and give orthogonal minimal projections, so they do not imply the present strict nonorthogonality for \(K_m\vee\overline K_n\). At \(m=2\), the same graph is a triangular book; existing weighted triangular-book projection results concern its **cycle-flow** subspace rather than this cut projection constant. The genuinely new strict-gap range is \(m\ge3,n\ge2\). Ellipsoidal and nonlinear norm calculations on split graphs determine distinct invariants. Work on Laakso graph projection estimates likewise concerns a different graph family. The word *projection constant* here refers specifically to the minimal norm of a retraction of the **edge \(\ell_1\) space onto its cut subspace**, not projection constants of the transportation-cost quotient itself.

## Limitations
The result is about the cut space, not the best projection onto the complementary cycle space. It gives the minimum operator norm but does not classify every non-invariant minimizer. All edges have unit weight, and no formula is asserted for weighted, directed, or infinite split graphs. No claim is made that the result was independently audited. An equivalent calculation under other electrical-network or Banach-space terminology remains a possible bibliographic risk.

## References
1. S. J. Dilworth, D. Kutzarova, M. I. Ostrovskii, *Cycle spaces: invariant projections and applications to transportation cost*, arXiv:2305.12582, first posted May 21, 2023. https://arxiv.org/abs/2305.12582
2. S. J. Dilworth, D. Kutzarova, M. I. Ostrovskii, *Analysis on Laakso graphs with application to the structure of transportation cost spaces*, arXiv:2007.07949, first posted July 15, 2020. https://arxiv.org/abs/2007.07949
