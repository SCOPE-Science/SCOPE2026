# Only time zero is positive for a compact-resolvent self-adjoint eventually positive semigroup

## Finding

There is a real self-adjoint contraction \(C_0\)-semigroup \((e^{tA})_{t\geq0}\) on the real Banach lattice \(H=\ell^2(\mathbb Z;\mathbb R)\), with compact-resolvent generator and a strictly positive unit vector \(u\), such that every orbit starting at a nonzero positive vector is eventually bounded below by a positive multiple of \(u\), while **no operator \(e^{tA}\) is positive for any \(t>0\)**. For the explicit operator below there is a quantitative witness:

\[
\langle e^{tA}e_n,e_{-n}\rangle<0
\quad\text{for every }t>0\text{ and every integer }n\geq\lceil t+3\rceil.
\]

Here \(e_j\) are the usual coordinate vectors. Thus the positivity-time set is exactly \(\{0\}\); the upper cutoff is a sufficient one, not asserted optimal. The construction originates with Dobrick [1]; the all-positive-times obstruction and its displayed cutoff are the additional conclusions proved here.

## Assumptions and scope

All Hilbert spaces, operators and lattice orders in the theorem are **real**. On \(H\) let \(d_0=1\) and \(d_j=|j|\) for \(j\ne0\), and let \(D\) be the positive self-adjoint diagonal operator \(De_j=d_je_j\) with domain
\[
\operatorname{dom}(D)=\left\{x\in H:\sum_{j\in\mathbb Z}d_j^2|x_j|^2<\infty\right\}.
\]
Set \(u_{\pm n}=e^{-3n^2/2}\) for integers \(n\geq1\), and
\[
u_0=\left(1-2\sum_{n\geq1}e^{-3n^2}\right)^{1/2}>0,\qquad
v=Du,\quad\kappa=\langle v,u\rangle.
\]
Indeed, \(2\sum_{n\geq1}e^{-3n^2}<2\sum_{n\geq1}20^{-n}=2/19<1\), so \(u_0>0\). The vector \(u\) is strictly positive coordinatewise, belongs to \(\operatorname{dom}(D)\), and has norm one. Rank-one notation is \((a\otimes b)x=a\langle b,x\rangle\). Define
\[
A_0=-D+\frac{v\otimes v}{\kappa},\qquad
q_n=\frac{e_n-e_{-n}}{\sqrt2},\qquad
\delta_n=ne^{-2n^2},\qquad
B=\sum_{n\geq1}\delta_n(q_n\otimes q_n),
\]
and \(A=A_0+B\), with domain \(\operatorname{dom}(A)=\operatorname{dom}(D)\). The series defining \(B\) converges in operator norm, since the \(q_n\) are orthonormal and \(\delta_n\to0\). No assumption of uniform eventual positivity is made or concluded.

## Proof

**Basic operator facts.** The bounded rank-one operator \(K=(v\otimes v)/\kappa\) is real, self-adjoint, and positive in the lattice order, so \(A_0=-D+K\) is self-adjoint and its semigroup is lattice-positive by the bounded positive perturbation argument. Cauchy–Schwarz in the \(D^{1/2}\)-inner product gives
\[
\langle A_0x,x\rangle=-\|D^{1/2}x\|_2^2+
\frac{|\langle D^{1/2}u,D^{1/2}x\rangle|^2}{\|D^{1/2}u\|_2^2}\leq0,
\]
with equality only if \(x\) is a scalar multiple of \(u\). Since \(A_0u=0\), its zero eigenvalue is simple. The diagonal \(D\) has compact resolvent; bounded perturbations preserve this property here. Consequently \(e^{tA_0}\to u\otimes u\) in operator norm because zero is an isolated simple top eigenvalue and the remaining spectrum lies below a negative gap. Each antisymmetric vector \(q_n\) is an eigenvector of \(A_0\) with eigenvalue \(-n\), because \(v\) is symmetric. The operator \(B\) vanishes on the symmetric subspace and gives eigenvalue shift \(\delta_n\) on \(q_n\). Since \(0<\delta_n<n\), \(A\) is again real, self-adjoint and nonpositive; compactness of its resolvent follows from bounded perturbation. Hence it generates a self-adjoint contraction \(C_0\)-semigroup. On these reducing subspaces, spectral calculus gives the exact norm-convergent expansion
\[
e^{tA}=e^{tA_0}+\sum_{n\geq1}h_n(t)(q_n\otimes q_n),\qquad
h_n(t)=e^{-nt}\big(e^{\delta_nt}-1\big).
\tag{1}
\]

