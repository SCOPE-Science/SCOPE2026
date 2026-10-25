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

Translate each selected KG(n,2) vertex into a K_n edge, and let H be the selected edge set. A test edge uv has exactly q_H(uv)=|H|-d_H(u)-d_H(v)+1_{uv in H} disjoint selected edges. Thus the ordinary fort rule excludes q=1 on unselected uv and skew fort excludes it on all uv. The submitted structural proof correctly rules out sizes 1,2,3 (consider all simple three-edge shapes), and classifies four-edge H by max degree: degree 4 forces a four-star; degree 3 permits only K_1,3 plus disjoint K_2 when n=6; max degree <=2 implies no mixed positive degrees 1 and 2 and hence C4 or matching4. Cycle and six-vertex claw+edge each have an *inside* selected vertex with exactly one disjoint selected edge and fail skew, while star/matching are skew forts. Independent from graph-neighborhood definitions (not the shape classifier), I enumerated every four-vertex subset for n=5,6,7,8, obtaining ordinary/skew counts (20,5),(135,30),(210,105),(595,385). Shapes give n*C(n-1,4), 3*C(n,4), 105*C(n,8), 60 only n=6. Terminal white fort equivalence establishes both failed-forcing numbers C(n,2)-4; no assertion about all inclusion-minimal forts or higher r.

## originality

PASS

The full paired minimum-fort shape spectrum and ordinary/skew multiplicities are not implied by the known ordinary failed-forcing number of KG(n,2), because a scalar maximum says nothing about its number or shape of attaining sets. A known skew-successful forcing parameter is different from failed skew. The inaccessible 2024 exact KG ordinary-failure paper could contain some ordinary shape data, so coverage risk remains explicit; the independent skew count/classification is beyond its established ordinary scalar. The combined claim best-of-knowledge passes with this named risk.

## value

PASS

Maximum failed-set multiplicities quantify how many distinct extremal forcing obstructions occur in a classical symmetric graph family; ordinary and skew processes have the same extremal size but provably different optima. The classification explains the n=6 exceptional six-vertex shape and onset of matching configurations n>=8, an intrinsically motivated full all-n census rather than a scalar rebranding.

The dated certificate retains the supplied scientific assessment, sources and limitations.
