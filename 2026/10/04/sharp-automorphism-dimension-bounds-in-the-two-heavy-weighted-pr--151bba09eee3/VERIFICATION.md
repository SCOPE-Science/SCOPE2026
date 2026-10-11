---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-05.md",
      "INDEPENDENT_AUDIT_2026-10-05.json"
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

Cox's automorphism theorem gives the covering-group dimension as the sum of the Cox-ring graded-piece dimensions; quotienting by the one-dimensional grading torus yields the submitted formula. Direct weighted-monomial counts give the three special formulas for \(1<a<b\), equal heavy weights and \(a=1\). On the canonical/terminal triangles, monotonicity of \(B_r(m)=\binom{r+m-1}{r-1}\) and the submitted binomial estimates isolate the outer corner, with the terminal \(r=2\) exception checked separately. I independently recomputed graded-piece dimensions by a weight-DP and exhaustively recovered every maximum for \(2\le r\le11\); the frozen verifier was also read.

## originality

PASS

Cox supplies the general automorphism formula and Kasprzyk supplies general weighted-projective singularity criteria; the published SCOPE triangular classification supplies the exact two-heavy feasible region. None of those results optimizes the graded-piece dimension over the family or states the all-dimensional maximizing weights and low-dimensional terminal tie. Resultary searches found same-family invariant records but no prior automorphism-dimension extremum.

## value

PASS

Automorphism dimension is a natural symmetry invariant relevant to moduli quotients. The result gives sharp all-dimensional extrema and equality cases, including a nontrivial boundary exception, rather than merely evaluating isolated weighted projective spaces.

The dated certificate retains the supplied scientific assessment, sources and limitations.
