---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-29.md",
      "INDEPENDENT_AUDIT_2026-10-29.json"
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

Der(A) is eight-dimensional: two generator images each have four coefficients because the square relations differentiate to zero in characteristic 2. The explicit invertible coordinate map Φ to tracezero 3×3 matrices intertwines squares Φ(D²)=Φ(D)². Any nonzero 3×3 square-zero matrix has rank 1 and form uv^T with u,v nonzero and v·u=0. Then D(xy)=v0(u2 x+u1 y+u0 xy), so zero precisely when v0=0. If v0=0 all generator images are in one line (rank_D=1) and H has dimension 2, a surviving unit and square-zero augmentation class, hence dual numbers. If v0≠0, rank_D=2 and H=0. Projective covector v has q+1 points with v0=0 and q² with v0≠0; for each q²−1 eligible nonzero orthogonal vectors u, proving the census. Independently brute-forced all 2^8 derivations on F2, recovering 1,9,12 for ranks 0,1,2. Crucially the original SLOGAN.txt has an actual newline breaking `\(D(xy)\ne0\)` into malformed KaTeX; the complete corrected UTF8 replacement is staged with the exact source Git blob and SHA256.

## originality

PASS

Independent best-of-knowledge comparison of exact final mathematical claim and implications against named primary literature and targeted Resultary results. Specific prior components are credited; no negative search alone establishes priority. A more general theorem may imply individual tools, but not the full proposed classification as explicitly identified.

## value

PASS

Socle evaluation is an intrinsic one-scalar acyclicity detector for unrestricted square-zero derivations of a small natural characteristic-two truncated polynomial algebra. Together with the complete cohomology-algebra and finite-field rank distributions, it provides a reusable structural classification rather than a bare matrix nilpotent count.

The dated certificate retains the supplied scientific assessment, sources and limitations.
