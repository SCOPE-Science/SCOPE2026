---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-25.md",
      "INDEPENDENT_AUDIT_2026-10-25.json"
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

Independently reconstructed the claimed finite certificate from the seven assigned frozen Git blobs (tree SHA exactly matched). For s=847/1000 and g(x)=1+(127/120)x, K_s^(12)g(x)-g(x) is the sum for a=1..12 of 4^(-a)[(a+x)^(1.694)+(127/120)(a+x)^(0.694)] minus 1-(127/120)x. Both exponents are positive, so on each cell [j/N,(j+1)/N] each positive summand is bounded below by its value at left endpoint while the subtracted linear g is bounded above at right endpoint. Independently performed this 60-digit mpmath.iv outward-enclosed endpoint proof for all N=2000 cells: worst lower endpoint >0.000051512874938653, attained at j=1005, exceeds 1/25000=0.00004; an independent N=4000 run also passed. This is an exhaustive finite interval proof of the CONTINUUM inequality, not samples; it differs from the source verifier which propagates intervals through the whole expression. Since every a>=13 summand is positive, full K_s g > g+1/25000. With g(x)<=247/120 it gives K_s g >= (1+3/154375)g. Iterating positivity and bounding operator norm gives r(K_s)>=1+3/154375>1. The directly inspected source Proposition 1 supplies strictly increasing P(s)=log r(K_s), unique zero D_2, so D_2<0.847. The source Fourier comparison eta_*<=D_2/2 yields eta_*<0.4235. No conclusion from a merely truncated finite numerical sum is used.

## originality

PASS

Best-of-knowledge novel content is an explicit, rigorous, rational pressure-sign certificate K_{847/1000}g >= (1+3/154375)g, hence the provable D_2<0.847 and eta_*<0.4235. Alkauskas 2026 supplies the operator, uniqueness of the pressure zero, Fourier comparison, and a numerical evaluation D_2/2=0.4223047..., not a proof of that rational sign. Pollicott 2026 explicitly uses positive-transfer-operator certification on a different Farey/Hausdorff-dimension problem; so no novelty is attributed to the positivity technique itself. The independent Resultary queries returned the identical record as their nearest hit; it was excluded as priority evidence. Checked broader and older primary results do not supply the correlation-pressure numerical sign. No inference that absent search results prove priority; residual risk of unindexed bounds retained.

## value

PASS

The 2026 primary theorem advances Salem's problem using a previously unquantified-in-proof correlation pressure zero, but reports D_2/2=0.4223047... only as a numerical evaluation. Converting the pressure sign at a natural three-decimal rational threshold to a replayable exhaustive continuum certificate yields a genuine proved Fourier-decay exponent obstruction eta_*<0.4235, strictly stronger than the older half-Hausdorff upper obstruction approx 0.4373581525. The particular certificate is short (12 branches, positive linear g), pertinent to a named research question, and supplies a precise rigor gap a future researcher may need to cite without trusting unquantified numerical approximation. Value is the explicit certified threshold rather than novelty of the general positive-operator method. It does not determine exact D_2 or eta_* and is not claimed numerically optimal.

The dated certificate retains the supplied scientific assessment, sources and limitations.
