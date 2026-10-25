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

# Computational verification

`verify.py` completely reconstructs the finite unordered two-particle deleted-product cubical model on the one-skeleton of the four-dimensional cube, using literal binary vertex labels. It builds signed first and second boundary matrices over integers and checks their product is zero; constructs every disjoint coordinate-square torus as a signed \(16\)-square cellular cycle; constructs the complete cube-automorphism group; selects pivot classes modulo small primes; verifies a genuinely unimodular square minor over integers; and computes exact integer Smith normal forms of all relevant orbit matrices.

The output in `verification_output.txt` was obtained by executing the embedded `verify.py` with the environment versions in `requirements.txt`. Checks include the second boundary rank \(312\) modulo \(101\), \(88\) independent torus columns modulo \(2\), unit cellular determinant \(+1\), orbit sizes \((24,12,96)\), and six Smith invariant factors \(2\) for the nonparallel torus orbit. Each of the two parallel-orbit additions has all unit invariant factors.

The explicit signed finite matrices, full enumeration, exact determinant, and exact Smith reductions are proof certificates for the finite claim. Mod-prime ranks alone only give lower bounds, as accounted for in the written proof. These calculations do not assert results for hypercubes of other dimensions, and no independent audit has been performed.
