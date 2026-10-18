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

The exact theorem is proved in `RESULT.md` using a classification of all subalgebras and counting all possible dimension-pair failures of permutability. The accompanying `verify.py` script requires only the Python 3 standard library. Run:

```bash
python3 verify.py
```

It constructs every linear subspace of a four-dimensional vector space using reduced row-echelon bases, checks closure under the defining Lie bracket and independently tests \([A,B]\subseteq A+B\) for every ordered pair of subalgebras. It independently verifies field operation axioms for the supported fields, including \(\mathbb F_4\) represented using \(lpha^2=lpha+1\). The checker was actually executed on the packaged source, giving:

```text
q= 2 subalgebras= 31 dimension_counts= {0: 1, 1: 15, 2: 11, 3: 3, 4: 1} nonpermuting_pairs= {(1, 1): 144, (1, 2): 80, (2, 1): 80, (2, 2): 24} permuting_pairs= 633
q= 3 subalgebras= 68 dimension_counts= {0: 1, 1: 40, 2: 22, 3: 4, 4: 1} nonpermuting_pairs= {(1, 1): 1296, (1, 2): 567, (2, 1): 567, (2, 2): 108} permuting_pairs= 2086
q= 4 subalgebras= 129 dimension_counts= {0: 1, 1: 85, 2: 37, 3: 5, 4: 1} nonpermuting_pairs= {(1, 1): 6400, (1, 2): 2304, (2, 1): 2304, (2, 2): 320} permuting_pairs= 5313
q= 5 subalgebras= 220 dimension_counts= {0: 1, 1: 156, 2: 56, 3: 6, 4: 1} nonpermuting_pairs= {(1, 1): 22500, (1, 2): 6875, (2, 1): 6875, (2, 2): 750} permuting_pairs= 11400
VERIFY_OK: all subspaces, Lie closures, and ordered permutability pairs checked for q=2,3,4,5
```

These finite tests do not prove a formula over every finite field; generality follows from the explicit algebraic incidence proof. No independent mathematical audit has been performed.
