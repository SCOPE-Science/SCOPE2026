# Universal interior reactivity allocation for a sticky run-and-tumble particle

## Finding
Let a one-dimensional run-and-tumble particle move in an interval with two sticky, partially absorbing endpoints. When the total wall absorption rate is fixed, **the mean absorption time has a unique optimal allocation that assigns a strictly positive rate to each wall**. This remains true for every nondegenerate initial position and even completely polarized initial velocity. The exact optimum depends on starting position and orientation only through one effective bias.

Write \(T=L/v\), \(\lambda=\alpha T\), \(\eta=\gamma T\), \(\beta=KT\), and
\[
 w=\lambda\left(\frac{2x}{L}-1\right)+(2p-1),\quad
 F=\beta(\lambda+1),\quad
 B=2(\lambda+1)[\beta(\lambda+1)+4\eta],\quad
 H=F+4\eta.
\]
For \(h=(\kappa_L-\kappa_R)/K\), the unique minimizer on \([-1,1]\) is
\[
 \boxed{h_*=-\frac{2Hw}{B+\sqrt{B^2-4FHw^2}}},\qquad
 \boxed{\kappa_L^*=\tfrac K2(1+h_*),\quad \kappa_R^*=\tfrac K2(1-h_*)}.
\]
In particular \(-1<h_*<1\) for all admissible data; it is odd and strictly decreasing in \(w\). Equal allocation is optimal exactly when \(w=0\). A particle initially nearer the right wall need not favor the right wall if its initial orientation bias compensates its position bias.

## Assumptions and scope
Take arbitrary \(L,v,\alpha,\gamma,K>0\), \(x\in(0,L)\), and \(p\in[0,1]\). In the bulk the particle has velocity \(\pm v\), switching between signs at exponential rate \(\alpha\). Its initial orientation is rightward with probability \(p\). At the left wall with leftward velocity, or the right wall with rightward velocity, it becomes immobile. In either sticky state it returns to the bulk with inward orientation at rate \(\gamma\), or is killed at respective rates \(\kappa_L\ge0\), \(\kappa_R\ge0\), independently. The rates satisfy \(\kappa_L+\kappa_R=K\). In the proof, when one absorption rate is zero, the other positive wall still guarantees finite mean killing time. No wall residence is assigned to the particle initially because \(x\) lies strictly inside the interval.

This is a theorem for *constant, memoryless, time-independent* wall rates under a sum-of-rates budget, not a theorem about optimal choices of bulk switching rates or about finite-horizon survival probability.

