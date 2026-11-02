---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-27.md",
      "INDEPENDENT_AUDIT_2026-10-27.json"
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

PASS. For commuting affine idempotents f_i, the idempotent product P fixes P(0) under each f_i, establishing a common fixed point without assuming one. Translating it to zero gives commuting linear projections A_i and orthogonal Boolean idempotents E_sigma whose images form a unique labelled direct-sum decomposition. The common fixed subspace is V_(1,...,1), so affine shifts contribute exactly q^(n-a_1) and stabilizer q^(a_1)*product(GL_(a_sigma)). For fixed q,k, log_q of each weight is (1-1/2^k)(n^2+n)-sum(delta_sigma^2)-delta_1; GL product factors have uniform finite bounds, and a summable discrete Gaussian majorant on the zero-sum deviation lattice proves the stated theta asymptotic and total-variation convergence via dominated convergence. Taking the ratio to k independent single-retraction counts gives gamma_k=k/2-1+2^-k. Independent direct function-table enumeration for F_2^2 recovered 17 idempotent affine maps, 121 ordered commuting pairs, and 617 ordered commuting triples. These finite cases corroborate, but do not prove, the fixed-arity limiting theorem; extension-field and further finite checks in repository were read but not treated as independent proof.

## originality

PASS

PASS, best-of-knowledge. Simultaneous eigenspace decomposition is classical. The audited additional statements are the affine translation-fibre census, all-k orbit/stabilizer formulas, joint-rank discrete-Gaussian limit, and sharp periodically weighted commutation probability. Inspected primary results on unrestricted commuting matrices in finite fields do not imply the joint affine-idempotent strata or the displayed limit without additional specialization and proof; found no identified stronger theorem covering all components. Boolean-module counting is a notable prior-method risk.

## value

PASS

PASS. Finite affine retractions are natural idempotents of a transformation monoid, and the compatibility constraint is pairwise composition commutativity. The result resolves not a tiny instance but complete labelled-orbit and rank spectra for arbitrary n,k, and an exact asymptotic probability with residue-dependent theta multiplier at fixed field and arity. These are substantive structural statistics not mechanically recoverable from single-retraction enumeration; the standard simultaneous diagonalization is properly attributed as input.

The dated certificate retains the supplied scientific assessment, sources and limitations.
