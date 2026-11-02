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

# Reproducibility and verification

Run `python3 verify.py` using Python 3 and its standard library. The
observed exact terminal message is:

`VERIFY_OK: exact witness, characteristic-two, rank and homogeneity checks`

The program verifies the coefficient Wronskian identity for the stated
witnesses, all homogeneous quadratic resultants and gcd-based common-root
tests, the rank-two and rank-three examples over the prime fields of
characteristics \(3,5,7,11,13,17,19\), the characteristic-two witness,
the universal characteristic-two middle-coefficient identity by all
\(2^6\) coefficient assignments, and the quadratic rescaling of the
ramification sections.

For the universal theorem, the proof in `RESULT.md` additionally uses the
normal exact sequence, Serre-dual cohomology, the two possible globally
generated rank-two bundles of degree two, the characteristic-independent
rank bound for an unramified triple, and the odd-characteristic smooth
\(\operatorname{PGL}_2\)-fibration from degree-two maps to their two
ramification points. Those structural arguments establish the
all-characteristic splitting classification and the odd-characteristic
smooth irreducible jumping divisor; finite samples alone are insufficient.

The evidence does not establish a result for ramified maps or a compactified
jump locus, and does not constitute an independent mathematical audit.
