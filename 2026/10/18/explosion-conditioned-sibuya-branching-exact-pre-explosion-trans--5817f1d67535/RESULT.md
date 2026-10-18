# Explosion-conditioned Sibuya branching: exact pre-explosion transform and a critical correction crossover

## Finding

Consider the continuous-time Galton–Watson process with unit exponential lifetimes, initially one particle, and Sibuya offspring law with probability-generating function
\[
f(z)=1-(1-z)^\alpha,\qquad 0<\alpha<1.
\]
Write \(\tau\) for its almost surely finite explosion time. For a fixed \(T>0\), condition on \(\tau=T\) using the regular conditional law associated with the strictly positive explosion-time density. Let \(b=1-\alpha\), \(E(t)=\mathbb P(\tau\le t)\), and \(X_u=E(u)N_{T-u}\), where \(0<u<T\). The explosion distribution is exactly
\[
E(t)=(1-e^{-bt})^{1/b}.
\]

**Exact pre-explosion transform.** Set \(w=E(u)\), \(q=e^{-b(T-u)}\), \(C=1-e^{-bT}\), and \(D(z)=1-(1-w)z\). Then, for every \(0\le z\le1\),
\[
G_{T,u}(z):=\mathbb E[z^{N_{T-u}}\mid\tau=T]
=z\left(\frac{D(z)}w\right)^{-\alpha}
\left[1+\frac qC\bigl(D(z)^b-w^b\bigr)\right]^{\alpha/b}.
\tag{1}
\]
Two finite-time consequences are
\[
\mathbb P(N_{T-u}=1\mid\tau=T)=\left(\frac{E(u)}{E(T)}\right)^\alpha,
\tag{2}
\]
\[
\mathbb E[X_u\mid\tau=T]
=w+\alpha(1-w)\frac{1-e^{-b(T-u)}}{1-e^{-bT}}.
\tag{3}
\]

**Sharp correction hierarchy.** Put \(g(s)=(1+s)^{-\alpha}\), \(h(s)=(1+s)^b-1\), \(c=e^{-bT}/(1-e^{-bT})\), and
\[
j(s)=-s+\frac{\alpha(s+s^2/2)}{1+s},\quad
A(s)=\alpha c\,g(s)h(s).
\]
Define
\[
B_{\rm lat}(s)=b^{1/b}g(s)j(s),\qquad
B_{\rm an}(s)=g(s)\left(\frac{\alpha b c}{2}h(s)+\frac{\alpha(2\alpha-1)c^2}{2}h(s)^2\right).
\]
For \(L_u(s)=\mathbb E[e^{-sX_u}\mid\tau=T]\), uniformly for \(s\) in each compact subset of \([0,\infty)\),
\[
L_u(s)=g(s)+uA(s)+
\begin{cases}
u^{1/b}B_{\rm lat}(s)+o(u^{1/b}), & 0<\alpha<1/2,\\
u^2\bigl(B_{\rm lat}(s)+B_{\rm an}(s)\bigr)+o(u^2),&\alpha=1/2,\\
u^2B_{\rm an}(s)+o(u^2),&1/2<\alpha<1.
\end{cases}
\tag{4}
\]
In particular, \(L_u(s)\to g(s)\), recovering the gamma limit with shape \(\alpha\), while the first finite-time correction remembers the conditioning time \(T\). For every \(s>0\), \(A(s)>0\) and \(B_{\rm lat}(s)<0\), whereas \(B_{\rm an}(s)>0\) for \(\alpha>1/2\). The next exponent changes from the fractional \(1/(1-\alpha)\) to two exactly at \(\alpha=1/2\).

The first correction also has a sharp measure-representation boundary:
\[
\frac{A(s)}{\alpha c}=(1+s)^{-(2\alpha-1)}-(1+s)^{-\alpha}.
\tag{5}
\]
For \(\alpha>1/2\), it is the Laplace transform of the finite signed measure \(\Gamma(2\alpha-1,1)-\Gamma(\alpha,1)\); for \(\alpha=1/2\), it is the transform of \(\delta_0-\Gamma(1/2,1)\). If \(\alpha<1/2\), the right side is unbounded as \(s\to\infty\) and hence cannot be the Laplace transform of a finite signed measure. This statement concerns the coefficient of a pointwise/locally uniform Laplace expansion; it is **not** a total-variation derivative. At every finite \(u\), \(X_u\) is lattice-supported and is mutually singular with the continuous limiting gamma law.

