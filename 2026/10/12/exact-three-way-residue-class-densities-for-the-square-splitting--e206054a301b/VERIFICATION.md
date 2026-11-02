---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-27.md",
      "INDEPENDENT_AUDIT_2026-10-27.json"
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

For f(p^j)=-1,-1,+1,0 (j=1,2,3,>=4), the Euler polynomial (1-z)(1-z^2) gives f(n)=sum_{d^2|n}mu(d)mu(n/d^2), and f^2=1_{4th-power-free}=sum_{d^4|n}mu(d). For any reduced b mod fixed q, PNT-AP cancels mu in each fixed inner class, while d>T contributes O(x/T). Every nonreduced progression restricted to f!=0 splits into finitely many factors supported at primes dividing q (exponents <=3), reducing to reduced classes; hence sum f=o_q(x). For support, CRT gives exactly one class modulo qd^4/gcd(q,d^4), if gcd(q,d^4)|a, with O(1) counting error. Summing d<=x^1/4 and estimating the tail using gcd<=q yields O_q(x^1/4). The Euler factors produce the asserted kappa; kappa=0 iff p^4|gcd(q,a), otherwise positive. Addition/subtraction proves the three densities. q=1, arbitrary a, nonunits, and e>=4 all satisfy the conditions. The independent finite test directly recomputed the convolution and 339 exact support progression counts up to 120000, without being used as an infinite proof.

## originality

PASS

The same-function source determines the prime-power values and global fourth-power-free support, while the submitted complete all-fixed-moduli three-way density involves an additional uniform-in-residue signed-mean argument and local CRT product. No identified prior statement mathematically implies the full formula directly; this best-of-knowledge conclusion does not treat the absence of a search hit as proof of priority.

## value

PASS

The three-way distribution is a natural and complete invariant for the new square-splitting Möbius function, specifically motivated by the identical source paper’s distribution questions. It determines all fixed progressions, including noncoprime classes, proves exact equal positive/negative densities when not arithmetically forbidden, gives the full Euler product and an if-and-only-if fourth-power obstruction, with quantitative support error. It is concise and uses standard inputs, but is not a single textbook identity or an arbitrary parameter slice; the exact local spectrum is mathematically meaningful.

The dated certificate retains the supplied scientific assessment, sources and limitations.
