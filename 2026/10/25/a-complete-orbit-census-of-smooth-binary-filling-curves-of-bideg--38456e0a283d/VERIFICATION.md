---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-29.md",
      "INDEPENDENT_AUDIT_2026-10-29.json"
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

Independent exhaustive F2 linear algebra reconstructed the nine evaluation functionals, rank 9, and 16-dimensional vanishing kernel of the 25 monomials, giving exactly 65535 nonzero filling equations. A distinct polynomial-generator basis via DX and DY reproduced this kernel. Rational-point Jacobian tests leave 3648 masks. Independently constructed all 72 ((PGL2(F2))² ⋊ C2) actions and obtained 54 rationally smooth orbits: 49×72,2×36,1×24,2×12. Fresh SymPy Groebner unit-ideal tests of (f,fx,fy) on all four affine charts of every orbit representative retained precisely 34 geometric-smooth orbits (31×72,2×36,1×24), totaling 2328 masks; these tests were independent of stored outputs. Smooth ample bidegree (4,4) divisors on P1×P1 cannot decompose into disjoint components, hence are integral; adjunction gives genus 9. Exact count is of embedded curves/equations, not abstract isomorphism classes.

## originality

PASS

For Complete F2 orbit census of smooth (4,4) filling curves on P1×P1: exact final statement and implication were compared against relevant published original mathematical statements and Resultary findings. The new exact census is not a formal restatement or specialization of either theorem; it uses full geometric smoothness and orbit-action arithmetic. Best-of-knowledge qualified by explicitly named risks.

## value

PASS

This exhausts a natural finite algebraic-geometry classification at the first symmetric bidegree immediately above the exceptional characteristic-two filling minimum: exact smooth count, rational automorphism orbit types and stabilizers are coherent invariants not implied by mere existence. The independent full-size enumeration makes it a useful reference for finite-field filling curves.

The dated certificate retains the supplied scientific assessment, sources and limitations.
