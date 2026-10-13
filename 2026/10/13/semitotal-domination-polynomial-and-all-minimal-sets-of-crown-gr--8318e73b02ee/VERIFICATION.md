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

The checker constructs \(\operatorname{Cr}_n\) directly for
\[
3\le n\le7.
\]
It computes all-pairs shortest-path distances by breadth-first search and enumerates every vertex subset. For each subset it checks domination and the literal condition that every selected vertex has another selected vertex within distance at most \(2\).

It then compares the direct answer with the structural set classification, the complete coefficient vector of
\[
\mathcal S_n(z)=2z^n+\bigl((1+z)^n-1-nz\bigr)^2+2nz^2\bigl((1+z)^{n-1}-1\bigr),
\]
and the minimal-set coefficient vector
\[
\mathcal M_n(z)=2z^n+2n(n-1)z^3+\binom n2\binom{n-2}{2}z^4.
\]

Recorded output:

```text
n=3: semitotal_sets=36, minimal_profile={3: 14}
n=4: semitotal_sets=179, minimal_profile={4: 8, 3: 24}
n=5: semitotal_sets=828, minimal_profile={5: 2, 3: 40, 4: 30}
n=6: semitotal_sets=3623, minimal_profile={6: 2, 3: 60, 4: 90}
n=7: semitotal_sets=15284, minimal_profile={7: 2, 3: 84, 4: 210}
VERIFY_OK
vertex_subsets_checked = 21824
all direct semitotal tests matched the all-set classification
all semitotal-polynomial coefficients and minimal-set profiles matched
```

The finite computation is corroborative only. The all-\(n\) result follows from the exact domination and distance analysis in the proof.
