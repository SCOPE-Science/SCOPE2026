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

The reproducibility script is `artifacts/verify.py` (standard-library Python 3). Run it from the extracted package directory. It checks the complete list of Gaussian prime norms through \(113\) including split multiplicity, verifies all seven finite tail-product inequalities by exact `Fraction` arithmetic, checks each of the \(66\) split-prime anchors is a prime congruent to \(1\pmod4\), and checks every adjacent squared gap strictly satisfies \(q_{j+1}^2<2q_j^2\).

The remaining analytic step invokes Bennett--Martin--O'Bryant--Rechnitzer, Theorem 1.2, and the proof explicitly shows why this theorem yields a split prime between \(x\) and \(\sqrt2 x\) when \(x\ge8\cdot10^9\). This step is mathematical use of a published theorem, not a computational extrapolation. Euler factor normalization, the interval-filling lemma, the exact endpoint identity, and the ramified-prime decomposition are justified in RESULT.md. No independent audit or external certification has occurred.
