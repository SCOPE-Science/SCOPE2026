---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-29.md",
      "INDEPENDENT_AUDIT_2026-10-29.json"
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

Reconstructed Gaussian conditioning: B_t | B_s=0 has variance t(s-t)/s for t<=s, (t-s)(1-t)/(1-s) for t>=s. Occupation density and Tonelli yield E[L I_q] by integrating p_s(0)*(2q-1)!! v(s,t)^q, whose time integral is beta(q+1,q+1)[s^(q+1)+(1-s)^(q+1)]. The s integral is beta(q+3/2,1/2); E[L]=sqrt(pi/2), E[I_q]=q!/[2^q(2q+1)]. Beta/gamma duplication gives the central-binomial bracket; strict negativity for q>=1 follows binom(2n,n)<2^(2n-1) for n>=2. q=0 is constant. Independent high precision beta/coefficient evaluations q=0..12 agreed.

## originality

PASS

Pitman derives bridge local-time distributions and related occupation-density identities but no all-q power-energy mixed covariance in inspected relevant report text. Knight studies conditional moments of the ABSOLUTE bridge area int|B|dt given local time; even-power energies are different. Knight full text unobtainable despite attempted open access followed by authorized institutional retrieval returning disconnected VPN; this alone does not force scientific rejection but creates concrete priority risk.

## value

PASS

The exact all-integer-order covariance hierarchy links zero-contact local time to amplitude-based path energies, and supplies strict negative sign and reusable closed coefficients. It is a natural joint path-functional invariant not determined by marginal local-time or energy moments alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
