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
# Direct verification

Run `python3 verify.py` and then `python3 verify_ring.py` with a standard Python 3 interpreter. The finite-field arithmetic is explicitly implemented; no external Python packages or network services are needed.

The first checker also reconstructs and directly verifies the Poisson bracket identities and the parameter action on \(16\), \(256\), and \(4096\) brackets, respectively. The ring checker forms the original four-element algebra multiplication, both Lichnerowicz differentials on their basis cochains, and computes exact ranks using Gaussian elimination over three finite fields. It exhausts all Poisson coefficients for \(\mathbb F_2\), \(\mathbb F_4\), and \(\mathbb F_8\), respectively \(16\), \(256\), and \(4096\) brackets. It checks the chain-complex identity, each rank and Betti tuple, the explicit independent degree-one cocycles for every parameter \(d\), the nonzero cup-product generator in degree two, and the punctured-socle cup and multiplication identities.

The expected terminal markers are `CHAR2_POISSON_TRUNCATED_PLANE_DIRECT_OK` and `CHAR2_POISSON_COHOMOLOGY_RINGS_AND_CUPS_OK`. The accompanying `CHECKS.txt` is the actual recorded run output; it is reproducible from the two standalone Python sources. The proof for arbitrary characteristic-two fields is in `RESULT.md`, not inferred from the finite tests.

The investigation does not establish independent validation, historical publication priority, higher-truncation statements, or nonalternating/restricted Poisson cohomology.
