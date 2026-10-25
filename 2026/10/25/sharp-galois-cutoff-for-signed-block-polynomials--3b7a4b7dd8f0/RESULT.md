# Sharp Galois cutoff for signed-block polynomials

## Finding
For integers \(n\ge2\) and \(1\le k<n\) with \(\gcd(n,k)=1\), define
\[
P_{n,k}(X)=\frac{X^n-2X^k+1}{X-1}
=\sum_{j=k}^{n-1}X^j-\sum_{j=0}^{k-1}X^j.
\]
The splitting-field Galois group over \(\mathbb Q\) satisfies
\[
\operatorname{Gal}(P_{n,k}/\mathbb Q)\cong
\begin{cases}
S_3\times S_3,&(n,k)\in\{(7,2),(7,5)\},\\
S_{n-1},&\text{otherwise}.
\end{cases}
\]
Here \(S_1\) denotes the trivial group. Consequently the smallest integer \(N\) such that every coprime pair with \(n\ge N\) has symmetric Galois group is **exactly \(N=8\)**. The distinct new endpoint calculations concern \((n,k)=(8,1)\) and \((8,3)\), with the other two choices following by reciprocity.

## Assumptions and scope
All groups are full Galois groups of splitting fields over \(\mathbb Q\). The index \(k\) is coprime to \(n\), and \(n\ge2\). The source theorem for \(n>8\), the lower-degree calculations, and the exceptional factorization are distinguished below. No result is asserted for noncoprime indices.

## Proof
**1. Infinite range and reciprocal reduction.** Garmi's Theorem 1.1 (arXiv:2610.22764v1, 16 October 2026) shows that the noncyclotomic factor of \(X^n-2X^k+1\) has full symmetric group when \(n>8\) and \(\gcd(n,k)=1\). Since \(X=1\) is a root and the displayed quotient is its other factor, this gives \(\operatorname{Gal}(P_{n,k}/\mathbb Q)=S_{n-1}\) for \(n\ge9\). Direct coefficient reversal gives
\[
P_{n,n-k}(X)=-X^{n-1}P_{n,k}(1/X),
\]
so reciprocal indices have identical splitting fields. Only representatives \(k\le n/2\) need to be checked below \(n=9\).

**2. Exact finite table.** The table contains every coprime representative with \(2\le n\le8\) other than the exceptional pair. The polynomial's degree is \(d=n-1\). For each row, \(p_{\rm irr}\) is a prime at which \(P_{n,k}\) is irreducible modulo \(p_{\rm irr}\). When listed, \(p_{\rm cyc}\) is a prime for which its reduction has exactly two distinct irreducible factors of degrees \(1,d-1\). The prime \(r\) divides its integer discriminant exactly once. Each assertion is reproducible by the supplied stand-alone script.

| \((n,k)\) | \(\operatorname{Disc}(P_{n,k})\) | \(p_{\rm irr}\) | \(p_{\rm cyc}\) | \(r\) |
| --- | ---: | ---: | ---: | ---: |
| \((2,1)\) | \(1\) | \(2\) | — | — |
| \((3,1)\) | \(5\) | \(2\) | — | \(5\) |
| \((4,1)\) | \(-44\) | \(3\) | — | \(11\) |
| \((5,1)\) | \(-563\) | \(2\) | \(3\) | \(563\) |
| \((5,2)\) | \(-331\) | \(2\) | \(5\) | \(331\) |
| \((6,1)\) | \(9584\) | \(5\) | — | \(599\) |
| \((7,1)\) | \(205937\) | \(3\) | \(17\) | \(205937\) |
| \((7,3)\) | \(61193\) | \(3\) | \(41\) | \(11\) |
| \((8,1)\) | \(-5390272\) | \(7\) | — | \(84223\) |
| \((8,3)\) | \(-1205696\) | \(3\) | — | \(18839\) |

For each nontrivial row, modular irreducibility proves that the group acts transitively on \(d\) roots. A prime dividing the discriminant exactly once supplies tame inertia acting as one transposition. When \(d\in\{2,3,5,7\}\) the transitive action is primitive because \(d\) is prime. For \(d\in\{4,6\}\), the \((d-1,1)\) Frobenius cycle proves primitivity: a nontrivial block containing its single fixed point would also have to contain the entire orbit of length \(d-1\). A primitive permutation group containing a transposition is the full symmetric group. The \(d=1\) row is tautological.

**3. Exceptional row.** Direct multiplication gives
\[
P_{7,2}(X)=(X^3+X+1)(X^3+X^2-1).
\]
The two cubics are irreducible modulo \(2\), and their discriminants are \(-31\) and \(-23\). Each has Galois group \(S_3\). The unique quadratic subfields of their splitting fields are distinct; two \(S_3\)-Galois extensions with distinct quadratic subfields are linearly disjoint. The compositum therefore has group \(S_3\times S_3\). Reciprocity gives the same group for \(k=5\). This exceptional small-degree behavior is not presented as a new discovery.

**4. Sharpness.** The preceding table proves the endpoint \(n=8\) has full symmetric Galois groups for all coprime indices. Garmi proves all \(n\ge9\). The two exceptions at \(n=7\) show that no smaller uniform threshold can work.

## Verification
Run `python3 verify.py` using Python's standard library. Its deterministic tests compute all ten integer discriminants by a fraction-free Sylvester determinant, prove modular irreducibility by Frobenius-power gcd tests, confirm the two \((d-1,1)\) modular factor degrees for each composite \(d\), check primality and valuation one of the displayed discriminant primes, verify the exceptional cubic factorization and discriminants, and check reciprocity for every coprime index through \(n=8\). The script returns a single `CERTIFICATE_OK` line on success. The infinite range is a direct application of the cited theorem, not a finite computation.

## Relationship to prior work
Hilel Garmi, *Galois Groups of Trinomials with Small Coefficients*, arXiv:2610.22764v1 (16 October 2026), Theorem 1.1 and Corollary 1.3, proves the uniform statement for \(n>8\). Its proof explicitly treats the coefficient product of absolute value two under this threshold. Martin's earlier theorem on generalized Fibonacci polynomials, cited in Garmi, handles certain older cases. The contribution here is closing the first excluded degree \(n=8\) with exact modular certificates and recording the sharp global cutoff together with its low-degree exceptions. It is not a new proof of the infinite-range theorem or of the previously computed \(n=7\) exceptional factorizations.

## Limitations
The group statement requires coprime exponents and explicitly relies on Garmi for \(n\ge9\). The finite calculation proves only the omitted small-degree cases. An earlier source might independently compute the degree-seven endpoint without discussing the global cutoff, so priority remains subject to further literature review. No separate external/independent mathematical validation has been performed.

## References
Garmi, H., *Galois Groups of Trinomials with Small Coefficients*, arXiv:2610.22764v1, first public 2026-10-16, https://arxiv.org/html/2610.22764v1. Earlier Martin theorem and the classical inertia/transposition facts are discussed and referenced therein.
