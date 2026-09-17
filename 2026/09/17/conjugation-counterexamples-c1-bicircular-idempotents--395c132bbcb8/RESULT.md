# Conjugation-generated counterexamples to the \(C^1\) generalized bi-circular idempotent dichotomy

Let
\[
X=C^1[0,1],\qquad \|f\|_\sigma=|f(0)|+\|f'\|_\infty .
\]
The isometric identification
\[
J:X\longrightarrow \mathbb C\oplus_1 C[0,1],\qquad
Jf=(f(0),f')
\]
makes a conjugation obstruction to the proposed classification of generalized
bi-circular idempotents explicit.

## The counterexample family

Fix arbitrary distinct \(\lambda,\mu\in\mathbb T\).  On \(\mathbb C\), let
\(Cz=\overline z\), and define the real-linear maps
\[
Q_\lambda=\frac{C-\mu I}{\lambda-\mu},\qquad
Q_\mu=\frac{\lambda I-C}{\lambda-\mu}=I-Q_\lambda .
\]
For every \(z\in\mathbb C\),
\[
\overline{Q_\lambda z}=\lambda Q_\lambda z,\qquad
\overline{Q_\mu z}=\mu Q_\mu z.
\]
Thus \(Q_\lambda\) and \(Q_\mu\) are complementary real-linear projections
onto the two real lines
\[
L_\nu=\{z\in\mathbb C:\overline z=\nu z\}\quad(\nu=\lambda,\mu).
\]
Apply these projections pointwise to \(C[0,1]\), and define
\[
JP_1J^{-1}(a,g)=(a,Q_\lambda g),\qquad
JP_2J^{-1}(a,g)=(0,Q_\mu g).
\]
Then \(P_1,P_2\) are distinct nonzero real-linear idempotents,
\[
P_1+P_2=I,\qquad P_1P_2=P_2P_1=0.
\]
Moreover
\[
J(\lambda P_1+\mu P_2)J^{-1}(a,g)
   =(\lambda a,\overline g).
\]
Consequently the associated map is
\[
(Tf)(t)=\lambda f(0)+\int_0^t\overline{f'(s)}\,ds,
\]
a surjective isometry of Form III in the terminology of
Kumar--Kumar--Abu Baker, with \(c=\lambda\), \(\beta\equiv1\), and
\(\phi=\mathrm{id}\).  Hence \(\{P_1,P_2\}\) is a generalized
bi-circular idempotent family for every distinct pair
\(\lambda,\mu\in\mathbb T\).

It is never a bi-circular family.  Choose unit generators
\(u_\lambda\in L_\lambda\) and \(u_\mu\in L_\mu\), put
\[
\rho=\frac{u_\lambda}{u_\mu}\in\mathbb T,
\]
and take \(f(t)=t(u_\lambda-u_\mu)\).  Then
\[
(P_1f)'=u_\lambda,\qquad (P_2f)'=-u_\mu,
\]
so
\[
(P_1+\rho P_2)f=0
\]
although \(f\ne0\).  Thus \(P_1+\rho P_2\) is not an isometry.

Taking, for example, \((\lambda,\mu)=(1,i)\) gives
\(\lambda+\mu=1+i\ne0\).  Therefore this family contradicts the dichotomy
stated in the abstract of arXiv:2609.18967v1, which asserts that an
associated isometry can occur only when \(\lambda_1+\lambda_2=0\) or the
family is bi-circular.  It also directly contradicts Theorem 3.3, which
claims that every Form III generalized bi-circular idempotent family is
bi-circular.

## Form IV has the same obstruction

Define instead
\[
J\widetilde P_1J^{-1}(a,g)=(Q_\lambda a,Q_\lambda g),\qquad
J\widetilde P_2J^{-1}(a,g)=(Q_\mu a,Q_\mu g).
\]
Then
\[
J(\lambda\widetilde P_1+\mu\widetilde P_2)J^{-1}(a,g)
=(\overline a,\overline g),
\]
which is the Form IV surjective isometry
\[
(\widetilde T f)(t)=\overline{f(0)}
+\int_0^t\overline{f'(s)}\,ds.
\]
The same cancellation argument with \(f(0)=0\) shows that
\(\{\widetilde P_1,\widetilde P_2\}\) is not bi-circular.  Hence Theorem
3.4 of arXiv:2609.18967v1 is also false as stated.

## A separate phase error in Forms I and II

The displayed equations (3.4) and (3.6) of arXiv:2609.18967v1 give
\[
\beta(t)\beta(\phi(t))f'(\phi^2(t))
-(\lambda_1+\lambda_2)\beta(t)f'(\phi(t))
+\lambda_1\lambda_2 f'(t)=0.
\]
In the nontrivial involutive branch \(\phi^2=\mathrm{id}\) and
\(\lambda_2=-\lambda_1\), this forces
\[
\boxed{\beta(t)\beta(\phi(t))=\lambda_1^2},
\]
not \(\pm\lambda_1\) as stated in Theorems 3.1 and 3.2.  The corrected
relation is also the one compatible with multiplying the associated
isometry by a common unimodular phase: the left side has phase weight two.

## Mechanism

The source of the Form III/IV obstruction is that conjugation is
real-linear rather than complex-linear.  A conjugation has a real
one-dimensional eigenspace \(L_\nu\) for every \(\nu\in\mathbb T\).
For any two distinct unit phases, the corresponding two eigendirections
form a real direct sum of \(\mathbb C\), and their real spectral
projections are idempotent.  This permits
\[
C=\lambda Q_\lambda+\mu Q_\mu
\]
for arbitrary distinct \(\lambda,\mu\).  Idempotence of the resulting
real-linear projections does not imply that arbitrary complex phase
combinations of them are isometries.  The last step of the proofs of
Theorems 3.3 and 3.4 makes precisely that unsupported inference.

## Relation to prior literature

Botelho--Miura's 2019 corrigendum corrected an earlier incomplete
classification of generalized bi-circular idempotents on a different
family of norms on spaces of continuously differentiable functions.  Its
abstract explicitly records that the earlier proposition omitted a case.
The 2026 paper cites that corrigendum but studies the specific norm
\(|f(0)|+\|f'\|_\infty\).

A closely related 2026 paper by Kumar--Abu Baker--Botelho on analytic
derivative spaces already emphasizes that generalized bi-circular
idempotents are only real-linear in general and gives a scalar
real-linear example.  Its Theorem 3.3 nevertheless contains a similar
conclusion that a conjugation-type Form III family is bi-circular.
The present result concerns the explicit \(C^1[0,1]\) classification in
arXiv:2609.18967v1 and supplies a phase-adapted counterexample family for
every pair of distinct unit phases.

## Sources

- H. Kumar, H. Kumar, A. B. Abu Baker, *Structure of Generalized bi-circular idempotents and isometric reflections on \(C^1[0,1]\)*, arXiv:2609.18967v1:
  https://arxiv.org/abs/2609.18967v1
- F. Botelho, T. Miura, *Corrigendum to “Examples of generalized bi-circular idempotents on spaces of continuously differentiable functions”*, J. Math. Anal. Appl. 474 (2019), 1481--1487:
  https://doi.org/10.1016/j.jmaa.2019.02.032
- H. Kumar, A. B. Abu Baker, F. Botelho, *Generalized bi-circular idempotents on some spaces of analytic functions*:
  https://profile.iiita.ac.in/abdullah/F13.pdf

## Limitation

This record addresses the statements in arXiv:2609.18967v1 as written.
A later revision may alter the hypotheses or conclusions.  It does not
claim that every other result in the preprint is invalid, nor does it
supply a complete replacement classification for all four isometry forms.
