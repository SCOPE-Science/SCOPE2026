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

# Verification of exact Bernoulli-image dependence phases

The bundled `verify.py` recomputes every one of the 256 Wolfram rule truth tables. For each rule it enumerates input words of lengths three, four, and five to compute symbolic joint probability polynomials for output words of lengths one, two, and three. It computes the exact monic gcd for each endpoint conditioning family, checks that the only possible common interior root is \(1/2\), and confirms the exact 32/56 one-dependence counts. It independently calculates both lag-two mean-difference polynomials and all seven exceptional bias values, with the 42/104/48/56/46 census stated in the theorem.

Running `python verify.py` with Python 3.10+ and SymPy installed regenerates `classification.csv`. This exact symbolic procedure returned:

```text
VERIFY_OK: 256 rules; one-dependent for every 0<p<1 exactly 32 rules;
at p=1/2 exactly 56 rules; no other exceptional one-dependence bias;
pairwise lag-2 independence generic 42, 7 exceptional biases;
independent 9-bit exact enumeration confirms 56/32/32/32 at 1/2,1/3,1/4,2/3;
classification CSV regenerated: 256 rows.
```

A separate direct enumeration of seven independent input bits for Rule 22 at \(p=1/3\) returned \(\Pr(A)=\Pr(B)=29/81\), \(\Pr(A\cap B)=97/729\), and covariance \(32/6561\). The mathematical argument in `RESULT.md` supplies the four-state stabilization lemma needed to pass from finitely many word tests to all half-line cylinder events. The script checks the finite calculations, not historical priority and not a statement about two or more temporal updates.

Independent audit has not been performed.
