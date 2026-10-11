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
# Reproducible checks

Run `python3 verify_star_diameter.py` with Python 3. The program requires only standard-library modules and prints `PASS` when successful.

The proof in `RESULT.md` reconstructs the support vertices and then establishes the diameter and all equality cases symbolically for every integer \(r\ge2\) and allowed real weight vector. Finite enumeration is not used as an all-dimensional proof.

The code independently generates exposed vertices by selecting a maximizing coordinate in each weighted hyperedge for every strict order of the hub and leaves. It verifies equality with the predicted prefix-weight vertex set and checks each squared pair distance and all equality cases exactly. The exhaustive cases are \(2\le r\le5\), every cut-off \(m\) and four nonnegative nonuniform weights at each size, totaling 30 checks. Additional binomial identities are tested at 299 parameter instances through \(r=24\).

Excluded claims: arbitrary asymmetric or signed weights, graph-theoretic diameter, and the Euclidean metric of a projection. An originality search is not independent certification.
