# Same-model review of “Exact Lyapunov monotonicity rules out bounded recurrent dynamics on the line-equilibrium slice of a 5D segmented disc dynamo”

## Correctness
**PASS.** The cancellation is exact: on \(k_1=0\), \(k_2=g>0\), and \(k_3=k_4=k_5=0\), differentiating \(H=z+g(1+m)x^2/(2r)\) gives \(\dot H=-gx^2\). For a bounded forward orbit, \(H\) has a finite limit and \(x\in L^2(0,\infty)\); bounded \(\dot x\) makes \(x\) uniformly continuous, so \(x(t)\to0\). The omega-limit set is invariant, and the tangency conditions \(x=0\Rightarrow y=0\Rightarrow v=0\Rightarrow u=0\) leave only the equilibrium line. Since \(z(t)\) also converges, the omega-limit set is one point. The invariant-measure argument follows from the same generator identity and invariance of the support. Exact arithmetic separately checks the source-parameter coefficient and the characteristic polynomial. No finite-time computation is used as an infinite-time proof.

## Originality
**PASS.** The introducing article (DOI 10.3934/dcdsb.2019130) was inspected through the exact equations, the line-equilibrium example, bifurcation sections, and conclusion. It reports the numerical chaotic/hyperchaotic cases but not the monotone function, convergence theorem, or invariant-measure classification. A related same-author segmented-disc-dynamo paper (DOI 10.1186/s13662-019-2284-0) uses a different five-dimensional vector field. General line-equilibrium work by Jafari and Sprott (DOI 10.1016/j.chaos.2013.08.018) shows that chaos can occur with an equilibrium line in other systems and therefore does not subsume this system-specific obstruction. Targeted searches by title, equations, parameters, aliases, and invariant-measure/Lyapunov formulations did not locate a statement implying the result. Residual risk remains that an unindexed secondary source contains the same identity.

## Value
**PASS.** The exact law rules out non-equilibrium compact recurrence on an entire natural parameter slice that the source uses to illustrate both chaos and hyperchaos. It also distinguishes a stationary state with unstable transverse variational dynamics from a hyperchaotic state-space trajectory, and classifies all compact stationary statistical states. That combination is structurally informative for interpreting numerical attractor claims in line-equilibrium systems and is not a generic consequence of having an equilibrium line.

## Closest literature and limitations
The closest source is the introducing 2019 DCDS-B article, because it contains the same equations and the exact line-equilibrium parameter example. Jafari–Sprott is the closest general line-equilibrium comparison, but its examples are different systems. The theorem assumes boundedness for forward-orbit convergence and does not classify unbounded trajectories or off-slice dynamics. The numerical finite-time exponent implementation itself was not reconstructed.

Same-model review: passed. Independent audit: not yet performed.
