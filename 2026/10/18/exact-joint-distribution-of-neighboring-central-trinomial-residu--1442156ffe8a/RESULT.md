# Exact joint distribution of neighboring central trinomial residues modulo five

## Finding

Let \(T_n=[x^n](1+x+x^2)^n\) for every integer \(n\geq0\). For every integer \(L\geq0\), and \(u,v\in\{1,2,3,4\}\), let
\[
N_L(u,v)=\#\{0\leq n<5^L:T_n\equiv u\pmod5,\ T_{n+1}\equiv v\pmod5\}.
\]
Put \(r\equiv vu^{-1}\pmod5\), interpreted as an element of \(\{1,2,3,4\}\), and define
\[
E_L=\lceil L/2\rceil,\quad O_L=\lfloor L/2\rfloor,
\quad B_L=(5^L-1-4L)/16.
\]
Use these two lookup vectors, indexed by \(r=1,2,3,4\):
\[
(a_1,a_2,a_3,a_4)=(1,2,1,3),\qquad
(b_1,b_2,b_3,b_4)=(2,4,3,4).
\]
**The exact sixteen-cell law** holds for every \(L\geq0\):
\[
\boxed{N_L(u,v)=B_L+E_L\mathbf1_{u=a_r}+O_L\mathbf1_{u=b_r}
+\mathbf1_{(u,v)=((-1)^L,1)}.}
\]
Here \((-1)^L\) is reduced modulo five. In particular, every pair of nonzero residues occurs once \(L\geq2\). The joint law converges to the uniform distribution on sixteen pairs and its **exact total variation distance** is
\[
\boxed{\frac12\sum_{u,v=1}^{4}\left|\frac{N_L(u,v)}{5^L}-\frac1{16}\right|
=\frac{4L+1}{2\cdot5^L}\qquad(L\geq2).}
\]
For \(L=0\) and \(L=1\), the respective distances are \(15/16\) and \(11/16\). Every \(T_n\) is nonzero modulo five.

For illustration, with \(L=2\), the integer matrix \((N_2(u,v))_{u,v=1}^{4}\) is
\[
\begin{pmatrix}
3&1&2&1\\
1&2&1&2\\
1&2&1&2\\
2&1&2&1
\end{pmatrix}.
\]

## Assumptions and scope

The counts are over integers \(0\leq n<5^L\), **including the last index**, with \(T_{n+1}\) evaluated at its true integer index rather than wrapping around at the cutoff. All residues are modulo the rational prime five. The vector entries \(a_r,b_r\) are ordinary integers in \(\{1,2,3,4\}\). The formula is valid also for the empty one-digit-length window \(L=0\) (one index, \(n=0\)); the closed total-variation expression requires \(L\geq2\).

## Proof

**1. Digit-factorization lemma.** Write \(n=\sum_i d_i5^i\), \(d_i\in\{0,1,2,3,4\}\). Since \(T_n=\operatorname{CT}(x^{-1}+1+x)^n\), the Frobenius congruence yields
\[
(x^{-1}+1+x)^n\equiv\prod_i(x^{-5^i}+1+x^{5^i})^{d_i}\pmod5.
\]
A term with total exponent zero has individual signed exponents \(e_i\in[-d_i,d_i]\subseteq[-4,4]\) with \(\sum_i e_i5^i=0\). Reduction modulo five forces \(e_0=0\); division by five and induction forces every \(e_i=0\). Therefore there is no cross-digit cancellation in the constant term and
\[
T_n\equiv\prod_i T_{d_i}\pmod5.
\]
The exact small values \((T_0,T_1,T_2,T_3,T_4)=(1,1,3,7,19)\) give the nonzero digit weights \(w=(1,1,3,2,4)\pmod5\). Consequently all \(T_n\) are units modulo five.

**2. Uniform prefix products with one distinguished residue.** Let \(P_j(g)\) count all \(j\)-digit base-five words, with leading zeros permitted, whose digit-weight product is \(g\in\mathbb F_5^\times\). For each nontrivial multiplicative character \(\chi\) of this group,
\[
\sum_{d=0}^4\chi(w_d)=2+\chi(2)+\chi(3)+\chi(4)=1,
\]
where the last equality follows from \(1+\chi(2)+\chi(3)+\chi(4)=0\). The trivial-character sum is five. By character orthogonality, for every \(j\geq0\),
\[
\boxed{P_j(g)=\frac{5^j-1}{4}+\mathbf1_{g=1}.}
\]
This includes \(j=0\).

