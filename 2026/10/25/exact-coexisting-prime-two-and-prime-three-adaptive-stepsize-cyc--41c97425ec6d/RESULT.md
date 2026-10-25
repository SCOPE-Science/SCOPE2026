# Exact prime-two and prime-three cycles in a locally adaptive proximal gradient rule

## Finding
The original adaptive proximal-gradient method adaPGM can generate exact, indefinitely periodic **nonconstant stepsizes** even on the scalar strongly convex quadratic \(f(x)=\lambda x^2/2\), \(\lambda>0\), with \(g\equiv0\). Both prime-two and prime-three stepsize cycles occur under admissible initialization, are **locally repelling** in stepsize-state space, and coexist with linearly convergent optimization iterates. Thus oscillation of the adaptively chosen steps is consistent with rapidly convergent primal variables; the cyclic regimes need not attract nearby stepsize initializations.

Put \(z_k=\lambda\gamma_k\). Let \(r_2>1\) be the unique root of \(r_2^3-r_2-1=0\) and set
\[
a_2=\frac{1+\sqrt{1+r_2^2}}{2r_2},\qquad b_2=r_2a_2.
\]
For initial \((z_{-1},z_0)=(a_2,b_2)\), the normalized stepsizes alternate \(b_2,a_2,b_2,a_2,\ldots\), with \(a_2\approx1.00390517\) and \(b_2\approx1.32989121\).

Let \(r_3>1\) be the unique root of
\[
r_3^2(r_3-1)^2(r_3+1)^3=1,
\]
and define
\[
R=r_3\sqrt{1+r_3},\quad a_3=\frac{1+\sqrt{1+R^2}}{2R},\quad b_3=r_3a_3,\quad c_3=Ra_3.
\]
For initial \((z_{-1},z_0)=(a_3,b_3)\), the normalized stepsizes cycle \(b_3,c_3,a_3,b_3,c_3,a_3,\ldots\), where
\[
(a_3,b_3,c_3)\approx(0.83721639,1.03848849,1.55440820).
\]
Each cycle is unique **among positive solutions with the indicated ordered branch itinerary and successive ratios**. This is not a claim about other possible symbolic itineraries.

## Assumptions and scope
Use Algorithm 2.1 in Latafat--Themelis--Stella--Patrinos [1], not its later parameterized replacement. Choose \(\lambda>0\), \(g\equiv0\), initial \(x^{-1}=1\), and the two specified initial steps \(\gamma_{-1},\gamma_0\), which obey the published constraint \(\gamma_0\ge\gamma_{-1}>0\). Initialization is \(x^0=(1-\lambda\gamma_0)x^{-1}\). Calculations are in exact real arithmetic. The scalar local curvature estimates are evaluated only at distinct consecutive iterates, for which \(\ell_k=c_k=\lambda\).

The exact normalized stepsize state map is \(T(u,v)=(v,\Phi(u,v))\), where
\[
\Phi(u,v)=\min\{G(u,v),F(v)\},\qquad G(u,v)=v\sqrt{1+v/u},
\]
\[
F(v)=\begin{cases}\frac12\sqrt{\frac{v}{v-1}},&v>1,\\ +\infty,&0<v\le1.\end{cases}
\]
The original point update is \(x^{k+1}=(1-z_{k+1})x^k\).

## Proof
**Reduction.** For any two distinct scalar iterates \(x,y\), the gradient-difference quotient and inverse-cocoercivity quotient both equal \(\lambda\), since \(\nabla f(x)-\nabla f(y)=\lambda(x-y)\). Substitution into [1, Algorithm 2.1] yields the displayed \(\Phi\). None of the listed cycle steps equals one, so for \(x^{-1}\ne0\) all iterates are nonzero, and every successive pair remains distinct. Thus this reduction holds indefinitely without a degenerate \(0/0\) substitution.

**The two-cycle.** For a positive orbit with growth at \((b,a)\) and cap at \((a,b)\), put \(r=b/a>1\). The identity \(G(b,a)=b\) is equivalent to \(r^2=1+1/r\), i.e. \(r^3-r-1=0\). Its unique solution above one is \(r_2\). The cap equality \(F(b)=a\) is equivalent to \(4ra^2-4a-r=0\), whose unique positive solution is \(a_2\) above. Exact inequalities \(1<a_2<b_2\), \(F(a_2)>b_2\), and \(G(a_2,b_2)>b_2>a_2\) certify respectively the growth and cap choices. Hence \(T(a_2,b_2)=(b_2,a_2)\) and \(T(b_2,a_2)=(a_2,b_2)\). Distinctness makes its prime period two. Since \(\gamma_0=b_2/\lambda\ge a_2/\lambda=\gamma_{-1}\), this is an allowed initialization.

