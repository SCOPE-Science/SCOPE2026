---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-31.md",
      "INDEPENDENT_AUDIT_2026-10-31.json"
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

The triangular density is continuous, compactly supported and normalized to mass one. Distributional differentiation twice gives F_c(t)=2E_c(t)/(c(1-c)t^2) for t!=0 and F_c(0)=1, with E_c=e^{-ict}-(1-c)-c e^{-it}. Strict convexity of the disk implies any real zero must have e^{-it}=1 and kc integer, hence nonzero zeros exist exactly for rational apex c=p/q at t=2pi*q*nonzero integer; E_c has vanishing first derivative and second derivative c(1-c) there, giving multiplicity two. For a cell t=2pi k+u, |u|<=pi, let P=(1-c)+c e^{-iu} and r=|E|. From 1-|P| <= r and 1-|P|^2=4c(1-c)sin^2(u/2), derive c(1-c)u^2 <= pi^2 r/2. The cancellation of the linear Taylor term in e^{icu}P bounds |e^{icu}P-1| <= pi^2r/4; triangle inequality yields the uniform lower cell bound with factor 1+pi^2/4, and u=0 gives equality for the upper estimate. |1-e^{-2pi ikc}| is comparable to ||kc||, so the cell minima of |t|^2|F| have exact Diophantine order; taking log-limsup gives mu(c)+1, including Liouville mu=infinity, and the globally weighted cubic lower bound is equivalent to inf_k k||kc||>0. Wiener L1 translation cyclicity follows for irrational c. Independent 100 frequency-cell checks at 201 sampled points each plus rational zero locations agreed with the global inequality; the proof, not samples, treats all real frequencies.

## originality

PASS

CharFun 2019 source explicitly implements the general three-exponential triangular characteristic function; the source transform is prior and trivial to specialize to [0,1]. Dimitrov–Xu 2016 treats the symmetric tent with sinc-squared zeros and Wiener translation density, not irrational asymmetric apex conditioning. Wiener’s criterion and irrationality exponent identity are classical. The claim is confined to a uniform full-cell inequality plus their exact application to this one-parameter family. Best-of-knowledge novelty assessment of the surviving precise mathematical contribution; unsuccessful database search is not proof of absolute priority.

## value

PASS

The full-frequency cell lower estimate quantifies how a positive compactly supported kernel can be zero-free but arbitrarily poorly conditioned. The exact link to irrationality exponent and badly-approximable threshold is a natural bridge between Fourier translation cyclicity and Diophantine small divisors; neither the already-known triangular characteristic function nor the zero classification alone is submitted as the principal novel value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
