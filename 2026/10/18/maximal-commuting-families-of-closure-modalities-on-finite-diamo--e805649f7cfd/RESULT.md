# Maximal commuting families of closure modalities on finite diamond lattices

## Finding
Let \(n\geq3\), and let \(M_n\) be the bounded lattice with bottom \(0\), top \(1\), and \(n\) incomparable atoms \(a_1,\ldots,a_n\). A **closure modality** here means an extensive, isotone, idempotent self-map of \(M_n\); no meet- or join-preservation is imposed. Two modalities **commute** if their functional composites agree.

The maximal (under inclusion) pairwise-commuting families of closure modalities on \(M_n\) are in canonical bijection with the subsets \(J\subseteq[n]\). There are therefore exactly \(2^n\) such families, and the family corresponding to \(J\) has size \(2^{n-|J|}+|J|+1\). Each maximal family is closed under composition, so it is also a maximal commutative submonoid of the full transformation monoid whose elements are closure modalities.

For every integer \(k\geq0\), let \(T_n(k)\) count **ordered** \(k\)-tuples of closure modalities that commute pairwise, with repeated members permitted and \(T_n(0)=1\). Then
\[
T_n(k)=\sum_{h=0}^{n}\binom nh\sum_{j=0}^{h}(-1)^{h-j}\binom hj(2^{n-h}+1+j)^k,
\]
with exponential generating function
\[
\sum_{k\geq0}T_n(k)\frac{z^k}{k!}
=\sum_{h=0}^{n}\binom nh e^{(2^{n-h}+1)z}(e^z-1)^h.
\]
In particular, the number of ordered commuting pairs is
\[
T_n(2)=4^n+(n+2)2^n+(n+1)^2.
\]
These are counts on the fixed labelled atom set; no quotient by permutations is taken.

## Assumptions and scope
Fix \(n\geq3\). The underlying order has \(0<a_i<1\) for every atom, and atoms are pairwise incomparable. We write composition in the usual right-to-left order. A collection is pairwise commuting if every pair of its members has equal composites in both orders. This is a monotone, inflationary, idempotent modal framework, not the stronger normal/additive modal-algebra convention.

For each \(S\subseteq[n]\), define \(A_S\) by \(A_S(0)=0\), \(A_S(1)=1\), and \(A_S(a_i)=a_i\) for \(i\in S\), otherwise \(A_S(a_i)=1\). For each \(i\in[n]\), let \(B_i(0)=a_i\), \(B_i(a_i)=a_i\), and \(B_i(a_j)=1\) when \(j\ne i\), with \(B_i(1)=1\). Let \(C\) be the constant-top map.

For each \(J\subseteq[n]\), put
\[
\mathcal F_J=\{A_S:J\subseteq S\subseteq[n]\}\cup\{B_j:j\in J\}\cup\{C\}.
\]

## Proof
**Normal forms.** Every closure modality fixes \(1\). If its value at \(0\) is \(0\), extensivity makes each atom map either to itself or to \(1\); these are exactly the \(A_S\). If its value at \(0\) is \(1\), isotonicity forces all elements to map to \(1\), giving \(C\). Otherwise that value is a unique atom \(a_i\). Idempotence fixes \(a_i\), and any other atom \(a_j\) must map to \(1\): its image must lie above both \(a_i\) (by isotonicity from \(0\)) and \(a_j\) (by extensivity). This gives \(B_i\). Conversely, every listed map satisfies all three axioms. Thus there are \(2^n+n+1\) modalities in all; this unrefined count and underlying classification already follow from Glück's diamond closure-system analysis and are *not* new here.

**Composition and commutation.** Direct evaluation at \(0\), the atoms, and \(1\) gives \(A_S\circ A_T=A_{S\cap T}\), \(B_i\circ B_i=B_i\), and \(B_i\circ B_j=C\) for distinct indices. The map \(C\) is absorbing under composition with every closure modality. Moreover \(A_S\circ B_i=B_i\circ A_S=B_i\) when \(i\in S\). If \(i\notin S\), then \(A_S\circ B_i=C\), whereas \((B_i\circ A_S)(0)=a_i\ne1\), so the pair fails to commute. These are all cases.

