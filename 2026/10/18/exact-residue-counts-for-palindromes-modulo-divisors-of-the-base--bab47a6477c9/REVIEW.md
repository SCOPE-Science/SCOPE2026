# Review of exact residue counts for palindromes modulo divisors of the base plus one

## Correctness — PASS

The residue reduction follows from \(b\equiv-1\pmod q\) and canonical digit pairing. The root-of-unity proof evaluates every Fourier frequency separately, including \(h=0\), \(h=q/2\) when applicable, and the remaining characters. The geometric sum identities require \(z^2\ne1\), exactly the removed cases. Orthogonality yields the formula; an exhaustive residue-case split gives a strict discrepancy bound. The exceptional one-digit case and all even lengths are proved directly. Independent enumeration using integer arithmetic and fractions agrees across the stated finite regression range. Finite evidence is not substituted for the proof.

## Originality — PASS, subject to limitations

The 2004 text of Banks–Hart–Sakata proves equidistribution under \(\gcd(q,b(b^2-1))=1\); the 2009 main distribution theorems of Col have the same restriction. Col’s later sieve Lemma 22 handles some exceptional prime divisors of \(b+1\) in averaged zero-residue estimates, so odd-prime limiting uniformity alone is not asserted to be original. The 2024 full text of Onphaeng and collaborators treats \(b\equiv0,1\pmod q\), not the general \(b\equiv-1\pmod q\) branch. The classical even-length obstruction and the modulus-two intersection are preexisting special cases. The new comparison is the exact **all-residue, odd-length** formula for \(q>2\) dividing \(b+1\). A generic convolution identity in prior work might imply this formula without explicit statement, and unindexed equivalent literature remains a risk.

## Mathematical value — PASS

Palindrome distribution in arithmetic progressions is an established number-theoretic problem. The result fills a natural excluded-modulus regime with an exact global formula instead of a qualitative asymptotic, distinguishes odd versus even moduli, and identifies the exact and nonvanishing parity bias. The uniform strict error bound and the two exceptional Fourier modes give a structural explanation. The value rests on the full family, not on rediscovery of even-length divisibility.

## Limits and review status

The theorem addresses complete canonical fixed-digit-length populations, not arbitrary intervals or general moduli. Independent external audit and independent novelty certification have not been performed.

Self-review: passed. Independent audit: not yet performed.
