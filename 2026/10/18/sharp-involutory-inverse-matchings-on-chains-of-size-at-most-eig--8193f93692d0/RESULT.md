# Sharp involutory inverse matchings on chains of size at most eight
## Finding
For each integer \(1\le n\le8\), there exists a bijection \(J_n:\mathcal O_n\to\mathcal O_n\) on the monoid of weakly increasing maps \([n]\to[n]\) such that \(J_n^2=\mathrm{id}\), the ranks of \(f\) and \(J_n(f)\) coincide, and
\[
fJ_n(f)f=f,\qquad J_n(f)fJ_n(f)=J_n(f).
\]
Here juxtaposition is transformation composition, and the identities are insensitive to choosing left-to-right or right-to-left convention if used consistently. Among **all** such involutory inverse matchings, precisely \(0\) idempotents need be moved when \(n=1,2,3,4,6,8\), and precisely \(1\) must be moved when \(n=5,7\). The single moved idempotent in each exceptional case lies in rank three. In particular, insisting that every idempotent be fixed is impossible for \(n=5,7\), but possible for the other chain sizes through eight.

## Assumptions and scope
\(\mathcal O_n\) consists of all maps \(f:[n]\to[n]\) satisfying \(i\le j\implies f(i)\le f(j)\); rank means the size of the image. An *inverse* of \(f\) in the semigroup sense is \(g\) with \(fgf=f\) and \(gfg=g\); it need not be a two-sided unit. A matching is an involution when applying it twice returns the original map. A displaced idempotent is an idempotent \(e\) for which \(J_n(e)\ne e\). The statement is a finite exhaustive theorem only for \(n\le8\), not an assertion for all \(n\).

## Proof
Fix \(1\le r\le n\). A rank-\(r\) isotone map has a unique ordered image \(1\le a_1<\cdots<a_r\le n\) and a unique list of \(r-1\) breakpoints \(1\le p_1<\cdots<p_{r-1}<n\): the map takes value \(a_i\) on its \(i\)-th consecutive fiber. Thus rank-\(r\) maps are indexed, without repetition, by lexicographically ordered pairs \((P,A)\) and their number is
\[
T_{n,r}=\binom{n-1}{r-1}\binom nr.
\]
The certificate file `INVOLUTION_CERT.json` gives, for each of all \(36\) pairs \((n,r)\) with \(1\le r\le n\le8\), the zero-based index of a partner for **every** rank-\(r\) map in that canonical lexicographic ordering. The standalone script `verify_involution_standalone.py`, requiring only Python's standard library, reconstructs each map from its breakpoint and image subsets and verifies **for every index**, directly by finite composition, that its partner has the same rank, that the index map is an involution, and that both inverse identities hold. This is a finite exhaustive proof: all \(\binom{2n-1}{n}\) order-preserving maps are included and there is no extrapolation from a sample. The enumerated sizes for \(n=1,\ldots,8\) are \(1,3,10,35,126,462,1716,6435\).

For optimality, in rank \(r\) the number of idempotents is
\[
I_{n,r}=\binom{n+r-1}{2r-1}.
\]
Indeed, an idempotent isotone map has each image point located inside its own fiber; a fixed composition \(b_1+\cdots+b_r=n\) of positive fiber sizes yields \(\prod_i b_i\) possible idempotents, and the generating series is \((x/(1-x)^2)^r\), with coefficient \(\binom{n+r-1}{2r-1}\). An isotone self-map fixed by the inverse-matching involution must satisfy \(f^3=f\). Iterating a monotone map has no cycles longer than one, so \(f^3=f\) entails \(f^2=f\), making it an idempotent. Therefore all \(T_{n,r}-I_{n,r}\) nonidempotents must occur in disjoint pairs. If their number is odd, the involution must also displace an odd number of idempotents in that rank class. Checking the explicit binomial formulas for all \((n,r)\) through eight shows that the only odd cases are \((5,3)\) and \((7,3)\). This gives lower bounds one or zero, respectively. The certificate attains these bounds rank by rank: the verifier checks exactly \(I_{n,r}-(T_{n,r}-I_{n,r}\bmod 2)\) fixed points. This proves both existence and optimality.

## Verification
From the directory containing the two supplied artifacts execute `python3 verify_involution_standalone.py INVOLUTION_CERT.json`. The script uses only the Python 3 standard library, checks every rank, every paired map and both composition equalities, and confirms the sharp idempotent displacement. An actual execution completed with `PASS: exhaustive rank-preserving involution inverse matching, n=1,...,8`. Direct finite verification, rather than an unverified search log, is the certificate for the finite assertion. The certificate is self-contained and deterministic; no optimization library is needed to replay it.

## Relationship to prior work
Higgins's 2026 manuscript proves a **permutation** inverse matching for every \(\mathcal O_n\) via balanced weightings and makes no universal claim of an *involutory* inverse matching. Higgins's 2024 article already proves an involution matching whenever the sizes of the two index sets of a regular \(\mathcal D\)-class have integer ratio in the necessary direction; that general theorem is not a novelty claim here and covers several individual rank classes. Earlier constructions for orientation-preserving transformations do not directly restrict to isotone maps. The contribution here is the single explicit finite cutoff covering **every rank** simultaneously, together with its sharp minimum displacement of idempotents, including the exceptional ranks not resolved by integer-ratio criteria alone. There remains a bibliographic risk of an equivalent prior finite computation, and this work does not settle the unrestricted involutory-matching problem.

## Limitations
No conclusion is drawn for \(n\ge9\). No closed-form uniform construction is established. The finite certificate and checker cover all maps only for the stated small chain sizes. The idempotent-optimality assertion concerns **involutory** matchings that pair semigroup inverses, not arbitrary permutations. Independent mathematical audit has not been performed; bibliography completeness remains uncertain.

## References
1. P. M. Higgins, “Balanced weightings and permutation matchings applied to the monoid of order-preserving mappings,” arXiv:2610.01912 (first public version, 2026-10-01).
2. P. M. Higgins, “Involution matchings in finite semigroups,” *Semigroup Forum* (2024), DOI:10.1007/s00233-024-10430-0, especially Proposition 2.3.
3. P. M. Higgins, “Involution matchings in finite transformation semigroups,” arXiv:1811.04472 (2018), for a related, different transformation family.
