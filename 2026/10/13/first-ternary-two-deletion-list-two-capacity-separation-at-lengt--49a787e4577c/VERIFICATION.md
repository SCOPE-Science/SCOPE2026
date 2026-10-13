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

# Reproduction

Use Python 3 and a C++17 compiler. Run `python3 verify.py` in the directory of the attached files. The Python program checks all displayed codebooks, all two-deletion shadows, and eight rational LP dual certificates. It regenerates the complete length-six compatibility graph and compiles `clique.cpp`, which performs an exhaustive branch-and-bound search with an integer greedy-coloring upper bound. Actual replay produced:

```
DUAL 2 1 1
DUAL 2 2 2
DUAL 3 1 3
DUAL 3 2 9/2
DUAL 4 1 3
DUAL 4 2 6
DUAL 5 1 33/5
DUAL 5 2 63/5
CLIQUE best=11 nodes=1680903
VERIFY_OK
```

The upper-bound enumeration is finite and terminates after the reported nodes. The code does not compute the exact length-six list-two optimum, and no statement about larger lengths or alphabets is verified.
