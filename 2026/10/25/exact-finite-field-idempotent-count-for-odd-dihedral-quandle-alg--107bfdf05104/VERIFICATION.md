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

# Verification details

The stated theorem has a complete proof in `RESULT.md`. To independently check finite instances, run `python3 check_idempotents.py`; it enumerates the defining coefficient-space equation without using the Fourier parametrization, and compares with the arithmetic divisor formula. It requires no third-party libraries. The direct checks in the standard invocation completed successfully:

| Coefficient field | Odd quandle order | Direct count | Arithmetic formula |
| --- | ---: | ---: | ---: |
| \(\mathbb F_2\) | 3 | 8 | 8 |
| \(\mathbb F_5\) | 3 | 8 | 8 |
| \(\mathbb F_2\) | 5 | 12 | 12 |
| \(\mathbb F_3\) | 5 | 12 | 12 |
| \(\mathbb F_2\) | 7 | 16 | 16 |
| \(\mathbb F_2\) | 9 | 80 | 80 |
| \(\mathbb F_2\) | 11 | 68 | 68 |
| \(\mathbb F_2\) | 15 | 768 | 768 |
| \(\mathbb F_4\) | 3 | 8 | 8 |
| \(\mathbb F_4\) | 5 | 12 | 12 |
| \(\mathbb F_4\) | 9 | 80 | 80 |

The \(\mathbb F_4\) cases explicitly use the relation \(u^2+u+1=0\) for a polynomial-field generator. The C program `check_prime_census.c` is a second exhaustive implementation over prime fields, also using the multiplication table only. Compile with `cc -O3 -std=c11 -o check_prime_census check_prime_census.c`; the following cases were enumerated successfully:

| Coefficient field | Odd quandle order | Direct count | Arithmetic formula |
| --- | ---: | ---: | ---: |
| \(\mathbb F_5\) | 9 | 80 | 80 |
| \(\mathbb F_3\) | 11 | 24 | 24 |
| \(\mathbb F_2\) | 17 | 648 | 648 |
| \(\mathbb F_2\) | 21 | 4096 | 4096 |

For each line, the C program's raw enumeration output is the number listed; the arithmetic numbers follow from the closed formula. The extra Python option `--extended` enables further prime-field enumeration. The code checks no instances where the coefficient characteristic divides the quandle size, and finite enumeration is not used in place of the general proof. Independent audit has not been performed.
