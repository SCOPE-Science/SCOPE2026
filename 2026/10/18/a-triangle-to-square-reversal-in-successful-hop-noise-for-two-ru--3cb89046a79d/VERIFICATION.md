---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

Reconstructed the transitions using d→d−u or d+v modulo n and deleting d=0 targets, and checked both reflection and particle exchange preserve the labels of counted events. A counted transition inside the first triangle orbit is a null state change but contributes exactly z=e^k−1 to the tilted diagonal; reversals remain unweighted. The irreducible generator at a>0 has a simple zero eigenvalue. Analytic dominant-eigenvalue differentiation gives Qg=μ1−J1, ν=μ+2πJg−2μπg. An independent symbolic reproduction used the 8- and 12-state unquotiented tilted matrices, not the supplied quotient or its Poisson equation. For p(y,z)=det(yI−Q−zJ) at (0,0), row multilinearity gives μ=−p_z/p_y and F=1−(p_yy μ²+2p_yz μ+p_zz)/(μ p_y). It reproduced both rational functions exactly. Replay: python /workspace/branches/check_full_activity.py (SymPy). The sign factorization gives the unique triangle crossing at a=1 and strict positivity of F4−1, and each derivative numerator has one sign change and changes sign between zero and infinity. The reproduced roots and minimum values round to the printed values. The leading and constant terms give the fast limits and slow-rate divergence. The frozen checker was inspected, not run.

## originality

PASS

The same dynamics and their stationary and un-tilted spectral solutions are established. Published SSEP activity cumulants and indexed exclusion activity records give both fast-reversal boundary Fano values, so those values are not credited as distinct. The inspected persistent-walker current work counts signed displacement, and the SSEP activity solutions eliminate orientation. Neither gives the finite-positive-a sign contrast or optimal reversal rates of the successful-hop activity.

## value

PASS

The triangle and square are the first ring geometries without and with a nonadjacent pair, respectively. Their exact contrast distinguishes a regime with sub-Poisson successful-hop noise from one with strictly super-Poisson noise for all finite rates, and the two genuine finite optima are quantitative benchmarks. This is a motivated finite comparison, not a classification of larger rings.

The dated certificate retains the supplied scientific assessment, sources and limitations.
