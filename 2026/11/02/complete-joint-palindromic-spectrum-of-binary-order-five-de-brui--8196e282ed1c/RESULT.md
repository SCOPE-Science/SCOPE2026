# Complete joint palindromic spectrum of binary order-five de Bruijn cycles

## Finding

Let \(\mathcal D_5\) denote the rotation classes of binary de Bruijn cycles of order \(5\). Each is a cyclic binary word of length \(32\) whose length-five circular windows are the \(32\) binary words of length five exactly once. For \(W\in\mathcal D_5\), let \(\mathcal P(W)\) be the set of all **distinct, nonempty, literal binary palindrome strings** among its circular windows of lengths \(1\) through \(32\). Define \(P(W)=|\mathcal P(W)|\) and \(L(W)=\max\{|u|:u\in\mathcal P(W)\}\). Distinct strings are counted once, irrespective of the number of starting positions.

The exact marginal distribution of \(P\) is:

| \(P(W)\) | Number of rotation classes |
| ---: | ---: |
| 22 | 32 |
| 23 | 32 |
| 24 | 200 |
| 27 | 192 |
| 28 | 920 |
| 29 | 544 |
| 30 | 128 |

No other \(P\) occurs. In particular, the sharp lower and upper bounds are \(22\) and \(30\), and the intermediate values \(25\) and \(26\) do not occur.

The exact distribution of maximum palindromic circular-factor length is:

| \(L(W)\) | Number of rotation classes |
| ---: | ---: |
| 7 | 200 |
| 8 | 192 |
| 9 | 856 |
| 10 | 128 |
| 11 | 392 |
| 12 | 32 |
| 13 | 200 |
| 15 | 48 |

All other maximum lengths are impossible, and the sharp upper bound is \(15\). The **complete joint distribution** of \((P(W),L(W))\) has exactly \(23\) supported pairs, tabulated in `joint_spectrum.tsv`. The entire lengthwise vector \((|\mathcal P(W)\cap\{0,1\}^j|)_{j=1}^{32}\) takes exactly \(51\) values, with full frequencies in `lengthwise_profiles.tsv`. The exact inventory for every canonical cycle appears in `full_census.tsv`.

## Assumptions and scope

All words are over \(\{0,1\}\). A circular window of length \(j\) starting at \(i\) is the contiguous string of length \(j\) in the periodic extension of \(W\), with \(0\le i<32\) and \(1\le j\le32\). A palindrome equals its reversal. A de Bruijn cycle is taken up to cyclic rotation, but **not** up to reversal or interchange of symbols. There is no sentinel and no extension to circular windows longer than one period.

Each order-five cycle contains all binary length-five words as windows. Hence it has precisely \(2,2,4,4,8\) distinct palindromes at lengths \(1,2,3,4,5\), respectively, for a universal subtotal of \(20\). The table classifies the additional longer palindromes and their possible coexistence.

## Proof

**Step 1: Exact finite search space and bijection.** Form the binary de Bruijn directed multigraph \(G\) with vertices the sixteen binary strings of length four. Every five-bit string \(x_1x_2x_3x_4x_5\) labels one directed edge from its first four bits to its last four bits. Each vertex has two outgoing edges. A cyclic length-32 word is an order-five de Bruijn cycle if and only if its consecutively overlapping five-bit windows list all the edges of \(G\) exactly once; thus it corresponds to a directed Euler circuit. Every such cycle has the window `00000` exactly once. Consequently rotating the circuit so the `00000` edge occurs first provides a **unique canonical representative** of its rotation class.

An exhaustive depth-first traversal begins at vertex `0000`, consumes the `00000` loop as its first edge, then chooses each next unused outgoing five-bit edge. It yields a representative only after consuming **all 32 distinct edges** and returning to vertex `0000`. This enumerates every possible Euler circuit: at each vertex all possible unused next edges are branched upon, and every valid circuit has a unique sequence of these choices after the fixed initial loop. No noncircuit or duplicate rotation class can pass. The complete traversal produces exactly \(2048\) canonical representatives, all distinct. This is also the familiar binary order-five de Bruijn cycle count, but no external counting theorem is used for the exhaustiveness certificate.

