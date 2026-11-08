---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-03.md",
      "INDEPENDENT_AUDIT_2026-11-03.json"
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

PASS: The polar form of Q_B(X)=tr(BX^2) is tr((BX+XB)Y). Orthogonality over X gives the squared magnitude q^4 times a character sum on ker L_B, so supported magnitudes are q^(4-r_B/2). For odd fields trB=0 nonzero implies image span(I,B) of rank 2, singular trace-nonzero B gives rank 3, and invertible trace-nonzero B rank 4; counting the classes proves R_odd(q)=q^8-2q^7+q^6+2q^5-q^4-q^2+1. In characteristic 2, scalar B gives an additive square-phase with exactly A=lambda^(q/2)I; nonscalar B centralizer span(I,B) gives two independent trace constraints, hence R_even=q^6-q^3+q. Independent full integer Fourier-Walsh/cyclotomic checks for q=2 (256 frequency pairs, rank 58) and q=3 (6561 pairs, rank 3313) confirmed all zero/nonzero predictions and squared amplitudes. Arbitrary q is established by field-algebra proof, not the prime-field enumeration.

## originality

PASS

PASS, best of knowledge: The general quadratic Fourier/radical identity is textbook background and Iosevich–Koh compute scalar paraboloid coefficients over odd fields, but the exact Sylvester rank stratification on the noncommutative squaring graph, the even-characteristic affine shift and the complete multiplicities for all extension fields are additional algebraic calculations. A general quadratic-form lemma is a tool; without classifying B and the restricted quadratic phase it does not give the displayed spectral table. Matrix/Jordan-algebra equivalences remain a literature risk.

## value

PASS

PASS: The matrix-square graph is a natural polynomial subvariety of a finite additive matrix group. An exact Fourier support classification and singular-value distribution, with opposite asymptotic supported fractions in odd and even characteristics, is a motivated natural harmonic invariant rather than a renamed scalar paraboloid calculation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
