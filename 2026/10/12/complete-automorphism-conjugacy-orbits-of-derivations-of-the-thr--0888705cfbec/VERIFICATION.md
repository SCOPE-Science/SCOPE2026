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

# Reproduction and boundaries

Run `python verify.py` with Python 3 standard library from the package directory. It independently enumerates bracket-preserving automorphisms and all derivations as full matrices over \(\mathbb F_2\) and \(\mathbb F_3\), then enumerates all actual conjugacy orbits and checks predicted orbit sizes over \(\mathbb F_2,\mathbb F_3,\mathbb F_4,\mathbb F_5\). The end marker is `VERIFY_OK`. The extension field uses the irreducible relation \(\alpha^2+\alpha+1=0\). Direct enumeration was run successfully and gives counts \(9,16,25,36\) orbits, respectively. These finite tests do not prove the all-field statement; the proof is the symbolic conjugation classification in `RESULT.md`. No external audit has been conducted.
