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
# Reproducible finite verification

The full claim is specific to a finite graph; no infinite-parameter extrapolation is involved. In a directory containing all the included artifacts, run:

```sh
python3 verify_franklin_character.py
python3 verify_chain_independent.py
```

The first program regenerates the eighteen graph edges from the LCF specification, the 1,091 simplices, the complete 48-element automorphism group and the four-element Hamiltonian-cycle orbit. It checks that the four-letter permutation action has image all of \(S_4\) and kernel exactly the identity and central half-turn, and that the sign of the eighteen-edge permutation distinguishes this central half-turn. It constructs a 539-pair discrete-Morse matching and checks the entire directed Hasse graph for acyclicity. Only one critical vertex and twelve critical three-simplices survive. This is an exact finite acyclic-Morse certificate for the homotopy premise.

For each of 48 automorphisms the first program computes the oriented fixed-simplex trace separately from the fixed-edge-orbit alternating-sum polynomial. It checks equality, the ten full conjugacy classes, the exact character formula, and all ten rational irreducible multiplicities. It writes the regenerated complete summary to `franklin_character_certificate.json` and prints `FRANKLIN_CHARACTER_VERIFIED` upon success.

The second program independently enumerates matching faces and performs binary boundary elimination, obtaining ranks \((1,17,100,236,169,17)\) and reduced Betti sequence \((0,0,0,12,0,0)\). It prints `FRANKLIN_INDEPENDENT_CHAIN_VERIFIED`. Finite-field ranks corroborate the integral Morse conclusion but are not substituted for it.

The recorded certificate and the embedded source code are both included for reproducibility. They provide exact finite mathematical checks, not formal proof-assistant certification, independent human assessment, publication-priority certification, or a theorem about larger crossed-prism graphs. Rational quotient homology follows mathematically from invariant rational homology under finite simplicial group actions after equivariant subdivision, not from a homotopy-type claim about those quotients.
