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

Install Python 3.10+ and `sympy==1.14.0` from `requirements.txt`, then run `python verify_durer.py`. The program is standalone and reconstructs every graph and chain object from the explicit definition of the generalized Petersen graph, without downloaded tables or other data dependencies.

Checks include: complete face enumeration and face vector \((18,117,334,402,156,10)\); a \(507\)-pair acyclic discrete-Morse matching with one critical zero-cell and \(22\) critical three-cells; exhaustive generation of \(93\) disjoint-four-path octahedral carriers; zero signed boundaries of their sixteen-term fundamental cycles; exact integral unit cancellations; a unimodular \(22\)-carrier minor; twelve automorphisms and eleven carrier orbits; exhaustive integral Hermite normal forms for all \(55\) two-orbit and \(165\) three-orbit unions; and Smith normal forms with factors \((2,2)\) for precisely the three index-four spanning triples. The marker `VERIFY_OK_DURER_INTEGRAL_SHORTEST_OCTAHEDRAL_CARRIERS` is printed only after every assertion succeeds.

These are exhaustive finite checks for the stated graph. The sharp general flag-support lemma and the cellular discrete-Morse interpretation are mathematical arguments stated in `RESULT.md`, not consequences extrapolated from tests. A separate independent scientific audit has not been performed. Bibliographic priority and any implication from unindexed sources are not mechanically certified.
