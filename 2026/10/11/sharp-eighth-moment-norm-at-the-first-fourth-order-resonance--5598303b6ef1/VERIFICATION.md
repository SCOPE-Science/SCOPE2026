---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-13.md",
      "INDEPENDENT_AUDIT_2026-10-13.json"
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

For F=a+bz+cz^4 on normalized circle, Parseval of F^4 gives the sole nontrivial degree-four collision between b^4 and 4a^3c at frequency 4; phase maximization is exact and forces arg c+3 arg a-4 arg b=0. The homogeneous nonnegative-coefficient eighth moment reduces to the explicit rational Q(x,r)/(1+x(1+r^2))^4, x=|a|²/|b|², r=|c|/|a|. Independent enumeration of multinomial exponent triples found exactly the same single collision. Independent SymPy differentiation and exact polynomial resultant factorization reproduced two stationary polynomials and the degree-21 resultant; Sturm count gives exactly four positive r roots. Recomputed local positive candidate (x,r)=(0.988015384889518...,0.987599119759780...) and K^8=7.989075749695772..., K=1.296618... . Full source proof/certificate selects the sole positive stationary pair; all two-frequency boundaries have eighth-power ratio at most 35/8 while the equal-coefficient interior witness gives 647/81>35/8. The all-complex-coefficient quantifier is handled by phase alignment. Algebraic certification, not numerical optimization alone, is essential.

## originality

PASS

The sharp arbitrary-amplitude L8/L2 norm and all non-flat optimizing magnitudes for spectrum {0,1,4} were not covered by phase-only unimodular three-frequency moment formulas, earlier sharp {0,1,2} Fourier norm, or independent Steinhaus inequalities. The first relation 4·1=3·0+1·4 is genuine fourth-fold alias; lower convolution moments have no additive collisions. Precise residual risk of older equivalent finite-spectrum optimization remains.

## value

PASS

The spectrum {0,1,4} is naturally singled out as the first three-point integer spectrum where coefficient phases first interact in the eighth moment but not earlier moments. The sharp induced L2-to-L8 constant and non-flat extremizer quantify a motivated fourth-order additive resonance beyond a known fixed-amplitude phase test. The exact self-contained finite-spectrum norm is an intrinsically reusable invariant, not an arbitrary set substitution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
