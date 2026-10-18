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

# Reproducibility and boundaries

The algebraic proof in `RESULT.md` is an all-index proof. No external certificate or infinite computation is claimed. The critical identities to recompute symbolically are the polynomial transfer formulas for \(\Theta((x-1)^k)\), the first two jets of \(\Theta(Q)/8\), the Chebyshev base seeds, and \(R_2'(1)=r^2(4r^2-1)(r^2+3)(4r^2+101)/630\). Their derivations are supplied in `RESULT.md`.

The standalone `opt_even_verify.cpp` uses modular generating-function multiplication, not the Chebyshev recurrence. Compile using `g++ -std=c++17 -O2 -Wall -Wextra opt_even_verify.cpp -o opt_even_verify` and execute `./opt_even_verify`. It checks the stated residues of the difference for twelve values of \(m\) and all admissible indices and \(n\) within coefficient bound \(2048\); an observed successful run printed:

```
VERIFY_OK cases=10116 odd_square_witnesses=364 colors=12 range_max=2048
```

These cases are finite and cannot establish the universal result. The proof applies for \(i\ge3\) when \(\nu_2(m)=1\), and \(i\ge2\) otherwise. Earlier index values are not claimed. No independent expert audit has been conducted.
