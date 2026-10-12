# A fixed cupping pair simultaneously excludes any prescribed countable family below the target
## Finding

Let \(C\) be computably enumerable, let
\[
A,B<_T C
\quad\text{and}\quad
A\nleq_T B,
\]
and let
\[
(E_n)_{n\in\omega}
\]
be a sequence of noncomputable sets such that the uniform join satisfies
\[
\bigoplus_{n\in\omega}E_n\leq_T B.
\]

Then there are fixed sets
\[
X_0,X_1\leq_T C
\]
such that, for each \(j<2\),
\[
B\leq_T A\oplus X_j,
\]
while for every \(n\in\omega\),
\[
\neg\bigl(E_n\leq_T X_0\ \wedge\ E_n\leq_T X_1\bigr).
\]

Equivalently, no Turing degree \(\deg_T(E_n)\) from the prescribed countable family is a common lower bound of both \(\deg_T(X_0)\) and \(\deg_T(X_1)\).

## Assumptions and scope

Fix a computable pairing function
\[
q:\omega^2\to\omega.
\]
Define a set \(D\) by columns:
\[
D(q(0,m))=B(m)
\]
and
\[
D(q(n+1,m))=E_n(m)
\]
for \(n,m\in\omega\).

Because the uniform join of the \(E_n\) is Turing reducible to \(B\), one has
\[
D\leq_T B.
\]
Conversely \(B\) is a computable column of \(D\), so
\[
B\leq_T D.
\]
Hence
\[
D\equiv_T B.
\]
In particular,
\[
D\leq_T C
\quad\text{and}\quad
A\nleq_T D.
\]

The conclusion is a prescribed-family avoidance theorem. It does **not** assert that \(X_0\) and \(X_1\) form a minimal pair or that they have no noncomputable common lower bound outside the designated countable family.

## Proof

Cintioli's structural two-witness theorem is formulated for an arbitrary finite effective certificate rule satisfying the protocol's admissibility requirements. Applied to \(A,D,C\), it produces total
\[
X_0,X_1\leq_T C
\]
with
\[
D\leq_T A\oplus X_j
\]
for each \(j<2\), provided the chosen certificate requirements are met.

Enumerate effectively all triples
\[
(n,e_0,e_1)\in\omega^3.
\]
For the requirement indexed by such a triple, write \(\Phi_{e_j}\) for the functional on side \(j\), and impose
\[
R_{n,e_0,e_1}:
\quad
\Phi_{e_0}^{X_0}\neq E_n
\ \text{or}\
\Phi_{e_1}^{X_1}\neq E_n.
\]

Use the certificate rule from Cintioli's designated-column lemma, with the sole change that the distinguished coordinate for an input \(m\) is
\[
q(n+1,m)
\]
instead of the single fixed odd column used there.

Concretely, when the protocol has a safe side \(j\) and a finite splitting for \(\Phi_{e_j}\) above the current candidate at input \(m\), choose a finite length \(k\) larger than both the current restraint and
\[
q(n+1,m).
\]
For each finite candidate \(\gamma\in2^k\), the certificate extension follows the branch whose functional output at \(m\) is
\[
1-\gamma(q(n+1,m)).
\]
This rule depends only on the finite requirement data \((n,e_0,e_1,m)\) and a finite approximation \(\gamma\), so it remains finite, effective, and of exactly the form permitted by the structural theorem.

The verification is the same diagonal argument as in the designated-column lemma.

If a requirement receives a certificate, then on the true long root the bit
\[
\gamma(q(n+1,m))
\]
is exactly
\[
D(q(n+1,m))=E_n(m).
\]
The chosen branch therefore forces the corresponding functional to output the opposite bit, so that requirement is met.

Suppose instead that a requirement were never certified and nevertheless both equalities
\[
\Phi_{e_0}^{X_0}=E_n
\quad\text{and}\quad
\Phi_{e_1}^{X_1}=E_n
\]
held. On either side, permanent absence of the finite splitting used by the source argument would make \(E_n\) computable from the finite base data. Since \(E_n\) is noncomputable, the needed splittings must eventually appear. The source protocol's safe-side invariant then forces one of them to be used for a certificate, contradicting the assumption that the requirement remained uncertified. Hence every requirement \(R_{n,e_0,e_1}\) holds.

