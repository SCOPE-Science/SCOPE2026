---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-24.md",
      "INDEPENDENT_AUDIT_2026-10-24.json"
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

The period-doubling fixed point has t_j=1-(nu_2(j+1) mod 2); occurrences of its prefix of length 2^n-1 are exactly B*k with t_k=1 and B=2^{n-1}, yielding return lengths B or 2B. For each dyadic offset D=2^r and n>=r+2, the number of D-steps per return is even, all but the last prefix-coordinate sums vanish, and the last is 1 by block-parity identity. Thus the return cocycle is exactly addition of e_{D-1} for every return. An explicitly recurrent reference bilateral point gives orbit-closure intersection with its fibre exactly {u,u+e_{D-1}}. The minimality/closure and uniform constant fibre-rank arguments partition all 2^D preimages into 2^{D-1} minimal sets each of rank 2. Independent direct-word enumeration tested 9286 return intervals for D=4,8,16. The all-r theorem uses the valuation and return-cocycle proof.

## originality

PASS

Kang and Jäger's accessible full arXiv paper proves these odd-block binary lifts are nonminimal and that finite permutative lifts decompose into finite minimal components of constant fibre ranks, but it does not supply the exact dyadic component numbers or rank two in the inspected theorem and proposition statements. The Resultary 2026 three-block formula concerns offset two, whereas this is all dyadic D>=4; taking repeated inverse images requires controlling a new return-permutation subgroup. Risk: a prior Toeplitz or odometer finite-extension theorem could encode the same count indirectly.

## value

PASS

Exact number and uniform fibre rank of minimal components are the canonical missing decomposition invariants after the known nonminimality theorem. The exponential 2^{2^r-1} count and explicit two-point fibre partition give a natural complete infinite-family classification, rather than an arbitrary finite sample.

The dated certificate retains the supplied scientific assessment, sources and limitations.
