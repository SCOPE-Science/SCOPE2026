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

`verify.py` is a standard-library replay of every finite component used by the claim. It reconstructs the six-rung ladder, enumerates all matching-complex faces, checks every Hasse cover and every directed edge of the Morse orientation, enumerates all graph automorphisms, computes signed simplicial-chain traces for the four automorphisms, and checks the character decomposition.

The expected exact outputs are 732 nonempty faces, 2586 Hasse covers, 363 Morse pairs, one critical 0-cell, five critical 3-cells, automorphism-group order 4, chain-trace rows `(16,92,234,263,114,13)`, `(6,10,0,-9,-2,1)`, `(2,-6,-10,7,8,-1)`, and `(0,-8,0,15,0,-5)`, followed by the homology character `(5,-1,1,3)` and multiplicities `(2,0,1,2)`.

As a separate cross-check, the script builds the simplicial boundary matrices and computes ranks modulo 2, 3, and 5; each field gives Betti vector `(1,0,0,5,0,0)`. These finite-field checks do not by themselves prove the rational representation; the discrete-Morse certificate and exact signed traces provide the required proof.

The replay does not assess claims outside the stated six-rung graph and does not classify the integral group-ring lattice.
