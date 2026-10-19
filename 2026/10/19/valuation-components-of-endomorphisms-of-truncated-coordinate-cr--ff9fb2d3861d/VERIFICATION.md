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

# Finite checks and proof boundaries

Run `python3 verify.py` with an ordinary Python 3 interpreter from this directory. It has no third-party dependencies. Its successful final line is `VERIFY_OK_CROSS_ENDOMORPHISMS`.

The verifier performs ten exhaustive calculations of pairwise-truncated polynomial products in finite prime fields: branch counts from two through four and truncation degrees two through four. It then enumerates complete endomorphism images in four cases and checks the associated linear coefficient matrix over the field for invertibility. The following observed whole-map counts are independent direct enumerations: `(r,d,q)=(2,2,2)` gives 144 endomorphisms and 32 automorphisms; `(2,2,3)` gives 2025 and 648; `(2,3,2)` gives 1024 and 128; `(3,2,2)` gives 32768 and 3072. In all tests, these match the formulas.

For every integer pair with two through five branches and truncation degree two through six, the verifier builds **all** valuation vectors satisfying the pairwise constraints, then independently finds the coordinatewise-minimal ones. These agree with the proved component list and equidimensionality condition.

Checks are finite. They neither establish the infinite-parameter theorem, prove prior-work novelty nor determine the possible nonreduced structure of the universal Hom scheme. Those claims rely on the separately written algebraic argument, and independent mathematical audit has not been performed.
