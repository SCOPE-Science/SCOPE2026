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
# Verification and scope
The exact proof is given in `RESULT.md` and does not depend on external computational output. The independently runnable `check.py` uses exact integer and rational arithmetic to confirm all fifteen perfect matchings, the incidence of each of fifteen edges in precisely three matchings, the maximum four in the relevant six-vertex 2-intersecting triple family, explicit attainable examples in each phase (including threshold endpoints), the binomial polynomial identities, and a supplementary rational grid of admissible stake vectors. Run `python3 check.py` with Python 3.10 or later and no third-party packages. Expected final output begins with `PASS:`. The program does not exhaust the continuum of real weights or of success probabilities; universal validity follows from the structural proof.

The strictly non-dominant class is empty for \(p\le1/6\). The phase boundaries use a strict inequality at their lower endpoints. The probability threshold is the expectation exactly, not an arbitrary tail threshold. Literature coverage and independent validation are not certified.
