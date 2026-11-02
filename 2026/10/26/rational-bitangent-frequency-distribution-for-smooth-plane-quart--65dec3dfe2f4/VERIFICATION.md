---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-30.md",
      "INDEPENDENT_AUDIT_2026-10-30.json"
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

There are exactly 2^15−1=32,767 nonzero ternary quartic forms over F2. The natural GL_3(F2)=PGL_3(F2) action has 168 matrices. Geometric smoothness is equivalent to the ideal (F,F_X,F_Y,F_Z) being unit after dehomogenizing each of the three coordinate charts, verified via Groebner over F2 (including algebraic-closure points). For each of seven F2-lines, the binary quartic restriction has divisor twice a degree-2 divisor exactly when its u³v and uv³ coefficients vanish. Read both packaged independent orbit/Groebner/restriction algorithms and original 279-row orbit file. Reconstructed independent full finite enumeration in a separately coded SymPy pipeline (not by executing opaque repository scripts), exhaustively partitioned all 32,767 forms into 279 orbits, found 78 smooth orbits of total weight 10,920 and independently reproduced the exact histogram b=0:3072,1:5278,2:2352,3:105,4:112,7:1. Orbit action, smoothness and all seven line restrictions are exact symbolic computations, not statistical sampling. Smooth quartic irreducibility excludes an entire line component; hyperflexes satisfy the square criterion and are included.

## originality

PASS

Qualified PASS only for the explicit coordinate-equation-weighted six-bin F2 rational-bitangent frequency table, not for quartic isomorphism classes or allowed geometric bitangent counts. Nart–Ritzenthaler (2003/04) fully classifies the curves up to F_q-isomorphism and Frobenius bitangent descent, so it strongly supplies raw ingredients for this table; Theorem 3.1 visibly tabulates Newton polygon class counts, not rational-line frequency weights. Additional orbit-stabilizer and line-restriction computations are necessary to reach the six exact values. The table may be derivable from prior stronger normal forms and could appear elsewhere; that is a material priority risk, not claimed absent from all literature.

## value

PASS

The number of F2-rational bitangents of a smooth quartic is a natural arithmetic/geometric invariant. The full equation-weighted distribution across every smooth ternary quartic answers an exact finite-field frequency question, including rare strata and zero-bitangent forms. Exact exhaustive certificates and independent cross-reconstruction make the table reusable; it does not purport to supersede known isomorphism or geometric classifications.

The dated certificate retains the supplied scientific assessment, sources and limitations.
