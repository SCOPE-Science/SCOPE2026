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
# Verification

The proof package contains `artifacts/verify.py` and `artifacts/certificate.json`.

Run:

`python3 artifacts/verify.py`

The verifier reconstructs the source and target partial orders from the stated cover relations, exhausts all \(9^4\) set maps, and checks that exactly \(461\) are monotone. It then reconstructs the full pointwise order on the mapping space and replays every certificate entry.

For each of the \(426\) beat deletions it verifies, at the moment of deletion, that the stored witness is respectively the minimum of the strict upper set or the maximum of the strict lower set. It verifies that the remaining \(35\)-point subspace has no beat points.

It enumerates every chain of that core and checks the simplex vector \((35,94,80,24)\). For every one of the \(90\) simplicial collapses it recomputes the current maximal simplices and checks that the stored free face is codimension one and belongs to exactly one maximal simplex. It finally checks that the residual complex is a connected graph with \(25\) vertices and \(28\) edges, hence cycle rank \(4\).

The expected successful terminal line is:

`VERIFY_OK maps=461 deletions=426 up=179 down=247 core=35 simplices=35,94,80,24 collapses=90 graph=25,28 rank=4`

The computation proves only the finite combinatorial statements described above. The premise that \(R\) is weakly contractible comes from the cited Cianci--Ottina theorem that \(\mathcal K(R)\) is contractible. No minimality claim is verified.
