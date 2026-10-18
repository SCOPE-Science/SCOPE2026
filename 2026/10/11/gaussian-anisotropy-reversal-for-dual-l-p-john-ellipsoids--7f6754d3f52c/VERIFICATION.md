---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-14.md",
      "INDEPENDENT_AUDIT_2026-10-14.json"
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

For n≥2, p>0 and a real symmetric traceless A, the ellipsoid radius obeys rho_K(u)=R(1+epsilon u^TAu)+O(epsilon²). With eta=R phi′(R)/phi(R), the conical measure has relative first variation (n+eta)q_A. In the exact Li–Liu–Huang characterization (1.10), the integrand variation is (2−p)q_B+(n+p+eta)q_A while the polar quadratic term varies as 2q_B. The normalized sphere moment n∫(x·u)²q_C(u)/|S|=(tr C+2q_C(x))/(n+2) yields trace(B)=0 and (n+p)B=(n+p+eta)A. The linearized ellipsoid equation has scalar eigenvalue p and traceless eigenvalue 2(n+p)/(n+2), both nonzero, so implicit differentiation is justified and global uniqueness identifies the branch. Gaussian phi′/phi=−R gives c_R=1−R²/(n+p). At the critical radius only the first derivative vanishes; no second-order theorem follows. This independently reconstructs all quantifiers, normalization and boundary restrictions; numerical stress tests are not the proof.

## originality

PASS

Independent source comparison found the defining weighted dual Lp John variational equation and existence/uniqueness, but not its explicit degree-two radial-density linearization. In the Lebesgue homogeneous case eta=0, the coefficient is 1 and affine covariance is consistent; a Gaussian radial weight introduces the genuinely new zero/sign reversal at R=√(n+p). Resultary returned the exact record being audited as its top match, which is self-reference, not independent prior art. Related unweighted and nondual John sources lack this same Gaussian dual anisotropy calculation. The assessment is best-of-knowledge, not proof of worldwide novelty.

## value

PASS

The derivative gives an exact n,p-dependent Gaussian radius where the weighted dual John ellipsoid map loses and then reverses anisotropic response. This is an interpretable stability/bifurcation threshold for a natural affine-geometric optimizer, rather than a mere numerical instance or a tautological normalization. The radial log-density formula also isolates which one-jet of the measure determines local anisotropy. The critical second-order dynamics remain open.

The dated certificate retains the supplied scientific assessment, sources and limitations.
