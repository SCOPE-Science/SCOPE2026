# Sharp onset and maximal binary insertion/deletion covering separators

## Finding
For every integer \(R\geq1\), a set \(C\subseteq\{0,1\}^{n}\), where \(n>R\), is an \(R\)-insertion cover if every binary word of length \(n+R\) has a length-\(n\) subsequence in \(C\), and is an \(R\)-deletion cover if every binary word of length \(n-R\) occurs as a subsequence of some element of \(C\). All subsequences here are scattered (not necessarily contiguous), and exactly \(R\) symbols are inserted or deleted.

**Theorem.** For every \(R\geq1\):

1. When \(R<n\leq R+3\), every binary \(R\)-insertion cover is also an \(R\)-deletion cover.
2. At the first separating blocklength \(n=R+4\), the **only inclusion-maximal** binary \(R\)-insertion covers which are not \(R\)-deletion covers are
   \[
   F_{0110}=\{x\in\{0,1\}^{R+4}:0110\not\preceq x\},\qquad
   F_{1001}=\{x\in\{0,1\}^{R+4}:1001\not\preceq x\},
   \]
   where \(\preceq\) denotes scattered-subsequence containment. They are distinct but exchanged by global bit complementation. Each has cardinality
   \[
   |F_{0110}|=|F_{1001}|=\sum_{j=0}^{3}\binom{R+4}{j}.
   \]
   Each one fails deletion covering at exactly the indicated length-four word, and adding any excluded length-\(n\) word restores deletion covering.

Here *inclusion-maximal* refers to inclusion among codes possessing insertion covering but not deletion covering; the theorem makes no minimum-code-cardinality assertion. The existence of \(F_{0110}\) as an insertion cover, for all \(R\), is due to Xie, Sun, and Ge (2026, Theorem III.2). The new assertions are sharp nonexistence below \(R+4\), exhaustion by the two exceptional patterns, and maximal-family classification.

## Assumptions and scope
The alphabet is exactly \(\{0,1\}\); \(R\) is any positive integer, and \(n\) is an integer greater than \(R\). A word may contain repeated symbols. All quantifiers are over complete finite word spaces, not over a sample of codes. Reversal and simultaneous interchange of the two alphabet symbols preserve both covering properties. No bound on \(|C|\) beyond \(|C|\leq 2^n\) is assumed.

For a binary word \(y\) of length \(m=n-R\), define \(F_y=\{x\in\{0,1\}^n:y\not\preceq x\}\). If a code fails deletion covering at \(y\), then necessarily \(C\subseteq F_y\). Thus a counterexample missing \(y\) is possible only if \(F_y\) is itself an insertion cover. The latter is equivalent to the absence of any \(z\in\{0,1\}^{m+2R}\) for which **every** length-\(m+R\) subsequence contains \(y\).

## Proof
**Short-pattern obstruction.** For each representative \(y\) in the following table, the displayed word \(z\), of length \(m+2R\), has the property that **every** subsequence of length \(m+R\) contains \(y\). The notation \(0^k\) means \(k\) successive zeros and \((uv)^k\) means \(k\) successive copies of \(uv\).

| \(m\) | \(y\) | Forcing word \(z\) |
|---|---|---|
| 1 | \(0\) | \(0^{2R+1}\) |
| 2 | \(00\) | \(0^{2R+2}\) |
| 2 | \(01\) | \((01)^{R+1}\) |
| 3 | \(000\) | \(0^{2R+3}\) |
| 3 | \(001\) | \(0^{R+2}1^{R+1}\) |
| 3 | \(010\) | \((01)^{R+1}0\) |
| 4 | \(0000\) | \(0^{2R+4}\) |
| 4 | \(0001\) | \(0^{R+3}1^{R+1}\) |
| 4 | \(0010\) | \(00(10)^{R+1}\) |
| 4 | \(0011\) | \(0^{R+2}1^{R+2}\) |
| 4 | \(0101\) | \((01)^{R+2}\) |

These representatives exhaust all binary words of lengths at most four under reversal and global complement, except for the length-four orbit \(\{0110,1001\}\). Since both operations preserve scattered-subsequence containment, the witnesses extend to all the corresponding orbits.

The constant and two-run witnesses are immediate: after at most \(R\) deletions, each required run retains the stated minimum number of symbols. Here is a complete justification of the remaining witnesses.

For an alternating word \(z\) beginning in zero, any length-\(L\) subsequence \(x\) with \(t\) adjacent changes of symbol has its last matched position, indexed from zero, at least \(x_1+2(L-1)-t\). Indeed, consecutive unequal selected symbols require at least one intervening index step, whereas equal selected symbols require at least two, and a selected initial one starts at index at least one. A binary word avoiding the scattered pattern \(01\) has at most zero changes if it begins with zero, or one if it begins with one; avoiding \(010\) allows at most one or two respectively; avoiding \(0101\) allows at most two or three respectively. For the listed alternating witnesses, substituting \(L=R+m\) gives a last matched position at least \(m+2R=|z|\), impossible. Thus every requested-length subsequence contains its pattern.

