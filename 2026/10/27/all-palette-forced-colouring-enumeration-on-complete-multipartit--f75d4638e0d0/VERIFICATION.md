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
# Reproduction and limitations

Run `python3 verify.py` with Python 3. The script uses only the standard library. It constructs the Stirling-number coefficient formula, independently enumerates random partial-colouring states with an explicit local forcing simulation, and compares integer counts for seventeen bipartite and multipartite parameter instances. It separately compares the set of assignments predicted by the structure theorem with those accepted by local forcing for four additional instances. The ending output is `ALL_EXHAUSTIVE_CASES_PASS`.

The independently checked \(K_{2,2,2}\) case with four available colours gives \(288,432,288,96\) at seeded domain sizes \(3,4,5,6\), respectively, after direct examination of all \(15625\) partial assignments. The code also checks minimum seeded-domain sizes independently against the subset-sum criterion. This is finite computational evidence; the proof for every positive part profile and larger palette is the structural argument in `RESULT.md`, not extrapolation from these cases.

Source-priority verification is incomplete because the full text of arXiv:2609.17108v1 could not be accessed during inspection. No independent scientific audit or external verification is claimed.
