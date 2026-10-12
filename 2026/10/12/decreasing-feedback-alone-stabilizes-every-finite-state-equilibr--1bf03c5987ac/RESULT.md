# Decreasing feedback alone stabilizes every finite-state equilibrium in the Situ–Lei stem-cell model

## Finding

Consider the finite-state form of the Situ–Lei stem-cell regeneration model under assumptions (A1)–(A3):
\[
\dot N_i
=
-N_i\bigl(\beta(N)+\gamma_i\bigr)
+
c_i\beta(N)N,
\qquad
N=\sum_{i=1}^nN_i,
\]
where
\[
c_i=2(1-\mu)p_i(1-\kappa_i).
\]

Let
\[
N^*=(N_1^*,\ldots,N_n^*)
\]
be a positive equilibrium and
\[
N_0=\sum_{i=1}^nN_i^*.
\]
Assume
\[
\beta\in C^1,\qquad \beta(N_0)>0.
\]

Then the equilibrium Jacobian is Hurwitz if and only if
\[
\beta'(N_0)<0.
\]

If
\[
\beta'(N_0)=0,
\]
the Jacobian has a zero eigenvalue. If
\[
\beta'(N_0)>0,
\]
the Jacobian has a positive real eigenvalue.

Therefore the additional same-sign hypothesis in Theorem 3.4(ii) of the source is unnecessary. For every finite number of epigenetic states, strictly decreasing population feedback at the positive equilibrium already guarantees local asymptotic stability.

## Assumptions and scope

The result concerns equation (18) in the source, obtained under its assumptions (A1)–(A3): proliferation depends on the total population rather than epigenetic state, apoptosis is state-independent, and daughter-state transition probabilities are independent of the mother state after the statistical-equilibrium simplification.

The equilibrium is assumed positive:
\[
N_i^*>0
\qquad
(1\le i\le n).
\]
Thus the equilibrium fractions
\[
w_i=\frac{N_i^*}{N_0}
\]
are strictly positive and sum to one.

The theorem is a local linear-stability classification. It does not assert global convergence, and it does not apply to the source's more general mother-state-dependent transition matrix before assumption (A3).

## Proof

Write
\[
\beta_0=\beta(N_0),
\qquad
a_i=\beta_0+\gamma_i.
\]
At a positive equilibrium, the source equilibrium formula gives
\[
N_i^*
=
\frac{c_i\beta_0N_0}{a_i}.
\]
Therefore
\[
w_i
=
\frac{N_i^*}{N_0}
=
\frac{c_i\beta_0}{a_i},
\qquad
w_i>0,
\qquad
\sum_{i=1}^nw_i=1.
\]

The source writes the Jacobian in rank-one form. With
\[
D=\operatorname{diag}(a_1,\ldots,a_n)
\]
and \(\mathbf 1\) the all-ones vector,
\[
A=-D+b\mathbf 1^{\mathsf T}.
\]
The row coefficient is
\[
b_i
=
c_i\left(
\beta_0+
\beta'(N_0)N_0\frac{\gamma_i}{a_i}
\right).
\]

