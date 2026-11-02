---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-28.md",
      "INDEPENDENT_AUDIT_2026-10-28.json"
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

The Hadamard graph has intersection array {n,n-1,n/2,1;1,n/2,n-1,n}. From the five adjacency sectors n, sqrt(n),0,-sqrt(n),-n with multiplicities 1,n,2n-2,n,1, the distance-j eigenvalues are (1,n,2n-2,n,1), (1,sqrt(n),0,-sqrt(n),-1), (1,0,-2,0,1), (1,-sqrt(n),0,sqrt(n),-1), and (1,-n,2n-2,-n,1). Weighted d^p eigenvalues yield exactly p<=1 and the two nontrivial inequalities. Centered Gram rank subtracts equality-sector multiplicities, including the n=4 Hamming special case. Exponential eigenvalues factor into (1-z²)(1±sqrt(n)z+z²), (1-z²)², and (1-z)²(1-(n-2)z+z²); n-2>=sqrt(n) makes the last the binding condition, leading to arcosh threshold. Distinct embedded points ensure strict PD of Gaussian powered distance for positive scale. Independently reconstructed Sylvester Hadamard graphs n=4,8,16 and numerically matched spectral sectors.

## originality

PASS

Best-of-knowledge specific comparison finds no demonstrated prior theorem covering this exact final claim; sourced close comparisons and residual priority risks are explicit, and unsuccessful search is not treated as proof of priority.

## value

PASS

Sharp conditional-negative-type exponents and covariance cutoffs on a canonical infinite distance-regular graph family are motivated metric-embedding and kernel-positivity invariants. Multiplicity-aware endpoint rank losses provide more information than the general spectral algorithm alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
