---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-07.md",
      "INDEPENDENT_AUDIT_2026-11-07.json"
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

For smooth connected projective Y/C, any line bundle L and m>=2, the split nilpotent thickening X_m=Spec_Y(⊕_{0<=j<m}L^-j) has global positive fiber scaling. Locally a semi-free resolution R[t,η], |η|=-1, ∂η=t^m admits Euler derivation E(t)=t,E(η)=mη commuting with ∂. Its contraction is a homotopy on the E1 horizontal differential: d1 i_E+i_E d1=w on each positive integer weight w, invertible over C, so all positive-weight classes die by E2. The weight-zero summand is precisely the smooth reduction Y and degenerates already at E1 by smooth-projective Hodge theory. Weight grading persists through gluing, derived global sections and Hodge completion; no higher differentials survive, giving E2^(p,q)=H^q(Y,Omega_Y^p). This is a filtered statement rather than a consequence of the unfiltered cohomology comparison. A multiple projective line has only (0,0) and (1,1) nonzero at E2. Independent exact rational derivative checks for truncations m=2..17 corroborate the local d1 isomorphism; they are not a global spectral sequence proof.

## originality

PASS

PASS best-of-knowledge for the full E2 page of every split line-bundle thickening in all orders and the projective nonreduced examples. The 2026-11-04 v2 of He–Wang explicitly restricts its main theorem to integral projective curves, whereas X_m is nonreduced. Bhatt establishes the Hodge-completed comparison after forgetting the filtration and cannot alone give page-by-page degeneration. Euler–Cartan contraction itself is classical and may be present in general equivariant derived de Rham literature, an important residual risk.

## value

PASS

The theorem computes an entire filtered spectral-sequence page for a natural infinite geometric family of projective nonreduced local complete intersections, distinguishing a large extra derived E1 page from its cancelled E2. It supplies a motivated counterexample to the naive expectation that nilpotent structure necessarily forces higher differentials, while carefully excluding nonsplit and characteristic-p analogues.

The dated certificate retains the supplied scientific assessment, sources and limitations.
