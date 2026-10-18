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

# Verification notes
Run `python3 verify.py` using a Python 3 standard library. The supplied executable enumerates the three rooted fully bifurcating five-tip topologies and constructs every fixed-size subset's rooted PD from the actual descendant sets and edge lengths. Exact symbolic quadratic arithmetic reproduces the two strictly negative \(1+4\) decompositions and the two \(2+3\) phase polynomials; exact rational arithmetic reproduces the five witness variances and both strict peak gaps. A second, separately encoded edge list evaluates all 31 nonempty subsets without using the symbolic-variance routine. The check completed successfully on the supplied file.

The proof of sharpness for at most four tips is analytic, relying on the constant singleton and complete-sample variances. The proof that the two nonpositive decompositions are strict on the positive-edge domain is analytic. No finite experiment supports an unbounded extrapolation. The verification does not assess real-tree phylogenetic uncertainty or bibliographic novelty. Independent audit has not been performed.
