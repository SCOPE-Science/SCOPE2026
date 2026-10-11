---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-05.md",
      "INDEPENDENT_AUDIT_2026-10-05.json"
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

The reduction modulo the Sylvester commutator is correct. For \(A=J_2(0)\oplus J_1(0)\), \(AX-XA\) has exactly the four effective entries used in the proof, so every matrix in the assigned cell is equivalent for both minima to \(\operatorname{diag}(\tau,0,\kappa)\), with \(\tau=a+b\) and \(\kappa=c\). If \(\tau\kappa\ne0\), the first/second/third column dependence argument forces Sylvester residual rank at least two, while \(X=0\) gives rank two. The zero and one-nonzero cases give ranks zero and one. Roth's theorem identifies the common zero case for \(\gamma\), and the displayed invertible \(P_0\) gives a rank-one intertwiner defect after normalization whenever both invariants are nonzero. The finite-field strict count \(q^4(q-1)^2\) follows from three free off-diagonal entries, \(q(q-1)\) choices with \(a+b\ne0\), and \(q-1\) nonzero choices of \(c\).

## originality

PASS

The complete Shi--Zhang--Zhang primary paper proves only the normalized point \(C=\operatorname{diag}(1,0,1)\), with \(\alpha=2\) and \(\gamma=1\), and closes by naming a more precise characterization of strictness as a natural remaining problem. The audited theorem classifies a six-dimensional linear cell containing that point and gives its exact equality/strictness boundary over every field. Resultary returned the assigned finding as the exact hit and no implication-equivalent prior classification. Ferrante--Wimmer supplies sufficient spectral equality conditions, but the repeated zero Jordan type here is outside those hypotheses.

## value

PASS

The theorem resolves a natural local classification problem raised by the first minimal counterexample: it shows the phenomenon occupies a Zariski-open locus in a natural commutator cell rather than an isolated point, identifies the exact equality boundary, and gives a finite-field density count. This is a structural boundary result, not a mere re-evaluation of the original example.

The dated certificate retains the supplied scientific assessment, sources and limitations.
