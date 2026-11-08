---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-05.md",
      "INDEPENDENT_AUDIT_2026-11-05.json"
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

Read pinned RESULT.md and direct-matrix verify.py. For Hermitian rank-one X=r uu*, Y=s vv*, Frobenius commutator square divided by positive weighted norms reduces exactly to 2t²(1-t²)/[(u*Au)(v*Av)], t=|u*v|. The fixed-overlap Rayleigh minimum, explicitly reconstructed and cited from Pang Lemma 3.1, is ab(1-t²) for t<=delta=(b-a)/(a+b), and ((a+b)-(b-a)t)²/4 for t>delta. On first branch quotient rises; on second derivative is controlled by h(t)=(a+b)(1-2t²)+(b-a)t³, strictly decreasing and crossing from positive to negative exactly once. Positive rank-one projections from eigenvectors at eigenvalues a,b attain the unique maximum; endpoints t=0,1 and a=b handled. The identity ab*C/2=3t_*²-t_*⁴-1 yields monotonicity in b/a. Independent direct projector matrix calculations and 800-point overlap scans for 5 spectra corroborated constants, not an exhaustive proof. Strong restriction: Hermitian rank one, n>=2, A>0.

## originality

PASS

Best-of-knowledge PASS for the restricted Hermitian/PSD rank-one sharp coefficient; Pang arXiv:2610.29240 Lemma 3.1 and his unrestricted rank-one sharp theorem are acknowledged established results. Pang permits independently varying left and right generators of nonsymmetric rank-one matrices, so its sharp numerator and constants differ. For a=b, Hermitian C=1/(2a²) versus Pang unrestricted C=2/a², while as b/a grows the former is ~2/(ab) and unrestricted stays ~1/a² for fixed a. Prior Mayumi et al weighted Frobenius commutators and Fang–Cheng bounds concern broader matrix classes without an identified exact Hermitian specialization. Full Fang–Cheng publisher text not inspected; residual overlap risk.

## value

PASS

Positive rank-one Hermitian matrices are pure-state projections and an intrinsic subclass in quantum commutator estimates. Determining an exact, attained, dimension-independent sharp weighted commutator constant, its optimizing overlap and contrasting spectral anisotropy is a motivated nontrivial refinement, not a relabeling of the unrestricted bound.

The dated certificate retains the supplied scientific assessment, sources and limitations.