**3. Exact carry partition.** Exclude temporarily \(n=5^L-1\). The base-five expansion of each remaining \(n\) has a unique suffix of \(t\) trailing fours, then a digit \(d\in\{0,1,2,3\}\), then a prefix of \(j=L-t-1\) freely chosen digits, with \(0\leq t<L\). If the prefix weight product is \(P\), digit factorization gives
\[
T_n\equiv(-1)^t w_dP,\qquad T_{n+1}\equiv w_{d+1}P\pmod5.
\]
Consequently, for a prescribed quotient \(r\equiv v/u\pmod5\), the digit \(d\) is uniquely determined because for even \(t\) the four quotients \(w_{d+1}/w_d\) are \((1,3,4,2)\), and for odd \(t\) their negatives are \((4,2,1,3)\), both permutations of \(\mathbb F_5^\times\). The corresponding value \((-1)^tw_d\), indexed by \(r=1,2,3,4\), is precisely \(a_r\) for even \(t\), and \(b_r\) for odd \(t\). For fixed \(t,u,v\), the number of prefixes is therefore
\[
P_j(u/a_r)\text{ if \(t\) is even, or }P_j(u/b_r)\text{ if \(t\) is odd}.
\]
The ordinary prefix contribution is
\[
\sum_{t=0}^{L-1}\frac{5^{L-t-1}-1}{4}
=\frac{5^L-1-4L}{16}=B_L.
\]
There are exactly \(E_L\) even indices \(t\) and \(O_L\) odd ones in this interval, giving the two indicator terms.

The excluded endpoint \(n=5^L-1\) consists of \(L\) fours, so \((T_n,T_{n+1})\equiv((-1)^L,1)\pmod5\). This produces the final indicator, proving the sixteen-cell identity, even at \(L=0\).

**4. Exact discrepancy and positivity.** The baseline deviation from the uniform cell count \(5^L/16\) is \(-q\), where \(q=(4L+1)/16\). For each of the four quotients \(r\), the cells \(u=a_r\) and \(u=b_r\) are distinct. Thus precisely eight of the sixteen cells receive positive adjustments \(E_L\) or \(O_L\), and the remaining eight receive no adjustment. The endpoint is one of those eight adjusted cells (\(a_1\) for even \(L\), \(b_4\) for odd \(L\)). For every \(L\geq2\), both \(E_L-q\) and \(O_L-q\) are strictly positive. Hence the total positive deviation of the sixteen unnormalized counts equals
\[
4E_L+4O_L+1-8q=\frac{4L+1}{2}.
\]
The total deviation over all cells vanishes because there are exactly \(5^L\) indices, so this positive deviation divided by \(5^L\) is precisely the total-variation distance. For \(L\geq2\), \(B_L\geq1\), giving every cell a positive count. At \(L=0,1\), direct substitution in the sixteen-cell formula gives the two exceptional distances.

## Verification

The standalone `verify.py` uses exact integer arithmetic. It independently constructs the first 261 central trinomial numbers by their three-term recurrence and binomial formula, tests the base-five digit product for those indices, enumerates every \(n<5^L\) for \(0\leq L\leq7\), matches all sixteen exact counts, and checks total variation as rational numbers. It also independently regenerates both carry-permutation vectors. Run `python3 verify.py` from the directory containing this document. Expected status: `VERIFY_OK`. These finite checks are not substituted for the preceding all-\(L\) proof.

## Relationship to prior work

The Lucas digit product for central trinomial coefficients modulo primes is known; Deutsch and Sagan initiated related congruence study, and Rowland and Yassawi explicitly identify the Lucas product and general automaton methods in Sections 4.2 and 5.1 of their paper. The theorem here is **not** a claim to rediscover that digit product. It derives a new, explicit and sharp **two-point law for consecutive indices** after base-five carries. Unlike marginal product frequencies, the neighboring joint law requires an exact carry-suffix partition and yields the finite-scale sharp total-variation constant.

The later study by Kohen proves a general offset-carry decomposition (Lemma 8), uses it to determine zero densities of linear combinations of nearby trinomial coefficients, and explicitly considers the equality \(T_n\equiv T_{n+1}\pmod p\) in the density of a related sequence (Proposition 14). That is substantial overlap in **method and certain marginal events**: the present theorem does not claim those as new. Kohen does not state the finite-scale sixteen-cell distribution of the ordered pair \((T_n,T_{n+1})\) or the exact total-variation formula. An independently identified previous two-point formula, or a stronger theorem explicitly entailing it, would supersede the novelty assertion.

## Limitations

Only modulo-five adjacent *ordered* pairs on exact initial intervals \([0,5^L)\) are classified. The result says nothing about higher prime powers, non-dyadic-like cutoffs in base five, longer patterns, or uniform error bounds over arbitrary \([0,N)\). General Lucas-product machinery is a strong predecessor and may permit a more general joint-law specialization elsewhere in the literature. Priority and mathematical correctness have not received independent validation.

## References

1. E. Deutsch and B. E. Sagan, *Congruences for Catalan and Motzkin numbers and related sequences*, arXiv:math/0407326, publicly posted 19 July 2004. https://arxiv.org/abs/math/0407326
2. E. Rowland and R. Yassawi, *Automatic congruences for diagonals of rational functions*, arXiv:1310.8635, publicly posted 31 October 2013, especially Sections 4.2 and 5.1. https://arxiv.org/html/1310.8635v2
3. N. Kohen, *Density and Symmetry in the Generalized Motzkin Numbers mod p*, arXiv:2411.03681, publicly posted 6 November 2024, especially Sections 1--3. https://arxiv.org/html/2411.03681v2
4. OEIS, A002426, central trinomial coefficients, https://oeis.org/A002426
