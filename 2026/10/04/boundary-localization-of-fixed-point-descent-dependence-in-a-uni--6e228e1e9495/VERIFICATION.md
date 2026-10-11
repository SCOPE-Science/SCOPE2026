---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-04.md",
      "INDEPENDENT_AUDIT_2026-10-04.json"
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

Conditioning on \(I_i=1\) leaves all remaining values uniformly permuted. If \(i\notin\{j,j+1\}\), exchangeability of \(\Pi(j)\) and \(\Pi(j+1)\) gives \(\Pr(D_j=1\mid I_i=1)=1/2\), hence zero covariance. For \(i=j\) and \(i=j+1\), direct counting gives conditional probabilities \((j-1)/(n-1)\) and \((n-j-1)/(n-1)\), yielding exactly the two displayed adjacent-entry formulas. Summing them gives every column sum \(-1/[n(n-1)]\); summing along each fixed-point row cancels in the interior and leaves \(-1/(2n)\) at the two endpoints. The wrap descent contributes \(+1/(2n)\) at those endpoints and zero elsewhere, proving exact cyclic orthogonality. With the standard \(\operatorname{Var}(F)=1\) and \(\operatorname{Var}(D)=(n+1)/12\), the correlation formula follows. The exhaustive checker through \(n=9\) was inspected only as finite corroboration.

## originality

PASS

Best-of-knowledge originality survives targeted comparison. Classical work treats the fixed-point set, descent classes with a prescribed total number of fixed points, and global joint fixed-point/descent statistics. Those statements collapse fixed-point locations or study other adjacent-pair encodings; they do not imply the submitted sparse coordinate cross-covariance matrix, endpoint-only row sums, or the exact restoration of covariance zero after cyclic closure. Resultary, SCOPE and exact web searches found no position-resolved equivalent.

## value

PASS

The result is a natural structural refinement of a classical joint-statistics problem: it identifies the entire cross-covariance matrix, proves that the aggregate \(-1/n\) dependence is purely an open-boundary effect, and shows cyclic closure restores exact coordinatewise orthogonality. This localization is potentially useful in multivariate limit/Stein calculations because it exposes the sparse dependence structure rather than merely another aggregate moment.

The dated certificate retains the supplied scientific assessment, sources and limitations.
