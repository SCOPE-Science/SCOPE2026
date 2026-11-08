---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-06.md",
      "INDEPENDENT_AUDIT_2026-11-06.json"
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

For each left-permutative rule f(a,b,c)=a XOR g(b,c), invert the left bit given output d and the next pair (b,c): T_{g,d}(2b+c)=2(d XOR g(b,c))+b. Cyclic closure of the n-target inverse recurrence equals a fixed point of its word composition Φ; closure after repeating the target m times is equivalent to a fixed point of Φ^m, so the minimum m is the shortest cycle length of a four-element transformation. Independently enumerated all 16 complete two-generator transformation monoids and all reachable augmented states including length mod 6, weight parity, both uniform flags and nonemptiness. Every reachable descriptor obeyed the exceptional-language claims, which thereby cover arbitrary word lengths (not merely words shorter than a cutoff). Rule 30 triple lift arises only for 1^n with 3 not dividing n; Rule 90 quadruple lift iff length and weight odd; Rule 165 quadruple lift iff length odd and weight even. Both composition conventions and independent original forward-ring comparisons were inspected; my new independent BFS verifies a finite closure sufficient for every length.

## originality

PASS

Known surjective-CA preimage-period algorithms and linear cellular automata are acknowledged. The assessed incremental claim is one simultaneous explicit all-output classification of all 16 left-permutative radius-one rules, including four nonlinear uniform-word triple-lift exceptions and the exact linear odd-parity fourfold cases. The accessible closest primary postprint develops general de Bruijn algorithms and linear bipermutive cases but, in the inspected sections, does not state or imply this compiled exception classification. Best-of-knowledge PASS, not an absolute historical novelty certificate.

## value

PASS

Periodicity of a predecessor after enlarging a specified cyclic ring is a natural finite-state reachability invariant not determined by bi-infinite surjectivity. A sharp universal fourfold bound, exact rule partition and regular all-length exceptional languages supply structural information across the complete 16-rule family and identify the qualitatively different nonlinear period-3 versus linear period-4 obstructions; this is more than a single algorithm execution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
