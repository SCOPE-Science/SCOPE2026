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

Reconstructed rational divided difference k(a,b) for q(s)=s+s^3/3+2s^5/25 on (0,0.01), with f=q(nu) and nu(x)=x/[100(1+x)]. Independently ran exact SymPy symbolic polynomial division: Q2=[d(t)d(t+u)-k(t,t+u)^2]/u² has 16 nonzero terms, constant 1/3, negative-monomial bound <1/12, hence 2x2 principal minors positive. Q3=det[k]/Vandermonde² has 44 rational terms all negative, constant -7/675, proving every distinct-node 3x3 L_q has one negative eigenvalue. Q3sq=det[k^2]/Vandermonde² has 681 terms, positive constant 22/675 and all 680 other coefficients negative; evaluation at (0.01,0.01,0.01)>0.03 certifies all ordered triples on the cube. The positive rank-one divided difference nu[x,y]=1/[100(1+x)(1+y)] gives diagonal congruences transferring both matrices to arbitrary positive x, with repeated-node PSD by continuity. Loewner finite-order criterion then gives 2-monotone, not 3-monotone; no claim about actual Frobenius radial convexity. The finding calls the scaling function u while the formula writes nu, but the proof explicitly defines nu and the intended single scaling x/[100(1+x)] is uniquely specified; treat as a notation inconsistency, not two mathematical maps.

## originality

PASS

The motivating 2026 paper derives the Loewner Hadamard-square necessary condition and states its three-dimensional determinant obstruction; its Remark 4.16 exhibits a 2-monotone function whose squared test also fails, not one passing the squared test globally while failing 3-monotonicity. Hiai–Sano study conditional definiteness of ordinary Loewner matrices and finite-order monotonicity, not this Schur-square separation. The all-triple rational witness therefore survives those comparisons, subject to unindexed kernel literature.

## value

PASS

The all-positive-three-node Schur-square Loewner positivity condition is a natural differential necessary test for the degree-three radial-convexity question. A single globally smooth analytic counterexample shows the full all-triple test does not force 3-monotonicity, beyond an isolated matrix or a sample triple. Exact rational certificates close the infinite-node assertion without extrapolation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
