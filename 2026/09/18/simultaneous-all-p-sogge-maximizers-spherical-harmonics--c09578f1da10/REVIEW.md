# Review status

Independent audit completed on 2026-10-01: **passed**.

Correctness: **PASS**. The construction is internally consistent. A well-conditioned zonal block of size \(M\) gives \(M\) orthonormal vectors with point peaks of order \(\sqrt{N_k}\). Projecting the rotational Gaussian-beam tight frame to the \(N_k-M\) dimensional complement preserves stable rank comparable to \(N_k-M\); the Spielman–Srivastava restricted-invertibility estimate selects at least \(M\) uniformly conditioned projected beams whenever \(M/(N_k-M)<1\). Orthogonal mixing preserves the zonal peak and, after a sign choice, a uniform Gaussian-beam pairing. Hölder yields the low-\(p\) Sogge exponent, while gradient propagation of the point peak over a radius \(O(k^{-1})\) ball yields the high-\(p\) exponent.

Originality: **PASS**. Han’s v1, submitted 2026-09-12, states that for every fixed \(p>2\) there is a positive-density subsequence, with density arbitrarily close to one; it does not assert one common subsequence for all \(p\). A later 2026-09-19 revision strengthens this to separate branchwise bases, but that revision postdates the audited record and still does not give one family carrying both mechanisms simultaneously. Resultary found no earlier equivalent common-family theorem.

Value: **PASS**. A common positive-density family that simultaneously realizes both classical concentration mechanisms answers a natural compatibility question left open by the branchwise constructions. The density \(\rho<1/2\) is a structural threshold of the two-complement construction, not an arbitrary slice.

Detailed evidence: `INDEPENDENT_AUDIT_2026-10-01.md` and `INDEPENDENT_AUDIT_2026-10-01.json`.
