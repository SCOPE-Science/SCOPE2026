# Exact state complexity of the intersection of opposite two-run subsequence ideals

## Finding
Let \(r,s\ge1\) be integers and let \(\Sigma=\{0,1\}\). Define \(u\preceq w\) to mean that \(u\) is a **scattered subsequence** of \(w\), i.e. deleting zero or more letters of \(w\) yields \(u\). For
\[
L_{r,s}=\{w\in\Sigma^*:0^r1^s\preceq w\ \text{and}\ 1^s0^r\preceq w\},
\]
the number of states of the minimal *complete* deterministic finite automaton is exactly
\[
\boxed{\kappa(L_{r,s})=\frac{(r+s)(r+s+3)}{2}+rs.}
\]
In the balanced case \(r=s=t\), this is \(3t(t+1)\), whereas the unminimized Cartesian product of the two single-subsequence automata contains \((2t+1)^2\) states. The exact formula describes the structure of simultaneous, oppositely ordered binary subsequence constraints, not the worst case over arbitrary regular-language intersections.

## Assumptions and scope
Both thresholds are strictly positive; the alphabet is exactly \(\{0,1\}\); occurrences need not be contiguous. The automaton is deterministic, complete, and minimizes among all such acceptors. Each requirement is an *upward* scattered-subsequence ideal; their intersection is also upward closed. The theorem covers every \(r,s\ge1\), with no computationally bounded parameter assumption.

## Proof
Put \(n=r+s\), \(P=0^r1^s\), and \(Q=1^s0^r\). A greedy prefix matcher for a fixed word increases its current matching length precisely when the next required letter is read. For any input \(w\), let \(i\) and \(j\) be the longest matched prefix lengths of \(P\) and \(Q\), respectively. The initial product state is \((0,0)\); reading \(c\in\Sigma\) updates \((i,j)\) by independently increasing a coordinate by one if that coordinate is not terminal and the next pattern letter equals \(c\). The sole accepting product state is \((n,n)\). The greedy-matching induction shows that this product accepts exactly \(L_{r,s}\).

**Reachability lemma.** The reachable states are exactly the disjoint regions
\[
\begin{aligned}
A&=\{(i,j):0\le i<r,\ 0\le j<s\},\\
B&=\{(i,s+t):0\le i<r,\ 0\le t\le i\},\\
C&=\{(r+u,j):0\le j<s,\ 0\le u\le j\},\\
D&=\{(i,j):r\le i\le n,\ s\le j\le n\}\setminus\{(r,s)\}.
\end{aligned}
\]
For \(A\), use input \(0^i1^j\). For \(B\), use \(0^{i-t}1^s0^t\). For \(C\), use \(1^{j-u}0^r1^u\). For \(D\), use \(0^{r-t}1^s0^t\) when \(i=r\) and \(j=s+t\) with \(1\le t\le r\), use \(1^{s-u}0^r1^u\) when \(i=r+u\) with \(1\le u\le s\) and \(j=s\), and use \(1^{s-u}0^r1^u0^t\) when both \(u,t\) are positive. Each displayed input reaches its specified state by direct greedy reading. Conversely, in a state with \(i<r\) and \(j=s+t\), the \(t\) zeros matched *after* the first \(s\) ones are among only \(i\) matched zeros, so \(t\le i\). Symmetrically, \(i=r+u\), \(j<s\) entails \(u\le j\). The state \((r,s)\) cannot be reached: the temporal order of the \(r\)-th zero and the \(s\)-th one forces progress beyond at least one of these thresholds. These observations exclude all states outside the listed regions.

**Right-quotient lemma.** Every pair of different reachable states has different continuation languages. At a state \((i,j)\), a suffix is accepted if and only if it contains both remaining pattern tails \(P[i:]\) and \(Q[j:]\) as scattered subsequences. Test whether the right quotient meets \(0^*1^*\) and \(1^*0^*\), respectively. The two Boolean answers are \((\mathrm{false},\mathrm{false})\) in \(A\), \((\mathrm{true},\mathrm{false})\) in \(B\), \((\mathrm{false},\mathrm{true})\) in \(C\), and \((\mathrm{true},\mathrm{true})\) in \(D\). Hence states from different regions are distinguished.

