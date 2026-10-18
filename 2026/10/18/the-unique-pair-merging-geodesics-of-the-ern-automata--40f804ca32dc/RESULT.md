# The unique pair-merging geodesics of the Černý automata

## Finding
For every integer \(n\ge3\), consider the deterministic automaton on \(Q_n=\{0,1,\ldots,n-1\}\) with letters \(a\) and \(b\) acting by
\[
 a(i)=i+1\pmod n,\qquad b(0)=1,\qquad b(i)=i\quad(1\le i<n).
\]
For \(1\le d\le\lfloor n/2\rfloor\), put \(L_d=n\) when \(2d<n\), and \(L_d=n/2\) when \(2d=n\). For \(0\le j<L_d\), define the unordered pair
\[
 P_{d,j}=\{(-j)\bmod n,(d-j)\bmod n\}.
\]
Every two-element subset of \(Q_n\) has exactly one such representation. Its **unique shortest merging word**, read from left to right, is
\[
 w_{d,j}=a^j b\bigl(a^{n-1}b\bigr)^{d-1},
 \qquad |w_{d,j}|=n(d-1)+j+1.
\]
Consequently the multiset of minimum pair-merging lengths is precisely \(\{1,2,\ldots,\binom n2\}\), with multiplicity one for each length. Exactly one unordered pair attains the worst length \(\binom n2\); the average minimum length over uniformly chosen unordered pairs is \(\tfrac12(\binom n2+1)\). The shortest word for \(P_{d,j}\) uses exactly \(d\) letters \(b\) and \(j+(d-1)(n-1)\) letters \(a\).

## Assumptions and scope
A word merges an unordered pair \(\{p,q\}\) if both states reach the same state after its letters are applied in order. Empty words do not merge distinct states. Alphabet letters have equal unit length; weighted-cost optimization and synchronization of larger subsets are not claimed. The representation chooses the shorter *unoriented* circular gap \(d\). In the antipodal case \(2d=n\), the two opposite orientations name the same pair, so \(j\) is restricted to \(0\le j<n/2\).

## Proof
**1. Exhaustive and unique parametrization.** Each unordered distinct pair has shorter cyclic separation \(d\) with \(1\le d\le\lfloor n/2\rfloor\). When \(2d<n\), there are exactly \(n\) distinct translates of \(\{0,d\}\), and the displayed \(P_{d,j}\) list them all once. When \(2d=n\), translation by \(d\) exchanges the two endpoints, so precisely \(n/2\) translates are distinct. The gap classes are disjoint. Their total cardinality is \(\binom n2\).

**2. A one-step lower-bound potential.** Set \(R(P_{d,j})=n(d-1)+j+1\) and set \(R(\{r\})=0\) on singleton images. Under \(a\), the index \(j\) decreases by one when positive; at \(j=0\), it wraps to \(L_d-1\). Thus, for \(j>0\), exactly one unit of potential is lost, and for \(j=0\) the potential increases (because \(L_d\ge2\)).

Under \(b\), pairs not containing state zero stay fixed. The pair \(P_{d,0}=\{0,d\}\) is merged when \(d=1\); for \(d\ge2\) it is sent to \(\{1,d\}=P_{d-1,n-1}\). Hence \(b\) decreases \(R\) by exactly one in these cases.

The only remaining pairs containing zero are \(P_{d,d}=\{n-d,0\}\) for \(2d<n\). The letter \(b\) sends these to \(\{n-d,1\}\). If \(2(d+1)\le n\), their new shorter circular separation is \(d+1\), giving a strictly higher gap layer and hence larger \(R\). Otherwise \(n\) is odd and \(d=(n-1)/2\); the new pair is \(P_{d,n-1}\), whose index is larger than \(d\) and whose potential is therefore also larger. This exhausts the possibilities.

Thus every letter reduces \(R\) by **at most one**, and at every non-singleton pair **exactly one** of the two letters reduces it by exactly one: \(a\) if \(j>0\), and \(b\) if \(j=0\). A word merging a pair with initial potential \(r\) must therefore have at least \(r\) letters.

