---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

Each triangle forces three named colours, and a fixed target hub colour h leaves exactly two independent choices on each blade edge. The maximum number of endpoint agreements is 0 for hh, 2 for two distinct non-h colours, and 1 otherwise. Adding hub agreement gives precisely α_h in linear time. For k≥2 only h=C has the required ordinary profile; the weak distance minimizes over all h. Since there is only one C, every edge retains at least one vertex when h=C, giving both distances ≤k+1. With hub A, the even witness AC, (k−2)/2 AA and k/2 BB gives (α_A,α_B,α_C)=(2+k/2,1+k/2,k). The odd witness BC with (k−1)/2 of each AA and BB gives ((k+5)/2,(k+1)/2,k). Both profiles are admissible and yield ordinary equality; the weak maximum of the agreements is k from k≥4. At k=2 or 3, hub C already gives ≥k+1 agreements. Up to exchanging A and B, hub A and a C-edge AC leave BB for k=2 or AB,BB for k=3; hub A for the former and hub C for the latter give ≥k+1. A C-edge BC instead leaves AB at k=2, or two AB edges or AA,BB at k=3; respectively hub C, C or A gives ≥k+1. The same parity witnesses attain weak costs 2 and 3. At k=1 every permutation on K3 is proper. These are endpoint Hamming distances, not proper intermediate recolouring paths.

## originality

PASS

The supported claim is the exact ordinary and weak classification on the hub join of a matching, including the transition at k=4 and the per-source formula. The strongest literature comparison gives profile methods and general composition or extremal results, not a formula for this connected join. Same-day indexed results for the same graph family concern genuinely different colouring invariants, not equivalent repair radii.

## value

PASS

The friendship graph is a natural family where a single shared vertex couples all triangles. The exact formulas expose when changing the hub colour can strictly help a worst-case repair (k=2,3), and when this freedom no longer improves the worst case (k≥4). A linear-time formula computes each repair distance without enumerating exponentially many proper targets, making the classification a useful small benchmark for profile-sensitive repair.

The dated certificate retains the supplied scientific assessment, sources and limitations.
