# Exact Nash equilibrium classification for complete multipartite public-goods opinion games

## Finding
In the coevolutionary public-goods game of Davidson, Zino, Cao and Ye, uniform agent parameters and a common (possibly nonzero) prejudice imply an exact classification of **all** Nash equilibria on an unweighted complete multipartite social graph. A non-unanimous action profile is Nash only when each part has the same fraction of cooperators and **every** player is indifferent between cooperation and defection. Such profiles exist only at one explicitly determined parameter equality; their number is a binomial product governed by the greatest common divisor of the part sizes. In particular, if that greatest common divisor is one, no non-unanimous Nash equilibrium exists for any admissible parameters. Under the deterministic tie-to-defect selection convention, no non-unanimous fixed point exists even when the equality holds.

## Assumptions and scope
Fix an integer \(q\ge2\), positive part sizes \(n_1,\dots,n_q\), and \(n=\sum_{a=1}^q n_a\). The influence graph is the unweighted complete \(q\)-partite graph. Each agent averages the opinions of all neighbors, so \(W_{ij}=1/(n-n_a)\) if agent \(i\) belongs to part \(a\) and \(j\) belongs to another part; otherwise \(W_{ij}=0\). Thus \(W\) has no self loops. Agent \(i\) selects a binary action \(x_i\in\{0,1\}\) and an opinion \(y_i\in[0,1]\). All agents share \(\alpha,\beta,\lambda>0\), \(\alpha+\beta+\lambda=1\), prejudice intensity \(0\le\gamma<1\), and prejudice value \(u\in[0,1]\). The public-goods multiplier satisfies \(1<r<n\). This is the common-parameter, loopless specialization of equations (2)–(4) of Davidson et al. (2026).

An agent's payoff is \(\alpha\) times its public-goods reward, minus \(\frac{\beta}{2}(1-\gamma)\sum_jW_{ij}(y_i-y_j)^2\), minus \(\frac{\beta\gamma}{2}(y_i-u)^2\), minus \(\frac{\lambda}{2}(x_i-y_i)^2\). Holding others fixed, the public-goods payoff difference (cooperate minus defect) is \(r/n-1\). Nash equilibrium means an optimal **joint action/opinion** response for every agent, allowing both actions at an exact payoff tie.

Define \(\kappa=\beta\lambda/(\beta+\lambda)\) and, for \(p\in[0,1]\),
\[
 m(p)=\frac{\beta\gamma u+\lambda p}{\beta\gamma+\lambda},\qquad
 F(p)=-\alpha(1-r/n)+\kappa\bigl((1-\gamma)m(p)+\gamma u-\tfrac12\bigr).
\]
Let \(g=\gcd(n_1,\dots,n_q)\). All Nash equilibria are precisely:

