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

The analytic derivation in `RESULT.md` uses the Foster--Pixley coordinate normal form from Mayr--Ruškuc. Once that normal form is fixed, the key exact identities are:

1. each target coordinate of an embedding has \(au+c\) possible actual coordinate maps;
2. injectivity is equivalent to using every one of the \(u\) source coordinates at least once among the \(au\) automorphic choices;
3. inclusion--exclusion therefore gives
\[
E_{v,u}=\sum_{j=0}^{u}(-1)^{u-j}\binom uj(c+aj)^v;
\]
4. at \(v=u\), \(E_{u,u}=u!a^u\), so dividing by the domain automorphism group counts image subalgebras;
5. the quotient is the standard explicit formula for \(W_{a,c}(v,u)\).

`verify_whitney_subpowers.py` checks the arithmetic and the structural reduction in three ways. It verifies the r-Whitney recurrence against the explicit formula on a broad parameter grid; exhaustively counts symbolic coordinate descriptors for small \((a,c,u,v)\); and independently enumerates operation-preserving maps for the concrete algebra \((\mathbb Z_2,x-y+z,\cdot)\) from Mayr--Ruškuc Example 1.2, followed by exhaustive embedding and distinct-image counts.

Replay:

```text
python3 verify_whitney_subpowers.py
```

Recorded terminal line:

```text
VERIFY_OK 2841 exact assertions
```

The computational replay does not replace the Foster--Pixley theorem; it independently checks the finite counting consequences and a concrete source example. Independent audit has not been performed.
