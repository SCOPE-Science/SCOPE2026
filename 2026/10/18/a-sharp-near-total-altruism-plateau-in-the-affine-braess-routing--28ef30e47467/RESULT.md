# A sharp near-total altruism plateau in the affine Braess routing game

## Finding

In a classical directed Braess network with three source–destination routes and positive affine edge delays, there is an open parameter regime where the exact equilibrium social cost stays **strictly above optimum and unchanged** until a sharp autonomous-vehicle penetration threshold. The threshold can approach \(100\%\) while the excess social cost remains bounded away from zero.

Write \(\alpha\in[0,1]\) for the mass of altruistic vehicles within unit demand and define
\[
H=b-a-c-\frac{p-q}{2},\quad K=p-q-(b-a-c),\quad L=\frac{p+q}{2}+r,\quad h=\frac{H}{L}.
\]
For every equilibrium, the flow on the middle shortcut and total social travel cost are exactly
\[
z(\alpha)=\min\{h,1-\alpha\},\qquad
S(\alpha)=a+b+\frac{p+q}{2}+Kz(\alpha)+Lz(\alpha)^2.
\]
In particular, the complete penetration-response law has one horizontal branch on \([0,1-h]\), followed by one strictly descending quadratic branch on \([1-h,1]\). The all-altruistic optimum is achieved only at \(\alpha=1\).

## Assumptions and scope

Use the directed graph with vertices \(s,u,v,t\) and five edges \(s\to u\), \(u\to t\), \(s\to v\), \(v\to t\), and \(u\to v\). Three paths are available: \(P_1=sut\), \(P_2=svt\), and \(P_3=suvt\). Edges \(s\to u\) and \(v\to t\) have delay \(a+pf\), edges \(u\to t\) and \(s\to v\) have delay \(b+qf\), and shortcut \(u\to v\) has delay \(c+rf\), where \(f\) denotes total edge flow. There is a unit-mass nonatomic population: humans of mass \(1-\alpha\) minimize path travel time, whereas altruistic vehicles of mass \(\alpha\) minimize the path marginal contribution to total network travel cost. All users may take any of the three paths. The ordinary mixed Wardrop equilibrium is defined by minimum perceived path cost within each positive-mass type, with arbitrary behavior by a zero-mass type.

Assume
\[
p>q>0,\qquad a>0,\ c>0,\ r>0,\qquad
\frac{p-q}{2}<b-a-c<p-q.
\]
Thus \(b>0\), \(H,K,L>0\), and \(0<h<1\). Every statement holds for every real \(\alpha\in[0,1]\); the theorem is not a limiting or perturbative statement.

## Proof

**1. Construct an equilibrium.** For a proposed total shortcut-path flow \(z\in[0,1]\), put equal total flow \((1-z)/2\) on each outer path. The two edges of type \(a+pf\) then carry \((1+z)/2\) each, the two edges of type \(b+qf\) carry \((1-z)/2\) each, and the shortcut carries \(z\). The two outer paths have identical travel times, as do their marginal social costs. Direct subtraction gives the cross-versus-outer differences
\[
C^H_3-C^H_1=-H+Lz,\qquad
C^A_3-C^A_1=K+2Lz.
\]
The same equalities hold with outer path \(P_2\) in place of \(P_1\). Since \(K>0\), an altruistic vehicle strictly prefers either outer path for every \(z\ge0\).

For \(0\le\alpha\le1-h\), route \(\alpha/2\) altruistic users onto each outer path, \(h\) human users onto the shortcut, and \((1-\alpha-h)/2\) human users onto each outer path. All these flows are feasible. Humans are indifferent because \(-H+Lh=0\), and the altruistic type strictly prefers its used outer paths. Hence these flows constitute an equilibrium, with \(z=h\).

For \(1-h\le\alpha\le1\), route \(\alpha/2\) altruists onto each outer path and **all** \(1-\alpha\) humans onto the shortcut. Then \(z=1-\alpha\le h\), so humans weakly prefer the shortcut and altruists strictly prefer outer paths. This is again an equilibrium. The endpoint \(\alpha=0\) and \(\alpha=1\) are covered, with the absent type imposing no condition.

**2. Rule out a second aggregate outcome.** Every edge has a common positive-affine delay \(k f+b_0\) with \(k>0\), \(b_0\ge0\), the exponent-one instance of Assumption 1 in Yi and Wei (2026). Their Theorem 2, including its Appendix II proof, establishes **uniqueness of aggregate equilibrium link flow** for the simultaneous nonatomic selfish/marginal-cost game. We use that established theorem only for uniqueness, not for construction, the cutoff, or the social-cost calculation. Because total shortcut flow is its own link flow, every equilibrium has the constructed value \(z(\alpha)\).

