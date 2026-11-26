---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

For fixed theta>0 and n>=2, the open row mass matrix has first row (a_j), unit downward shifts, and a single deficient row of deficit t_n. It is irreducible with a self-loop, including the one-cell case; the backward left-eigenvector recursion and mass loss give both identities in (2) with the stated normalization. For theta>1, the derivative of the characteristic sum is asymptotic to the truncated first moment, which tends to zeta(theta); pointwise convergence to t_j/zeta(theta) preserves total mass and hence gives TV, including for the spatial measures because their conditional laws within cells agree. At theta=1, every tilted weight differs multiplicatively from its harmonic proxy by at most exp(1/(H_n-1)); summing the proxy to floor(n^s) gives the uniform Kolmogorov bound, and the cell-coordinate logarithms differ by at most log(2)/log(n). For 0<theta<1 the exponential root sum is an integrable Riemann sum (v^(-theta) at 0), and the eigenvector sum gives the locally uniform density limit. The bound pi_{n,j}<=C n^(theta-1) j^(-theta) controls the mass of j/n near 0 and also gives O(delta+1/n) for the last delta n sites. Tonelli and the root equation normalize the limiting density; the cell endpoints squeeze n^theta X_n. The two divergent-index regimes imply unscaled convergence to zero. A finite independent check using root bisection followed by the backward recurrence and direct weighted-sum formula at theta=0.6,1,1.5 and cutoffs 20 and 5000 found eigen-identity residuals below 7e-17; critical proxy TV at n=5000 was 0.00371 versus a bound of 0.1315. These are floating-point diagnostics, not evidence for uniformity in theta or a proof of the limits. The frozen scripts and verification metadata were inspected without execution; no formal verification or expert attestation is claimed.

## originality

PASS

The same open operator, closed ACIM, and escape-rate constants are prior work. The finite cell formula is a short consequence of the known operator and is not a separate novelty. The supported distinct claim is the spatial scaling theorem for the normalized uninduced Perron law, particularly the quantitative log-uniform critical law and explicit nondegenerate cell-scale density in the infinite-measure case.

## value

PASS

For this natural family the observation of surviving locations is not predicted by the escape rate alone. The theorem specifies what can replace a finite limiting invariant probability when mass accumulates at the neutral point, including the critical distribution on logarithmic position scales, an error bound, and an explicit law on the hole scale below the critical exponent.

The dated certificate retains the supplied scientific assessment, sources and limitations.
