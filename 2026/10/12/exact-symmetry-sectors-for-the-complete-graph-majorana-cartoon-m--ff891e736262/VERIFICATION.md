---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-16.md",
      "INDEPENDENT_AUDIT_2026-10-16.json"
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

In Lucas--Osborne's Clifford representation, each N-1-factor vertex star is anti-Hermitian because (-1)^[(N-1)(N-2)/2]=-1 for N divisible by four. Thus raw Psi_v^2=-I, while S_v=i Psi_v is Hermitian, squares to I and inherits [S_v,H]=[S_u,S_v]=0 from Proposition 3.3. Product support of stars indexed by T is the edge cut delta(T). For a nonempty subset T omitting one fixed vertex, this cut is nonempty and its Majorana monomial has vanishing trace by source Prop. 3.2. The projectors P_epsilon=2^{-(N-1)} product(1+epsilon_v S_v) therefore have trace 2^{N(N-1)/4-(N-1)} and are orthogonal complete projectors. Every 2^{N-1} sector occurs at dimension 2^{(N-1)(N-4)/4}; product of all N stars has empty support and is scalar, so there is no missing symmetry label. Commutation alone guarantees block diagonalization, not energy degeneracy between sectors. Independently represented six Majoranas by 8x8 matrices for N=4 and checked anti-Hermitian stars and eight rank-one sectors, plus source's Clifford mask verification at N=4,8,12,16; these illustrate but do not prove all N.

## originality

PASS

The same Lucas--Osborne article is a decisive comparison: Proposition 3.3 proves star-H commutation but prints the incompatible claims that raw stars are Hermitian and square to one, then suggests an exponential degeneracy without computing the eigenspectrum. Rechecking its preceding definition and the anticommutation rules establishes the sign error. Neither its text nor related SYK, graph-growth, or tensor-model literature searched states the corrected N-1 independent commuting involutions and exact equal-rank 2^{N-1}-character decomposition for this edge-Majorana model. This is more than a restatement of Proposition 3.3, though standard character-projector theory is used.

## value

PASS

An incorrect normalization in a published model obstructs correct interpretation of conserved quantities. The all-N exact nonzero symmetry-sector dimension is an independently useful invariant for Hamiltonian diagonalization and rules out a purported implication to exponential level degeneracy. It is motivated by a concrete paper-specific unresolved claim, not a generic Clifford textbook identity alone; no within-sector spectrum is asserted.

The dated certificate retains the supplied scientific assessment, sources and limitations.
