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

The proof has two logically separate parts.

1. **Symbolic inclusion.** For each selected exponent vector on \(2,3,5,7,11,13\), the exact local-ratio product is at least one. Every larger prime is allowed only with exponent zero or one, and an exponent-one tail factor contributes \((q+1)/q>1\). Thus all selected integers satisfy the strict inequality except the five tail-free equality cases, a finite set of density zero.
2. **Exact density calculation.** `verify_density.py` enumerates all \(6^6=46656\) exponent vectors with exact rational arithmetic, finds \(17230\) accepted vectors and five equality vectors, sums the exact valuation probabilities, and verifies
\[
\frac{6W}{\prod_{p\in\{2,3,5,7,11,13\}}(1-p^{-2})}
=\frac{6097572635664749695003}{819750822146736480000}.
\]
Multiplication by \(1/\pi^2\) comes from the standard square-free Euler product for the unrestricted tail.

Fresh replay output:

`VERIFY_OK`

`patterns_total=46656 good_patterns=17230 equality_patterns=5`

`coefficient=6097572635664749695003/819750822146736480000`

`lower_bound=0.753659844064288`

Limits: the verifier certifies the stated finite union, not optimality of the cutoff or the exact comparison density. No finite sampling is used as evidence for the infinite lower bound.
