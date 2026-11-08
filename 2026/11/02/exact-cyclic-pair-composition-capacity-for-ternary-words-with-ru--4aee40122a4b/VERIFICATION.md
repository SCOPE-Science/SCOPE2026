---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-04.md",
      "INDEPENDENT_AUDIT_2026-11-04.json"
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

The complete general-q criterion follows by contracting runs of length 1 or 2 into a closed switching walk: the off-diagonal multigraph is nonempty and connected on active vertices, all degrees even, and loops h_ii do not exceed d_i/2. Conversely an Euler circuit has d_i/2 visits at vertex i, of which any h_ii may be doubled, proving all lengths including cyclic n=2. For q=3 the three cross-multiplicities have common parity eps and are uniquely x=2u+eps,y=2v+eps,t=2w+eps; the loop bounds give an exact positive generating sum. An independent symbolic common-denominator reduction recovered the stated z²P/[(1-z)^6(1+z)^3(1+z²)^2(1+z+z²)^2]. Nonzero factors at third/fourth roots enforce least period 12, with leading coefficient [5/96]/5!=1/2304. Enumeration of all ternary words through n=8 corroborated the analytic all-length proof.

## originality

PASS

The core directed DNA profile and Euler/flow machinery are established; an unordered cyclic adjacent-composition histogram under the length-two run ceiling has additional degree-parity and diagonal-loop constraints. The explicit ternary period-12 capacity is not a directly named or implied evaluated table in inspected primary sequence-profile work. Risk remains of unindexed undirected multigraph flow enumeration equivalences.

## value

PASS

An exact zero-error distinguishability capacity under two meaningful experimental limitations (unoriented pair compositions and cyclic homopolymer ceiling two) gives practical benchmark cardinalities, nontrivial 12-periodic structure and a complete all-alphabet constructive feasibility test. Not a trivial restatement of generic Euler circuits.

The dated certificate retains the supplied scientific assessment, sources and limitations.
