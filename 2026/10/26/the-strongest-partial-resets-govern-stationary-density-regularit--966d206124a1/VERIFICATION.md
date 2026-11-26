---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

Checked the stationary two-sided Poisson construction: the age and preceding gaps are iid Exp(r), their Brownian increments mix to Laplace(a), and the contribution from j gaps back is multiplied by at most q_+^j. A synchronous coupling contracts by q_+ per reset and proves uniqueness. For f=ell*nu, nu=Law(QX'), only the Q=0 part gives an atom at 0 since X' has a density. Bounded difference quotients give the derivative jump -a^2 nu({0}); equivalently the jump comes from the delta term in (r-D partial_x^2)f=r nu. The positive-q_- case is a separate regime, not an additional hypothesis compatible with p_0>0. With h=-log q_-, the deterministic product upper bound gives log phi(a exp y)<=-y^2/h+O(y). Conditioning the first ceil(y/(-log b)) contractions to be <=b for any b>q_- costs only exp(-O(y)); the remaining factors have a uniform positive product by q_+<1. Summing the arithmetic progression in the bounded products and letting b decrease to q_- gives the sharp matching lower limit. All polynomial Fourier moments exist. For the 2k-th derivative, after t=a exp y, sandwich the exponent on y>=Y between (2k+1)y-(1/h±epsilon)y^2, with the remaining t<=a exp Y contribution at most exponential in k. The upper Gaussian integral and a fixed-width interval around the lower Gaussian maximizer yield h for the k^-2 log-limit. Positivity prevents cancellation, and factorial growth is o(k^2) on the log scale, proving zero Taylor radius. Analytic replay: RESULT.md §§1–4. Additional deterministic normalization check: for Q=q, multiplying the product by 1+(t/a)^2 gives Phi_q(qt), hence its even Fourier integrals satisfy I_{2k}/I_{2k-2}=a^2(q^{-(2k-1)}-1); summation reproduces the leading constant. Inspected verify.py and its recorded 223 finite checks without executing the uploaded code; they are not proofs of the limits.

## originality

PASS

Credit the sharp universality over genuinely random iid contraction laws with positive essential infimum. The fixed-contraction special case has direct and even sharper overlap; the zero-atom formula is a useful but short consequence of the stationary adjoint equation, not a separate new method. Same display date does not settle priority.

## value

PASS

The logarithmic derivative rate extracts the strongest essentially available contraction from the density even if contractions near that bound are rare. This is materially different from fixed-factor smoothness or finite moment identities. Distinguishing the zero atom by an exact spatial jump gives a useful contrasting diagnostic without extending the claim to the unresolved regime ess inf Q=0 with no atom.

The dated certificate retains the supplied scientific assessment, sources and limitations.
