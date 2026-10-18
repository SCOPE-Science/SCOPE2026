---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-18.md",
      "INDEPENDENT_AUDIT_2026-10-18.json"
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

For all connected complete multipartite graphs except stars: two colors force R_i=B_i in each part by outside-neighborhood balance and (r-1)(R-B)=0; hence every part is even, and the half-half coloring is sufficient. K4 and K_{2,1,1} require four. For N>=12, 123-periodic colors over part blocks give every outside-part color spread <=2; for degrees >=6, maximum <=d/2, while placing a uniquely large low-degree part last gives direct d=2..5 balance. Inspected verify.py exhaustive count matrices for all profiles N<=11 (183 listed), and independently enumerated all nonstars through N=8, finding 7 two-color, 42 three-color and 2 four-color profiles. Infinite result uses proof, not stress tests.

## originality

PASS

Best-of-knowledge new three-versus-four strong-majority vertex palette classification; exact two-color neighborhood-balanced criterion and K4 exception are acknowledged prior results, not claimed new. Distinguish majority C-chromatic count and strong-majority EDGE index from vertex palette parameter.

## value

PASS

Exact natural classification for all connected complete multipartite graphs, with two unexpected four-color obstructions, closes the gap between known neighborhood-balanced two-color criterion and minimum unrestricted strong-majority palette.

The dated certificate retains the supplied scientific assessment, sources and limitations.
