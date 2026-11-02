---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-30.md",
      "INDEPENDENT_AUDIT_2026-10-30.json"
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

PASS. Elementary symmetric recursion e_b=e_b(tail)+w_j e_{b-1}(tail) verifies the sequential fixed-cardinality weighted sampling exactly, while Newton log-concavity makes p_j(b) monotone in residual budget. For adjacent budgets, common uniforms produce ordered indicators until the unique extra inclusion, then budgets and subsequent indicators coincide, proving the exact before/at/after h product Q. Summing Q rows/columns follows from the two exact cut marginals. An independent uniformly randomized permutation of labels maps cuts to blocks; the elementary block-order identity sum_sigma product_t(prefix size)^(-1)=n/prod_i b_i yields the conditioned Ewens weight prod_i(b_i−1)!/c(n,k). Independent rational enumeration verified 240 row/column marginals through n=7; all n follows from the identities.

## originality

PASS

PASS, qualified and limited to the explicit pair-transition law. Gnedin–Pitman (2006) already gives the independent Bernoulli cut representation and discusses the one-split fixed-cycle-count problem; Borcea–Brändén–Liggett stochastic covering already implies abstract existence of adjacent coupling, so existence and Gibbs marginals are NOT new. The shared-uniform elementary-symmetric sampler with an individual Q_{n,r}(S,h) exact rational expression was not present in the inspected published statements. Generic conditional Poisson sampling algorithms may make this specialized formula implicit; this remains a substantive historical priority risk.

## value

PASS

PASS, with moderate scope. Adjacent-layer joint laws are natural missing data for conditional Ewens fragmentation, not determined by the known marginal distribution or mere abstract covering existence. This construction gives each rational transition coefficient and a simultaneous all-k explicit sampler for a canonical family, with a usable proof of positivity and correct marginals. It is self-contained even though a more general covering theorem already settles qualitative existence; no downstream grand theorem is asserted.

The dated certificate retains the supplied scientific assessment, sources and limitations.
