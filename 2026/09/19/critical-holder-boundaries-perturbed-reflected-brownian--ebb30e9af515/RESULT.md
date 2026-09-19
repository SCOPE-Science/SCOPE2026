# Contact-measure criterion and critical Hölder closure for perturbed reflected Brownian motion

## Statement

Let \(B\) be standard Brownian motion, \(x\ge 0\), \(\nu<1/2\), and let \(b:[0,\infty)\to\mathbb R\) be deterministic, continuous, locally of finite variation, with \(b(0)=0\). Write
\[
M_t(W)=\sup_{0\le s\le t}W_s.
\]
Consider the reflected regulator equation
\[
W_t=(1-\nu)x+B_t+\nu M_t(W)+K_t,\qquad W_t\ge b(t),
\tag{R}
\]
where \(K\) is continuous, nondecreasing, \(K_0=0\), and \(dK\) is supported by \(\{t:W_t=b(t)\}\). For \(\nu<1/2\), the orthant Skorokhod construction used by Wang gives a unique adapted solution of (R) for every continuous boundary \(b\); no modulus condition on \(b\) is needed for this regulator problem.

The local-time equation is
\[
W_t=(1-\nu)x+B_t+\nu M_t(W)+\frac12L_t^0(W-b),
\qquad W_t\ge b(t).
\tag{LT}
\]
The distinction between (R) and (LT) is whether the regulator is actually half of the semimartingale local time.

Define \(X=W-b\), where \((W,K)\) is the canonical solution of (R).

### Theorem 1: contact-measure criterion

If for every \(T>0\),
\[
\int_0^T \mathbf 1_{\{X_t=0\}}\,|db|(t)=0\qquad\text{a.s.},
\tag{C}
\]
then
\[
K_t=\frac12L_t^0(X),\qquad t\ge0,
\]
and consequently (LT) has a unique strong solution.

If in addition \(b\) is increasing, then (C) is also necessary. Thus, for increasing continuous locally finite-variation boundaries and \(\nu<1/2\), the local-time equation is well posed if and only if the unique canonical regulator solution does not charge its contact set with the Stieltjes measure \(db\).

### Theorem 2: a variation-a.e. Brownian-LIL criterion

Set
\[
c_\nu:=\max\{1,1-\nu\}
\]
and, for \(t>0\),
\[
\ell_b(t):=
\limsup_{h\downarrow0,\ h<t}
\frac{(b(t)-b(t-h))^+}
{\sqrt{2h\log\log(1/h)}}.
\]
If
\[
c_\nu\,\ell_b(t)<1
\quad\text{for }|db|\text{-a.e. }t>0,
\tag{LIL-b}
\]
then (C) holds and (LT) has a unique strong solution.

This criterion is strictly weaker than Wang's condition
\[
\sup_{0\le s<t\le T,\ t-s\le h}(b(t)-b(s))^+=o(\sqrt h),
\tag{PB}
\]
because (LIL-b) is only required at \(|db|\)-almost every time and uses the larger Brownian LIL scale \(\sqrt{h\log\log(1/h)}\).

### Corollaries

1. **Critical \(1/2\)-Hölder endpoint.** Every locally \(1/2\)-Hölder, continuous, locally finite-variation boundary satisfies (LIL-b), hence (LT) is strongly well posed for every \(x\ge0\) and every \(\nu<1/2\). Combined with Wang's counterexample for every Hölder exponent \(\alpha<1/2\), this closes the universal Hölder threshold at the critical exponent in the subcritical perturbation regime \(\nu<1/2\).

2. **No modulus restriction for absolutely continuous boundaries.** If \(b\) is locally absolutely continuous, then (LT) is strongly well posed for every \(x\ge0\) and every \(\nu<1/2\), with no Hölder or modulus assumption at all.

3. In particular, for every \(\alpha>0\),
\[
b(t)=t^\alpha
\]
is admissible for \(\nu<1/2\). When \(0<\alpha<1/2\), this boundary violates (PB) strongly, since \(\omega_b^+(h)/\sqrt h\asymp h^{\alpha-1/2}\to\infty\), yet the local-time equation remains well posed. Hence the obstruction below exponent \(1/2\) is not roughness by itself; singular variation can be essential.

