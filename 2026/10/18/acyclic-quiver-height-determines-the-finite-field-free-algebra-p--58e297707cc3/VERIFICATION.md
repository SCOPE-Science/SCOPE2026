---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-25.md",
      "INDEPENDENT_AUDIT_2026-10-25.json"
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

For any finite nonempty acyclic directed multiquiver Q and finite field F_q, the relatively free unital associative F_q-algebra on n generators is the algebra of polynomial maps A^n→A for A=F_qQ. Each output path coefficient of a word factors into r≤h−1 nontrivial paths with diagonal vertex blocks, hence a polynomially many (≤constant n^r) union of q^{n(r+1)}-dimensional spaces of scalar coordinate functions; this gives d_n≤C_Q n^{h−1}q^{hn}. Along a longest path, finite-field coordinate indicators Δ_b=∏(1−(Xi−bi)^(q−1)) and adjacent commutators [Xi,Xn] with Xn=sum path arrows isolate distinct diagonal-vector tuples with unequal adjacent vectors. Exactly q^{n−1}(q^{n−1}−1)^{h−1} such isolated evaluations give independent polynomial functions, proving the lower bound. n-th roots yield d_n^(1/n)→q^h and (log|F_n|)^(1/n)→q^h. h=1 is scalar polynomial functions, d_n=q^n, including disconnected isolated vertices. Independent GF(2) UT2(F2) function-algebra closure gave 24-dimensional n=2 free object on 64 input pairs, and 36 binary 3-chain separator supports; finite checks supplement universal proof.

## originality

PASS

The concept of finite-algebra potential originates in Olshanskii (2026) who focuses on prime/maximality properties; quiver path algebras with radical and arbitrary directed branching are not prime. Existing finite-field upper-triangular PI studies may overlap the chain case, and graded linear bases might imply partial growth results; no inspected full theorem dominates every acyclic multiquiver and gives the path-height potential.

## value

PASS

This evaluates a natural growth invariant uniformly for a broad nonprime family of finite-dimensional associative algebras: only the longest directed path matters, even under changes of branching, vertex count away from longest path, or parallel arrows. The contrast between algebra size and potential height is a concrete structural classification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
