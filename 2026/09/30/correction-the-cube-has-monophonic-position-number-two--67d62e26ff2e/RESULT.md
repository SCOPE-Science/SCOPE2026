# Correction: the cube has monophonic position number two
## Finding
Let \(Q_n\) denote the binary \(n\)-cube, with vertices identified with subsets of \([n]\) and adjacency given by symmetric difference of size one. For every \(n\ge 1\),
\[
\operatorname{mp}(Q_n)=2.
\]
In particular, the ordinary three-dimensional cube \(Q_3\) has monophonic position number \(2\), not \(4\).

This corrects the explicit statement in *On monophonic position sets in graphs* that the cube has order eight and monophonic position number four. The corrected numerical value is also an immediate consequence of the later general Cartesian-product inequality
\[
\operatorname{mp}(G\square H)\le
\max\{\operatorname{mp}(G),\operatorname{mp}(H)\},
\]
because \(Q_n=K_2\square Q_{n-1}\) and every graph of order at least two has monophonic position number at least \(2\). The contribution recorded here is the identification and documentation of this literature inconsistency together with a direct elementary certificate; the numerical formula is not claimed as independent novelty beyond the later Cartesian-product theorem.

## Assumptions and scope
Graphs are finite, simple, and undirected. A path is monophonic if it is induced. A vertex set is in monophonic position if no three of its vertices lie on a common induced path, and \(\operatorname{mp}(G)\) is the maximum size of such a set.

The statement concerns binary hypercubes \(Q_n\) for \(n\ge1\). It does not assert that the cubic-graph upper bound for which the cube was offered as a sharpness example is itself non-sharp; it only shows that \(Q_3\) does not witness equality.

## Proof
Fix three distinct vertices \(X,Y,Z\) of \(Q_n\). Translation by symmetric difference with \(Z\) is an automorphism of the cube, so it is enough to construct an induced path through
\[
\varnothing,\qquad A=X\triangle Z,\qquad B=Y\triangle Z.
\]
Partition the active coordinates as
\[
P=A\setminus B,\qquad Q=B\setminus A,\qquad R=A\cap B.
\]

If \(P=\varnothing\), then \(A\subset B\). Starting at \(\varnothing\), flip each coordinate of \(A\), reaching \(A\), and then flip the coordinates of \(B\setminus A\), reaching \(B\). Every coordinate is flipped at most once, so this is a geodesic and hence an induced path containing all three vertices. The case \(Q=\varnothing\) is symmetric.

Assume now that \(P\) and \(Q\) are both nonempty. Construct a path from \(A\) to \(\varnothing\) by first flipping all coordinates of \(R\) and then all coordinates of \(P\). Continue from \(\varnothing\) to \(B\) by first flipping all coordinates of \(Q\) and then all coordinates of \(R\).

Each of the two halves is geodesic and therefore induced. It remains only to rule out a chord joining a nonzero vertex \(U\) on the first half to a nonzero vertex \(V\) on the second half. Every such \(U\) contains at least one coordinate of \(P\): coordinates of \(R\) are removed first, and the path reaches \(\varnothing\) only after the last coordinate of \(P\) is removed. Every such \(V\) contains at least one coordinate of \(Q\): coordinates of \(Q\) are inserted first and never removed. Since \(P\cap B=\varnothing\) and \(Q\cap A=\varnothing\), these two coordinates both belong to \(U\triangle V\). Hence
\[
|U\triangle V|\ge2,
\]
so \(U\) and \(V\) are not adjacent in the cube. Thus the concatenated path is induced.

Therefore every three distinct vertices of \(Q_n\) lie on a common induced path. No monophonic-position set can have size three, so \(\operatorname{mp}(Q_n)\le2\). Any pair of vertices is in monophonic position, giving \(\operatorname{mp}(Q_n)\ge2\), and the equality follows.

## Verification
The accompanying `verify.py` implements exactly the constructive proof above. For every unordered triple of vertices of \(Q_n\) for \(1\le n\le7\), it constructs the prescribed path, checks that the three vertices occur on the path, verifies every consecutive pair is adjacent, verifies there are no repeated vertices, and checks that no nonconsecutive pair is adjacent. It checks \(388620\) triples and ends with `VERIFY_OK`.

This finite computation is corroborative only. The proof for arbitrary \(n\) is the coordinate argument above, and no independent audit, proof-assistant verification, or expert attestation is claimed.

## Relationship to prior work
Thomas, Chandran, Tuite, and Di Stefano introduced the monophonic position problem and explicitly wrote, immediately after their cubic-graph upper bound, that the cube has order eight and monophonic position number four. Their preprint first appeared on 18 December 2020 and the statement remains in the published article.

Chandran, Klavžar, Neethu, and Tuite later proved the general Cartesian-product inequality
\[
\operatorname{mp}(G\square H)\le
\max\{\operatorname{mp}(G),\operatorname{mp}(H)\}.
\]
Applied inductively to \(Q_n=K_2^{\square n}\), this theorem already entails \(\operatorname{mp}(Q_n)=2\). In the checked article text, hypercubes are not singled out and the conflict with the earlier cube example is not noted. Thus the corrected numerical value is covered by stronger later work; the present finding is specifically the correction and reconciliation of the two statements, with a direct proof from the definition.

## Limitations
The originality claim is deliberately narrow: it concerns identifying and documenting the unnoted contradiction and supplying a direct certificate. It does not claim the formula \(\operatorname{mp}(Q_n)=2\) as a standalone theorem independent of the later Cartesian-product result. Literature coverage is best-of-knowledge and may miss an unusually phrased or inaccessible erratum. The status of the broader cubic-graph sharpness assertion is not settled here.

## References
1. E. J. Thomas, S. V. Ullas Chandran, J. Tuite, and G. Di Stefano, *On monophonic position sets in graphs*, arXiv:2012.10330, first posted 18 December 2020; Discrete Applied Mathematics 354 (2024), 72–82, doi:10.1016/j.dam.2023.02.021.
2. U. Chandran S. V., S. Klavžar, P. K. Neethu, and J. Tuite, *Monophonic position sets of Cartesian and lexicographic products of graphs*, arXiv:2412.09837, first posted 13 December 2024; doi:10.1007/s40314-026-03901-3.
