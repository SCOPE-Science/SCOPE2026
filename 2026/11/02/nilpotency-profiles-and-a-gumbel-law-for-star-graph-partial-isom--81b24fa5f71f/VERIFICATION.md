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

# Computational and mathematical verification

Execute `python verify_star_nilpotents.py` from the directory containing the checker. The checker independently enumerates all injective partial maps on each labeled star with one through five leaves, checks whether all pairwise ambient distances are preserved, and iterates each map through the maximum nilpotency index. It then compares exact counts for every pair (rank, index), the monoid cardinality, and the total nilpotent count against the stated coefficient formula. Actual execution completed with `VERIFY_OK`.

Observed total counts for numbers of leaves \(m=1,2,3,4,5\): all partial isometries \(7,22,83,442,3127\), nilpotent elements \(3,9,25,93,531\). The theorem assumes \(m\ge2\), while the smallest case serves as an additional boundary test.

The unrestricted proof uses a disjoint structural decomposition and labeled path/cycle generating functions. For asymptotics, the Poisson conditioning and local central limit argument is analytic rather than a finite search. The code does **not** establish the asymptotic Gumbel law, the nilpotent density, or statements for all star sizes. The Gumbel derivation is given in the proof, with its dependence on the local limit estimate explicit.

Independent external mathematical review has not been performed.
