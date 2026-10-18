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
# Finite verification instructions

Run in the directory containing the delivered scripts:

```
python3 verify_icosahedral_character.py
python3 verify_icosahedral_orbits.py
```

Each script uses only Python 3 standard-library modules. Their mathematical inputs are explicitly listed in `RESULT.md`: an edge list of the icosahedral graph, twelve neighborhood facets, and three automorphism permutations.

The first program builds the complete simplicial complex with augmented face counts \((1,12,60,120,60,12)\), reconstructs all \(120\) graph automorphisms by a unique-extension search from triangular flags, computes the mod-two ranks \((11,49,48,12)\) and orientation signs, and checks every signed fixed-face trace. Those ranks force the stated rational homology by the chain-complex dimension bounds spelled out in `RESULT.md`.

The second program independently constructs the full \(120\)-element group from explicit generators, creates the complex as unions of twelve neighborhood facets, and for each symmetry computes character traces by selecting unions of cycles in the vertex permutation rather than scanning oriented simplices. It checks the same class counts, trace values, and rational irreducible multiplicities. Both completed successfully with `VERIFY_OK`.

No numerical tolerance, probabilistic sample or cutoff extrapolation is involved. The scripts reproduce a finite proof for a single graph; they make no claim about all graphs or integral equivariant homology. Independent scientific review and external certification have not been performed.
