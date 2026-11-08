# A binomial maximal-common-subsequence law for two ternary permutation powers

## Finding
Let \(\Sigma=\{0,1,2\}\), \(X_r=(012)^r\), and \(Y_s=(021)^s\), for arbitrary positive integers \(r,s\). An MCS is a *distinct word* which is a subsequence of both inputs, but no proper supersequence of it is a common subsequence. Let \(\mathcal M(r,s)\) denote the set of MCS words and \(\mathcal L(r,s)\) the set of longest common subsequence (LCS) words.

**Theorem.** For every \(r,s\ge1\), the two sets are equal, and
\[
\operatorname{LCS}(X_r,Y_s)=\min\{r+s,3\min(r,s)\},\qquad
|\mathcal M(r,s)|=
\begin{cases}
\displaystyle\binom{r+s}{2\min(r,s)-\max(r,s)},&\max(r,s)\le2\min(r,s),\\[4pt]
1,&\max(r,s)>2\min(r,s).
\end{cases}
\]
The count is by *different subsequence strings*, not by embeddings. In the first case, all MCS words have length \(r+s\). In the second, the only MCS is the complete shorter-period-count input: \(Y_s\) if \(r>2s\), or \(X_r\) if \(s>2r\).

In the nontrivial triangle \(r\le2s\) and \(s\le2r\), the theorem also classifies **all** optimizers: they are exactly the words \(w\) starting with \(0\), ending in \(1\) or \(2\), having no equal adjacent letters, and satisfying
\[
d_{012}(w)=r-1,\qquad d_{021}(w)=s-1,
\]
where \(d_\pi\) counts adjacent weak descents in the total order \(\pi\). Equivalently, these are the length-\(r+s\) common subsequences. For equal repetition counts \(r=s=n\), the count is the central binomial coefficient \(\binom{2n}{n}\); thus the MCS set can be exponentially large even though every MCS is longest.

## Assumptions and scope
Strings are finite. A subsequence is formed by deleting positions while retaining the order of the others. A proper supersequence of \(w\) need not be contiguous. Maximality is inclusion-maximality in the subsequence partial order, not merely inability to append one symbol. The powers use literal concatenation, and the alphabet consists of the three displayed, pairwise distinct symbols. No asymptotic hypothesis is made; both repetition counts range over all positive integers. The two input permutations differ by swapping the final two symbols.

For any total order \(\pi\) on the three symbols, define \(d_\pi(w)=|\{i:w_i\ge_\pi w_{i+1}\}|\), with \(d_\pi(w)=0\) for a one-letter word. Throughout, binomial coefficients are zero unless the lower argument lies between zero and the upper argument.

## Proof
**1. Greedy-subsequence criterion.** For every nonempty \(w\), its leftmost greedy embedding into \(\pi^m\) starts in the first copy of \(\pi\). Between consecutive symbols, it advances to the next copy precisely when the next symbol is not strictly later in the order \(\pi\). Consequently
\[
w\preceq\pi^m\quad\Longleftrightarrow\quad d_\pi(w)\le m-1.\tag{1}
\]
In particular, common subsequences are exactly the nonempty words with \(d_{012}\le r-1\) and \(d_{021}\le s-1\), together with the empty word.

**2. Saturation for proper maximal words.** Inserting one letter anywhere in a word increases its weak-descent count for any fixed total order by either zero or one. At an internal insertion, if the old adjacent pair was increasing, the two replacement pairs cannot both be weakly descending; if it was descending, at least one replacement pair is weakly descending. Insertion at either endpoint is immediate. Thus, if \(w\) is a proper subsequence of \(X_r\) and \(d_{021}(w)\le s-2\), inserting an occurrence omitted from an embedding into \(X_r\) gives a longer subsequence of \(X_r\) still satisfying the \(Y_s\) bound in (1). The symmetric statement holds with the roles interchanged. Therefore every maximal common word other than an entire input word satisfies both equalities \(d_{012}=r-1\), \(d_{021}=s-1\).

**3. Zero-cost extensions.** A word with an equal adjacent pair admits a one-letter insertion between those two equal symbols that changes neither weak-descent count: insert \(1\) between \(00\), or insert \(0\) between \(11\) or \(22\). Any word starting in \(1\) or \(2\) can be extended by prepending \(0\) at zero cost, and any word ending in \(0\) can be extended by appending \(1\). Hence a saturated maximal common word must start in \(0\), end in \(1\) or \(2\), and have unequal neighbors. Conversely, for such a word, every possible one-letter insertion increases at least one of the two weak-descent counts. This follows directly from the complete strict-transition cost table:

| Transition | Increment to \((d_{012},d_{021})\) |
|---|---|
| \(0\to1\), \(0\to2\) | \((0,0)\) |
| \(1\to0\), \(2\to0\) | \((1,1)\) |
| \(1\to2\) | \((0,1)\) |
| \(2\to1\) | \((1,0)\) |

At the left endpoint the first symbol is already \(0\), and at the right endpoint the final symbol is nonzero, so there are no zero-cost endpoint insertions either. Once both budgets are saturated, (1) excludes all insertions. Since any proper supersequence contains a one-letter supersequence, the word is maximal.

For a word with these endpoint and adjacency properties, the number of nonzero-to-zero transitions is one less than that of zero-to-nonzero transitions. The table implies \(d_{012}(w)+d_{021}(w)=|w|-2\). Double saturation therefore forces \(|w|=r+s\). If \(r>2s\), then \(d_{012}(Y_s)=2s-1<r\), so \(Y_s\preceq X_r\) and it is the unique MCS (all common words are its subsequences). Symmetrically, for \(s>2r\), the only MCS is \(X_r\). On the boundaries \(r=2s\) or \(s=2r\), the whole shorter input is already doubly saturated, so the characterization remains valid.

