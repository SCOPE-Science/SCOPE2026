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

Independently reconstructed the complete maximal subgroup list: A itself and, for each maximal index-p hyperplane preimage L<A, the p groups L union (a s)L indexed by a mod L. Since A is abelian and inversion stabilizes L, these are subgroups and are all maximal. Counting hyperplanes of A_p/pA_p yields M=1+sum p h_p and Frattini Phi(G)=product pA_p. Each reflection lies in one extension of each L and has incidence H=sum h_p; a rotation with nonzero Sylow residues at S lies in M-sum_{p in S}p^{r_p} maximal subgroups. Binomial-independent residue counts give the polynomial. The elementary combinatorial identity ui=1+max_{g notin Phi}delta(g) then gives M+1-min p^{r_p}; reflection degree cannot exceed this rotation maximum because their difference is sum_{p != p*}(p^{r_p}-1)>=0. Wrote and executed an independently implemented group-multiplication/subgroup-closure enumeration (not repository program) for A=C2xC2, C3xC3, C4xC2, C2xC3 and C3xC3xC5; exhaustive subgroup lists give expected profiles/maximal counts/ui=4,5,4,5,14 respectively. General theorem follows the all-finite-abelian structural argument, not the samples.

## originality

PASS

Choudhury–Khanra (2026), Theorem 2.6, already establishes the cyclic rotation-kernel uniform intersection number and generic Frattini tools. Archer et al. (2019), Proposition 4.1, gives the different MINIMUM intersection number for cyclic dihedral groups. Two related published Resultary findings classify minimal-generator graphs and subgroup commutativity, not maximal-subgroup element incidences. The noncyclic abelian kernel profile and sharp ui appear not directly covered, although generic subgroup-lattice theory may implicitly imply them.

## value

PASS

Maximal subgroup intersection properties are a natural finite-group invariant, with a recent paper computing only cyclic dihedral cases. This result extends to arbitrary abelian kernels including noncyclic p-ranks and even-order kernels, giving the complete elementwise incidence distribution rather than only one threshold. Rank dependence captures genuine structure absent from the cyclic formula; it is an all-family classification rather than a small-instance exercise.

The dated certificate retains the supplied scientific assessment, sources and limitations.
