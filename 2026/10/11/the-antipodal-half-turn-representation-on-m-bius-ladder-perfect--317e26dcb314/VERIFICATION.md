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

# Exact checks and proof boundaries

Run `python3 verify_ladder.py` with Python 3 standard library only. The script constructs graph edges and their central half-turn permutation, computes all perfect matchings, and enumerates all faces for each size from \(n=2\) through \(n=9\). A direct signed invariant-simplex calculation is compared against a separately enumerated cyclic monomer–dimer partition function and the proven parity formula. The final output is `VERIFY_OK` only if every assertion holds.

For \(2\le n\le8\), the program additionally constructs mod-two augmented boundary maps and performs exact bitwise Gaussian elimination to recover reduced Betti numbers; this checks the ranks quoted from Agarwal–Basak in a finite range. The homology output vector uses position zero for degree minus one (the augmented chain convention); positive simplicial degree is shifted accordingly. These computations do **not** determine rational homology solely from their finite mod-two values; the published non-equivariant homotopy theorem is essential.

The universal Lefschetz equality is established symbolically: each invariant face is a uniquely extendible column monomer–dimer packing; alternating over every unused monomer gives a binomial cancellation; the only survivors are the two complete dimer tilings for even column count. For odd column count none survive. The transition from reduced Lefschetz number to full rational \(C_2\)-representation uses a published universal homology rank/dimension theorem and elementary order-two linear algebra. The experiment is a guard against indexing and orientation errors, not proof by sampling.

Independent audit has not been performed. An unindexed overlap remains possible.
