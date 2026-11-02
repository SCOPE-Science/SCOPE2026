# Four-point VC complexity and the first online entropy obstruction in two-defect Dyck paths

## Finding
Let \(\mathcal P_n\), for integer \(n\ge3\), consist of the Dyck words of semilength \(n\) that have exactly \(n-2\) peaks. View each word as a Boolean hypothesis on the \(2n\) step positions, with label one on an upstep and zero on a downstep. Then
\[
\operatorname{VCdim}(\mathcal P_n)=4\qquad(n\ge6).
\]
The initial exact dimensions, including the exceptional sizes, are:

| \(n\) | Number of hypotheses | VC dimension | Littlestone dimension | \(\lfloor\log_2|\mathcal P_n|\rfloor\) |
|---:|---:|---:|---:|---:|
| 3 | 1 | 0 | 0 | 0 |
| 4 | 6 | 2 | 2 | 2 |
| 5 | 20 | 3 | 4 | 4 |
| 6 | 50 | 4 | 5 | 5 |
| 7 | 105 | 4 | 6 | 6 |
| 8 | 196 | 4 | 7 | 7 |
| 9 | 336 | 4 | 7 | 8 |
| 10 | 540 | 4 | 8 | 9 |
| 11 | 825 | 4 | 8 | 9 |

In this natural fixed-peak Narayana layer, semilength nine is the first failure of the concept-count upper bound for adaptive shattering. At semilength ten the adaptive-minus-static dimension gap is four. The Littlestone dimension is unbounded as \(n\) increases, even though the VC dimension remains four.

## Assumptions and scope
A Dyck word is a string in \(\{U,D\}^{2n}\) with exactly \(n\) occurrences of each letter and nonnegative height of every prefix, where \(U\) increases and \(D\) decreases the height. A peak is an adjacent subword \(UD\). A query names a single step position \(i\in\{1,\ldots,2n\}\). Static shattering requires all assignments on a fixed support; a complete adaptive tree of depth \(d\) has a possibly different step-position query at each internal node, with all \(2^d\) branch sequences realized. The theorem concerns this binary position-query class, not queries about heights or interval containment of the path.

The class size is the classical Narayana count
\[
|\mathcal P_n|=\frac1n\binom n2\binom n3
=\frac{n(n-1)^2(n-2)}{12}.
\]

## Proof
**General upper bound on VC dimension.** Let \(a=UDUD\cdots UD\) be the alternating Dyck word of semilength \(n\). For each \(w\in\mathcal P_n\), define its mismatch vector \(e_i=1\) when \(w_i\ne a_i\), and \(e_i=0\) otherwise. The number of equal adjacent letter pairs in \(w\) is \(2n-2(n-2)=4\), because a word with \(k\) peaks has \(k\) up-runs and \(k\) down-runs. Since the reference word alternates, \(e_i\ne e_{i+1}\) precisely at such equal adjacent pairs. Also \(e_1=e_{2n}=0\). Thus the support of \(e\) is a union of exactly two nonempty disjoint intervals of step positions. The family of unions of at most two intervals on a line has VC dimension at most four: among any five increasing query points, the alternating pattern \(1,0,1,0,1\) needs three positive runs. Coordinatewise label complementation by the fixed word \(a\) preserves shattering, so \(\operatorname{VCdim}(\mathcal P_n)\le4\).

**Attainment at all semilengths at least six.** At \(n=6\), the four step positions \(2,4,7,8\) are shattered. The sixteen exact labeled realizations are reproduced by `VERIFY.py`, with a witness for every four-letter output pattern obtained from the exhaustive list of 50 valid paths. For each \(n>6\), concatenate a six-semilength witness with \((UD)^{n-6}\). This preserves the first twelve step labels, adds exactly \(n-6\) peaks, and gives a member of \(\mathcal P_n\); hence all sixteen patterns remain represented. Together with the upper bound this proves the all-size VC assertion. (Here concatenation is literal word concatenation.)

