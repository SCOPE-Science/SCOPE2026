# Exact two-step conjugate-gradient energy sensitivity at a two-cluster collision

## Finding

Let a real symmetric positive-definite reference matrix have exactly two distinct eigenvalues, \(\beta>\gamma>0\), of any positive multiplicities. Its small symmetric perturbation has an **exact leading constant** for the squared energy error after two steps of conjugate gradients (CG). Only perturbations *within* each original eigenspace contribute to this constant; couplings *between* the eigenspaces cancel at first order.

Let \(\Pi\) be the orthogonal spectral projector for \(\beta\) and \(Q=I-\Pi\). Put \(C_0=\beta\Pi+\gamma Q\), \(C(t)=C_0+tF\), and fix a real symmetric \(F\) and a right-hand side \(d\) with \(u=\Pi d\ne0\), \(v=Qd\ne0\). Let \(y_2(t)\) be the second exact-arithmetic CG iterate for \(C(t)y=d\), with \(y_0=0\), and \(y_*(t)=C(t)^{-1}d\). Set
\[
F_{\beta\beta}=\Pi F\Pi,\quad F_{\gamma\gamma}=QFQ,\qquad
\Pi_u=\frac{uu^{\mathsf T}}{\|u\|_2^2},\quad
\Pi_v=\frac{vv^{\mathsf T}}{\|v\|_2^2}.
\]
For all sufficiently small real \(t\), \(C(t)\) is positive definite, and
\[
\boxed{\begin{aligned}
\|y_2(t)-y_*(t)\|_{C(t)}^2
=t^2(\beta-\gamma)^2\biggl[
&\frac{\|(I-\Pi_u)F_{\beta\beta}u\|_2^2}{\beta^3\gamma^2}\\
+&\frac{\|(I-\Pi_v)F_{\gamma\gamma}v\|_2^2}{\beta^2\gamma^3}
\biggr]+O(|t|^3).
\end{aligned}}
\]
The coefficient is nonnegative and vanishes **if and only if** \(u\) and \(v\) are eigenvectors, respectively, of the restrictions of \(F\) to their two original spectral subspaces. When it vanishes, the sharper rate \(\|y_2(t)-y_*(t)\|_{C(t)}^2=O(t^4)\) holds. A nonzero coefficient gives a genuine \(\Theta(t^2)\) squared error. No restriction is imposed on \(\Pi FQ\).

There is also an **exact worst-case perturbation law**. If \(\dim\operatorname{ran}\Pi\ge2\), set \(a_\beta=\|u\|_2^2/(\beta^3\gamma^2)\); otherwise set \(a_\beta=0\). If \(\dim\operatorname{ran}Q\ge2\), set \(a_\gamma=\|v\|_2^2/(\beta^2\gamma^3)\); otherwise set \(a_\gamma=0\). Then
\[
\boxed{\sup_{F=F^{\mathsf T},\ \|F\|_F\le1}
\lim_{t\to0}\frac{\|y_2(t)-y_*(t)\|_{C(t)}^2}{t^2}
=\frac{(\beta-\gamma)^2}{2}\max\{a_\beta,a_\gamma\}.}
\]
Whenever the maximum is positive, a unit-Frobenius symmetric rank-two perturbation supported *entirely inside the maximizing eigenspace* attains it. Thus cross-cluster mixing is not only absent from the first-order expression but is also unnecessary for the sharp worst case.

## Assumptions and scope

All vector spaces and matrices are finite-dimensional and real. The two eigenspaces of \(C_0\) have arbitrary positive dimensions and \(u,v\) must both be nonzero. The perturbation \(F=F^{\mathsf T}\) is fixed, with no required size normalization; only sufficiently small \(|t|\) is considered. The result describes the energy norm \(\|z\|_{C(t)}^2=z^{\mathsf T}C(t)z\), not a residual or Euclidean-error bound. CG is taken in exact arithmetic.

This includes a fixed, recycled spectral preconditioner: let \(A=\operatorname{diag}(a,\beta,\gamma)\), \(a>\beta>\gamma>0\), and set \(D=\operatorname{diag}(\sqrt{\beta/a},1,1)\). For \(B(t)=A+tE\), fixed symmetric \(E\), and \(C(t)=DB(t)D\), ordinary CG on \(C(t)y=Db\) is equivalent to symmetric preconditioned CG on \(B(t)x=b\), with \(x=Dy\); their squared energy errors are exactly equal. Choosing the scale \(\beta\) merges the preconditioned leading eigenvalue with an untouched eigenvalue.

## Proof

