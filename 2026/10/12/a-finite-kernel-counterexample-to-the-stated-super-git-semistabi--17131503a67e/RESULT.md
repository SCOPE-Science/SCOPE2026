# A finite-kernel counterexample to the stated super-GIT semistability criterion
## Finding
Let \(m\ge 2\) and work over \(\mathbf C\). Set
\[
G=\mathbf G_m,\qquad X=\mathbf A^1=\operatorname{Spec}\mathbf C[x],
\]
and let the action be the weight-\(m\) action, written as the coaction
\[
\rho(x)=x\otimes t^m.
\]
Let \(\Delta=\mu_m\subset G\) and let \(\chi=t\) be the identity character of \(G\).

Then \(\Delta\) acts trivially on \(X\), but the restriction of the chosen character is not trivial:
\[
r_\Delta(\chi)=u\neq 1
\]
in
\[
\mathbf C[u,u^{-1}]/(u^m-1),
\]
and \(u\) has exact order \(m\).

Despite this, the semistable and stable loci in the definition of Quintero Vélez--Rizzo--Torres-Gomez are both
\[
X^{ss}_\chi=X^s_\chi=D(x)=\mathbf A^1\setminus\{0\}.
\]
Consequently the condition \(r_\Delta(\chi)=1\) asserted as necessary in Lemma 4.8, and imported into the forward direction of Theorem 4.12(1), is false even for a purely even reductive group acting on an ordinary affine scheme.

More generally, the argument in that lemma proves only the torsion conclusion
\[
r_\Delta(\chi)^n=1
\]
for the degree \(n\) of a semistability witness. Thus nonempty semistability forces \(r_\Delta(\chi)\) to have finite order, but does not force it to be trivial.

## Assumptions and scope
The base field is \(\mathbf C\). This avoids any issue about nonreduced roots of unity and makes \(\mu_m\) a reduced finite subgroup of \(\mathbf G_m\). The acting group is purely even, so the source's odd-infinitesimal decoupling condition is vacuous. The subgroup \(\Delta=\mu_m\) is closed and normal, and it acts trivially because restriction sends \(t^m\) to \(1\).

The claim concerns the necessity of \(r_\Delta(\chi)=1\) in Lemma 4.8 and Theorem 4.12(1) of arXiv:2609.14904v1. It does not claim that the orbit-closure equivalence in Lemma 4.8(1), the sufficiency direction of Theorem 4.12(1), or the remaining results of the paper are false.

## Proof
Write
\[
A=\mathbf C[x],\qquad \mathbf C[G]=\mathbf C[t,t^{-1}],
\]
with
\[
\rho(x)=x\otimes t^m.
\]
Restriction to \(\Delta=\mu_m\) sends \(t\) to the class \(u\) in
\[
\mathbf C[\mu_m]=\mathbf C[u,u^{-1}]/(u^m-1).
\]
Therefore
\[
(\operatorname{id}\otimes r_\Delta)\rho(x)
=x\otimes u^m=x\otimes1,
\]
so the induced \(\Delta\)-coaction is trivial. On the other hand, \(r_\Delta(\chi)=u\), and \(u\) has exact order \(m\), hence is nontrivial for \(m\ge2\).

The source defines a point to be \(\chi\)-semistable when some integer \(n\ge1\) and some even relative invariant of weight \(\chi^n\) do not vanish there. Here
\[
\rho(x)=x\otimes\chi^m,
\]
so \(x\) is a relative invariant of weight \(\chi^m\). It follows immediately that every point of \(D(x)\) is \(\chi\)-semistable.

Conversely, the monomial \(x^d\) has weight \(\chi^{md}\). Since the \(G\)-weights in \(A\) are exactly the nonnegative multiples of \(m\),
\[
A^{G,\chi^n}=
\begin{cases}
\mathbf Cx^d,&n=md,\\
0,&m\nmid n.
\end{cases}
\]
Every positive-degree relative invariant therefore vanishes at the origin. Hence the origin is not semistable and
\[
X^{ss}_\chi=D(x).
\]

