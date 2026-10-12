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
# Verification of exact Jacobian-rank stratification

All computations use exact coefficient fields. With SymPy 1.14 or later, run `python verify.py`, `python verify_special.py 4`, and `python verify_special.py 5` from the directory containing both scripts. Both scripts are supplied in full; no recorded output is accepted in place of actually executing them.

The generic multiplication matrices in degrees \(3,4,5\) have shapes \(55\times30\), \(66\times45\), and \(78\times63\), respectively. The first verifier checks ranks \(30,43,56\) over \(\mathbb Q(t)\). Two degree-three maximal minors have gcd proportional to \(t^7\), two degree-four minors have gcd proportional to \(t^{11}(t^2+4)\), and a degree-five maximal minor is proportional to \(t^{15}(t^2-1)(t^2+4)^2\). The chosen minors and their exact coefficients are embedded in `verify.py`, so no unpublished computation or external data set is required. The scripts check specialization at \(t=1\) and at \(t=2i\), with the opposite signs supplied by the involution \(x\mapsto-x\).

The singularity calculation also requires independent geometric reasoning: the three fixed line-conic contacts and the three fixed line crossings are directly substituted into the factors; the new conic meets the three fixed lines in two points each, and its four intersections with the fixed conic satisfy \(x^2+tx-1=0\). The discriminant \(t^2+4\) and the two line-node conditions \(t=\pm1\) exhaust collisions; Bézout gives global exhaustiveness. These steps are explained in the proof, not delegated to a numerical sampler.

The checks do not certify all higher Jacobian syzygies, any characteristic-positive analogue, or exhaustive novelty in unpublished literature. Independent audit status: not performed.
