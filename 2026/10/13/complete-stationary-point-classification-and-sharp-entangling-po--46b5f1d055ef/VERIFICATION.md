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

The final claim in /workspace/repairs/5/RESULT.md corrects the frozen table's literal labels ‘strict global minima/maxima’: two points share each global value, so each is a strict local extremum attaining the corresponding global value, not a strict global extremum at an individual point. All point sets, phases, values and equality cases are unchanged. The Haar normalization checks: the two-copy Haar moment on each qutrit is (I+swap)/12; in the purity swap trace the terms with zero or two input swaps each contribute 27, and the two remaining contractions are the realignment and partial-transpose fourth moments. Thus the linear entropy is 5/8−(I_R+I_T)/144. In the real Cartesian spin-one basis, with swap S, Q=3P0=|Ω⟩⟨Ω| for Ω=Σ_i|ii⟩, and x=e^{iα}, y=e^{iβ}, the gate is (1+y)I/2+(1−y)S/2+(x−1)Q/3. Realignment interchanges I,Q and partial transpose interchanges S,Q; both moments can therefore be evaluated on the singlet, antisymmetric and traceless symmetric spaces of dimensions 1,3,5. Independent replay (python /workspace/branches/independent_reproduction.py 5, SymPy) reproduces the entire Laurent phase identity, the elimination factorization, all eight stationary values and Hessian determinants, without executing the supplied code. For exhaustion, B(α)=20+5e^{iα}+2e^{2iα} has modulus at least 13, so β-stationarity lies on two smooth sign branches locally. Along each branch E=A(c)±√Q(c)/216, c=cos α; by β-stationarity the derivative along the branch equals the α partial. For sin α≠0, a necessary equation is 9(Q′)^2−4(65+40c)^2Q=0, whose exact factorization −500(4c+5)(8c+19)(64c²+64c+115) is strictly negative for |c|≤1. At α=0 and π, B is positive real, so the β-stationarity condition gives exactly 0, π/2, π, 3π/2, each also α-stationary. The determinant signs, with positive αα at (0,0) and negative αα at (π,π/2), classify the two definite pairs and two saddle pairs; periodicity and compactness give all global equality cases. This proves the all-phase result analytically, not by sampling. It is specifically for independent Haar pure inputs, unnormalized linear entropy, and spin-invariant two-site unitaries.

## originality

PASS

The prior exact phase function and four corner cases are credited and excluded from the distinct claim. On the inspected evidence, the surviving result is the exhaustive stationary set, noncorner critical values and types, and sharp all-phase bound with equality gates. Merely substituting the prescribed corners or a fixed Hamiltonian trajectory cannot establish the exhaustion or uniform equality conditions. The repair changes only extremum terminology and leaves this comparison intact.

## value

PASS

The sharp phase-torus benchmark is needed to decide which fully spin-invariant two-qutrit gates maximize Haar-averaged output entanglement, and those gates are directly accessible by tuning two BLBQ couplings. The best invariant gate is not among the four previously analyzed corners (131/324 exceeds 20/81), and even on the α=0 branch the noncorner stationary gates are saddles. Exhaustion and exact stability types show which phase configurations are genuinely optimal rather than extremal only along a chosen evolution; this is a substantive exact classification for a natural family, not a repackaging of the known phase polynomial.

The dated certificate retains the supplied scientific assessment, sources and limitations.
