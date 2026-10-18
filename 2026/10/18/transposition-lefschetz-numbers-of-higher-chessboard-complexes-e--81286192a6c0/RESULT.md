# Transposition Lefschetz numbers of higher chessboard complexes enumerate regular graphs

## Finding

Fix integers \(n\ge 2\) and \(1\le r\le n-1\). Let \(X_{n,r}=M_r(K_{n,n})\), the higher matching (bounded-degree chessboard) simplicial complex whose vertices are positions \((i,j)\in[n]\times[n]\) and whose faces are the sets of positions meeting every row and column at most \(r\) times. The transposition \(\tau(i,j)=(j,i)\) is a simplicial involution. Let \(R(n,r)\) be the number of labeled simple \(r\)-regular graphs with vertex set \([n]\); thus \(R(n,r)=0\) when \(nr\) is odd.

**Theorem.** The reduced rational Lefschetz number of transposition is

\[
\widetilde L(\tau;X_{n,r})
=\sum_{k\ge0}(-1)^k\operatorname{tr}\bigl(\tau_*\mid\widetilde H_k(X_{n,r};\mathbb Q)\bigr)
=\begin{cases}-(-1)^{nr/2}R(n,r),&nr\text{ even},\\0,&nr\text{ odd}.\end{cases}
\]

In particular, the total reduced rational Betti number satisfies

\[
\sum_{k\ge0}\dim_{\mathbb Q}\widetilde H_k(X_{n,r};\mathbb Q)\ge R(n,r).
\]

For \(r=2\), let \(c_n=R(n,2)\) count spanning disjoint unions of undirected cycles of length at least three. Then \(\widetilde L(\tau;X_{n,2})=(-1)^{n+1}c_n\), and

\[
\sum_{n\ge0}\frac{c_n}{n!}t^n=(1-t)^{-1/2}\exp(-t/2-t^2/4).
\]

An additional orientation consequence is that, for every \(n\ge2\), transposition has degree \((-1)^{\binom{n+1}{2}+1}\) on the unique top integral homology of the homotopy sphere \(M_{n-1}(K_{n,n})\).

## Assumptions and scope

Graphs counted in \(R(n,r)\) are undirected, simple, labeled by \([n]\), with no loops or parallel edges. A face of \(X_{n,r}\) is an arbitrary subset of the \(n^2\) bipartite edges meeting the row and column degree caps; it need not be a graph-theoretic matching unless \(r=1\). The empty face occurs in the augmented simplicial chain complex in degree \(-1\). Since \(n\ge2\) and \(r\ge1\), \(X_{n,r}\) has vertices, so its reduced homology in degree \(-1\) is zero. All homology character statements are over \(\mathbb Q\), except the orientation-degree corollary, which concerns \(\mathbb Z\) on a rank-one group. No assertion of complete homotopy type is made for intermediate degree caps.

## Proof

Order the vertices \((i,j)\) lexicographically and orient each nonempty simplex in this order. By the Hopf trace theorem applied to the finite augmented simplicial chain complex, the reduced Lefschetz number is the alternating trace on oriented chains, including the degree \(-1\) empty face with contribution \(-1\). Non-fixed simplices make no contribution to the trace.

A transposition-invariant face has \(d\) selected diagonal positions \((i,i)\) and \(e\) selected unordered off-diagonal pairs \(\{(i,j),(j,i)\}\). It therefore contains \(d+2e\) vertices and \(d+e\) orbits. The involution on its oriented simplex is a product of \(e\) transpositions, with sign \((-1)^e\). Its contribution to the reduced alternating chain trace is

\[
(-1)^{d+2e-1}(-1)^e=-(-1)^{d+e}.
\]

The same formula also gives \(-1\) for the empty face with \(d=e=0\). Thus the reduced Lefschetz number is minus the signed sum \(\sum_F(-1)^{q(F)}\) over invariant admissible faces, where \(q(F)\) counts the chosen transposition orbits.

The selected off-diagonal orbits are canonically the edges of a labeled simple undirected graph \(H\) on \([n]\). Each vertex \(i\) has both row and column occupancy \(\deg_H(i)\) from these orbits. Hence admissibility first requires \(\deg_H(i)\le r\) for every \(i\). For such an \(H\), the diagonal position \((i,i)\) can be chosen or omitted precisely when \(\deg_H(i)<r\); it must be omitted if \(\deg_H(i)=r\).

