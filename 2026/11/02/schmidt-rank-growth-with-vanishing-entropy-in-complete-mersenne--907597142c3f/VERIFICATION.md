---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-06.md",
      "INDEPENDENT_AUDIT_2026-11-06.json"
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

Lucas parity for binomial(w,q−1) where q=2^j gives a phase -1 precisely for total weight ≡q−1 (mod q), so the n-qubit hypergraph amplitude matrix is constant on Hamming-weight residue classes. Both subsystem sizes ≥q−1 realize all residues. Compression by normalized residue superpositions gives T=D_m(11ᵀ−2R)D_b, and invertible diagonals leave rank determined by reversal permutation R. Direct multiplication (11ᵀ−2R)(11ᵀ−2R)ᵀ=4I+(q−4)11ᵀ gives eigenvalues (q−2)^2 once and 4 (q−1)-fold; for q≥8 rank is q. Fourier root-of-unity filter makes each residue probability tend to 1/q as both blocks grow at fixed q. Hence exact limiting spectrum {(1−2/q)^2,4/q² [q−1 times]}, and purity/entropy S_q=O(log q/q)→0 as the second limit q→∞. Independent direct diagonalization of a 128×128 computational-basis amplitude matrix for q=8,m=b=7 matched compressed spectrum; independent q=8,16,32 reversal eigenvalues verified. The proof establishes all q, not the finite checks.

## originality

PASS

Original hypergraph-state phase formalism is Rossi et al.; general sign matrix and rank restriction certificates are Fajardo–Paraschiv 2026; Nöller et al. analyze other entanglement quantities. Power-of-two uniformity results use k=2^j, whereas this theorem uses k=2^j−1 and a distinct Lucas phase kernel. The assessed novel result is the exact complete Mersenne bipartite spectrum and sequential entropy collapse with high Schmidt rank. Potential hidden equivalent symmetric-state spectrum results remain a best-of-knowledge priority risk, especially unread parts of Nöller.

## value

PASS

For physically natural complete-uniform hypergraph states the theorem computes every nonzero bipartite eigenvalue using a small cyclic matrix rather than an exponentially large amplitude matrix. It sharply separates Schmidt rank, which grows unbounded, from operational von Neumann entropy, which vanishes after the stated sequential limit; this is a motivated many-body entanglement phenomenon rather than an arbitrary parameter substitution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
