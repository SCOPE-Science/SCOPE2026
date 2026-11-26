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

Reconstructed the distinct-eigenvalue projector sum with H the unweighted adjacency. For each positive incidence singular sector a normalized left/right pair yields the two adjacency projectors with factor 1/2; hence the top sector gives zz^T/2, and the contrasts give C_a S_a C_a^T/2 and C_b S_b C_b^T/2. At a=b cross terms survive only on the midpoint block, where the Schur product of D_a⊗(J_b/b) with (J_a/a)⊗D_b, multiplied by 2 per eigenvalue and 1/4 from the projector factors and summed over two signs, gives (D_a⊗D_b)/(ab). The zero sector has the signed-constant original line and the row-and-column-zero midpoint subspace; its Schur square is the stated J/(a+b)^2 and S_a⊗S_b. The common PSD kernel gives Z=x=y=0 when a,b>=3. For a=2<b it forces zero column sums of Z, y=0 and x a contrast; when a=b=2 it allows the two single-index midpoint contrasts and the two original contrasts, but excludes the double contrast. For a=1, b>=3 the lifted condition gives y=-Z^T and the remaining scalar equations force sum(Z)=x=0. At (1,2) the same scalar equations force both sums and x to zero but the two contrasts are independent, and at (1,1) only x=-y with Z=0 remains. This proves the whole table. An independent finite reproduction, python -B reviews/check_biclique.py, found the squared eigenvalues from the characteristic polynomial and formed orthogonal nullspace projectors without using the frozen decomposition; exact stochasticity and ranks passed for (1,1),(1,2),(1,5),(2,2),(2,5),(3,3),(3,4). The frozen checker was inspected, not executed; these finite cases corroborate, not replace, the general proof.

## originality

PASS

The supported contribution is the specific two-parameter rational decomposition, kernels and sharp rank boundary, with distinct-eigenvalue treatment at equal dimensions. Neither the general projector identity, related graph families nor the known path cases are new here.

## value

PASS

Average mixing rank measures how much of the initial vertex distribution survives in the averaged observable; this is a natural exact invariant, not just a test of a few instances. The result identifies the sharp part-size cutoff, gives the entire hidden subspace at all thin boundaries, and shows exactly when coincident contrast spectra alter the matrix and the kernel on a canonical graph family.

The dated certificate retains the supplied scientific assessment, sources and limitations.
