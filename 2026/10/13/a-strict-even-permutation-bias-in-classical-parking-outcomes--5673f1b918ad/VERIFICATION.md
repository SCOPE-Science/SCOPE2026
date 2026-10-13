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

# Verification record

The proof establishes the claimed infinite sequence by an exact final-car decomposition, a Gaussian-binomial identity at \(q=-1\), and coefficientwise induction on formal power series. It neither presupposes analytic convergence of those series nor infers infinitely many cases from a finite computation.

Run `python3 verify.py` from the supplied file collection using any current Python 3 installation; the script imports only the standard library. Direct simulation of the underlying preference lists covers every input through \(n=7\), with explicit successful-parking and sign checks. An independent sum over weighted outcome permutations uses Pinsky's formula through \(n=8\). Separate integer tests cover Gaussian-binomial alternating subset sums through ambient size \(12\), both parity-separated recurrences through \(m=14\), and the formal differential identity through \(m=14\). On the reviewed package, the checker printed `PASS: 209 exact assertions`.

The successful finite replay supports implementation integrity only; it does not independently establish priority, external certification, or the theorem's infinite extent. A final independent scientific audit has not been performed.
