# Quadratic topological complexity after adjoining maximal antichains
## Finding
Let \(X\) be a nonempty noncontractible finite \(T_0\)-space and let \(D_n\) be the discrete finite space on \(n\) points. For every integer \(n\ge 2\), form the non-Hausdorff join
\[
Z=X\oplus D_n,
\]
meaning that the order on \(X\) is unchanged, the points of \(D_n\) are pairwise incomparable, and every point of \(X\) lies below every point of \(D_n\). In the unreduced Schwarz-genus convention for topological complexity,
\[
\mathrm{TC}(Z)=n^2.
\]

## Assumptions and scope
Finite \(T_0\)-spaces are identified with their specialization posets, so open subsets are lower sets. The space \(X\) is assumed nonempty and noncontractible. The integer \(n\) is at least \(2\). Topological complexity is unreduced: \(\mathrm{TC}(Y)\) is the least number of open subsets covering \(Y\times Y\) on each of which the path fibration admits a local section.

The theorem concerns the finite topology of \(Z\), not merely the homotopy type of its order complex. No Hausdorff product inequality is used.

## Proof
Write \(D_n=\{d_1,\ldots,d_n\}\). For each \(d_i\), the principal open set
\[
U_i=X\cup\{d_i\}
\]
has maximum \(d_i\), hence is contractible. The \(n\) sets \(U_i\) cover \(Z\). Tanaka's finite-space inequality
\[
\mathrm{TC}(Z)\le \operatorname{cat}(Z\times Z)\le \operatorname{cat}(Z)^2
\]
therefore gives \(\mathrm{TC}(Z)\le n^2\).

For the reverse inequality, suppose that fewer than \(n^2\) open motion-planning domains cover \(Z\times Z\). The \(n^2\) points of \(D_n\times D_n\) are precisely the maximal points of \(Z\times Z\), so one domain \(Q\) contains two distinct maximal pairs, say \((a,b)\) and \((c,d)\). At least one coordinate differs. Assume first that \(b\ne d\); the other case is symmetric.

Choose any \(x\in X\). Since \(Q\) is a lower set,
\[
(x,b),(x,d)\in Q.
\]
Let
\[
V=\{z\in Z:(x,z)\in Q\}.
\]
A local section of the path fibration over \(Q\) gives a homotopy between the two coordinate projections on \(Q\). Restricting this homotopy to the slice \(z\mapsto(x,z)\) shows that the inclusion \(V\hookrightarrow Z\) is homotopic to the constant map with value \(x\).

Because \(V\) is open and contains the two distinct maximal points \(b,d\), it contains
\[
Y=X\oplus\{b,d\}.
\]
Hence the inclusion \(j:Y\hookrightarrow Z\) is null-homotopic. But there is an order-preserving retraction \(r:Z\to Y\): fix \(X\), \(b\), and \(d\), and send every other point of \(D_n\) to \(b\). Thus \(r\circ j=\mathrm{id}_Y\). If \(j\) were null-homotopic, then \(\mathrm{id}_Y\) would be null-homotopic, so \(Y\) would be contractible.

Kandola's suspension theorem says that for a finite \(T_0\)-space \(X\), the two-point non-Hausdorff suspension \(X\oplus S^0\) has topological complexity \(4\) whenever \(X\) is noncontractible. In particular, \(Y=X\oplus\{b,d\}\) is noncontractible. This contradiction shows that no motion-planning domain can contain two distinct maximal pairs. Therefore at least \(n^2\) domains are required, and
\[
\mathrm{TC}(Z)=n^2.
\]

## Verification
The proof is symbolic and applies to every nonempty noncontractible finite \(T_0\)-space \(X\) and every \(n\ge2\). Its critical steps are: the \(n^2\) maximal-pair pigeonhole argument; restriction of a local path section to obtain a homotopy between a constant map and a slice inclusion; the explicit retraction from \(Z\) onto any two-top suspension; and the known noncontractibility of that suspension when \(X\) is noncontractible.

The standalone checker `artifacts/verify.py` does not certify the quantified theorem by enumeration. It checks the finite order-theoretic mechanism on three noncontractible sample bases: a two-point antichain, the four-point minimal circle, and the six-point minimal \(2\)-sphere. For \(n=2,3,4\) it verifies the \(n^2\) maximal-pair count and every two-top retraction, and it independently verifies that the sampled two-top suspensions have nontrivial Stong cores. Its expected output is stored in `artifacts/verify_output.txt`.

## Relationship to prior work
Tanaka introduced combinatorial complexity for finite spaces and proved that it equals their genuine topological complexity. His Example 3.5 computes \(n^2\) for a two-level space whose lower and upper levels are both discrete, and Example 3.7 obtains \(4\) for the canonical minimal finite sphere models. The arXiv preprint was first public on 2016-05-22.

Kandola later proved two complementary extensions. Her Theorem 1.2 gives \(\mathrm{TC}(X\oplus S^0)=4\) for every noncontractible finite \(X\), while Theorem 1.3 gives \(\mathrm{TC}(D_m\oplus D_n)=n^2\) for arbitrary discrete levels. Neither statement covers arbitrary noncontractible \(X\) together with arbitrary \(n\). The present theorem fills exactly that gap, using a retraction onto the two-top suspension to make the maximal-pair obstruction work for all \(n\).

Searches using the aliases “non-Hausdorff join,” “ordinal sum,” “maximal antichain,” “finite weak order,” and “topological/combinatorial complexity” found no inspected source stating or implying the arbitrary-base/arbitrary-\(n\) theorem. The closest database result on finite weak orders concerns interval-endomorphism algebra dimensions, a different invariant.

## Limitations
The hypothesis that \(X\) is noncontractible is essential for \(n\ge2\): if \(X\) is contractible, then the join is contractible and has topological complexity \(1\). The theorem uses the unreduced convention. It does not classify optimal motion planners beyond the exact number of required domains, nor does it assert a corresponding formula for arbitrary finite joins in which the new upper factor is not discrete.

The originality comparison is limited to the sources and searches recorded in the review. In particular, a result phrased solely in motion-planning or finite-poset language without the standard join terminology could still have been missed.

## References
1. K. Tanaka, *A combinatorial description of topological complexity for finite spaces*, arXiv:1605.06755v1 (submitted 2016-05-22); later Algebraic & Geometric Topology 18 (2018), 779–796.
2. S. Kandola, *The Topological Complexity of Finite Models of Spheres*, arXiv:1812.07604v1 (submitted 2018-12-18).
