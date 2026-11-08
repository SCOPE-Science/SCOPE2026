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

For any norm-one complex Hilbert Fourier orbit ψθ=Σe^{ik·θ}v_k with pairwise orthogonal v_k and weights p_k, Haar averaging of projected squared norm combined with Ky Fan bounds gives N-width²=1−ΣtopN p; the span of top modes achieves uniform-in-phase equality. Rank-one projector orbit ρθ in complex Hilbert–Schmidt class has orthogonal difference-index Fourier operators with weights q_l=Σ_k p_k p_{k−l}, yielding N-width²=1−ΣtopN q. Convex convolution q=p*check p is majorized by p; strictly so for all finite N when p is strictly positive Poisson product law. For coherent phases p is Poisson(t²a_j²) product, q is Skellam(t²a_j²) difference product. Multivariate local CLT, strict radial normal superlevel sets and Gaussian ball mass give dimensions Nv∼v_d R^d t^d∏a_j and Nproj∼2^{d/2} times this, fixed d, ai>0, ε∈(0,1), hence ratio 2^{d/2}. This is strictly about complex-linear Hilbert/HS widths, not physical positive-state compression. Independent μ=2 one-mode calculation reproduced top5 p mass≈.94734698 versus q≈.79975660 and strict N=1..14 finite majorization.

## originality

PASS

Arbes–Greif–Urban 2025 is a CLOSE broad theorem: full open-access 36-page article §§3–4, especially Corollary3.6, derives sorted shift-isometric covariance eigenspace N-width tails. Hence the universal optimal Fourier-orbit lemma is PRIOR mathematical machinery and is not independently novel. The proposed claim applies it to two distinct coherent-state phase orbits, identifies Poisson vs Skellam weights, proves strict finite-N overhead and exact anisotropic high-intensity compression ratio 2^{d/2}, not stated by inspected transport article. Mensah 2026 Pego HS criterion concerns precompactness and not quantitative widths. Existing group-orbit approximation articles may include an equivalent formulation; priority qualified.

## value

PASS

Compression of vectors and projector lifts of a d-mode phase orbit are natural competing linear approximation problems. A complete exact formula, a strict comparison at every finite N, and a sharp 2^{d/2} asymptotic resource overhead provide a motivated, quantitatively actionable invariant beyond the generic N-width theorem; no physically implementable compression claim is made.

The dated certificate retains the supplied scientific assessment, sources and limitations.
