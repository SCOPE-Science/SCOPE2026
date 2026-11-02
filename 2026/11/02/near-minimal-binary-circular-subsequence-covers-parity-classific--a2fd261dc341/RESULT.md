# Near-minimal binary circular subsequence covers: parity classification and exact orbit counts

## Finding

For every integer \(k\geq1\), a labeled binary word of length \(n=2k+1\) is **circularly \(k\)-universal** if some cyclic rotation contains every binary length-\(k\) word as a scattered subsequence. Let the *equal-adjacency edges* of such a word be the cyclic edges whose endpoint symbols agree. These edges partition the remaining unequal-adjacency edges into paths; let \(\ell_1,\ldots,\ell_r\) be the numbers of unequal edges in the paths, read cyclically, including zero-length paths.

**Characterization.** The word is circularly \(k\)-universal if and only if precisely one of \(\ell_1,\ldots,\ell_r\) is even.

**Exact enumerations.** For every \(k\geq1\), the numbers of admissible labeled words, cyclic-rotation orbits (necklaces), and rotation-and-reversal orbits (bracelets) are, respectively,

\[
L_k=(2k+1)2^k,\qquad N_k=2^k,\qquad B_k=2^{k-1}+2^{\lfloor k/2\rfloor}.
\]

Every admissible word has \(k\) copies of one binary symbol and \(k+1\) of the other; hence every admissible necklace is primitive, with exactly \(2k+1\) labeled rotations. Membership is decidable in time linear in the word length by scanning equal-adjacency edges and counting the even path lengths. Length \(2k\) is the absolute minimum for binary \(k\)-universality. Thus the result enumerates the first full length level beyond that minimum.

## Assumptions and scope

The alphabet is the *labeled* binary alphabet \(\{0,1\}\). Scattered subsequences preserve symbol order but need not use adjacent positions. Circular universality uses **one rotation for all requested target words**, not a target-dependent rotation. A labeled word distinguishes its cyclic starting position. Necklace equivalence permits rotations only; bracelet equivalence permits rotations and reversal, but does not identify symbols under complement. All assertions concern every integer \(k\geq1\) and words of length exactly \(2k+1\); no asymptotic approximation is used.

## Proof

**1. Matching lemma for linear binary words.** A binary linear word is \(k\)-universal precisely when it contains \(k\) pairwise vertex-disjoint adjacent unequal-symbol pairs. Indeed, \(k\) such pairs suffice: choose from each pair whichever binary symbol is required in the corresponding position of an arbitrary target. Conversely, greedily partition a \(k\)-universal word into shortest successive blocks containing both symbols. There are at least \(k\) complete blocks: if there were only \(t<k\), take the last letter of each of these \(t\) shortest complete blocks, followed by a symbol absent from the remaining incomplete suffix. Greedy subsequence matching is forced to reach each chosen last letter precisely at its arch boundary; it then cannot match the last chosen symbol, so this target of length \(t+1\), and every extension to length \(k\), is absent. Every complete binary block contains an adjacent unequal pair, and the complete blocks are disjoint. This proves the equivalence. Alternatively, it is the binary specialization of the arch-factorization universality criterion.

**2. Cyclic matching and parity.** Put the \(2k+1\) letter positions at vertices of a cycle; retain just those cycle edges with unequal endpoint symbols. A rotation is linearly \(k\)-universal exactly when the retained-edge graph has a matching of size \(k\). For the converse direction, such a matching leaves one vertex unmatched; cut the circle on an edge incident with that vertex, so all matching edges remain consecutive pairs in the resulting linear word. Equal-adjacency edges remove the cycle into \(r\) paths with \(\ell_i+1\) vertices each. A path of \(\ell_i+1\) vertices has maximum matching size \(\lfloor(\ell_i+1)/2\rfloor\), so the maximum retained matching has size

\[
\sum_{i=1}^{r}\left\lfloor\frac{\ell_i+1}{2}\right\rfloor
=\frac{2k+1-E}{2},\qquad E=\#\{i:\ell_i\text{ is even}\}.
\]

The equal-edge set is nonempty because a binary coloring cannot alternate around an odd cycle. Consequently the matching has size \(k\) if and only if \(E=1\), establishing the characterization (including isolated single-vertex paths).

**3. Labeled count.** The number of unequal cyclic edges of any binary coloring is even, hence \(r\), the number of equal edges, is odd. Write \(r=2s+1\). For \(E=1\), the unique even path length is \(2a\), and all the others have lengths \(2b_j+1\), where \(a,b_j\geq0\). Since the total number of unequal edges is \(2k+1-r\), these parameters satisfy

\[
a+\sum_j b_j=k-2s.
\]

Thus \(0\leq s\leq\lfloor k/2\rfloor\), and choosing the even-path position within an ordered list of the \(r\) path lengths gives \(r\binom{k}{2s}\) valid lists by stars and bars. Marking an initial equal edge in the labeled cycle provides \(n=2k+1\) choices, but each equal-edge set is then counted \(r\) times, once for each possible marked equal edge. There are therefore \(n\binom{k}{2s}\) labeled equal-edge sets with this value of \(r\). Each set specifies all cyclic equality/inequality relations and has exactly two binary colorings, exchanged by bit complement, because the number of inequality edges is even. Summing yields

\[
L_k=2(2k+1)\sum_{s=0}^{\lfloor k/2\rfloor}\binom{k}{2s}
=(2k+1)2^k.
\]