**Finite adaptive dimensions.** For a finite nonempty set \(H\) of distinct hypotheses define \(W(H,0)=\mathrm{true}\). For \(d\ge1\), put
\[
W(H,d)\iff\exists i\;[W(H_{i,0},d-1)\wedge W(H_{i,1},d-1)],
\]
where \(H_{i,b}\) is the subset of hypotheses with step-position \(i\) labeled \(b\). Empty sets fail at depth zero. This is an equivalence by induction on \(d\): the first node of a complete tree must choose such a coordinate, and the two subtrees must be complete of depth \(d-1\). Any state with fewer than \(2^d\) distinct hypotheses is necessarily false. `VERIFY.py` enumerates every Dyck word and every possible coordinate split of each recursively occurring state, memoizes the recursion, and computes the table without probabilistic search or early cutoff. `ALT_CHECK.py` checks the decisive depth-eight and depth-nine obstructions using a separate literal-set representation. Explicit complete witness trees for \(n=8,9,10,11\) are supplied in `certificates.json`, with 128, 128, 256, 256 distinct leaf witnesses respectively. The special VC values at \(n=3,4,5\) are established by exhaustive fixed-support enumeration.

**Unbounded online dimension.** For any \(m\ge2\), the Dyck words with exactly \(m-1\) peaks are obtained uniquely from \((UD)^m\) by complementing an interval of positions \([2a,2b-1]\) for \(1\le a<b\le m\); each such word is Dyck. At the even positions \(2j\), these represent all nonempty interval indicators on the ordered set \(\{1,\ldots,m-1\}\), up to a fixed label complement. Restricting to intervals of the form \([a,m-1]\) gives \(m-1\) different threshold hypotheses; balanced binary splitting yields a complete online-shattering tree of depth \(\lfloor\log_2(m-1)\rfloor\). Prefixing every word by the fixed Dyck block \(UUDD\) gives a subset of \(\mathcal P_{m+2}\). Consequently, for \(n\ge4\),
\[
\operatorname{Ldim}(\mathcal P_n)\ge\lfloor\log_2(n-3)\rfloor,
\]
so the online dimension is unbounded with \(n\), notwithstanding the uniform VC bound.

## Verification
Run `python3 VERIFY.py` in the directory containing `certificates.json`, then `python3 ALT_CHECK.py`. Both use only the Python standard library. The first program generates all words directly from the Dyck prefix condition; independently checks Narayana counts and peak counts; checks static supports for \(n\le6\); applies the exact complete-tree recurrence through \(n=11\); and validates every query and root-to-leaf witness in the four supplied adaptive trees. The second program independently performs the decisive adaptive upper-bound tests at \(n=9,10,11\) by literal word subsets rather than integer bitmasks. The literal recursion also cross-checks all small dimensions. No untested extrapolation is used for the finite table.

## Relationship to prior work
The classical Narayana enumeration fixes the concept counts but not the query-shattering dimensions. Chase and Freitag (2018) explain the correspondence between Littlestone/thicket dimension and model-theoretic stability and give the complete-tree definition; they do not compute these Dyck-word dimensions. Shigechi (first arXiv version 2024) studies Catalan objects, Dyck paths, and peak/valley statistics, but not their Boolean position-query VC or Littlestone dimensions. The standard union-of-two-intervals VC bound supplies only the upper bound in the proof; the exact Narayana-slice lower construction and adaptive obstruction do not follow from knowing the unrestricted interval class. The finite upper bounds rely on exhaustive computation; their historical priority remains open to further scholarly inspection.

## Limitations
The exact Littlestone table ends at semilength eleven; no closed formula for all sizes is asserted. A logarithmic lower bound establishes qualitative unboundedness, not the asymptotically exact growth rate. The large finite upper bounds have transparent exact recurrences and two implementations, but the calculations are computational certificates, not hand-enumerated derivations. Literature searching cannot prove historical uniqueness, and independent scientific validation has not been conducted.

## References
- H. Chase and J. Freitag, *Model Theory and Machine Learning*, arXiv:1801.06566, first public version 2018-01-19; *Bulletin of Symbolic Logic* 25 (2019).
- N. Alon, R. Livni, M. Malliaris, and S. Moran, *Private PAC learning implies finite Littlestone dimension*, arXiv:1806.00949, first public version 2018-06-04.
- K. Shigechi, *Major Index on Catalan Combinatorics*, arXiv:2407.17168v1, first public version 2024-07-24, sections 2 and 4.
- S. Cambie, A. Girão, and R. J. Kang, *VC Dimension and a Union Theorem for Set Systems*, *Electronic Journal of Combinatorics* 26 (2019), P3.24, DOI:10.37236/8288.
