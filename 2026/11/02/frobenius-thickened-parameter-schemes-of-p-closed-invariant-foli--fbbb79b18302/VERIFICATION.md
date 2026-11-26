---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

The differential of relative Frobenius is zero, so the Lie algebra of its kernel is all of Lie A, with the same restricted operation. The split height-one factors have generators with p-power respectively itself and zero. Semilinearity in the abelian Lie algebra gives (X,Y)↦(X^p,0); wedging with the tautological line is the correct zero-scheme condition, locally equivalent to vanishing in the quotient bundle. For a line of invariant vector fields, closure for its invariant generator implies closure for all local multiples by the characteristic-p derivation identity (fD)^p=f^pD^p+(fD)^{p−1}(f)D. On each Y_a chart the ideal is exactly (x_i^p); on each X_i chart it is (y_a,x_j^p−x_j). The latter consists of reduced F_p-coordinate points because derivative −1 is a unit, and the two kinds of charts have disjoint support on the zero scheme. This includes pure nilpotent or pure multiplicative split kernels and p=2. The thick component's graded ring is free over k[Y_1,…,Y_s] on X^e, 0≤e_i<p, with degree shifts |e|. Thus the projective Hilbert polynomial is the sum of the shifted projective-space polynomials and the contribution N_r of the disjoint reduced component. At r=0 the empty multi-index contributes one term, binomial(m+s−1,s−1), not the constant 1 unless s=1. Generic length p^r and tangent dimension g−1 follow directly from the local truncated ring; the asserted lengths and degree follow. No extension to arbitrary kernels with the same p-rank is used. The supplied example checker was inspected as finite corroboration, not executed or relied on for the theorem.

## originality

PASS

Best-of-knowledge credit is limited to the explicit embedded zero scheme for the split invariant-line problem and its infinitesimal and Hilbert data. The geometric-point interpretation, split restricted-p normal form and low-dimensional reduced counts are established inputs. The inspected strongest sources do not state the mixed scheme or its scheme-theoretic invariants.

## value

PASS

The natural zero scheme of a restricted-Lie closure condition has full ambient tangent spaces and multiplicity p^r along an entire linear support, despite the reduced ordinary points and known geometric-point counts. The classification supplies exact infinitesimal and Hilbert data that the reduced classification loses, for all split types rather than a chosen small example.

The dated certificate retains the supplied scientific assessment, sources and limitations.