**3. Achievability and uniqueness.** From \(P_{d,j}\), the forced potential-reducing path begins with \(j\) uses of \(a\), reaching \(P_{d,0}\). The next letter \(b\) either merges the pair (when \(d=1\)) or takes it to \(P_{d-1,n-1}\). In the latter case \(n-1\) uses of \(a\) and a further \(b\) repeat the reduction to the next gap layer. Iteration yields exactly \(w_{d,j}\) and reaches a singleton after \(R(P_{d,j})\) steps. Any equally short word must decrease \(R\) at every step and therefore must take the unique potential-decreasing letter at every step. It equals \(w_{d,j}\).

**4. Spectrum and compositions.** For each \(d\), the index \(j\) ranges over \(0,\ldots,L_d-1\), so the lengths form the consecutive interval from \(n(d-1)+1\) to \(n(d-1)+L_d\). Adjacent gap classes concatenate these intervals without gaps or overlaps; their union is \(\{1,\ldots,\binom n2\}\). The displayed word gives the exact two-letter composition. Summing all lengths gives the stated average. Equivalently, the bivariate enumerator of *unique minimum words indexed by their initial pairs* is
\[
 H_n(x,y)=\sum_{d=1}^{\lfloor n/2\rfloor}
    y^d x^{(n-1)(d-1)}\sum_{j=0}^{L_d-1}x^j,
\]
where \(x\) marks occurrences of \(a\), and \(y\) marks occurrences of \(b\).

## Verification
The accompanying standalone `checker.py` constructs the actual pair-transition digraph directly from the two letter actions. For each \(3\le n\le40\), it obtains minimum merger lengths from independent reverse breadth-first search starting at the merged sink. Dynamic programming on shortest-distance layers counts shortest merger words without using the proposed classification. It independently compares all \(10{,}659\) unordered pairs with the closed formula, checks unique shortest words, verifies the potential inequalities on every edge, and replays every proposed minimizing word. Running `python3 checker.py` reproduces the recorded `checker_output.txt` line. These finite checks corroborate but do not constitute the all-\(n\) proof above.

## Relationship to prior work
Szykuła's 2026 survey gives the modern setting for pair compression and reset-word length problems, including the classical extremal Černý family. Gusev (2014), especially Section 3 and Lemma 1, specifies an isomorphic pair automaton for **odd** \(n\) (using the opposite letter names) and derives expected **random-input** merging times; it does not state the unique shortest merger word for every pair, the unit-multiplicity shortest-distance spectrum, or the bivariate minimizing-word enumerator. Gusev does also discuss even \(n\) for the random-input expectation. Gonze–Gusev–Gerencsér–Jungers–Volkov (2017) study pair-digraph distances for a **different** automaton family and explain the relevance of pair distances to synchronization bounds. The classical general upper bound \(\binom n2\) for a shortest pair-merging word, when it applies, is not claimed as new; the claim here is its unique exact realization by the family, at every intermediate length, together with unique geodesics.

## Limitations
This classification is for unit-cost deterministic merging of exactly two states in the stated two-letter Černý automata. It does not improve the general Černý reset threshold, solve a wider pair-compression extremal problem, or apply to arbitrary synchronizing automata. The full odd-state pair-transition description in Gusev is a particularly close precursor, and the present formulas are derivable from it by additional shortest-path analysis. Historical-priority checking is limited to the primary literature and indexed records examined; independent review has not been performed.

## References
1. M. Szykuła, *Synchronizing Automata: Open Problems*, arXiv:2608.24245v1, first posted 2026-08-25, EPTCS 451 (2026), 33–47, DOI:10.4204/EPTCS.451.3.
2. V. V. Gusev, *Synchronizing Automata with Random Inputs*, arXiv:1404.6731v1 (2014), especially Section 3, Lemma 1, and Theorems 3–4.
3. F. Gonze, V. V. Gusev, B. Gerencsér, R. M. Jungers, and M. V. Volkov, *On the Interplay Between Babai and Černý's Conjectures*, arXiv:1704.04047v2 (2017), especially Sections 1.3 and 3.