For states within \(A\), a suffix of the form \(0^a1^s0^r\) is accepted precisely when \(a\ge r-i\); a suffix \(1^a0^r1^s\) is accepted precisely when \(a\ge s-j\). Thus their quotients determine both coordinates. Within \(B\), where \(j=s+t\), a suffix \(0^a1^s0^b\), with \(a,b\ge0\), is accepted precisely when
\[
a\ge r-i\quad\text{and}\quad a+b\ge n-j=r-t.
\]
Because \(t\le i\), the first threshold does not exceed the second; each can be recovered from the accepted pairs \((a,b)\): the smallest admissible \(a\) is \(r-i\), and the smallest admissible \(a+b\) is \(n-j\). The two coordinates are determined. The mirror argument in \(C\) uses suffixes \(1^a0^r1^b\) and the inequalities \(a\ge s-j\), \(a+b\ge n-i\). Within \(D\), a suffix \(0^a1^b\) is accepted precisely when \(a\ge n-j\) and \(b\ge n-i\); again both coordinates are determined. Therefore all reachable product states are pairwise Myhill–Nerode inequivalent.

Finally, the four cardinalities are \(|A|=rs\), \(|B|=r(r+1)/2\), \(|C|=s(s+1)/2\), and \(|D|=(r+1)(s+1)-1\). Their sum is \((r+s)(r+s+3)/2+rs\). Reachability and pairwise distinguishability show that this is exactly the minimal state count. \(\square\)

## Verification
A standalone Python 3 verifier, `verify_opposite_subseq.py`, constructs each reachable greedy-product DFA for \(1\le r,s\le10\), checks the four-region classification, minimizes it by independently refining final/nonfinal partitions, and compares the minimized size with the formula: 100 parameter pairs passed. For nine parameter pairs, it also compares greedy-product acceptance with a separate direct subsequence predicate for every binary word of length at most twelve: 73,719 checks passed. Run `python3 verify_opposite_subseq.py` from the folder containing the supplied script; the expected final line begins `VERIFY_OK`. These finite checks corroborate, but do not replace, the all-parameter proof.

## Relationship to prior work
Brzozowski, Davies, and Madan (2018) develop state complexity for subsequence pattern matching against a regular text language, including a generic worst-case bound and single-word pattern matching. Their general bound applies to this intersection but does not give the present exact opposite-two-run formula: it does not classify the reachable states or prove their individual inequivalence for this restricted pair. Brzozowski, Davies, and Liu's general intersection results for right ideals concern worst-case witnesses in a broader class and likewise do not force equality for this family. Masopust and Thomazo study Boolean combinations of piecewise-testable languages, whose framework contains this example but whose inspected results do not state this sharp two-parameter quotient formula. Thus the contribution is the exact count *and* regional quotient classification for a motivated constrained intersection. The literature search is not a proof of absolute novelty.

## Limitations
The result is restricted to a binary alphabet and two oppositely ordered block patterns sharing the same positive multiplicities; it does not address arbitrary patterns, larger alphabets, or general Boolean combinations. The proof is fully mathematical; no independent external audit has been performed. Unindexed or inaccessible literature could contain equivalent results. The comparison with broad worst-case bounds is a comparison of implications, not a claim to improve those universal bounds.

## References
1. J. A. Brzozowski, S. Davies, and A. Madan, *State Complexity of Pattern Matching in Regular Languages*, first public arXiv version 12 June 2018, arXiv:1806.04645, https://arxiv.org/abs/1806.04645.
2. J. A. Brzozowski, S. Davies, and B. Y. V. Liu, *Most Complex Regular Ideal Languages*, arXiv:1511.00157, https://arxiv.org/abs/1511.00157.
3. T. Masopust and M. Thomazo, *On Boolean Combinations Forming Piecewise Testable Languages*, *Theoretical Computer Science* (2017), accessible author's PDF, https://iccl.inf.tu-dresden.de/w/images/7/79/Tcs_bool.pdf.
4. P. Karandikar and Ph. Schnoebelen, *The Height of Piecewise-Testable Languages and the Complexity of the Logic of Subwords*, arXiv:1511.01807, https://arxiv.org/abs/1511.01807.
