# At most three defector–protector coexistence states, sharply attained at four players

## Finding

In the three-strategy quorum-activated collective-risk public-goods game of Li, Li, He, Shi, and Szolnoki [1], **every defector–protective-cooperator edge has at most three distinct nonendpoint equilibria (counting multiplicities), regardless of group size**, and at most one can attract nearby states *within that edge*. These bounds hold for every integer group size \(N\ge3\), quorum \(2\le M\le N-1\), multiplication factor \(1<r<N\), costs \(c,k,L>0\), risk parameter \(\gamma>0\), and protection effectiveness \(0\le\omega\le1\).

The bound on equilibria is sharp in the smallest possible group: for
\[
(N,M,r,c,L,k,\gamma,\omega)
=(4,2,2,1,5/2,9/50,\log 5,1/2),
\]
the edge selection gradient equals
\[
B(z)=\frac{528z^3-879z^2+474z-83}{125}.
\]
There are exactly three simple coexistence equilibria, in the disjoint intervals \((0,1/2)\), \((1/2,3/5)\), and \((3/5,3/4)\). The middle equilibrium attracts on the edge **and in the full three-strategy simplex**; the other two repel in the edge direction. A group of three cannot have three such states because its gradient has degree at most two.

## Assumptions and scope

The well-mixed infinite population has ordinary cooperators \(C\), defectors \(D\), and protective cooperators \(S\) with frequencies \((x,y,z)\), \(x+y+z=1\). Random groups have \(N\) members, with public-goods multiplier \(r\). Each \(C\) or \(S\) contributes \(c\); each \(S\) pays additional protection cost \(k\). If a group has \(d_f\) defectors, its collective-failure probability before protection is \(1-e^{-\gamma d_f}\). Each group member incurs expected loss \(L\) times the failure probability. Once the number of protective cooperators reaches quorum \(M\), the failure probability is multiplied by \(1-\omega\). These are the payoff assumptions of [1], with \(\rho=e^{-\gamma}\in(0,1)\). The biological or social interpretation of the parameters is not used in the algebra.

We restrict to the invariant \(D\)--\(S\) edge \(x=0\), writing \(z\) for the frequency of \(S\) and \(n=N-1\). On this edge \(\dot z=z(1-z) B(z)\), where \(B(z)=P_S(z)-P_D(z)\). A nonendpoint equilibrium has \(0<z<1\) and \(B(z)=0\). *Edge attraction* is two-sided local asymptotic stability under this one-dimensional equation. Full-simplex attraction additionally requires decay of the missing-\(C\) coordinate; this is established only for the explicit sharpness example, not for every possible edge equilibrium.

## Proof

**Exact payoff reduction.** Condition on \(j\in\{0,\ldots,n\}\) protective coplayers (the other \(n-j\) coplayers being defectors), and let \(d=1-\rho\) and \(a=rc/N-c<0\). Comparing focal \(S\) and focal \(D\), their expected-payoff difference in that group is
\[
\Delta_j=a-k+Ld\rho^{n-j}\bigl(1-\omega\mathbf1_{j\ge M}\bigr)
   +L\omega(1-\rho^{n-j})\mathbf1_{j=M-1}.
\]
Indeed, when the quorum is unmet for both focal choices, a focal \(S\) reduces the defector count by one; when it is met for both, that risk benefit is reduced by \(1-\omega\); when exactly \(M-1\) protective coplayers are present, focal \(S\) additionally activates protection while focal \(D\) does not. The public-goods payoff difference is \(a\), and the additional personal cost is \(k\).

Binomial sampling gives \(B(z)=\sum_{j=0}^n\binom nj\Delta_j z^j(1-z)^{n-j}\). Put
\[
h=\frac{k-a}{Ld}>0,\qquad
B(z)=Ld\bigl(f(z)-h\bigr),\qquad
f(z)=\sum_{j=0}^n\binom nj b_j z^j(1-z)^{n-j},
\]
with explicit Bernstein coefficients
\[
b_j=\begin{cases}
\rho^{n-j},&0\le j\le M-2,\\
\rho^{n-M+1}+\dfrac{\omega(1-\rho^{n-M+1})}{1-\rho},&j=M-1,\\
(1-\omega)\rho^{n-j},&M\le j\le n.
\end{cases}
\]
For the middle coefficient, \(b_{M-1}\ge\rho^{n-M+1}\); for the pre-quorum block \(b_{j+1}>b_j\). For the post-quorum block \(b_{j+1}\ge b_j\), with equality there only when \(\omega=1\). Thus \((b_0,\ldots,b_n)\) increases strictly until index \(M-1\), may drop at the single boundary \(M-1\to M\), and is nondecreasing thereafter.

**Universal three-root ceiling.** Subtracting any constant \(h\) from a sequence that is increasing, possibly drops once, and is thereafter nondecreasing gives at most three nonzero sign changes. Substitute \(z=t/(1+t)\), with \(t>0\):
\[
(1+t)^n\left(f\!\left(\frac{t}{1+t}\right)-h\right)
=\sum_{j=0}^n\binom nj(b_j-h)t^j.
\]
The positive binomial weights preserve the coefficient sign pattern. Descartes' rule of signs bounds the number of positive roots counted with multiplicities by three, hence gives the same bound for \(B\)'s zeros in \((0,1)\). No identically zero exception arises because \(b_1>b_0\): when \(M=2\), the middle coefficient dominates \(\rho^{n-1}>\rho^n\), and when \(M>2\), both are consecutive powers of \(\rho\). This use of Bernstein sign variation follows the general theory in [2], but the three-block coefficient structure and its exact consequences here are model-specific.

