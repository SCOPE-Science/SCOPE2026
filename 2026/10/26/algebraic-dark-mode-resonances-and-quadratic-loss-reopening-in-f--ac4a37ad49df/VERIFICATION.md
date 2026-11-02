---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-30.md",
      "INDEPENDENT_AUDIT_2026-10-30.json"
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

The irreducible 2N-site Jacobi chain has nonzero, simple real energies; eliminating B amplitudes gives E² a_j=(1+r²)a_j+r(a_{j-1}+a_{j+1}), with a_0=-r a_1 and a_{N+1}=0. For an interior node at A_m the only admissible real k satisfy sin(Lk)=0, k=πj/L, and the left boundary gives the positive finite ratio r=-sin(mk)/sin((m-1)k); both ± eigenvalues are dark and distinct j give distinct energies. Any eigenmode of K=-iH-γP_loss/2 with zero decay must have zero loss amplitude, hence be precisely such a clean dark orbital. If none, finite-dimensional e^{tK}->0, expectation of number decays for every fermionic density matrix, and vacuum attraction follows; otherwise dark occupied Fock configurations give 2^q orthogonal stationary pure states. At isolated roots the simple eigenvalue branch k(r) has k′=b, while the normalized loss-site weight is L²b²/[2 sum_h sin²(hk0)]·(r-r0)²; analytic first-order weak-loss perturbation proves the stated iterated limit. Independently diagonalized 28-site SSH matrix for N=14,m=3,r=√2, found four nodal orbitals, indices j=5,11, and checked both quadratic reopenings for two detunings. No claim of joint (γ,r) uniformity or exhaustion of all stationary density matrices.

## originality

PASS

The single-loss finite-SSH model, local-weight weak-loss law and possible exact nodal modes are in Wang–Zhang (2026); dissipative edge modes are also known. The new finite all-(N,m,r>0) positive algebraic resonance list, exact multiplicity and coefficient are not stated in the primary full text inspected. General Jacobi recurrence/controllability theory may contain equivalent classifications, a material residual priority risk.

## value

PASS

The set of exact dark-mode couplings is a motivated observability/control boundary in a finite open dissipative chain; an explicit arbitrary-loss-site classification and its quadratic reopening coefficient give usable quantitative robustness information. Nonuniform N=14,m=3,r=√2 yields four dark one-body orbitals and a 16-dimensional noiseless Fock sector, so the result is not merely a renamed parity count.

The dated certificate retains the supplied scientific assessment, sources and limitations.
