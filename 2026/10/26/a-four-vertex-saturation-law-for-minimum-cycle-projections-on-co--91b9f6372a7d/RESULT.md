# A four-vertex saturation law for minimum cycle projections on complete split graphs

## Finding
For integers \(r\geq2\) and \(s\geq1\), let \(G_{r,s}=K_r\vee\overline{K_s}\) be the complete split graph: a clique \(A\) of \(r\) vertices joined to an independent set \(S\) of \(s\) vertices. Give every edge unit length and let \(Z_{r,s}=\ker\partial\) be its real cycle-flow subspace of \(\ell_1(E(G_{r,s}))\), where \(\partial\) is the oriented vertex-edge incidence matrix. Its **relative minimum projection norm**, minimized over all real-linear projections of the full edge space onto \(Z_{r,s}\), is
\[
\boxed{\lambda(Z_{r,s})=\begin{cases}
3-\dfrac6{r+s}+\dfrac{6s(r-4)(s-1)}{r(r+s)[6s+(r-1)(4-s)]},&1\leq s\leq3,\\[7pt]
\dfrac{3(r-1)}r,&s\geq4.
\end{cases}}
\]
Thus **four independent-side vertices suffice for saturation**: after \(s=4\), enlarging the independent part does not change the minimum projection norm. In contrast, the norm of the canonical Euclidean-orthogonal cycle projection generally does change with \(s\).

## Assumptions and scope
All graphs are finite, simple, connected, and unweighted. Orient clique edges \(i\to j\) for \(i<j\), and every clique-to-independent edge \(i\to b\). Put \(n=r+s\). The norm \(\|T\|_{1\to1}\) is the maximum absolute column sum of the actual edge-coordinate matrix. Projection means \(P^2=P\) with range exactly \(Z_{r,s}\); no permutation invariance is imposed on the projections being minimized. The case \(s=1\) is the known complete-graph boundary case, included to state the full family without claiming that boundary case as a separate discovery.

## Proof
**1. Symmetry reduces the unrestricted problem to one parameter.** The finite group \(\mathfrak S_r\times\mathfrak S_s\) acts on oriented edges by signed coordinate permutations, hence by \(\ell_1\) isometries, preserving the cycle space. Averaging conjugates of any projection onto this subspace gives an equivariant projection of no greater norm. The average remains a projection because its image is in the cycle space and every summand fixes that space pointwise.

Write \(W_r\) and \(W_s\) for the real sum-zero standard permutation modules, allowing \(W_s=0\) when \(s=1\). The oriented edge module is \(\bigwedge^2\mathbb R^r\oplus(\mathbb R^r\otimes\mathbb R^s)\), whereas the cut space is \(W_r\oplus W_s\oplus\mathbf1\). Splitting the permutation modules into trivial and standard parts and taking the kernel of the incidence map gives
\[
Z_{r,s}\cong W_r\oplus\bigwedge^2W_r\oplus(W_r\otimes W_s).
\]
The only common irreducible constituent of cut and cycle modules is a single copy of \(W_r\): \(\bigwedge^2W_r\) is inequivalent to \(W_r\) (or zero), and the tensor term is nontrivial on \(\mathfrak S_s\) when present. This remains true for the small permutation groups \(r=2,3\). Consequently the real intertwiner space from cuts to cycles is one-dimensional, so *every* equivariant cycle projection lies in the following family.

Let \(L=\partial\partial^{\mathsf T}\) and \(\phi=L^+\partial x\), where \(L^+\) is the Moore--Penrose inverse and \(\phi\) is the mean-zero vertex potential. On clique vertices put \(u_i=\phi_i-r^{-1}\sum_{a\in A}\phi_a\), and define an edge flow \(z(u)\) by
\[
z(u)_{ij}=u_i-u_j\quad(i,j\in A),\qquad z(u)_{ib}=-\frac rs u_i\quad(i\in A,b\in S).
\]
The divergences of these two components cancel at each clique vertex, and both sum to zero at every independent vertex; hence \(z(u)\in Z_{r,s}\). The operator
\[
P_t x=x-\partial^{\mathsf T}L^+\partial x+t z(u),\qquad t\in\mathbb R,
\]
fixes each cycle flow and has range in the cycle space, so it is a projection. Since the correction spans the equivariant intertwiners, these \(P_t\) exhaust the averaged candidates.

**2. Exact column sums.** On the mean-zero vertex subspace, the graph Laplacian acts as multiplication by \(n\) except on sum-zero potentials supported on \(S\), where it acts as multiplication by \(r\). In particular,
\[
L^+=\frac1n\left(I-\frac{\mathbf1\mathbf1^{\mathsf T}}n\right)
+\left(\frac1r-\frac1n\right)\Pi_S,
\]
where \(\Pi_S\) is the orthogonal projector onto sum-zero vectors supported in \(S\). Applying this identity to a clique-edge or a cross-edge incidence column and grouping the absolute values by edge orbit gives exactly
\[
F_A(t)=\left|1-\frac{2(1-t)}n\right|
+\frac{2(r-2)}n|1-t|+\frac{2s}n\left|1+\frac{rt}s\right|,
\]
\[
F_X(t)=\frac{r-1}n|1-t|
+\frac{2(r-1)}{rn}\left|n-1-\frac{rt}s\right|
+\frac{2(r-1)(s-1)}{rn}\left|1+\frac{rt}s\right|.
\]
Here \(F_A\) is the absolute column sum for any clique edge and \(F_X\) that for any cross edge. Therefore \(\|P_t\|_{1\to1}=\max\{F_A(t),F_X(t)\}\); this is an exact identity for all real \(t\), without a sign approximation.

