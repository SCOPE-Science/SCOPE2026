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

# Mathematical verification and reproducibility

The proof contains three independent exact arguments: the three-moment off-diagonal characterization of a Parseval operator, the analytic four-node solution with a strictly positive cosine weight, and cyclotomic irreducibility for rational-weight lower bounds and classification. A fourth argument establishes distinctness of translated examples. The theorem is for all primes \(p\ge5\); the supplied finite evaluations do not replace these arguments.

The standalone file `verify.py` executes without nonstandard dependencies. It directly constructs the complex three-by-three Gram matrix from each explicit family at the seven primes \(5,7,11,13,17,31,101\). There are fourteen successful Gram comparisons; the maximum entrywise residual was \(6.66\times10^{-16}\). It separately checks positivity, distinct support nodes and the trigonometric disparity. Results are in `verification_output.txt`.

No exhaustive real-weight classification, perturbation bound or independent mathematical audit has been performed. The numerical residual is a floating-point error, not a certified error bound for all field orders.
