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

# Reproducibility of two-factor edge-query shattering

On Python 3, execute `python3 verify_certificates.py two_factor_certificates.json`. The verifier constructs the two-factor hypotheses **independently** of the candidate-subset generator, checks every recorded hypothesis, verifies the binary shattered-tree paths, recomputes the complete finite Littlestone recurrence, and exhaustively excludes all edge-query sets of size one larger than the reported VC dimension. See `verification_output.txt` for the actual output. The generator may be rerun with `python3 generate_certificates.py two_factor_certificates.json`; its JSON output is reproducible and canonical with the indicated program.

The cases \(n=3,4,5,6\) yield hypothesis counts \(1,3,12,70\), VC dimensions \(0,1,3,4\), Littlestone dimensions \(0,1,3,5\), and the six-vertex depth-five tree includes \(31\) internal queries and \(32\) distinct witnesses. Every subset and membership check is exact, not numerical approximation. The general connected-family argument is mathematically proved in `RESULT.md`; computational replay for small \(n\) does not certify arbitrary \(s\). No independent external audit has yet been performed.
