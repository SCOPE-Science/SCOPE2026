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
# Finite verification record

The graph has \(15\) duad vertices, \(15\) syntheme vertices and \(45\) incidence edges. The provided `verify.py` constructs it without external data, exhausts all perfect matchings, canonicalizes all simple eight-cycles, writes the complete `certificate.json`, and computes every flip and shortest-path distance. The following command was run successfully:

`python3 verify.py certificate.json`

The generated record includes \(288\) matchings, \(90\) eight-cycles, \(1440\) flip edges, \(288\) complementary two-factor types and \(288\) full shortest-path histograms. The console output is `python_output.txt`.

The separate thirty-vertex enumerator was compiled and executed successfully using:

`g++ -std=c++17 -O2 independent.cpp -o independent`

`./independent`

It verifies by independent matching enumeration and all-pairs comparison that every length-eight symmetric difference is a single eight-cycle, and independently computes the same distance distributions; see `cpp_output.txt`. A reachable-state count is not merely inferred from a partial sample: every one of the \(288\) enumerated vertices was used as a shortest-path source and all destinations were reached.

Verification is exact for the finite graph and specified exchange operation. It is not an independently conducted scientific audit, a proof for an infinite family, or a claim about other cycle lengths. No external validation was performed.
