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

The unrestricted proof in `RESULT.md` uses Hall's matching theorem. Run `python3 verify.py` to perform exhaustive finite consistency checks. It enumerates all 34 path/edge-component profiles for one through four blocks, and checks all pair-query supports for three and six vertices, using concept-cardinality impossibility to prune supports with too many binary labelings. The exact stdout is supplied in `verification_output.txt`.

The finite enumerator cannot certify the unrestricted mathematical theorem or historical novelty; those aspects depend on the stated proof and literature comparison. The recorded program has no external packages, downloaded data, or network requirements.
