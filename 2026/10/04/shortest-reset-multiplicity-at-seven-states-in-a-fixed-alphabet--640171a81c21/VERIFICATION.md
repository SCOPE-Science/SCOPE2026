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

Run `python3 artifacts/verify.py` from the package root. The script reconstructs the seven-state transition maps from the published Theorem 3 table and performs exact breadth-first dynamic programming over reachable subsets.

It verifies that the first singleton distance is \(32\) for both \(\{a,e\}\) and \(\{a,b,e\}\); that the former has exactly \(331{,}776\) shortest words, all to state \(4\); that the latter has exactly \(1{,}327{,}104\), split equally between states \(3\) and \(4\); and that the latter count is exactly four times the former. It also replays the source witness \((ea^5)^5ae\), whose length is \(32\) and whose image is a singleton.

The computation is finite and exhaustive for the two stated seven-state automata. It does not test or certify any formula for other values of \(n\). The recorded verifier result is in `artifacts/verification_output.json`.
