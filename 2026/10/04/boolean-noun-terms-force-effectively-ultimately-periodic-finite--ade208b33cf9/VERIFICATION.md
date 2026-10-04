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

The verification is symbolic.

Let the finite theory mention raw nouns
\[
p_1,\ldots,p_r.
\]
The \(2^r\) Boolean atoms determined by these nouns partition every finite model. Assign a nonnegative integer variable \(z_\varepsilon\) to each atom.

Every Boolean noun term is a union of atoms, so its cardinality is a \(0/1\) linear form in the \(z_\varepsilon\). The four syllogistic atomic forms translate exactly to:

\[
\text{inclusion: a linear sum equals }0,
\]
\[
\text{overlap: a linear sum is at least }1,
\]
\[
\text{weak comparison: one linear sum is at least another},
\]
\[
\text{strict comparison: one linear sum is at least another plus }1.
\]

Thus model existence at total size
\[
N=\sum_\varepsilon z_\varepsilon
\]
is an existential Presburger formula. Presburger quantifier elimination yields an effective semilinear description, and one-dimensional semilinear sets are ultimately periodic.

Dilation closure is checked independently: replacing every model element by \(m\) copies multiplies every noun cardinality by \(m\) while preserving inclusion, nonemptiness, weak comparison, and strict comparison.

For \(\Delta_k\), pairwise disjointness plus
\[
\overline{x_1}\subseteq x_2\vee\cdots\vee x_k
\]
forces a partition of the universe into \(k\) blocks. Paired weak comparisons force the block cardinalities equal. Hence the model size is exactly a positive multiple of \(k\), and every positive multiple is realized by an equal-block partition.

## Limits

The proof does not give a complete converse characterization of realizable semilinear sets. It also does not claim efficient Presburger elimination or cover infinitary theories.