**4. Rotation orbits.** The \(k\) matched unequal pairs contribute exactly \(k\) zeros and \(k\) ones, leaving one unmatched symbol. Thus every admitted word has symbol multiplicities \(k\) and \(k+1\). A word with a proper rotational period must repeat a shorter block at least twice, forcing a common divisor greater than one of both symbol multiplicities. Since \(\gcd(k,k+1)=1\), that is impossible. Hence every rotation orbit has size \(2k+1\), and \(N_k=L_k/(2k+1)=2^k\).

**5. Reversal orbits.** Consider any fixed reflection of the odd labeled cycle. It fixes one vertex and the edge opposite that vertex. The opposite edge must be an equal edge. All other equal edges occur in reflected pairs; each of the \(k\) edge positions on one semicircle has a unique reflected partner. The path containing the fixed vertex has even length automatically. To ensure it is the **only** even-length path, every intervening path between consecutive equal edges on either semicircle must have odd length. Equivalently, moving outward from the fixed opposite edge, paired equal edges may occur only at even edge distances \(2,4,\ldots,2\lfloor k/2\rfloor\). Those \(\lfloor k/2\rfloor\) distances can be chosen independently, yielding \(2^{\lfloor k/2\rfloor}\) admissible reflected equal-edge patterns. Each pattern yields precisely two colorings, both reflection-invariant because the reflection fixes a vertex and preserves the edge equalities. Therefore one prescribed reflection fixes \(2^{\lfloor k/2\rfloor+1}\) admitted labeled words.

As all admitted words are primitive, each self-reversing necklace has exactly one representative fixed by a prescribed reflection. Thus reversal fixes \(2^{\lfloor k/2\rfloor+1}\) of the \(2^k\) admitted necklaces. Burnside's lemma for the two-element reversal action gives

\[
B_k=\frac{2^k+2^{\lfloor k/2\rfloor+1}}{2}
=2^{k-1}+2^{\lfloor k/2\rfloor}.
\]

For \(k=1\) this gives the six nonconstant labeled words, two necklaces, and two bracelets, consistent with every step. Length \(2k\) is the sharp minimum, since \(k\) disjoint unequal pairs require at least \(2k\) positions, and the alternating word realizes that minimum. The claim does not enumerate all minimizers at length \(2k\).

## Verification

A standalone standard-library Python implementation in `verify.py` performs independent comparisons between the cyclic equal-edge parity criterion and greedy linear arch factorization over every binary word of lengths \(3,5,\ldots,17\) (\(174{,}760\) words). For lengths \(3,5,7,9\), a further checker explicitly enumerates scattered subsequences of every rotation (\(680\) words). For all tested lengths it independently tallies labeled words, rotation orbits, reversal orbits, fixed-reflection words, and verifies primitive necklaces. The script prints `VERIFY_OK` on success. The exhaustive finite checks corroborate, but do not replace, the combinatorial proof for all \(k\).

For \(k=1,2,3,4,5\), labeled totals are \(6,20,56,144,352\), necklace totals are \(2,4,8,16,32\), and bracelet totals are \(2,4,6,12,20\).

## Relationship to prior work

Barker–Fleischmann–Harwardt–Manea–Nowotka (2020) introduced circular scattered-factor universality and arch methods. Fleischmann–Germann–Nowotka (2021) studied its powers and arch remainders, and Schnoebelen–Veron (2023) developed algorithms for circular universality indices. The present result concerns the separate, exact **length-\(2k+1\) binary fiber**: a cyclic matching criterion together with complete labeled, necklace, and bracelet enumerations. These counts are not asserted to follow automatically from the general decision or index algorithms. Day–Fleischmann–Manea–Nowotka (2019) examined spectra for balanced binary words in another length regime.

The integer sequence \((2k+1)2^k\) is already recorded as OEIS A014480 in unrelated combinatorial contexts. No novelty is claimed for that naked sequence, only for this universality-specific structural classification and accompanying orbit interpretations. The similarity of the sequence alone is not a proof of prior coverage or of novelty.

## Limitations

The theorem treats only a labeled binary alphabet and length exactly one more than the absolute minimum for circular \(k\)-universality. It does not classify higher surplus lengths or larger alphabets. Finite verifier output is not an infinite proof. An equivalent reformulation under graph-matching, circle-coloring, or necklace terminology may have been published elsewhere; the accessible compared literature did not establish it. Independent scientific validation has not been performed.

## References

1. L. Barker, P. Fleischmann, K. Harwardt, F. Manea, D. Nowotka, *Scattered Factor-Universality of Words* (first public 2020-03-10), https://arxiv.org/abs/2003.04629.
2. P. Fleischmann, S. B. Germann, D. Nowotka, *Scattered Factor Universality — The Power of the Remainder* (first public 2021-04-19), https://arxiv.org/abs/2104.09063.
3. P. Schnoebelen, J. Veron, *On arch factorization and subword universality for words and compressed words* (first public 2023-04-24), https://arxiv.org/abs/2304.11932.
4. J. D. Day, P. Fleischmann, F. Manea, D. Nowotka, *k-Spectra of weakly-c-Balanced Words* (first public 2019-04-19), https://arxiv.org/abs/1904.09125.
5. OEIS Foundation, *A014480* (a previously catalogued numerical sequence), https://oeis.org/A014480.
