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

The verification uses only exact set-theoretic identities and four checked source statements.

For
\[
Q=\{A\subseteq D:D\setminus A\text{ is finite}\},
\]
the dual is
\[
Q^d=\{A\subseteq D:A\text{ is infinite}\}.
\]
For
\[
P_0=\{A:|A\cap X|\ge2\},
\]
we have
\[
P_0^d=\{A:|X\setminus A|\le1\}.
\]
For
\[
P_1=\{A:|A\cap Y|=\aleph_1\},
\]
we have
\[
P_1^d=\{A:|Y\setminus A|\le\aleph_0\}.
\]
Hence
\[
P^d=P_0^d\cap P_1^d.
\]

The source's Lemma 4.4 applies twice. First, \(P_0\) is \(\omega\)-small and \(Q\) is \(\omega\)-complete, so
\[
P_0\cdot Q=P_0\boxtimes Q.
\]
Second, \(Q^d\) is \(\omega_1\)-small and \(P_1^d\) is \(\omega_1\)-complete, so
\[
Q^d\cdot P_1^d=Q^d\boxtimes P_1^d.
\]
Proposition 2.4 transfers the second dominance statement through duality, and Lemma 7.1 combines the two outer components.

For the lower failure, the relation with rows
\[
R_y=D\setminus\{y\}\quad(y\in Y),
\qquad
R_x=\varnothing\quad(x\in X)
\]
belongs to \(P\cdot Q\). Any supposed \(P\)-by-\(Q\) rectangle must use an uncountable first-coordinate set contained in \(Y\), and a cofinite second-coordinate set. These sets intersect, forcing a forbidden diagonal point.

For the upper failure, choose distinct \(x_n\in X\) and \(k_n\in Y\), and use rows
\[
S_{k_n}=D\setminus\{x_n\}.
\]
The set of large rows is countably infinite, so \(S\in Q^d\cdot P^d\). Any branching rectangle would require its second-coordinate set to omit infinitely many \(X\)-points, contradicting the exact dual condition \(|X\setminus B|\le1\).

Finally, the checked countable-domain theorem states that dominance on a countable domain forces one of the two branching equalities. Therefore no smaller cardinal can support a counterexample, and the construction on \(\aleph_1\) is minimal.

No finite enumeration, probabilistic experiment, or unproved infinitary extrapolation is used. The only cardinal closure fact beyond the definitions is that a countable union of countable sets is countable in ZFC.
