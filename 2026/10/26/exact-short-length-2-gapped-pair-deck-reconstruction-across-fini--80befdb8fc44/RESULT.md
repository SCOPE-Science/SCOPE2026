# Exact short-length \(2\)-gapped pair-deck reconstruction across finite alphabets

## Finding
Let \(\Sigma\) be any labeled alphabet of cardinality \(q\ge2\). For a word \(w=w_1\cdots w_n\), its complete \(2\)-gapped deck through subsequence length two, denoted \(\mathcal G_2(w)\), is the multiset consisting of each individual symbol \(w_i\) and every ordered pair \(w_iw_j\) with \(1\le i<j-1\le n-1\). Multiplicities matter. Let \(N_q(n)\) be the number of different such decks of words in \(\Sigma^n\).

For every integer \(q\ge2\), the exact initial spectrum is
\[
N_q(n)=\begin{cases}
q,&n=1,\\
\binom{q+1}{2},&n=2,\\
q^n,&3\le n\le5,\\
q^6-3\binom q2,&n=6,\\
q^7-10\binom q2-15\binom q3,&n=7.
\end{cases}
\]
At lengths \(3\le n\le7\), every deck fiber (the set of source words with that deck) has size one or two. There are no collisions at lengths three through five. At length six, exactly \(3\binom q2\) two-word fibers occur; each uses exactly two symbols, with three colliding pairs for every unordered pair of symbols. At length seven, exactly \(10\binom q2+15\binom q3\) two-word fibers occur: ten supported on each unordered two-symbol set, fifteen supported on each unordered three-symbol set, and none using four or more symbols.

The maximum size of a length-\(n\) code with distinct \(\mathcal G_2\)-readouts equals \(N_q(n)\): choose one source word from each fiber. In particular, the first ambiguity using three distinct alphabet symbols is at length seven, and the alphabet-uniform length-seven capacity has the exact cubic correction shown above.

## Assumptions and scope
The alphabet is a set of \(q\) distinct symbols, with no algebraic structure assumed. Words are **linear**, not circular; pairs are ordered by occurrence position, and only pairs with at least one skipped position are counted. The readout includes the complete singleton multiset. The statements concern all integer \(q\ge2\) and only lengths \(1\le n\le7\); no assertion is made for length eight or greater. At length two no pair is eligible, so the readout is only the letter composition.

