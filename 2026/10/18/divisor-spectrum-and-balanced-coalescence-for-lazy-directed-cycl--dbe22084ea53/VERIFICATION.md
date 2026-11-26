---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

An independent finite-chain proof verifies the key separation step without any mixing or spatial independence assumption. Before collision the lifted separation D lies in {1,...,m-1}; the next change is B(Y)-B(X), has conditional mean zero by equal marginals, and can leave this interval only at 0 or m (both collision). If the pair chain had a closed irreducible class off the diagonal, D would be harmonic on that class and therefore constant by the maximum principle. Its first-coordinate projection contains every vertex since a supported advance is possible at every coordinate and the class is closed. Thus a constant positive separation d on that class forces every supported mask to agree at x and x+d for every x, i.e. d is a common nonzero period. A quotient with no such periods has no off-diagonal closed class and coalesces almost surely by finiteness. The period subgroup on the original n-cycle consists of the multiples of q=n/|H_mu|; the quotient masks are well-defined and inherit the same marginal. A new quotient period would lift to an original period not in H_mu, which is impossible. If q=1 synchronization on the quotient is immediate. Equivariance makes every original H_mu-coset map bijectively to an image coset under each composition. After all quotient paths coalesce in finite time almost surely, the original image is one full coset, with exactly one preimage from each original coset for each target. This proves both rank and equal deterministic cardinalities, including full-period and trivial-period cases. Full-support Bernoulli(p) bits on the quotient, repeated periodically, realize every divisor because a one-bit marker witnesses each nonzero shift when q>=2. All statements hold at n=2 and require iid maps in time and 0<p<1 as stipulated.

## originality

PASS

Grimmett–Holmes already pose the spectrum and class-cardinality questions and prove a divisor construction for complete uniform chains. Their theorems use a different transition family and do not give the common-period characterization or rule out all nondivisors even for their complete uniform setting. The surviving claim is the necessary-and-sufficient, law-by-law period criterion for every balanced stay/advance law on the directed cycle, and the resulting equal fiber sizes and complete spectrum.

## value

PASS

This answers two natural coalescence questions for a canonical sparse family from one checkable structural invariant: all and only divisor ranks occur, and each admissible law has explicit deterministic rank and class sizes. The necessity direction constrains every spatial dependence law, not just examples from a block construction or small-cycle enumeration. The interaction between harmonic separation and symmetry is substantively explanatory.

The dated certificate retains the supplied scientific assessment, sources and limitations.
