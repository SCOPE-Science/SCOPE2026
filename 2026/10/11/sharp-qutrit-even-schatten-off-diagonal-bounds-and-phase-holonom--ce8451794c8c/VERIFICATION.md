---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-15.md",
      "INDEPENDENT_AUDIT_2026-10-15.json"
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

For B=ρ−diagρ and u=Tr B², the Hilbert–Schmidt orthogonality yields u≤t−1/3 with equality only for uniform diagonal. The gauge-invariant cubic v=Tr B³=6Re(B12B23B31) obeys |v|≤u^(3/2)/sqrt6 by AM–GM, with equal-modulus edges and phase 0 or π at equality. Cayley–Hamilton for traceless Hermitian 3×3 B gives B³−uB/2−vI/3=0; recurrence h_k=(u/2)h_(k−2)+(v/3)h_(k−3), in particular h6=u³/4+v²/3, gives all even 2m≥6 moments with positive v² dependence. Their maximum is (2^(2m)+2)(u/6)^m and is attainable via ρ=I/3±s(ww*−I/3), |wi|²=1/3. Eigenvalues (1±2s)/3,(1∓s)/3 twice give negative branch PSD iff s≤1/2, i.e. t≤1/2. Entrywise l1 maximum 2s and determinant positivity 1−3s²+2s³cosθ≥0 follow separately. Independently recomputed Cayley–Hamilton polynomial coefficients through moment order 32 and exact phase/eigenvalue cases. No higher-dimensional or noninteger extension claimed.

## originality

PASS

Singh–Bera–Dhar–Pati (2015), inspected complete source, proves the entrywise l1 mixedness inequality and exhibits the positive pseudo-pure maximizing family; that numerical inequality is not new. The present result concerns direct even Schatten norms of the fixed-basis off-diagonal matrix and classifies the gauge-invariant ±triangle phase, including an admissible negative branch contradicting any blanket positive-family uniqueness. Rana–Parashar–Lewenstein (2015–16) study minimization of Schatten distances to arbitrary diagonal states, not ||ρ−Δρ|| at fixed purity. A classical matrix inequality in older traceless-3x3 spectral-moment literature could coincide; retained as risk.

## value

PASS

The qutrit three-edge gauge product is the first phase-sensitive invariant beyond quadratic purity: quartic moment is u²/2 and cannot distinguish phases, whereas every even moment from order six does. Sharp analytic fixed-purity control, all equality cases, and the exact t=1/2 positivity threshold are structurally motivated quantum-matrix inequalities, not a routine numerical tightening of l1 coherence.

The dated certificate retains the supplied scientific assessment, sources and limitations.