## Assumptions and scope

The initial number of particles is exactly one. Each particle waits an independent exponential time of rate one, and then is replaced by an independent Sibuya number of children. The offspring probabilities are \(\mathbb P(K=k)=(-1)^{k+1}\binom{\alpha}{k}\), \(k\ge1\), which are positive and sum to one; the offspring mean is infinite. The explosion time is \(\tau=\inf\{t:N_t=\infty\}\), with \(N_t=\infty\) thereafter. The convention \(z^\infty=0\) applies for \(0\le z<1\).

All assertions require fixed \(T>0\) and \(0<\alpha<1\). Remainders may depend on \(T\), \(\alpha\), and the compact interval of Laplace arguments. No uniformity as \(T\downarrow0\), \(T\to\infty\), or \(\alpha\to0,1\) is claimed. Equation (4) is for finite \(s\) on bounded ranges. \(\Gamma(k,1)\) denotes the gamma probability law of shape \(k>0\) and rate one; \(\delta_0\) is the unit atom at zero.

## Proof

**Step 1: solve the branching semigroup.** Put \(F_t(z)=\mathbb E[z^{N_t}]\) for \(z<1\). The branching equation is \(\partial_tF_t(z)=f(F_t(z))-F_t(z)\), \(F_0(z)=z\). Setting \(Y_t(z)=1-F_t(z)\) gives \(\partial_tY_t=Y_t^\alpha-Y_t\), and \(Y_t^b\) solves \(\partial_t(Y_t^b)=b(1-Y_t^b)\). Hence
\[
F_t(z)=1-\left[1-e^{-bt}+e^{-bt}(1-z)^b\right]^{1/b}.
\tag{6}
\]
Taking \(z\uparrow1\) yields the stated \(E(t)=1-F_t(1-)\). It has positive derivative \(E'(t)=e^{-bt}E(t)^\alpha\) for every \(t>0\).

**Step 2: conditioning at the explosion time.** Conditional on \(N_t=n<\infty\), the probability of no explosion by time \(T>t\) is \((1-E(T-t))^n\). Differentiation in \(T\) and Bayes' rule give
\[
\mathbb E[z^{N_t}\mid\tau=T]
=\frac{zE'(T-t)}{E'(T)}F'_t\!\left(z(1-E(T-t))\right).
\tag{7}
\]
The semigroup identity implies \(E'(T)=E'(T-t)F'_t(1-E(T-t))\). From (6),
\[
F'_t(v)=e^{-bt}(1-v)^{-\alpha}
\left[1-e^{-bt}+e^{-bt}(1-v)^b\right]^{\alpha/b}.
\tag{8}
\]
Use \(t=T-u\) and the identity \(1-q+qw^b=C\). Substitution in (7), followed by division by its value at \(z=1\), gives equation (1). The coefficient of \(z\) in (7), with \(F'_t(0)=e^{-bt}\), gives equation (2). Differentiating (1) at \(z=1\) gives equation (3). These calculations also show that (1) is a normalized probability-generating function for the stated conditioned process.

**Step 3: two competing small-time scales.** Fix \(S<\infty\) and \(s\in[0,S]\). Set \(z=e^{-sw}\), \(d=D(z)/w\), and \(Q=e^{-bT}\). Then
\[
w=b^{1/b}u^{1/b}(1+O(u)),\qquad
 d=1+s-w(s+s^2/2)+O_S(w^2),
\tag{9}
\]
and \(qw^b=Q(e^{bu}-1)\) exactly. Consequently the conditional Laplace transform in (1) factors as
\[
L_u(s)=z d^{-\alpha}
\left[1+c(e^{bu}-1)(d^b-1)\right]^{\alpha/b}.
\tag{10}
\]
The first factor has the expansion
\[
z d^{-\alpha}=g(s)[1+j(s)w+O_S(w^2)].
\tag{11}
\]
Because \(w=o(u)\), the second factor equals
\[
1+\alpha c h(s)u+
\left[\frac{\alpha b c}{2}h(s)+\frac{\alpha(2\alpha-1)c^2}{2}h(s)^2\right]u^2
+O_S(u^3+uw).
\tag{12}
\]
The cross term in multiplying (11) and (12) is \(O_S(uw)=o(u^2)\). If \(\alpha<1/2\), then \(1<1/b<2\) and \(u^2=o(w)\); if \(\alpha>1/2\), then \(w=o(u^2)\); at equality, \(w\sim u^2/4\). These three cases produce (4), including the claimed local uniformity. Since \(\alpha<1\), for \(s>0\) one has \(j(s)<0\) directly from its formula. The positivity of \(B_{\rm an}\) above the crossover follows from \(2\alpha-1>0\).

**Step 4: the finite-measure threshold.** For positive shape \(k\), the gamma transform is \((1+s)^{-k}\); an atom at zero has constant transform one. These identities yield the signed measures above and at \(\alpha=1/2\). For \(\alpha<1/2\), the right side of (5) diverges to \(+\infty\) as \(s\to\infty\), whereas the Laplace transform of any finite signed measure on \([0,\infty)\) is bounded by its total variation. This proves the sharp threshold without implying measure-level convergence.

## Verification

The standalone script `verification.py` uses high-precision arithmetic for independent evaluations of (1), (2), (3), and the semigroup expression (7). It also verifies the special square-root case \(\alpha=1/2\), where (1) is exactly a mixture of a single-particle atom and a shifted negative-binomial law:
\[
G_{T,u}(z)=(1-\lambda)z+\lambda z\sqrt{\frac{w}{1-(1-w)z}},
\qquad \lambda=\frac{1-e^{-(T-u)/2}}{1-e^{-T/2}}.
\tag{13}
\]
The script checks decreasing asymptotic residuals for \(\alpha\) on both sides of the crossover and at equality. It is a finite reproducibility check; all infinite limits and signed-measure conclusions follow from the displayed proof, not numerical extrapolation.

## Relationship to prior work

Harris, Johnston and Pardo (2026) establish the gamma limit of scaled populations conditioned on an explosion time, the branching semigroup and general conditional generating-function identity (their equation (3.11)), and a limiting immigration-and-branching process. Their general limit is recovered as the leading term \(g(s)\). The calculation here fixes the classical Sibuya offspring law to obtain the exact finite-time transform, the conditioning-time-dependent correction, its fractional/analytic crossover and the measure-representation boundary. The general gamma limit alone does not specify these subleading coefficients.

Sagitov and Lindo (2015) develop explicit iterates and continuous-time embeddings for a class of theta-branching processes; this family contains semigroups of the same power form as (6). Their explicit semigroup technology is a close antecedent, but the results examined concern generations, absorption and non-absorption conditioning rather than the stated fixed-explosion-time two-scale asymptotic expansion. The present claim is not a claim of inventing power-form semigroups or the Sibuya law.

## Limitations

The sharp corrections are proved only for this Sibuya offspring subfamily, not arbitrary slowly varying factors in explosive branching laws. The \(s\)-uniformity is on bounded intervals; the unbounded behavior of the first coefficient for small \(\alpha\) does not contradict locally uniform convergence. The law of \(X_u\) is discrete for each \(u>0\), so no total-variation convergence to its continuous gamma limit, and no total-variation expansion, is asserted. Although the coefficient is represented by signed gamma measures for \(\alpha\ge1/2\), this is a statement about a Laplace-transform coefficient, not convergence of signed probability-measure differences in total variation. The status of a comparable two-scale expansion for general slowly varying offspring factors remains open here.

## References

1. S. C. Harris, S. G. G. Johnston and J.-C. Pardo, *Behaviour near explosion in continuous-time Galton–Watson trees*, arXiv:2610.01810v1 (publicly posted 1 October 2026), especially Sections 3 and 5.
2. S. Sagitov and A. Lindo, *A special family of Galton–Watson processes with explosions*, arXiv:1502.07538 (initially publicly posted 26 February 2015), especially Sections 2, 6 and 7.
