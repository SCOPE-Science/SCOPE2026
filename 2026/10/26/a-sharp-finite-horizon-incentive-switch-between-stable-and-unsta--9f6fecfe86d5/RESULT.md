# A sharp finite-horizon incentive switch between stable and unstable feedback

## Finding

An exactly solvable two-period instance of bilinear functional-incentive design has a discontinuous globally optimal feedback gain, even though the plant, follower response, and stage costs are smooth. The discontinuity occurs at a precise ratio of the follower's effort cost to the leader's tracking cost. The same calculation yields a complete classification of stability of the globally cost-minimizing feedback, including a critical cubic-root cusp.

**Theorem.** Let \(A,B,Q,R>0\), let \(x_0\ne0\) be deterministic, and consider the scalar system and two-period objective specified below. Define
\[
 a=A+\frac{B\Theta}{2R},\qquad
 \eta=\frac{QB^2}{2R},\qquad
 G_{A,\eta}(a)=\bigl((a-A)^2+\eta\bigr)(1+a^2).
\]
Every global optimizer has \(0<a<A\). When \(\eta\ne1\), the global optimizer \(a_*(A,\eta)\) is unique. At \(\eta=1\) it is unique and equal to \(A/2\) for \(A\le2\), whereas for \(A>2\) there are exactly two global optimizers,
\[
 a_{\pm}=\frac{A\pm\sqrt{A^2-4}}{2},\qquad
 G_{A,1}(a_\pm)=A^2,\qquad a_-<1<a_+.
\]
For \(A>2\), the unique global minimizer is strictly larger than \(a_+\) when \(0<\eta<1\), and strictly smaller than \(a_-\) when \(\eta>1\). Thus the preferred fixed incentive switches from an unstable closed loop to a stable one at \(R=QB^2/2\); at the threshold both a stable and an unstable incentive are globally optimal. The jump in the preferred multiplier has magnitude \(\sqrt{A^2-4}\). For the normalized optimal value \(V_A(\eta)=\min_a G_{A,\eta}(a)\), the one-sided derivative gap is
\[
 V_A'(1^-)-V_A'(1^+)=A\sqrt{A^2-4}.
\]

The entire stability phase diagram for the globally optimal feedback is as follows; *stable* means \(|a|<1\), *neutral* means \(a=1\), and *unstable* means \(a>1\):

| Plant parameter | Global optimum classification |
|---|---|
| \(0<A\le1\) | Stable for every \(\eta>0\). |
| \(1<A<2\) | Stable for \(\eta>(A-1)(3-A)\), neutral at equality, unstable below. |
| \(A=2\) | Stable for \(\eta>1\), neutral for \(\eta=1\), unstable for \(0<\eta<1\). |
| \(A>2\) | Stable for \(\eta>1\), unstable for \(0<\eta<1\), and exactly two global optima (one of each type) at \(\eta=1\). |

At the critical point \(A=2\), the optimal multiplier is continuous but obeys the singular law
\[
 a_*(2,1+\delta)=1-\operatorname{sgn}(\delta)
 \left(\frac{|\delta|}{2}\right)^{1/3}
 +o\bigl(|\delta|^{1/3}\bigr)
 \quad(\delta\to0,\ \delta\ne0).
\]

## Assumptions and scope

The system is \(x_{k+1}=Ax_k+Bu_k\), with fixed reference state zero. At each stage the myopic follower chooses \(u_k\) to minimize \(Ru_k^2-p(x_k,u_k;\Theta)\), where the fixed incentive is \(p(x,u;\Theta)=\Theta xu\). The leader chooses **one** real parameter \(\Theta\), without changing it during the two stages, to minimize
\[
 J(\Theta)=\sum_{k=0}^{1}\left(Qx_k^2+p(x_k,u_k;\Theta)\right).
\]
There is no terminal state penalty, admissibility constraint on \(\Theta\), or imposed Schur-stability constraint. The follower has an unconstrained real input. These are the minimal two stages for which feedback influences a subsequent state cost in this formulation. The analysis also applies to random \(x_0\) when \(0<\mathbb E[x_0^2]<\infty\), after multiplying \(J\) by that moment instead of \(x_0^2\).

