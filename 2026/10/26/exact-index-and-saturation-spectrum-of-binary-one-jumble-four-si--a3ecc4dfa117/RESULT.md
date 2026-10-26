# Exact index and saturation spectrum of binary one-jumble four-Simon equivalence

## Finding
Let \(\Sigma=\{0,1\}\). A pattern \(u\in\Sigma^{\le4}\) is **one-jumbled scattered in** \(w\in\Sigma^*\) when both its symbol counts do not exceed those of \(w\), and some subsequence of \(u\) obtained by deleting at most one position is an ordinary scattered subsequence of \(w\). Two words are equivalent, written \(w\equiv_{4,1}v\), when they have the same one-jumbled scattered patterns of lengths at most four.

**Theorem.** The relation \(\equiv_{4,1}\) on all binary words has exactly \(66\) classes. If \(E(n)\) counts the classes that contain a word of length \(n\), then
\[
E(n)=\begin{cases}
n+1,&0\le n\le3,\\
10,&n=4,\\
\min\{31,5n-9\},&n\ge5.
\end{cases}
\]
In particular, exactly \(31\) classes occur at every length \(n\ge8\), and \(8\) is the first such length. The complete class classification and explicit witnesses below establish both conclusions.

## Assumptions and scope
All words are finite; the empty word is allowed. Scattered subsequences preserve order but need not be contiguous. A one-jumbled occurrence requires **both** Parikh-count containment and a common subsequence of length at least \(|u|-1\); the count condition is not dropped when a position is deleted from the pattern. The empty pattern is present in every word. The equivalence is the binary \(k=4\), \(\ell=1\) instance of jumbled Simon equivalence, not ordinary Simon equivalence and not an assertion of concatenation congruence.

For \(w\) write \(i=|w|_0\), \(j=|w|_1\), and \(a=\min(i,4)\), \(b=\min(j,4)\). Let
\[
B=\{0011,0101,0110,1001,1010,1100\}
\]
be the six balanced four-letter patterns. A word's signature records all permitted patterns. Its **missing-balanced set** means the subset of \(B\) whose patterns are not one-jumbled in \(w\). The convention also applies when \(i<2\) or \(j<2\), although it is informative only when both counts are at least two.

## Proof
**Step 1 (only six potentially order-sensitive patterns).** The symbol counts of all permitted patterns are determined by the pair \((a,b)\). Any pattern of length at most three with counts available in \(w\) is automatically one-jumbled: if it is not constant, delete its minority symbol to leave a constant subsequence of length at least \(|u|-1\); if constant, use the pattern itself. For a four-letter pattern with multiplicities \((3,1)\), delete its singleton symbol, leaving a threefold constant subsequence. Four-letter constant patterns are present exactly when the corresponding symbol count is at least four. Consequently every permitted pattern except the six in \(B\) depends only on \((a,b)\), while the pair \((a,b)\) itself is recoverable from the signature using constant patterns of lengths at most four.

**Step 2 (reduce balanced-pattern membership to ordinary four-subsequences).** Assume \(i,j\ge2\). Write \(T(w)\subseteq B\) for its nonempty set of balanced *ordinary* length-four scattered subsequences. Nonemptiness follows by choosing any two occurrences of each letter. For a balanced pattern \(u\), a one-jumbled occurrence yields an ordinary length-three subsequence of \(w\) that is also in \(u\). It has two occurrences of one letter and one of the other. Since \(w\) contains at least two of each letter, an unused occurrence of its minority letter can be inserted among the three indices to obtain a balanced ordinary length-four subsequence \(t\) of \(w\). Thus \(u\) and \(t\) share an ordinary length-three subsequence. The converse is immediate. Therefore membership of \(u\) is equivalent to having a common length-three subsequence with some \(t\in T(w)\).

**Step 3 (compute all possible missing sets).** For the six possible balanced ordinary subsequences, direct comparison of their four three-letter deletion subsequences gives the following table. The second column consists of the balanced patterns \(u\) having no common length-three scattered subsequence with \(t\).

