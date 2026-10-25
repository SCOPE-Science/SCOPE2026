---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-24.md",
      "INDEPENDENT_AUDIT_2026-10-24.json"
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

For F(t)=t^4+1, the integral resultant identity bounds common factors for shifts 1..5. Independent SymPy computations gave R_1=153=3^2*17, R_2=73728=2^13*3^2, R_3=46584153=3^4*7^2*11^2*97, R_4=4421910528=2^16*3^4*7^2*17, and R_5=154497425625=3^6*5^4*23^2*641. Every odd prime divisor of F(t) has order 8, hence p=1 mod 8 and only 17,97,641 remain; each is simple in its relevant resultant, excluding hidden common valuation >1. Independent root lists and modular gap pairs matched 17: (8,1),(15,4 with wrap); 97: (47,3); 641: (318,5). v2(F(t))=1 iff t odd. Thus exactly the indicator formula and least periods 17,34,1649,3298,1057009. Exhaustive CRT counting over 17*97*641=1057009 residue triples reproduced all eight values/multiplicities, and direct product/lcm checks for n=1..299 and k=1..5 matched. Computation checks finite arithmetic; universal proof uses resultants and modular root exhaustion.

## originality

PASS

PASS best of knowledge for the exact Phi_8 k<=5 quotient formula, least periods and complete k=5 frequency table, not for the general resultant technique. Bodin-Drouin treat gcd of two polynomial values through resultants and period patterns; Farhi-Kane and other progression papers address linear/quadratic/cubic or generic periods, but none inspected enumerates these four collision types or the eight exact frequencies. An unindexed Phi_8 table could cover the narrow result.

## value

PASS

This is a natural cyclotomic quartic test case in the established consecutive-polynomial LCM quotient problem. The first exceptional gap-five collision at 641 and concomitant loss of parity in the least period are meaningful exact arithmetic boundaries; the full CRT spectrum is directly reusable as a nontrivial benchmark for degree-four extensions.

The dated certificate retains the supplied scientific assessment, sources and limitations.
