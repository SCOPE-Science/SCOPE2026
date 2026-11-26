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

Checked the phases and minimality in RESULT.md:29–84 using the stated ZX=iY convention. For N=2m, the pair sum on a weight-k state is 2(m-k)^2-m, so the diagonal two-phase form follows from k parity. Its square and the square of its B conjugate multiply to (-1)^m P_zP_x=P_y; B^4=I. The projective period divides 8 but does not divide 4. For N=2m+1, each pair gate is e^(-i pi/4) S_j S_k CZ_jk; collecting site powers gives the stated e^(i pi m/4)D including the constant sign in q. The radical is the all-ones line, on which q is translation invariant. The zero-frequency Gauss sum is the real part of sqrt(2)e^(-i pi/4)(1+i(-1)^m)^(2m+1) times (-1)^(m(m+1)/2), which equals +2^(m+1) for both parities of m. For t even, shifting by t gives the Walsh phase q(t)+q(0); for t odd, complement pairing gives zero. In (DF)^3 the remaining sum over z with p(z)=p(x) has exponent (w+x)·z+p(x), and hence is supported at w=x and w=x+1, with the respective coefficients (-1)^p(x)/sqrt(2) and +1/sqrt(2). With K=P_xP_z, this gives (DF)^6=I and U^6=i^(3m)K^3=i^(m+1)P_y. The phase-free Pauli map has order 2 on the all-ones sector and 3 on the nonzero even-parity sector, so odd sizes have no scalar power below 12; the sign of U^12 then distinguishes ordinary orders 12 and 24. All identities are on the full Hilbert space and N=2,3 are included. The integer Walsh checker check.py and the finite dense-matrix claims in VERIFICATION.md:21–25 were inspected as corroboration only; no uploaded code was run.

## originality

PASS

The supported distinction is the all-N full-Hilbert-space Pauli power identity with exact scalar and minimal ordinary/projective orders for this drive. Same-drive periodicity and finite-size symmetric-sector results are prior. The inspected follow-up uses broad periodicity language but describes analytic eigensystems only through N=12 and treats the larger cases numerically; its reduction and conclusions inspected do not provide the exact full-space statement.

## value

PASS

This is a motivated exact recurrence problem for a published drive. An all-size bound with the shortest true and projective orders and the intervening Pauli operation is useful for recurrence of arbitrary states and operators without symmetric-sector diagonalization. The distinction between scalar and ordinary orders has real mathematical content; the result does not infer quantum integrability or diagnostic-specific periods.

The dated certificate retains the supplied scientific assessment, sources and limitations.
