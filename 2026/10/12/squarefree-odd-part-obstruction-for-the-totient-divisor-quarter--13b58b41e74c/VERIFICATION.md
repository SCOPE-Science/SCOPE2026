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

# Exact arithmetic verification and its limits

Run the standalone standard-library-only program `python verify.py` in the same directory as `RESULT.md`. The supplied `verification_output.txt` is the resulting output from a fresh execution, and its first line is `VERIFY_OK`.

The symbolic proof needs only the multiplicative identities for \(\varphi\) and \(\tau\), parity of \(P-2Q\), elementary inequalities, and the factorization \(233\) as a prime. The program performs the following finite independent cross-checks: admissible valuation pairs for prime-support parameters \(r=3,4,5,6\); exact rational comparisons of the five relevant prime-product upper bounds; the positive gaps for the prefixes \((3,5,7)\), \((3,5,11)\), \((3,5,13)\); the numerical mismatch of the printed 2023 proposed example; and separately sieved \(\varphi\) and \(\tau\) values for every multiple of \(4\) through \(100000\) with squarefree odd part.

The prime-product bounds apply to arbitrarily large primes because \(p/(p-1)\) strictly decreases with \(p\). The argument for all \(k\) above the finite valuation cases is given symbolically by growth of powers of \(2\) relative to \(k+3\), not by stopping enumeration. These proofs and the case analysis in `RESULT.md` establish the infinite exclusion. Finite verification does not establish a global claim by itself. No six-odd-prime solution, independent external review, or complete solution of the unrestricted Diophantine equation is certified.
