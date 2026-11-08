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

For independent uniformly random k-subsets of n with k/n -> p in (0,1), two incidence columns collide per row with exact probability q_n. Factorial moment graph expansion: disjoint pairs contribute lambda^r, and nonmatching components s>=3 vanish since p^s+(1-p)^s < (p^2+(1-p)^2)^{s/2}. Thus Poisson X and lattice zero-collision CDF exp[-binom(n,2)q_n^t]. Expected unseen coupon n(1-k/n)^t -> 0 at the collision window, yielding Type II equality probability ->1 and expected delay o(1); collision second-moment lower tail plus first-moment upper tail establish E QI=b_n+O(1). Partition-lattice Mobius inversion proves exact finite formula. Independent enumeration of row sequences confirmed probabilities (n,k,t)=(3,1,2):2/3,(4,2,3):8/9,(5,2,3):12/25,(5,2,4):96/125. Boundary p->0 or1 intentionally excluded.

## originality

PASS

Rényi 1961 Theorem 1 proves birthday-window and factor-two design overhead for independent fair coin-bit rows, i.e. random unrestricted-size subsets, and deserves priority for the phenomenon. A fixed row weight creates dependent incidence columns, so Rényi’s product identity does not imply the claimed factorial-moment Poisson limit. Tan et al 2025 define exactly this labeled coupon problem and stopping criteria, addressing deterministic designs and expected values (not dense-group Poisson window). No precise dependent-window prior located; qualified PASS restricted to fixed-size dense sampling theorem and Type II coupling.

## value

PASS

Natural sharp probabilistic recovery threshold for dense uniformly fixed-size observations; gives full critical-window distribution, exact finite partition formula and nearly equal informational stopping times. Random-versus-planned overhead is known in a different sampling model, not claimed independently novel.

The dated certificate retains the supplied scientific assessment, sources and limitations.
