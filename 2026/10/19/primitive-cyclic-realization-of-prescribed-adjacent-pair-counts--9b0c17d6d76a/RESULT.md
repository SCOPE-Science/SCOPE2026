# Primitive cyclic realization of prescribed adjacent-pair counts

## Finding
Let \(\Sigma\) be a labeled alphabet of cardinality \(q\ge 1\), and let \(M=(m_{ab})_{a,b\in\Sigma}\) be a nonnegative integral matrix whose entries sum to \(n\ge1\). A cyclic word \(w=w_0\cdots w_{n-1}\) realizes \(M\) when
\[
m_{ab}=\#\{i\in\{0,\ldots,n-1\}:w_i=a,\ w_{(i+1)\bmod n}=b\}.
\]
Its cyclic period is *primitive* if the linear word \(w\) is not a proper integer power of a shorter word (equivalently, if the orbit under cyclic rotation has size \(n\)).

**Theorem.** Suppose \(M\) is realizable. Then \(M\) has a primitive realizing word **unless** its positive-entry support consists of a single directed simple cycle through \(d\) distinct alphabet symbols, with every cycle arc appearing with one common multiplicity \(r\ge2\). The case \(d=1\) is a loop; zero-frequency symbols are immaterial. In that exceptional case every realization is the same cyclic \(d\)-word repeated \(r\) times and hence is nonprimitive. If the support is a single directed cycle with multiplicity \(r=1\), its realization is primitive.

Equivalently, for any realizable \(M\), branching at even one used symbol (at least two distinct outgoing successor symbols) guarantees a primitive realization, irrespective of the common divisors of the entries of \(M\).

**Exact count.** Among all realizable length-\(n\) adjacent-pair matrices on a fixed labeled \(q\)-letter alphabet, the number \(H_q(n)\) for which **no** primitive cyclic realization exists is exactly
\[
\boxed{H_q(n)=\sum_{\substack{d\mid n\\1\le d<n,\ d\le q}}\binom qd(d-1)!.}
\]
The sum is empty, hence zero, for \(n=1\). In particular \(H_q(p)=q\) for each prime \(p\) and \(q\ge1\), and for fixed \(q\) the obstruction count is bounded uniformly in \(n\). This counts **frequency profiles**, not words or necklaces.

## Assumptions and scope
An active vertex is a symbol having positive incident arc multiplicity. A matrix is *realizable* if and only if its active support graph is weakly connected and every row sum equals the corresponding column sum. Isolated inactive vertices are permitted. This is the directed Eulerian-circuit criterion, including loops and parallel arcs. The theorem concerns a *finite circular word with prescribed ordered pairs*; graph-theoretic aperiodicity (gcd of closed-walk lengths) is a different notion and is not assumed. Multiplicities label indistinguishable occurrences of ordered symbol pairs, not separately identifiable edges.

## Proof
**1. Feasibility and the unbranched case.** Associate \(m_{ab}\) directed arcs from symbol \(a\) to \(b\). A circular realization traverses every arc once, so conservation and connectedness are necessary, and the Eulerian-circuit theorem makes them sufficient. In a finite weakly connected balanced directed graph, all active vertices are strongly connected: otherwise its acyclic condensation has a source component with a positive outgoing cut and no incoming cut, contradicting conservation.

Suppose each active vertex has exactly one distinct outgoing successor. Strong connectivity implies that these successor arrows form a directed simple cycle using all active symbols, including the one-vertex loop case. Conservation at successive vertices forces all cycle-arc multiplicities to equal an integer \(r\ge1\). Every circular realization therefore follows the same \(d\) successors, repeated \(r\) times; its least period is \(d\). It is primitive precisely when \(r=1\).

**2. Excursion factorization when there is branching.** Otherwise choose an active vertex \(v\) with two distinct successor symbols. Take any Eulerian circuit, start it at \(v\), and cut the circuit at **every** visit to \(v\). This gives a nonempty list of first-return excursions \(E_1,\ldots,E_s\), each a directed walk starting and ending at \(v\) and having no internal occurrence of \(v\). Regard the full vertex sequence of each excursion as its *type*. There are at least two excursion types: the first symbol after \(v\) distinguishes excursions departing via different successors.

Each excursion can be permuted freely relative to all other excursions because each starts and ends at \(v\); concatenation still traverses exactly the same multiset of arcs. Sort the excursions by their complete type (any fixed total order), and concatenate them, identifying each terminal \(v\) with the next starting \(v\). This produces a cyclic word \(w\) realizing exactly \(M\).

