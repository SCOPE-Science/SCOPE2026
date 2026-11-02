# Coefficient fingerprints govern logarithmic growth of positive power-sum images

## Finding

Fix an integer \(k\ge2\), an integer \(r\ge1\), and positive integers \(c_1,\ldots,c_r\). Consider the positive additive image of the Cartesian power of the base-\(k\) exponential set,
\[
X_{k,\mathbf c}=\left\{\sum_{i=1}^r c_i k^{e_i}:e_i\in\mathbb N_0\right\}.
\]
Write each coefficient uniquely as \(c_i=k^{v_i}d_i\) with \(v_i\in\mathbb N_0\) maximal, so \(k\nmid d_i\). For each positive integer \(d\), let \(m_d=|\{i:d_i=d\}|\), and put \(M=\prod_{d:m_d>0}m_d!\).

**Theorem (coefficient-fingerprint leading law).** For every such base and coefficient vector,
\[
\boxed{|X_{k,\mathbf c}\cap[0,N)|=\frac{(\log_k N)^r}{M}+O_{k,\mathbf c}\!\bigl((1+\log_k N)^{r-1}\bigr)}\qquad(N\to\infty).
\]
Thus the exact leading coefficient is the reciprocal of the product of the factorials of the equivalence-class sizes under \(c\sim c'\) when one is an integral power-of-\(k\) multiple of the other. It is independent of all other features of the coefficient digits.

The error order cannot in general be improved to \(o((\log N)^{r-1})\): for \(k=2\) and coefficient vector \((1,3)\), **every integer** \(L\ge3\) satisfies
\[
\boxed{|X_{2,(1,3)}\cap[0,2^L)|=L(L-2)}.
\]

## Assumptions and scope

The base is an integer at least two; coefficients are fixed, *strictly positive integers*; exponents range independently over all nonnegative integers. The asymptotic refers to **distinct represented integers**, not to the number of exponent tuples. Positivity is used to bound individual exponents from the size of their sum. The zero coefficient and negative-coefficient cases are not addressed. The integer \(k\) need not be prime. For composite \(k\), maximal divisibility by powers of \(k\) is the intended normalization; ordinary prime-adic valuations are not used.

## Proof

**Step 1: a unique large-gap digit fingerprint.** Let \(W\) be the largest length of a base-\(k\) expansion of any \(d_i\). The last and first digits of each \(d_i\), written with the least significant digit first, are both nonzero: the first is nonzero because \(k\nmid d_i\), and the last is nonzero by definition of length. For a tuple of exponents define its normalized starting positions \(t_i=e_i+v_i\). Call a tuple *separated* when distinct \(t_i\)'s differ by more than \(3W\). Each summand \(d_i k^{t_i}\) occupies a digit interval of width at most \(W\); separation implies these intervals are disjoint, so there are no carries between summands. Every zero gap between successive summand intervals has length at least \(2W\), whereas a zero gap within one summand's nonzero-to-nonzero digit interval has length at most \(W-2\). Consequently, cutting the base-\(k\) expansion at every zero run of length at least \(W\) uniquely recovers all the pairs \((d_i,t_i)\), including each normalized position. (When \(W=1\), every distinct supported digit is a separate block; the same conclusion holds.) Hence two separated tuples have the same sum if and only if their multisets of normalized pairs are equal.

**Step 2: generic tuples dominate.** At a cutoff of \(k^L\), every represented number has a representing tuple satisfying \(0\le e_i<L\): since each coefficient is positive, any \(e_i\ge L\) alone yields at least \(k^L\). There are \(L^r\) exponent tuples in this box. For every fixed pair \(i\ne j\), the constraint \(|(e_i+v_i)-(e_j+v_j)|\le3W\) removes \(O_{k,\mathbf c}(L^{r-1})\) tuples. Also remove tuples in which some normalized start \(t_i\) is within a sufficiently large fixed distance \(B\) of either end of \([0,L]\). This removes another \(O_{k,\mathbf c}(L^{r-1})\) tuples. Take \(B\) larger than all \(v_i\) and \(W\); among the remaining tuples, all normalized starts lie in one common interior interval, so swapping starts between indices of the same primitive coefficient \(d\) preserves admissibility and separatedness. Such permutations act freely since the starts are pairwise distinct. Thus each distinct generic sum has exactly \(M=\prod_d m_d!\) generic preimages. Their number is \(L^r/M+O_{k,\mathbf c}(L^{r-1})\).

**Step 3: bounds for the image.** The generic sums in Step 2 provide an upper bound because at most \(O(L^{r-1})\) other exponent tuples remain. For a lower bound, choose a fixed integer \(C\ge1\) so large that \(\sum_i c_i k^{-C}<1\). Every exponent tuple with \(0\le e_i<L-C\) has total less than \(k^L\). Repeating the separated/interior analysis in that smaller cube gives \((L-C)^r/M+O(L^{r-1})=L^r/M+O(L^{r-1})\) distinct represented numbers below \(k^L\). Therefore
\[
|X_{k,\mathbf c}\cap[0,k^L)|=L^r/M+O_{k,\mathbf c}(L^{r-1}).
\]
For arbitrary real \(N\ge k\), set \(L=\lfloor\log_k N\rfloor\). Monotonicity sandwiches the count at \(N\) between its counts at \(k^L\) and \(k^{L+1}\); their main terms differ by \(O(L^{r-1})\). This gives the stated asymptotic.

**Step 4: exact binary example.** Write \(2^a+3\cdot2^b=2^a+2^b+2^{b+1}\). If \(a=b\), the result has a single binary one, at position \(b+2\); below \(2^L\) there are exactly \(L-2\) such values. If \(a=b+1\), the ones form the pattern \(101\), again giving \(L-2\) results. If \(a=b-1\) or \(a=b+2\), the ones form \(111\), with \(L-2\) results in total; the two representations of each such result are intentionally counted once. In every remaining case, the expansion consists of an adjacent pair of ones in positions \(b,b+1\) and one isolated one strictly below position \(b-1\) or strictly above position \(b+2\). There are \((L-3)(L-2)/2\) choices of each type. The four digit-pattern types are disjoint and exhaustive, so the total is
\[
3(L-2)+(L-3)(L-2)=L(L-2),\qquad L\ge3.
\]
This completes the proof. \(\square\)

## Verification

The accompanying standard-library-only Python program `checker.py` exhaustively forms all represented values below \(2^L\) and checks the exact binary identity for every integer \(3\le L\le22\). It also checks eight coefficient/base families, normalized coefficient multiplicities, and separated-tuple collision rigidity. Expected output is `ALL_CHECKS_OK exact_cutoffs=20 diverse_families=8 generic_tuples=192`. The generic argument above, rather than finite enumeration, proves the theorem for all bases, coefficients, and cutoffs.

## Relationship to prior work

Schulz's 2026 Theorem 3.3 characterizes sparse \(k\)-automatic sets as images of Cartesian powers of the powers of \(k\) under Presburger-definable maps. The present sets are a particularly canonical fixed positive *linear* image family within that framework. His paper does not state a leading constant for the distinct-output counting function; its counting estimates concern polylogarithmic growth order. Krieger, Rampersad and Shallit (2007) determine the polynomial growth **degree** of regular languages, not the coefficient-fingerprint constant for these additive images. The classical Szilard–Yu–Zhang–Shallit decomposition of polynomial-density regular languages provides broader qualitative context. Our specific fingerprint formula and exact illustrative count are not asserted to be consequences merely of those degree/decomposition theorems.

## Limitations

The result is confined to positive integral coefficients and independent nonnegative exponents. It gives a leading coefficient and an optimal-order remainder, not an arbitrary full asymptotic expansion or a uniform error constant as the coefficients vary. Existing general regular-language enumeration techniques may potentially yield an equivalent special-case formula; the older Szilard–Yu–Zhang–Shallit paper was accessible by its abstract but not in full, so historical priority remains a nonzero risk. No claim of independent external validation is made.

## References

1. C. Schulz, *Sublinear Michaux–Villemaire over \((\mathbb N,+,k^\mathbb N)\)*, arXiv:2610.26409v1 (first posted 2026-10-19), especially Theorem 3.3 and Corollary 3.2.
2. D. Krieger, N. Rampersad, J. Shallit, *Finding the growth rate of a regular language in polynomial time*, arXiv:0711.4990v1 (2007), especially Sections 1–3.
3. A. Szilard, S. Yu, K. Zhang, J. Shallit, *Characterizing regular languages with polynomial densities*, Mathematical Foundations of Computer Science 1992, LNCS 629, pp. 494–503, DOI:10.1007/3-540-55808-X_48.
