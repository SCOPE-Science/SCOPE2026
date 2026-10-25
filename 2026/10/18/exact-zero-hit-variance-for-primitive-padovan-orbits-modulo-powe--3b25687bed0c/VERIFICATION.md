---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-20.md",
      "INDEPENDENT_AUDIT_2026-10-20.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

PASS: Q is unimodular and Q^7=I+2B, Q^14=I+4D with det(B)=det(D)=1. Squaring shows the exact primitive period T_k=7·2^(k-1), giving N_k=4^(k-1) cycles. For lag h not divisible by 7 the two observation rows remain independent mod 2; for h=7t their common 2-adic content is 2^(1+v_2(t)), which leads to primitive solution count C_h=2^(k+hval-1). Summing the six ordinary lag classes and k-1 2-adic valuation classes gives E Z_k=3, E Z_k²=k+8, Var=k-1. Independently enumerated all primitive cycles for k=1..4 and checked exact first two moments, including k=1 boundary. This does not prove the infinite period lifting by enumeration.

## originality

PASS

Best-of-knowledge claim-versus-prior assessment with direct source comparisons; see four named checks, source inspections and retained risks.

## value

PASS

PASS: The exact variance k-1 of zero-hit counts on every primitive orbit is a natural finer statistic beyond classical period computations; it quantifies increasingly unequal zero occurrence despite constant mean. A complete ensemble moment can support error analysis and pseudorandom-recursion design; no paper-sized extension is required.

The dated certificate retains the supplied scientific assessment, sources and limitations.
