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

The included checker constructs the square-page book graph directly. It computes every closed neighborhood and tests a subset \(C\) by the definition: every non-codeword must have a nonempty identifying set, and for every ordered pair of distinct non-codewords \(s,t\),
\[
I_C(s)\setminus I_C(t)\ne\varnothing.
\]

Independently of that predicate, the checker generates the four structural code families from the theorem. For each
\[
1\le m\le8,
\]
it enumerates every vertex subset and compares the exact accepted subset family with the structural prediction. It also independently constructs the coefficient dictionary of
\[
2z^{m+1}(1+z)^m+(m+1)z^{2m}+z^{m+2}(z+2)^m
\]
and compares it with the actual code-size histogram.

Recorded output:

```text
VERIFY_OK
m=1: gamma_DLD=2, minimum_codes=4, all_DLD_codes=9
m=2: gamma_DLD=3, minimum_codes=2, all_DLD_codes=20
m=3: gamma_DLD=4, minimum_codes=2, all_DLD_codes=47
m=4: gamma_DLD=5, minimum_codes=2, all_DLD_codes=118
m=5: gamma_DLD=6, minimum_codes=2, all_DLD_codes=313
m=6: gamma_DLD=7, minimum_codes=2, all_DLD_codes=864
m=7: gamma_DLD=8, minimum_codes=2, all_DLD_codes=2451
m=8: gamma_DLD=9, minimum_codes=2, all_DLD_codes=7082
vertex_subsets_checked = 349520
all solid-location-dominating codes matched the structural classification and polynomial
```

Thus \(349{,}520\) subsets were tested directly. The finite computation is corroborative only; the theorem for all \(m\) follows from the symbolic case analysis in `RESULT.md`.
