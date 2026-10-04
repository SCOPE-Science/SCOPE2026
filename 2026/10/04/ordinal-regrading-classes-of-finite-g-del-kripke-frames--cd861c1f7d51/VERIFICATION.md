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

The verification is proof-based.

The critical semantic identity is
\[
e^h(w,\varphi)=h(e(w,\varphi)).
\]
It was checked connective by connective. For Gödel implication, an increasing endpoint-fixing map preserves the two cases \(a\le b\) and \(a>b\). For the modalities, finiteness of the world set turns infima and suprema into finite minima and maxima, which commute with every increasing map.

The valuation transformation is bijective because \(h\) is a homeomorphism. This is essential: it upgrades model-by-model preservation to equality of frame-validity logics.

For the census, an accessibility matrix with \(N\) labelled entries is specified up to regrading by:
1. which \(s\) entries lie strictly inside \((0,1)\);
2. a binary choice \(0\) or \(1\) for every non-interior entry;
3. an ordered set partition of the \(s\) interior entries into equality classes.

This yields
\[
T_N=\sum_{s=0}^N\binom Ns2^{N-s}\sum_{k=0}^s k!\,S(s,k).
\]

The bundled `verify.py` independently enumerates canonical signatures for \(N\le4\), checks the values \(3,11,51,299\), and performs exhaustive small-chain semantic tests of regrading commutation for a generated family of formulas. These computations are consistency checks only; the theorem for arbitrary finite \(m\) follows from the proof.

## Limits

The checker does not enumerate all frames for arbitrary \(m\). The exact theorem does not require it. The language is assumed not to contain named intermediate truth constants, and the exact orbit count is for labelled worlds.
