# Reversal-twisted Lefschetz series of half-graph matching complexes

## Finding
For every integer \(n\geq1\), let \(B_n\) be the half-graph with distinct vertices \(p_1,\ldots,p_n,q_1,\ldots,q_n\) and edges \(p_iq_j\) exactly when \(1\leq i\leq j\leq n\). Let \(K_n=\mathcal M(B_n)\) be its ordinary matching complex. The involution \(\rho(p_i)=q_{n+1-i}\), \(\rho(q_j)=p_{n+1-j}\) induces a simplicial involution of \(K_n\).

Write \(\widetilde C_{k-1}(K_n;\mathbb Q)\) for its augmented oriented simplicial chains, including \(\widetilde C_{-1}\cong\mathbb Q\) in degree \(-1\), and define the signed face-trace polynomial
\[
T_n(y)=\sum_{k=0}^{n}\operatorname{tr}\!\left(\rho\mid\widetilde C_{k-1}(K_n;\mathbb Q)\right)y^k.
\]
All of its coefficients are determined by two exponential generating functions. With
\[
F(z,y)=\frac{1-e^{-y^2z}}{y}+\frac{1-e^{-2y^2z}}{2y^2},
\]
where the apparent denominators are removed by formal expansion, for every integer \(m\geq1\) one has
\[
\boxed{T_{2m-1}(y)=m!\,[z^m]\exp(F(z,y)),\qquad
T_{2m}(y)=m!\,[z^m]e^{-y^2z}\exp(F(z,y)).}
\]
In particular the reduced rational Lefschetz number of the involution on homology is
\[
\boxed{\widetilde L_n(\rho):=\sum_{i\geq0}(-1)^i\operatorname{tr}\!\left(\rho\mid\widetilde H_i(K_n;\mathbb Q)\right)=-T_n(-1).}
\]
Let \(\left\{\begin{smallmatrix}a\\b\end{smallmatrix}\right\}\) denote a Stirling number of the second kind, and set
\[
A_n=\sum_{k=0}^n(-1)^k\left\{\begin{smallmatrix}n+1\\n+1-k\end{smallmatrix}\right\}.
\]
The rational Euler characteristic of the geometric quotient is then exactly
\[
\boxed{\chi(|K_n|/\langle\rho\rangle)=1-\frac{A_n+T_n(-1)}{2}.}
\]
For example, the polynomials \(T_n(y)\) for \(n=2,3,4\) are respectively \(1+y-y^2\), \(1+2y-y^2-y^3\), and \(1+2y-3y^2-3y^3+y^4\). The result determines all graded *cellular traces*, all reduced Lefschetz numbers, and all quotient Euler characteristics; it does not assert an individual-degree homology character formula.

## Assumptions and scope
The graphs are finite, simple, and undirected, and \(K_n\) is the matching simplicial complex with **all** matchings (not the subcomplex of perfect matchings). A \(k\)-edge matching determines a simplex of dimension \(k-1\). Every trace is taken over \(\mathbb Q\), although cellular traces and the generating series have integer coefficients. The graph involution is the simultaneous exchange of the two vertex classes and reversal of their order. The formulas include \(n=1\); they also apply to disconnected and non-pure stages of the matching complex without any homology-concentration assumption.

## Proof
**1. Set partitions encode matchings.** Identify an edge \(p_iq_j\) with the forward directed arc \(i\to j+1\) on \([n+1]\). Pairwise disjoint half-graph edges are precisely selections of arcs for which each label has at most one outgoing and at most one incoming arc. Because arcs strictly increase the label, such a selection is a vertex-disjoint union of directed paths and isolated vertices. Sorting each path's vertex set gives a bijection with set partitions of \([n+1]\): for each block, connect consecutive labels in increasing order. The correspondence preserves the number of arcs \(k=(n+1)-\#\text{blocks}\). Consequently the number of size-\(k\) matchings is \(\left\{\begin{smallmatrix}n+1\\n+1-k\end{smallmatrix}\right\}\).

**2. The involution acts as order reversal.** Under this bijection \(\rho\) sends arc \(a\to b\) to \((n+2-b)\to(n+2-a)\), so it sends each block to its image under the reversal \(a\mapsto n+2-a\). A simplex contributes to \(T_n(y)\) only if its set partition is reversal-invariant. Its coefficient is the orientation sign of the permutation of its arcs, not merely the number of invariant faces.

**3. Classify invariant blocks and compute exact signs.** Group the \(\lfloor(n+1)/2\rfloor\) reversed pairs of labels as distinguishable atoms. Away from a possible central fixed label, the invariant partition's blocks split uniquely into two species.

