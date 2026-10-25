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

Run `python3 verify.py` with Python 3. The program independently forms all actual matrices over indicated finite rings and tests \(X^2=0\) by ring multiplication, without using the anticommutator normal form. It enumerates every module vector to compute the exact image size and infers the two image invariants from reduction rank and cardinality. The rank formula is computed separately through Gaussian binomial coefficients.

The passing test included \(n=1,2,3\) for \(q=2\) over both \(\mathbb Z/4\mathbb Z\) and dual numbers; \(n=2\) for \(q=3\) over both \(\mathbb Z/9\mathbb Z\) and dual numbers; and \(n=2,q=4\) over dual numbers over \(\mathbb F_4\). The program printed `VERIFY_OK_SQUARE_ZERO_CHAIN2_SHAPE` on success. For \(n=3,q=2\), each of the two nonisomorphic rings yielded exactly \(1184\) matrices satisfying \(X^2=0\), with the six nonzero strata \((r,t)=(0,0),(0,1),(0,2),(0,3),(1,0),(1,1)\) having counts \(1,49,294,168,336,336\), respectively.

Exhaustive checks cover only the enumerated small cases and do not establish any result beyond them. The unrestricted correctness argument is the mathematical proof in `RESULT.md`. No independent external mathematical audit has been conducted.