## Proof
**Step 1: finite binary base.** For binary words define their signature by \(c_a=|w|_a\) and \(p_{ab}=\#\{(i,j):i+2\le j,\ w_i=a,\ w_j=b\}\), for \(a,b\in\{0,1\}\). A complete enumeration of all \(2^n\) binary words for \(1\le n\le7\) gives unique fibers for \(n=1,3,4,5\), the expected composition collision \(01\sim10\) at \(n=2\), exactly three double fibers at \(n=6\), and exactly ten double fibers at \(n=7\). The three binary length-six double fibers are

\[
\begin{gathered}
\{001101,010011\},\\
\{011001,100110\},\\
\{101100,110010\}.
\end{gathered}
\]
Each member of every binary length-six double fiber has three zeros and three ones. At length seven, each member of a binary double fiber has at least two occurrences of each binary symbol. The complete binary length-seven list is explicitly checked in the standalone verifier. This step is an **exhaustive finite computation**, not an inference from sample values. The verifier implements both the defining pair count and an independent streaming update of the signature and enumerates every possible word.

**Step 2: binary projections.** For any symbol \(a\in\Sigma\), map \(a\) to \(1\) and every other symbol to \(0\). Equal \(q\)-ary decks imply equal decks after this map, because all projected counts are sums of original counts. If two words are different, at least two different symbols have changed position sets: at a position where the words disagree, the indicator words of both the departing and arriving symbols differ. Hence, by the binary base, the projection for every changed symbol is one of the binary collision pairs.

For \(3\le n\le5\), binary deck uniqueness forces all indicator words to be equal, hence the original words are equal. For \(n=6\), every changed symbol occurs at least three times. At least two symbols change, so the six positions are exhausted by exactly two changed symbols. The complete binary list therefore gives exactly three double fibers per unordered pair of alphabet symbols; no other collisions exist.

**Step 3: reduce all length-seven alphabets to five letters.** At \(n=7\), each changed symbol occurs at least twice, by the binary length-seven list. If \(m\) different symbols change position sets, then \(2\le m\le3\). The remaining unchanged symbols occupy at most \(7-2m\) positions, so the union of all symbols used by both words has size at most \(m+(7-2m)=7-m\le5\). Thus every collision over an arbitrary alphabet is, up to an injective renaming of its used letters, already a collision over the five-symbol alphabet.

**Step 4: exhaustive five-letter finite base.** The verifier enumerates every word of length seven over alphabet \(\{0,1,2,3,4\}\) (exactly \(5^7=78125\) words). It checks the signatures by both counting methods, groups identical signatures into fibers, and checks every fiber. All collision fibers are of size two and use either exactly two symbols or exactly three symbols; there are no collisions involving four or five symbols. It also checks that for each alphabet subset of size two there are ten double fibers, and for each subset of size three there are fifteen double fibers. An exhaustive binary enumeration certifies the ten two-letter templates, and a complete ternary enumeration certifies the fifteen three-letter templates. The templates are present in the executable, with exact equality checks, not merely a log.

Any support of size two or three can be relabeled into the verified finite alphabet. By symmetry under injective symbol relabeling, each unordered pair supports ten classes and each unordered triple supports fifteen; no class is counted twice because its support is unique. Therefore the total number of double fibers at length seven is \(10\binom q2+15\binom q3\), and all other \(q^7-2(10\binom q2+15\binom q3)\) words have singleton fibers. It follows that the number of different decks is \(q^7-(10\binom q2+15\binom q3)\).

At length two each repeated-letter word is a singleton fiber and each unordered pair of distinct symbols supplies one double fiber. Together these statements establish the displayed count at every length from one through seven. The coding-capacity equality is immediate because any distinguishable family contains at most one word per fiber and a set containing one representative per fiber exists.

## Verification
Run `python3 verify_gapped_two_deck.py` with a standard Python 3 interpreter. The program exhaustively checks all \(123032\) words over alphabet sizes \(2,3,4,5\) at each length from one through seven, compares direct positional enumeration with a streaming recurrence, verifies exact binary and ternary collision lists, and asserts the fiber-size and support formulas. Its expected final output includes `GAPPED_TWO_DECK_PASS q=2..5 n=1..7 words=123032 binary6=3 binary7=10 ternary7=15 max_fiber=2`. This is a finite, complete verification within the projection-reduction proof, not an attempted infinite brute-force search.

## Relationship to prior work
Golm, Nahvi, Gabrys, and Milenkovic introduced the gapped \(k\)-deck framework and explicitly reported the binary first nondegenerate collision threshold \(G(2)=6\), including one example. That threshold and example are **previously known**. The present finding adds the complete length-six fiber census, an alphabet-uniform reconstruction-capacity formula, and especially the complete length-seven support-refined classification with exactly fifteen three-symbol collisions per alphabet triple. Its extension to all finite alphabets uses a rigorous projection-and-support reduction, not an extrapolation of ternary numerical data. The ordinary ungapped \(k\)-deck enumerations by Chrisnata and collaborators concern a different observation, as do substring multispectra in work of Gabrys and Milenkovic. No statement about the original ungapped deck is inferred from this theorem.

## Limitations
The theorem does not classify lengths eight or higher, larger pair gaps, or gapped subsequences of length three and above. The novelty comparison covers inspected accessible literature and published database searches; equivalently formulated results outside the indexed/inspected sources remain possible. The finite enumeration is exhaustive for the reduced cases, but it requires ordinary reproducible execution of the included code; no external independent audit has been performed.

## References
1. J. Golm, M. Nahvi, R. Gabrys, and O. Milenkovic, *The Gapped \(k\)-Deck Problem*, arXiv:2201.12671, first posted 2022-01-29, v2 2022-05-17, Sections I-IV and the numerical \(G(k)\) table. https://arxiv.org/html/2201.12671v2
2. J. Chrisnata, H. M. Kiah, S. R. Karingula, A. Vardy, E. Yaakobi, and H. Yao, *On the number of distinct \(k\)-decks: Enumeration and bounds*, *Advances in Mathematics of Communications* 17 (2023), 960-978, DOI 10.3934/amc.2021032; publicly available 2021-08-30. https://www.aimsciences.org/article/doi/10.3934/amc.2021032
3. R. Gabrys and O. Milenkovic, *Unique Reconstruction of Coded Strings from Multiset Substring Spectra*, arXiv:1804.04548v2, 2019. https://arxiv.org/html/1804.04548v2
