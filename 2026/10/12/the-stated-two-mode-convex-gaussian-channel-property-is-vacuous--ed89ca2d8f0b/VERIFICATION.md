---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---
# Verification

The proof is symbolic. Its decisive steps are:

1. Parity superselection decomposes every physical two-mode state into two \(2\times2\) positive blocks.
2. Every pure vector in either parity block is obtained from a Gaussian occupation-number state by a determinant-one matchgate block, so every physical mixed two-mode state is convex-Gaussian by spectral decomposition.
3. The source's noisy parity-preserving gate family maps physical states to physical states, hence satisfies the stated local convex-Gaussian input-output property for every \(p\).
4. The source's own formula has \(\eta(\mathrm{SWAP})=1\), \(C_-(U,p)=0\), and therefore \(C_+(\mathrm{SWAP},0)=1\), contradicting Eq. (35) under the stated definition.

The accompanying checker independently replays the finite matrix identities behind steps 2--4 and confirms the stated threshold is a root of the source's concurrence expression for \(\eta=1\). The finite replay is not used as a substitute for the general spectral-decomposition and matchgate argument.

Unproved limit: no claim is made about equivalence between four-mode Choi convex-Gaussianity and a separately defined channel property stable under arbitrary fermionic reference extensions. That stronger question is outside this finding.