## Proof

### 1. Canonical regulator solution for \(\nu<1/2\)

Wang rewrites (R) as a two-dimensional Skorokhod problem in the orthant. With \(\nu^*=\nu/(1-\nu)\), the corresponding off-diagonal matrix has spectral radius
\[
\rho(|Q|)=\sqrt{|\nu^*|}<1
\]
exactly when \(\nu<1/2\). The orthant Skorokhod theorem therefore gives a unique adapted solution for every continuous driving path. This step does not require (PB).

Any solution of (LT), with \(K=L^0(W-b)/2\), is in particular a solution of (R), because local time is continuous, nondecreasing and carried by \(\{W=b\}\). Hence uniqueness for (R) reduces uniqueness for (LT) to the identification \(K=L^0/2\).

### 2. Contact-measure sufficiency

Let \(X=W-b\ge0\) and \(F=M(W)-b\ge0\). Since \(M(W)\) increases only when \(M(W)=W\), on the contact set \(\{X=0\}\) any increase of \(M\) can occur only where \(F=0\). Moreover, for the continuous finite-variation process \(F=M-b\),
\[
\mathbf 1_{\{F=0\}}\,dF=0,
\]
so on \(\{F=0\}\) the measures \(dM\) and \(db\) coincide. Condition (C) therefore implies
\[
\int_0^T\mathbf 1_{\{X_t=0\}}\,dM_t=0.
\tag{1}
\]

The local martingale part of \(X\) is \(B\), hence its quadratic variation is \(t\). By the occupation-density formula,
\[
\int_0^T\mathbf 1_{\{X_t=0\}}\,dt=0,
\]
and consequently
\[
\int_0^T\mathbf 1_{\{X_t=0\}}\,dB_t=0.
\tag{2}
\]

Tanaka's formula for the nonnegative semimartingale \(X=X^+\) gives
\[
\int_0^t\mathbf 1_{\{X_s=0\}}\,dX_s=\frac12L_t^0(X).
\]
Since
\[
dX=dB+\nu\,dM+dK-db,
\]
while \(dK\) is supported on \(\{X=0\}\), equations (C), (1), and (2) yield
\[
K_t=\frac12L_t^0(X).
\]
This proves sufficiency.

### 3. Necessity for increasing boundaries

Assume \(b\) is increasing and (LT) has a solution. By uniqueness of the canonical regulator problem it must coincide with the solution of (R). Put \(A=\{X=0\}\). Tanaka's formula, the support property of local time, and the occupation-density argument give
\[
\int_A db=\nu\int_A dM.
\tag{3}
\]
On \(A\), an increase of \(M\) can occur only on \(A_0=A\cap\{F=0\}\), and there \(dM=db\). Thus
\[
db(A)=\nu\,db(A_0).
\]
If \(\nu<0\), the two sides have opposite signs unless both vanish. If \(0\le\nu<1/2\), then
\[
0\le db(A)=\nu db(A_0)\le\nu db(A),
\]
which again forces \(db(A)=0\). This is (C).

### 4. Variation-a.e. LIL criterion

Fix deterministic \(t>0\). On the event \(\{X_t=0\}\), for all sufficiently small \(h>0\), the regulator equation implies
\[
B_t-B_{t-h}
\le c_\nu\,(b(t)-b(t-h))^+.
\tag{4}
\]
Indeed, if \(F_t>0\), the running maximum is locally constant before \(t\). If \(F_t=0\), then
\[
0\le M_t-M_{t-h}\le b(t)-b(t-h),
\]
and the factor \(c_\nu=1\vee(1-\nu)\) handles both signs of \(\nu\).

