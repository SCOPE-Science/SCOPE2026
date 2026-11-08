---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-03.md",
      "INDEPENDENT_AUDIT_2026-11-03.json"
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

PASS: The full zero-matrix Jacobian and equilibrium conditions at any point with nonzero coordinates reduce, by diagonal scaling and translation, each degree-two scalar field to a quadratic in u=x-1,v=y-1. Any 4 of the 6 source exponent columns (1,i,j) have rank 3, so both components share a one-dimensional kernel and are scalar multiples of one quadratic. Enumerating all 15 absent-monomial pairs, each generator has nonnegative discriminant and a real linear factor; therefore an entire real equilibrium line passes through the point, prohibiting isolation. At least five distinct active reactant monomials and hence >=5 channels are necessary. Direct channel summation in the cited five-channel witness gives dx=(x-y)^2,dy=(y-1)^2, with unique equilibrium (1,1) and zero Jacobian. Independently derived exact SymPy 15-case rank and discriminant checks passed; exhaustive structural cases, not all rates or networks. Hypotheses include degree <=2 reactants and full zero Jacobian; products unrestricted.

## originality

PASS

The five-channel witness already appears in Yeung and Erban; the surviving candidate contribution is the universal four-support no-isolated-double-zero obstruction. Unlike generic bifurcation and few-source partition theorems, this covers all quadratic vector fields supported on four of six monomials. Search gaps are not evidence of guaranteed priority.

## value

PASS

PASS: The minimal reaction-channel complexity of an isolated positive zero-matrix degeneracy is a motivated, exactly attained extremal invariant in quadratic reaction kinetics. Four-source line obstruction gives a structural nonisolatedness result valid for any coefficient signs and any finite products; it is not a restatement of an example or mere routine linearization. The five-channel construction itself is prior and credited.

The dated certificate retains the supplied scientific assessment, sources and limitations.
