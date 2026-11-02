---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-26.md",
      "INDEPENDENT_AUDIT_2026-10-26.json"
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

The circle-unitary symmetry gives w(T)=lambda_max(T+T*)/2 on complex ℓ². The positive geometrically decaying Jacobi matrix is compact; for s,t>0 its simple isolated Perron eigenvalue and positive eigenvector support analytic perturbation. At s=0 the block split is one weight-1 edge plus geometrically scaled four-vertex paths with edges (q²,tq³,q⁴); the quartic λ⁴-(a²+b²+d²)λ²+a²d² gives λ=1 at t=q^{-3}sqrt((1-q⁴)(1-q⁸)). Every s>0 forces λ>1 via principal first-three vertices. Above that budget, endpoint derivatives decrease strictly along the segment into its interior; global strict Hessian positivity follows from the spectral second-derivative formula, since Dv=αv has α=0 at row 0 then direction components vanish at rows 1 and 3. Thus unique strictly positive analytic optimizer and strict convexity in c. At large c, the leading disjoint A and B edges have equal top weight a=q³/(1+q²) at x0=q²/(1+q²). Principal edges bound the optimizer displacement y in a fixed compact interval. The top two-dimensional eigenspace has complementary gap a(1-q⁴); uniform Schur control leaves 2×2 M_y=[[qy,q²/2],[q²/2,-q³y]], whose minimum eigenvalue top branch is a at y*=-(1-q²)/(2(1+q²)). This proves the stated nonuniform-in-q two-term expansions. Independently SymPy verified the quartic zero and M_y eigenvalues and a 160-dimensional Jacobi spectral implementation sampled q=.3,.6,.85 at c/c*=.7,1,1.3,10,1000, confirming phases and asymptotic convergence. These finite checks are not asserted to prove all q,c.

## originality

PASS

Best-of-knowledge novelty of the fixed-total-modulation optimization theorem, not of the four-periodic shift itself: the identical weight family is introduced in Ghosh–Birbonshi–Ojha (2026), and a general entire-determinant representation evaluates its numerical radius at fixed parameters. The accessible abstract and detailed secondary synopsis discuss bounds, polynomial critical-point questions, and determinant recurrences, but do not establish the constrained c=s+t threshold, uniqueness/analytic curvature, or the two-term c-to-infinity optimizer displacement. The originating full text could not be inspected despite lawful arXiv/OA attempts and authorized Oxford request, so possible direct coverage is an explicit residual risk rather than a fabricated negative conclusion. The earlier 2022 primary paper has a different eventually-periodic nonzero tail; related published SCOPE findings concern q-to-one limits with fixed s,t or finite cyclic bound optimization, and do not imply this budget theorem.

## value

PASS

The already-motivated two-parameter four-periodic geometric shift makes a fixed total coefficient budget s+t=c a natural spectral allocation problem, not an arbitrary finite sample. An exact threshold separating a nonattained open-domain infimum from a unique interior optimizer is a full, nontrivial parametric classification for every q∈(0,1), with rigorous curvature and the sharp order-one displacement of the optimal split as c→∞. The model is compact infinite-dimensional, and the singular two-edge spectral crossing requires specific analysis beyond fixed-parameter determinant evaluation. The result is self-contained and could inform subsequent optimal spectral design calculations for weighted Jacobi operators; no general theorem or paper-sized downstream consequence is required. Its mathematical significance does not depend on uniqueness of wording; remaining priority caveats are in originality.

The dated certificate retains the supplied scientific assessment, sources and limitations.
