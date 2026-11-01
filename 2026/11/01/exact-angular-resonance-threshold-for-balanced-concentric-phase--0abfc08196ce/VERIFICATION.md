---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-01.md",
      "INDEPENDENT_AUDIT_2026-11-01.json"
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

Let p(z)=sum_{k=0}^d a_k z^k. Its squared modulus on each radius r is a trigonometric polynomial with modes [-d,d]; a 2d-point regular ring DFT recovers every mode |k|<d and aliases only the conjugate top pair into 2r^d Re(a_d conj(a_0)e^{idφ}). Two rings give independent real linear equations in the same complex v=a_d conj(a_0) iff sin(d(φ2−φ1))≠0. With that condition all full-circle intensities on both radii are determined. If p,q have same two full-circle intensities, the rational R=p/q satisfies R(z)overline{R(r_j²/conj?)}=1 in the standard rational-reflection identity; eliminating j yields invariance of R#(w) under dilation r2²/r1²≠1, forcing rational R constant, then unit modulus. Zeros are handled as rational identities; p=0 gives q=0 since 2d>d sample zeros. When radii coincide, p=z−t and q=(t/r)z−r with t≠r have same full-circle modulus, not global phase. When angular sine vanishes, p=1+i exp(−idφ1)z^d and q=1−i exp(−idφ1)z^d have identical samples, not phase equivalents. These prove sharp iff for every d≥1, including vanishing coefficients. Source checker.py finite degrees 1–12 supports, does not replace analytic proof.

## originality

PASS

Best-of-knowledge: the exact new assertion was compared to its natural aliases, stronger/general results and selected primary literature, as well as the Resultary search. Known foundations are not claimed as new. Sources read and unresolved priority limitations are recorded explicitly. resonance.

## value

PASS

The determinant sin(dΔφ) exactly partitions a natural fixed-budget phase-retrieval design into universal and nonuniversal configurations, with concrete sharp obstructions. It is mathematically motivated by otherwise unresolved top Nyquist harmonic, and provides a design criterion rather than only an existence construction or numerical small-degree example.

The dated certificate retains the supplied scientific assessment, sources and limitations.
