# Binary submask criterion for the sharp two-adic exponent of recursive divisor counts

## Finding

For every positive integer \(n>1\), define its recursive-divisor count \(\kappa_0(n)\) by the divisor recurrence below. If its prime factorization has positive prime exponents \(a_1,\ldots,a_r\) and largest exponent \(A\), then the previously known divisibility \(2^A\mid\kappa_0(n)\) is sharp **exactly** when each exponent is a binary submask of \(A\). More precisely, for any distinguished exponent \(a_1=A\),

\[\boxed{\frac{\kappa_0(n)}{2^A}\equiv\prod_{j=2}^r\binom{A}{a_j}\pmod 2.}\]

Thus \(\nu_2(\kappa_0(n))=A\) precisely when all the displayed binomial coefficients are odd, and otherwise \(\nu_2(\kappa_0(n))\ge A+1\).

## Assumptions and scope

For integers \(n\ge1\), set \(\kappa_0(1)=1\) and
\[\kappa_0(n)=1+\sum_{d\mid n,\,d<n}\kappa_0(d)\qquad(n>1).\]
Write \(n=\prod_{j=1}^r p_j^{a_j}\) for distinct primes \(p_j\) and positive integer exponents \(a_j\), with \(r\ge1\), and let \(A=\max_j a_j\). Reorder the primes so that \(a_1=A\). A nonnegative integer \(b\) is a **binary submask** of \(A\) if every one-bit of \(b\) is also a one-bit of \(A\); equivalently \(\binom{A}{b}\) is odd. The theorem covers all \(n>1\), with no restriction on prime support. The case \(n=1\) is excluded because there is no largest prime exponent.

## Proof

Introduce commuting formal variables \(X_1,\ldots,X_r\). For exponent vectors \(\mathbf e=(e_1,\ldots,e_r)\) of nonnegative integers, define
\[F(\mathbf X)=\sum_{\mathbf e\ge\mathbf0}\kappa_0\!\left(\prod_{j=1}^r p_j^{e_j}\right)\prod_{j=1}^r X_j^{e_j},\qquad H(\mathbf X)=\prod_{j=1}^r(1-X_j)^{-1}.\]
The defining recursion, including its \(n=1\) boundary case, gives \(2\kappa_0(n)=1+\sum_{d\mid n}\kappa_0(d)\). Coefficientwise this is \(2F=H+HF\), so the unique formal power series with constant term one is
\[F=\frac{H}{2-H}=\frac1{2\prod_{j=1}^r(1-X_j)-1}.\]
Let \(Q=\prod_{j=2}^r(1-X_j)\); for \(r=1\) the empty product is \(Q=1\). Extracting the coefficient of \(X_1^A\) by an ordinary geometric expansion gives the **exact** identity in integer formal power series
\[[X_1^A]F=\frac{2^A Q^A}{(2Q-1)^{A+1}}.\]
The denominator \(2Q-1\) has constant term \(1\), hence its negative powers are integer formal series and reduce to \(1\) modulo \(2\). Therefore
\[\frac{\kappa_0(n)}{2^A}\equiv [X_2^{a_2}\cdots X_r^{a_r}]Q^A\equiv\prod_{j=2}^r\binom{A}{a_j}\pmod2.\]
This also proves the asserted integrality. Finally, in characteristic two,
\[(1+X)^A=\prod_{h:\,\text{bit}_h(A)=1}(1+X^{2^h}).\]
Its coefficient at \(X^b\) is one if and only if the one-bits of \(b\) are a subset of the one-bits of \(A\). Applying this independently to every exponent proves the classification, including the prime-power case. All arguments are exact identities of formal power series, not limiting calculations.

## Verification

The standalone Python program `VERIFY.py` independently constructs \(\kappa_0\) by its proper-divisor recurrence for exponent vectors; it does not reuse the generating-function calculation. It checks all vectors of length \(1\) through \(4\), each entry from \(1\) through \(5\), a total of \(780\) vectors, checking both the divisibility lower bound and the sharp-parity criterion. The saved exact-integer output in `VERIFY_OUTPUT.txt` reports \(192\) sharp cases and \(588\) strict cases. These finite checks supplement, but do not replace, the unrestricted proof.

Examples: \(\kappa_0(p^3q)=40\) gives \(\nu_2=3\), because \(1\) is a binary submask of \(3\); \(\kappa_0(p^4q^2)=416\) gives \(\nu_2=5>4\), because \(2\) is not a binary submask of \(4\). The values depend only on exponent signatures, not on the primes.

## Relationship to prior work

Fink's 2019 work (later published in 2024) already proves \(2^A\mid\kappa_0(n)\). That lower bound is **not** a new claim here. Fink's July 2023 papers give exact Dirichlet-series and arbitrary-signature formulas for the values of \(\kappa_0\); the second explicitly asks about the significance of the normalized sequence \(\kappa_0(n)/2^A\) in its closing questions. The present theorem identifies its parity by an exact binary pattern, independently of the unproved positive multiple-sum representation appearing as Conjecture 1 in that paper. It answers only the first-bit aspect of the broader normalized-sequence question. The classical ordered-factorization representation for two-prime support is consistent with the theorem but does not itself state the criterion for arbitrary prime support.

## Limitations

When some exponent has a bit outside \(A\), the theorem gives only a strict lower bound \(\nu_2(\kappa_0(n))\ge A+1\), not the exact higher valuation. The complete higher-bit structure of normalized values is open here. Explicit arithmetic formulas in the cited literature can compute individual values, and an equivalent parity characterization might exist in unindexed references. No independent audit or claim of exhaustive literature coverage is made.

## References

1. T. M. A. Fink, *Properties of the recursive divisor function and the number of ordered factorizations*, arXiv:2307.09140v1, 18 July 2023, Theorems 1–3. https://arxiv.org/abs/2307.09140
2. T. M. A. Fink, *Number of ordered factorizations and recursive divisors*, arXiv:2307.16691v1, 31 July 2023, Theorems 1–2, Conjecture 1, and Section 6, Question 4. https://arxiv.org/abs/2307.16691
3. T. M. A. Fink, *Recursively divisible numbers*, arXiv:1912.07979v1, 17 December 2019; later Journal of Number Theory 256 (2024), Corollary 1. https://arxiv.org/abs/1912.07979
4. B. Chor, P. Lemke and Z. Mador, *On the number of ordered factorizations of natural numbers*, Discrete Mathematics 214 (2000), 123–133, DOI 10.1016/S0012-365X(99)00223-X.