## Proof

**Reduction.** The follower's strictly convex single-stage problem has the unique solution \(u_k=\Theta x_k/(2R)\), and the leader pays \(p=\Theta^2x_k^2/(2R)\). The closed-loop multiplier is \(a=A+B\Theta/(2R)\); therefore \(x_1=ax_0\) and
\[
 J(\Theta)=x_0^2\left(Q+\frac{\Theta^2}{2R}\right)(1+a^2)
 =\frac{2Rx_0^2}{B^2}G_{A,\eta}(a).
\]
The linear change between \(\Theta\) and \(a\) is bijective. Since \(G_{A,\eta}(-a)>G_{A,\eta}(a)\) for every \(a>0\), \(G'_{A,\eta}(0)=-2A<0\), and \(G'_{A,\eta}(a)>0\) for all \(a\ge A\), every global optimizer lies in \((0,A)\).

**Global minimizers and symmetry.** Put \(y=a-A/2\). Direct expansion gives
\[
 G_{A,\eta}(A/2+y)
 =y^4+\left(1+\eta-\frac{A^2}{2}\right)y^2
 +A(\eta-1)y
 +\frac{A^4}{16}+\frac{A^2(\eta+1)}4+\eta.
\]
When \(\eta\ne1\), reflection \(y\mapsto-y\) shows that every global minimizer has \(y>0\) if \(\eta<1\) and \(y<0\) if \(\eta>1\). On that favored half-line, writing \(z=|y|>0\), the objective is a constant plus \(z^4+pz^2-|A(\eta-1)|z\), whose derivative \(4z^3+2pz-|A(\eta-1)|\) has **exactly one** positive root. If \(p\ge0\) the derivative is increasing. If \(p<0\), it first decreases and then increases, crossing zero only on its increasing branch. Hence the global minimizer is unique. It is equivalently the unique derivative root on the favored side of \(A/2\), where
\[
 \frac12G'_{A,\eta}(a)=P_{A,\eta}(a)
 =2a^3-3Aa^2+(A^2+1+\eta)a-A.
\]
At \(\eta=1\), differentiation factors exactly:
\[
 G'_{A,1}(a)=2(2a-A)(a^2-Aa+1).
\]
The centered quartic is \(y^4+(2-A^2/2)y^2+\text{constant}\). For \(A\le2\), its sole global minimum is \(a=A/2\). For \(A>2\), its precisely two global minima are \(a_\pm\). Since \(a_+a_-=1\) and \(a_++a_-=A\), both give \(G_{A,1}(a_\pm)=A^2\); the central stationary point is strictly higher by \((A^2-4)^2/16\).

**Closed-loop stability.** Every optimal multiplier is positive, so Schur stability is equivalent to \(a<1\). If \(A\le1\), the already-proved bound \(a<A\) suffices. If \(1<A<2\), note that \(a=1\) is on the favored half-line whenever \(\eta<1\) and
\[
 P_{A,\eta}(1)=\eta-(A-1)(3-A).
\]
The unique derivative zero on that half-line lies below, at, or above one according as this expression is positive, zero, or negative. For \(\eta\ge1\), the optimizer lies at or to the left of \(A/2<1\). This proves the middle row. For \(A=2\), the sign of \(\eta-1\) locates the optimizer strictly to one side of \(a=1\), except that \(\eta=1\) gives \(a=1\). For \(A>2\) and \(\eta>1\), the favored minimizer is left of \(A/2\); since \(P_{A,\eta}(0)<0\) but \(P_{A,\eta}(a_-)=(\eta-1)a_->0\), it lies below \(a_-<1\). Similarly, if \(\eta<1\), then \(P_{A,\eta}(a_+)=(\eta-1)a_+<0\), so the favored minimizer lies above \(a_+>1\). This proves the full classification.

