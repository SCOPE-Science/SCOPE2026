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

The scalar numerator is positive on the real nonpositive spectrum and the denominator never vanishes; r(0)=1 handles normalization and h=0. The Taylor recurrence gives coefficients 1,1,1/2,1/6,1/24,1/144,0,−1/1728 through degree seven. For distance d≤5 only shortest walks contribute at h^d, giving a positive coefficient. At distance six the coefficient at h⁶ vanishes: (L^7)_{0,6}=14(A^6)_{0,6}−(A^7)_{0,6} gives 28 for C₁₂ and 13 for C₁₃, so the h⁷ term remains positive. At distance seven the h⁷ term is strictly negative, with two shortest walks on C₁₄ and one for n≥15. No extrapolation in n is used. Exact independent rational inversion for n=3–6 matched the distance-class formulas; for n≤5 their off-diagonal numerators are positive for h>0, and for n=6 only the distance-one sign depends on Q(h)=5h⁴−12h³−102h²−144h−72, via the numerator −2hQ. Descartes or the independent Sturm count gives one positive root, numerically 6.36885080963102, with Q(6)<0<Q(7); diagonals are positive by spectral calculus. At large h the scalar leading term gives T=I−12L⁺/h+O_n(h⁻²), and the periodic second differences and mean-zero condition give the displayed Green kernel. Its nearest-neighbor coefficient is (n−1)(n−5)/(12n), positive for n≥6. In normalized row coordinate x=d/n the leading negative positions tend to the set x(1−x)<1/6, whose length is 1−1/√3. For each fixed n, rationality ensures eventual sign or identically zero even at vanishing leading coefficient; at most two signed residues solve the equality, so they do not influence the iterated limit. The packaged replay is python artifacts/verify_cycle_pade.py with the dependency in artifacts/requirements.txt. Both files were inspected, not executed; the original 438-assertion run is recorded support, not independent verification. The classification concerns exact end steps, with small/large neighborhoods per fixed n and no intermediate-step classification for n≥7.

## originality

PASS

The supported distinct result is the sharp fourteen-site threshold for arbitrarily small steps and the consequent split between sizes 6–13 and sizes ≥14. Direct earlier coverage establishes the all-step cases through five, the large-step boundary at six, and the identical exact six-cycle horizon. It also supplies the full large-step Green coefficient, from which the spatial fraction follows directly; neither the coefficient nor its sign-count corollary is credited as independent novelty. The earlier record's informal small-step nonnegativity remark does not prove a cutoff and, if read as all cycle sizes, is corrected by the distance-seven calculation. The frozen three-way classification is not covered by the earlier dichotomy.

## value

PASS

The distinct small-step threshold is a motivated sharp boundary for a standard diffusion model and timestep method. It distinguishes failure that can be avoided by shrinking the step on intermediate meshes from failure that persists at arbitrarily small positive steps on every larger cycle. The vanishing sixth coefficient and the two sizes where walk counts must settle its sign provide a structural reason for the precise threshold; value does not rest on recomputing the known quartic or row kernel.

The dated certificate retains the supplied scientific assessment, sources and limitations.
