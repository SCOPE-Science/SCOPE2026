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

For n agents with one common strict ranking and uniform bistochastic matrix U=(1/n), Dec-EF of each ordered pair is equivalent to Pr(P(i)>P(j))=1/2. Marginals require at least n supported permutation matchings. If exactly n, all their weights=1/n and odd n cannot make an integral multiple of 1/n equal 1/2. The n+1 impossibility follows because every supported weight<=1/n and for each row exactly one rank is repeated, so exactly two globally sub-1/n weights must correspond to permutations agreeing in every row, contradicting their distinctness. For even n=2m, pair n cyclic shifts of q=(0,...,m-1,2m-1,...,m) through q(k+m)=n-1-q(k) to balance every pair with support n. For odd n>=3, forward cyclic shifts and their distinct rank reversals yield balanced uniform lottery on 2n supports. At n=3, direct six-column marginal equations leave one parameter, and fairness sets it to 1/6 on every permutation, giving unique s(3)=6. Independently recomputed exact 6-variable rational balance system rank 6 and unique uniform weights; boundary n2 and n3 verified. The unknown exact odd n>=5 minimum is explicitly NOT claimed; n+2<=s(n)<=2n only.

## originality

PASS

Kawase–Suksompong–Sumita–Yokoi (arXiv:2604.16973) introduced Dec-EF and exhibited six-way uniform decomposition for n=3, but their inspected existence theorems do not establish uniqueness of the six-way lottery, minimum n for every even size, or the impossibility of n+1 supports. Li–He–Li (arXiv:2609.35192) concerns larger-agent decomposition existence and computational hardness; only its abstract could be accessed, so the complete source remains a named priority risk, not a decisive rejection. Best-of-knowledge pass on identifiable support-optimality and parity structural statements.

## value

PASS

Sparsity of lottery support is a natural operational complexity of implementing a fractional assignment. The exact even-size support optimum, impossible n+1 for uniform matrices, and uniquely forced n=3 fair lottery identify a nontrivial parity obstruction within the existing Dec-EF model, without overclaiming odd-size exact optima beyond n=3.

The dated certificate retains the supplied scientific assessment, sources and limitations.
