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

The two standalone Python 3 standard-library programs `verify_bipartite.py` and `verify_cycles.py` were executed against the embedded `certificate.json` file. Recorded reproducible outputs are `bipartite_output.txt` and `cycles_output.txt`.

The first program checks \(40320\) possible bipartition bijections and all \(528\) unordered pairs of the \(33\) valid matchings. The second independently enumerates matchings by exact-cover recursion and cycles by simple-path search; it finds \(24\) six-cycles and \(30\) eight-cycles before enumerating legal switches. The resulting full labeled pair lists agree with the certificate. Both check the three-hub structure and shortest-path assertions.

Canonical certificate SHA-256: `7594df583189eabc5ab8acb6feff960f57f872dfbeca09e3c79888614b332a33`.

Finite exhaustive computation establishes the stated claims on this fixed graph, not a general theorem for arbitrary \(GP(n,k)\). No probabilistic or incomplete search is used. Source novelty checks retain residual uninspected-literature risk.
