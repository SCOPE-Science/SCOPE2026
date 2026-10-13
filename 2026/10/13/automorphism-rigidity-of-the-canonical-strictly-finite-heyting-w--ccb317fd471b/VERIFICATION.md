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

The finite verifier replays the order-theoretic mechanism from Definition 4.1.

For adjacent levels of width \(m+1\), it uses
\[
x_{i+1}^l\le x_i^u\quad\Longleftrightarrow\quad u\ne l+1.
\]
It exhaustively enumerates all pairs of level permutations for \(m\le5\) and verifies that incidence preservation is equivalent to the intrinsic endpoint/shift rules
\[
p(0)=0,\qquad q(m)=m,\qquad p(l+1)=q(l)+1\quad(l<m).
\]
It separately checks through \(m=100\) that upper label \(0\) and lower label \(m\) are uniquely universal and that every lower \(l<m\) misses exactly upper \(l+1\). It also verifies the iterated missing-upper reconstruction and finite compatible level chains for manageable widths.

Replay:

```text
python3 verify_rigidity.py
```

Expected terminal line:

```text
VERIFY_OK 202219 exact assertions
```

The finite replay is not the proof of the all-\(n\) theorem. The proof is the intrinsic level/end-point/missing-neighbor argument in RESULT.md. Independent audit has not been performed.