**4. Counting all saturated words.** Assign the formal weights \(x,y\) to increments of \(d_{012},d_{021}\) in the table. Let \(f_i\) enumerate all paths starting at symbol \(i\), with unequal successive symbols, which terminate at \(1\) or \(2\); a zero-edge path counts exactly when its starting symbol is a permitted endpoint. Thus
\[
f_0=f_1+f_2,\qquad
f_1=1+xyf_0+yf_2,\qquad
f_2=1+xyf_0+xf_1.
\]
Solving these three formal-power-series equations gives
\[
F(x,y)=f_0=\frac{2+x+y}{1-xy(3+x+y)}.
\]
Every word counted by \(F\) starts in \(0\), ends nonzero and has no adjacent equality; it is counted once by its symbol sequence. Therefore the number of doubly saturated words for repetition counts \(r,s\) is \([x^{r-1}y^{s-1}]F(x,y)\).

To evaluate the coefficient, put \(C_{r,s}=\binom{r+s}{2r-s}\) for \(r,s\ge1\), with zero outside the binomial range. The denominator gives the recurrence
\[
N_{r,s}=3N_{r-1,s-1}+N_{r-2,s-1}+N_{r-1,s-2}\quad(r,s\ge2),
\]
with \(N_{1,1}=2\), \(N_{1,2}=N_{2,1}=1\), and zeros on the remaining positive-index coordinate edges (any nonpositive index means zero). The candidate binomial numbers obey the same recurrence because, with \(n=r+s\) and \(j=2r-s\),
\[
(1+z)^n=(1+z)^{n-3}\bigl(3z(1+z)+z^3+1\bigr),
\]
and comparison of coefficients of \(z^j\) yields exactly the three terms above. Their boundary data agree. Thus
\[
[x^{r-1}y^{s-1}]F(x,y)=\binom{r+s}{2r-s}.
\]
The binomial coefficient is positive precisely in the triangle \(r\le2s\) and \(s\le2r\). Its symmetry in \(r,s\) follows from \(\binom{r+s}{2r-s}=\binom{r+s}{2s-r}\). This proves the stated count and existence in the triangle. Since all MCS words there have length \(r+s\), and outside the triangle the unique MCS is the contained complete input word of length \(3\min(r,s)\), all maximal common subsequences are longest common subsequences and the length formula follows. \(\square\)

## Verification
Run `python3 verify.py` in the same directory as this document. The verifier independently constructs *all distinct common subsequences* for every \(1\le r,s\le5\), tests maximality by all possible one-letter insertions, compares the actual sets with the described optimizers, checks the binomial counts and lengths, and separately calculates 900 LCS lengths by dynamic programming for \(1\le r,s\le30\). It also verifies the derived rational-series recurrence against the binomial formula at 1,600 coefficient pairs. The actual observed output was `PASS: 25 complete maximal-subsequence sets; 11718 common words; 900 independent LCS DP instances; 1600 transfer coefficients`. These finite experiments are supplementary: the proof above establishes the infinite parameter range.

For illustration, \(\mathcal M(2,2)=\{0101,0102,0121,0201,0202,0212\}\), so its count is \(\binom42=6\). For \(r=s=3\), there are \(\binom63=20\) longest and maximal words; for \((r,s)=(4,2)\), the only one is \((021)^2\).

## Relationship to prior work
General output-sensitive MCS enumeration was established by Conte, Grossi, Punzi and Uno (Algorithmica, 2022), whose accepted manuscript treats arbitrary inputs with a polynomial-delay algorithm and includes Sakai's interspace characterization. Their Theorem 1 and Theorems 2--3 are algorithmic structural results; the material inspected does not state the exact two-parameter binomial MCS count, a full closed description of all optimizer words for these two powers, or the equality of maximal- and longest-subsequence sets in this family. Conte, Grossi, Punzi and Uno (ISAAC 2023; arXiv first public 2023-07-25) develop a compact DAG for general MCS search, counting, ranking and enumeration; their construction applies, but their inspected statement does not present this closed formula or phase transition. The present theorem specializes to a structured ternary string pair and solves its combinatorial counting problem directly. Existing general algorithms can of course compute each fixed instance; that computational implication is not denied. No claim of general MCS enumeration complexity improvement is made.

## Limitations
The result is restricted to the two specified three-letter permutations and positive integral powers. Arbitrary permutations, higher alphabets, cyclic rotations, weighted letters, or occurrence-counted embeddings are not classified. It is a statement about distinct subsequence strings; embeddings of the same string are deliberately identified. The literature comparison cannot exclude an unindexed equivalent formula or a derivation hidden in ancillary examples. Independent external validation of the theorem has not been performed.

## References
1. A. Conte, R. Grossi, G. Punzi, T. Uno, *Enumeration of Maximal Common Subsequences Between Two Strings*, Algorithmica 84 (2022), 757–783, https://doi.org/10.1007/s00453-021-00898-5 . Accepted-manuscript full text: https://arpi.unipi.it/retrieve/bdbfd69d-6f35-448b-9ecc-2aea1e8b05c5/MCS_AAM.pdf .
2. A. Conte, R. Grossi, G. Punzi, T. Uno, *A Compact DAG for Storing and Searching Maximal Common Subsequences*, arXiv:2307.13695, first public 2023-07-25; ISAAC 2023, https://arxiv.org/abs/2307.13695 , https://doi.org/10.4230/LIPIcs.ISAAC.2023.21 .
