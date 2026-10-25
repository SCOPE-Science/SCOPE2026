---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-23.md",
      "INDEPENDENT_AUDIT_2026-10-23.json"
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

Direct integration gives H_g z^k= sum_j n_j b_j/(n_j+k) z^{n_j−1}. Factor through V with columns v_j(k)=sqrt(n_j)/(n_j+k) and U=V*. Under x=e^t, normalized continuous kernels become separated translates of h(t)=1/(2cosh(t/2)). Their Gram kernel K(s)=|s|/[2sinh(|s|/2)] has summable off-diagonals, yielding an upper Riesz bound; a triangular Fourier minorant for separated log n_j and nonzero h-transform gives a strictly positive lower bound. Integer step sampling has derivative Hilbert–Schmidt error with decaying tail since sum n_j^-2 finite. Tail lower bound plus injectivity from vanishing Hausdorff moments of analytic F(t)=sum c_j sqrt(n_j)t^{n_j−1} yields global bounded-below V. Thus V* surjective with bounded right inverse, and approximation-number ideal inequalities show a_k(H_g) comparable with a_k(D), uniform in k,p,coefficients. Includes boundedness, compactness, S_p and realizable decay consequences, without assuming finite tests prove infinite Riesz bound.

## originality

PASS

Prior theory contains qualitative Hardy boundedness/compactness and Schatten membership for p>=1; the claim adds all-index coefficient-independent a_k equivalence, including quasi-Schatten p<1 and arbitrary prescribed decay. The nearest August 2026 Hardy lacunary paper full text was inaccessible; this remains a serious overlap risk.

## value

PASS

An all-index singular-decay profile for a nontrivial Hardy-space integral operator is an informative operator-ideal classification. It yields a constructive realization of arbitrary compact s-number rates and unifies every quasi-Schatten exponent p>0 from a single coefficient criterion, beyond qualitative compactness or a mechanical restatement of a single Schatten class.

The dated certificate retains the supplied scientific assessment, sources and limitations.
