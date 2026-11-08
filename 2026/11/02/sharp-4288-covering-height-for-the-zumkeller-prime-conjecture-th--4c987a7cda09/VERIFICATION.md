---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-05.md",
      "INDEPENDENT_AUDIT_2026-11-05.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

For the finite hard progression n=18k+3, 2<=k<=55,555,555, the embedded C++ `verify.cpp` enumerates all even Zumkeller z<=4288 with descending exact subset-sum DP on complete proper-divisor lists (972 z), constructs complete odd prime Eratosthenes bit sieve <=10^9, and scans all 55,555,554 n, stopping at smallest successful even offset each time. I independently wrote a different C++ sieve/subset-sum enumeration and executed the ENTIRE finite domain, not a sample: checked=55,555,554, uncovered=0, even_z=972, max minimal even offset=4288, unique n=679570815, n-z=679566527 sieve-prime; partial H(X) 464,928,2368,2368 for 10^5 through 10^8. The witness z=4288=64*67 is Zumkeller by sigma(z)=8636 and balanced subset 4288+2+4+8+16=4318. An odd Zumkeller offset for odd n leaves even prime 2 and equals n-2, which cannot improve h(n*) or tie max elsewhere below 4288. Somu–Kukla–Tran Proposition 4.12 covers other congruence classes, yielding full odd 9..10^9 except21. Scope strictly finite; no unbounded conjecture proven.

## originality

PASS

Somu–Kukla–Tran 2023 primary Proposition 4.12 handles remaining odd congruence classes and Conjecture 4.20 poses 18k+3, with initial k<=1000 checked in the source; the submitted finite computation extends this to k=55,555,555 and supplies the distinct sharp H(10^9) and unique extremizer. OEIS A368082 lists representable sums but not this maximum/minimal-addend profile; Li 2026 exceptional-set density is asymptotic and does not imply exact finite height. Resultary semantic search surfaced unitary Zumkeller classifications but no hard-progression coverage. Historical unpublished large computations remain possible.

## value

PASS

This is a natural finite cutoff in an explicitly open residue-class arithmetic representation problem. The covering height H(X) is a meaningful exact natural invariant, not an arbitrary isolated evaluation; it records the worst least Zumkeller addend, unique extremizer and reproducible proof by exhaustive integers. One-billion finite milestone is not a theoretical boundary; finite computational result still has independent value for further research.

The dated certificate retains the supplied scientific assessment, sources and limitations.
