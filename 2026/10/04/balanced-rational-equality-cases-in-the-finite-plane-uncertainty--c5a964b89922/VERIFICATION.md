---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-04.md",
      "INDEPENDENT_AUDIT_2026-10-04.json"
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

Balanced equality forces \(|S|=|X|=2(p-1)\). For rational-valued \(f\), cyclotomic Galois symmetry makes \(X\setminus\{0\}\) a union of punctured dual lines; the principal character cannot occur because \(2p-3\) is not divisible by \(p-1\). Thus \(X\) is exactly two punctured one-dimensional subspaces. After a linear coordinate change, Fourier inversion gives \(f(x,y)=U(x)+V(y)\) with both means zero. The zero-set size is \((p-1)^2+1\). The multiplicity rearrangement bound \(\#\{U+V=0\}\le(p-1)^2+1\) is correct, and equality forces the two value-multiplicity patterns to be \((p-1,1)\). The mean-zero equations then force opposite values on two affine coordinate lines, giving exactly a scalar difference of two nonparallel affine-line indicators. The converse Fourier-support calculation and the projective count \(\binom{p+1}{2}p^2\) are correct. The finite verifier is supplementary only.

## originality

PASS

Biró–Lev prove the sharp finite-plane inequalities, use the same rational Galois invariance, and explicitly exhibit differences of nonparallel line indicators as sharp examples; the inspected material does not classify all balanced rational sharp cases. Bonami–Ghobber classify functions attaining the minimum possible Fourier support at a prescribed spatial support size, a different extremality problem: for \(|S|=2(p-1)\) the balanced case has \(|X|=2(p-1)\), not the minimal spectrum size addressed by their theorem. Resultary returned only the assigned record as the exact balanced-rational rigidity hit. The multiplicity-rigidity step is therefore not covered by the closest primary results.

## value

PASS

Rigidity of all rational balanced extremizers for a sharp two-dimensional uncertainty inequality is a natural equality-classification problem. The result upgrades a known construction to a complete all-prime theorem and gives an exact projective census, so it is more than a routine restatement of the inequality.

The dated certificate retains the supplied scientific assessment, sources and limitations.