**Step 1: polynomial optimality and regularity.** For each sufficiently small \(t\), CG's energy minimization characterizes the residual after two steps as \(r_t=p_t(C(t))d\), where \(p_t(z)=1+c_1(t)z+c_2(t)z^2\) minimizes
\[
J_t(p)=d^{\mathsf T}p(C(t))C(t)^{-1}p(C(t))d.
\]
The normal equations for its coefficients have Gram matrix
\[
G_t=\begin{pmatrix}m_1(t)&m_2(t)\\m_2(t)&m_3(t)\end{pmatrix},\qquad
m_j(t)=d^{\mathsf T}C(t)^j d,
\]
and right-hand side \(-(m_0(t),m_1(t))^{\mathsf T}\). At \(t=0\), the positive spectral weights \(\|u\|_2^2\) and \(\|v\|_2^2\) on two distinct positive eigenvalues make \(G_0\) positive definite: any nonzero \(az+bz^2\) cannot vanish at both \(\beta\) and \(\gamma\). In fact, \(\det G_0=\|u\|_2^2\|v\|_2^2\beta\gamma(\beta-\gamma)^2>0\). Thus \(c_1(t),c_2(t)\) are real analytic near zero. At zero,
\[
p_0(z)=\left(1-\frac z\beta\right)\left(1-\frac z\gamma\right),\qquad p_0(C_0)d=0.
\]
The first CG step is nonterminating and the second iterate is well-defined near zero; at zero the second iterate is exact.

**Step 2: matrix-polynomial derivative.** Write \(q(z)=\partial_t p_t(z)|_{t=0}\), a polynomial of degree at most two with \(q(0)=0\). Expanding \(C(t)\) and its square yields
\[
r'_0=q(C_0)d+\mathcal Dp_0(C_0)[F]d,\qquad
\mathcal Dp_0(C_0)[F]
=-\left(\frac1\beta+\frac1\gamma\right)F
+\frac{C_0F+FC_0}{\beta\gamma}.
\]
The off-diagonal blocks of this derivative vanish because their coefficient is \(-(\beta+\gamma)/(\beta\gamma)+(\beta+\gamma)/(\beta\gamma)=0\). In the two diagonal blocks the coefficients are \(p_0'(\beta)=(\beta-\gamma)/(\beta\gamma)\) and \(p_0'(\gamma)=(\gamma-\beta)/(\beta\gamma)\). Consequently,
\[
r'_0\big|_{\operatorname{ran}\Pi}=
q(\beta)u+\frac{\beta-\gamma}{\beta\gamma}F_{\beta\beta}u,\qquad
r'_0\big|_{\operatorname{ran}Q}=
q(\gamma)v-\frac{\beta-\gamma}{\beta\gamma}F_{\gamma\gamma}v.
\]

