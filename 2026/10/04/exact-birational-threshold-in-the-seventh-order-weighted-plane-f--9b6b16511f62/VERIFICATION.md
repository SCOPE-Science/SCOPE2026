---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-04.md",
      "INDEPENDENT_AUDIT_2026-10-04.json"
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

For even n>=2 the weights a=n²-1, b=n²+1 and c=2n³ are pairwise coprime, and the degree-zero character lattice ar+bs+ct=0 has the displayed primitive basis u=(b,-a,0), v=(-n,-n,1). For degree-m monomials, D=x-y and T=x+y+2nz satisfy m=n² T-D, so admissible D-levels differ by 2n² and a repeated level costs another 2n³. The feasibility cost is f(D)=n²|D|-D. Three distinct D-levels below the proposed threshold are impossible because the extreme-level cost is at least 2(n⁴-1), which exceeds M=(n+1)(n³-1). For two adjacent levels, optimizing the repeated lower level gives D=-n²+n+1 and common cost M; repeating the upper level is strictly more expensive. At m=M the three stated monomials have exponent differences exactly u and v, so the torus map generates the full character lattice and is birational. Independent symbolic checks reverified the two adjacent-level identities and 2(n⁴-1)>M. Bie's primary source independently verifies mld(X_n)=1/n.

## originality

PASS

The exact same family is treated in Bie's current primary paper. Theorem 10.2 computes its discrepancy, volume and threshold data, but Remark 10.4 gives only the general necessary lower order epsilon to exponent negative seven halves, explicitly says this is not a calculation of the actual birationality threshold, and Section 10.4 asks for that threshold to clarify the gap with the sufficient epsilon to exponent negative nine halves bound. The audited formula M=n⁴+n³-n-1 therefore fills an expressly identified gap on the source family. Resultary searches found the assigned result but no prior exact threshold formula or implication-equivalent theorem.

## value

PASS

The result answers a specific open quantitative question posed for the sharp seventh-order family and resolves the source's 7/2-versus-9/2 gap there with the exact exponent 4 and exact first degree. An exact birational threshold in the extremal weighted-projective family is a natural invariant with direct relevance to the effective-birationality problem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
