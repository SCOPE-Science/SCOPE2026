# Exact shortest-reset letter marginals for the six-state five-letter slow automaton
## Finding
Let \(A_6\) be the six-state instance of the five-letter automaton \(A\) in Theorem 3 of de Bondt--Don--Zantema. Thus the state set is \(Q=\{1,\ldots,6\}\), the alphabet is \(\{a,b,c,d,e\}\), and the transition maps are the specialization to \(n=6\) of the published table. The reset threshold is \(20\). Every shortest reset word sends all six states to state \(3\), and the exact number of shortest reset words is
\[
452{,}984{,}832=2^{24}3^3.
\]
Moreover, every shortest reset word avoids the letter \(b\).

For each letter \(x\in\{a,b,c,d,e\}\), define the marginal letter-count enumerator
\[
P_x(z)=\sum_{w}z^{|w|_x},
\]
where the sum ranges over all shortest reset words and \(|w|_x\) is the number of occurrences of \(x\) in \(w\). Then
\[
P_a(z)=64(z+1)^6(z+2)^3(z+3)^6,
\]
\[
P_b(z)=452{,}984{,}832,
\]
\[
P_c(z)=P_d(z)=8z(z+1)^3(z+3)^6(z^2+4z+7)^3,
\]
and
\[
P_e(z)=64(z+1)^3(z+3)^6(z+5)^3.
\]
In particular, substituting \(z=1\) in any marginal gives the same total \(452{,}984{,}832\).

## Assumptions and scope
The automaton is exactly the six-state specialization of the transition table in Theorem 3 of arXiv:1609.06853. In one-based state notation its transition columns are
\[
a=(2,3,4,5,6,1),\quad b=(1,3,3,4,5,6),
\]
\[
c=(3,3,4,5,6,1),\quad d=(2,4,4,5,6,1),\quad e=(3,4,4,5,6,1).
\]
The claim is finite and exact for this one automaton. No analogous factorization for arbitrary \(n\) is asserted.

## Proof
Use the power automaton whose states are the nonempty subsets of \(Q\). A letter sends a subset to its pointwise image. Breadth-first search from \(Q\) visits all \(63\) nonempty subsets and gives minimum distance \(20\) to a singleton; the unique singleton attained at distance \(20\) is \(\{3\}\). This recovers the published threshold \(6^2-3\cdot6+2=20\) and fixes the reset target for every shortest word.

Every prefix of a shortest reset word is itself a shortest path to its image subset: if a prefix reaching \(S\) could be shortened, replacing it while retaining the suffix would shorten the reset word. Hence all shortest reset words are exactly the paths in the directed acyclic graph consisting of power-automaton edges that increase the breadth-first distance by one.

For a fixed letter \(x\), attach weight \(z\) to an \(x\)-edge and weight \(1\) to every other edge. Starting with polynomial \(1\) at \(Q\), propagate exact integer polynomials layer by layer along these distance-increasing edges and add at the singleton layer. This computes \(P_x(z)\) without enumerating the words individually. The resulting coefficient arrays are recorded in `certificate.json`; exact integer convolution verifies the displayed factorizations coefficient by coefficient. Their sums are \(452{,}984{,}832\). The \(b\)-enumerator is constant, so no shortest word uses \(b\). The terminal mass is entirely at \(\{3\}\).

A second computation using `frozenset` subsets, separate first-arrival layers, and independent histogram propagation reproduces the same threshold, target, and every coefficient, without consulting the bit-mask distance table.

## Verification
Run `python3 verify.py`. The verifier uses only the Python standard library. It reconstructs the five transition maps, exhaustively traverses the six-state power automaton, computes all five shortest-path marginals by bit-mask dynamic programming, independently recomputes them using set-valued layers, expands the claimed factorizations by integer convolution, and compares all results exactly. A successful run prints `VERIFY_OK length=20 total=452984832 target=3 reachable_subsets=63`.

## Relationship to prior work
The defining paper proves for the general five-letter construction that the reset threshold is \(n^2-3n+2\); for \(n=6\) this gives \(20\). Its proof also shows that there exists a shortest reset word using only \(c\) and \(d\), but an existence-preserving replacement argument does not determine all shortest words. The same paper explicitly records shortest-word multiplicities for several other small critical automata, so multiplicity is a native structural invariant in this literature, and its exhaustive small-state investigation ends at six states.

The general shortest-reset-word algorithm of Kisielewicz--Kowalski--Szykuła computes a shortest reset word efficiently on known slowly synchronizing families, but the inspected text does not give this automaton's all-shortest-word count or its marginal letter-count enumerators. The new statement therefore refines a known reset threshold to the complete one-letter composition distributions of all optimal reset controls.

## Limitations
This is a finite six-state theorem proved by exhaustive traversal of its \(63\)-vertex nonempty power automaton. It does not establish an infinite-family formula. Originality was checked against the defining full text, a broader shortest-reset-word algorithm paper, targeted database searches, and prior local records; a non-indexed ancillary or unpublished computation could still contain the same finite enumerators.

## References
1. M. de Bondt, H. Don, H. Zantema, *Slowly synchronizing automata with fixed alphabet size*, arXiv:1609.06853, first public version 22 September 2016; later Information and Computation 279 (2021), 104614, DOI:10.1016/j.ic.2020.104614.
2. A. Kisielewicz, J. Kowalski, M. Szykuła, *Computing the shortest reset words of synchronizing automata*, Journal of Combinatorial Optimization 29 (2015), 88--124, DOI:10.1007/s10878-013-9682-0.