Define
\[
r
=
-\frac{N_0\beta'(N_0)}{\beta_0}.
\]
Using
\[
c_i=\frac{w_ia_i}{\beta_0},
\]
one obtains
\[
b_i=w_i(a_i-r\gamma_i).
\]

By the matrix determinant lemma,
\[
\det(\lambda I-A)
=
\prod_{i=1}^n(\lambda+a_i)
\left(
1-\sum_{i=1}^n\frac{b_i}{\lambda+a_i}
\right).
\]
Because
\[
\sum_iw_i=1,
\]
the secular factor reduces exactly to
\[
1-\sum_i\frac{w_i(a_i-r\gamma_i)}{\lambda+a_i}
=
\sum_iw_i
\frac{\lambda+r\gamma_i}{\lambda+a_i}.
\]

Suppose first that
\[
\beta'(N_0)<0.
\]
Then
\[
r>0.
\]
Let
\[
\lambda=x+iy
\]
with
\[
x\ge0.
\]
For every \(i\),
\[
\operatorname{Re}
\frac{\lambda+r\gamma_i}{\lambda+a_i}
=
\frac{
(x+r\gamma_i)(x+a_i)+y^2
}{
(x+a_i)^2+y^2
}
>0.
\]
The weights \(w_i\) are positive, so the weighted sum cannot vanish in the closed right half-plane. The possible pole locations
\[
-a_i
\]
are strictly negative. Hence every eigenvalue of \(A\) has negative real part.

If
\[
\beta'(N_0)=0,
\]
then
\[
r=0
\]
and the secular factor vanishes at
\[
\lambda=0.
\]
Thus the Jacobian is not Hurwitz.

If
\[
\beta'(N_0)>0,
\]
then
\[
r<0.
\]
Along the nonnegative real axis the secular factor is continuous,
\[
\Phi(\lambda)
=
\sum_iw_i
\frac{\lambda+r\gamma_i}{\lambda+a_i}.
\]
At zero,
\[
\Phi(0)
=
r\sum_iw_i\frac{\gamma_i}{a_i}
<0,
\]
whereas
\[
\Phi(\lambda)\to1
\qquad
(\lambda\to+\infty).
\]
The intermediate value theorem therefore gives a positive real eigenvalue.

This proves the exact classification.

The improvement over the source is strict. Take
\[
\beta(N)=e^{-2(N-1)},
\qquad
N_0=1,
\qquad
\mu=0,
\qquad
\kappa_i=0,
\]
and
\[
(p_1,p_2,p_3)=(0.3,0.4,0.3),
\qquad
(\gamma_1,\gamma_2,\gamma_3)=(0.2,1,5).
\]
Then
\[
(c_1,c_2,c_3)=(0.6,0.8,0.6),
\]
and
\[
\sum_i\frac{c_i\beta(N_0)}{\beta(N_0)+\gamma_i}
=
0.5+0.4+0.1
=
1,
\]
so the equilibrium fractions are
\[
(w_1,w_2,w_3)=(0.5,0.4,0.1).
\]
The source's additional sign-test quantities are
\[
\frac23,\quad0,\quad-\frac23,
\]
so they are neither all nonnegative nor all nonpositive. The source's sufficient condition therefore does not apply, while the exact Jacobian spectrum is
\[
-2,\qquad
\frac{-18+8\sqrt3}{5},
\qquad
\frac{-18-8\sqrt3}{5},
\]
which is strictly stable.

## Verification

The bundled `verify.py` reconstructs the three-state strict-extension example with exact rational arithmetic and symbolic characteristic-polynomial factorization.

It verifies the equilibrium identity, confirms the mixed signs in the source's extra condition, derives the Jacobian, and checks that its characteristic polynomial factors with the exact eigenvalues stated above.

The general theorem does not depend on finite enumeration. Its decisive step is the analytic positivity of the real part of each secular summand throughout the closed right half-plane.

## Relationship to prior work

The motivating article proves the two-state equivalence between decreasing feedback and local asymptotic stability. For general finite \(n\), its Theorem 3.4 proves that nonincreasing feedback is necessary and gives a sufficient condition requiring all row-feedback quantities to have the same sign. The result here removes that sign restriction and upgrades the finite-\(n\) statement to the same exact classification already obtained in the source for two states.

The earlier Lei–Levin–Nie model introduced the broader epigenetic-state regeneration framework and population feedback, but it is an optimization and control model rather than the rank-one equilibrium stability calculation treated here.

The breast-cancer state-transition work of Gupta and coauthors motivates equilibrium recovery of phenotypic proportions through stochastic state conversion, but its Markov description does not contain the source's nonlinear population-feedback Jacobian.

Targeted searches by DOI, exact title, theorem number, decreasing-feedback terminology, mixed-sign terminology, and rank-one stability terminology did not locate a published source-specific removal of Theorem 3.4(ii)'s same-sign condition.

## Limitations

The theorem applies only after assumptions (A1)–(A3), especially the simplification that the daughter-state transition probability is independent of the mother state.

The result is local: it proves that the positive equilibrium Jacobian is Hurwitz exactly when the proliferation feedback has negative derivative there. It does not prove global attraction.

At
\[
\beta'(N_0)=0,
\]
the Jacobian has a zero eigenvalue. The nonlinear behavior at that nonhyperbolic case is not classified here.

The first-public-date record used for bibliographic classification is day-resolved in OpenAlex, while the archival publisher page states only that the article was published online in May 2017.

## References

1. Q. Situ, J. Lei, “A mathematical model of stem cell regeneration with epigenetic state transitions,” Mathematical Biosciences and Engineering 14 (2017), 1379–1397. DOI: 10.3934/mbe.2017071.
2. J. Lei, S. A. Levin, Q. Nie, “Mathematical model of adult stem cell regeneration with cross-talk between genetic and epigenetic regulation,” Proceedings of the National Academy of Sciences 111 (2014), E880–E887. DOI: 10.1073/pnas.1324267111.
3. P. B. Gupta et al., “Stochastic state transitions give rise to phenotypic equilibrium in populations of cancer cells,” Cell 146 (2011), 633–644. DOI: 10.1016/j.cell.2011.07.026.
