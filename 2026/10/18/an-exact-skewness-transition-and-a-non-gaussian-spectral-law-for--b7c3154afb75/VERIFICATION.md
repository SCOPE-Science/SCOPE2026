---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-22.md",
      "INDEPENDENT_AUDIT_2026-10-22.json"
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

Iid uniform circle points imply every forest of distinct edge indicators is independent by iterative leaf integration; thus E E_n=C(n,2)*2r and Var E_n=C(n,2)*(2r)(1−2r). For a triangle the Dirichlet(1,1,1) ordered spacings give exact probability 3r²+(3r−1)_+²; subtracting p³ yields delta(r)=r²(3−8r) for r<=1/3 and (1−2r)³ above 1/3. Expanding centered edge sum cube, only one-edge repeated terms and ordered full triangles remain, so E[(E_n−mp)^3]=m p(1−p)(1−2p)+6*C(n,3)*delta(r). Divide by m: p(1−p)(1−2p)+2(n−2)delta. In upper regime with q=1−2r this factors q[−1+3q+2(n−3)q²], giving exact root r_n=1/2−1/(3+sqrt(8n−15)); lower regime strictly positive and n>=3. For fixed r, Fourier eigenvalues a_k=sin(2pi kr)/(pi k) of degenerate connection kernel and joint CLT yield (E_n−mp)/n⇒sum_{k>=1}a_k(Exp_k(1)−1). Degenerate U-stat tail L2 bound by sum_{k>K}a_k², and Parseval gives variance r(1−2r), triangle trace gives third cumulant delta(r)>0, hence non-Gaussian. Independently 20k-term Fourier checks for r=1/5 and 2/5 reproduced third cumulants .056 and .008 to ~5e−15 and limiting variances to <3e−6; truncations do not prove the limit.

## originality

PASS

Pairwise-independence and classical degenerate U-stat Fourier chaos are known methods, and geometric triangle correction has predecessors. The identified papers address isolated-node Poisson/soft models, high-dimensional signed-triangle detection, or sparse high-dimensional regimes, rather than the exact *hard circle fixed-n edge-count* third-moment sign boundary tied to its explicit fixed-r spectral limit. Best-of-knowledge novelty is the simultaneous specific finite-n and limiting law; broader old U-stat formulas remain risk.

## value

PASS

Uniform-circle hard random geometric graphs are a canonical model. Pairwise-independent edges have exactly binomial variance yet a strong explicitly radius-dependent skewness anomaly with a unique finite-n sign boundary; the explicit non-Gaussian spectral chaos shows how long-range triangle dependence survives order-n scaling. The concrete exact transition and limit jointly motivate this result beyond generic Fourier/U-stat machinery.

The dated certificate retains the supplied scientific assessment, sources and limitations.
