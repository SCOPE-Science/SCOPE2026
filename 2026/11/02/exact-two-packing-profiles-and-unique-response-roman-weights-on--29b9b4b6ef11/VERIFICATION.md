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

# Reproducibility and limits
Run the accompanying standalone \(\texttt{verify.py}\) with Python 3.10 or newer, without packages or internet access:

```sh
python3 verify.py
```

The program evaluates \(\det(I-xM)\) in \(\mathbb Z[x,u]\) by its full 120-permutation expansion, constructs the actual circular-ladder adjacency and two-step distance prohibition masks, and brute-forces all candidate subsets of at most \(\lfloor n/2\rfloor\) selected vertices for each \(3\le n\le12\). Independently, for \(3\le n\le6\), it tests **every** ternary function directly against both defining Roman conditions. It checks the evaluated transfer matrix, explicit coefficient formula, polynomial recurrence through \(n=60\), and residue-class extrema through \(n=100\).

The expected final line is \(\texttt{VERIFY_OK}\). Finite enumeration and symbolic checking corroborate the explicit general proof; they are not a substitute for the quantified proof of the local characterization, coefficient formula, or extremal transition. No external or independent audit has been performed.