**Step 3: two independent first-order projections.** Since \(q(z)=az+bz^2\), the two numbers \(q(\beta),q(\gamma)\) can be varied independently: the evaluation map has determinant \(\beta\gamma(\gamma-\beta)\ne0\). The exact CG minimum of \(J_t\), expanded to order \(t^2\), must therefore minimize \(\|r'_0\|_{C_0^{-1}}^2\) separately in the two blocks. Projecting \(F_{\beta\beta}u\) perpendicular to \(u\) and \(F_{\gamma\gamma}v\) perpendicular to \(v\) yields
\[
r'_0=\frac{\beta-\gamma}{\beta\gamma}
\bigl((I-\Pi_u)F_{\beta\beta}u-(I-\Pi_v)F_{\gamma\gamma}v\bigr).
\]
Equivalently, differentiate the analytic normal equations from Step 1; the same orthogonality conditions result. The two displayed terms belong to orthogonal eigenspaces.

**Step 4: exact coefficient and zero cases.** The identity \(\|y_2(t)-y_*(t)\|_{C(t)}^2=r_t^{\mathsf T}C(t)^{-1}r_t\), together with \(r_t=t r'_0+O(t^2)\), gives the boxed expression. A sum of two nonnegative terms vanishes exactly under the stated eigenvector conditions. If it vanishes, \(r'_0=0\), whence analyticity implies \(r_t=O(t^2)\) and the squared error is \(O(t^4)\). This establishes the directional formula and its zero cases.

**Step 5: Frobenius-optimal perturbation.** On a cluster of dimension at least two, choose a unit vector \(e\) parallel to the nonzero spectral component and decompose any symmetric within-cluster block relative to \(\mathbb Re\oplus e^\perp\) as
\[
\begin{pmatrix}a&z^{\mathsf T}\\z&H\end{pmatrix}.
\]
Its Frobenius norm squared is \(a^2+2\|z\|_2^2+\|H\|_F^2\). Hence the squared orthogonal component of its action on a vector of norm \(s\) is bounded by \(s^2\|F_{\mathrm{block}}\|_F^2/2\). For a one-dimensional cluster this component is zero. Since the two diagonal blocks are Frobenius-orthogonal and the cross blocks expend norm without changing the leading coefficient, the best allocation of a unit Frobenius budget is to the larger of the two weighted cluster coefficients. The asserted worst-case value follows. For a maximizing cluster of dimension at least two, take \(F=(ew^{\mathsf T}+we^{\mathsf T})/\sqrt2\), with \(w\) any unit vector in the same cluster orthogonal to \(e\); it is symmetric, has Frobenius norm one, and attains the bound. This proves the sharp optimality formula.

## Verification

`VERIFY.py` uses only Python's standard library. It differentiates the exact two-step CG normal equations using rational arithmetic, compares the derivative residual against both blockwise orthogonal projections, and verifies the final coefficient. It passed 560 independently generated exact-rational test configurations across seven block multiplicity pairs, including one-dimensional and higher-dimensional eigenspaces. Two explicit rational families are also checked by direct two-step CG at three shrinking perturbation sizes, and two within-cluster rank-two perturbations attain the sharp Frobenius coefficients after normalization.

For a concrete recycled three-mode preconditioner, take \(A=\operatorname{diag}(16,4,1)\), \(D=\operatorname{diag}(1/2,1,1)\), \(b=(2,1,1)^{\mathsf T}\), and \(E=\operatorname{diag}(1,0,0)\). Then \(C_0=\operatorname{diag}(4,4,1)\), \(d=(1,1,1)^{\mathsf T}\), and \(F=\operatorname{diag}(1/4,0,0)\). The exact coefficient is \(9/2048\). A perturbation supported only on the first/third cross-block instead has zero quadratic coefficient and squared error of order at most \(t^4\).

To reproduce: run `python3 VERIFY.py`. The rational tests corroborate the finite algebra; the dimension-uniform claim follows from the proof, not from finite enumeration.

## Relationship to prior work

Diouane, Gürol, Mouhtal and Orban (2026, arXiv:2610.28808, Theorem 3.14) prove an energy-error upper comparison with a second-order remainder, subject to a fixed spectral-separation set for the placement parameter. Their Definition 3.7 excludes placements at an untouched eigenvalue. The present exact asymptotic is for precisely such a two-cluster collision and determines the leading constant and the vanishing criterion, neither of which follows from that upper bound.

Their earlier 2026 scaling analysis and 2024 preprint treat spectral placement and unperturbed CG performance. Giraud and Gratton (2006) analyze spectral sensitivity under inaccurate eigenelements, while Kahl and Rittich (2012) study deflated-CG effective conditioning and perturbations of the deflation subspace. Those spectral and conditioning statements do not directly establish a fixed-two-step residual-energy derivative. The classical polynomial characterization of CG is used here as prior technique, not claimed as a discovery.

## Limitations

The theorem concerns exactly two unperturbed eigenvalue levels and exactly two CG steps, with fixed preconditioner and fixed right-hand side. It assumes exact arithmetic, symmetric perturbations and small \(|t|\), not generic approximate spectral information or time-varying preconditioners. The vanishing criterion is directional in \(d\); the sharp Frobenius bound also fixes \(d\) and does not optimize over right-hand sides. No finite-precision, multi-cluster or end-to-end iteration-complexity guarantee is asserted. Historical priority is not independently certified, and a general older matrix-polynomial sensitivity statement could conceivably imply this formula.

## References

1. Y. Diouane, S. Gürol, O. Mouhtal and D. Orban, [*Deflation-Based Spectral Preconditioning for the Conjugate Gradient Method on Perturbed Systems*](https://arxiv.org/abs/2610.28808), arXiv:2610.28808, first submitted 20 October 2026; especially Definition 3.7 and Theorem 3.14.
2. Y. Diouane, S. Gürol, O. Mouhtal and D. Orban, [*A Spectral Preconditioner for the Conjugate Gradient Method with Iteration Budget*](https://arxiv.org/abs/2603.28969), arXiv:2603.28969 (2026).
3. Y. Diouane, S. Gürol, O. Mouhtal and D. Orban, [*An Efficient Scaled Spectral Preconditioner for Sequences of Symmetric Positive Definite Linear Systems*](https://arxiv.org/abs/2410.02204), arXiv:2410.02204 (2024).
4. L. Giraud and S. Gratton, [*On the Sensitivity of Some Spectral Preconditioners*](https://doi.org/10.1137/040617546), SIAM J. Matrix Anal. Appl. 27 (2006), 1089–1105.
5. K. Kahl and H. Rittich, [*The Deflated Conjugate Gradient Method: Convergence, Perturbation and Accuracy*](https://arxiv.org/abs/1209.1963), arXiv:1209.1963 (2012).