## Proof
Let \(m_+(y)\) and \(m_-(y)\) be the expected remaining times until absorption starting at interior point \(y\) with respective orientations. The backward generator gives
\[
 vm_+'+\alpha(m_--m_+)=-1,\qquad
 -vm_-'+\alpha(m_+-m_-)=-1.
\]
Define \(d=m_+-m_-\), \(s=(m_++m_-)/2\), and \(a=y/v\). Integrating yields
\[
 d(y)=C-2a,\qquad s(y)=A+\alpha Ca-\alpha a^2.
\]
At the left wall, the outgoing (leftward) state waits an exponential time of parameter \(\gamma+\kappa_L\), then either dies or returns rightward. Similarly at the right wall. Hence the exact boundary conditions are
\[
 (\gamma+\kappa_L)m_-(0)=1+\gamma m_+(0),\qquad
 (\gamma+\kappa_R)m_+(L)=1+\gamma m_-(L).
\]
Putting \(u=\kappa_L\), \(q=\kappa_R\), these linear conditions determine
\[
 C=\frac{\alpha T^2uq+2\gamma Tu+Tuq+u-q}
 {\alpha Tuq+\gamma(u+q)+uq},\qquad
 A=\frac{1+(\gamma+u/2)C}{u}
\]
for \(u>0\); the endpoint allocation values are obtained continuously from the linear system. The requested orientation mixture has mean
\[
 \mathcal M(u,q;x,p)=A+\alpha C\frac xv-\alpha\left(\frac xv\right)^2
 +(2p-1)\left(\frac C2-\frac xv\right).
\]
Substitute \(u=K(1+h)/2\), \(q=K(1-h)/2\), \(\xi=2x/L-1\), and \(\zeta=2p-1\). Exact differentiation and cancellation produce
\[
 \frac{d}{dh}\frac{\mathcal M}{T}
 =\frac{2(\eta+1)}{[F(h^2-1)-4\eta]^2}
 \left\{Fw(h^2+1)+Bh+4\eta w\right\},
 \qquad w=\lambda\xi+\zeta.
\]
The denominator is strictly positive for \(-1\le h\le1\). Let \(P(h)=Fw(h^2+1)+Bh+4\eta w\). Since \(|w|\le\lambda+1\),
\[
 P'(h)=2Fwh+B\ge B-2F(\lambda+1)=8\eta(\lambda+1)>0,
\]
and
\[
 P(-1)\le -B+(2F+4\eta)(\lambda+1)=-4\eta(\lambda+1)<0,
\]
\[
 P(1)\ge B-(2F+4\eta)(\lambda+1)=4\eta(\lambda+1)>0.
\]
Thus \(P\) has exactly one zero strictly inside \((-1,1)\), and the mean absorption time decreases before it and increases after it. Solving this quadratic by its cancellation-stable branch gives \(h_*\) above. Its discriminant is positive because \(B>(2F+4\eta)(\lambda+1)\ge2\sqrt{FH}\,|w|\). Since \(\partial_wP=F(h^2+1)+4\eta>0\) and \(P'(h_*)>0\), implicit differentiation shows \(dh_*/dw<0\). Oddness and the condition \(h_*=0\iff w=0\) follow directly. All statements hold at \(p=0,1\) because the strict inequalities use only \(|2p-1|\le1\).

## Verification
The proof is analytical. The companion standard-library checker implements the backward-equation solution independently of the closed-form optimizer, compares the latter with numerical minimization on multiple physical parameter sets, and verifies the sign of the derivative on both sides of the optimum. An additional event-driven simulation was run for three disparate parameter sets with 35,000 independent trajectories each; relative deviations between simulated mean absorption times and the exact formula were below \(0.12\%\). The simulation is a finite numerical check, not a proof of uniqueness or validity for all parameters.

## Relationship to prior work
Bressloff (2023) establishes the sticky-boundary run-and-tumble model, residence-time absorption, and forward boundary-value machinery, including distinct wall reactivities. Angelani (2023) gives a broad first-passage framework and general mean exit-time formulas for assorted boundary conditions, with a symmetric orientation preparation. Angelani (2023, *Optimal escapes in active matter*) optimizes *tumbling rates* under boundary conditions. None of the inspected passages asserts the positive-interior **fixed-total-reactivity** optimality law for all initial orientation mixtures, or the one-dimensional effective-bias collapse and explicit optimizing split. Earlier first-passage formulas provide major ingredients. They should not be confused with a new derivation of the underlying process or of the unrestricted first-passage distribution.

## Limitations
The result does not establish an optimal time-varying wall policy, an optimal policy under a different physical cost function, or uniform finite-horizon survival stochastic ordering for arbitrarily prepared initial states. It assumes common positive boundary release rate and memoryless events. The exact optimization statement may be derivable from sufficiently general published first-passage formulas by substantial specialization and additional optimization; determining priority beyond the sources inspected remains a scientific risk. No independent audit has been performed.

## References
1. P. C. Bressloff, *Encounter-based model of a run-and-tumble particle II: absorption at sticky boundaries*, arXiv:2302.01158, first posted 2023-02-02. https://arxiv.org/abs/2302.01158
2. L. Angelani, *One-dimensional run-and-tumble motions with generic boundary conditions*, J. Phys. A: Math. Theor. **56** (2023), 455003, doi:10.1088/1751-8121/ad009e. https://iris.cnr.it/retrieve/e1d78abe-8685-4eff-936b-9bcad8ad4c0f/prod_489129-doc_203607.pdf
3. L. Angelani, *Optimal escapes in active matter*, arXiv:2311.11873, first posted 2023-11-20. https://arxiv.org/abs/2311.11873
