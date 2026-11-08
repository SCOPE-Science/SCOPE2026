---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-04.md",
      "INDEPENDENT_AUDIT_2026-11-04.json"
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

The additive function F(n)=∑_{p^a∥n} log[(p^a+1)/(∑_{d|a}p^d)] has a limiting law by the Erdős–Wintner conditions; the Lévy continuity criterion applies because f(p)=log(1+1/p)≠0 for all primes and ∑1/p diverges, so δ=P(X>0). For p>31 all exponents a≥2 satisfy local ratio <1, so a=1 upper-majorizes positive-exponent states. Integer upper logarithm grids β=50001/50000 preserve strict event inclusion; 11 capped small primes have explicitly charged missing mass. An independently rerun integer-convolution certificate over 168 primes ≤1000 generated 153387 coefficients, offset −52491 and threshold 51991; exact rational comparison gives P(S≥−500)<784271/10^6 and omitted mass <145/10^6. Infinite tail U=∑_{p>1000}1_{E_p>0}/p has E exp(1000U)<6, so Markov and rational exp bounds give P(U>500logβ)<300/10^6. Total strict upper <784716/10^6. The finite certificate and analytic infinite-tail argument are separate; no numerical finite-n density extrapolation.

## originality

PASS

Trudgian’s 2013 original explicitly asks for the strict density, supplies a squarefree lower bound and finite-n sample ~0.778307, not rigorous upper. Tenenbaum–Verwee give general distribution theory, not the inequality-specific numerical bound. Published Resultary SCOPE record gives rigorous lower 0.753659844…, logically complementary, not covering an upper. No matching stronger upper found in bounded checks; cannot certify no specialist source exists.

## value

PASS

A rigorous nontrivial numerical upper bound answers the quantitative side of an explicit natural multiplicative-arithmetic density question with an existing lower bound and sample measurements. The computed finite-prime cylinder is substantively motivated by this open comparison, not arbitrary table recomputation, and the rigorous infinite-prime control closes the infinite problem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