For a nonzero point, its \(G\)-orbit is all of \(D(x)\), which is closed in itself. Its stabilizer is exactly \(\mu_m\), so the effective quotient \(G/\Delta\) acts freely and the orbit dimension equals \(\dim(G/\Delta)=1\). Thus every semistable point is stable:
\[
X^s_\chi=X^{ss}_\chi=D(x).
\]

The graded relative-invariant algebra is
\[
R=\bigoplus_{n\ge0}A^{G,\chi^n},
\]
with
\[
R_{md}=\mathbf Cx^d
\]
and all other positive graded pieces zero. Equivalently, \(R\cong\mathbf C[x]\) with \(\deg x=m\), so
\[
\operatorname{Proj}R\cong\operatorname{Spec}\mathbf C.
\]

Finally, the source's proof correctly derives, from any semistability witness \(f\) of weight \(\chi^n\),
\[
r_\Delta(\chi)^n=1.
\]
The example above realizes the missing possibility with exact order \(m\): the witness degree is \(n=m\), while \(r_\Delta(\chi)\neq1\). This disproves the stronger asserted necessity.

## Verification
The hypotheses were checked directly against arXiv:2609.14904v1: the definition of semistability allows an arbitrary witness degree \(n\ge1\); Section 4.2 permits a closed normal subgroup \(\Delta\) with trivial induced coaction; Lemma 4.8 asserts \(r_\Delta(\chi)=1\) as necessary; and Theorem 4.12(1) uses that condition in its semistability characterization.

No finite experiment is needed for the proof. The computation is an identity in the Hopf algebra of \(\mathbf G_m\) and its quotient by \(t^m-1\). As an additional consistency check, the numerical half of Theorem 4.12(1) does not cause the failure: a one-parameter subgroup \(t\mapsto t^q\) gives a polynomial coextension of the weight-\(m\) action exactly when \(q\ge0\), and then \(\langle\chi,\lambda\rangle=q\ge0\). Thus the obstruction is precisely the extra requirement \(r_\Delta(\chi)=1\).

## Relationship to prior work
Quintero Vélez, Rizzo, and Torres-Gomez define semistability by the existence of a nonvanishing relative invariant of some positive character power. Their proof of Lemma 4.8 derives \(r_\Delta(\chi)^n=1\) for the witness degree \(n\), then strengthens this to \(r_\Delta(\chi)=1\). The explicit weight-\(m\) action above shows that this strengthening is not merely unproved: it is false.

A public review of arXiv:2609.14904v1 independently identifies the same logical gap and notes that a nontrivial finite-order group-like element could occur. That review does not exhibit a semistable counterexample. The family above supplies such counterexamples for every \(m\ge2\), determines the exact semistable and stable loci, and computes the resulting graded quotient.

Targeted searches for the source identifier, the restriction condition, finite ineffective kernels, character descent, and the specific \(\mathbf G_m\)-on-\(\mathbf A^1\) construction found no checked source stating this explicit counterexample or its quotient calculation.

## Limitations
This finding is a counterexample to one necessary condition in the stated semistability criterion. It does not supply a complete corrected Hilbert--Mumford theorem for arbitrary superschemes. Replacing triviality by torsion is necessary for the implication proved from a semistability witness, but additional hypotheses may be needed for a full if-and-only-if criterion.

A later correction, revision, or poorly indexed note could independently contain the same explicit family; none was found in the checked sources.

## References
1. Alexander Quintero Vélez, Pedro Rizzo, Alexander Torres-Gomez, *Geometric Invariant Theory for Affine Superschemes*, arXiv:2609.14904v1 (2026).
2. Pith, *Review of Geometric Invariant Theory for Affine Superschemes*, record ZDF7UWRA (2026).