Now fix \(n\). If both
\[
E_n\leq_T X_0
\quad\text{and}\quad
E_n\leq_T X_1,
\]
choose indices \(e_0,e_1\) witnessing those reductions. The corresponding requirement \(R_{n,e_0,e_1}\) is in the enumeration and would fail, a contradiction. Therefore no \(E_n\) is computable from both witnesses.

Finally, since \(B\leq_T D\) and
\[
D\leq_T A\oplus X_j,
\]
one obtains
\[
B\leq_T A\oplus X_j
\]
for both \(j<2\), as required.

## Verification

The recent source was inspected at the three points needed for the argument.

First, its main two-witness construction provides \(X_0,X_1\leq_T C\) with the required cupping conclusion from a set \(D\leq_T C\) satisfying \(A\nleq_T D\).

Second, the structural theorem explicitly allows any finite effective certificate rule meeting the construction's admissibility conditions. The rule above only replaces one designated coordinate by the computably decoded coordinate
\[
q(n+1,m),
\]
so it does not alter the finite nature of the certificate mechanism.

Third, the source's designated-column lemma proves exactly the local diagonal step used here: if a noncomputable designated column were computed by both sides, the splitting argument and safe-side invariant force a certificate and hence a contradiction. The present proof applies that same finite step separately to the target index decoded by each requirement.

No finite experiment or exhaustive computation is used.

## Relationship to prior work

Cintioli proves one-target avoidance: given a noncomputable target \(E\), two cupping witnesses can be chosen so that \(E\) is not computable from both. The paper also explicitly notes the limitation that the witnesses may depend on the avoided target and that this does not construct a fixed pair with no nonzero common lower bound.

The present observation keeps one fixed pair while diagonalizing against a prescribed **countable** family whose uniform join lies below the cupping target \(B\). The extra step is to place all targets into separate columns of a single set \(D\equiv_T B\) and enumerate the target index together with the two candidate reductions.

Classical simultaneous cone-avoidance theorems work in a different relativized framework: the avoided sets are required to be noncomputable relative to the base oracle. Here each \(E_n\) is allowed, and indeed required uniformly, to lie below \(B\), because \(B\) is the object that both witnesses cup with \(A\). Taking the classical base oracle to contain \(B\) makes the \(E_n\) base-computable, so those simultaneous-cone results do not directly imply this fixed-pair cupping statement.

## Limitations

Uniformity is essential to the stated coding argument:
\[
\bigoplus_n E_n\leq_T B
\]
is used to obtain a single set \(D\equiv_T B\) containing all target columns. Merely assuming each \(E_n\leq_T B\) separately does not provide that uniform reduction.

Every \(E_n\) is assumed noncomputable, since the contradiction from a permanently absent splitting uses noncomputability.

The theorem excludes only the prescribed countable family. It does not show that the two witnesses have no other nonzero common lower bound, and therefore does not settle the full fixed-pair minimality question highlighted by the source.

## References

[1] Patrizio Cintioli, “Cone Avoidance and the No-Least-Join Theorem,” arXiv:2610.02027v1, first posted 1 October 2026.

[2] Rod Downey, Noam Greenberg, Matthew Harrison-Trainor, Ludovic Patey, and Dan Turetsky, “Relationships between computability-theoretic properties of problems,” *Journal of Symbolic Logic* 87 (2022), 47–71, DOI 10.1017/jsl.2020.38; arXiv:1903.04273.

[3] Rod Downey, Noam Greenberg, Andrew E. M. Lewis, and Antonio Montalbán, “Extensions of embeddings below computably enumerable degrees,” *Transactions of the American Mathematical Society* 365 (2013), 2977–3018, DOI 10.1090/S0002-9947-2012-05660-1.
