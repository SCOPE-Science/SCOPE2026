---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-20.md",
      "INDEPENDENT_AUDIT_2026-10-20.json"
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

Over characteristic-zero algebraically closed k and m>=3, invert all leaf z_i: exact Schur congruence reduces all submaximal minors to u=v=w=0 with w=-sum b_i*d_i/z_i; this rank-m bilinear polynomial is primitive and irreducible, giving a dense domain of affine dimension 3m-1. On a stratum with t zero z_i the residual M=[C B; B^T 0_t] has rank<=t. For t=1 the two B entries and det C vanish (ambient codim>=4); t=2 requires rank B<=1 plus a further scalar C condition (codim>=4); t=3 requires rank B<=1 (codim>=5); t>=4 leaf vanishing already gives codim>=4. The published Deng–Kretschmer theorem gives radical/unmixed codimension three, excluding any boundary component, so the ideal is prime. Rationality follows on b_j nonzero, dimension 3m-2, degree from the published resolution. The full determinant is irreducible by their Proposition 15; its singular set is exactly rank<=m via derivatives w.r.t. present diagonal entries, and S2+R1 gives normality; generic transverse Schur parameters give uv-w^2. Independent exact rational block checks for m=3,4 confirmed the congruence/determinant identity, not a general proof.

## originality

PASS

Compared theorem-level implications and all four named originality checks against relevant primary literature, published Resultary records, numerical sources and compatible general statements; conclusion is best-of-knowledge with explicit residual risks.

## value

PASS

The two-vertex-connected K_{2,m} family is an infinite natural test of the published sparse-symmetric submaximal-minor primality question. The all-m positive result, together with rational singular locus and its generic transverse node, gives new structural geometry beyond finite computational checks and provides a motivated boundary for the general conjecture.

The dated certificate retains the supplied scientific assessment, sources and limitations.
