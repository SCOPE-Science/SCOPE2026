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

For any finite A⊂Z, Parseval turns the fourth power L⁴ norm into n²+2Σ_{h>0}|C_h|². The diagonal of E=Σ|C_h|² is binomial(n,2); independent Haar characters make every off-diagonal term mean zero. For positive h and distinct correlation start points x<y, let d=y−x. The exponent vector is (+ at x+h and x+d; − at x and x+d+h). If d=h it is the unique 3-term progression character (−1,2,−1) and its conjugate; each counts 2 in Var(E). If d≠h it is a four-distinct equal-sum character, and (d,h) versus (h,d) are its only two occurrences; the conjugate pair contributes 8 in Var(E). Thus Var(X)=4(2T+8Q)=8T+32Q; every nontrivial B₂ collision in integer support is of one of these two forms. Independently enumerated exponent vectors for all 255 nonempty subsets of {0,…,7}, comparing coefficients exactly with T,Q, not as replacement for the proof. Conjugates are distinct and no torsion occurs on Z.

## originality

PASS

Neuwirth’s three-frequency Sidon constant concerns sup norm extremization, not random L⁴ fourth-power variance; Choi–Mossinghoff and Borwein–Lockhart treat full consecutive coefficient supports and average/asymptotic moments, not finite arbitrary sparse A. The published Resultary exact parity formula on A={0,…,n−1} follows as a special case of this T(A),Q(A) theorem; the implication is from the assigned claim to prior work, not conversely. Its phase-independent rigidity for all Sidon B₂ sets and two collision weights for every finite A supply genuinely broader additive structure.

## value

PASS

The formula identifies precisely which additive relations control random Fourier fourth-power norm fluctuations for EVERY finite integer support, distinguishing 3-point progressions (weight 8) and 4-point pair-sum collisions (weight 32). The exact zero-variance iff B₂ rigidity is a natural independent structural characterization rather than a small finite census, and explains support sensitivity invisible in n-only random-polynomial results.

The dated certificate retains the supplied scientific assessment, sources and limitations.
