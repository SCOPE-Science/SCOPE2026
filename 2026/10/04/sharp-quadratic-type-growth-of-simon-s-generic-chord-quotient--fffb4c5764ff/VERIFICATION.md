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

The proof in `RESULT.md` reduces the type count to a finite dihedral-orbit problem. `verify.py` replays that problem directly.

For every \(m=1,\ldots,6\), it enumerates all perfect matchings of the cyclic endpoint set \(\{0,\ldots,2m-1\}\). Each pair is treated as a separately named parameter, so a symmetry is retained only when it preserves every matching edge setwise. The script then computes the induced action of the full dihedral stabilizer on the \(\binom{2m+1}{2}\) unordered pairs of complementary arcs, allowing repeated arcs, and counts the resulting orbits.

The maximal nonalgebraic counts are
\[
2,7,21,36,55,78,
\]
and, after adding the \(m\) equality types, the full maxima are
\[
3,9,24,40,60,84.
\]
For \(m\ge3\), the script also verifies that the adjacent-pair matching \((0,1),(2,3),\ldots\) has trivial pointwise dihedral stabilizer, so every raw placement survives. The output ends with `VERIFY_OK`.

The finite computation is not used to extrapolate the theorem. The general \(m\ge3\) proof is the explicit trivial-stabilizer argument in `RESULT.md`; computation independently checks representative finite cases and the two exceptional small cases.

No independent audit has yet been performed.
