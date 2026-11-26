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

In reflection coordinates, the bright amplitude block is strictly stable: a neutral eigenvector must vanish at site 0, and the nonzero tridiagonal hoppings then force it to vanish everywhere. Hence the only unperturbed peripheral operator blocks are the dark Hamiltonian-frequency sectors; they are semisimple. The first-order compression of site dephasing onto the dark block is minus the identity plus one-half of the diagonal projection in the antisymmetric position basis. Its Rayleigh quotient on every frequency subspace is at most -1/2; equality requires a diagonal matrix. The only nonzero diagonal eigenoperators of the connected dark Hamiltonian commutator are scalar multiples of the dark projector at frequency zero, also for L=1. This gives a simple first-order eigenvalue and a uniquely dominant analytic branch at small positive gamma by reducing the semisimple zero block and dividing its reduced matrix by gamma. Complex conjugation of eigenvalues follows from Hermiticity preservation, making the isolated branch real. With right vector P_-/L and fixed left normalization Tr(P_-X)=1, the first-order eigenvector equation has bright component T/(2L), where A_+T+TA_+^*=-B. The true eigenvector derivative can differ from this candidate by a dark zero-frequency component, but that component has zero dark trace and does not contribute to the second-order pairing: Tr(P_-D(K))=-Tr(K)/2 there. The eigenvalue's quadratic coefficient is therefore Tr(BT)/(4L). For the displayed T, write beta_j=L+1-j with the missing endpoint beta_(L+1)=0. The adjacent imaginary entries give diagonal flux beta_(j+1)-beta_j=-1; at the center the incoming flux L cancels kappa T_00. For interior equal-parity off-diagonals the imaginary-entry contributions cancel by the second difference of beta. For opposite parity the real entries cancel by the linear index and beta differences, with the common diagonal constants canceling for adjacent indices. In row 0 the even columns cancel by the beta recurrence with the weighted first edge, and the odd columns cancel against the sink term (at column 1 the hopping uses T_11-T_00). This verifies the Lyapunov residual and gives the diagonal sum L^2/kappa+kappa L(L+1)(L+2)/(48g^2). Negating the eigenvalue gives the stated expansion. For any gamma>0 the real-part dissipative identity would force a neutral eigenmatrix to be site-diagonal with zero center, and then commute with the connected hopping matrix, forcing it to be zero. The dominant spectral projector tends to X mapped to Tr(P_-X)P_-/L; its survival-trace amplitude tends uniformly to one on normalized dark initial states.

## originality

PASS

A symmetry-center dark component and its dephasing-assisted escape are established mechanisms, including for this geometry. The supported distinct claim is the uniquely dominant weak-dephasing spectral branch and its explicit all-length quadratic coefficient. Neither a trapping-efficiency study of this geometry nor the inspected exact path/cycle absorption and dark-space results supplies that spectral evaluation.

## value

PASS

The model is an established example of symmetry-protected transport, where eventual capture or mean trapping time alone does not identify the long-time survival rate. The theorem identifies the mode that actually controls survival, gives the same leading slope across all finite lengths, and separates the inverse-sink and coherent length-dependent parts of the first correction. This is a useful exact benchmark for weak-noise trapping rather than a numerical recalculation or a light-harvesting performance claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
