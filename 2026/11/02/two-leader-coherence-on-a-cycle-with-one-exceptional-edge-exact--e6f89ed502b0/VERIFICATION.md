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

Execute `python3 verify.py` (Python standard library only) in the extracted package directory. The included `verify_output.txt` is the output of an actual run with exact fractions.

It checks 1,476 different grounded-Laplacian inverse traces against the derived pair formula over vertex counts \(3\le n\le10\) and nine rational exceptional-edge resistances \(\{1/7,1/4,1/2,3/4,1,5/4,2,5,20\}\). It also exhaustively compares optimal pairs with the analytic reduced candidate sets for 72 model instances and the strong-link explicit pair classification for 32 instances. Representative weak-link optimum outputs are included.

The finite tests neither exhaust all \(n\) nor all real \(x\). The general correctness argument is the Dirichlet Green identity plus exact finite sums, product optimization, and strict-convexity/adjacent-difference proof in `RESULT.md`.

No independent audit or third-party formal certification is asserted.