**Step 2: Exact classification of each representative.** For each representative \(W\), form the doubled word \(WW\). For each of its \(32\) starting positions \(i\) and each length \(j\in\{1,\ldots,32\}\), take the length-\(j\) window in \(WW\). Check literal equality with its reversal. Insert every passing string into a set, whose membership rule removes repeated occurrences. Counting this set gives \(P(W)\); taking its largest length gives \(L(W)\); counting members of each length gives the complete lengthwise profile. Thus each of the \(2048\) cycles requires exactly \(1024\) candidate-window decisions, with finite loops and direct palindrome tests specified in `checker.py`.

**Step 3: Exact aggregation.** The program `checker.py` executes Steps 1 and 2, constructs integer counters keyed by \(P\), by \(L\), by the pair \((P,L)\), and by all \(32\) lengthwise counts, and compares each counter with the full reference data. The complete row-by-row outcome is `full_census.tsv`. Both marginal tables above are exact sums of `joint_spectrum.tsv`, which lists all \(23\) nonzero cells and sums to \(2048\). Likewise, `lengthwise_profiles.tsv` lists all \(51\) nonzero lengthwise-vector cells and sums to \(2048\). The exhaustive bijection of Step 1 and exact-set computation of Step 2 imply there can be no omitted cycles, profiles, or lengths. This proves all displayed claims, including sharpness and impossible cases. The source and complete exact tables constitute an independently rerunnable finite certificate, not an extrapolation from sampled data.

## Verification

Run `python checker.py` with Python 3 and the three included `.tsv` tables in the same directory; only the Python standard library is needed. `generate_tables.py` regenerates all three tables directly. Beyond the Euler-circuit traversal, `checker.py` independently enumerates the same cycle set from all \(2^{16}=65536\) choices of vertex-local outgoing-edge order using Hierholzer's algorithm and checks equality of the two resulting sets. It also independently enumerates each cycle's palindromes by outward expansion from odd and even centers and checks agreement with the circular-window reversal test. Both independently computed methods agree on all \(2048\) cases. It checks that every representative has all \(32\) distinct five-bit factors and is primitive, and that all table bytes match the computations.

The result is a complete finite theorem. It makes no asymptotic claim about other de Bruijn orders. The computational proof depends on execution of the provided transparent, bounded enumerator; formal machine-independent verification beyond replay has not been performed.

## Relationship to prior work

Palindromic complexity is a standard combinatorial-word invariant. Baláži, Masáková, and Pelantová [1] studied palindromic versus factor complexity for *infinite uniformly recurrent words*; it does not directly give finite order-five circular de Bruijn spectra. Anisiu, Anisiu, and Kása [2], especially their full-text discussion of palindrome occurrence and generation from de Bruijn words, establishes relevant general combinatorial relationships, but does not state the exact \(2048\)-cycle joint histogram here. Simpson [3] establishes a general bound for palindromes in circular words, not the joint finite distribution conditional on de Bruijn uniqueness. The public record [4] tabulates unrestricted binary circular-word maxima; those maxima are for a much larger family. The classical cycle count \(2048\) appears in [5]. The present result is a special-family **joint profile census** with full exact certificates, distinct from these broader or differently quantified statements.

## Limitations

This theorem applies only to binary order-five de Bruijn cycles, up to rotation alone, with distinct literal palindrome strings and circular windows of length at most one period. It does not cover arbitrary circular words, different de Bruijn orders, occurrence multiplicities, reverse-complement palindromes, or sentinel-based transforms. The full text of Simpson [3] was unavailable to this comparison, so complete historical priority cannot be certified by the inspected record; the general upper bound alone does not imply this joint table. Independent external mathematical validation is not claimed.

## References

1. P. Baláži, Z. Masáková and E. Pelantová, *Factor versus palindromic complexity of uniformly recurrent infinite words*, arXiv:math/0603607, first publicly posted 2006-03-26. https://arxiv.org/abs/math/0603607
2. V. Anisiu, M.-C. Anisiu and Z. Kása, *Properties of palindromes in finite words*, Pure Math. Appl. 17 (2006), 183–195. https://ictp.acad.ro/anisiu/papers/2006-Anisiu-A-K-Properties.pdf
3. J. Simpson, *Palindromes in circular words*, Theor. Comput. Sci. 550 (2014), 66–78. https://doi.org/10.1016/j.tcs.2014.07.012
4. OEIS A247000, unrestricted binary circular-word maximum palindromes. https://oeis.org/A247000
5. OEIS A016031, binary de Bruijn cycle enumeration. https://oeis.org/A016031