| \(t\) | Missing patterns for a singleton \(T=\{t\}\) |
|---|---|
| \(0011\) | \(\{1010,1100\}\) |
| \(0101\) | \(\{1100\}\) |
| \(0110\) | \(\{1001\}\) |
| \(1001\) | \(\{0110\}\) |
| \(1010\) | \(\{0011\}\) |
| \(1100\) | \(\{0011,0101\}\) |

For a general \(w\), its missing-balanced set is the intersection of the table entries for all \(t\in T(w)\). This restricts it to precisely the following **seven formal possibilities**:
\[
\varnothing,\ \{1010,1100\},\ \{1100\},\ \{1001\},\ \{0110\},\ \{0011\},\ \{0011,0101\}.
\]
These seven are not always simultaneously realizable at a fixed pair of symbol counts.

**Step 4 (exclude two types at large symbol counts and one at length four).** A missing set containing \(1001\) must equal \(\{1001\}\); the table forces \(T(w)=\{0110\}\). Choose two zeros straddling two ones in a subsequence \(0110\). If a third zero existed, it would lie before the first one, between the two ones, or after the second one. In the three cases the word would contain respectively a balanced subsequence \(0011\), \(0101\) or \(1010\), or \(1100\), contradicting \(T(w)=\{0110\}\). Hence \(\{1001\}\) can occur only when \(i=2\). The symmetric reversal-and-letter-exchange argument (or the same direct positional argument) shows that \(\{0110\}\) can occur only when \(j=2\). If \(i=j=2\), the word has length four and \(T(w)\) is its singleton whole word; no empty missing set can occur.

**Step 5 (construct every other type).** For every pair \(i,j\ge2\), the following words have exactly the indicated missing-balanced sets; these are checked from the balanced subsequences in Step 3. Exponents denote repetition, and all words in the table have exactly \(i\) zeros and \(j\) ones.

| Missing-balanced set | Representative | Conditions |
|---|---|---|
| \(\{1010,1100\}\) | \(0^i1^j\) | \(i,j\ge2\) |
| \(\{1100\}\) | \(0^{i-1}101^{j-1}\) | \(i,j\ge2\) |
| \(\{0011\}\) | \(1^{j-1}010^{i-1}\) | \(i,j\ge2\) |
| \(\{0011,0101\}\) | \(1^j0^i\) | \(i,j\ge2\) |
| \(\{1001\}\) | \(01^j0\) | \(i=2, j\ge2\) |
| \(\{0110\}\) | \(10^i1\) | \(j=2, i\ge2\) |
| \(\varnothing\) | \(0^{i-2}10101^{j-2}\) | \(i,j\ge2\), \(i+j\ge5\) |

Here repetition expressions involving unambiguous adjacent literal digits are interpreted by concatenation, e.g. \(0^{i-1}101^{j-1}\) means \(0^{i-1}\cdot 1\cdot0\cdot1^{j-1}\), and \(0^{i-2}10101^{j-2}\) means \(0^{i-2}\cdot1\cdot0\cdot1\cdot0\cdot1^{j-2}\). The first and fourth witnesses have respectively \(T(w)=\{0011\}\) and \(T(w)=\{1100\}\). The second has \(0101\in T(w)\subseteq\{0011,0101\}\), and the third has \(1010\in T(w)\subseteq\{1010,1100\}\). The fifth and sixth have respectively \(T(w)=\{0110\}\) and \(T(w)=\{1001\}\). The final witness contains ordinary balanced subsequences \(1010\) and \(0101\), whose missing sets have empty intersection. These inclusions can be verified by the relative positions of the two transitions (or direct enumeration of subsequence types) and hold for every permitted \(i,j\), not merely the tested finite range. When \(\min(i,j)<2\), the sole class for the corresponding counts has representative \(0^i1^j\).

Therefore the number of classes for one fixed capped-count pair \((a,b)\) is exactly
\[
f(a,b)=\begin{cases}
1,&\min(a,b)<2,\\
6,&a=b=2,\\
6,&\min(a,b)=2<\max(a,b),\\
5,&a,b\ge3.
\end{cases}
\]
(The second and third cases may be consolidated, but are separated to record why the empty missing set fails only in the \((2,2)\) cell.) All seven types are available in no single capped-count cell: the two rare exceptional types need an exactly twofold symbol count.