1. All defectors, with \(x_i=0\) and \(y_i=m(0)\), if and only if \(F(0)\le0\).
2. All cooperators, with \(x_i=1\) and \(y_i=m(1)\), if and only if \(F(1)\ge0\).
3. For an integer \(j\in\{1,\dots,g-1\}\) satisfying \(F(j/g)=0\), every profile with exactly \(j n_a/g\) cooperators in each part, and opinions
\[
 y_i=m(j/g)+\frac{\lambda}{\beta+\lambda}\bigl(x_i-j/g\bigr).
\]
There are exactly \(\prod_{a=1}^q\binom{n_a}{j n_a/g}\) such non-unanimous equilibria. Since \(F'(p)=\kappa(1-\gamma)\lambda/(\beta\gamma+\lambda)>0\), at most one value of \(j\) qualifies. Any such value coexists with both unanimous Nash equilibria. No other equilibria exist.

## Proof
**Joint best responses.** Since there are no self loops, other opinions are fixed when an agent optimizes its own opinion. Write \(M_i=\sum_jW_{ij}y_j\). For fixed action \(s\in\{0,1\}\), strict quadratic concavity gives the unique optimal opinion
\[
 y_i^{(s)}=\frac{\beta(1-\gamma)M_i+\beta\gamma u+\lambda s}{\beta+\lambda}.
\]
Substitution in the full payoff, including the constant-marginal public-goods term, yields the optimal cooperation-minus-defection payoff
\[
 \Delta_i=-\alpha(1-r/n)+\kappa\bigl((1-\gamma)M_i+\gamma u-\tfrac12\bigr).
\]
Thus Nash requires \(\Delta_i\ge0\) where \(x_i=1\), and \(\Delta_i\le0\) where \(x_i=0\), with ties permitted.

**Unique opinion vector for each action vector.** Put \(t=\beta(1-\gamma)/(\beta+\lambda)\), \(a=\beta\gamma/(\beta+\lambda)\), and \(h=\lambda/(\beta+\lambda)\). Note \(0\le t<1\) and \(a+t+h=1\). At any equilibrium,
\[
 (I-tW)y=a u\mathbf1+h x.
\]
The inverse exists by the convergent Neumann series since \(W\) is stochastic and \(t<1\). Its inverse preserves the opinion cube because the original fixed-point map is a convex combination. Consequently every binary \(x\) determines a unique feasible candidate \(y\).

**The nonpositive transverse spectrum.** Let \(A\) be the graph adjacency matrix and \(D\) its positive degree diagonal. Then \(W=D^{-1}A\) is reversible under \(\pi_i=D_{ii}/\sum_jD_{jj}\), and is similar to the symmetric matrix \(D^{-1/2}AD^{-1/2}\). The complete multipartite identity \(A=\mathbf1\mathbf1^{\mathsf T}-\sum_{a=1}^q\mathbf1_a\mathbf1_a^{\mathsf T}\) shows that \(A\), hence the similar symmetric matrix by congruence, has at most one positive eigenvalue: outside the hyperplane orthogonal to \(\mathbf1\), its quadratic form is nonpositive. Connectivity makes the simple Perron eigenvalue of \(W\) equal to one. Thus **all other eigenvalues of \(W\) are nonpositive**.

**A spectral sign contradiction unless all players tie.** Suppose \(x\) is neither all zero nor all one. Set \(p=\sum_i\pi_i x_i\in(0,1)\), \(x_c=x-p\mathbf1\). In the weighted inner product \(\langle v,w\rangle_\pi=\sum_i\pi_i v_iw_i\), stationarity gives
\[
 \big\langle x_c,Wy\big\rangle_\pi
 =h\big\langle x_c,W(I-tW)^{-1}x_c\big\rangle_\pi
 =h\sum_{k\ge2}\frac{\mu_k}{1-t\mu_k}c_k^2\le0,
\]
where \(\mu_k\le0\) are the nonprincipal eigenvalues and \(c_k\) are coordinates in a weighted orthonormal eigenbasis. On the other hand, because the coefficient \(\kappa(1-\gamma)>0\), the Nash inequalities imply
\[
 \kappa(1-\gamma)\langle x_c,Wy\rangle_\pi
 =\sum_{i:x_i=1}\pi_i(1-p)\Delta_i
   -\sum_{i:x_i=0}\pi_i p\Delta_i\ge0.
\]
Hence both sides vanish. Every displayed term on the right is nonnegative, so \(\Delta_i=0\) for **every** agent. Equality in the eigenvalue sum forces \(x_c\) to lie in the zero eigenspace of \(W\); therefore \(Wx=p\mathbf1\).

**Graph combinatorics and sufficiency.** Let \(k_a\) be the number of cooperators in part \(a\), and \(k=\sum_a k_a\). For a vertex in part \(a\), the equation \(Wx=p\mathbf1\) says \((k-k_a)/(n-n_a)=p\). Summing these relations over the \(q\) parts gives \(k=pn\), then \(k_a=pn_a\) for every \(a\). Thus \(p=j/g\) with an integer \(0<j<g\). Conversely these equal part fractions imply \(Wx=p\mathbf1\).

For such \(x\), the unique opinion solution is \(y=m(p)\mathbf1+h(x-p\mathbf1)\), and every neighbor average equals \(m(p)\). All discriminants equal \(F(p)\), so this mixed profile is Nash exactly when \(F(p)=0\). The binomial product counts its labeled configurations. The derivative of \(F\) is strictly positive, so at most one positive interior fraction qualifies, and its existence forces \(F(0)<0<F(1)\). For unanimous actions the same inverse calculation gives \(y=m(0)\mathbf1\) and \(y=m(1)\mathbf1\); the relevant unilateral inequalities are exactly \(F(0)\le0\) and \(F(1)\ge0\). This proves completeness.

**Tie-to-defect dynamics.** In each non-unanimous Nash profile just classified, every \(\Delta_i=0\). Under the deterministic revision rule choosing defection at equality, a cooperator would change action when activated. Hence no such profile is a fixed point of that selected revision rule. This distinction does not deny that the unselected game has these Nash equilibria.

## Verification
The self-contained `verify.py` uses standard-library rational arithmetic, solves the opinion equations exactly, and independently evaluates optimized unilateral payoffs (not only the stated discriminant formula). It exhaustively compared the predicted classification with direct Nash checks on 1,416 binary action profiles over ten complete multipartite part-size patterns and four rational parameter families.

For the graph \(K_{2,2}\), take \(\alpha=1/7\), \(\beta=\lambda=3/7\), \(\gamma=1/2\), \(u=1\), and \(r=2\). Here \(F(1/2)=0\). Exactly six Nash equilibria exist: the two unanimous profiles and four balanced profiles with one cooperator in each part. At every mixed equilibrium cooperators have opinion \(11/12\), defectors have opinion \(5/12\), and every player's payoff difference vanishes exactly. The exhaustive checks do not substitute for the general spectral proof.

## Relationship to prior work
Davidson, Zino, Cao and Ye (2026, arXiv:2604.08840v1) introduced the particular public-goods/opinion payoff, derived individual best responses and sufficient unanimous-equilibrium conditions, and explicitly left mixed-cooperation equilibria and positive-prejudice extensions for later investigation. The present claim is an exact complete equilibrium classification on **loopless complete multipartite social networks** with uniform parameters and common prejudice. It is not a claim that their general best-response expression is new.

Dehghani Aghbolagh and colleagues (2023, arXiv:2206.07242v2) established polarized equilibria in a different coevolutionary model with **network coordination** action payoffs and two interaction layers; their sufficient partition-cohesion conditions do not imply the sign obstruction for the constant-marginal public-goods game. The fact that a complete multipartite adjacency matrix has one positive eigenvalue is classical; it is used here as a premise, not claimed as novel. The coupling of this spectral fact to the Nash-sign inequalities and the complete greatest-common-divisor enumeration constitutes the proposed addition.

## Limitations
The classification requires homogeneous action/opinion parameters, common prejudice, loopless unweighted complete multipartite influence, and binary actions. It need not hold for heterogeneous prejudices, arbitrary weights, other graph classes, or nonlinear public-goods payoffs. The proof treats static Nash equilibria and deterministic tie-to-defect fixed points, not global convergence from arbitrary initial conditions. It makes no assertion that non-multipartite graphs must admit mixed equilibria. Historic priority outside the inspected literature, including generalized monotone threshold-network results, remains open to independent assessment.

## References
- E. C. Davidson, L. Zino, M. Cao, M. Ye, *Modelling the coevolution of opinion dynamics and decision making in social dilemmas*, arXiv:2604.08840v1 (first publicly posted 2026-04-10). https://arxiv.org/abs/2604.08840
- H. Dehghani Aghbolagh, M. Ye, L. Zino, Z. Chen, M. Cao, *Coevolutionary Dynamics of Actions and Opinions in Social Networks*, IEEE Transactions on Automatic Control 68 (2023), 7708–7723; arXiv:2206.07242v2. https://arxiv.org/abs/2206.07242
- C. Delorme, *Eigenvalues of complete multipartite graphs*, Discrete Mathematics (2012), DOI:10.1016/j.disc.2011.07.018. https://doi.org/10.1016/j.disc.2011.07.018
