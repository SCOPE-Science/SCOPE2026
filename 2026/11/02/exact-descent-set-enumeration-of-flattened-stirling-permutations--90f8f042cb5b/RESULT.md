# Exact descent-set enumeration of flattened Stirling permutations

## Finding

Let \(n\ge1\), and let \(\mathcal F_n\) be the set of flattened Stirling permutations on the multiset \(\{1,1,\ldots,n,n\}\). A Stirling permutation has all letters between the two copies of \(i\) greater than \(i\); it is flattened when the leading letters of its maximal weakly increasing runs are weakly increasing. Define its descent set by
\[
\operatorname{Des}(w)=\{j\in\{1,\ldots,2n-1\}:w_j>w_{j+1}\}.
\]
For any \(T\subseteq\{1,\ldots,2n-1\}\), let \(N_n(T)=|\{w\in\mathcal F_n:\operatorname{Des}(w)=T\}|\).

Here is a **positive finite binomial-sum formula for every exact descent set**. Consider all data consisting of an integer \(b\ge1\), a nonnegative integer \(k\), positive integers \(s_1,\ldots,s_k\), and integers \(q_i\) with \(0\le q_i<s_i\), subject to \(b+s_1+\cdots+s_k=n\). Empty sequences are allowed when \(k=0\). Write \(a_0=b\) and \(a_i=b+\sum_{j=1}^{i}s_j\). Define the set
\[
\Delta(b,\mathbf s,\mathbf q)
=\bigl(\{2b-1\}\text{ if }b\ge2;\ \emptyset\text{ otherwise}\bigr)
\cup\bigcup_{i=1}^{k}\Bigl[
\bigl(\{2a_{i-1}+2q_i\}\text{ if }q_i>0;\ \emptyset\text{ otherwise}\bigr)
\cup
\bigl(\{2a_i-1\}\text{ if }s_i-q_i\ge2;\ \emptyset\text{ otherwise}\bigr)
\Bigr].
\]
Then, for every \(n\ge1\) and every such \(T\),
\[
\boxed{
N_n(T)=
\sum_{\substack{b,k,\mathbf s,\mathbf q\\ b+\sum_i s_i=n\\\Delta(b,\mathbf s,\mathbf q)=T}}
\binom{n-1}{b-1}
\prod_{i=1}^{k}
\binom{n-a_{i-1}-1}{s_i-1}\binom{s_i-1}{q_i}.
}
\tag{1}
\]
For \(k=0\), the product is \(1\). All summands are nonnegative integers.

This determines the complete **ordered run-length composition**: for any composition \(\lambda=(\lambda_1,\ldots,\lambda_d)\) of \(2n\), the number of flattened Stirling permutations with successive run lengths exactly \(\lambda_1,\ldots,\lambda_d\) equals \(N_n(\{\lambda_1,\lambda_1+\lambda_2,\ldots,\lambda_1+\cdots+\lambda_{d-1}\})\). In particular, if \(d\mid2n\), the number with exactly \(d\) runs all having length \(2n/d\) is
\[
\boxed{E_{n,d}=N_n\bigl(\{2n/d,2(2n/d),\ldots,(d-1)(2n/d)\}\bigr).}\tag{2}
\]
If \(d\nmid2n\), the count is zero. Formula (1) is an explicit answer for every admissible \(n,d\), rather than a search over permutations or an unproved recurrence.

There is also an exact arithmetic algorithm for \(N_n(T)\) requiring \(O(n^3)\) arithmetic operations after binomial preprocessing. For example, \(E_{6,3}=8\), \(E_{9,3}=243\), \(E_{12,3}=5576\), \(E_{8,4}=48\), and \(E_{10,5}=384\).

## Assumptions and scope

The words, positions, and colors of blocks are labeled: permutations are not identified under relabeling, reversal, or cyclic symmetry. Descent indices are one-based and lie strictly between consecutive letters. Runs are maximal **weakly** increasing factors; their lengths sum to \(2n\). No assertion is made for higher-multiplicity Stirling permutations. Binomial coefficients in (1) have nonnegative arguments because each block includes the currently smallest unused label. The sole empty-block convention is that \(k=0\) is permitted when \(b=n\); all \(s_i\) are otherwise positive.

## Proof

We use, and explicitly credit, the canonical type-\(B\) set-partition bijection of Buck, Elder, Figueroa, Harris, Harry, and Simpson (2023, Theorem 3.9). This is a known ingredient, **not** a claimed new bijection. In its canonical representation, a type-\(B\) partition of the signed labels associated with \(\{1,\ldots,n\}\) has a zero block \(P_0\) containing \(1\) and, in increasing order of least positive element, ordinary blocks \(N_iP_i\). In each ordinary block, \(P_i\) contains its least absolute label, and \(N_i\) contains the negative choices among the other labels; write \(|P_0|=b\), \(|N_i|=q_i\), and \(|P_i|=s_i-q_i\). Thus \(s_i\ge1\) and \(0\le q_i<s_i\).

**Exact multiplicities of shapes.** Choose the other \(b-1\) positive labels in \(P_0\) from the \(n-1\) labels other than \(1\), giving \(\binom{n-1}{b-1}\) choices. Now \(r_i=n-a_{i-1}\) labels remain when block \(i\) is opened. Its smallest remaining label must be in that block and positive. Choose \(s_i-1\) of the other \(r_i-1\) labels; exactly \(q_i\) of those chosen are negative. This gives
\[
\binom{r_i-1}{s_i-1}\binom{s_i-1}{q_i}
\]
choices, independent of prior sign choices. The next block again contains the smallest still-unused label. Consequently every canonical partition has exactly one size/sign profile \((b,\mathbf s,\mathbf q)\), every such profile is admissible, and its number of realizations is the product appearing in (1). There is no missing factor for ordering the ordinary blocks: that order is forced by their minima.

