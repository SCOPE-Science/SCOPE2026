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

# Verification and reproducibility

The included `verify_p5.py` enumerates every nonempty vertex subset of the complete bipartite graph for each of six size pairs. It checks the exact path-forbidding criterion, computes all simplicial boundary ranks by independently implemented finite-field elimination over four prime fields, and confirms that only degree-three reduced homology survives, with the rank given by the theorem. It passed for \((3,3),(3,4),(4,4),(3,5),(4,5),(5,5)\) and primes \(2,3,5,101\).

The included `verify_char.py` independently builds the allowed vertex subsets and computes signed oriented-simplex traces under every color-preserving automorphism of each of three small graphs. Its checks cover all \(36\) group elements for \((3,3)\), all \(144\) for \((3,4)\), and all \(576\) for \((4,4)\). Every trace agrees both with the closed character formula and the sum of three exterior-standard tensor-product characters.

Run both programs with `python3 verify_p5.py` and `python3 verify_char.py`, using Python 3 with the standard library only. The expected final lines are `ALL EXACT FINITE HOMOLOGY CHECKS PASSED` and `ALL EQUIVARIANT LEFSCHETZ CHECKS PASSED`.

The finite tests do not constitute an infinite proof and cannot establish integral torsion freedom on all graph sizes. That conclusion follows from the explicit integral connecting map, which contains a full-rank identity minor and whose kernel is a subgroup of a free abelian group. The representation theorem concerns the color-preserving group only. No independent external audit or validation has been performed.
