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

The initiating source was inspected in full text.

For a well-formed weighted projective threefold
\[
X=\mathbf P(w_0,w_1,w_2,w_3)
\]
admitting a \(\mathbb Q\)-Gorenstein smoothing to \(\mathbf P^3\), the source proves
\[
(w_0+w_1+w_2+w_3)^3=64w_0w_1w_2w_3.
\]
The family
\[
\mathbf P(1,1,a,b)
\]
is automatically well formed, so the identity applies with no additional hypothesis and becomes
\[
(a+b+2)^3=64ab.
\]

Set
\[
s=a+b.
\]
The exact inequality
\[
ab\le\frac{s^2}{4}
\]
gives
\[
(s+2)^3\le16s^2.
\]
The polynomial
\[
F(s)=(s+2)^3-16s^2
\]
satisfies
\[
F(9)=35>0
\]
and
\[
F'(s)=3s^2-20s+12>0
\]
for \(s\ge9\). Thus \(s\le8\).

Because
\[
ab=\frac{(s+2)^3}{64}
\]
is an integer, \(64\mid(s+2)^3\). For \(4\le s+2\le10\), this forces \(4\mid s+2\), so
\[
s+2\in\{4,8\}.
\]
The two cases give
\[
(s,ab)=(2,1)\quad\text{or}\quad(6,8),
\]
hence
\[
\{a,b\}=\{1,1\}\quad\text{or}\quad\{2,4\}.
\]

The source and its primary predecessor were checked for sufficiency. The ordinary projective case is trivial, and \(\mathbf P(1,1,2,4)\) is explicitly recorded as a known \(\mathbb Q\)-Gorenstein degeneration of \(\mathbf P^3\).

No computational enumeration is used in the proof. The only unresolved issue is bibliographic rather than mathematical: one highly relevant recent preprint could not be inspected in full text and is therefore retained as an originality risk.
