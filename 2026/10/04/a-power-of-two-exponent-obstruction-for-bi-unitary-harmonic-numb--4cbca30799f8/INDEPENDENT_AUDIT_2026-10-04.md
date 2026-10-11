# Independent mathematical audit

## correctness

PASS

Let \(b=2^t\). Bi-unitary harmonicity gives \((p+1)(p^2+1)B\mid 8bp^3q^{2b}\), where \(B=\sum_{j=0}^{2b}q^j-q^b\). Because \(b\) is a power of two, prime-support forcing and \(\gcd(p+1,p^2+1)=2\) reduce the first factor to \(p+1=2^u\), \(p^2+1=2q^v\), so \(q\equiv1\pmod4\). Also \(B\equiv1\pmod q\), while even \(b\) gives \(q+1\mid B\); hence \(q+1=2p^s\). Size comparisons force \(s=v=1\), then \(p=3,q=5\). For that pair harmonicity would require \(B\mid216b\), but \(B>25^b>216b\) for every \(b\ge2\), contradiction. The finite verifier is consistent with the argument but is not used as the infinite proof.

## originality

PASS

Sándor's primary paper was inspected at the relevant theorem: it excludes \(p^3q^2\) and immediately remarks that \(p^3q^4\) is also impossible, but it does not give the full power-of-two exponent family. Manea and Minculete's 2016 full text repeats the fixed exclusions and studies other factorization forms. OEIS A286325 is a finite list and does not imply the uniform theorem. Fresh Resultary search found the audited record itself but no stronger pre-existing bi-unitary result covering all \(t\ge1\).

## value

PASS

The theorem turns a previously isolated fixed-exponent exclusion into an infinite, naturally parameterized obstruction and identifies a reusable arithmetic mechanism—prime-support collapse plus the divisor \(q+1\) of the bi-unitary divisor sum. This is a motivated structural extension rather than a finite table check.

The dated certificate retains the supplied scientific assessment, sources and limitations.