**Location of descents.** The cited bijection maps the partition into a concatenation
\[
g(P_0)\,f(N_1)g(P_1)\cdots f(N_k)g(P_k).
\]
For an increasing list \(v_1<\cdots<v_t\), the fragment \(f\) consists of \(v_1v_1\cdots v_tv_t\), whereas \(g\) consists of \(v_1v_2v_2\cdots v_tv_tv_1\); if \(t=1\), both are \(v_1v_1\). The zero-block fragment has a unique internal descent after its \((2b-1)\)st letter when \(b\ge2\), and none when \(b=1\).

In ordinary block \(i\), the negative fragment has \(2q_i\) letters and is weakly increasing. When \(q_i>0\), its final letter exceeds the first (least positive) letter of \(g(P_i)\), so a descent occurs at global position \(2a_{i-1}+2q_i\). Within \(g(P_i)\) itself, there is one descent just before the final copy of its least positive letter if and only if \(|P_i|=s_i-q_i\ge2\), at position \(2a_i-1\). The last letter of every positive fragment is its block minimum; the next block begins with a letter larger than that minimum, because the block minima strictly increase and every negative magnitude is larger than its own block minimum. Hence **no descent occurs across block boundaries**. These are all descents, and their positions are exactly \(\Delta(b,\mathbf s,\mathbf q)\). Summing the exact shape multiplicities conditional on \(\Delta=T\) proves (1). A run ends precisely at a descent, which proves (2) and the general ordered composition statement.

**Polynomial arithmetic evaluation.** Fix the indicator vector of \(T\). Choose \(b\) first and test the cuts internal to the first \(2b\) letters. For a suffix of \(r\) remaining labels, its starting character offset is forced to be \(p=2(n-r)\), regardless of previous choices. For every \(1\le s\le r\) and \(0\le q<s\), test whether the proposed internal descent set \(\{p+2q:q>0\}\cup\{p+2s-1:s-q\ge2\}\) is exactly the portion of \(T\) in the index interval from \(p\) through \(p+2s-1\); this interval includes the boundary index \(p\), which must not be a descent. A prefix-sum array for the indicator of \(T\) and at most two membership tests give an \(O(1)\) test. Multiply by \(\binom{r-1}{s-1}\binom{s-1}{q}\) and recurse to \(r-s\), using a single memoized value for each \(r\). There are \(O(n)\) suffix states and \(O(r^2)\) transitions per state, proving \(O(n^3)\) arithmetic operations. The included `verify.py` implements exactly this algorithm and a separate unrestricted block-profile evaluation.

## Verification

Execute `python3 verify.py` in the directory containing this file and the supplied script. It independently generates **all** \((2n-1)!!\) Stirling permutations by insertion of adjacent copies of the next maximum, filters using the original flattened-run definition, and compares every descent-set count from (1) for \(1\le n\le8\). It separately checks the published run-count table through \(n=10\), evaluates six equal-length cases (including \(E_{12,3}=5576\)), and compares the polynomial-time prescribed-descent dynamic program against every formula profile through \(n=8\). The script completed successfully with `VERIFY_OK`. The exhaustive work covers only those finite orders; the proof above establishes all \(n\).

## Relationship to prior work

Buck et al. (arXiv:2306.13034, first posted 2023-06-22) proved the type-\(B\) bijection, analyzed *the number* of runs and posted equal-run-length enumeration as Open Problem 3. Their bijection is the starting point here, not a new contribution. Shankar (arXiv:2307.07730, first posted 2023-07-15) solved their proposed total-count formula and gave generating functions for the *total number* of descents for all multiplicities, as well as the maximum-run count. Those univariate descent distributions are obtained by summing the present position-specific counts by \(|T|\), but they do not state the individual \(N_n(T)\) or the equal-length specialization. The new statement is the explicit exact **descent-position and ordered run-composition refinement** with a positive coefficient formula and \(O(n^3)\) arithmetic extraction. Similar terminology for ordinary flattened permutations or flattened parking functions concerns different objects.

The full relevant source text and the primary formulations, rather than merely their titles, were compared. This is a self-review originality assessment, not an independent publication-priority certificate. Equivalent unindexed results, or a prior multivariate refinement not uncovered in the searches, remain possible.

## Limitations

This formula is an exact positive finite sum and a polynomial-time arithmetic computation; it is **not** claimed to be a simple product, a fixed-order scalar recurrence in \(n\), or a closed analytic generating function for every run composition. It uses the known type-\(B\) bijection as an essential premise. Publication priority, independent mathematical audit, and generalization to all higher-multiplicity Stirling words remain unestablished. Computation through finite orders cannot establish the infinite identity without the preceding proof.

## References

1. A. Buck, J. Elder, A. A. Figueroa, P. E. Harris, K. Harry, and A. Simpson, *Flattened Stirling Permutations*, first posted 2023-06-22, arXiv:2306.13034, especially Theorem 3.9, Lemma 4.1, Table 1, and Open Problem 3. https://arxiv.org/abs/2306.13034
2. U. Shankar, *Enumeration of flattened k-Stirling permutations with respect to descents*, first posted 2023-07-15, arXiv:2307.07730, especially the descent-enumerating exponential generating function (Theorem 8) and Section 5. https://arxiv.org/abs/2307.07730
3. V. È. Adler, *Set partitions and integrable hierarchies*, Theoretical and Mathematical Physics **187** (2016), 455–486, for canonical signed-partition notation, as cited by Buck et al.