Writing \(u(H)=\#\{i:\deg_H(i)<r\}\), the sum over all admissible choices of diagonal positions, for fixed \(H\), is

\[
(-1)^{|E(H)|}\sum_{D\subseteq\{i:\deg_H(i)<r\}}(-1)^{|D|}
=(-1)^{|E(H)|}(1-1)^{u(H)}.
\]

This cancels unless every vertex of \(H\) has degree exactly \(r\). Each surviving \(r\)-regular \(H\) has exactly \(nr/2\) edges by the handshake lemma, and there are \(R(n,r)\) such graphs. If \(nr\) is odd, none exists. Including the leading minus sign proves the displayed Lefschetz formula. This is an identity for every stated pair \((n,r)\), not a deduction from a finite enumeration.

For the Betti-number bound, the absolute value of an alternating sum of traces is at most the sum of homology dimensions, because \(\tau_*\) is an involution and each eigenvalue is \(\pm1\).

For \(r=2\), a simple two-regular graph is uniquely a vertex-disjoint union of cycles of lengths at least three. There are \((\ell-1)!/2\) unoriented labeled cycles on a prescribed \(\ell\)-element set for \(\ell\ge3\). The labeled exponential formula gives

\[
\exp\left(\sum_{\ell\ge3}\frac{t^\ell}{2\ell}\right)
=(1-t)^{-1/2}\exp(-t/2-t^2/4),
\]

and the sign specializes to \(-(-1)^n=(-1)^{n+1}\).

For \(r=n-1\), the unique simple \((n-1)\)-regular graph is \(K_n\), so \(R(n,n-1)=1\). Singh's homotopy theorem [1, Theorem 1.2] gives \(X_{n,n-1}\simeq S^{(n-1)^2-1}\). The reduced Lefschetz number is thus \((-1)^{(n-1)^2-1}\) times the degree of transposition on its rank-one top homology. Solving for that degree gives \((-1)^{\binom{n+1}{2}+1}\). This step uses the previously established sphere theorem; the orientation character, not the sphere homotopy type, is the additional conclusion.

## Verification

Run the supplied `verify_transpose.py` with Python 3, using only the standard library. `verification_output.txt` records one successful execution. The program **independently** enumerates all bounded-row/column faces and computes the signed trace on oriented augmented simplicial chains for each \(2\le n\le4\) and every \(1\le r<n\). It separately enumerates all labeled simple graphs on \([n]\) to compute \(R(n,r)\). The predicted and directly computed traces agree in all six cases. For \(r=2\), an independent cycle-component recurrence gives \(c_n\) for \(3\le n\le8\); exhaustive simple-graph enumerations also agree for \(3\le n\le6\), yielding \(1,3,12,70,465,3507\) at \(n=3,\ldots,8\). The computations are finite cross-checks, not the proof for general parameters.

## Relationship to prior work

Singh [1] introduced the studied higher matching complexes and determined the homotopy type at the extremal cap \(r=n-1\); this provides the input for the orientation corollary, but does not specify the action of the factor-interchange involution. Reiner and Roberts [2, Theorem 3.3] computed rational homology representations under **independent row and column relabelings**, i.e., the \(S_n\times S_n\) subgroup. Interchanging the bipartite factors is an additional operation outside that subgroup; knowledge of a representation on the subgroup does not determine the action of this extra generator. The new claim is the explicit signed topological character of this involution for every cap, its regular-graph-count interpretation, and the resulting lower bounds and sphere orientation signs. No new claim is made about the previously determined normal-subgroup representation.

## Limitations

The result computes one alternating equivariant homology character, not the separate trace in each homological degree for general \(r\), and not integral torsion or a complete decomposition of the full automorphism representation. The absolute-trace lower bound need not be tight. Existing computations and literature comparison do not rule out equivalent formulas in unindexed sources or terminology using symmetric chessboards and graph-degree restrictions. The computational tests cover only the stated finite sizes; the general theorem rests on the signed orbit cancellation proof.

## References

[1] Anurag Singh, *Higher matching complexes of complete graphs and complete bipartite graphs*, arXiv:2006.13632, first posted 24 June 2020, https://arxiv.org/abs/2006.13632 . Theorem 1.2 and discussion of earlier rational homology.

[2] Victor Reiner and Joel Roberts, *Minimal Resolutions and the Homology of Matching and Chessboard Complexes*, Journal of Algebraic Combinatorics **11** (2000), 135–154, DOI: 10.1023/A:1008728115910 . Theorem 3.3 on the rational homology as a representation of independently permuted rows and columns.
