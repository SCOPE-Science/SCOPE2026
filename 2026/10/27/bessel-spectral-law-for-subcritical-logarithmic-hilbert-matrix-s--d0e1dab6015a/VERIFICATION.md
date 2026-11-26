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

Reconstructed the result for fixed 1<alpha<2 and each fixed positive j. Normalized area gives target monomial squared norm 1/(m+1) and source moment v_n. Substituting u=(n+1)(1-t) in v_n gives pointwise exponential density and normalized logarithmic weight tending to one, dominated by C exp(-u/2)(1+|log u|)^alpha for n>=1. Thus v_n has leading coefficient one and the model entries in RESULT.md (46) have the stated normalization. Dividing each normalized entry by the square root of the two cell lengths gives kernel (75)-(77), with limit y^(-alpha/2) for x<y and zero for x>y. On y>=epsilon uniform domination applies. The sum over m of the squared entries in column n is O((log(n+2))^(1-alpha)/(n+1)); integral comparison bounds the normalized sum on y<epsilon by O(epsilon^(2-alpha))+o(1), including a cell straddling epsilon (its upper logarithmic coordinate differs by O(1/log(N+2))). The limit kernel has the same integrable small-column behavior. A bounded diagonal correction tending to one in high columns preserves convergence, as the finitely many early columns vanish after normalization. The exact full-output squared tail is O((log(N+2))^(-alpha)); embedding its additional cells in L2(0,infinity) gives the same limit with zero extension. For the Bessel reduction the adjoint implies x^alpha u'=-s^(-2) integral_0^x u and hence the zero flux condition; the J branch has zero flux and the independent branch has leading behavior x^(1-alpha) with nonzero flux, also at integer order. Conversely, a regular solution satisfying u(1)=0 gives f=-x^(alpha/2)u' in L2 and reproduces the adjoint eigen-equation by integrating the flux. This yields exactly the stated Bessel zeros; norm convergence controls fixed-index singular values, and the squared kernel norm is 1/(2-alpha).

## originality

PASS

The supported distinct claim is the subcritical finite-section Hilbert–Schmidt transfer and its spectral consequences, not the continuous Bessel spectrum, the moment asymptotic, or the boundedness threshold. The checked stronger and adjacent results do not give that transfer.

## value

PASS

Quantifies the spectral divergence of the natural polynomial truncations below a known mapping threshold. The full compact limit gives the entire squared mass and each fixed-index constant, matters not determined by unboundedness or norm growth alone, and identifies a reusable operator approximation rather than just fitting a first singular value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