**3. Compute social cost and optimum.** For any symmetric route split with shortcut flow \(z\), the exact total edge-delay sum is
\[
S(z)=2\Big(\frac{1+z}{2}\Big)\Big(a+p\frac{1+z}{2}\Big)
+2\Big(\frac{1-z}{2}\Big)\Big(b+q\frac{1-z}{2}\Big)+z(c+rz)
=a+b+\frac{p+q}{2}+Kz+Lz^2.
\]
The all-altruistic equilibrium has \(z=0\), and strictly convex total edge delay makes it the unique social optimum in aggregate link flows; alternatively, at \(z=0\) the two used outer paths have equal marginal costs and the unused shortcut has marginal cost larger by \(K>0\). For all \(z>0\), \(S(z)-S(0)=Kz+Lz^2>0\). The equilibrium formula follows by substitution. For \(\alpha>1-h\), \(z=1-\alpha\) decreases and \(dS/dz=K+2Lz>0\); thus the improvement is strict and no smaller \(\alpha\) reaches optimum.

**4. A near-total-penetration family with fixed-size loss.** For integers \(n\ge2\), set \(p=2n\), \(q=r=a=c=1\), and \(b=n+5/2\). Then all stated strict inequalities hold,
\[
H=1,\quad L=n+\frac32,\quad K=n-\frac32,\quad h=\frac{2}{2n+3}.
\]
Consequently the first improving fraction is \(1-2/(2n+3)\to1\), whereas the **entire plateau** exceeds the social optimum by
\[
Kh+Lh^2=\frac{2n-1}{2n+3}\longrightarrow1.
\]
This proves that near-universal penetration by itself does not ensure even a small absolute improvement, when network coefficients are allowed to vary.

## Verification

The included `verification.py` uses only Python's standard library and exact rational arithmetic. Running `python3 verification.py` verifies both route-cost difference identities, the exact social-cost polynomial, the two equilibria's Wardrop inequalities at 71 rational penetration rates for a concrete instance, and the near-total-penetration family for 39 integers with five penetration values each. The mathematical proof, not this finite collection, establishes the continuum statement and asymptotic limit. A numerical or finite check alone is not a proof of uniqueness; the theorem explicitly invokes the established aggregate-uniqueness result.

For the rational example \((p,q,r,a,b,c)=(4,1,1,1/10,21/10,1/5)\), one has \(H=3/10\), \(K=6/5\), \(L=7/2\), \(h=3/35\), and plateau end \(\alpha=32/35\). Optimal travel cost is \(47/10\), and the excess on the plateau is exactly \(9/70\).

## Relationship to prior work

Yi and Wei (2026), *Routing Equilibrium in Mixed-Autonomy Traffic Networks with Altruistic Autonomous Agents*, introduce the exact simultaneous game used here, establish existence and aggregate uniqueness under polynomial edge delays, give sufficient welfare-effect conditions, and numerically observe plateaus for a **different**, six-edge modified Braess example. The present result uses their uniqueness theorem and does not claim it as new. Its contribution is the explicit all-penetration law for the standard five-edge Braess graph on an open parameter region and an extreme-fraction family with a quantitatively persistent welfare gap.

Wang, He, and Li (2026) prove social-delay plateaus for a **two-lane weaving-ramp Stackelberg–Wardrop** framework, rather than the present simultaneous three-route Braess game. Brown (2020) studies worst-case perversity for **series-parallel** networks, not this individual Braess instance; Hill and Brown (2024) characterize improvement guarantees for series-parallel/Braess-resistant networks. Classical Stackelberg routing thresholds characterize central control budgets for social optima; they do not automatically imply the displayed welfare curve for simultaneous altruists with a compulsory marginal-cost response.

## Limitations

The theorem concerns one origin–destination pair, nonatomic users, identical delays for human and autonomous traffic, fully marginal-cost altruism, strictly positive affine edge slopes, one particular five-edge topology, and the displayed strict parameter domain. It makes no claim about general networks, integer vehicle fleets, road-capacity constraints, dynamic rerouting, or uniqueness of individual-type path decompositions. The near-total-penetration example is nonuniform across networks: coefficients change with \(n\). Historical priority remains subject to independent inspection, especially possible reductions in general multiclass variational-inequality literature; no independent audit has been performed.

## References

1. L. Yi and E. Wei, *Routing Equilibrium in Mixed-Autonomy Traffic Networks with Altruistic Autonomous Agents*, arXiv:2605.23782v1 (22 May 2026), particularly Theorems 1–2, Appendix II, and Sections V–VI. https://arxiv.org/pdf/2605.23782
2. K. Wang, H. He, and R. Li, *When Altruism Meets Autonomy: Managing Bottleneck Congestion with Strategic Autonomous Vehicles*, arXiv:2604.21941v1 (12 April 2026), particularly Theorem 3 and Sections 6–7. https://arxiv.org/pdf/2604.21941
3. P. N. Brown, *Partial Altruism is Worse than Complete Selfishness in Nonatomic Congestion Games*, arXiv:2007.05591v1 (10 July 2020), particularly Sections 1–2. https://arxiv.org/pdf/2007.05591
4. C. Hill and P. N. Brown, *Altruism Improves Congestion in Series-Parallel Nonatomic Congestion Games*, arXiv:2404.07302v1 (10 April 2024), particularly introduction and network hypotheses. https://arxiv.org/pdf/2404.07302
