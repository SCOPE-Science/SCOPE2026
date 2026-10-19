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

# Verification

The accompanying `CHECK.py` builds the generalized quaternion group directly with products \((i,e)(j,f)=(i+(-1)^e j+nef,\ e+f\bmod2)\) in coordinates modulo \(2n\), constructs exact integer matrices for left multiplication by each balanced four-tap sum, and performs modular Gaussian elimination over the prime \(1000003\). Its output is compared against the full analytic nullity formula. Exhaustive normalized difference-and-offset tests for \(k=2,3\) comprise respectively 147 and 675 operator comparisons, with 150 and 45 additional deterministic randomized comparisons for \(k=4,5\). The script also calculates complete difference-pair histograms and verifies the first-moment formula for \(k=2,3,4,5\). All runs succeeded.

The complete proof is independent of the modular computations. Its key critical points are the multiplicity-two occurrence of each two-dimensional irreducible in the regular representation; nested dyadic congruence classes; the zero-block valuation criterion; the exceptional odd-block case; and the exact inclusion–exclusion for the aggregate mean. Modular rank cannot itself establish a complex *upper* rank bound when the relevant determinant vanishes modulo the prime. No unrestricted claim is based on that inference.

The stated boundary is \(k\ge2\), with exactly two distinct taps in each cyclic coset and coefficient one on each tap. A support is counted once as a four-element set. Equivalent sign choices of the two nonzero differences leave the formula unchanged. The theorem makes no assertion about other support families or arbitrary coefficient choices.
