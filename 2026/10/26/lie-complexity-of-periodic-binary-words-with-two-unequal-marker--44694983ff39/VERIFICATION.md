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

# Reproducibility and verification

Run \(\texttt{python3 verify_lie.py}\) from the extracted package directory with standard Python 3; no third-party packages are needed. The verifier constructs each periodic word explicitly, enumerates all distinct factors beginning at every phase, obtains the canonical lexicographically least cyclic representative of each, and checks whether **all** cyclic rotations are present. It compares these whole factor-class sets against the theorem's predicted representatives for \(b=1,\ldots,19\), \(d=b+1,\ldots,27\), and \(n=1,\ldots,3p+4\). The exhaustive finite comparison has \(28{,}766\) parameter/length cases.

It then directly enumerates all admissible unequal-gap pairs at each primitive period \(p=5,\ldots,99\), computes the spectrum and first-period mass for each, and confirms the stated exact maximum and all maximizing gap parameters. Further independent arithmetic checks cover all tested \(1\le b<d\) with \(b\le39\), \(d\le49\), establishing the predicted mass and threshold in that finite range.

Expected successful output (reproduced by executing the packaged source):

\(\texttt{VERIFY\_OK complete\_necklace\_sets=28766 sharp\_length\_extrema=5..99 exact\_mass=true peak\_transition=true}\)

The universal statements follow from the phase-rigidity and zero-count arguments in RESULT.md; no finite enumeration is claimed to establish them. These checks do not constitute an independent audit. Potential unindexed equivalent earlier literature remains a known originality risk.