**Jump and cusp.** Coercivity gives compactness of minimizing sequences as \(\eta\to1\), while the strict favored-side condition and the isolated minima at \(\eta=1\) give the one-sided limits \(a_+\) and \(a_-\), respectively. On either side, the smooth unique optimizer allows the envelope formula \(V_A'(\eta)=1+a_*(A,\eta)^2\), yielding the stated derivative gap. When \(A=2\), set \(\delta=\eta-1\) and \(y=a_*-1\). Stationarity reads \(2y^3+\delta y+\delta=0\). Uniqueness and continuity give \(y\to0\); hence \(y^3/\delta\to-1/2\), proving the cubic-root law.

## Verification

The standalone `CHECK.py` uses standard-library rational arithmetic to check 54,000 polynomial identities, 855 exact rational identities for the two global minimum branches, and 143 independently bracketed high-precision phase-diagram cases. Its saved output is `CHECK_OUTPUT.txt`. The symbolic factorization, favored-half-line uniqueness argument, and sign comparisons above—not the finite tests—prove the conclusions for all permitted parameters.

A fully rational witness is \(A=5/2\), \(B=1\), \(Q=2\), \(R=1\), and \(x_0=1\). Then \(\eta=1\), and the two globally optimal incentives \(\Theta=-4\) and \(\Theta=-1\) give respective closed-loop multipliers \(1/2\) and \(2\), with identical leader cost \(25/2\). The midpoint multiplier \(5/4\) instead costs \(1681/128\), exceeding the minimum by \(81/128\).

## Relationship to prior work

Matt, Bolognani, and Dörfler (arXiv:2604.27770, first posted 30 April 2026) introduce the fixed bilinear incentive and derive the general scalar finite-horizon leader cost (their Proposition 2), followed by long-horizon and high-follower-cost optimal incentive formulas. Their displayed finite-horizon objective provides the starting point here. It does **not** state a global optimizer classification for the two-period horizon, its cost-ratio duality, the transition between stable and unstable *global* optimizers, or the cubic-root boundary. Those results require the exact global minimization and root-order arguments above. The earlier dynamic-contract formulation of Wasa, Hirata, and Uchida (2019) uses a different LEQG agency contract with risk and information constraints; the accessible article does not derive this two-period bilinear feedback phase diagram. The algebraic centered-quartic normal form is classical; no claim of novelty is made for generic quartic minimization itself.

## Limitations

The result concerns an unrestricted finite-horizon leader objective. It does not assert that an unstable feedback is advisable or admissible when asymptotic stability is required; imposing Schur stability changes the feasible leader problem. The exact reflection symmetry depends on zero reference, constant scalar plant, fixed bilinear payment, identical stage weights, and exactly two cost stages. It does not establish an equivalent switch for arbitrary horizons, strategic rather than myopic followers, constrained controls, nonlinear plants, or payment mechanisms. A literature-priority risk remains from earlier dynamic incentive and nonconvex control research; independent evaluation has not been performed.

## References

1. J. G. Matt, S. Bolognani, and F. Dörfler, *Optimal Functional Incentives for Control: The Linear-Quadratic Case with Bilinear Incentives*, arXiv:2604.27770, first public version 30 April 2026; https://arxiv.org/html/2604.27770 . Section III-B, Proposition 2 and the adjacent asymptotic results.
2. Y. Wasa, K. Hirata, and K. Uchida, *Optimal agency contract for incentive and control under moral hazard in dynamic electric power networks*, IET Smart Grid, 2019, DOI:10.1049/iet-stg.2018.0256; https://doi.org/10.1049/iet-stg.2018.0256 .
3. X. Feng, Y. Hu, and J. Huang, *Backward Stackelberg Differential Game with Constraints: A Mixed Terminal-Perturbation and Linear-Quadratic Approach*, SIAM J. Control Optim. 60 (2022), 1488–1518, arXiv:2005.11872; https://arxiv.org/abs/2005.11872 . (Different dynamics and contracts; abstract examined.)
