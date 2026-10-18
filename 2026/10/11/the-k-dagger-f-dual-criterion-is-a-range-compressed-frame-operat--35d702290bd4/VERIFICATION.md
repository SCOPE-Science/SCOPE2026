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

For Bessel F and closed-range K, K† is bounded and reconstruction of K†F through F is S_F(K†)*. Moore–Penrose identities (K†)*K*=P_R(K), K*(K†)*=P_{N(K)⊥} imply S_F(K†)*=K iff S_FP_R(K)=KK*. Direct one-point example H=C, K=I/2, F=1 has ∫|<f,F>|²=||f||² and ||K*f||²=||f||²/4, satisfying printed mixed A=B=1 frame inequalities, but reconstruction 2I≠I/2. Exact direct operator proof, no numerical dependency.

## originality

PASS

Published K-Parseval frame dual results use the stronger exact S_F=KK* hypothesis, not the printed mixed A=B=1 inequalities. The exact iff criterion S_FP_{R(K)}=KK* and its one-point refutation of the specific 2021 lemma are not supplied by the checked related K-frame studies; best of knowledge with unindexed erratum risk.

## value

PASS

Identifies a false canonical-dual lemma under its printed mixed Parseval convention and replaces a merely sufficient all-space operator identity with the exact weaker range-compressed necessary-and-sufficient criterion; clarifies genuine reconstruction for non-surjective K.

The dated certificate retains the supplied scientific assessment, sources and limitations.
