---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-27.md",
      "INDEPENDENT_AUDIT_2026-10-27.json"
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

Reconstructed from actual frozen RESULT.md: bisector unit normals yield M(omega)=I−2omega diag(p,q)+omega²(p,q)(p,q)^T for expected coordinate squares, with p=(1+c)/2,q=(1−c)/2. Its positive offdiagonal for omega>0 makes Perron root the exact asymptotic expected squared norm factor for any nonzero deterministic starting error. Conditional energy identity and positive definite average Gram yield convergence iff 0<omega<2. For stable omega, rank-one secular equation 1=omega S(z) with z=delta/omega in (0,2q); S strictly increases from 1/2 to infinity, parametrizing omega∈(0,2), and derivative S−zS′=2F has strictly negative derivative −zS″ for z>0, so unique optimizer. At c=0 symmetry yields omega*=1. At c>0 the derivative of rho at omega=1 equals −2pq c²/(p²+q²)<0, giving strict overrelaxation. Near parallel q↓0, critical balance 2q−z~2q^(3/2) implies optimized spectral gap~4q versus default 2q. All boundary quantifiers and the excluded singular c=1 were checked. Independent new SymPy/algebraic replay 7 identities plus eight high-precision representative values; tests are corroboration only, not infinite proof.

## originality

PASS

The actual IID-with-replacement, uniform two-row *mean-square* Perron-rate optimizer is not implied by the closest full-primary material assessed: 2007 standard-projection expected bounds, 2014 exact-MSE covariance operator with optimization of sampling rather than relaxation, 2015 unrelaxed exact MSE, and separately published deterministic cyclic two-row finite-horizon optimization. In particular the cyclic optimum 2/(1+sqrt(1-c²)) differs from the IID optimum (for c=1/2, about 1.071797 versus 1.179020). Published semantic searches returned no covering exact two-row IID relaxation result. This is explicitly best-of-knowledge, with major uninspected-relaxation-paper residual risks: source access is not fabricated, and failed search is not a novelty certificate.

## value

PASS

Constant-relaxation choice in two-row uniformly randomized Kaczmarz is a natural measurable performance question whose exact annealed asymptotic factor differs from one-step energy bounds and deterministic cyclic sweeps. The unique root characterization spans every nonorthogonal angle, reveals overrelaxation is strictly optimal for all nonorthogonal rows, and gives a sharp limiting factor-two improvement in spectral gap for nearly parallel lines. It is a nontrivial precise benchmark for stochastic projection dynamics rather than a relabeled standard upper bound or a tiny isolated numerical gain; no claim for finite horizon, general sampling, almost-sure exponents or more rows.

The dated certificate retains the supplied scientific assessment, sources and limitations.
