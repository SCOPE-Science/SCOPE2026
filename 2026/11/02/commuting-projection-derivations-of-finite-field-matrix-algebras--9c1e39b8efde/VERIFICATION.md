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

# Verification record

Run `python3 verify.py`. The exact output is in `verification_output.txt`; the checker uses Python's standard library only. It enumerates every scalar-normalized inner representative for each listed finite matrix algebra and directly verifies the original \(D^2=D\) identity on all matrix units. It independently computes the whole operator rank, constructs every ordered pair of accepted derivations, and verifies the predicted commuting-neighborhood counts. For the six smaller cases it also tests equality of both endomorphism compositions on the full matrix-unit basis. For \((n,q)=(4,2)\), it tests commutation of the underlying representative matrices (the equivalence is proved separately). The extension field \(\mathbb F_4\) uses polynomial arithmetic modulo \(z^2+z+1\). The final marker is `COMMUTING_PROJECTION_DERIVATIONS_OK 7_EXHAUSTIVE_CONFIGURATIONS`.

The exact counted configurations are \((q,n)=(2,1),(3,2),(5,2),(2,2),(4,2),(2,3),(2,4)\). The \(n=1\) computation is a boundary sanity check, not a claim of additional novelty. These finite experiments do not establish the infinite family without the algebraic proof. No external or independent validation was performed.
