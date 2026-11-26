---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

The root-of-unity sum factors the normalized evaluation columns into residue classes k modulo n, each containing exactly k and k+n. Their two row vectors have the lengths specified by the two normalized rings, and the squared two-row minor is a positive constant times |rⁿ−sⁿe^{inθ}|². Thus the stated constant trace and phase-dependent determinant give the complete spectrum and the precise singular case. With fixed trace, every smaller root increases and every larger root decreases strictly as this minor increases, even if the two roots eventually coincide. Since there are finitely many modes, strict improvement survives the global minimum and maximum, yielding all four optima and strict uniqueness modulo 2π/n. In the Hardy case the block row Gram has diagonal (u_k,1), u_k=a_nr^{2k}, and determinant γ_nu_k. The branch derivatives are positive since the squared discriminant radical minus (u+1−2γ_n)² is 4γ_n(1−γ_n)>0. Hence the extreme modes are k=n−1 and k=0 as stated. The product formula L_−L_+=γu verifies the fixed-radius growth when u_{n−1}→0, as well as the large-c asymptotic of the limiting formula. Substituting r_n=e^{−c/n} gives the claimed finite limit with positive denominator, and both relevant roots tend to 1 as c↓0. The proof requires positive weights and regular polygons and uses a finite Hardy polynomial space, not the full Hardy space. The supplied script and output were inspected, not run: the 12 asymptotic trials check fixed r only, not the critical exponential sequence; that limit is established by the formulas.

## originality

PASS

The supported distinct contribution is the simultaneous four-objective finite weighted two-ring design coupled with its exact finite-Hardy boundary-scale conditioning law. The nearest indexed spectral optimum is for infinite Gaussian-Fock kernels; the nearest Hardy results differ in number of orbits, kernel, or optimized objective. Root-of-unity block reduction and the determinant argument alone are not claimed to be new.

## value

PASS

This design problem has a meaningful noise-sensitivity objective: a single rotation simultaneously improves both extreme singular scales as well as determinant for arbitrary positive monomial weights. In the finite Hardy case the exact law explains the difference between exponential loss at a fixed inner radius and finite conditioning when the radial gap scales as the reciprocal degree. It gives a design and quantitative threshold information, not just a determinant computation or an optimization claim for unconstrained sampling arrays.

The dated certificate retains the supplied scientific assessment, sources and limitations.
