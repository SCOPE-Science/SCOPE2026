# Boundary-charge criterion for subcritical perturbed Brownian reflection

## Statement

Let \(B\) be a standard Brownian motion, \(x\ge 0\), \(\nu<1/2\), and let
\(b:[0,\infty)\to\mathbb R\) be deterministic, continuous, locally of finite
variation, with \(b(0)=0\). Consider
\[
W_t=(1-\nu)x+B_t+\nu M_t(W)+\frac12L_t^0(W-b),
\qquad W_t\ge b(t),
\tag{1}
\]
where \(M_t(W)=\sup_{s\le t}W_s\), and local time uses the normalization in
Wang (2026).

Put
\[
\nu^*=\frac{\nu}{1-\nu},\qquad
R=\begin{pmatrix}1&\nu^*\\-1&1\end{pmatrix}.
\]
Since \(\nu<1/2\),
\[
\rho(|I-R|)=\sqrt{|\nu^*|}<1.
\]
Hence the orthant Skorokhod problem with driver
\[
\binom{x+B_t-b(t)}{-B_t}
\]
has a unique continuous adapted solution
\[
\binom{X_t}{Y_t}
=
\binom{x+B_t-b(t)}{-B_t}
+
R\binom{K_t}{V_t},
\tag{2}
\]
where \(K,V\) are continuous nondecreasing, \(dK\) is supported on
\(\{X=0\}\), and \(dV\) on \(\{Y=0\}\).

Define \(W=X+b\) and \(F=M(W)-b\).

### Theorem 1: exact regulator-local-time defect

Almost surely, on every finite interval, the following signed-measure identity
holds:
\[
\boxed{
d\!\left(K-\frac12L^0(X)\right)
=
\mathbf 1_{\{X=0,F>0\}}\,db
+
(1-\nu)\mathbf 1_{\{X=0,F=0\}}\,db .
}
\tag{3}
\]

Consequently,
\[
\boxed{
K=\frac12L^0(X)\ \text{on }[0,T]
\quad\Longleftrightarrow\quad
|db|\bigl(\{t\le T:X_t=0\}\bigr)=0 .
}
\tag{4}
\]

Thus, for \(\nu<1/2\), equation (1) has a strong solution if and only if the
unique orthant-Skorokhod candidate has zero boundary-variation charge on its
contact set. Whenever a solution exists, it is pathwise unique.

### Theorem 2: all locally absolutely continuous boundaries are well posed

If \(b\) is locally absolutely continuous, then for every \(x\ge0\) and every
\(\nu<1/2\), equation (1) has a pathwise unique strong solution.

