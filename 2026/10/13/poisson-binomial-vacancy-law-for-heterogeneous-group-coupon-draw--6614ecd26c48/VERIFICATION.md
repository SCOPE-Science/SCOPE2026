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

# Reproduction and proof scope

Run `python verify.py` from the extracted file directory (requires Python 3 and SymPy). The exact-rational script checks 710 distribution-and-real-rootedness cases over all \(1\leq n\leq8\) and nondecreasing packet-size lists of length at most three; it also checks 5,144 exact binomial factorial moments and eight distinct underlying subset enumerations. The expected output begins `PASS: 710 exact distribution-and-real-root checks, 5144 factorial-moment identities, 8 independent subset enumerations.`

The analytical proof, not enumeration, establishes all integers \(n\geq1\) and all finite packet sequences. Independently check (i) conditional hypergeometric coefficient extraction, (ii) the mixed-half-plane zero exclusion, (iii) Gauss–Lucas derivative preservation, (iv) Hurwitz nonzero limit justified by \([w^t]G(1,w)=\binom nt\), and (v) the multiaffine polarization conclusion. The exact Bernoulli parameters are derived from the nonpositive real zeros; the physical vacancy indicators are not asserted independent.

No external independent scientific audit has been conducted, and an unreviewed earlier equivalent publication cannot be excluded.
