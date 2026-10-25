---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-23.md",
      "INDEPENDENT_AUDIT_2026-10-23.json"
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

Take Burek's explicit elliptic model with twelve Q(i)[v,t] sections, and use Burek Proposition 5.6's geometric Mordell–Weil upper bound 12 and good K3 specialization v=5. Conjugation σ fixes K=Q(v,t). Height pairing H of published points and cross-pairing G=<P_i,σP_j> define Gram pairings 2(H±G) of traces Q=P+σP and anti-traces R=P−σP. The inspected exact symbolic script constructs all twelve published x,y polynomials, tests Weierstrass identities and computes G by K3 type-IV component corrections and polynomial gcd intersection at v=5,7. Independently, I reconstructed rational H,G from the actual cross_pairing.json and checked rank(2(H+G))=8, rank(2(H−G))=4, nonzero principal minors 16777216/9 and 256, and det H=4096/9; a separate independent coordinate-derived cross-height spot check gives G_11=2/3 using exact gcd t at v=5. The 8 fixed and 4 anti-fixed independent generic sections saturate geometric rank 12, forcing Q(v,t) rank8 and Q(i)(v,t) rank12. This does not prove a saturated integral basis or ranks in other fields; prior geometric rank is an explicit input.

## originality

PASS

The original Burek paper gives geometric rank12 and coordinates of twelve sections over Q(i), but existence over Q(i) does not determine the rank of the Q-rational Galois fixed space. Kumar–Kuwata's generic K3 field-of-definition results concern distinct families and do not compute this curve's conjugate cross-height matrix. The new 8+4 eigenspace split therefore contributes arithmetic descent not shown in the inspected source statements.

## value

PASS

Arithmetic Mordell–Weil descent from a new geometric rank-twelve Calabi–Yau fibration is a natural invariant of independently motivated arithmetic geometry. Exact rank8 and conjugation eigenspace dimensions clarify rational sections vs quadratic-extension sections, useful without producing an integral basis or new geometric rank theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
