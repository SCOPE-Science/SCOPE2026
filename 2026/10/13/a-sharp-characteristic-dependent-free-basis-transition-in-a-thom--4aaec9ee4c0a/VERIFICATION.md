---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-17.md",
      "INDEPENDENT_AUDIT_2026-10-17.json"
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

Reconstructed reducedness: G squarefree, gcd(G,H)=1; if p∤d then H_z=−dz^{d−1}, while when p|d, H is nonreduced precisely for all p|k_j. Writing U=x∂x+y∂y, A=L(−b∂x+a∂y), det(U,A,∂z)=G, tame frame E=U+z∂z, B=A+(zβ/d)∂z, T=z^{d−1}U+P∂z has det(E,B,T)=GH; wild frame (∂z,U,HA) also has determinant GH. Checked logarithmic multipliers algebraically. Squarefree determinant/divisibility makes each frame span in arbitrary characteristic; deg 0,1,d+m−1 in wild case. H_z=0 forces tangent concurrence; H(0,0,1)=−1. Exact source verifier inspects 13 representative specializations but universality follows from determinant identities, not sampling.

## originality

PASS

General published char-zero freeness for precisely the same divisor is credited. The wild positive-characteristic reducedness threshold, explicit degree-zero free derivation, wild basis transition and tangent-concurrency phenomenon are not stated in the inspected original theorem or general methodological references. Best-of-knowledge PASS with implicit corollary/unindexed characteristic-p work risk.

## value

PASS

The complete characteristic-dependent logarithmic module is a natural invariant of an established free-curve family; an Euler-derivation degeneration changes the degrees and global tangent geometry. Exact p-th-power boundary and full formula across all positive weights are structurally motivated, rather than a small isolated computational gain.

The dated certificate retains the supplied scientific assessment, sources and limitations.
