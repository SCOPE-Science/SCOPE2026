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

The entire proof is reconstructed for arbitrary n>=3 and common zero-insertion vector z in all n+1 original gaps. Writing I={a+1,...,b}, J={c+1,...,d}, r=b-a, s=d-c, and N=n+sum(z), the two resulting circular two-one words are rotations exactly if R=S or R+S=N, where R=r+sum_I(z), S=s+sum_J(z). The two linear coefficient equations give feasible minimal costs |r-s| and |n-r-s| with exactly the stated disjoint/nested/overlap feasibility; each inserted zero can improve its equation by at most 1. For strict nesting r+s lies between 3 and 2n-3; outside nesting |r-s|<=n-3, yielding global maximum n-3. Equality cases are exhausted by nested interval lengths {1,2}, {n-2,n-1}, or disjoint {1,n-2}, with 4(n-2)+4+4=4n ordered maximizers. The n=3 and n=2 boundary cases are separately covered. Independently constructed and tested literal expanded words under all weak compositions up to the predicted minimum for every ordered pair n=3,4,5,6, 9+36+100+225=370 pairs. Exact cost histograms were {0:9}, {0:20,1:16}, {0:50,1:30,2:20}, {0:81,1:84,2:36,3:24}; all agreed. The n>=3 proof is infinite and does not rely on this finite test.

## originality

PASS

The exact weight-two minimum zero-only padding cost, sharp n-3 worst case, 4n ordered maximizers, and three equality geometries go beyond published existence and general bounded constructions, best of knowledge. These statements are not inferred from lack of search matches; the directly relevant primary theorem and its explicit optimal-length open question were read.

## value

PASS

Weight two is the first nontrivial fixed-weight cyclic equalization case: unlike qualitative parity/weight feasibility, the exact minimum number of shared zero insertions measures the cost of a natural constrained string operation. The theorem supplies an all-length optimum and a rigid count/geometric classification of worst inputs, a reusable benchmark for broader open optimum-length questions. This is neither a mere restatement of equal-weight existence nor an arbitrary one-off sample.

The dated certificate retains the supplied scientific assessment, sources and limitations.