Indeed, the martingale part of \(X\) is \(B\), so
\(\langle X\rangle_t=t\). Occupation density implies
\[
\operatorname{Leb}\{t\le T:X_t=0\}=0
\quad\text{a.s.}
\]
For \(db=b'(t)\,dt\), this gives
\[
|db|\bigl(\{X=0\}\cap[0,T]\bigr)=0,
\]
and Theorem 1 applies.

In particular, for every \(c>0\) and every \(\alpha>0\),
\[
b(t)=ct^\alpha
\]
is admissible when \(\nu<1/2\). For \(\alpha=1/2\), the upward modulus is of
order \(\sqrt h\), not \(o(\sqrt h)\); for \(0<\alpha<1/2\), it is even larger.
Hence these examples lie outside Wang's condition (PB) while remaining strongly
well posed in the subcritical perturbation regime.

### Corollary: the increasing-boundary no-charge condition is sufficient

If \(b\) is continuous and increasing, then for \(\nu<1/2\) the local-time
equation (1) has a solution if and only if the unique orthant candidate satisfies
\[
\int_0^T\mathbf 1_{\{W_t=b(t)\}}\,db(t)=0
\qquad\text{for every }T>0.
\tag{5}
\]
Wang's Lemma 6.1 proves this condition is necessary for every \(\nu<1\).
In the subcritical range \(\nu<1/2\), (5) is therefore also sufficient.

## Proof

From the second coordinate of (2),
\[
Y=x-W+\frac{V}{1-\nu}.
\]
Since \(V/(1-\nu)\) is continuous, nondecreasing, starts from zero, and increases
only when \(Y=0\), the one-dimensional Skorokhod lemma gives
\[
\frac{V_t}{1-\nu}=M_t(W)-x.
\tag{6}
\]
Substitution into the first coordinate yields
\[
W_t=(1-\nu)x+B_t+\nu M_t(W)+K_t,
\qquad W_t\ge b(t).
\tag{7}
\]

Fix \(T\), set \(C=\{t\le T:X_t=0\}\), and define
\[
A_t=\int_0^t\mathbf1_{\{X_s=0\}}\,db(s),
\qquad
J_t=\int_0^t\mathbf1_{\{X_s=0\}}\,dM_s(W).
\]
Because \(\langle X\rangle_t=t\), occupation density gives
\[
\int_0^t\mathbf1_{\{X_s=0\}}\,ds=0,
\]
and therefore
\[
\int_0^t\mathbf1_{\{X_s=0\}}\,dB_s=0.
\]
Tanaka's formula for the nonnegative semimartingale \(X=X^+\) gives
\[
\frac12L_t^0(X)
=
K_t+\nu J_t-A_t.
\tag{8}
\]

Now \(F=M(W)-b\) is continuous, nonnegative and locally of finite variation.
For such a process,
\[
\mathbf1_{\{F=0\}}\,dF=0
\]
as a signed measure. Thus on \(\{F=0\}\),
\[
dM(W)=db.
\tag{9}
\]
Moreover \(dM(W)\) is supported on \(\{W=M(W)\}\). On the support of
\(\mathbf1_{\{X=0\}}\,dM(W)\) we have \(W=b=M(W)\), hence \(F=0\).
Consequently
\[
J_t
=
\int_0^t\mathbf1_{\{X_s=0,F_s=0\}}\,db(s).
\tag{10}
\]
Combining (8) and (10) gives (3).

The weight multiplying \(db\) on the contact set is either \(1\) or \(1-\nu\).
Since \(\nu<1/2\), it is strictly positive and bounded away from zero. Hence the
signed measure on the right of (3) vanishes identically if and only if the
restriction of \(db\) to \(C\) vanishes; equivalently \(|db|(C)=0\). This proves
(4).

If (4) holds, (7) becomes (1), so the orthant candidate supplies a strong
solution. Conversely, every solution of (1) produces a solution of the orthant
problem (2) with \(K=L^0(W-b)/2\). Uniqueness of the orthant problem therefore
forces it to coincide with the candidate, proving necessity and pathwise
uniqueness.

For locally absolutely continuous \(b\), the zero-Lebesgue-measure property of
\(C\) immediately yields \(|db|(C)=0\), proving Theorem 2. If \(b\) is
increasing, \(|db|=db\), so (4) becomes exactly (5).

## Context and significance

Wang (2026) proves strong existence and pathwise uniqueness for all
\(\nu<1\) under the one-sided boundary condition
\[
\omega^+_{b,T}(h)=o(\sqrt h),
\]
and constructs singular increasing \(\alpha\)-Hölder boundaries,
\(\alpha<1/2\), for which no continuous adapted solution exists. In the
\(\nu<1/2\) part of that proof, the orthant Skorokhod problem already supplies a
unique regulator; condition (PB) is then used to show that the boundary
variation does not charge the contact set and hence that the regulator equals
half the semimartingale local time.

The identity (3) isolates that final identification exactly. In the subcritical
orthant regime, the relevant obstruction is not a Hölder exponent by itself but
boundary Stieltjes mass carried by the random contact set. This separates two
boundaries with the same rough Hölder scale: an absolutely continuous example
such as \(t^\alpha\), \(0<\alpha<1/2\), is well posed, whereas Wang's singular
\(\alpha\)-Hölder construction can fail because its Stieltjes measure charges
contact.

The ingredients—Tanaka's formula, occupation density, and the orthant
Skorokhod map—are classical. The contribution claimed here is the exact
boundary-charge identity and its consequences for the 2026
maximum-perturbed moving-boundary model, not a new general theory of reflected
semimartingales.

## Limitations

- The orthant uniqueness argument used here requires \(\nu<1/2\). No claim is
  made for the critical or supercritical range \(1/2\le\nu<1\).
- For a general singular finite-variation boundary, criterion (4) is exact but
  implicit because its contact set is random.
- The result does not classify which singular boundaries satisfy the criterion,
  nor does it give quantitative stability or approximation rates.
- Classical moving-boundary Skorokhod theory may contain equivalent
  regulator/local-time identities in broader notation. The originality claim is
  restricted to the displayed defect formula and its application to the
  maximum-perturbed model, to the best of our knowledge.

## References

1. C. Wang, "Perturbed Brownian motion reflected at a time-dependent boundary",
   arXiv:2609.20491 (2026). https://arxiv.org/abs/2609.20491
2. R. J. Williams, "Semimartingale reflecting Brownian motions in the orthant",
   in *Stochastic Networks*, IMA Vol. 71, pp. 125-137 (1995).
   https://doi.org/10.1007/978-1-4757-2418-9_7
3. R. A. Doney and T. Zhang, "Perturbed Skorohod equations and perturbed
   reflected diffusion processes", *Ann. Inst. H. Poincare Probab. Statist.*
   41(1), 107-121 (2005). https://doi.org/10.1016/j.anihpb.2004.03.005
4. K. Burdzy, W. Kang and K. Ramanan, "The Skorokhod problem in a
   time-dependent interval", *Stochastic Processes and their Applications*
   119(2), 428-452 (2009). https://doi.org/10.1016/j.spa.2008.03.001
