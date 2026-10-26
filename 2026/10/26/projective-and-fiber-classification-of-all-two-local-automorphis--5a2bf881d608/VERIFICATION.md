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

# Reproduction and limits

Run `python3 check_2local.py` with Python 3.8 or later; only the standard library is used. Successful execution prints `HEISENBERG_TWO_LOCAL_OK` after the displayed checks. The actual packaged script was executed and returned this success marker.

For the prime field \(\mathbb F_2\), the checker constructs all \(24\) genuine Lie automorphisms of the eight-element Heisenberg Lie algebra, enumerates their \(11\) orbits on ordered pairs, then checks all \(8!=40320\) bijections against exact orbit preservation. The \(48\) that pass are exactly the \(48\) independently generated classification maps, a complete finite-case check.

For \(\mathbb F_3\), all \(432\) ordinary automorphisms and \(14\) ordered-pair orbits are constructed. All \(729\) ordered-pair conditions are tested for each of \(120\) pseudorandom parameterized maps. For the genuine extension field \(\mathbb F_4\), defined by adjoining a root of \(u^2+u+1\), the checker enumerates all \(2880\) automorphisms and \(17\) pair orbits; it tests all \(4096\) ordered-pair conditions for \(100\) parameterized maps. A fixed seed makes the randomized cases reproducible.

The general finite-field formula and arbitrary-field classification are established by the proof in `RESULT.md`: no finite test is presented as an infinite certificate. The literature comparison does not establish absolute publication priority. The independent audit is not performed.
