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
# Verification of depth-wise witnessing

The proof supplies four independently checkable steps: (1) structural-induction preservation under height truncation \(T_b\); (2) exact identification of the branch neighborhoods through depth \(H-2\); (3) calculation of \(e(o,\Box^H p)=\inf_{n\ge2}1/n=0\) with each branch value strictly positive; and (4) closure of finite atomic truth-value sets under crisp Gödel modal semantics.

Run `python3 witness_depth_check.py` with Python 3. The program uses exact rational arithmetic, constructs finite-prefix chains, verifies all \(48\) finite prefixes for \(0\le H-1\le5\) and \(4\le N\le11\), and performs \(8{,}000\) depth-limited random formula comparisons with fixed seed. The completed test prints `WITNESS_DEPTH_FINITE_STRESS_OK shallow_formula_comparisons= 8000`.

Crucially, every finite prefix is fully witnessed; the program does not falsify witnessedness on any finite model. It checks the positive rational values and their convergence pattern. The required nonattainment in the countably infinite union and the arbitrary-formula cutoff follow from the mathematical proof, not from finite testing.

No independent audit or external certification is represented.
