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

The accompanying `verify_dihedral_cover.py` uses only the Python standard library. Execute `python verify_dihedral_cover.py` from the directory containing it. It constructs the finite dihedral group, verifies that doubling rotation exponents is an automorphism for the tested odd indices, evaluates branch inertia permutations of the degree-\(2n\) action, all four classes of crossing-orbit cardinalities, and the faithful order \(4n^2\) permutation image. The finite test indices are \(n=5,7,9,11,13\); the expected final line is `VERIFY_OK`.

For arbitrary odd \(n\ge5\), correctness depends on the written group-theoretic proof: trivial graph core by \(Z(D_n)=1\); reflection and rotation cycle structures; reflection centralizer cardinality \(2\); and the known local stabilizer descriptions of Malara--Merta--Szpond--Zieliński. No computation over five instances certifies those universal statements. The branch discriminant coefficient follows from the tame codimension-one discriminant formula, independent of the finite enumerator.

No independent audit or external certificate has been performed. The inspected sources are identified in the references; no claim of exhaustive publication coverage is made.
