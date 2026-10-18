---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-13.md",
      "INDEPENDENT_AUDIT_2026-10-13.json"
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

On real ℓ²(Z) let d0=1, d±n=n, D=diag(dj), u±n=e^{−3n²/2}, u0 chosen to normalize, v=Du, κ=⟨v,u⟩. The nonpositive self-adjoint A0=−D+(v⊗v)/κ has a simple top 0 eigenvalue at u; compact resolvent plus a spectral gap imply e^{tA0}→u⊗u in norm. Antisymmetric q_n=(e_n−e_{−n})/√2 are A0 eigenvectors with eigenvalue −n. Add B=Σ δ_n q_n⊗q_n, δ_n=n e^{−2n²}, then A=A0+B remains real self-adjoint nonpositive compact-resolvent and e^{tA}=e^{tA0}+Σ e^{−nt}(e^{δ_nt}−1)q_n⊗q_n. The Dyson expansion bounds a_n(t)=⟨e^{tA0}e_n,e_−n⟩ by n²e^{−3n²}(e^{2t}−1), using b=||v||²/κ<2. The correction is −(1/2)e^{−nt}(e^{δ_nt}−1), at most −(nt/2)e^{−2n²−nt}. For every REAL t>0 and integer n≥ceil(t+3), e^{n²−nt}≥e^{3n}>4ne^{2t}, giving strict negative off-diagonal entry. Duhamel positivity and e^{tA0}→u⊗u yield an eventual c_xu lower bound on each positive nonzero orbit; the antisymmetric perturbation has sup_t h_n(t)/u_n≤e^{−n²/2}/[e(1−e^{−2n²})]→0 and finitely many remaining n decay in time. Identity at t=0 is positive. Source verify.py was inspected and independent rational-time inequality checks corroborated estimates; none substitutes for the all-real-time proof.

## originality

PASS

Dobrick's exact self-adjoint compact-resolvent generator and its individual eventual strong positivity are expressly PRIOR; available first-version abstract says operators fail positivity at arbitrarily large times without asserting an all-time obstruction. The submitted package attributes a stronger inspected-in-package theorem/proposition comparison only at certain large integer times, but the primary complete text could not be independently checked here. The submitted work's new analytic comparison supplies simultaneous negativity for EVERY t>0 and quantitative n≥ceil(t+3). The general nowhere-positive phenomenon in Daners–Glück–Kennedy 2016 is known on C(K), with different generators; no demonstrated theorem transfers all structural properties and the explicit cutoff to this particular Hilbert-lattice operator. Another Resultary spectral-level barrier treats limited spectral-level systems, not shown to imply this infinitely spectral diagonal-plus-rank-one case. Full primary Dobrick paper inaccessible in this execution, so unverified theorem/appendix or newer revision remains a significant but not independently decisive originality risk.

## value

PASS

Exact positivity-time set {0} is a natural sharp qualitative refinement of an eventual-positivity counterexample: infinitely many bad integer times do not prohibit isolated positive noninteger times. The explicit all-real-time cutoff demonstrates the extreme obstruction despite compact resolvent, self-adjointness and individual eventual strong positivity. This resolves a logically distinct question for a rigid operator class rather than rebranding the originating construction.

The dated certificate retains the supplied scientific assessment, sources and limitations.
