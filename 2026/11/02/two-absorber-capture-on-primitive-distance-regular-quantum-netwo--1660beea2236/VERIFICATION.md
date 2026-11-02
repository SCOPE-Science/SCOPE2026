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

# Reproducibility and limits

The universal proof is in `RESULT.md`, including the strict cosine-separation lemma, finite-dimensional non-Hermitian decay step, and explicit two-site projector inversion. The numerical and exact-arithmetic checks are independent finite corroboration, not an infinite certification.

## Executable checks

Execute `OPENBLAS_NUM_THREADS=1 python scripts/verify.py` with NumPy installed. This independently builds five primitive distance-regular graph examples, verifies each distance graph is connected, and for **every absorber pair** in each test graph calculates both (a) the two-column spectral Gram projector and (b) an independent singular-value Krylov projector, comparing all matrix entries and every starting-site probability. It tests \(21+45+595+1540+351=2552\) absorber pairs across \(7+10+35+56+27\) vertices per respective family. The largest finite numerical projector difference is \(2.856\times10^{-15}\).

Execute `OPENBLAS_NUM_THREADS=1 python scripts/exact_check.py` with SymPy installed. This constructs the exact rational adjacency projectors on the 10-vertex Petersen graph and 35-vertex Odd graph, verifies all projector identities and reconstructs their exact cosine values and all nonprincipal Gram minors for each admissible distance. Exact positive minors are listed in `verification_output.txt`.

The command output was reproduced from these standalone scripts and recorded as `verification_output.txt`. No external dataset or unembedded path is required. All statements about arbitrary graph order, diameter and absorber positions depend on the algebraic proof; finite checks do not extrapolate to every graph.

## Scope limitations

Two distinct absorbing vertices, strictly positive sink rates, uniform coherent adjacency hopping, all distance graphs connected, finite connected simple distance-regular graphs with at least three vertices. No claims are made about imprimitive families, noise, finite-time rates or additional absorbers.