For \(y=0010\), write \(z=00(10)^k\) with \(k=R+1\). A subsequence \(x\) avoiding \(0010\) and having at most one zero has length at most \(k+1\). Otherwise, let its second selected zero be the \(j\)-th zero of \(z\), with \(j\geq2\). Up to and including that zero, at most \(j\) letters can be selected while retaining exactly two selected zeros. After the second selected zero, avoidance of \(0010\) requires any further selected letters to form \(0^a1^b\). The remaining suffix of \(z\) is \((10)^{k+2-j}\), whose longest \(0^a1^b\) subsequence has length \(k+2-j\). Hence \(|x|\leq j+(k+2-j)=k+2=R+3\), strictly smaller than the required \(R+4\). This proves the last non-alternating forcing case.

For \(m\leq3\), every missing deletion target has a forcing word. Such a forcing word cannot be insertion-covered by any subset of \(F_y\), proving assertion 1. At \(m=4\), the same argument excludes every \(y\) except \(0110\) and \(1001\).

**Exceptional patterns do permit insertion covering.** We re-establish the pertinent existence argument of Xie, Sun, and Ge, to make the implication self-contained. Suppose some \(z\in\{0,1\}^{2R+4}\) had every length-\(R+4\) subsequence containing \(0110\). If \(z\) had at most \(R+1\) zeros, deleting at most \(R\) of them would leave at most one zero and therefore avoid \(0110\); similarly for ones. Thus \(z\) has exactly \(R+2\) occurrences of each symbol. Retain any two zeros and all \(R+2\) ones by deleting the other \(R\) zeros. The resulting subsequence must contain \(0110\), so at least two ones occur between those two zeros. In particular every one of the \(R+1\) intervals between consecutive zeros contains at least two ones. This requires at least \(2R+2>R+2\) ones, a contradiction. Hence \(F_{0110}\) insertion-covers every longer word. Complementation proves the same for \(F_{1001}\). Both miss their defining deletion targets.

**Maximality and counting.** Fix one exceptional \(y\). Every other length-four word \(v\neq y\) avoids \(y\). Greedily match the longest prefix of \(y\) inside \(v\); because that prefix is still proper, there is a binary letter which does not advance the greedy match. Append such letters until length \(R+4\). The resulting \(x\in F_y\) contains \(v\), proving that \(F_y\) deletion-covers every length-four word other than \(y\). Adding any word not in \(F_y\) covers \(y\) as well and therefore destroys the counterexample property. Conversely, any counterexample is contained in one of these two \(F_y\), so these are exactly the inclusion-maximal counterexamples.

Finally, while greedily matching a fixed length-four pattern \(y\), each proper matched-prefix state has exactly one bit that leaves the state unchanged and one that advances it. A length-\(n\) word avoids \(y\) precisely when it advances at most three times. Choosing those advance positions yields \(|F_y|=\sum_{j=0}^{3}\binom{n}{j}\). Substituting \(n=R+4\) proves the stated cardinality. \(\square\)

## Verification
The accompanying standalone `verify.py` implements exact dynamic programming for the longest subsequence avoiding a given pattern. It exhausts every binary target pattern and potential forcing superword for \(1\leq R\leq5\), \(1\leq m\leq4\), and finds only \(0110\) and \(1001\) as positive exceptional patterns at \(m=4\). For \(R\leq3\), a separate explicit deletion-position enumerator agrees with the dynamic program. The program checks all symbolic forcing templates for \(1\leq R\leq50\), and independently enumerates the sizes and deletion targets of both inclusion-maximal families for \(1\leq R\leq7\). Run `python3 verify.py`; `verification_output.txt` records the resulting checks. The uniform proof above, not the finite tests, establishes the all-radius theorem.

## Relationship to prior work
Xie, Sun, and Ge, *New bounds for covering codes under insertions or deletions* (first publicly submitted 13 June 2026), Theorem III.2, establish that avoiding \(0110\) yields an insertion cover which is not a deletion cover at \(n=R+4\). They also extend non-equivalence to larger blocklengths. Their assertion is an existence result; it does not give the reverse implication for all smaller blocklengths, rule out other forbidden length-four patterns, or classify all inclusion-maximal separators. These are the contributions proved here. Lenz, Rashtchian, Siegel, and Yaakobi (2019/2020) develop covering-code bounds and constructions, not this sharp boundary classification. Nearby work on subsequence universality and shortest absent subsequences concerns distinct optimization problems and does not imply an insertion/deletion covering separator classification.

## Limitations
The result is binary and concerns exact error count \(R\). The maximality is by inclusion, **not** optimal cardinality, and the proof does not classify smaller subcodes that also separate the covering properties. The sharp-onset theorem does not classify maximal separators at larger blocklengths or over alphabets with more than two symbols. Computational experiments only independently check bounded instances; no claim of independent external audit or historical uniqueness of publication is made.

## References
1. Chengfei Xie, Yubo Sun, Gennian Ge, *New bounds for covering codes under insertions or deletions*, arXiv:2606.15379, first submitted 13 June 2026; especially Section III, Theorem III.2 and Remark III.3. https://arxiv.org/abs/2606.15379
2. Andreas Lenz, Cyrus Rashtchian, Paul H. Siegel, Eitan Yaakobi, *Covering Codes using Insertions or Deletions*, arXiv:1911.09944, first submitted 22 November 2019, updated 2020. https://arxiv.org/html/1911.09944v4
