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

# Checks and boundaries
The standalone `verify.py` reconstructs primitive Pythagorean triangles in two independent ways: Euclid's coprime/opposite-parity parameters, and coprime odd factors of the unique odd leg. For each \(k=2,3,4\) it compares the complete sorted triples below five hypotenuse bounds, including \(10^6\). Expected high-bound counts are \(112912,147134,155649\), respectively. The script stops with an exception if any discrepancy appears; passing the executable regression does not imply the asymptotic.

The proof of the infinite result uses an exact Euclidean/odd-factor bijection, local residue enumeration, fixed-modulus lattice-point counting with a sector boundary error, and a tail estimate uniform enough to let the prime cutoff tend to infinity after the hypotenuse bound. The residue exclusions are disjoint: both coordinates divisible by the prime, or exactly one coordinate divisible by its \(k\)-th power. The factor \(1/4\) at the prime \(2\), the sector area \(\pi X/4\), and \(\prod_{p>2}(1-p^{-2})=8/\pi^2\) determine the normalization.

The result does not prove an explicit error bound, a statement for exponents increasing with \(X\), or that no inaccessible prior theorem covers the density. No external or independent audit was performed.