A self-reversed block on \(t\geq1\) pairs has \(2t\) labels and \(2t-1\) consecutive arcs. Reversal permutes these arcs with exactly \(t-1\) transpositions, contributing \((-1)^{t-1}y^{2t-1}\). A pair of mutually reversed, distinct blocks on \(t\geq1\) pairs has \(2^{t-1}\) possible assignments of the labels to the two unlabelled blocks. The blocks have altogether \(2t-2\) arcs, exchanged in \(t-1\) pairs, contributing \(2^{t-1}(-1)^{t-1}y^{2t-2}\). These are the only possibilities: any block is either self-reversed or belongs to a unique two-orbit under reversal.

When \(n+1=2m+1\) is odd, the unique central label lies in one additional self-reversed block. If this block contains \(t\geq0\) reversed pairs, it has \(2t\) arcs exchanged in \(t\) pairs, contributing \((-1)^ty^{2t}\). No other block contains the central label.

**4. Labelled exponential formula.** For the two species without a central label, the exponential generating series on the reversed-pair atoms are respectively
\[
\sum_{t\geq1}(-1)^{t-1}y^{2t-1}\frac{z^t}{t!}=\frac{1-e^{-y^2z}}y,
\qquad
\sum_{t\geq1}2^{t-1}(-1)^{t-1}y^{2t-2}\frac{z^t}{t!}=\frac{1-e^{-2y^2z}}{2y^2}.
\]
The invariant partition is an unordered **set** of these components, hence the exponential of their sum. In the odd-ground-set case the central block adds the factor
\[
\sum_{t\geq0}(-1)^ty^{2t}\frac{z^t}{t!}=e^{-y^2z}.
\]
Extracting the coefficient for \(m\) labelled atom pairs proves both boxed series, including all orientation signs and all exponents. The proof uses finite combinatorial bijections, so it is valid for every integer \(m\geq1\), rather than extrapolating finite computations.

**5. Lefschetz and quotient Euler characteristics.** The reduced Hopf trace identity on the finite augmented chain complex gives \(\widetilde L_n(\rho)=\sum_{k\geq0}(-1)^{k-1}\operatorname{tr}(\rho\mid\widetilde C_{k-1})=-T_n(-1)\). Setting the chain trace to the identity recovers \(\chi(|K_n|)=1-A_n\) from step 1. Barycentric subdivision makes the finite group action cellular without inversions; its fixed-subdivision Euler characteristic is the ordinary Lefschetz number \(1-T_n(-1)\). Averaging cellular fixed-chain dimensions for the order-two group proves \(\chi(|K_n|/\langle\rho\rangle)=\tfrac12((1-A_n)+(1-T_n(-1)))\), as claimed.

## Verification
The standard-library script `verify.py` independently (a) enumerates every matching of \(B_n\), and sums the **signed** orientation trace of \(\rho\) on each augmented chain group, and (b) calculates the graded trace by an integer recurrence derived from reversed-pair components. It asserts equality of every coefficient for all \(1\leq n\leq9\), including the empty-simplex term. On replay it prints `HALFGRAPH_REFLECTION_GRADED_TRACE_VERIFIED n=1..9`. The all-parameter result is established by steps 1–5, not by this finite test.

## Relationship to prior work
Caputi, Collari, Di Trani and Smith (arXiv:2208.04656, first posted August 9, 2022) identified multipaths of transitive tournaments with set partitions and computed the **identity** Euler characteristic via Stirling numbers, as well as wedge-of-spheres homotopy types. Caputi, Collari and Ramos (arXiv:2401.01248, first posted January 2, 2024), Theorems 4.20 and 4.23, identified the corresponding half-graph matching complexes and established their wedge-or-contractible nature. The finding here isolates the *part-swapping reversal* and counts fixed partitions with signed arc orientations, which are not determined by the earlier nonequivariant formula. The exponential series thus refines the ordinary Euler number to a full graded signed trace and an exact quotient Euler characteristic.

## Limitations
The graded chain trace determines the alternating action on rational homology but does not generally determine the individual rational homology representations, integral torsion, or homotopy type of the quotient. Although both cited primary texts were available for statement-level comparisons, an algebraically equivalent signed set-partition enumeration could exist in unindexed combinatorial literature. The finite verification up to \(n=9\) is a check, not an exhaustive proof over all sizes. No independent audit is claimed.

## References
1. L. Caputi, C. Collari, S. Di Trani and J. P. Smith, *On the homotopy type of multipath complexes*, arXiv:2208.04656 (2022), especially Theorems 3.4 and 5.1. https://arxiv.org/abs/2208.04656
2. L. Caputi, C. Collari and E. Ramos, *The weak categorical quiver minor theorem and its applications: matchings, multipaths, and magnitude cohomology*, arXiv:2401.01248 (2024), especially Theorems 4.20 and 4.23. https://arxiv.org/abs/2401.01248
