# Maximal nilpotency index in products of random upper triangular matrices

## Finding
Let \(q\) be a prime power, let \(n\ge 2\), and let \(T_n(q)\) be the algebra of upper triangular \(n\times n\) matrices over \(\mathbb F_q\). Choose \(A,B\in T_n(q)\) independently and uniformly, and put \(N=AB\). Define the nilpotency index of a nilpotent matrix \(N\) to be the least positive integer \(r\) with \(N^r=0\).

The number of **ordered pairs** for which \(N\) is nilpotent of **maximal possible index \(n\)** is

\[
\boxed{q^{(n-1)^2}(q-1)^{2n-2}\big((n+1)q-1\big).}
\]

The exact conditional probability among pairs with nilpotent product is

\[
\boxed{\Pr\big(N^{n-1}\ne 0\mid N^n=0\big)
=\frac{(q-1)^{2n-2}((n+1)q-1)}{q^{n-1}(2q-1)^n}.}
\]

For fixed \(n\) this probability tends to \((n+1)/2^n\) as \(q\to\infty\); for fixed \(q\) it decays exponentially in \(n\). In contrast, a *uniformly chosen strictly upper triangular matrix* has maximal index with probability \((1-1/q)^{n-1}\), so the product-conditioned law is quantitatively different from the uniform nilpotent law.

## Assumptions and scope
All field sizes \(q\ge 2\) are prime powers; all matrix sizes are integers \(n\ge2\). The probability distribution is on ordered pairs of elements of the full upper triangular matrix algebra, including singular matrices. It is **not** the distribution obtained by multiplying two already nilpotent matrices or by conditioning each factor individually. We count labeled matrices in their fixed standard basis, not conjugacy classes. The nilpotent product condition is \(N^n=0\), and maximal index is the conjunction \(N^n=0\), \(N^{n-1}\ne0\).

## Proof
Write \(a_i=A_{ii}\), \(b_i=B_{ii}\). As \(AB\) is upper triangular, it is nilpotent exactly when its diagonal vanishes, namely when \(a_i b_i=0\) for every \(i\). There are \(2q-1\) possible ordered scalar pairs \((a_i,b_i)\) with zero product. The off-diagonal entries of \(A\) and \(B\) remain arbitrary, yielding exactly

\[
q^{n(n-1)}(2q-1)^n
\]

ordered pairs with nilpotent product. This recovers the nilpotent-product probability \(((2q-1)/q^2)^n\) found for triangular matrix rings in the cited work of Sarma and Subedi, without assuming any further structural claim from that paper.

For every strictly upper triangular \(n\times n\) matrix \(N\), the sole entry that can be nonzero in \(N^{n-1}\) is its \((1,n)\) entry, and matrix multiplication gives the identity

\[
(N^{n-1})_{1n}=\prod_{i=1}^{n-1}N_{i,i+1}.
\]

Thus a nilpotent product has index exactly \(n\) if and only if every entry of its first superdiagonal is nonzero.

Condition on \(a_i b_i=0\) for all \(i\). Label each diagonal pair by one of three mutually exclusive types:

* \(L\): \(a_i\ne0\), \(b_i=0\); weight \(q-1\).
* \(R\): \(a_i=0\), \(b_i\ne0\); weight \(q-1\).
* \(Z\): \(a_i=b_i=0\); weight \(1\).

Weights count the underlying choices of diagonal values; the total weight over all words of length \(n\) is \((2q-1)^n\).

For each \(1\le i<n\), multiplication yields

\[
N_{i,i+1}=a_i B_{i,i+1}+A_{i,i+1}b_{i+1}.
\]

If \(a_i=b_{i+1}=0\) then this entry is forced to zero. Otherwise, at least one coefficient is nonzero, and the two indicated free off-diagonal entries are independent uniform field elements. Consequently \(N_{i,i+1}\) is uniform in \(\mathbb F_q\) and is nonzero with probability \((q-1)/q\). Distinct values of \(i\) use disjoint off-diagonal coordinates, so these nonzero events are independent after fixing the diagonal.

In terms of types, the \(i\)-th superdiagonal entry can be nonzero exactly when the type at \(i\) is \(L\), or the type at \(i+1\) is \(R\). The permitted adjacent transitions therefore consist of \(L\) followed by any type, or \(R\) or \(Z\) followed by \(R\). All permitted length-\(n\) strings are *uniquely* of one of the forms

\[
L^kR^{n-k}\quad (0\le k\le n),
\qquad
L^k ZR^{n-k-1}\quad(0\le k<n).
\]

Let \(u=q-1\). The total weight of the first family is \((n+1)u^n\), and that of the second family is \(nu^{n-1}\). Hence the total weight of compatible diagonal tuples is

\[
C_n=(n+1)(q-1)^n+n(q-1)^{n-1}
=(q-1)^{n-1}((n+1)q-1).
\]