**A pointwise bound for the positive reference semigroup.** Put
\[
b=\frac{\|v\|_2^2}{\kappa}.
\]
Because \(d_j\geq1\) and \(\|u\|_2=1\), \(\kappa\geq1\). Also \(e^{-3}<1/20\), whence
\[
\|v\|_2^2=u_0^2+2\sum_{n\geq1}n^2e^{-3n^2}
\leq1+2\sum_{n\geq1}n^2(1/20)^n
=1+\frac{840}{6859}<2.
\]
Thus \(0<b<2\). In the Dyson–Phillips series for \(e^{t(-D+K)}\), the zeroth term \(e^{-tD}\) has zero \((-n,n)\) entry. For the term containing exactly \(m\geq1\) factors of \(K\), the initial and terminal rank-one factors contribute \(v_n^2/\kappa\), each intermediate factor is bounded by \(b\), and the ordered integration simplex has volume \(t^m/m!\). All terms are coordinatewise nonnegative. Therefore, for each \(t\geq0\) and integer \(n\geq1\),
\[
0\leq a_n(t):=\langle e^{tA_0}e_n,e_{-n}\rangle
\leq\frac{v_n^2}{\kappa}\sum_{m\geq1}\frac{b^{m-1}t^m}{m!}
=\frac{v_n^2}{\kappa b}(e^{bt}-1)
\leq n^2e^{-3n^2}(e^{2t}-1).
\tag{2}
\]
For the last inequality use \(\kappa b=\|v\|_2^2\geq\kappa\geq1\) and \(b<2\); all bounds hold uniformly in the coordinate index.

**Every strictly positive time has negative entries.** Since
\(\langle(q_n\otimes q_n)e_n,e_{-n}\rangle=-1/2\), equation (1) gives
\[
\langle e^{tA}e_n,e_{-n}\rangle=a_n(t)-\frac12h_n(t).
\]
For \(t>0\), the elementary inequalities \(e^z-1\geq z\) and \(e^{2t}-1<2te^{2t}\) imply, using (2),
\[
\begin{aligned}
\langle e^{tA}e_n,e_{-n}\rangle
&\leq n^2e^{-3n^2}(e^{2t}-1)-\frac{nt}{2}e^{-2n^2-nt}\\
&<\frac{nt}{2}e^{-3n^2}\left(4ne^{2t}-e^{n^2-nt}\right).
\end{aligned}
\tag{3}
\]
If \(n\geq\lceil t+3\rceil\), then \(n\geq3\), \(n^2-nt\geq3n\), and \(t<n\). Moreover \(e^n>4n\) for every real \(n\geq3\): the first four nonzero Taylor terms give \(e^n\geq1+n+n^2/2+n^3/6>4n\); the final cubic difference is positive at \(3\) and strictly increasing thereafter. Consequently
\[
e^{n^2-nt}\geq e^{3n}>4ne^{2n}>4ne^{2t}.
\]
The last parenthesis in (3) is strictly negative, proving the displayed witness inequality simultaneously for all real \(t>0\). Since a positive bounded lattice operator must send \(e_n\geq0\) to a coordinatewise nonnegative vector, \(e^{tA}\) is not positive for any \(t>0\). At \(t=0\) it equals the identity, hence is positive.

