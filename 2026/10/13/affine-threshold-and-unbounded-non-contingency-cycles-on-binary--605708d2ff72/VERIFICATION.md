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

For r successor bits, the all-agree indicator is product(x_i)+product(1+x_i) over F2. At r=0 or1 it is constant1; at r>=2 cancellation of leading degree-r terms leaves every degree-(r-1) monomial with coefficient one, so algebraic degree exactly r-1. Thus coordinatewise Boolean affine iff every row has at most two successors. In that case Delta(x)=1+Bx where every B row has weight0 or2; B1=0 gives Delta^k(x)=1+B^k x for all k>=1. The first stable rank index a>=1 identifies Fitting decomposition ker B^a plus U=im B^a, with B|U invertible; equality of operator iterates is exactly B^{k+p'}=B^k iff k>=a and ord(B|U) divides p'. For n<=2 stable image dim<=1 implies p=1. At n3 the explicit 3x3 matrix yields period3. For each odd n>=3, B=I+P for a cyclic permutation has minimal polynomial (t+1)^n-1=t*g(t), g degree n-1 with g(0)=1; the order p of B|U obeys deg(g)<=p, hence p>=n-1. Independent direct matrix/valuation checker verified all 15002 at-most-two-successor frames n<=4, 237068 valuation cases, and odd-cycle periods n=3,5,7,9 equal 3,15,7,63. These finite tests corroborate but do not replace the universal ANF/Fitting/minimal-polynomial proofs.

## originality

PASS

The non-contingency/knowing-whether semantics are classical (Humberstone 2002, Fan–Wang–van Ditmarsch 2015) and the 2026 Sierra Miranda–Wang–Zenger primary paper gives proof theory for this very operator, not this binary-Boolean matrix dynamics in its inspected definitions and main argument. Fitting decomposition and elementary ANF are standard, credited ingredients. The new candidate identifies an exact sharp branching threshold, full uniform transient and period formula, and unbounded periodic family for nontransitive finite frames; those do not follow from ordinary semantics or finite transitive-frame stabilization. No direct equivalent surfaced in relevant published mathematical searches, subject to older Boolean-network modal-iteration material not inspected exhaustively.

## value

PASS

The natural iteration of the knowing-whether event operator acquires a sharp local algebraic-degree boundary and a complete global finite-time/cycle classification. The unbounded-period odd-cycle family shows that severe local branching restriction does not force convergence; this is a meaningful structural separation, not an arbitrary numerical frame example.

The dated certificate retains the supplied scientific assessment, sources and limitations.
