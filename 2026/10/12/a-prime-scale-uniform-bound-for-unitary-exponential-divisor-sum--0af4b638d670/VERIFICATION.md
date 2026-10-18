---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-15.md",
      "INDEPENDENT_AUDIT_2026-10-15.json"
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

Multiplicativity follows from the two correct prime-power formulas. For squarefree s, R(s)=∏_{p|s}(p+1)/p is injective: after cancelling common primes, the greatest p>=5 of disjoint supports would have to divide q+1 for some q<=p prime, forcing even q=p-1; tiny supports {2,3} are directly checked. Every n=d*s*m with d powerful small-prime repeated powers, s squarefree small-prime exponent-one part, and m y-rough, pairwise coprime; at most one s for fixed (d,m,c). The published Fan–Pomerance inequality Φ(X,y)<(3/5)X/log y for 3<=y<=sqrt X applies when d<=x^(2 epsilon) with y=x^(1/2-epsilon). The unique powerful a²b³ (b squarefree) representation yields A=ζ2ζ3/ζ6 and tail sum O(z^-1/2). Remaining d give O(x^(1-epsilon)). First x→infty then epsilon→0 proves uniform limsup <=(6/5)A, independently evaluated as 2.3323157241849110461. Numerical checks are non-proofs of the infinite bound.

## originality

PASS

Trudgian states the σ*=σ^(e) equality problem and finite witnesses, but not a quantified unrestricted level-set upper bound. The closest published Resultary records establish a strict-comparison lower density and a bounded-exponent p^a q classification, neither implying the uniform maximum fiber O(x/log x). Fan–Pomerance supplies a general rough-number ingredient but not this theorem; a more general concentration theorem remains a named residual risk.

## value

PASS

The equality σ*(n)=σ^(e)(n) is an explicit open question of Trudgian, and a uniform bound for every ratio value is a natural strengthening. The result shows every fiber, including the unknown infinitude equality fiber, is at most prime-scale O(x/log x), far stronger than finite example tables or an unquantified zero-density result. Squarefree injectivity and sieve decomposition are a substantive arithmetic mechanism.

The dated certificate retains the supplied scientific assessment, sources and limitations.
