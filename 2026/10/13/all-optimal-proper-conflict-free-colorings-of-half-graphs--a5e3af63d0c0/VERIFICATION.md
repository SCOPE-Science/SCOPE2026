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

The verifier constructs \(H_n\) directly from
\[
a_i b_j\in E(H_n)\quad\Longleftrightarrow\quad i\le j.
\]
For each coloring it checks both conditions independently of the proof:
1. every edge has differently colored endpoints;
2. every open neighborhood contains at least one color occurring exactly once.

Every assignment with three or four named colors is exhaustively checked for \(n=3,4,5\), totaling \(1{,}184{,}547\) assignments. The verifier finds no three-color PCF coloring. For \(n=4,5\) it finds exactly \(384\) four-colorings.

After fixing the four forced core colors by
\[
\varphi(a_1)=0,\quad \varphi(a_2)=1,\quad \varphi(b_{n-1})=2,\quad \varphi(b_n)=3,
\]
the exhaustive optimum set for \(n=4,5\) is compared with the symbolic family and consists of exactly \(16\) colorings.

The symbolic family is also constructed and definition-checked for every
\[
4\le n\le50.
\]

Recorded output:

```text
VERIFY_OK
n=3, k=3: PCF_colorings=0
n=3, k=4: PCF_colorings=216
n=4, k=3: PCF_colorings=0
n=4, k=4: PCF_colorings=384
n=5, k=3: PCF_colorings=0
n=5, k=4: PCF_colorings=384
total_colorings_checked = 1184547
normalized_construction_range = 4..50
for n=4,5 exactly 16 normalized optima and 384 named four-colorings
```

The finite tests are corroborative. The arbitrary-order theorem follows from the four forced core colors and the binary prefix/suffix lemma in `RESULT.md`.
