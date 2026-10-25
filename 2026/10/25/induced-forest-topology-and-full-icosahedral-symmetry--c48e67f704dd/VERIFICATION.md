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

# Verification instructions

Execute `python3 verify.py` with Python 3. The script is standalone and uses only standard-library modules. Compare its stdout with `verification_output.txt`; success concludes with `VERIFY_OK`.

The script explicitly lists the thirty graph edges and three full-symmetry generators. It checks both definitions of an induced forest against all \(2^{12}\) vertex subsets, reconstructs the acyclic matching, and verifies absence of cycles in the complete directed face Hasse diagram. Critical-cell data establish the integral homotopy equivalence, while ordinary simplicial boundary ranks are separately recomputed over \(\mathbb F_2\) and \(\mathbb F_3\).

For the symmetry claim it verifies that 120 generated permutations preserve the icosahedral graph, that a directed triangular flag bounds the full automorphism group by 120, and that signed Lefschetz traces agree with the exact rational irreducible decomposition. The result makes no assertion about integral representation splitting or an equivariant wedge decomposition. Independent validation has not been performed.
