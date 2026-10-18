---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-18.md",
      "INDEPENDENT_AUDIT_2026-10-18.json"
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

The Pauli XX+YY+ZZ action on the single-excitation basis equals twice the cycle adjacency, with zero diagonal; its two opposite-momentum modes have eigenvalue zero. A normalized superposition has site probabilities p_j=(1+2(-1)^j Re(a conj(b)))/4. Since the one-site density is diag(1-p_j,p_j), Brennen’s average-purity identity gives Q=1-Σp_j²=3/4-Re(a conj(b))². Because |Re(a conj(b))|≤1/2 and every intermediate magnitude is achievable, the range is exact. The endpoint |1000>-|0010> normalized has Q=1/2 while momentum waves have Q=3/4. The independent exact fraction endpoint check agrees, but the continuous formula comes from algebra, not enumeration. This is not a contradiction to the source plane-wave computation; it refutes the unqualified statement about every energy eigenvector in a degenerate eigenspace.

## originality

PASS

The source Meyer–Wallach calculation says translation invariance makes one-excitation eigenstates plane waves and reports Q=4(n-1)/n²; this implication does not hold for arbitrary degenerate energy eigenvectors, even though a plane-wave eigenbasis exists. Brennen gives the one-site purity reformulation, not a degeneracy correction. No comparable published same-Hamiltonian exact two-dimensional range emerged from the scientific-record query, but search failure is not absolute priority proof.

## value

PASS

This precise four-site example identifies a consequential logical boundary in a foundational entanglement calculation: energy eigenspaces can contain states with different multipartite entanglement even when excitation number and energy are fixed. The complete minimal degenerate-eigenspace range, not merely a one-line numeric witness, is a motivated diagnostic for spectral entanglement claims.

The dated certificate retains the supplied scientific assessment, sources and limitations.