For each compatible diagonal tuple, all \(n-1\) superdiagonal entries are independently nonzero with probability \(((q-1)/q)^{n-1}\). The resulting conditional probability is

\[
\frac{C_n}{(2q-1)^n}\left(\frac{q-1}{q}\right)^{n-1}
=\frac{(q-1)^{2n-2}((n+1)q-1)}{q^{n-1}(2q-1)^n}.
\]

Multiplying by the previously counted \(q^{n(n-1)}(2q-1)^n\) nilpotent pairs proves the integer counting formula. Letting \(q\to\infty\) at fixed \(n\) gives \((n+1)/2^n\). For fixed \(q\), the conditional probability can also be written as

\[
\frac{(n+1)q-1}{2q-1}\left(\frac{(q-1)^2}{q(2q-1)}\right)^{n-1},
\]

whose exponential base is strictly smaller than one. Finally, a uniformly chosen strictly upper triangular matrix has independent uniform first-superdiagonal entries, proving the comparison formula. This completes the proof for every field size and dimension in the stated range.

## Verification
The standalone source file `verify.cpp` exhaustively enumerates ordered upper triangular matrix pairs over the prime fields for \((n,q)=(2,2),(2,3),(2,5),(3,2),(3,3),(4,2)\). It directly forms their product and separately tests zero diagonal and all nonzero first-superdiagonal entries. The independently programmed state-word enumeration checks the compatible-diagonal polynomial at every \(2\le n\le8\) for \(q\in\{2,3,4,5,7\}\) (where only the integer value of \(q\) enters this latter check).

The exhaustive count of nilpotent ordered pairs followed by maximal-index ordered pairs is, respectively:

| \((n,q)\) | Nilpotent pairs | Maximal-index pairs |
| --- | ---: | ---: |
| \((2,2)\) | 36 | 10 |
| \((2,3)\) | 225 | 96 |
| \((2,5)\) | 2025 | 1120 |
| \((3,2)\) | 1728 | 112 |
| \((3,3)\) | 91125 | 14256 |
| \((4,2)\) | 331776 | 4608 |

Build and run with `c++ -O2 -std=c++17 verify.cpp -o verify && ./verify`. The program prints `VERIFY_OK` after all assertions succeed. Exhaustion at the listed finite sizes is an independent check of examples, **not** a substitute for the universal symbolic proof.

## Relationship to prior work
Sarma and Subedi, *Nilpotent Product Probability of Finite Rings* (arXiv:2610.07892v1, 6 October 2026), Theorem 2.24, obtain the probability that a random product of triangular matrices is nilpotent, with no classification there by the *index* of the nilpotent product. We use that event as the sampling denominator and independently derive it as above.

Fuchs and Kirillov, *Jordan types of triangular matrices over a finite field* (arXiv:2204.00066v1), and Yip, *Rook Placements and Jordan Forms of Upper-Triangular Nilpotent Matrices* (2018), count Jordan types for **uniformly sampled strictly upper triangular matrices**. The distribution here instead weights each possible product by its number of factorizations into arbitrary upper triangular matrices, and is not a uniform nilpotent matrix distribution. Van Peski, *The rank of a random triangular matrix over* \(\mathbb F_q\) (arXiv:2407.19578), likewise studies uniformly distributed strictly upper triangular matrices rather than the product-conditioned ensemble.

## Limitations
The formula only counts the **top nilpotency-index stratum** and does not give the entire Jordan-type distribution of the product, nor the lower nilpotency-index strata. It assumes independent uniform factors in the full upper triangular algebra over a field, not an arbitrary finite ring or a prescribed distribution on matrices. The algebraic proof is accompanied by finite computational checks; no independent mathematical audit has been performed. Priority outside the inspected sources is not established, particularly if an older formula for factorization-weighted Jordan types of triangular matrix products exists.

## References
1. D. Sarma and T. Subedi, *Nilpotent Product Probability of Finite Rings*, arXiv:2610.07892v1 (6 October 2026), especially Section 2.3 and Theorem 2.24. https://arxiv.org/html/2610.07892v1
2. D. Fuchs and A. Kirillov, *Jordan types of triangular matrices over a finite field*, arXiv:2204.00066v1 (31 March 2022), Sections 1, 3, and 7. https://arxiv.org/html/2204.00066v1
3. R. Van Peski, *The rank of a random triangular matrix over* \(\mathbb F_q\), arXiv:2407.19578 (2024), Sections 1, 3, and 4. https://arxiv.org/abs/2407.19578
4. M. Yip, *Rook Placements and Jordan Forms of Upper-Triangular Nilpotent Matrices*, Electronic Journal of Combinatorics 25 (2018), #P1.68, DOI:10.37236/6888. https://www.combinatorics.org/ojs/index.php/eljc/article/view/v25i1p68
