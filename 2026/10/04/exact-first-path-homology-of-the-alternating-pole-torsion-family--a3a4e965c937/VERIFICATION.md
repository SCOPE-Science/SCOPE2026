---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-05.md",
      "INDEPENDENT_AUDIT_2026-10-05.json"
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

The proof was reconstructed from the frozen RESULT.md rather than from the saved audit. For the non-regular integral path complex, the allowed 2-paths split by endpoints exactly as claimed: each \(c_i\to c_{i+2}\) class has the two routes through \(c_{i+1}\) and the appropriate pole, giving the boundary \(R_i\), while each pole-to-itself class contributes differences of same-parity spoke cycles. No other missing-shortcut class permits cancellation. The underlying directed graph has cycle-lattice rank \(4n-1\); the \(4n\) cycles \(R_i,T_i\) have the single primitive alternating relation. Quotienting by the \(R_i\) boundaries and the same-parity \(T\)-differences leaves two generators \(U,V\) with relation \(n(U-V)=0\), hence \(\widetilde H_1(D_n;\mathbb Z)\cong\mathbb Z\oplus\mathbb Z/n\mathbb Z\) for every \(n\ge2\).

## originality

PASS

The 2020 primary source introduces exactly this alternating-pole central-cycle family and explicitly states the \(\mathbb Z/n\mathbb Z\) torsion pattern as a conjecture, computationally checked only through \(n=8\). The submitted theorem proves that conjecture for all \(n\) and also identifies the free \(\mathbb Z\) summand. Fresh Resultary and web searches did not locate a prior proof or a stronger theorem implying the full integral group.

## value

PASS

This closes an explicit all-parameter torsion conjecture from the defining path-homology paper and strengthens it to the complete first integral homology group. The symbolic cycle-lattice/Smith presentation is a structural theorem, not a finite extrapolation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
