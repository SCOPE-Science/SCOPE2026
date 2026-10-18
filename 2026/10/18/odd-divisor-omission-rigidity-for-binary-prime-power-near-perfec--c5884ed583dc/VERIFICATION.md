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

# Reproduction and verification

The proof uses only the elementary geometric-series identity and modular arithmetic, with no external theoretical black box. The crucial identities are \(Q=(p^e-1)/(p-1)\), \(p^e=(p-1)Q+1\), and \(\sigma(2^kp^e)-2\cdot2^kp^e=(2^{k+1}-p)Q-1\). The subset-count argument is exact and covers all parameters, not just a numerical range.

Run `python3 verify.py`. The expected output is:

```
checked 1680 triples; 243840 subsets; 21 matching cases
```

The verifier enumerates all subsets of the \(e+1\) odd divisors for \(k\in\{1,\ldots,10\}\), \(e\in\{2,\ldots,8\}\), and each odd prime \(p\le97\), computing ordinary divisor sums exactly. This checks all candidates in the stated finite box but makes no assertion about other parameter values. Failure to find a counterexample in this box is not itself an infinite proof; the independent modular argument supplies that proof.

As a hand check, \(n=162\) has \(\sigma(n)=363\), \(2n=324\), and the only qualifying odd deletion set is \(\{3,9,27\}\), which sums to \(39\). The proof concerns only odd-only deletion sets, not mixed-parity sets. No separate independent audit has been performed.
