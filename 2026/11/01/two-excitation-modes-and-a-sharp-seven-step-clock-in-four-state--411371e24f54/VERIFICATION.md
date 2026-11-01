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

# Reproducibility and exact checks

The archive contains source programs and the corresponding saved standard output. The Python finite quotient checks **every** initial capped class-population signature (6561 cases); the C++ program separately checks labelled configurations with a different transition representation. All scripts are ordinary proof/checker programs, not external certification.

From a directory containing the embedded files, execute:

```sh
python3 cap_certificate.py cap_certificate_replay.csv > cap_certificate_replay.out
cmp cap_certificate.csv cap_certificate_replay.csv
python3 basin_formula_check.py cap_certificate.csv > basin_formula_replay.out
c++ -std=c++17 -O2 -Wall -Wextra direct_check.cpp -o direct_check
./direct_check > direct_check_replay.out
cmp direct_check.out direct_check_replay.out
cmp basin_formula_check.out basin_formula_replay.out
```

`cap_certificate.py` checks the exact threshold at two representatives for all eight color classes through eleven time steps and asserts the equality of steps seven and eleven. It checks periodic-type classification, including absence of primitive two-cycles, first-entry sharpness in all 49 representative shore-size pairs, and feasibility stabilization beyond eight vertices. Its CSV is a complete 6561-row certificate, with each row's capped class sizes, first-periodic-entry time, and eventual primitive period. `basin_formula_check.py` expands the labelled multinomial weights implied by the same coefficient formula at five shore-size pairs and cross-checks direct histograms.

`direct_check.cpp` exhaustively iterates 4,657,408 labelled states over ten shore-size pairs (largest individual space size 1,048,576) and verifies the equality \(F^{11}=F^7\), the fixed count one, the periodic count \(1+2S(a)S(b)+T(a)T(b)\), and all first-entry histograms. It does **not** claim an exhaustive search over all graph sizes. The proof of the all-size statements rests on the population-capping lemma and the exhaustive finite quotient.

The exact first-entry witness on \(K_{7,8}\) has shore strings `0011233` and `00112233`; its trajectory first satisfies \(F^{t+4}=F^t\) at \(t=7\). The witnesses and capped pattern classification are established by the exact quotient program. All input sizes in the theorem are finite integers, \(a,b\ge2\); signedness, floating-point approximation and random sampling play no part in these computations.

The historical literature comparison does not constitute a proof of uniqueness or precedence. Independent scientific audit has not been performed.
