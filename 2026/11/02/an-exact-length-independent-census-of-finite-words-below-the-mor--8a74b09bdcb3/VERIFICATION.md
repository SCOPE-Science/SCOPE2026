---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

The needed existence theorem is Khrystik arXiv:2605.00141 Theorem 3.3 (also Theorem 4.2 with m=n=k), not the theorem numbers quoted in the frozen text. Its bounded-fringe form uses a periodic prefix of the prescribed central length. Taking the primitive root and extending its phased repetition until the first mismatch or endpoint keeps the fringe-plus-period budget. Any two permitted cores overlap in at least L−2k+p+p′≥p+p′ letters; Fine–Wilf gives period gcd(p,p′) on that overlap. A full cycle in each core would be a proper power if its period exceeded the gcd. Equal primitive periods and at least one cycle of overlap force equal continuation and phase, and the mismatch at each endpoint forbids unequal corresponding cuts. The frozen line 69 repeats the same left-cut inequality in reverse notation; the opposite inequality is excluded by interchanging the two representations. At most a+b factors meet fringes, and at most p distinct factors lie within the core. Counting phased primitive words and the two independently mismatching fringe letters gives the stated convolution; the cumulative fringe series is (1−t)/(1−qt)². Replacing M_q(p) by q^p incurs O_q(kq^k), since p q^(−p/2) is summable, and the explicit main sum has the stated coefficient. The unary case gives exactly one word, and for k≥2 the plateau polynomial has degree k in q, less than 2k−1 at the preceding vacuous length. The incorrect citation numerals and the duplicated inequality are locational/expository slips, not changes to the theorem or its proof mechanism.

## originality

PASS

Distinct supported content is the canonical boundary-normal primitive representation and its exact all-alphabet, all-length census in the specified range. The existential structural decomposition and primitive-word counts are known inputs; the overlap argument is needed to make the count disjoint.

## value

PASS

At the natural finite Morse–Hedlund threshold, the canonical decomposition supplies a uniform bijective description and an exact plateau across all word lengths in the domain, explained by a fixed amount of fringe and primitive-period information. It gives an exact census for all alphabets and the leading growth with k, rather than only a new proof of existential periodicity or a small instance count.

The dated certificate retains the supplied scientific assessment, sources and limitations.
