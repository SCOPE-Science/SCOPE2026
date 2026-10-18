---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-18.md",
      "INDEPENDENT_AUDIT_2026-10-18.json"
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

Set G=sqrt(m) S U and h=sqrt(m) S z. Conditional Gaussian orthogonal projection yields Z=m*rho²~chi²_d independent of least-squares coefficient c. Schur complement/inverse-Wishart gives c in distribution as v/sqrt(Y), v standard k-Gaussian and Y~chi²_(d+1), independently of Z. Residual-only selection chooses Zmax independent of selected c. Therefore ||q||²=m(1+X/Y)/Zmax and inverse-moment integrability at 0 yields exactly p<d+1 and p<Ld; equal endpoints diverge logarithmically. The scalar ordering Zselected<=Zmax gives simultaneous optimality; X/(X+Y) gives Beta angle. For d=2,L=2 an exponential maximum inverse moment integrates to log2. Direct theoretical derivation, not the finite checker, establishes infinite-moment boundaries.

## originality

PASS

Classical multivariate Student and chi-square regression furnish the factors and are not novel. Balabanov–Grigori RGS uses sketched LS residual orthogonalization but does not analyze selecting among independent sketches by largest residual or give the combined min(d+1,Ld) moment cutoff, Beta angular invariance and saturation. Reorthogonalization methods change the algorithm, not residual-only selection. Resultary searches for Gaussian residual-selection moment thresholds did not locate an equivalent classification. Classical Wishart t-coefficient and chi-square residual distributions imply factors, but do not state independent multi-residual selection saturation or angular invariance for this algorithm without their joint proof.

## value

PASS

Selection among multiple sketched Gram–Schmidt candidates is a natural defense against extreme residual normalization. The exact result quantifies the maximum possible rescue using that observable alone, and proves a separate invariant angular defect that cannot be screened away. This informs motivated randomized orthogonalization design despite being a one-step Gaussian model.

The dated certificate retains the supplied scientific assessment, sources and limitations.
