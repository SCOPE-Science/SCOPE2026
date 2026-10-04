---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---
# Verification

The proof was checked symbolically from the definitions. For \(z^{(j)}\in S(B_Z,F_j,\delta)\), the active coordinate has norm greater than \(1-\delta\), so the entire complementary \(\ell_p\)-tail has norm at most \(\eta_\delta=(1-(1-\delta)^p)^{1/p}\). Averaging \(m\) active coordinates gives exact disjoint-support estimate \(\|a\|_p^p\le m^{1-p}\). Because the chosen center lies on an unused coordinate, \(\|x_0-a\|_p^p=1+\|a\|_p^p\). The averaged tail has norm at most \(\eta_\delta\) by convexity of the norm.

The finite conclusion follows after \(\delta\downarrow0\). For an infinite index set, the same construction is available for every finite \(m\), and \(m^{1-p}\to0\) because \(p>1\). The proof does not rely on finite experiments, exhaustive enumeration, numerical optimization, or an external certificate.

Boundary checks: at two summands the bound is \(2^{1/p}\); the proof requires nonzero factors only to choose a unit center and norm-one coordinate functionals; no norm-attainment assumption is made. The result is not asserted for \(p=1\) or \(p=\infty\), and no claim of sharpness is made beyond the already known two-summand scale.
