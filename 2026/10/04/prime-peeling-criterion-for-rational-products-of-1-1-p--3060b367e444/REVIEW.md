# Independent mathematical audit

## correctness

PASS

For the largest used generator prime \(P\ge5\), no numerator \(r+1\) from a smaller prime generator can contain \(P\): it would force \(r=P-1\), an even integer greater than two. Nor can a prime factor of \(P+1\) exceed \(P\). Hence the largest nonzero valuation is exactly \(-a_P\), so peeling recovers the exponent and strictly lowers the largest possible prime. At support \(\{2,3\}\), solving \(x=-u+2v\), \(y=u-v\) gives the stated cone and unique exponents. Reversing the forced steps proves sufficiency. The finite verifier is consistent with the symbolic proof.

## originality

PASS

The focal 2023 paper was inspected around its plus-sign uniqueness result and Question 32, which explicitly asks to determine the rationals admitting such a representation. It proves uniqueness of an existing representation but does not provide a recognition/reconstruction criterion. Resultary search returned the audited theorem as the only exact hit; the Dedekind-psi OEIS entries concern related values but not this repeated-generator rational semigroup.

## value

PASS

The theorem resolves an explicit published recognition problem by a finite deterministic decoder, not merely by another uniqueness argument. The terminal cone and exact integer corollary give a concise structural description that a future study of this semigroup can directly reuse.

The dated certificate retains the supplied scientific assessment, sources and limitations.
