# Exact ordered-tuple orbit profiles of the side-preserving random bipartite reducts
## Finding
Let \(\Gamma\) be the countable random bipartite graph with named sides \(R_l,R_r\), and let
\(\operatorname{Aut}(\Gamma)^*, S_l(\Gamma), S_r(\Gamma), S_{l,r}(\Gamma)\), and
\(\operatorname{Sym}_{l,r}(\Gamma)\) be the five closed side-preserving groups in Yun Lu's classification.

For a group \(G\), write \(f_G(k)\) for the number of \(G\)-orbits on ordered \(k\)-tuples of pairwise distinct vertices. Then \(f_G(0)=1\), and for every \(k\ge 1\),
\[
f_{\operatorname{Aut}(\Gamma)^*}(k)
=
2+\frac12\sum_{a=1}^{k-1}\binom{k}{a}2^{a(k-a)},
\]
\[
f_{S_l(\Gamma)}(k)
=
2+\sum_{a=1}^{k-1}\binom{k}{a}2^{a(k-a-1)},
\]
\[
f_{S_r(\Gamma)}(k)
=
2+\sum_{a=1}^{k-1}\binom{k}{a}2^{(a-1)(k-a)},
\]
\[
f_{S_{l,r}(\Gamma)}(k)
=
2+\sum_{a=1}^{k-1}\binom{k}{a}2^{(a-1)(k-a-1)},
\qquad
f_{\operatorname{Sym}_{l,r}(\Gamma)}(k)=2^k.
\]
In particular,
\[
f_{S_l(\Gamma)}(k)=f_{S_r(\Gamma)}(k)
\]
for every \(k\), although \(S_l(\Gamma)\) and \(S_r(\Gamma)\) are distinct closed subgroups in the side-preserving reduct lattice.

If \(o_G(n)\) denotes the number of \(G\)-orbits on all ordered \(n\)-tuples, allowing repeated entries, then
\[
o_G(n)=\sum_{k=0}^{n}{n\brace k}f_G(k),
\]
where \({n\brace k}\) is a Stirling number of the second kind.

The first injective profiles, indexed by \(k=0,\ldots,7\), are:
- \(\operatorname{Aut}(\Gamma)^*\): \(1,2,4,14,82,722,9154,165314\);
- \(S_l(\Gamma)\) and \(S_r(\Gamma)\): \(1,2,4,11,46,287,2584,33161\);
- \(S_{l,r}(\Gamma)\): \(1,2,4,8,22,92,574,5168\);
- \(\operatorname{Sym}_{l,r}(\Gamma)\): \(1,2,4,8,16,32,64,128\).

Consequently the ordered-tuple orbit profile alone does not distinguish all five closed groups: the left-switch and right-switch groups have identical profiles in every arity.

Their injective-profile logarithmic growth is
\[
\log_2 f_{\operatorname{Aut}(\Gamma)^*}(k)
=
\frac{k^2}{4}+k-\frac12\log_2 k+O(1),
\]
\[
\log_2 f_{S_l(\Gamma)}(k)
=
\log_2 f_{S_r(\Gamma)}(k)
=
\frac{k^2}{4}+\frac{k}{2}-\frac12\log_2 k+O(1),
\]
\[
\log_2 f_{S_{l,r}(\Gamma)}(k)
=
\frac{k^2}{4}-\frac12\log_2 k+O(1),
\qquad
\log_2 f_{\operatorname{Sym}_{l,r}(\Gamma)}(k)=k.
\]

## Assumptions and scope
The sides \(R_l\) and \(R_r\) are named and must be preserved setwise. Cross-edges are encoded by one of Lu's two cross-types; choosing the opposite convention changes no orbit count. The result concerns Lu's five closed groups lying between \(\operatorname{Aut}(\Gamma)^*\) and \(\operatorname{Sym}_{l,r}(\Gamma)\). No claim is made here about groups that interchange the two sides.

The formulas use only finite induced substructures of the countable random bipartite graph and its standard homogeneity: every isomorphism between finite induced bipartite subgraphs that respects the named sides extends to an automorphism.

## Proof
Fix an ordered injective \(k\)-tuple and a side assignment having \(a\) coordinates in \(R_l\) and \(b=k-a\) in \(R_r\). If \(a,b>0\), its cross-type data is an \(a\times b\) binary matrix \(M\). Homogeneity implies that, after the side assignment is fixed, the orbit question is exactly the orbit question for \(M\) under the finite restrictions of the relevant switch operations.

