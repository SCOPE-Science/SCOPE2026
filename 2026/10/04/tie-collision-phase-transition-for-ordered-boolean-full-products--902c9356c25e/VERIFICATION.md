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

The bundled `verify.py` uses only the Python standard library. It computes ordered Bell numbers, signed and unsigned Stirling tables, the all-tuple profile \(T_d(n)=F_n^d\), and the inverse-Stirling injective profile \(I_d(n)\).

It verifies the forward Stirling transform for \(d\le5\), checks \(I_1(n)=n!\), and reproduces OEIS A101370 exactly from \(I_2(n)/n!\) through ten terms. It records the first ten \(d=3\) set-orbit values. As an independent finite route, it generates every weak order as a surjective rank vector for \(n\le4\), forms all Cartesian powers for \(d\le3\), tests directly whether any pair of indices is tied in all coordinates, and checks that these direct counts equal the inverse-Stirling formula.

Finally, for \(d=2,3,4,5\) it prints numerical ratios or scaled deficits through \(n=30\), showing the expected approach to \(e^{-(\log2)^2/2}\) at \(d=2\) and to \((\log2)^d/2\) after multiplying the \(d\ge3\) deficit by \(n^{d-2}\). These numerical checks are not used as a proof of the asymptotic theorem; that proof is the Bonferroni calculation in `RESULT.md`.

Replay command: `python3 verify.py`. Expected final line: `VERIFY_OK`.