**Every positive orbit eventually becomes strongly positive.** Here is a reconstruction of the companion property originally established in [1]. Fix \(0\ne x\in H_+\), and put \(\alpha=\langle u,x\rangle>0\). Operator-norm convergence \(e^{sA_0}\to u\otimes u\) implies \(\langle v,e^{sA_0}x\rangle\geq\alpha\kappa/2\) for all \(s\) beyond some \(T_x\). The positive Duhamel formula for \(A_0=-D+K\) then yields, for every coordinate \(j\) and \(t\geq T_x+1\),
\[
(e^{tA_0}x)_j\geq\frac\alpha2u_j(1-e^{-d_j(t-T_x)})
\geq c_xu_j,\qquad c_x=\frac\alpha2(1-e^{-1})>0.
\tag{4}
\]
The perturbation in (1) changes coordinates \(\pm n\) of \(x\) in magnitude by at most \(h_n(t)\|x\|_2/\sqrt2\). Since \(n-\delta_n=n(1-e^{-2n^2})>0\),
\[
\sup_{t\geq0}\frac{h_n(t)}{u_n}
\leq\frac{\delta_n}{e(n-\delta_n)u_n}
=\frac{e^{-n^2/2}}{e(1-e^{-2n^2})}\longrightarrow0.
\]
Choose \(N_x\) so the perturbation is at most \(c_xu_n/2\) for all \(n\geq N_x\) and all times. For each of the finitely many smaller \(n\), \(h_n(t)\to0\), so a single later time makes the same bound valid there; the coordinate \(0\) is unchanged. Combining with (4), one gets \(e^{tA}x\geq(c_x/2)u\) coordinatewise for every sufficiently large \(t\). This is individual eventual strong positivity, with a threshold depending on \(x\).

## Verification

The standalone script `verify.py` checks the exact rational geometric-series estimate used to bound \(b\), Taylor-series inequalities underlying \(e^{-3}<1/20\) and \(e^n>4n\), and several rational-time instances of the explicit cutoff. Its successful execution reports `NOWHERE_POSITIVE_SEMIGROUP_RATIONAL_BOUNDS_AND_CUTOFF_OK`. The complete statements for infinitely many coordinates and **all** positive real times are proved analytically above, not inferred from finite testing. The norm-convergent spectral decomposition (1), the Dyson bound (2), and positivity of the reference semigroup are the critical infinite-dimensional ingredients.

## Relationship to prior work

Dobrick's arXiv:2609.00425v1 [1] defines this exact generator and proves individual eventual strong positivity, self-adjointness, compact resolvent, and negativity of \(e^{nA}\) at every sufficiently large **integer** time (Theorem 1.1, Proposition 3.5). That statement alone does not rule out a positive semigroup operator at a noninteger time. The present proof replaces the special-integer-time estimate with (2)–(3) and shows negativity at **every** strictly positive real time with an explicit coordinate cutoff. The underlying operator and the positive-orbit theorem are credited to [1], not claimed as independently constructed here.

Daners, Glück, and Kennedy [2, Example 5.7] previously gave a semigroup on \(C([-1,1])\) whose individual orbits are eventually strongly positive while no single positive operator time exists. Their example has a bounded generator on a different Banach lattice; it is not a self-adjoint Hilbert-space semigroup with compact resolvent. Their Example 5.8 has compact resolvent on a \(C(K)\)-space but proves negative entries at selected large times. The new point is the simultaneous self-adjoint Hilbert-lattice and compact-resolvent setting, for the specific operator [1], plus the explicit all-time quantitative obstruction. The smoothing-based sufficient criteria in [3] do not imply uniform positivity in this setting because the requisite uniform regularization into the principal ideal fails.

## Limitations

The theorem concerns this explicitly specified real Hilbert-lattice semigroup; it does not classify positivity-time sets of all self-adjoint semigroups. The cutoff \(\lceil t+3\rceil\) is sufficient and need not be minimal. Positivity of each individual orbit is an asymptotic property with an initial-vector-dependent threshold, not positivity of the operators. Existing published constructions of nowhere-positive individually eventually positive semigroups on \(C(K)\)-spaces make the abstract phenomenon non-new; the gain is the additional Hilbert self-adjoint compact-resolvent structure for a concrete construction.

## References

[1] Alexander Dobrick, *Individual and Uniform Eventual Positivity of Self-Adjoint Semigroups*, arXiv:2609.00425v1, first publicly submitted 2026-08-31. https://arxiv.org/abs/2609.00425 ; complete HTML https://arxiv.org/html/2609.00425v1 .

[2] Daniel Daners, Jochen Glück, and James B. Kennedy, *Eventually Positive Semigroups of Linear Operators*, Journal of Mathematical Analysis and Applications 433 (2016), 1561–1593, Examples 5.7–5.8; arXiv:1511.09020. https://arxiv.org/abs/1511.09020 .

[3] Jochen Glück and Delio Mugnolo, *Eventual Domination for Linear Evolution Equations*, Mathematische Zeitschrift (2021), https://doi.org/10.1007/s00209-021-02721-x .