For each fixed deterministic \(t>0\), the backward Brownian law of the iterated logarithm states
\[
\limsup_{h\downarrow0}
\frac{B_t-B_{t-h}}
{\sqrt{2h\log\log(1/h)}}=1
\qquad\text{a.s.}
\tag{5}
\]
If \(c_\nu\ell_b(t)<1\), equations (4) and (5) are incompatible. Therefore
\[
\mathbb P(X_t=0)=0
\]
for \(|db|\)-almost every \(t\). Fubini with the deterministic finite measure \(|db|\) on each compact interval gives (C).

### 5. Critical Hölder and absolutely continuous corollaries

If \(b\) is locally \(1/2\)-Hölder, then on compact intervals
\[
(b(t)-b(t-h))^+\le C\sqrt h,
\]
so \(\ell_b(t)=0\) for every \(t>0\). This proves the critical Hölder corollary. Wang's Theorem 1.2 supplies, for each \(\alpha<1/2\), an increasing globally \(\alpha\)-Hölder finite-variation boundary for which no solution from zero exists, so the exponent \(1/2\) is sharp as a universal Hölder guarantee when \(\nu<1/2\).

If \(b\) is locally absolutely continuous, then \(|db|=|b'(t)|dt\). The occupation-density identity already gives \(dt(\{X=0\})=0\), hence (C) without any modulus assumption. This proves the second corollary.

## Relation to prior work and originality boundary

Wang (2026) proves strong existence and pathwise uniqueness under (PB) for all \(\nu<1\), and constructs singular increasing \(\alpha\)-Hölder counterexamples for every \(\alpha<1/2\). In the regime \(\nu<1/2\), Wang also invokes Williams' orthant Skorokhod theorem for the regulator problem and proves a local-time identification under (PB). Those ingredients are prior work and are not claimed here.

The new claim is the sharper synthesis in the subcritical regime: the contact-measure criterion, the variation-a.e. Brownian-LIL condition, the critical \(1/2\)-Hölder endpoint, and the modulus-free absolutely continuous corollary. Searches of the recent source, older perturbed-reflection literature, and time-dependent Skorokhod literature did not locate these statements or an equivalent critical-endpoint theorem. The result is nevertheless close to Wang's proof architecture, so the originality claim is deliberately narrow and is made only to the best of our knowledge.

Burdzy, Kang and Ramanan (2009) study Skorokhod reflection in time-dependent intervals and local-time variation, but not the present maximum-perturbed local-time equation or the contact-measure/LIL criterion above. Classical perturbed reflected Brownian-motion papers treat fixed boundaries and provide background rather than this moving-boundary endpoint result.

## Limitations

- The main extension is restricted to \(\nu<1/2\), where the orthant Skorokhod map is uniquely available for arbitrary continuous drivers by the spectral-radius criterion.
- The exact equivalence between local-time solvability and contact Stieltjes mass is stated only for increasing boundaries. For signed finite-variation boundaries, (C) remains sufficient but cancellation can prevent the same necessity argument.
- The LIL condition is sufficient, not claimed necessary; the constant threshold at equality is not resolved.
- Local finite variation remains assumed, so the result does not cover arbitrary rough \(1/2\)-Hölder boundaries of infinite variation.
- The result does not settle the critical-boundary question for \(\nu\ge1/2\).

## References

1. C. Wang, *Perturbed Brownian motion reflected at a time-dependent boundary*, arXiv:2609.20491v1 (2026). https://arxiv.org/abs/2609.20491v1
2. R. J. Williams, *Semimartingale reflecting Brownian motions in the orthant*, in *Stochastic Networks*, IMA Vol. 71, 125–137 (1995).
3. K. Burdzy, W. Kang and K. Ramanan, *The Skorokhod problem in a time-dependent interval*, Stochastic Processes and their Applications 119 (2009), 428–452. https://doi.org/10.1016/j.spa.2008.03.001
4. L. Chaumont and R. A. Doney, *Pathwise uniqueness for perturbed versions of Brownian motion and reflected Brownian motion*, Probability Theory and Related Fields 113 (1999), 519–534. https://doi.org/10.1007/s004400050216
5. D. Revuz and M. Yor, *Continuous Martingales and Brownian Motion*, 3rd ed., Springer (1999).
