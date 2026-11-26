---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

The repaired result holds. Generate uniform X0 by choosing an independent uniform branch J and uniform Y, and write X0=(J-1/2+epsilon_J(Y-1/2))/m; this gives the signed conditional mean S(Y-1/2)/m^2. In the cell representation Y-1/2=(a_I+U-1/2)/N and X1-1/2=(a_pi(I)+U-1/2)/N with I and U independent, giving the Spearman term plus the common within-cell variance. Every future observable is a function of Y, so S=0 suffices; identity shuffle at lag one proves necessity for the stated universal quantifiers. Uniform rank sampling gives Var(Q)=(sum a_i^2)^2/(N-1), and reversal negates Q, not the uncentered covariance. The variance-normalized array is centered in rows and columns and uniformly O(N^-1/2), so Chen–Fang (1.5) gives the asserted rate for S nonzero. The frozen proof's line 89 incorrectly says the reversal magnitude vanishes for N=2. For m=N=2 with both signs positive the exact identity and reversal covariances are 1/24 and -1/48. Replacing that aside with the exact magnitude ratio 1-2/N^2 preserves the extrema, their strict comparison, and every Finding statement. Replayed the affected claim by the affine formula and strict rearrangement, not the supplied finite checker.

## originality

PASS

The supported distinct claim is the exact signed dynamical Spearman reduction and balanced universal orthogonality. The map family, classical rank-law ingredients and combinatorial CLT are existing work. The repair changes only a mistaken numerical aside in the proof and does not broaden the originality claim.

## value

PASS

On a natural established family that is generally analyzed via mixing, the result identifies a finite-size covariance offset that a ranks-only guess misses and supplies an exact test for persistent linear orthogonality uniformly across shuffles. Those are reusable diagnostic distinctions, beyond the routine moment/CLT corollaries.

The dated certificate retains the supplied scientific assessment, sources and limitations.
