# Sharp directional-rescue allocation in the two-patch extinction chain

## Finding

**Theorem (complete directional-budget optimization).** Let two habitat patches have positive local extinction rates \(a>0\) and \(b>0\). An occupied patch may recolonize the other, if empty: patch 1 to patch 2 at rate \(x\), and patch 2 to patch 1 at rate \(y\). Choose \(x,y\geq0\) subject to the fixed total rate budget \(x+y=C>0\). Assume a continuous-time Markov chain of occupancy states and a fixed initial distribution independent of the chosen rates: \(w_{11}\) for both occupied, \(w_{10}\) for patch 1 alone, and \(w_{01}\) for patch 2 alone, with nonnegative weights totaling one. Let \(\mathcal T(x)\) be the expected time until both patches are empty (absorbing total extinction), where \(y=C-x\).

Writing \(\delta=a w_{10}-b w_{01}\), the expected extinction time is a strictly concave quadratic in directional allocation, and its **unique** global maximizer is
\[
\boxed{x^*=\min\!\left\{C,\max\!\left\{0,\frac{C+\delta}{2}\right\}\right\},\qquad y^*=C-x^*.}
\]
Equivalently, the optimum is interior exactly when \(-C<\delta<C\), is all patch-1-to-patch-2 when \(\delta\ge C\), and all patch-2-to-patch-1 when \(\delta\le-C\). At equality the boundary optimum remains unique.

The perhaps unexpected special case is **full initial occupancy** \(w_{11}=1\): \(x^*=y^*=C/2\) for arbitrarily unequal positive extinction rates. For a single occupied source, the unique allocation tilts towards restoring the missing patch: \(w_{10}=1\) gives \(x^*=\min\{C,(C+a)/2\}\); \(w_{01}=1\) gives \(y^*=\min\{C,(C+b)/2\}\). Thus the optimal direction depends on *initial occupancy*, not just habitat quality.

## Assumptions and scope

There are two distinguishable habitat patches and one species. The states \(11,10,01,00\) record which patches are currently occupied; \(00\) is absorbing because external immigrants are absent. Local extinction is an independent exponential transition at rate \(a\) for occupied patch 1 and \(b\) for occupied patch 2, regardless of the other patch. Colonization is possible only from an occupied patch to an empty patch, with rates \(x\) for \(10\to11\) and \(y\) for \(01\to11\). The total linear colonization-rate budget is \(x+y=C\); there is no budget for changing local extinction rates. Initial-state weights are specified independently of the allocation. All claims concern **mean time to total extinction**, not deterministic equilibrium, finite-horizon viability, or arbitrary multi-patch networks.

## Proof

Let \(t_{11},t_{10},t_{01}\) denote the mean hitting times of \(00\) from the three nonabsorbing states. First-step conditioning gives the exact backward equations
\[
\begin{aligned}
(a+b)t_{11}&=1+b t_{10}+a t_{01},\\
(a+x)t_{10}&=1+x t_{11},\\
(b+y)t_{01}&=1+y t_{11}.
\end{aligned}
\]
Since \(a,b>0\) and the state space is finite, eventual absorption is certain and all expectations are finite. Solving the three linear equations, with \(D=ab(a+b+x+y)>0\), yields
\[
\begin{aligned}
t_{11}&=\frac{a^2+ab+b^2+(a+b)(x+y)+xy}{D},\\
t_{10}&=\frac{(b+x)(a+b+y)}{D},\\
t_{01}&=\frac{(a+y)(a+b+x)}{D}.
\end{aligned}
\]
These identities can also be checked by direct substitution into all three backward equations. The common denominator depends on \(x,y\) only through \(x+y\), which is fixed.

Set \(y=C-x\), \(D_C=ab(a+b+C)\), and
\[
K=w_{11}\bigl[a^2+ab+b^2+(a+b)C\bigr]
 +w_{10}b(a+b+C)+w_{01}(a+C)(a+b).
\]
Expanding the three numerators and using \(w_{11}+w_{10}+w_{01}=1\) gives the exact objective
\[
\boxed{\mathcal T(x)=\frac{K+(C+a w_{10}-b w_{01})x-x^2}{D_C}},\qquad 0\le x\le C.
\]
Its second derivative is \(\mathcal T''(x)=-2/D_C<0\); hence it has at most one maximizer. Completing the square with \(z=(C+\delta)/2\),
\[
\mathcal T(x)=\frac{K+z^2-(x-z)^2}{D_C}.
\]
Maximizing over the closed interval \([0,C]\) is therefore equivalent to projecting \(z\) onto that interval, proving the displayed unique optimizer and every boundary condition.

