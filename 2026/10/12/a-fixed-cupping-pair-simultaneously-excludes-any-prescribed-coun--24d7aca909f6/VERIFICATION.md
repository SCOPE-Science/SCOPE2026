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
D(q(0,m))=B(m)
\]
and
\[
D(q(n+1,m))=E_n(m).
\]
The uniform reduction
\[
\bigoplus_n E_n\leq_T B
\]
gives
\[
D\leq_T B,
\]
while the zeroth column gives
\[
B\leq_T D.
\]
Hence
\[
D\equiv_T B,
\quad
D\leq_T C,
\quad
A\nleq_T D.
\]

Enumerate all triples
\[
(n,e_0,e_1).
\]
At the corresponding requirement impose
\[
\Phi_{e_0}^{X_0}\neq E_n
\quad\text{or}\quad
\Phi_{e_1}^{X_1}\neq E_n.
\]

The source's structural protocol allows a finite effective certificate rule. Use its designated-column rule, replacing the single distinguished column coordinate by
\[
q(n+1,m)
\]
for the target index \(n\) decoded from the requirement.

For a finite splitting at input \(m\), choose a finite approximation length \(k\) exceeding the distinguished coordinate. The certificate branch is selected to output the complement of the finite approximation at that coordinate. Along the true root, that coordinate equals \(E_n(m)\), so certification diagonalizes against the selected functional.

If both sides computed \(E_n\) and the requirement never certified, the source's splitting argument would force the necessary finite splittings because \(E_n\) is noncomputable; the safe-side invariant would then force certification, contradiction. Therefore every triple requirement succeeds.

If some \(E_n\) were reducible to both \(X_0\) and \(X_1\), the indices of those two reductions would occur in the enumeration and violate their requirement. Thus
\[
\neg(E_n\leq_T X_0\wedge E_n\leq_T X_1)
\]
for every \(n\).

The structural theorem also yields
\[
D\leq_T A\oplus X_j
\]
for \(j<2\), and hence
\[
B\leq_T A\oplus X_j.
\]

## Limits

The proof uses uniform reducibility of the whole target sequence to \(B\).

Every target is assumed noncomputable.

The argument excludes only the designated countable family and does not establish a minimal pair.

No numerical computation or finite experimental evidence is used.
