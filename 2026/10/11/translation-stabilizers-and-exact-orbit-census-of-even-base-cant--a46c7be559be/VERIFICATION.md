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

# Reproducible checks and their limits

With Python 3, run `python checker.py` in the directory containing the file. It uses only the standard library and returns twelve `EXACT_OK` reports. It constructs the finite spectral sets by parity-digit recursion, tests every pair's Fourier-zero condition, obtains stabilizers by translating the sets, and compares the distinct translation orbit count with the theorem. For eleven of the twelve parameter pairs, it additionally checks **all** subsets of the relevant cardinality to verify completeness independently of the digit-tree generator. The non-brute case is \((b,n)=(4,3)\); there, the generator makes \(16384\) spectra and independently computes \(256\) translation orbits.

With SymPy installed, run `python cyclotomic_check.py`. This forms cyclotomic-polynomial remainders in exact integer polynomial arithmetic and tests the Fourier-zero criterion for each frequency in the listed six parameter pairs. Expected last line: `EXACT_CYCLOTOMIC_OK comparisons=194 fields=6`.

Representative reports from the standard-library checker are `EXACT_OK b=6 n=2 spectra=729 orbits=23 stabilizer_counts={1: 648, 2: 72, 4: 9} brute=True` and `EXACT_OK b=4 n=3 spectra=16384 orbits=256 stabilizer_counts={1: 16384} brute=False`.

The proof's all-base and all-level quantifiers are justified by the finite-ring Fourier factorization, subgroup structure and exact combinatorial argument in `RESULT.md`, **not** by a finite enumeration. The code does not establish uniqueness against the literature or certify any infinite fractal-measure theorem.