**3. Primitivity.** In the sorted excursion-type sequence, each distinct type appears in exactly one nonempty consecutive block, and at least two distinct types appear. This cyclic type sequence is primitive: were it a nontrivial power, its repeating root would either use just one type, contradicting the presence of two types, or contain at least two types, forcing every root type to form at least two disjoint cyclic blocks in the repeated sequence, a contradiction.

If the constructed cyclic symbol word \(w\) had a proper period \(t<n\), rotation by \(t\) would preserve all symbols, hence the set of occurrences of \(v\). It would induce a nonidentity rotation of the cyclic list of first-return excursions; because those excursions have no internal \(v\), this rotation must preserve their type sequence. It would give a proper cyclic period of that type sequence, contradicting the preceding paragraph. Thus \(w\) is primitive.

**4. Counting exceptional matrices.** Let \(d\) be the number of active symbols in an exceptional matrix. Necessarily \(d\mid n\), \(d<n\), and \(d\le q\), and the common arc multiplicity is forced to be \(r=n/d\ge2\). Choose the \(d\) active symbols in \(\binom qd\) ways and a directed simple cycle through them in \((d-1)!\) ways (one loop when \(d=1\)). The resulting matrices are distinct, every one is feasible and exceptional, and no matrix is counted at two different \(d\). Summation proves the formula. For prime \(n\), only \(d=1\) contributes; there are \(q\) possible singleton loops. The total over all \(d\le q\) bounds the count independently of \(n\). \(\square\)

## Verification
The independent enumeration program `verify.py` enumerates every word for alphabet sizes \(q=1,2,3,4\), with maximal lengths \(8,11,10,8\), respectively. It computes each cyclic pair-count matrix, classifies whether at least one realizing word is primitive using direct period testing, independently constructs an Eulerian circuit followed by sorted first-return excursions, and compares the predicted exceptional count with the exact divisor sum for every tested \((q,n)\). In particular there are \(95\) ternary profiles of length \(6\), precisely \(8\) of which force periodicity; there are \(3317\) quaternary profiles of length \(8\), precisely \(16\) of which force periodicity. The proof above applies to all \(q,n\), not only to enumerated cases. Run: `python3 verify.py` (Python standard library only).

The phenomenon is not simply the gcd of the entries: the two-letter matrix with all four entries equal to \(2\) admits the primitive word `00010111` of length \(8\). Both diagonal and off-diagonal ordered-pair counts then equal \(2\).

## Relationship to prior work
Jacquet, Knessl, and Szpankowski study cyclic first-order Markov types as connected Eulerian frequency matrices and enumerate their total number and asymptotics. Their type-counting and balance criteria establish the ambient objects, but do not provide an all-alphabet criterion for when a given type class contains a **primitive** cyclic word or count the classes that contain none. Obscura Acosta and Tomescu characterize Eulerian graphs with a unique **edge-distinguished Eulerian circuit** and safe traversed walks. Their uniqueness result does not imply primitive realizability of **vertex-labeled circular words** with indistinguishable repeated arcs; in particular, a multigraph can have multiple edge-distinguished Euler tours but only one periodic symbol necklace. Results on generalized de Bruijn words and invertible necklaces use additional overlap and Burrows–Wheeler conditions, not prescribed arbitrary order-two transition matrices.

The present exact characterization and divisor-sum obstruction count are separate from general counts of Markov types or Eulerian circuits. Neither total type counts nor edge-tour counts alone identify which individual type classes have an aperiodic necklace.

## Limitations
This concerns **existence** of at least one primitive realization, not a count of primitive words in an arbitrary class, uniqueness of reconstruction, higher-order factor profiles, or an arbitrary supplied word's least period. The proof assumes exact nonnegative integer transition counts, exact circular adjacency, and a finite labeled alphabet. It does not extend automatically to linear words with unconstrained endpoints or to constraints on words beyond adjacent-pair counts. The assertion of novelty is restricted to literature actually examined; equivalent historical or unindexed formulations may exist. No independent mathematical audit has been performed.

## References
1. P. Jacquet, C. Knessl, and W. Szpankowski, *Counting Markov Types, Balanced Matrices, and Eulerian Graphs*, IEEE Transactions on Information Theory **58** (2012), 4261–4272. DOI: `10.1109/TIT.2012.2191476`.
2. N. Obscura Acosta and A. I. Tomescu, *Simplicity in Eulerian Circuits: Uniqueness and Safety*, arXiv:2208.08522, initially public 17 August 2022; Information Processing Letters **183** (2024), 106421. DOI: `10.1016/j.ipl.2023.106421`.
3. *Generalized De Bruijn Words, Invertible Necklaces, and the Burrows–Wheeler Transform*, MFCS 2025, LIPIcs **345**, article 48. DOI: `10.4230/LIPIcs.MFCS.2025.48`.
