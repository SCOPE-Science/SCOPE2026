# Complete noncoprime image spectra for cyclic defect-one automata

## Finding
For integers \(n\ge4\) and \(1\le d<n\) with \(g=\gcd(n,d)\ge2\), consider the complete deterministic automaton on \(Q=\mathbb Z/n\mathbb Z\) with transition letters \(a:i\mapsto i+1\pmod n\) and \(b:0\mapsto d\), with \(b(i)=i\) for \(i\ne0\). Put \(m=n/g\). Its family of images of \(Q\) under arbitrary input words is **exactly**
\[
\mathcal I_{n,d}=\{S\subseteq Q:S\cap(r+g\mathbb Z/n\mathbb Z)\ne\varnothing\text{ for all }0\le r<g\}.
\]
Thus its exact rank enumerator, counting **different image subsets** once each, is
\[
F_{n,d}(z)=\sum_{S\in\mathcal I_{n,d}}z^{|S|}=\big((1+z)^m-1\big)^g,
\qquad |\mathcal I_{n,d}|=(2^m-1)^g.
\]
The minimum attainable image rank is precisely \(g\), so this strongly connected circular automaton is not synchronizing. Each rank \(g,g+1,\ldots,n\) occurs. In particular, the number of reachable \(k\)-subsets is
\[
[z^k]F_{n,d}(z)=\sum_{t=0}^g(-1)^t\binom gt\binom{n-tm}{k},
\]
where \(\binom{x}{k}=0\) when \(x<k\).

More precisely, for any reachable target \(S\), set \(H=Q\setminus S\) and \(h=|H|\). Decompose \(H\) into its maximal directed paths under the directed successor map \(j\mapsto j+d\pmod n\), obtaining path lengths \(\ell_1,\ldots,\ell_t\). Write \(E_j=a^{n-j}ba^j\) for \(j\in\{0,\ldots,n-1\}\). There are **exactly**
\[
\frac{h!}{\ell_1!\cdots\ell_t!}
\]
orderings of the distinct macros \(E_j\), \(j\in H\), that all strictly lower image rank at their applications and finish with image \(S\). Each has exactly \(h\) occurrences of the rank-deficient letter \(b\), and no input word reaching \(S\) can use fewer than \(h\) such occurrences. For \(H=\varnothing\), the quotient is \(1\).

## Assumptions and scope
The alphabet consists exactly of the two transformations \(a,b\); the image of a word is its action on the full state set, not the image from one initial state. The displacement \(d\) is chosen in \(\{1,\ldots,n-1\}\) and is noncoprime to \(n\). The counted image subsets are labelled subsets, not transformation functions or words. The macro count is for all rank-reducing orderings of the explicitly defined \(E_j\) with each missing vertex used exactly once; it is **not** a count of all automaton words having minimum possible numbers of \(b\)'s.

## Proof
**Invariant.** The \(g\) residue classes modulo \(g\) are the cycles of \(T(j)=j+d\pmod n\), each with \(m\) members. Letter \(a\) permutes these classes bijectively; letter \(b\) moves one state only inside its own residue class and fixes all other states. An image that meets all residue classes remains such after either letter, proving necessity by induction from \(Q\).

**Sufficiency and optimality.** Since \(a^n\) is the identity, direct evaluation gives \(E_j(j)=j+d\pmod n\) and \(E_j(i)=i\) for all \(i\ne j\). Because \(S\) meets every \(T\)-cycle, the restriction of directed edges \(j\to T(j)\) to the deleted vertices \(H\) consists of vertex-disjoint directed paths (possibly empty). On each path delete vertices in directed order, and interleave different paths arbitrarily. At the moment vertex \(j\) is deleted, both \(j\) and \(T(j)\) belong to the current image: \(T(j)\) is either a later deleted vertex or a permanent survivor. Hence \(E_j\) deletes \(j\) without introducing new states, decreases rank exactly once, and does not disturb other vertices. After every vertex of \(H\) is deleted the image is \(S\), proving sufficiency.

Any word reaching \(S\) must reduce the initial rank \(n\) to \(|S|\). Letter \(a\) never changes image cardinality and any occurrence of \(b\) reduces it by at most one, so at least \(h=n-|S|\) occurrences of \(b\) are necessary. The displayed sequence of \(E_j\) has exactly one occurrence of \(b\) per deleted vertex, attaining this lower bound.