For \(\operatorname{Aut}(\Gamma)^*\), Lu's global cross-type exchange sends \(M\) to \(M+J\), where \(J\) is the all-one matrix. This action is free when \(ab>0\), so it has \(2^{ab-1}\) orbits.

For \(S_l(\Gamma)\), switching any chosen finite set of left vertices adds arbitrary row-constant matrices. The translation space has dimension \(a\), hence there are
\[
2^{ab-a}=2^{a(b-1)}
\]
matrix orbits.

For \(S_r(\Gamma)\), arbitrary column switches form a translation space of dimension \(b\), giving
\[
2^{ab-b}=2^{(a-1)b}
\]
matrix orbits.

For \(S_{l,r}(\Gamma)\), row and column switches together produce the subspace
\[
\{(r_i+c_j)_{i,j}:r_i,c_j\in\mathbf F_2\}.
\]
Its kernel consists exactly of the two simultaneous constant choices \((r_i,c_j)=(0,0)\) and \((1,1)\), so its image has dimension \(a+b-1\). The number of matrix orbits is therefore
\[
2^{ab-(a+b-1)}=2^{(a-1)(b-1)}.
\]

For \(\operatorname{Sym}_{l,r}(\Gamma)\), only the side assignment survives, so there is one orbit for each of the \(2^k\) assignments.

There are \(\binom{k}{a}\) side assignments with \(a\) left coordinates. The all-left and all-right cases each contribute one orbit. Summing the matrix-orbit counts over \(1\le a\le k-1\) proves all five formulas. Replacing \(a\) by \(k-a\) proves
\[
f_{S_l(\Gamma)}(k)=f_{S_r(\Gamma)}(k).
\]

For non-injective tuples, the equality relation on coordinate positions is invariant under every permutation group. Choosing a set partition of \([n]\) into \(k\) equality blocks and then an injective \(k\)-tuple orbit gives the Stirling transform
\[
o_G(n)=\sum_{k=0}^{n}{n\brace k}f_G(k).
\]

For the asymptotics, the dominant terms occur for balanced \(a\). The relevant binary-matrix exponents attain maxima
\[
\frac{k^2}{4},\qquad \frac{(k-1)^2}{4},\qquad \frac{(k-2)^2}{4},
\]
respectively. The central binomial coefficient contributes
\[
k-\frac12\log_2 k+O(1),
\]
and displacement by \(t\) from the maximizing \(a\) suppresses a summand by a factor \(2^{-\Theta(t^2)}\). Thus summing all near-central terms changes the logarithm only by \(O(1)\), yielding the displayed growth laws.

## Verification
The accompanying `verify.py` performs two independent finite checks. First, it exhaustively enumerates binary \(a\times b\) matrices for all tested pairs with \(1\le a,b\le3\) and \(ab\le8\), constructs the actual global-complement, row-switch, column-switch, and row-plus-column-switch translation actions, and compares the resulting orbit counts with the closed formulas. Second, it recomputes the injective profiles and their Stirling transforms through arity \(7\), and verifies the equality of the left-switch and right-switch profiles through arity \(49\). Successful execution ends with `VERIFY_OK`.

## Relationship to prior work
Lu classified the closed side-preserving reduct groups of the random bipartite graph and supplied the switch definitions and finite parity characterizations that identify the relevant translation actions. The classification does not state the ordered-tuple orbit formulas above or the profile collision between \(S_l(\Gamma)\) and \(S_r(\Gamma)\).

Recent general work on oligomorphic groups treats orbit finiteness and cites bipartite graphs as basic homogeneous examples, but it does not provide these five exact profiles. Searches for the formulas, their initial sequences, and the all-arity profile collision did not locate a stronger or equivalent published result.

## Limitations
Originality is a best-of-knowledge conclusion based on targeted literature and semantic-result searches, not an exhaustive proof that no equivalent formula occurs anywhere. The result is restricted to side-preserving groups in Lu's five-group classification. The computational verifier checks finite instances and arithmetic identities; it does not replace the general group-theoretic proof. Independent audit, formal proof-assistant verification, and expert attestation have not been performed.

## References
1. Yun Lu, “Reducts of the random bipartite graph,” arXiv:1101.1947, first public version 2011-01-10; later published in *Notre Dame Journal of Formal Logic* 54(1), DOI 10.1215/00294527-1731371.
2. Nate Harman and Andrew Snowden, “Oligomorphic groups and tensor categories,” *Inventiones mathematicae* (2026), DOI 10.1007/s00222-026-01452-2.
