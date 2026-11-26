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

Plancherel gives the exact continuum maximum of n|phi|^(n-1)|1-phi|. Positive coefficients force common phases at modulus-one contacts, which by Bezout are t=2pi j/g; their values run over exactly the q-th roots of unity. Evaluating at contacts and using exponential decay on the compact complement of their neighborhoods proves the c_q limit. When q=1 the neighborhoods are exact copies. With u=x/sqrt(n), the centered and drifting multipliers, including their specified normalizations, converge locally uniformly to (v x^2/2)exp(-v x^2/2) and |m x|exp(-v x^2/2). They have uniform polynomial-times-Gaussian majorants on the expanded neighborhoods, so maxima converge, giving e^(-1) and |m|/sqrt(e v) respectively. This proves the Ritt criterion for the contraction and also covers proper sublattices. A one-atom multiplier has constant modulus one and is either identically one or takes the value minus one, giving the two stated boundaries.

## originality

PASS

The supported distinct content is the sharp universal centered limit e^(-1) for finite nondegenerate probability laws with q=1, including nonsymmetric laws, and its inclusion in a complete bilateral classification. The resonant and noncentered constants have substantial previous Resultary coverage, and the qualitative centered Ritt property follows from Cuny even on proper sublattices. Neither of those overlaps supplies the sharp centered multiplier maximum.

## value

PASS

The distinct centered limit gives the exact nonzero asymptotic defect, rather than only boundedness, for a natural class of finite-range Markov operators with arbitrary asymmetric centered laws and lattice span. Together with the previously covered regimes it provides a usable lattice/drift classification and explains why the sharp constant in the nondegenerate centered class is independent of all the weights and of the sublattice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
