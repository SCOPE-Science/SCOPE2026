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
# Reproduction and boundaries

Compile and run the attached standalone C++17 source:

```sh
g++ -O3 -std=c++17 verify.cpp -o verify
./verify
```

The program builds the reflexive symmetric relation of nonempty-intersection subsets and enumerates all \(3^{2^n-1}\) functions for \(n=1,2,3,4\). It applies the relational forth requirement and the back requirement at every domain point, independently of the proposed atom-partition characterization. Recorded output:

```text
n=1 vertices=1 possible_maps=3 p_morphisms=0 surjective=0 expected=0
n=2 vertices=3 possible_maps=27 p_morphisms=2 surjective=2 expected=2
n=3 vertices=7 possible_maps=2187 p_morphisms=6 surjective=6 expected=6
n=4 vertices=15 possible_maps=14348907 p_morphisms=14 surjective=14 expected=14
```

The theorem for arbitrary \(X\), including infinite \(X\), is proved symbolically by the singleton-rigidity and back-condition arguments in `RESULT.md`; none of the finite checks establishes the infinite statement. The executable uses a 32-bit neighborhood bitmask solely for cases with at most 15 vertices. It is not intended as a general-purpose evaluator for larger frames. No independent audit has been performed.
