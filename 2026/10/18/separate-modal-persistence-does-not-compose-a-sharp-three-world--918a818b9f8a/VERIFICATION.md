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

# Finite verification and reproduction

The code `verify.py` is self-contained and uses Python 3 standard library only. Execute `python3 verify.py` in the extracted package directory.

The checker independently generates the exact three-world upset lattice and evaluates both extrinsic modal operations. It closes the one-atom truth sets under every intuitionistic connective and under the permitted modal operator until saturation, with no formula-depth bound. The box-only closure has 3 sets, the diamond-only closure has 6, and the mixed closure has 8 (which includes a non-upset). It directly computes:

\[
\llbracket\Diamond p\rrbracket=\{b\},\quad
\llbracket p\to\Diamond p\rrbracket=\{a,b\},\quad
\llbracket\Box(p\to\Diamond p)\rrbracket=\{a,c\}.
\]

In an independent small-universe check it enumerates every 1- and 2-world labelled preorder, all binary modal relations, and all two-variable persistent valuations. Of 616 configurations, 454 have both unimodal fragments persistent; all 454 also have every mixed formula persistent. This enumeration corroborates, but is not the source of, the separate lower-bound proof for arbitrary vocabularies.

Expected terminal marker: `LOCAL_PERSISTENCE_COUNTEREXAMPLE_VERIFY_OK`.

The construction and proof use no unverified infinite extrapolation. No independent audit has been performed. Historical originality is supported by a direct comparison with Sato's Problem 3.10 and the nearest published relation-condensation study, subject to documented residual risk from older literature.