**Exact macro-order count.** For a sequence containing every \(E_j\), \(j\in H\), once, to decrease rank at every step, vertex \(j\) must still be present and its successor \(T(j)\) must still be present when \(E_j\) acts. Consequently, whenever both \(j\) and \(T(j)\) are in \(H\), \(j\) must precede \(T(j)\). These are the only restrictions: following them leaves all successors present, as shown above. Hence valid sequences are exactly the linear extensions of disjoint chains of lengths \(\ell_1,\ldots,\ell_t\). Interleaving the fixed internal order of each chain yields exactly \(h!/(\ell_1!\cdots\ell_t!)\) sequences.

**Enumeration.** Every class independently contributes a nonempty subset of \(m\) labelled elements, with generating polynomial \((1+z)^m-1\). Multiplication over the \(g\) classes proves \(F_{n,d}(z)\). Evaluating at \(z=1\), taking its lowest nonzero degree, and expanding using binomial inclusion–exclusion yield respectively the total count, minimum rank, and coefficient formula. Every intermediate degree occurs by first taking one element per class and adding arbitrary other vertices.

## Verification
A standalone Python 3 standard-library checker (`verify.py`) independently enumerates the complete subset-power-automaton graph, using the literal transitions of letters \(a,b\), and compares every reachable subset against the claimed residue-class characterization for all \(2\le n\le12\) and all \(0\le d<n\); it checks the rank polynomial coefficients separately. It checks \(77\) parameter pairs and \(90{,}112\) candidate subsets (including the boundary regimes outside the theorem). An independent recursion counts valid contraction orders and matches the chain-multinomial formula on \(6{,}496\) reachable target cases for \(n\le9\). The recorded output is in `check_output.txt`.

For \(n=10,d=4\), \(g=2,m=5\), there are exactly \((2^5-1)^2=961\) distinct reachable image subsets. For target \(S=\{0,1\}\), its missing vertices form two directed paths of length \(4\), yielding \(\binom84=70\) optimal contraction-macro orders.

## Relationship to prior work
The 2026 survey *Synchronizing Automata: Open Problems* by Szykuła (arXiv:2608.24245) motivates exact image and subset reachability questions. Don's Proposition 15 in *The Černý Conjecture and 1-Contracting Automata* (2016) treats the **coprime displacement** case and obtains all nonempty subsets plus length bounds, but does not assert the present noncoprime reachable-subset spectrum. Hoffmann's *State Complexity of the Set of Synchronizing Words for Circular Automata and Automata over Binary Alphabets* (2020) studies complete reachability and distinguishability; its necessary and sufficient criteria for full reachability do not enumerate reachable images when the automaton is **not** synchronizing. Casas and Volkov's *Binary Completely Reachable Automata* (2022) proves a subgroup-invariance obstruction for full reachability (Proposition 1), but does not give the exact image family or rank polynomial when the obstruction holds. Ferens and Szykuła's *Recognizing Completely Reachable Automata in Quadratic Time* (2026; earliest arXiv version 2022) supplies general complete-reachability algorithms and bounds, not this exact noncoprime rank distribution. The theorem is about the noncoprime phase, rather than a restatement of the known coprime case.

## Limitations
The theorem concerns one cyclic permutation letter together with a **simple idempotent** rank-deficient letter, and cannot be extended merely by replacing the letter with an arbitrary map of rank \(n-1\). No claim is made about all transformation functions in the generated monoid, the shortest input-word length, all minimal-\(b\) words, or arbitrary automata. Finite verification is supplementary; the proof establishes the infinite parameter family. Exact literature priority remains subject to independently inspecting any previously unindexed semigroup result.

## References
1. Marek Szykuła, *Synchronizing Automata: Open Problems*, arXiv:2608.24245 (first posted 2026-08-25).
2. Henk Don, *The Černý Conjecture and 1-Contracting Automata*, Electronic Journal of Combinatorics 23(3), #P3.12 (2016), DOI:10.37236/5616.
3. Stefan Hoffmann, *State Complexity of the Set of Synchronizing Words for Circular Automata and Automata over Binary Alphabets*, arXiv:2011.14404 (2020).
4. David Casas and Mikhail V. Volkov, *Binary Completely Reachable Automata*, arXiv:2205.09404 (2022).
5. Robert Ferens and Marek Szykuła, *Recognizing Completely Reachable Automata in Quadratic Time*, ACM Transactions on Algorithms 22(2) (2026), DOI:10.1145/3798283 (earliest public preprint 2022).
