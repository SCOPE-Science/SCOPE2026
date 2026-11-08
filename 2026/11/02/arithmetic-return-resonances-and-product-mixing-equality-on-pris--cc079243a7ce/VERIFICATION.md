---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-06.md",
      "INDEPENDENT_AUDIT_2026-11-06.json"
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

Adjacency of C_n square K_2 has branches c_k±1, c_k=2cos(2pi k/n). Cesaro spectral averaging gives R_n=(4n²)^-1 sum multiplicity². The cross-branch equation a-b=2 for cyclotomic cosine sums forces nonnegative conjugates of the algebraic integer a; the trace mu(m) and integral norm force a in {0,1,2}, and the only collisions require 4|n (a,b)=(2,0),(0,-2) or 6|n (1,-1). Multiplicity-squared increments are +8 each, proving R_n=1/n-(1+[2|n])/(2n²)+2([4|n]+[6|n])/n². Schur product of merged orthogonal spectral projectors proves product-mixing PSD inequality, with strict positive diagonal excess exactly in resonant cases. Independent direct spectral multiplicity enumeration for n=3..84 agrees exactly; it does not establish infinite collision exclusion.

## originality

PASS

Godsil 2011 supplies spectral average mixing, and Godsil–Guo–Sobchuk 2019 Lemma 4.2 supplies the Cartesian PSD product inequality. The all-prism equality criterion controlled by divisibility by 4/6 and exact diagonal excess require the cyclotomic resonance classification not supplied there.

## value

PASS

An all-size equality characterization for a general known matrix inequality is mathematically natural; two distinct cyclotomic resonances provide exact return probability and quantify how product separability fails.

The dated certificate retains the supplied scientific assessment, sources and limitations.