**3. Global convex minimization.** Both \(F_A\) and \(F_X\) are convex piecewise-affine functions on \(\mathbb R\). On the interval \([-s/r,1]\), all their displayed linear terms have the indicated fixed signs (allowing boundary zeros). Thus
\[
F_A(t)=3-\frac6n+\frac{6t}n,
\qquad F_X(t)=\frac{(r-1)(3r+4s-4)}{rn}+\frac{(r-1)(s-4)t}{sn}.
\]
For \(1\leq s\leq3\), the first slope is positive and the second negative. The two lines meet at
\[
t_*=\frac{s(r-4)(s-1)}{r[6s+(r-1)(4-s)]},
\]
which lies in \([-s/r,1]\) for all allowed integers. Their maximum has a global minimum at the crossing, because the opposing affine slopes give a zero subgradient and the maximum is convex globally. Substitution yields the first branch of the stated formula.

For \(s\geq4\), the cross-edge function \(F_X\) alone has its global minimum at \(t_*=-s/r\): its slope to the left is \(-3(r-1)/n\), and its slope immediately to the right is \((r-1)(s-4)/(sn)\geq0\). Direct substitution gives
\[
F_X(-s/r)=\frac{3(r-1)}r,\qquad F_A(-s/r)=\frac{3(r-2)}r.
\]
Consequently \(\max\{F_A,F_X\}\) attains the lower bound supplied by \(F_X\), proving the second branch and the sharp saturation threshold.

**4. Canonical comparison.** The orthogonal cycle projection is \(P_0\), with
\[
\|P_0\|_{1\to1}=\max\left\{3-\frac6{r+s},\frac{(r-1)(3r+4s-4)}{r(r+s)}\right\}.
\]
For every \(r\geq2\) and \(s>4\), this strictly exceeds the minimum in the theorem. Moreover, with \(r\) fixed as \(s\to\infty\), the ratio of the canonical to the minimum norm tends to \(\max\{r/(r-1),4/3\}\): it is \(2\) for \(r=2\), \(3/2\) for \(r=3\), and \(4/3\) for \(r\geq4\).

## Verification
The accompanying standalone `verify_split.py` uses exact rational Gaussian elimination on grounded graph Laplacians and builds the claimed projections directly, independently of the orbit-sum formulas. It checks all \(56\) pairs \(2\leq r\leq8\), \(1\leq s\leq8\), including \(1932\) actual edge columns and \(1754\) full projection-idempotence entries on smaller cases. It also verifies each cycle-flow divergence and exact agreement with the closed formula. Run the included checker with `python3 verify_split.py` (Python standard library only).

## Relationship to prior work
Dilworth, Kutzarova, and Ostrovskii, *Cycle spaces: invariant projections and applications to transportation cost* (first arXiv submission 2023-05-21), establish the general graph-cycle projection framework, finite-group averaging methodology and detailed results for tori and Hamming graphs. Its table of contents and full-text search, together with inspection of the introduction, the general representation problem, the minimal-projection discussion and the Hamming-graph section, did not reveal a complete-split-graph two-parameter minimizer or four-vertex saturation theorem. The group-averaging step here is a use of an existing method; the split-graph representation reduction, explicit minimax solution and saturation law are the asserted contributions. The complete-graph case \(s=1\) is a familiar specialization, not an independent novelty claim. Related exact statements for cycle spaces on complete bipartite or matching-deleted bipartite graphs concern different graphs and do not imply this family-wide minimizer.

## Limitations
This is a real, unweighted, relative \(\ell_1\) projection-constant result. It does not establish corresponding formulas for arbitrary positive edge weights, other \(\ell_p\) exponents, or complex-linear projection minima. The finite checker corroborates but cannot certify all parameters; the full conclusion depends on the representation decomposition and exact convex argument above. No independent mathematical audit is claimed. An equivalent calculation in less accessible older minimal-projection literature is a residual bibliographic risk.

## References
- S. J. Dilworth, D. Kutzarova, M. I. Ostrovskii, *Cycle spaces: invariant projections and applications to transportation cost*, arXiv:2305.12582, first publicly submitted 2023-05-21; particularly sections 1.4--1.6 and 2.1--2.7. https://arxiv.org/abs/2305.12582
- M. Cúth and M. Doucha, *Projections in Lipschitz-free spaces induced by group actions*, Mathematische Nachrichten 296 (2023), 3301--3317, https://doi.org/10.1002/mana.202100222 (related symmetry-projection context, not a covering graph-cycle calculation).