**At most one edge attractor.** Differentiate in Bernstein form:
\[
f'(z)=n\sum_{j=0}^{n-1}\binom{n-1}{j}(b_{j+1}-b_j)z^j(1-z)^{n-1-j}.
\]
The difference coefficients have the sign pattern positive, possibly one negative entry, then nonnegative. The same Descartes argument bounds the number of interior derivative zeros (counted with multiplicities) by two, while \(f'(0)=n(b_1-b_0)>0\). Consequently the set where \(f'<0\) can have at most one connected interval: two disjoint negative intervals would require at least three derivative zeros between them and the initial positive derivative. Any two-sided attracting zero of \(B\) requires \(B\) to change from positive to negative through that zero. Two such transitions would require two disjoint declining regions, impossible by the preceding derivative structure. Hence at most one interior equilibrium attracts on the edge, and therefore at most one can attract in the full simplex.

**Sharp instance and full-simplex stability.** At the specified four-player parameters, \(n=3\), \(\rho=1/5\), \(d=4/5\), \(a=-1/2\), \(Ld=2\), and \(h=17/50\). The Bernstein coefficients are
\[
(b_0,b_1,b_2,b_3)=(1/125,16/25,1/10,1/2),
\]
which expand to the cubic \(B\) in the finding. Direct exact evaluations give
\[
B(0)=-83/125<0,\quad B(1/2)=1/500>0,\quad
B(3/5)=-124/15625<0,\quad B(3/4)=13/2000>0.
\]
The intermediate-value theorem and degree three imply exactly three simple roots in the indicated disjoint intervals, with directional signs \(-,+,-,+\). The middle root is attracting on the edge.

For its transverse stability, compare ordinary cooperators with defectors along \(x=0\). Let \(A(z)=P_C-P_D\); in this model
\[
A(z)=a+Ld\!\left[(\rho+dz)^n-\omega\sum_{j=M}^{n}\binom nj\rho^{n-j}z^j(1-z)^{n-j}\right].
\]
At any edge equilibrium \(B=0\), the payoff identity gives \(A(z)=k-L\omega\Psi_M(z)\), where \(\Psi_M(z)=\binom{n}{M-1}(1-\rho^{n-M+1})z^{M-1}(1-z)^{n-M+1}\). For the explicit instance this reduces, *at an edge equilibrium*, to \(A(z)=9/50-(18/5)z(1-z)^2\). Throughout \(z\in[1/2,3/5]\), \(z(1-z)^2\ge12/125\), giving \(A(z)\le9/50-216/625<0\). The full replicator Jacobian at the middle root is triangular in coordinates \((x,z)\) with eigenvalues \(A(z)<0\) and \(z(1-z)B'(z)<0\). Thus the middle equilibrium is locally asymptotically stable in the full simplex, whereas the outer two are unstable in their edge direction. Finally, group size \(N=3\) gives \(n=2\), so a cubic three-root example is impossible there.

## Verification

The self-contained `verify.py` checks group-level payoff differences directly against the derived Bernstein representation, for \(2\le n\le9\), every allowable quorum, three exact rational risk values, four effectiveness values, and five frequencies. It also verifies the coefficient sign patterns at five comparison levels, the exact polynomial identity, the four rational root brackets, and the transverse eigenvalue sign on the stabilizing interval. Its recorded output is `PASS: 2169 exact checks; 3 simple D/S roots in disjoint rational intervals`. The exact proof of the universal root and stability bounds is the Descartes/Bernstein argument above, not these finite calculations.

## Relationship to prior work

Li, Li, He, Shi, and Szolnoki [1] derive the multinomial payoff differences and investigate protection quorum saddle-node bifurcations numerically and analytically. Their displayed stability cases concern a single attracting coexistence state and a saddle-type coexistence state; the inspected text does not state this global three-root ceiling or provide the four-person three-root witness. Archetti [2, §§2.2, 2.4] teaches the general Bernstein variation-diminishing approach for nonlinear public-goods games. The method is therefore **not new**. The additional content is the exact jump structure induced by activating protection at quorum, the resulting universal bound and edge-attractor uniqueness for [1]'s model, and an explicit smallest-group sharpness and full-simplex stability witness. These statements are not implied by generic root-count bounds without establishing the specific Bernstein coefficient shape.

## Limitations

The result counts equilibria only on the defector–protective-cooperator boundary, not equilibria in the interior of the three-strategy simplex or on other edges. No global basin-area or finite-population stochastic conclusion is claimed. The general uniqueness statement concerns attraction on the boundary; full-simplex stability is shown for the explicit middle root only. The conclusions presume the precise binomial sampling, threshold activation, multiplicative risk reduction, and costs specified above. Literature-index coverage is not a proof of priority, and an equivalent result outside inspected sources remains possible. The mathematical verification is not an independent audit.

## References

1. Shulan Li, Xiaogang Li, Jun He, Lei Shi, and Attila Szolnoki, *Bifurcation and Multistability in a Collective-Risk Public Goods Game with Quorum-Activated Protection*, arXiv:2609.28132 (first posted 2026-09-23), https://arxiv.org/abs/2609.28132. See its model payoffs, defector–protector edge analysis, and appendices.
2. Marco Archetti, *How to Analyze Models of Nonlinear Public Goods*, *Games* **9**(2):17 (2018), https://doi.org/10.3390/g9020017; especially §§2.2 and 2.4 on Bernstein sign variation.
