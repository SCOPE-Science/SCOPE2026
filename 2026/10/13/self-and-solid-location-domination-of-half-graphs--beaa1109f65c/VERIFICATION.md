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

The checker constructs the half graph \(H_n\) directly for
\[
2\le n\le8.
\]
For every vertex subset \(C\), it forms the identifying set
\[
I(C;u)=N[u]\cap C.
\]

Self-location-domination is checked from its original intersection definition: every non-codeword has nonempty identifying set and
\[
\bigcap_{c\in I(C;u)}N[c]=\{u\}.
\]
Solid location-domination is checked by testing, for every distinct pair of non-codewords,
\[
I(C;u)\setminus I(C;v)\ne\varnothing.
\]

The complete minimum families are then compared with the theorem. The checker also records the exceptional \(H_2\) self-locating boundary.

Recorded output:

```text
VERIFY_OK
n=2: gamma_DLD=2, DLD_minima=2; boundary gamma_SLD=3, SLD_minima=2
n=3: gamma_DLD=gamma_SLD=4, DLD_minima=7, SLD_minima=1
n=4: gamma_DLD=gamma_SLD=6, DLD_minima=14, SLD_minima=1
n=5: gamma_DLD=gamma_SLD=8, DLD_minima=23, SLD_minima=1
n=6: gamma_DLD=gamma_SLD=10, DLD_minima=34, SLD_minima=1
n=7: gamma_DLD=gamma_SLD=12, DLD_minima=47, SLD_minima=1
n=8: gamma_DLD=gamma_SLD=14, DLD_minima=62, SLD_minima=1
subsets_checked = 87376
all minimum-code classifications matched the theorem
```

The checker exhausts \(87{,}376\) subsets. This computation is exhaustive for the tested orders and corroborative only for the arbitrary-order theorem, which follows from the nested-neighborhood and forced-codeword proof.
