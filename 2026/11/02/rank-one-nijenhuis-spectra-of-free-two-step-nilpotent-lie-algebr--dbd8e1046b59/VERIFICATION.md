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

# Reproduction and verification

Run `python verification/verify.py` with Python 3.10+ and NumPy installed. The checker uses the Lie bracket \([v+z,w+t]=v\wedge w\) and tests the Nijenhuis torsion for all nonzero rank-one factorizations \((u,\phi)\) in the listed finite-field configurations, then divides the counts by \(q-1\) to count distinct maps.

The exhaustive prime-field cases are \((n,q)=(2,2),(2,3),(2,5),(3,2),(3,3)\). The quadratic extension case \((n,q)=(2,4)\) uses \(\mathbb F_4=\mathbb F_2[a]/(a^2+a+1)\) and checks the original operator identity directly on each basis pair.

For the six cases, the respective triples (total rank-one Nijenhuis maps, non-character maps, maps with nonzero trace) are `(21,0,12)`, `(104,0,72)`, `(744,0,600)`, `(833,392,224)`, `(18590,9126,6318)`, `(315,0,240)`. Exactly `554023` nonzero factor pairs were tested. The expected completion marker is `NIJENHUIS_RANK_ONE_FREE_CLASS_TWO_OK 6 554023`.

For the general case, verify independently from the proof that the relevant annihilator of \(v\wedge V\) has dimension \(\binom n2-n+1\), then count the possible central corrections and scalar factorizations. No finite computation alone can justify the all-dimension result. This package does not prove publication priority or provide independent third-party validation.
