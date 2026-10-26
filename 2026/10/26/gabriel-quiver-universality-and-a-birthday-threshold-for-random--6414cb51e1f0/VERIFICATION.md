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

# Verification of the stated theorem

The proof is given in RESULT.md. Its nonstandard point is the loss of one sample direction in each off-diagonal bimodule block after changing the semisimple complement. That change is conjugation by a unit of the form \(1+z\), possible because the diagonal quotient is separable and the radical square is zero. For each pair of distinct vertex labels, the difference of their \(r\)-coordinate tuples is nonzero, leaving precisely \(r-1\) effective independent uniform vectors in that arrow block. Loop blocks retain \(r\) effective vectors. Every factor is the probability that a random matrix has full row rank.

Reproducible finite check: run `python3 verify_generation.py` with Python 3. The program enumerates all tuples of elements in specified truncated path algebras, closes the unital linear span under multiplication, and compares the resulting exact rational proportion to the quiver formula. Thirteen small cases over prime fields passed. Truncating path length from two to three for the path with two arrows leaves the observed probability unchanged, as predicted. Computations cover no nonprime finite fields and cannot by themselves prove all dimensions.

The asymptotic verification is analytic: the probability of distinct \(q^r\)-valued vertex labels is a falling factorial, whose logarithm is \(-v(v-1)/(2q^r)+O(v^3/q^{2r})\). Under the given sparsity assumptions, a union bound for all radical ranks is \(O(vq^{M-r})\to0\) when \(r=2k+t\) and \(v=q^k\). No external independent audit was undertaken.
