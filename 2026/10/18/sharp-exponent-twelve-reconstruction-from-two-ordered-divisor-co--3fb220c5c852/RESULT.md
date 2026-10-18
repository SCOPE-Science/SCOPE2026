# Sharp exponent-twelve reconstruction from two ordered divisor counts

## Finding

For a positive integer \(n\), let \(d_k(n)\) denote the number of ordered \(k\)-tuples of positive integers with product \(n\), and let \(\mathcal E(n)\) be the **multiset** of positive exponents in the prime factorization of \(n\). Put \(\tau(n)=d_2(n)\). The following injectivity statement is sharp:

**Theorem.** Suppose \(m,n\ge2\) and every prime exponent in both \(m\) and \(n\) is at most \(12\). If
\[
\bigl(\tau(m),d_3(m)\bigr)=\bigl(\tau(n),d_3(n)\bigr),
\]
then \(\mathcal E(m)=\mathcal E(n)\). The exponent bound \(12\) cannot be replaced by \(13\): the two distinct exponent multisets \(\{2,2,13\}\) and \(\{1,6,8\}\) both give
\[
\bigl(\tau,d_3\bigr)=(126,3780).
\]
Consequently \(12\) is the **largest uniform prime-exponent cutoff** for which the pair of ordered two-factor and three-factor counts determines the prime-exponent multiset.

## Assumptions and scope

Only positive integers and their usual integer prime factorizations are involved. Prime bases themselves are not determined by the two statistics, and the theorem asserts equality only of the unordered multisets of prime exponents. Factors equal to \(1\) are permitted in the ordered factorizations defining \(d_k\). No restriction is imposed on the number of distinct prime factors or on the magnitude of the integers.

## Proof

**1. Local formula.** If \(n=\prod_p p^{e_p}\), distribute each exponent \(e_p\) among \(k\) ordered factors by stars and bars. The multiplicative factorization count is therefore
\[
d_k(n)=\prod_{p\mid n}\binom{e_p+k-1}{k-1}.
\]
Write \(c_e(n)=\#\{p:\nu_p(n)=e\}\). For exponents at most \(12\), this yields
\[
\tau(n)=\prod_{e=1}^{12}(e+1)^{c_e(n)},\qquad
 d_3(n)=\prod_{e=1}^{12}\binom{e+2}{2}^{c_e(n)}.
\]

**2. Twelve independent valuation measurements.** Let \(q_1,\ldots,q_6=(2,3,5,7,11,13)\) and form the vector
\[
\mathbf y(n)=\bigl(\nu_{q_j}(\tau(n))\bigr)_{j=1}^6\mathbin{\|}\bigl(\nu_{q_j}(d_3(n))\bigr)_{j=1}^6.
\]
Then \(\mathbf y(n)=A\mathbf c(n)\) for the integer matrix \(A\) whose entries are
\[
A_{j,e}=\nu_{q_j}(e+1),\qquad A_{6+j,e}=\nu_{q_j}\!\left(\binom{e+2}{2}\right),
\quad 1\le j\le6,\quad 1\le e\le12.
\]
For complete reproducibility, its twelve rows, with columns indexed by \(e=1,\dots,12\), are:

```text
1 0 2 0 1 0 3 0 1 0 2 0
0 1 0 0 1 0 0 2 0 0 1 0
0 0 0 1 0 0 0 0 1 0 0 0
0 0 0 0 0 1 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 1 0 0
0 0 0 0 0 0 0 0 0 0 0 1
0 1 1 0 0 2 2 0 0 1 1 0
1 1 0 1 1 0 2 2 0 1 1 0
0 0 1 1 0 0 0 1 1 0 0
0 0 0 0 1 1 0 0 0 0 0 1
0 0 0 0 0 0 0 0 1 1 0 0
0 0 0 0 0 0 0 0 0 0 1 1
```

Direct exact integer elimination on this displayed matrix gives
\[
\det A=1.
\]
The enclosed `verify.py` reconstructs every matrix entry from its defining prime valuations and independently evaluates the determinant by fraction-free Bareiss elimination, testing each exact division. Because \(A\) is invertible over the integers (in particular, over the rationals), equal pairs \(\bigl(\tau,d_3\bigr)\) give equal vectors \(\mathbf y\), hence equal \(\mathbf c\). The multiplicity vector \(\mathbf c\) is exactly the prime-exponent multiset.

**3. Sharp failure at exponent thirteen.** For the two exponent multisets in the theorem, the local-factor formulas give
\[
3\cdot3\cdot14=2\cdot7\cdot9=126,
\]
\[
6\cdot6\cdot105=3\cdot28\cdot45=3780.
\]
For instance, \(2^2\,3^2\,5^{13}\) and \(2\,3^6\,5^8\) realize the two multisets. Thus injectivity fails already at exponent cutoff \(13\); it cannot fail at any smaller cutoff by Step 2. This proves the sharp statement. \(\square\)

## Verification

Run `python3 verify.py` with the Python 3 standard library. It constructs the \(12\times12\) matrix directly from the local factor formula, certifies determinant \(1\) using integer-only Bareiss elimination, and checks the exponent-\(13\) linear relation. It separately enumerates ordered factorizations for every integer from \(2\) through \(400\), comparing them against the multiplicative formulas, and explores bounded exponent signatures for consistency. The full theorem relies on the invertible integer matrix and factorization identities, not on the finite sanity checks.

## Relationship to prior work

The recent paper by Huxley, Lettington and Schmidt develops generating polynomials for ordered factorization functions, their Dirichlet series, and special squarefree cases [1]. The earlier Lettington–Schmidt paper develops associated divisor functions and formulas for sum-system enumeration [2]. The present theorem instead asks how much arithmetic prime-power information is retained by **only the two low-order factorization statistics** \(d_2\) and \(d_3\). Neither inspected paper states the sharp exponent cutoff or the determinant-one recovery matrix. The new assertion is not a claim that divisor-function formulas or ordered-factorization counts themselves are new.

## Limitations

The result concerns the **multiset of exponents**, not the prime bases or equality of integers. At exponent cutoff \(13\) injectivity fails, but this does not classify all collisions or reconstruct exponents beyond the cutoff. The determinant is a finite exact certificate; independent mathematical review has not been performed. Literature indexing is incomplete, so earlier specialized work on pairs of divisor values may remain undiscovered.

## References

[1] M. N. Huxley, M. C. Lettington, K. M. Schmidt, *On Divisor Function Polynomials and Dirichlet Series*, arXiv:2610.13864v1, first posted 9 October 2026, https://arxiv.org/html/2610.13864v1.

[2] M. C. Lettington, K. M. Schmidt, *Divisor Functions and the Number of Sum Systems*, *Integers* **20** (2020), A61; arXiv:1910.02455v1, https://orca.cardiff.ac.uk/id/eprint/133889/.
