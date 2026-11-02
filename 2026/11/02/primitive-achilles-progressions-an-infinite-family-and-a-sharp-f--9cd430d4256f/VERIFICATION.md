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

# Reproducibility

Run `python3 verify.py` with Python 3 standard library only. The script recomputes: (i) the full coefficient identity \(27X(t)^2+343Z(t)^2=250Y(t)^2\), (ii) the strictly positive quartic-difference formula, (iii) the exact Sylvester resultant and its prime factorization, (iv) the Chinese-remainder modulus and residue, and (v) the valuations at \(11,17,19\) that combine with exact fixed-cube valuations to certify Achilles status. It checks seven integer parameters spread across the CRT progression as a reproducibility aid, not as a proof of the infinite statement.

For the sharp lower bound, the script factors **every** integer from \(2\) through \(57967\) by a smallest-prime-factor sieve and selects precisely those with all prime exponents at least \(2\) and gcd of exponents \(1\). It independently checks that all selected numbers arise as square-times-cube powerful numbers and exhaustively scans all ordered pairs \(a<b\) with \(c=2b-a\le57967\), imposing Achilles membership and primitivity. This complete finite search returns exactly one qualifying triple. It does not rely on any external prime tables or approximate number-theoretic tests.

The exact infinite argument is written in `RESULT.md`: resultant coprimality and CRT valuations apply to every integer in a nonempty unbounded congruence class, so the infinite part is a mathematical proof rather than a finite experiment. The finite exhaustive check depends only on exhaustive loops with proved factorization and pair coverage.

No independent audit has been performed; publication priority outside the inspected literature is not certified.
