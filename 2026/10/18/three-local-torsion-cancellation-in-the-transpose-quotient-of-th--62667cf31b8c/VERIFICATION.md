---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-19.md",
      "INDEPENDENT_AUDIT_2026-10-19.json"
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

Used original RESULT.md and exact verify.py/certificate.json, reconstructed all rook faces sizes 1..5: (25,200,600,600,120). From α(0;0,1)∧α(1;2,3)∧β(2,3;4), independently built 8-term Z and transposed signed 8-term cycle. Independently parsed the actual 60-term mod-3 chain W and 184-term cocycle φ; checked ∂W=Z+τZ exactly mod3, δφ=0 on all 600 four-rook faces, <φ,Z>=1, and pairings with τZ, transposed row01 and col01 are all 2 mod3. Independently computed exact F3 ranks ∂2=176 and ∂3=423, giving H2(F3) one-dimensional, proving τ acts −1 on the unique Z/3 via UCT and known H1=0. Each four-rook face belongs to uniquely one five-rook face, giving unit minor and free integral H3; reduced Euler −56 then rank56, given cited prior integral homology and connectivity. For transpose, signed fixed-face Lefschetz recurrence F5=0 yields trace zero and 28 +1 eigenrank; coinvariants over Z_(3) are exact since 2 invertible. Simply connected X and a fixed diagonal vertex yield π1 quotient=0 via Armstrong. Localized H3 only free rank28 implies a 3-local wedge of 28 S3 by Hurewicz/Whitehead. Does NOT assert integral wedge or no 2-primary torsion. Full rank/cocycle checks independently reimplemented, not trusted solely to log.

## originality

PASS

Shareshian–Wachs explicitly supplies the Z/3 class and side-preserving sign characters. Jonsson supplies an independent computer-free proof of the same torsion group. Those results do not supply transpose action, which is a nontrivial extension of the side-group sign character, or the ordinary orbit-space localized topology. A new concrete mod-3 boundary certificate determines it. The prior ordinary Betti and rational representation theory also cannot by itself fix torsion transposition. Best-of-knowledge original with noted earlier equivariant-homology search risk.

## value

PASS

The smallest 5×5 torsion chessboard complex is a natural boundary example in matching-complex theory. The sign of the non-side-preserving transposition controls whether 3-torsion survives under an actual topological quotient, and the exact 28-sphere 3-local answer is a substantial structural computation, not a normalization or a small numerical increment.

The dated certificate retains the supplied scientific assessment, sources and limitations.
