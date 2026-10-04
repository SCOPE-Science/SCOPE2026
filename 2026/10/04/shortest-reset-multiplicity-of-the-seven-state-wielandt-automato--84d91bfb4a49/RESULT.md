# Shortest-reset multiplicity of the seven-state Wielandt automaton \(W_7\)
## Finding
For the seven-state Wielandt automaton \(W_7\), let the states be \(1,\ldots,7\). For \(1\le i<7\), both input letters send \(i\) to \(i+1\); at state \(7\), the shortcut letter \(a\) sends \(7\) to \(2\), while \(b\) sends \(7\) to \(1\). This is the standard unique two-letter coloring of the seven-vertex Wielandt digraph, up to isomorphism and renaming of letters.

Among words of minimum reset length, define
\[
P(z)=\sum_w z^{|w|_a},
\]
where \(|w|_a\) is the number of occurrences of \(a\). Then
\[
P(z)=z^6(1+z)^{20}.
\]
Thus \(W_7\) has exactly \(2^{20}=1{,}048{,}576\) shortest reset words. Every shortest reset word has length \(31\), every one resets to state \(2\), and for each \(0\le k\le20\), exactly \(\binom{20}{k}\) shortest reset words contain \(6+k\) copies of \(a\).

## Assumptions and scope
The statement concerns exactly the seven-state automaton defined above. It does not assert the analogous polynomial for every member of the Wielandt family. The letter names are fixed so that \(a\) is the shortcut at state \(7\); exchanging the letter names exchanges the corresponding letter-count statistic.

The source introducing the family proves that the reset length of \(W_n\) is \(n^2-3n+3\), hence \(31\) at \(n=7\), and proves that a shortest reset word ends at state \(2\). The new part here is the complete shortest-word multiplicity and its \(a\)-count generating polynomial for \(W_7\).

## Proof
Represent a nonempty subset of the seven states by a seven-bit mask. A letter sends a subset to the union of the images of its states. Starting from the full set, breadth-first search in the nonempty power automaton visits at most \(2^7-1=127\) masks. The first singleton is reached at distance \(31\), and the only singleton at that distance is \({2}\).

To count all shortest paths without enumerating \(2^{31}\) words, attach to each mask \(S\) a polynomial \(F_S(z)\). Initially the full-set mask has polynomial \(1\). Whenever a shortest-path edge labelled \(b\) reaches \(T\) from \(S\), add \(F_S(z)\) to \(F_T(z)\); for an edge labelled \(a\), add \(zF_S(z)\). Processing masks in nondecreasing breadth-first distance gives the exact generating polynomial of shortest words reaching every mask. At the unique minimum-distance singleton \({2}\), this polynomial is
\[
z^6+20z^7+190z^8+1140z^9+4845z^{10}+15504z^{11}+38760z^{12}+77520z^{13}+125970z^{14}+167960z^{15}+184756z^{16}
\]
\[
+167960z^{17}+125970z^{18}+77520z^{19}+38760z^{20}+15504z^{21}+4845z^{22}+1140z^{23}+190z^{24}+20z^{25}+z^{26},
\]
which is exactly \(z^6(1+z)^{20}\).

A second calculation reverses every power-automaton edge, computes exact distance-to-\({2}\) values, retains only edges that lower that reverse distance by one, and recursively accumulates the same letter-count polynomial along this optimal-path directed acyclic graph. It returns the identical polynomial independently of the forward polynomial accumulation.

## Verification
Run `python3 verify.py`. It reconstructs the transition function from the displayed definition, checks all nonempty subsets, verifies minimum reset length \(31\), verifies that the unique minimum-distance singleton is \({2}\), and computes the polynomial by both forward and reverse routes. It also replays the classical witness \((ab^5)^5a\). The expected terminal line is:

`VERIFY_OK length=31 target=2 total=1048576 polynomial=z^6(1+z)^20 nonzero_subsets=127`

The accompanying `certificate.json` records the transition table and exact coefficient vector checked by the verifier.

## Relationship to prior work
Ananichev, Gusev, and Volkov introduced the slowly synchronizing Wielandt family in arXiv:1005.0129v1. Their Theorem 4.1 defines the unique two-letter coloring \(W_n\), proves reset length \(n^2-3n+3\), gives the witness \((ab^{n-2})^{n-2}a\), and proves that a minimum reset word ends at state \(2\). Gusev and Pribavkina later place the same family inside the more general Wielandt-type automata in arXiv:1403.3992v1 and again determine reset thresholds.

Targeted searches for the number of shortest reset words, shortest-word multiplicity, reset-language enumeration, and letter-count generating polynomials did not locate a source stating the polynomial or the count above. The closest literature determines minimum length and supplies individual witnesses rather than enumerating all minimum words.

## Limitations
This is a finite exact statement for \(W_7\). The computation is exhaustive over the complete seven-state power automaton, so it is not an extrapolation from sampled words; however, no claim is made here about a closed formula for all \(W_n\). Literature searches cannot prove absence from every unindexed source, so an unindexed prior enumeration remains a residual originality risk.

## References
1. D. S. Ananichev, V. V. Gusev, M. V. Volkov, “Slowly synchronizing automata and digraphs,” arXiv:1005.0129v1, submitted 2010-05-02; MFCS 2010, pp. 55–65.
2. V. V. Gusev, E. V. Pribavkina, “Reset thresholds of automata with two cycle lengths,” arXiv:1403.3992v1, submitted 2014-03-17.