**Maximal families.** Let \(\mathcal H\) be pairwise commuting and set \(J=\{i:B_i\in\mathcal H\}\). The preceding criterion forces every \(A_S\in\mathcal H\) to contain \(J\). Thus \(\mathcal H\subseteq\mathcal F_J\). Conversely, all maps in \(\mathcal F_J\) commute pairwise, and their products remain in \(\mathcal F_J\). Any modality outside \(\mathcal F_J\) is either some \(B_i\) with \(i\notin J\), which fails to commute with \(A_J\in\mathcal F_J\), or some \(A_S\) omitting an element of \(J\), which fails to commute with a corresponding \(B_j\in\mathcal F_J\). Hence each \(\mathcal F_J\) is maximal; every maximal family is one of them, and distinct \(J\)'s give distinct families. Its stated size is immediate.

**Ordered tuples.** In a mutually commuting ordered \(k\)-tuple, let \(J\) be exactly the set of indices of the \(B_i\) that occur, and put \(h=|J|\). The allowed entries are then \(C\), the \(2^{n-h}\) maps \(A_S\) with \(S\supseteq J\), and the \(h\) maps \(B_j\) indexed by \(J\), with each of the latter required to occur at least once. For a fixed \(J\), inclusion-exclusion counts these tuples by \(\sum_{j=0}^{h}(-1)^{h-j}\binom hj(2^{n-h}+1+j)^k\). Choosing \(J\) proves the formula. Summing the exponential series gives the claimed generating function. Directly splitting the ordered commuting pairs into \(A/A\), \(A/B\) and \(B/A\), \(B/B\), and pairs involving \(C\) gives \(4^n+n2^n+n^2+(2^{n+1}+2n+1)\), which simplifies to the displayed expression.

## Verification
The accompanying standalone `check.py` exhaustively generates *all* extensive self-maps of the labelled diamond, independently filters the original isotonicity and idempotence requirements, and compares with the normal forms for \(2\leq n\leq8\). It directly compares compositions for every ordered pair and verifies maximality of every \(\mathcal F_J\). An independent recursion over the actual commutation graph checks the ordered-tuple formula at \((n,k)=(2,3),(2,4),(3,3),(3,4),(4,3),(4,4),(5,3),(6,3)\). It also checks the empty-tuple case. Run with `python3 check.py`, which prints `VERIFY_OK` and `TUPLES_VERIFY_OK` if every assertion succeeds. Finite tests corroborate but do not replace the proof for arbitrary \(n,k\).

For orientation, the counts of modalities, commuting pairs, and commuting triples for \(n=3,4,5,6\) are respectively \((12,120,1080)\), \((21,377,6237)\), \((38,1284,41192)\), and \((71,4657,296567)\).

## Relationship to prior work
Glück's *Isolated Suborders and their Application to Counting Closure Operators* (2023 preprint; 2024 journal paper), Definition 3.1 and Lemma 7.4, gives the closure-system principle and the unrefined diamond count \(2^n+n+1\). The present claim is **not** that count or merely its normal form: it is the complete commutation-compatible family structure and all-arity enumeration. Grigoriev and Petrukhin (first public 2022) establish a broad monotone-modal multilattice setting, but no claim of their completeness theorems is needed for the finite calculation. Cousot and Cousot (1979) study common fixed points of commuting maps on complete lattices; those general results do not supply this diamond-specific compatibility classification and tuple enumerator.

## Limitations
The theorem counts labelled closure modalities only; it does not impose join or meet preservation, and cannot be transferred verbatim to normal modal algebras. The result is not an enumeration of arbitrary families of commuting monotone maps. No uniqueness claim against all unindexed publications is made. General composition of two noncommuting closure operators can fall outside the closure-operator class. These conclusions do not extend automatically to arbitrary finite lattices.

## References
1. R. Glück, *Isolated Suborders and their Application to Counting Closure Operators*, arXiv:2302.13081 (first preprint 2023-02-25), especially Definition 3.1 and Lemma 7.4; https://arxiv.org/abs/2302.13081 .
2. O. Grigoriev and Y. Petrukhin, *Basic modal congruent and monotonic multilattice logics*, *Journal of Logic and Computation* 33 (2023), 1379–1398 (first online 2022-04-07); https://doi.org/10.1093/logcom/exac028 .
3. P. Cousot and R. Cousot, *Constructive versions of Tarski's fixed point theorems*, *Pacific Journal of Mathematics* 82 (1979), 43–57; https://doi.org/10.2140/pjm.1979.82.43 .