**The three-cycle.** Suppose an ordered positive orbit \(a<b<c\) makes a growth step \((c,a)\to(a,b)\), another growth step \((a,b)\to(b,c)\), then a cap step \((b,c)\to(c,a)\). Set \(r=b/a>1\) and \(s=c/b\). The two growth equalities give
\[
r^2=1+\frac{1}{rs},\qquad s^2=1+r.
\]
Eliminating \(s=\sqrt{1+r}\) yields \(r(r^2-1)\sqrt{1+r}=1\), equivalently the displayed seventh-degree equation. The left side of this unsquared relation increases strictly from zero to infinity for \(r>1\), so there is exactly one such root \(r_3\). Put \(R=rs\). The final cap equality \(F(c)=a\), with \(c=Ra\), gives \(4Ra^2-4a-R=0\). Its unique positive root is exactly \(a_3\). The displayed numbers satisfy \(0<a_3<1<b_3<c_3\); at \(a_3\) the cap is infinite, at \(b_3\) one has \(F(b_3)>c_3=G(a_3,b_3)\), and at \(c_3\) one has \(G(b_3,c_3)>c_3>a_3=F(c_3)\). Therefore the required branches really win, giving \(T(a_3,b_3)=(b_3,c_3)\), \(T(b_3,c_3)=(c_3,a_3)\), and \(T(c_3,a_3)=(a_3,b_3)\). These three values are distinct, so the prime period is three. Again \(\gamma_0=b_3/\lambda\ge a_3/\lambda=\gamma_{-1}\) is admissible.

**Repelling return maps.** Along the strict growth branch, putting \(q=v/u\) and \(s=\sqrt{1+q}\) gives the exact Jacobian
\[
DT_G(u,v)=\begin{pmatrix}0&1\\ -\frac{q^2}{2s}&\frac{2+3q}{2s}\end{pmatrix}.
\]
On the strict cap branch,
\[
DT_F(u,v)=\begin{pmatrix}0&1\\0&-\frac{F(v)}{2v(v-1)}\end{pmatrix}.
\]
Their product along one prime period has determinant zero because at least one factor is a cap Jacobian. Its two eigenvalues are therefore zero and the trace of the product. For the three-cycle beginning at state \((c_3,a_3)\), this product is
\[
J_3=DT_F(b_3,c_3)\,DT_G(a_3,b_3)\,DT_G(c_3,a_3).
\]
For the two-cycle beginning at \((b_2,a_2)\), it is \(J_2=DT_F(a_2,b_2)\,DT_G(b_2,a_2)\). Rational arithmetic with outward-rounded square-root enclosures (see `verify_cycles.py`) rigorously places the nonzero eigenvalue of \(J_2\) in \((-2.057,-2.056)\), and of \(J_3\) in \((-1.327,-1.326)\). Both moduli exceed one, proving local repulsion, not attraction.

**Simultaneous primal convergence.** Over the two-cycle the exact primal multiplier is \((1-a_2)(1-b_2)\in(0,1)\); over the three-cycle it is \((1-a_3)(1-b_3)(1-c_3)\in(0,1)\). Furthermore every listed step belongs to \(0,2\), so each one-step primal ratio has modulus strictly below one. Thus all corresponding primal iterates converge Q-linearly to the unique minimizer, even though the stepsizes never converge. This completes the proof.

## Verification
The standalone `verify_cycles.py` uses only Python's standard library, integer square roots and exact `Fraction` endpoints. It isolates both defining algebraic roots between rational endpoints, proves branch inequalities with rational interval arithmetic, and bounds both return multipliers strictly below minus one. It also bounds both positive primal period factors strictly below one. Run `python3 verify_cycles.py`; it prints `PASS` or fails an assertion. The analytical identities and monotonicity arguments above prove infinite-time periodicity; numerical traces alone would not.

## Relationship to prior work
Reference [1] introduces this exact adaptive rule, describes apparently cyclic stepsizes in Figure 4 and Section 4.3, and explicitly asks whether more rigorous supporting arguments can be given. No exact period-two/three algebraic orbit or return-map multiplier was found in its inspected original text. Reference [2] gives a later, broader parameterized update with an improved square-root coefficient; a general convergence theorem for primal iterates does not imply these precise cycle equations. Reference [3] introduces a different Bregman-adaptive recurrence. A published published-finding corpus analysis [4] already obtains a plastic-constant **two-cycle for that different update**, whose scalar cap is \(1/\sqrt{2z(z-1)}\), rather than \(\frac12\sqrt{z/(z-1)}\) here. Its values \((1.17897,1.56181)\) differ from the two-cycle values here, and it does not imply the prime-three orbit or the repelling return-map classification. Both existence constructions are considered one finding, not two incremental findings.

## Limitations
The construction proves the existence and local instability of specially initialized periodic stepsize trajectories on a one-dimensional quadratic. It does not assert typical behavior, chaotic dynamics, global stability of the stepsize map, a census of all periods, or such periodicity for every smooth convex objective. The local multipliers describe the stepsize-state dynamics, not a perturbation of the full algorithm across varying objectives. Specialized earlier observations under other notation remain a publication-priority risk; the literature comparison cannot establish absolute novelty.

## References
1. P. Latafat, A. Themelis, L. Stella, and P. Patrinos, *Adaptive proximal algorithms for convex optimization under local Lipschitz continuity of the gradient*, arXiv:2301.04431, initially submitted 2023-01-11; Algorithm 2.1 and Section 4.3. https://arxiv.org/pdf/2301.04431.
2. P. Latafat, A. Themelis, and P. Patrinos, *On the convergence of adaptive first order methods: Proximal gradient and alternating minimization algorithms*, PMLR 242 (2024), 197–208. https://proceedings.mlr.press/v242/latafat24a/latafat24a.pdf.
3. H. Ou, P. Latafat, and A. Themelis, *Linesearch-free adaptive Bregman proximal gradient for convex minimization under local relative smoothness*, arXiv:2508.01353.
4. *Plastic-constant exact stepsize two-cycle for quadratic-kernel B-adaPGα*, published-finding corpus research record record e7d7ac1b509b (2026), RESULT.md, inspected for a nonidentical adaptive rule.
