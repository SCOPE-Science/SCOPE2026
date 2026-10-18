---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-16.md",
      "INDEPENDENT_AUDIT_2026-10-16.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

Checked exact problem domain n=2^(alpha−1)p^(beta−1), alpha,beta>1, p odd prime <3·2^(alpha−1)−1, k=13, M=8191. Primary Chu Lemmas 8,9,10 yield alpha≤v+1 for p≡1(mod4), p^(2^v−27)<2^(13(v−1))/8191 for p≡3(mod4), alpha≤lambda+v for p+1=2^lambda q. Growth yields v≤4 or v≤5; p=M=8191 separately excluded by LTE. The non-Mersenne case t≠2^v uses finite bound 2^m ≤ (|2^(13v)−t^13|+1)/t. Independently regenerated all exact integer candidates admitting composite p (over-enumeration): p≡1 cases empty for v1,2 and only (alpha,p,valuation)=(4,5,1) at v3,4; p≡3 max valuation u=(0,1,1,2,2) at v1..5. These contradict beta−1≥2^v−1 except Mersenne p=2^alpha−1, beta=2. Chu Theorem3 reverse holds excluding 2^12·8191. Finite enumeration is proven exhaustive by prior inequalities; not mistaken for infinite proof.

## originality

PASS

Conjecture 5 of Chu is proved for k=5 and previously solved for k=7 in other publication; the k=13 branch needs its own new cutoffs and finite exact elimination and is not a corollary of source k5 or k7.

## value

PASS

Settles an explicit genuinely open prime-exponent instance of Chu’s divisor-sum conjecture beyond the earlier k5/k7 cases; the exact finite certificate combined with global inequalities gives a meaningful arithmetic classification, not a finite table substituted for proof.

The dated certificate retains the supplied scientific assessment, sources and limitations.
