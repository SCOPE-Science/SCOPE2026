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
# Verification

The mathematical proof uses exact Fourier row elimination and a factorized two-by-two determinant over the full range of odd primes. The distinct residue differences in the two parity blocks are nonzero; consequently all singular four-by-four partners have rank exactly three. For homogeneous and three-versus-one blocks, the required three-by-three Fourier minors over a prime field are nonsingular because, after multiplying columns by a nonzero phase, their three rows become powers zero, one, and two evaluated at three distinct nonzero roots of unity. The count follows from \((p-1)/2\) distinct unordered two-element frequency pairs for each sum modulo \(p\).

Replay `python3 checker.py` from a folder containing the supplied standalone script. It uses no third-party dependencies, floating-point numbers, imported datasets, or external services. The determinant expansion is reduced to length-\(p\) integer coefficient vectors; a polynomial of degree at most \(p-1\) vanishes at a primitive \(p\)-th root of unity if and only if every coefficient is equal. Thus the checker performs exact singularity testing, not approximate rank thresholding.

An exhaustive comparison of all four-frequency subsets for \(p=3,5,7,11,13\) returns the singular totals \(3,30,133,935,1898\), respectively; the exact counting formula agrees in every case. For the same primes, exact row/column phase-ratio tests show that exactly \(3,20,63,275,468\) singular submatrices, respectively, have no proportional row or column pair, confirming the balanced-resonance count. The program ends with `CHECK_PASS`. This finite check supplements, rather than establishes, the infinite-prime theorem.

The result does not classify noncentered four-point apertures or nonsingular matrix condition numbers. Historical equivalences under alternate terminology remain possible. Independent audit has not been performed.
