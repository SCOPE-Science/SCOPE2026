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

The focal 33-page preprint defines a leaf projection P using normalization phi_t(0)=t (section 3.3.1) and equivariance P o f=psi o P. Since f is area preserving, nu=P_*(Lebesgue area) is invariant under psi. For a short oriented parameter interval I=[s,t], P^-1(I) is a strip between ordered graph leaves, whose area is int_0^1(phi_t(x)-phi_s(x)) dx. The source Definition (8), page 28 formula (59), compares this gap to t-s between factors K_Fol^-1 and K_Fol at each x. Hence nu gives all arcs two-sided density bounds, so its cumulative-distribution lift H is bi-Lipschitz. Invariance implies H(psi(t))-H(t) constant (mod integer), forcing conjugacy to rotation by the irrational rotation number alpha established in Proposition 3.16. The exact remaining bi-Lipschitz conjugacy hypothesis in Theorem C is fulfilled, so f minimal. Wraparound arcs lifted periodically; leaves have zero area; no claim foliation Lipschitz follows automatically.

## originality

PASS

Full text of Addas-Zanata–Lazaro Aguirre explicitly distinguishes the proof of psi itself being bi-Lipschitz (Lemma 3.17) from its conjugacy being bi-Lipschitz (still a separate assumption of Theorem C). The new invariant transverse-area marginal supplies the latter and removes a substantive condition. Older annulus leafwise-invariant Arnol'd–Liouville work covers a different system; no indexed equivalent found.

## value

PASS

Removes a real extra regularity assumption from a new minimality theorem by a geometric invariant-measure mechanism, isolating the remaining transverse-foliation regularity gap. Not merely reparameterization; has direct consequence for dynamical minimality.

The dated certificate retains the supplied scientific assessment, sources and limitations.
