---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-02.md",
      "INDEPENDENT_AUDIT_2026-11-02.json"
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

From normalized radial moments alpha^(-n/p)Gamma((n+1)/p)/Gamma(1/p), p=m/2>1, reconstructs reproducing kernel Gamma(1/p)E_(1/p,1/p)(alpha^(1/p)z conjugate(w)). Published sectorial Mittag–Leffler asymptotic and intrinsic Gaussian metric bound yield delta_R^2 B_alpha(R+delta_R u,R+delta_R v) -> G_alpha(u-v)=alpha p^2/pi exp(-alpha p^2|u-v|^2), delta_R=R^(1-p), with strong L2 convergence on compactly supported test functions after inner Gaussian and far-region tail control. Multiplier is exp(-|xi|^2/(4alpha p^2)); expanding smooth compactly supported wave packets at |xi|=2p sqrt(s) have error O(1/L). Taking each packet first and R_n afterward handles nonuniformity and obtains a weakly-null common Weyl sequence for all fixed alpha, including s=infinity by frequency going to infinity. Bounded polynomial telescoping and compact operators vanishing on weakly-null sequences imply asserted Calkin lower bounds. Maximizing |t-t^r| on [0,1] gives |r-1|r^(-r/(r-1)); independently checked r=2 and r=1/2 both give 1/4. Full local-to-global tail proof imports Borichev–Fantolini–Youssfi Lemma 3.2; CHECK.py finite kernel tests are not substituted for that analytical premise.

## originality

PASS

Read the primary 2026 Borichev–Fantolini–Youssfi article full HTML, especially Lemma 3.2 and Proposition 4.1: it proves bounded Berezin operators, compact commutators and asymptotic Gaussian estimates but does not state common singular approximate eigenvectors or this multi-parameter Calkin lower-bound curve. Tian’s products paper addresses identities not common essential spectrum. The new wave-packet extraction is additional, albeit potentially a special case of general limit-operator machinery.

## value

PASS

Extracts a continuum of joint approximate spectral data from a family known to have compact commutators: every polynomial combination acquires explicit essential-norm lower bounds and distinct parameters have a strictly positive computable separation, clarifying what qualitative almost-commutation does not say.

The dated certificate retains the supplied scientific assessment, sources and limitations.
