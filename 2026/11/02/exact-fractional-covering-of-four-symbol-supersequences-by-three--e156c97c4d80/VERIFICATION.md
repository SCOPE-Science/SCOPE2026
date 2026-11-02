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

The proof in `RESULT.md` supplies unrestricted primal and dual feasible solutions with equal objective for every alphabet size at least three. The coverage proof lists all fifteen equality partitions of a four-position word. The dual proof classifies every three-position word into four types and counts all its positive-weight supersequences. The binary exception is supported by a four-center covering witness and a matching four-receiver dual witness.

Running `python3 verify.py` recomputes the incidence matrix directly from distinct deletion outputs and checks each constraint and the exact rational objective for \(q=3,\ldots,9\). It separately checks the binary witnesses and the fifteen equality partitions. No external libraries, network access or precomputed data are needed. This finite computation checks the supplied identities at test sizes only; the proof handles all larger alphabets symbolically.

The integer-cover asymptotic separation additionally uses the published strict density bound in Pikhurko, Verbitsky and Zhukovskii (2025); the exact fractional LP result itself is independent of that external theorem.
