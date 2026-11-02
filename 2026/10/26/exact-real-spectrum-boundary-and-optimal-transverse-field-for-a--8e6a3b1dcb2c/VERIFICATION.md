---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-31.md",
      "INDEPENDENT_AUDIT_2026-10-31.json"
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

Reconstructed all eight-spin-spectrum eigenvalues from H/J with outer-exchange reflection: odd sector contributes ±q/2 and even sector det=(F(λ²;u,z)/64). Fresh independent SymPy construction of the 8×8 Pauli Hamiltonian checked this characteristic identity; the cubic-y discriminant equals 65536 D(u,z). For every z>0, exact identities D(0,z)>0, D(z,z)=z(1+4z)^3>0, D(z+1/4,z)<0 and u-leading coefficient +16, together with Descartes, give exactly two simple positive u roots and z<u_-<z+1/4<u_+. At u=0 the matrix is Hermitian and F roots nonnegative; for u>0, F(0)<0 prevents crossing y=0. Therefore y-roots remain positive until u_-, with an endpoint double positive root. For u_-<u<u_+ a nonreal pair appears; for u>u_+ continuity from large u, positive sum of roots and negative second symmetric sum force two negative y-roots, so not all λ are real. At z=0 direct factorization F=4y[(4y-1)^2-4u] gives p_c=1/2. The exact resultant Res_u(D,D_z) factors with only one positive field candidate, root of 3072z³+876z²+52z-3; initial negative slope and eventual growth force it to be the unique global minimum. Direct numerical spectra at six q values and four interior/exterior defect values independently corroborate, but are not used as a proof of the all-parameter conclusion.

## originality

PASS

Qualified best-of-knowledge novelty: the 2023 Muldoon–Joglekar primary paper defines the exact central-raising Ising model and the J/2 zero-field bulk threshold, and plots N=7 transverse-field single-defect thresholds. Its fully inspected main text confines the analytic derivation to h_z=0 and does not give the complete N=3 finite-field discriminant, all-real inequality or unique optimizing field. Generic cubic discriminant theory and EP machinery are old, but do not by themselves evaluate this 8-by-8 Hamiltonian. Two other closely named EP papers use non-equivalent perturbations. Targeted published-finding semantic searches and public literature search did not identify a stronger or equivalent statement; that search absence is not a priority certificate.

## value

PASS

The open three-spin Ising chain is the smallest chain with a genuine interior local nilpotent perturbation, a canonical finite test of localized non-Hermitian spectral control. Exact all-field real-spectrum boundaries answer a model-specific sharp question not answered by known numerical N=7 phase plots; unique optimizing transverse field and a strictly positive all-field defect floor distinguish it from a routine eigenvalue list or a zero-field parameter substitution. The joint polynomial sign/root and resultant classification is mathematically motivated and provides a reproducible exact small-system benchmark; no claim of a thermodynamic transition or paper-sized general theorem is required.

The dated certificate retains the supplied scientific assessment, sources and limitations.
