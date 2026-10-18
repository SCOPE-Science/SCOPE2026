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
# Verification

**Method.** Using only Python 3 standard-library arithmetic, `verify.py` constructs the full Apéry set by Dijkstra's algorithm on residue classes modulo the smallest generator. This method is independent of the greedy presentations used in the proof. The script then checks the published Apéry formula, exact genus, conductor, strict Wilf number and displayed polynomial bound for every odd \(3\le m<2^n\), \(3\le n\le7\).

**Observed result.** All 119 semigroups and all 599039 Apéry-representative comparisons passed. For \(n=3,m=3\): \(k=4,M=24,g=334,F=651,e(c-g)-c=938\), polynomial lower bound \(328\).

**Reproduction.** With Python 3, execute `python3 verify.py` from the folder containing the extracted standalone file. It requires no third-party modules, network, or auxiliary files. A successful run prints two `PASS`/sample lines and raises no assertion errors.

**Mathematical limits.** Tests for finitely many parameters are not an infinite proof. The universal statement is established by the published Apéry theorem, greedy-digit restrictions and algebra in `RESULT.md`. Independent mathematical audit has not been performed.
