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

The all-arity theorem in `RESULT.md` is structural: a finite injective point tuple determines a strict chain of threshold equivalence relations, every such chain reconstructs an ordinal ultrametric, and dc-homogeneity turns equality of finite dc-types into equality of global automorphism orbit.

`verify.py` independently replays the exact finite combinatorics without using OEIS data as an oracle. It:

1. Generates every set partition as a restricted-growth string.
2. Counts every strict chain from the discrete partition to the indiscrete partition for \(1\le n\le7\), recovering
   \[
   1,1,4,32,436,9012,262760.
   \]
3. Computes the same values from the Stirling recurrence and asserts equality.
4. Explicitly enumerates every partition chain for \(n\le5\), converts each pair to its first-merge level, and checks the ultrametric inequality for every ordered triple.
5. Computes the repeated-coordinate Stirling transform through \(n=7\), obtaining
   \[
   1,2,8,64,872,18024,525520,
   \]
   and checks \(b_n=2a_n\) for every tested \(n\ge2\).

The bundled output ends with `VERIFY_OK`.

The finite computation is a replay of arithmetic and encoding, not evidence from which the infinite theorem is extrapolated. The extension from finite dc-isomorphism to global automorphism uses the source-supported dc-homogeneity of the Fraïssé limit.

No independent audit has yet been performed.
