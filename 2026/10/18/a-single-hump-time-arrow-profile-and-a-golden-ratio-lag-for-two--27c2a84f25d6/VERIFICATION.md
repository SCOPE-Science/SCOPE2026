---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-24.md",
      "INDEPENDENT_AUDIT_2026-10-24.json"
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

The stationary 3-dimensional linear Gaussian drift eigenvalues are -a,-d,-b with all positive. Independent observer noises have zero cross-spectrum. Exact cross-spectrum subtraction gives delta(t)=2D_f*c1*c2*(d-a)*F(t) with F(t)=(2/pi) int_0^infty omega*sin(omega*t)/[(omega²+a²)(omega²+d²)(omega²+b²)] d omega and Fprime(0)=1/[(a+d)(a+b)(d+b)]. Writing each Laplace Green kernel ell_r(t)=exp(-r|t|)/(2r) and G=ell_a*ell_d*ell_b yields F=-2Gprime>0 for every t>0 by strict monotonicity of convolution of positive symmetric decreasing kernels. Distinct poles give a three-term sum of exponentials and equal poles give confluent polynomial-exponential terms. Its derivative lies in a Chebyshev space of total order 3, so at most two real zeros including multiplicity; Fprime(0)>0 and its positive decaying eventual tail forces exactly one positive simple maximum (any tangent would violate the zero bound). Gaussian reversibility for observed two-probe covariance is equivalent to a=d when c1*c2 !=0. Triple equal rates κ give F=e^{-κt}(κt)(1+κt)/(8κ⁴); differentiation yields 1+z-z², hence unique optimum at κt=(1+sqrt5)/2. Smooth positive-rate perturbation and simple root yield coalescence. Independent symbolic differentiation and sampled positive-rate checks corroborate; full universal statement follows from Chebyshev/convolution proof.

## originality

PASS

Best-of-knowledge originality assessment of this EXACT final statement against published mathematical results and the source model, not certification of historical priority. General mathematical machinery and prior model definitions are attributed; claim-specific evaluated classification is not found among inspected primaries. A failed search is not novelty proof. Prior frequency-domain cross-spectral formulas enable deriving the cross-spectrum and sometimes imply its algebraic antisymmetric part, but do not by themselves force globally fixed sign, unique peak, or triple-coalescence optimizer; these depend on convolution strictness and the zero-count of exponential polynomials. Neither ordinary observation irreversibility nor global full-system entropy production alone yields this theorem.

## value

PASS

For a canonical partial observation of irreversible OU motion, a precise positive-lag orientation sign and a unique optimal sampling lag independent of independent probe noise or coupling magnitudes are meaningful population diagnostics. The unexpected golden-ratio coalescence is an exact limiting invariant, not merely a numerical coincidence; distinction from finite-sample statistical power is explicit.

The dated certificate retains the supplied scientific assessment, sources and limitations.
