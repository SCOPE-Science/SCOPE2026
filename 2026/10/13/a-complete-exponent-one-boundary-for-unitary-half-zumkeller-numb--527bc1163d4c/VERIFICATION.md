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

The proof depends on the exact proper-unitary-divisor list \(\{1,A,B,AB,C,AC,BC\}\), the equivalence of equal-sum partitions with a seven-sign equation, and three exhaustive exponent-boundary arguments. In the bound \(a=1,b\ge2\), \(|D|\ge B-3\) forces \(B\le9\); in \(b=1,a\ge3\), \(|D|\ge A-4\) forces \(A\le24\); in \((a,b)=(2,1)\), the vanishing-denominator branch has \(N\ne0\). All cases are completed by explicit partition witnesses.

`verify.py` implements two independent finite descriptions: a direct subset-sum test on the seven proper unitary divisors and exhaustive enumeration of all signed coefficients. Running `python3 verify.py` reproduced `verification_output.txt`. The run covered 2277 parameter tuples with \(\min(a,b)=1\), exponents up to \(12\) on the unrestricted block, primes through \(150\), and prime-power exponents through \(3\). The script also checks the six exceptional witnesses and the four exclusions from full unitary Zumkeller membership.

Neither these computations nor the finite OEIS table prove the unlimited assertion. The unrestricted proof is the signed-coefficient argument in `RESULT.md`. No machine-certified theorem prover or independent mathematical review was performed.
