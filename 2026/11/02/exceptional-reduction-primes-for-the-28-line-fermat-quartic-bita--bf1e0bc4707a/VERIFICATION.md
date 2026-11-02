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

# Reproducing the exact arithmetic checks

Execute `python3 verify_reduction.py` with Python 3 and no third-party packages. The program first builds the 28 coefficient vectors in the integer ring \(\mathbb Z[Z]/(Z^4+1)\), calculates all 3276 triple determinants and their multiplication-matrix norms using exact division in Bareiss elimination, and compares the entire 13-value norm histogram with recorded expected counts. These norms contain no odd prime factors outside \(\{3,5,17\}\), which is the necessary all-primes part of the proof.

Next the verifier constructs the reduced line arrangement and intersects every pair in finite splitting fields, checks each intersection against every line, and compares the resulting multiplicity profile with the claimed counts: \(63\) quadruple points in characteristic three; \(240\) double, \(16\) triple, \(15\) quadruple points in characteristic five; \(288\) double and \(15\) quadruple points in characteristic seven; \(144\) double, \(48\) triple, \(15\) quadruple points in characteristic seventeen. It asserts that the new characteristic-five triples consist only of \(B\)-lines and the characteristic-seventeen triples contain exactly two \(H\)-lines and one \(B\)-line. It checks the characteristic-three fourfold-intersection category split and pair sums.

The expected completion marker is `FERMAT_28_BITANGENTS_ARITHMETIC_INCIDENCE_EXACT_OK`. The argument for all odd primes and the geometric interpretations are explained in `RESULT.md`. Exhaustive finite-field computations establish exactly the indicated finite-field cases but are not used by themselves as an infinite-prime proof. A run success marker alone is not a substitute for inspecting the code or proof. Mathematical validation beyond the self-review has not been performed.
