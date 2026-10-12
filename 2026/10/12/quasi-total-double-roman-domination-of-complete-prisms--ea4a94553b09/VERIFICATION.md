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

The verifier constructs the two clique layers and their perfect matching directly. It checks a labeling against the definition without using the proof:

1. each label-\(0\) vertex has a label-\(3\) neighbor or at least two label-\(2\) neighbors;
2. each label-\(1\) vertex has a neighbor labeled at least \(2\);
3. every positive vertex isolated in the positive-support subgraph has label \(2\).

It exhaustively tests every labeling for \(n=3,4,5\):
\[
4^6+4^8+4^{10}=1{,}118{,}208
\]
labelings. The minimum value is \(6\) in all three cases. For \(n=4\) and \(n=5\), the complete set of minimum functions is exactly the predicted matched label-\(3\) family, of sizes \(4\) and \(5\). The \(n=3\) boundary has \(15\) minimum functions, confirming that the optimizer classification must start at \(n=4\).

The verifier also constructs and definition-checks every claimed minimum function for every
\[
4\le n\le50.
\]

Recorded output:

```text
VERIFY_OK
n=3: gamma_qtdR=6, minimum_functions=15
n=4: gamma_qtdR=6, minimum_functions=4
n=5: gamma_qtdR=6, minimum_functions=5
full_labelings_checked = 1118208
constructed_parameter_range = 4..50
for n=4,5 every exhaustive minimum matched the n matched 3-3 functions
for n=3 the same value 6 has additional minimum functions
```

The finite checks are corroborative only. The arbitrary-\(n\) lower bound and complete equality classification follow from the symbolic layer-weight proof in `RESULT.md`.
