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

# Verification and reproducibility

Run `python3 verify.py` from the directory containing the embedded public files. No third-party modules, web access, or other data files are required.

The standalone program factors integers exactly, computes \(T(n)=\psi(n)-n\) independently from prime factors, constructs the finite prime-support-word classifier, then directly enumerates all positive two-step periodic points with initial value from \(2\) through \(25000\). Each observed ordered support word is independently counted by direct enumeration and by the classifier's canonical-generator formula; all comparisons must agree. It additionally checks the known fixed support \(\{2,3\}\), rejects an impossible singleton word, verifies both orientations of the two-cycle \((1330,1550)\), checks the count through \(100000\) for that fiber, and directly checks \(25\) higher-exponent scalings of the two-cycle.

The expected output is the accompanying `verify_output.txt` obtained from the actual standard-library replay. All arithmetic verification uses integers; logarithms occur only in the written theorem's asymptotic formula and not in the exact finite computations.

The general mathematical assertion for arbitrary length and arbitrary primes follows from the proved valuation-shift equivalence and lattice-volume argument. The exhaustive finite search is not a proof of an infinite classification, and the program does not certify originality or future source coverage. The parameterized result does not classify all possible support words without their being prescribed, nor does it sum its per-fiber counting estimates over all words.