**Step 6 (global index).** There are \(25\) possible capped-count pairs. Exactly \(16\) have at least one coordinate below two. The cell \((2,2)\) contributes six classes; the four cells with one coordinate two and the other three or four contribute six each; the four cells with both coordinates three or four contribute five each. The index is thus
\[
16+6+4\cdot6+4\cdot5=66.
\]
Different capped-count pairs cannot yield equivalent words by Step 1, and the missing-balanced set distinguishes the classes within a pair.

**Step 7 (fixed lengths and sharp saturation).** At fixed length \(n\), let \(i\) range from zero to \(n\) and set \(j=n-i\). Distinct capped-count pairs are counted only once; every admissible missing-balanced type can be witnessed at the prescribed exact counts by Step 5. This gives \(E(n)=n+1\) for \(0\le n\le3\), \(E(4)=10\), and \(E(5),E(6),E(7),E(8)=(16,21,26,31)\). For \(n\ge8\), the only capped-count pairs represented are \((0,4),(1,4),(2,4),(3,4),(4,4),(4,3),(4,2),(4,1),(4,0)\). Their counts sum to \(1+1+6+5+5+5+6+1+1=31\). All nine cells occur at every such length, and their witnesses remain valid. Thus the stated fixed-length formula holds and saturation first occurs at eight. \(\square\)

## Verification
The accompanying stdlib-only `check.py` constructs one representative of every claimed global class and independently computes signatures by directly testing all patterns of lengths zero through four against subsequences obtained by a single deletion. It verifies that all \(66\) representatives have distinct signatures. It separately computes balanced ordinary subsequences and checks the structural signature formula for every binary word of lengths zero through twelve (\(8191\) words total), reproducing class counts \((1,2,3,4,10,16,21,26,31,31,31,31,31)\). The exact witness table is `WITNESSES.tsv`. Run `python3 check.py` with these files in the same directory. The infinite result rests on Steps 1–7, not on the finite checks.

## Relationship to prior work
Fleischmann, Huch, Kim, Koß, and Wiards introduced and investigated jumbled Simon equivalence and embeddings in their October 2026 paper [1]. Their general treatment supplies algorithms and, for the case where the permitted jumbling count is one below the pattern length, a closed index formula. The present binary \(k=4\), \(\ell=1\) case is different from that extremal parameter regime, and the specific exact index, fixed-length spectrum, and full missing-balanced classification are not given in the inspected portions of that work. The June 2025 foundational study of jumbled scattered factors [2] develops the generalized notion and finite-index theory, not this exact small-parameter quotient. Classical Simon congruence [3] concerns ordinary scattered-subsequence equivalence without jumbling; its index results do not imply this theorem. This comparison is based on the cited, examined versions and does not guarantee absolute historical novelty.

## Limitations
The result covers precisely the two-letter, one-jumble, length-at-most-four relation. No formula is established here for larger alphabets, larger pattern bounds, or additional jumbling. The fixed-length saturation is a statement about **classes represented**, not the number of words or unique representatives, and the equivalence need not be a monoid congruence. The computational tests through length twelve do not substitute for the infinite proof. Equivalent results in unindexed or otherwise unavailable literature remain possible. Independent scientific validation has not been performed.

## References
[1] P. Fleischmann, A. Huch, S. Kim, T. Koß, E. Wiards, *Jumbled Simon’s Equivalence and Embeddings*, arXiv:2610.17910v1, publicly posted 2026-10-13. https://arxiv.org/html/2610.17910v1

[2] P. Fleischmann and collaborators, *Jumbled Scattered Factors*, arXiv:2506.03814v1, publicly posted 2025-06-04. https://arxiv.org/html/2506.03814v1

[3] P. Karandikar, M. Kufleitner, P. Schnoebelen, *On the index of Simon’s congruence for piecewise testability*, arXiv:1310.1278. https://arxiv.org/abs/1310.1278
