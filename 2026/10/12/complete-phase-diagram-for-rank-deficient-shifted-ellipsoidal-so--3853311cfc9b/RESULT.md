# Complete phase diagram for rank-deficient shifted ellipsoidal SOCPs
## Finding

Let
\[
H\succeq0
\]
be a real symmetric singular matrix, let
\[
\delta>0,
\]
and define
\[
C_{\delta,H}
=
\left\{
(t,z):
t\ge
\sqrt{\delta^2+z^{\mathsf T}Hz}
\right\}.
\]
Consider
\[
\inf_{(t,z)\in C_{\delta,H}}
\left(
at+b^{\mathsf T}z
\right).
\]

Write
\[
\mathcal R=\operatorname{Range}(H),
\qquad
\mathcal N=\ker H.
\]

There are two qualitatively different regimes.

If
\[
b\notin\mathcal R,
\]
then the value is
\[
-\infty
\]
for every real \(a\).

If
\[
b\in\mathcal R,
\]
define
\[
\beta
=
\sqrt{b^{\mathsf T}H^\dagger b},
\]
where \(H^\dagger\) is the Moore--Penrose pseudoinverse. Then:

\[
a<\beta
\quad\Longrightarrow\quad
\operatorname{val}=-\infty.
\]

If
\[
a>\beta,
\]
put
\[
\Delta=\sqrt{a^2-\beta^2}.
\]
The optimal value is
\[
\operatorname{val}
=
\delta\Delta,
\]
and the complete minimizer set is
\[
t^*
=
\frac{\delta a}{\Delta},
\qquad
z^*
=
-\frac{\delta}{\Delta}H^\dagger b+k,
\qquad
k\in\mathcal N.
\]
Thus strict copositivity no longer gives a unique primal optimizer: rank deficiency produces an affine family parallel to the nullspace.

If
\[
a=\beta>0,
\]
the value is
\[
0
\]
and it is not attained.

Finally, if
\[
a=\beta=0,
\]
then necessarily \(b=0\), and every feasible point is optimal.

The compatibility condition
\[
b\in\operatorname{Range}(H)
\]
is therefore essential. Merely replacing \(H^{-1}\) by \(H^\dagger\) in the positive-definite formula without checking the nullspace is incorrect: an objective component along \(\ker H\) makes the problem unbounded independently of the coefficient \(a\).

The same compatibility condition appears in the conic dual. Writing the constraint as
\[
(t,H^{1/2}z,\delta)\in\mathcal Q^{n+2},
\]
dual feasibility requires a vector \(u\) satisfying
\[
H^{1/2}u=b.
\]
Such a vector exists exactly when
\[
b\in\operatorname{Range}(H).
\]
Its unique minimum-norm choice is
\[
u_0=(H^\dagger)^{1/2}b,
\qquad
\|u_0\|=\beta.
\]
Hence dual feasibility further requires
\[
a\ge\beta.
\]
For \(a\ge\beta\), the optimal dual choice uses \(u_0\) and the Lorentz coordinate
\[
\nu=-\sqrt{a^2-\beta^2}.
\]
At the nonzero boundary
\[
a=\beta,
\]
the dual optimum is attained with zero gap even though the primal optimum is not attained.

## Assumptions and scope

The theorem concerns the shifted ellipsoidal epigraph above with a positive shift \(\delta\) and a symmetric positive-semidefinite matrix \(H\) that may be rank deficient.

The recent source proves the corresponding phase diagram under the stronger assumption
\[
H\succ0.
\]
Its radial theory also assumes a genuine norm. A singular \(H\) produces only a seminorm, so nullspace directions require a separate analysis.

The statement includes the extreme case in which \(H\) has a nontrivial kernel. If \(H=0\), the same formulas reduce correctly: a nonzero \(b\) gives unboundedness, while for \(b=0\) and \(a>0\) the minimizers have \(t=\delta\) and arbitrary \(z\).

## Proof

Because \(H\) is symmetric,
\[
\mathbb R^n
=
\mathcal R\oplus\mathcal N
\]
orthogonally. Decompose
\[
z=z_{\mathcal R}+z_{\mathcal N}
\]
and
\[
b=b_{\mathcal R}+b_{\mathcal N}.
\]

Since
\[
Hz_{\mathcal N}=0,
\]
we have
\[
z^{\mathsf T}Hz
=
z_{\mathcal R}^{\mathsf T}Hz_{\mathcal R}.
\]
Thus the constraint is completely insensitive to \(z_{\mathcal N}\).

Suppose first that
\[
b_{\mathcal N}\ne0.
\]
Take
\[
z_{\mathcal R}=0,
\qquad
t=\delta,
\qquad
z_{\mathcal N}=-s b_{\mathcal N}
\]
with \(s>0\). These points are feasible for every \(s\), while
\[
at+b^{\mathsf T}z
=
a\delta-s\|b_{\mathcal N}\|^2
\longrightarrow
-\infty.
\]
Hence the problem is unbounded below. Since
\[
b_{\mathcal N}=0
\]
is equivalent to
\[
b\in\mathcal R,
\]
this proves the first branch.

