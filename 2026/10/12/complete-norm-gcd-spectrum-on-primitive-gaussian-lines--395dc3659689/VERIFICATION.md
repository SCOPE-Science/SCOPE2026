---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-17.md",
      "INDEPENDENT_AUDIT_2026-10-17.json"
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

For Gaussian-coprime alpha0=a+bi, delta=c+di with gcd(c,d)=1, F(n)=N(alpha0+n delta), A=N(delta), B=2(ac+bd), Delta=ad-bc and Q=odd(A^2+4Delta^2). If 2 divided two adjacent norms, 1+i would divide alpha0 and delta, impossible. For odd p, p|A and p|Delta would force the isotropic nonzero step modulo p and scalar-dependent starting vector, hence a common Gaussian prime, so gcd(A,Q)=1 and each p|Q splits (p=1 mod4). With D(n)=A(2n+1)+B and 4AF(n)=D(n)^2-2AD(n)+A^2+4Delta^2, the exact p-adic adjacent norm gcd exponent is min(v_p(Q),v_p(D(n))). Thus gcd(Fn,F(n+1))=gcd(Q,D(n)) for all integer n, including zeros. Since n->D(n) is bijective modulo each odd p^e dividing Q, Chinese remaindering gives every divisor and exact fiber weights (p-1)p^(e-t-1) for t<e, 1 for t=e; adjacent D(n+1)-D(n)=2A proves the triple gcd is 1. Separate self-written exact Gaussian arithmetic tests on 20,860 adjacent/triple index pairs gave zero mismatches, but are not the universal proof.

## originality

PASS

The Magness–Nugent–Robertson source gives primitive Gaussian line definitions and Gaussian-integer divisibility of terms; norm divisibility by a rational prime is a different question because split conjugate factors can alternate. A general resultant only restricts possible primes, not the equality with D(n), complete divisor set, and per-residue exact frequency. Published related SCOPE finite-resultant correction is a different two-variable density theorem and does not imply this one-dimensional complete local spectrum.

## value

PASS

Natural classification of a simple arithmetic observable (gcds of adjacent rational norms on primitive Gaussian lines), with exact periodic distribution and universal three-term coprimality. The distinction from coprimality of Gaussian integers is mathematically substantive (conjugate split primes), and the formula is directly reusable in divisibility questions.

The dated certificate retains the supplied scientific assessment, sources and limitations.
