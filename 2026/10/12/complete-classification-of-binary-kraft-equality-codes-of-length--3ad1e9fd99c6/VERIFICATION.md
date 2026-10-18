---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-16.md",
      "INDEPENDENT_AUDIT_2026-10-16.json"
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

For a short layer S subset of eight 3-bit words with 1<=a=|S|<=7, Kraft equality forces b=16-2a four-bit words. Every unordered candidate is reached once by choosing S and b distinct four-bit words; sum_a C(8,a)C(16,16-2a)=1,901,636. A fresh independent C++ complete enumeration implemented the Sardinas-Patterson remainder-state reachability recurrence, not the submitted program, over all candidates. It reproduced unique-decipherability counts 16,56,112,140,116,56,16 (512 total), 4 exceptional neither-prefix-nor-suffix cases at a=5, and the exact complement/reversal orbit; prefix-free and suffix-free counts each equal sum_a C(8,a)=254. Prefix/suffix intersections are impossible because the three-bit de Bruijn graph is strongly connected. The SP finite remainder-state equivalence is valid for all these codes, so this is exhaustive, not a sampled experiment. Only the restricted length profile is proved; the infinity of deciphering delay uses classical Schützenberger finite-maximal-code theory, not novel proof.

## originality

PASS

Classical Sardinas-Patterson and Kraft-McMillan determine the decision procedure and candidate-space constraint but not this completed mixed-length saturated census. Woryna 2016 gives general length-sequence bounds and exact small three-word cases; its detailed statements do not imply this profile, which permits many words of both lengths. Resultary semantic search found different alphabet/blocklength/code criteria, not a theorem implying 512 or the four non-prefix/non-suffix exceptions. A prior unindexed exact table is residual risk, not assumed absent.

## value

PASS

Uniquely decodable Kraft-equality codes are a natural extremal family, and the first mixed 3/4-length binary profile asks how many maximal codes are nonprefix. The exact 512 code census and four exceptional word sets separate the classical obvious prefix/suffix subclasses from genuinely nonprefix codes; that is a reproducible natural finite classification rather than a named parameter substitution or isolated sample.

The dated certificate retains the supplied scientific assessment, sources and limitations.
