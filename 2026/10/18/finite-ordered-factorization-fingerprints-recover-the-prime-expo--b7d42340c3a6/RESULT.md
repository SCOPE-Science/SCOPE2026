# Finite ordered-factorization fingerprints recover the prime-exponent shape

## Finding

Let \(n>1\), let \(r=\omega(n)\) denote its number of distinct prime factors, and let \(c_j(n)\) count ordered factorizations of \(n\) into exactly \(j\) integers greater than one. If \(n,m>1\) have the same \(r\ge1\) and
\[
c_j(n)=c_j(m)\qquad(1\le j\le r+1),
\]
then the multisets of positive exponents in their prime factorizations are identical. Conversely, identical prime-exponent multisets give equality of every \(c_j\). Thus the first \(r+1\) coefficients of the nontrivial divisor polynomial \(P(n,z)=\sum_{j\ge1}c_j(n)z^{j-1}\) determine the entire polynomial and the unordered prime-exponent shape, regardless of the size of the exponents.

The length \(r+1\) cannot be shortened to \(r\) for \(r=1,2,3,4\). This sharpness assertion is **only** for those four support sizes.

## Assumptions and scope

All integers exceed one. The support size \(r=\omega(n)=\omega(m)\) is known and is the same on both sides. Repeated exponents are permitted; the identity of the primes themselves is neither recovered nor asserted. The samples are the nontrivial **ordered** factorization counts, not the unordered multiplicative-partition counts. Each \(P(n,z)\) is a finite polynomial because no more than \(\Omega(n)\) factors greater than one can occur. No bound on \(\Omega(n)\) is imposed.

## Proof

Write \(n=\prod_{i=1}^{r}p_i^{a_i}\), where each \(a_i\ge1\), and let \(d_t(n)\) count ordered \(t\)-tuples of positive integers, with units allowed, whose product is \(n\). Selecting the \(j\) nonunit positions gives the exact binomial transform
\[
d_t(n)=\sum_{j=1}^{t}\binom tj c_j(n),\qquad t\ge1.
\]
Distributing the \(a_i\) copies of each prime across \(t\) positions (stars and bars) gives
\[
d_t(n)=\prod_{i=1}^{r}\binom{t+a_i-1}{a_i}.
\]
In particular, every \(d_t(n)\) is positive. Taking consecutive ratios yields
\[
\frac{d_{t+1}(n)}{d_t(n)}=\prod_{i=1}^r\frac{t+a_i}{t}.
\]
Define the **monic** degree-\(r\) polynomial
\[
H_n(T)=\prod_{i=1}^{r}(T+a_i).
\]
For each positive integer \(t\),
\[
H_n(t)=t^r\frac{d_{t+1}(n)}{d_t(n)}.
\]
Knowing \(c_1(n),\ldots,c_{r+1}(n)\) therefore gives \(d_1(n),\ldots,d_{r+1}(n)\) and the values \(H_n(1),\ldots,H_n(r)\). If \(m\) has the same prime-support size and the same \(c_j\) through \(r+1\), then \(H_m-H_n\) has degree at most \(r-1\) but vanishes at the \(r\) distinct integers \(1,\ldots,r\). Hence \(H_m=H_n\). Equality of factorizations of this monic polynomial into linear factors over \(\mathbb Z\) gives equality, with multiplicity, of \(\{a_1,\ldots,a_r\}\) and the exponent multiset of \(m\).

Conversely, equality of exponent multisets gives equality of the products for \(d_t\) for all \(t\ge1\). The triangular binomial transform is invertible, so the entire sequence of \(c_j\), and thus \(P\), agrees.

A constructive recovery algorithm computes each \(d_t\) from the given \(c_j\), interpolates the monic polynomial \(H_n(T)\) using \(H_n(1),\ldots,H_n(r)\), and reads off the negative integer roots, counted with multiplicity. The integrality and positivity of the recovered exponents follow because the data originate from a positive integer of support \(r\).

For sharpness at the stated sizes, choose any distinct primes and give them the following exponent multisets:

* \(r=1\): \((1)\) and \((2)\) have equal \(d_1=1\), but \(d_2\) equals \(2\) and \(3\), respectively.
* \(r=2\): \((1,5)\) and \((2,3)\) have equal \(d_1=1\) and \(d_2=12\), but \(d_3=63\) and \(60\).
* \(r=3\): \((1,6,8)\) and \((2,2,13)\) have equal \(d_1=1\), \(d_2=126\), \(d_3=3780\), but \(d_4=55440\) and \(56000\).
* \(r=4\): \((3,7,11,74)\) and \((4,4,17,63)\) have equal \(d_1=1\), \(d_2=28800\), \(d_3=80028000\), \(d_4=63903840000\), but \(d_5=22488659943750\) and \(22478175720000\).

Because the binomial transform between the first \(r\) entries of \(d\) and \(c\) is invertible, each pair has identical \(c_1,\ldots,c_r\) yet distinct exponent multisets. Therefore the first \(r\) nontrivial factorization counts do not suffice in these four support sizes. No assertion is made about necessity of \(r+1\) counts for larger \(r\).

## Verification

The standalone standard-library script `CHECKER.py` exactly reconstructs the exponent multiset from \(c_1,\ldots,c_{r+1}\) for 33,487 tested multisets across support sizes \(1\le r\le5\), and separately checks the three sharpness witness pairs for \(r=2,3,4\), using arbitrary-precision integers and fractions. Run `python3 CHECKER.py`. The elementary \(r=1\) witness is verified directly above. These are finite regression checks; the proof for every \(r\) is the polynomial identity and interpolation argument, not an extrapolation from the tests.

## Relationship to prior work

Huxley, Lettington and Schmidt's 2026 work defines and investigates the nontrivial divisor-function polynomial, including its Dirichlet series and special values. Hill, Huxley, Lettington and Schmidt's earlier work develops ordered nontrivial divisor functions and binomial transforms. The classical positive-factor count has a stars-and-bars Euler-factor formula. The finite-support inverse statement here combines these standard identities with the monic-ratio interpolation argument, and exhibits concrete sharpness at small support sizes. It is not a claim of novelty for either the binomial transform or the individual divisor-count formulas. Known source statements inspected did not explicitly establish the finite \(r+1\) fingerprint or the four support-size sharpness witnesses; unindexed or implicit prior derivations remain possible.

## Limitations

The support size must be known and common to both integers. The prime values cannot be recovered. The count \(r+1\) is proved sufficient for all \(r\), but optimal only for \(1\le r\le4\); no optimality statement is offered beyond these cases. The polynomial interpolation proof is constructive but does not address stability under approximate/noisy factorization counts or the computational cost of factoring large integers. Earlier literature may contain an equivalent reformulation not located by the searches.

## References

1. M. N. Huxley, M. C. Lettington and K. M. Schmidt, *On Divisor Function Polynomials and Dirichlet Series* (2026), arXiv:2610.13864v1, https://arxiv.org/html/2610.13864v1 (first public version 2026-10-09).
2. S. L. Hill, M. N. Huxley, M. C. Lettington and K. M. Schmidt, *Some properties and applications of non-trivial divisor functions*, Ramanujan Journal 51 (2020), 611–628.
3. M. C. Lettington and K. M. Schmidt, *Divisor functions and the number of sum systems* (2020), on generalized divisor functions and sum-system enumeration.
4. H. G. Hylock, M. C. Lettington and K. M. Schmidt, *On c-polynomial factorisations* (2026), arXiv:2609.38567, https://arxiv.org/abs/2609.38567.
