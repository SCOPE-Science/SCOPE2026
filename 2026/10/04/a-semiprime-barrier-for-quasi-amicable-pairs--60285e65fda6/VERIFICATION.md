---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---
# Verification

The infinite theorem is proved symbolically in `RESULT.md`.

The proof partitions every positive integer with at most two prime factors
counted with multiplicity into the exhaustive cases:
\[
p,\qquad p^2,\qquad pq\quad(p<q\ \text{prime}).
\]
For a prime, the nontrivial-divisor sum is \(0\). For \(p^2\) it is \(p\), so
a quasi-amicable two-cycle is impossible. For \(pq\) it is \(p+q\). If both
members were distinct-prime semiprimes, the two cycle equations would force
each product to be strictly larger than the other member.

The packaged checker supplies finite corroboration through
\(2{,}000{,}000\). It constructs a smallest-prime-factor table, computes
\(\Omega(t)\) and \(\sigma(t)\) exactly, and tests every integer in the range
with \(\Omega(t)\le2\). No quasi-amicable two-cycle having both members in that
layer is found.

The finite computation is not an exhaustive proof beyond its stated bound and
is not used to infer the unrestricted result.
