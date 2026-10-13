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

The verifier constructs the crown graph directly, with
\[
a_i b_j\in E
\quad\Longleftrightarrow\quad
i\ne j.
\]

For a candidate set \(S\), it independently checks:
1. every vertex outside \(S\) has a neighbor in \(S\);
2. the induced graph on \(S\) has at least one isolated vertex;
3. for every vertex \(u\notin S\), at least one selected neighbor \(v\) can be swapped out so that
\[
(S\setminus\{v\})\cup\{u\}
\]
again satisfies both preceding conditions.

Every nonempty subset is tested for \(3\le n\le7\), totaling
\[
21{,}819
\]
subsets. The recorded output is:

```text
VERIFY_OK
n=3: total_ISDS=14, gamma_0s=3, minima=14
n=4: total_ISDS=2, gamma_0s=4, minima=2
n=5: total_ISDS=2, gamma_0s=5, minima=2
n=6: total_ISDS=2, gamma_0s=6, minima=2
n=7: total_ISDS=2, gamma_0s=7, minima=2
subsets_checked = 21819
construction_checked_n = 4..50
for every exhaustive n>=4, the only ISDS were the two bipartition classes
```

For every exhaustive case with \(n\ge4\), the only isolate secure dominating sets are the two bipartition classes. The \(n=3\) boundary has fourteen feasible sets.

The construction check also verifies both bipartition classes directly for every
\[
4\le n\le50.
\]

The finite checks are corroborative only. The arbitrary-order result follows from the isolated-vertex confinement and forced-swap argument in `RESULT.md`.
