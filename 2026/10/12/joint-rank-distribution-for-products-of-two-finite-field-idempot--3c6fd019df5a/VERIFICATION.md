---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-16.md",
      "INDEPENDENT_AUDIT_2026-10-16.json"
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

Reconstructed parameter h=dim(W∩U) for W=imF and U=imE with E projection U⊕K. For fixed rank-r E, there are [n r]_q q^{r(n-r)} possibilities. rank(EF)=p enforces dim(W∩K)=s-p. First choose A=W∩U and B=W∩K, then W/(A⊕B) is graph of a rank c=p-h isomorphism between c-subspaces in U/A,K/B: factor [r h]_q[n-r s-p]_q[r-h c]_q[n-r-s+p c]_q GL_q(c). For fixed W, F kernels are complements L to W, parameterized by φ:V/W→W; rank(FE)=t iff induced φ on π(U)→W/A has rank t-h, contributing R_q(s-h,r-h;t-h) q^{h(r-h)+s(n-s-r+h)}. All dimension constraints are stated and ensure nonnegative exponents. Independent Python brute force enumerated all idempotents and both ordered product ranks for (q,n)=(2,2),(3,2),(2,3): all 64,196,3364 ordered pairs and every possible rank quadruple matched the formula. Swapping E,F gives (r,s,p,t)↔(s,r,t,p); independent summation over all p,t gives product of idempotent rank counts.

## originality

PASS

The known fact that idempotents correspond to complementary image/kernel subspaces and the individual rank enumeration are credited. Actual primary literature found linear-combination rank and semigroup idempotent counts, not a full four-rank joint distribution of two ordered noncommuting projections over each finite field. The coupled (rank EF,rank FE) distribution is not determined by either marginal or by a single idempotent count.

## value

PASS

The paired product-rank distribution is an exact natural invariant for two noncommuting projections in a finite vector space; it resolves more than the classical one-idempotent count, distinguishes EF from FE, and supplies a uniform finite-field formula with meaningful limiting and special-stratum uses. It is a substantive finite-geometric enumeration, not a trivial parameter rename.

The dated certificate retains the supplied scientific assessment, sources and limitations.
