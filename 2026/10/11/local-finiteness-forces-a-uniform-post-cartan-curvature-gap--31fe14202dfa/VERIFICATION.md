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

Let
\[
F_n=\mathcal E_n^{(3)}\cap(2n,2n+1].
\]
The local-finiteness theorem makes \(F_n\) finite. Therefore
\[
D_n=\{s-2n:s\in F_n\}\cup\{1\}
\]
is a finite nonempty subset of the positive reals, so
\[
\delta_n=\min D_n>0.
\]

If an admissible value satisfies
\[
2n<S\le2n+1,
\]
then by definition
\[
S-2n\ge\delta_n.
\]
If
\[
S>2n+1,
\]
then
\[
S-2n>1\ge\delta_n.
\]
Thus every admissible value strictly above \(2n\) satisfies
\[
S\ge2n+\delta_n.
\]

The second-gap theorem supplies the remaining dichotomy:
\[
S>n\Longrightarrow S\ge2n.
\]
Its equality classification says that, for \(n\ge5\), the level \(2n\) is realized exactly by minimal Cartan hypersurfaces and only in dimensions
\[
6,\ 12,\ 24.
\]

No computation, finite sample, or numerical search is used in the proof. The verification consists of checking the exact scope of the two primary theorems and the elementary finite-set implication above.
