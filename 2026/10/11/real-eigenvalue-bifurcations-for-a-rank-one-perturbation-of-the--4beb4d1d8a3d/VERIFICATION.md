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

## Analytic checks
The main proof establishes the scalar secular criterion exactly off the unperturbed circle. The spectral transform is checked by the beta integral \(\int_0^\infty v^{ia}/(1+v)^2\,dv=\pi a/\sinh(\pi a)\). The quotient functions \(q\) and \(p\) have an explicitly positive second derivative for \(q\), yielding strict monotonicity and the three exact real ranges of \(G\). The half-integer inverse-square sum supplies the boundary constants \((4\pm\pi^2)/8\). The boundary eigenvectors are handled by direct integral-operator calculation and Fourier local integrability, respectively. The eigenvalue crossing coefficient comes from the Taylor expansions of \(q'\) and \(p'\). The mathematical theorem is infinite-dimensional and rests on this proof, not numerical samples.

## Standalone check
Run `python3 verify_rank_one_cesaro.py` with Python 3 and its standard library. The program independently quadratures the real spectral integral and the three Laplace formulas for twelve real parameters, verifies \(G(1)=1-\pi^2/6\), checks the two explicit endpoint constants, tests sample strict monotonicity and the local crossing slope. Success is the literal line `RANK_ONE_REAL_CESARO_BIFURCATION_NUMERICAL_CHECKS_OK`.

## Known limits
The checker is finite and cannot establish any universal monotonicity, endpoint equality, completeness of point spectrum, or absence of nonreal eigenvalues. Those universal assertions are proved analytically where claimed. Nonreal eigenvalues and perturbations of other vector directions have not been classified. No independent audit was performed.
