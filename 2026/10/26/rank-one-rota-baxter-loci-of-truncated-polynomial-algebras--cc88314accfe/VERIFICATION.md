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

# Reproducibility and verification

The theorem is established symbolically in `RESULT.md`: factor a nonzero rank-one map as \(a\otimes\varphi\), reduce the weight-zero Rota–Baxter equation to \(a^2=0\) and \(\varphi(aA_n)=0\), and use the exact \(t\)-adic valuation and principal ideals in \(k[t]/(t^n)\). The geometric component and intersection formula follows by elementary rank-one determinantal coordinates. These arguments apply to all fields and all integers \(n\ge4\).

Run `python3 CHECKER.py` using Python 3 without external dependencies. For each test it enumerates all nonzero rank-one maps with canonical image-line generators. It directly checks the original Rota–Baxter equation on each ordered pair of basis elements and compares the decision to the independently computed valuation predicate, all valuation fibers and the claimed point-count formula. The arithmetic covers prime fields \(\mathbb F_2\), \(\mathbb F_3\) and the extension field \(\mathbb F_4\). Observed final line: `RANK_ONE_ROTA_BAXTER_IDENTITY_OK 13 cases`.

Coverage: \(q=2\), \(2\le n\le7\); \(q=3\), \(2\le n\le5\); \(q=4\), \(2\le n\le4\). The tests also include boundary lengths \(n=2,3\) outside the claimed range. In total, 77,267 distinct nonzero rank-one maps were checked across 13 cases. Small finite enumerations do not certify the infinite family, higher-rank solutions or scheme-theoretic reducedness; the theorem instead explicitly defines the reduced locus and provides a general proof.