Now assume
\[
b\in\mathcal R.
\]
Both the constraint and the objective are independent of \(z_{\mathcal N}\). Restrict the problem to \(\mathcal R\). On that subspace the restriction
\[
H_{\mathcal R}
\]
is positive definite, and its inverse is exactly the restriction of \(H^\dagger\) to \(\mathcal R\). Therefore
\[
\beta^2
=
b^{\mathsf T}H^\dagger b
\]
is the dual ellipsoidal norm squared on the effective subspace.

The positive-definite ellipsoidal SOCP phase diagram now applies on \(\mathcal R\). For
\[
a<\beta
\]
the reduced problem is unbounded, hence so is the original problem. For
\[
a=\beta>0
\]
the reduced problem has value zero without a minimizer. Adding an arbitrary nullspace component cannot change the reduced variables, so it cannot create attainment.

For
\[
a>\beta,
\]
the reduced problem has the unique solution
\[
t^*
=
\frac{\delta a}{\Delta},
\qquad
z_{\mathcal R}^*
=
-\frac{\delta}{\Delta}
H^\dagger b,
\qquad
\Delta
=
\sqrt{a^2-\beta^2},
\]
with value
\[
\delta\Delta.
\]
Every \(z_{\mathcal N}\in\mathcal N\) leaves feasibility and objective value unchanged. Conversely, every optimizer must have the unique reduced component above. Hence the complete optimizer set is precisely
\[
z^*
=
-\frac{\delta}{\Delta}H^\dagger b+\mathcal N.
\]

If
\[
a=\beta=0,
\]
then \(b=0\), so the objective vanishes identically and every feasible point is optimal.

For the dual statement, use the Lorentz representation
\[
(t,H^{1/2}z,\delta)\in\mathcal Q^{n+2}.
\]
The transverse dual equation is
\[
H^{1/2}u=b.
\]
It is solvable exactly when \(b\in\mathcal R\). Among all solutions, the minimum Euclidean norm is attained uniquely at
\[
u_0=(H^\dagger)^{1/2}b,
\]
and
\[
\|u_0\|^2
=
b^{\mathsf T}H^\dagger b
=
\beta^2.
\]
The Lorentz inequality can therefore hold exactly when
\[
a\ge\beta.
\]
For fixed \(a\) and \(u_0\), maximizing the dual objective chooses
\[
\nu=-\sqrt{a^2-\beta^2},
\]
which gives the same value as the primal strict case and remains feasible at the boundary with \(\nu=0\).

## Verification

The standalone script `artifacts/verify_rank_deficient_socp.py` checks the formulas exactly on diagonal rank-deficient models using rational arithmetic. It verifies nullspace invariance, the pseudoinverse formula, strict-case feasibility and objective value, and explicit unbounded rays when the objective has a nullspace component.

The finite replay is not the proof. The theorem follows from the orthogonal range--kernel decomposition and the positive-definite theorem on the effective quotient subspace.

## Relationship to prior work

Nguyen derives an exact phase diagram for the shifted ellipsoidal SOCP when
\[
H\succ0,
\]
including strict-case uniqueness and nonattainment at the copositive boundary. The same paper's general radial theory assumes a norm, so the seminorm produced by singular \(H\) is outside those hypotheses.

Ben-Tal and Nemirovski explicitly include flat ellipsoids and ellipsoidal cylinders in their robust-optimization framework. That establishes the importance of rank-deficient ellipsoidal geometry, but the inspected treatment does not give the range-compatibility phase diagram above for this shifted epigraph objective.

Kostyukova and Tchemisova give general constraint-qualification-free optimality criteria for linear SOCPs. Their framework is broader, but the inspected paper does not specialize those criteria to the singular shifted-ellipsoid family or derive the pseudoinverse optimizer set and nullspace unboundedness dichotomy.

Targeted searches over singular ellipsoids, pseudoinverse formulations, range compatibility, nullspace unboundedness, and rank-deficient SOCP phase diagrams did not locate a statement that dominates the theorem above.

## Limitations

The finding is an exact extension for one structured SOCP family, not a general theory of singular conic programs.

When \(b\in\operatorname{Range}(H)\), the result reduces the problem to the positive-definite quotient. It does not analyze numerical algorithms for forming that quotient or for computing \(H^\dagger\) stably.

The conditioning formulas in the positive-definite source require care after rank loss because the unreduced Hessian has zero directions. Any condition number should therefore be defined on the effective range space, not on the full ambient space.

## References

1. V. Nguyen, *Attainment Boundaries and Escape Rates in Asymptotically Conic Optimization*, arXiv:2608.10341v1, 2026.
2. A. Ben-Tal, A. Nemirovski, *Robust Convex Optimization*, Mathematics of Operations Research 23(4), 769--805, 1998. DOI: 10.1287/moor.23.4.769.
3. O. Kostyukova, T. Tchemisova, *Exploring constraint qualification-free optimality conditions for linear second-order cone programming*, An International Journal of Optimization and Control: Theories & Applications 14(3), 168--182, 2024. DOI: 10.11121/ijocta.1421.