The exact *global optimality certificate* for any feasible allocation \(x\) is
\[
\boxed{\mathcal T(x^*)-\mathcal T(x)
=\frac{(x-z)^2-(x^*-z)^2}{D_C}\ge0,}
\]
with equality exactly when \(x=x^*\). If \(|\delta|<C\), the gain over a symmetric budget split is precisely \(\delta^2/(4D_C)\). Substituting \(w_{11}=1\), \(w_{10}=1\), or \(w_{01}=1\) proves the stated initial-state cases.

## Verification

A standalone Python 3 standard-library checker, `verify_allocation.py`, independently solves the rational \(3\times3\) backward system by Gauss-Jordan elimination and compares it to all three closed forms. It checks every positive integer triple \((a,b,C)\in\{1,2,3,4\}^3\), every ninth-grid allocation \(x=jC/8\) for \(0\le j\le8\), and all 15 nonnegative initial-distribution profiles with weights of denominator four. It then checks projected optimizer superiority on each nine-point grid, and exact stationary-point and local strictness identities in all interior cases. Output on the packaged code: `VERIFY_OK exact_backward_systems=576 weighted_expectations=8640 allocation_instances=960 global_grid_inequalities=8640`. The universal proof is algebraic and does not rely on finite testing.

A checkable example is \(a=2\), \(b=5\), \(C=3\). Starting at \(11\), the unique optimum is \((x^*,y^*)=(3/2,3/2)\) with mean extinction time \(249/400\). Starting at \(10\), it is \((5/2,1/2)\) with time \(9/16\). Starting at \(01\), it is \((0,3)\) with time \(7/20\). These numbers follow from the displayed rational formulas.

## Relationship to prior work

Vuilleumier and Possingham (2006) examine the ecological importance of directional connections using simulation of 100-patch landscapes with common local extinction probability and a finite-horizon persistence outcome. Their directional-colonization motivation is directly relevant, but their reported model and results do not provide the exact budget-constrained two-patch mean-extinction-time optimizer above. Ross and Pollett (2009, with a 2010 journal presentation) derive metapopulation management rules comparing a **single aggregate colonization rate** with a local extinction rate under a budget; splitting the aggregate into oppositely directed rates at fixed total and allowing an arbitrary allocation-independent initial occupancy distribution is a different problem. Ross, Sirl, Pollett and Possingham (2008) consider protecting versus creating habitat patches. Etienne and Heesterbeek (2001) develop extinction/colonization investment heuristics in a stochastic winking-patch model; that work is relevant but the accessible abstract does not establish this continuous-time directional-budget theorem. The closest available comparisons, their precise model differences, and limits of document access are documented in the accompanying scientific review.

## Limitations

The two-patch Markov assumptions, independent constant extinction hazards, fixed sum of directed colonization rates, and allocation-independent starting weights are essential to the stated optimization. No claim is made for more than two patches, demographic population sizes, time-varying dispersal, nonlinear management costs, stochastic environmental coupling, or transition-dependent local extinction. The directionally biased optimum may change if the initial distribution changes with the decision. Exact algebra does not establish empirical realism. The literature comparison is extensive but not exhaustive, and the complete texts of the 2001 winking-patch and 2010 management papers were not obtained; a stronger previously published result remains a residual risk.

## References

1. S. Vuilleumier and H. P. Possingham (2006), *Does colonization asymmetry matter in metapopulations?*, Proceedings of the Royal Society B, 273, 1637–1642. DOI: `10.1098/rspb.2006.3469`. Public article date: 2006-03-29. https://pmc.ncbi.nlm.nih.gov/articles/PMC1634917/
2. R. S. Etienne and J. A. P. Heesterbeek (2001), *Rules of thumb for conservation of metapopulations based on a stochastic winking-patch model*, American Naturalist 158, 389–407. DOI: `10.1086/321986`.
3. J. V. Ross and P. K. Pollett (2009), *Rules of thumb for metapopulation management*, MODSIM09, 1795–1801. https://digital.library.adelaide.edu.au/items/e3f694a2-efa9-41c7-be9d-baa9d79b1fd9
4. J. V. Ross and P. K. Pollett (2010), *Simple rules for ranking and optimally managing metapopulations*, Ecological Modelling 221, 2515–2520. DOI: `10.1016/j.ecolmodel.2010.02.016`.
5. J. V. Ross, D. J. Sirl, P. K. Pollett and H. P. Possingham (2008), *Metapopulation persistence in a dynamic landscape: more habitat or better stewardship*, Ecological Applications 18, 590–598. DOI: `10.1890/07-1094.1`.
