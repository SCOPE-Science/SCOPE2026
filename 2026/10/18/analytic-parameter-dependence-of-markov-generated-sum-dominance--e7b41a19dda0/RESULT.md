# Analytic parameter dependence of Markov-generated sum-dominance probabilities

## Finding
Let \(0<p,q<1\). In the stationary two-state Markov model with transition matrix
\[
P(p,q)=\begin{pmatrix}p&1-p\\1-q&q\end{pmatrix},
\]
write \(A_n=\{i\in\{0,\ldots,n\}:X_i=1\}\). Let \(\rho_+(p,q)\), \(\rho_-(p,q)\), and \(\rho_0(p,q)\) be the limiting probabilities, as \(n\to\infty\), of \(\lvert A_n+A_n\rvert-\lvert A_n-A_n\rvert\) being positive, negative, and zero, respectively.

**Theorem.** Each of the three functions \(\rho_+\), \(\rho_-\), and \(\rho_0\) is real analytic on the entire open square \((0,1)^2\). More precisely, near every \((p_0,q_0)\in(0,1)^2\), all three admit jointly holomorphic extensions that are limits of explicit rational functions \(F_K^\star(p,q)\), with locally uniform geometric convergence. On every compact subpolydisc of a sufficiently small complex neighborhood and for every fixed pair of nonnegative integers \((a,b)\), the mixed derivatives \(\partial_p^a\partial_q^b F_K^\star\) converge geometrically to the corresponding derivatives of the extension. The rational approximants are defined explicitly below.

## Assumptions and scope
All integer sets below are finite subsets of nonnegative integers. Sumsets and difference sets use \(S+T=\{s+t:s\in S,t\in T\}\) and \(S-T=\{s-t:s\in S,t\in T\}\); empty sets have empty sumsets. The chain starts in its stationary distribution
\[
\pi(p,q)=\left(\frac{1-q}{2-p-q},\frac{1-p}{2-p-q}\right).
\]
For every integer \(K\ge0\), let \(L\) and \(R\) be **independent** stationary copies of the chain, each observed at indices \(0,\ldots,K\). Regard \(L_K=\{i\le K:L_i=1\}\) and \(R_K=\{i\le K:R_i=1\}\) as random sets, and put
\[
\Delta_K=\bigl\lvert(L_K+L_K)\cap[0,K]\bigr\rvert+\bigl\lvert(R_K+R_K)\cap[0,K]\bigr\rvert-2\bigl\lvert(L_K+R_K)\cap[0,K]\bigr\rvert.
\]
For \(\star\in\{>,<,=\}\), define \(F_K^\star(p,q)=\Pr_{p,q}(\Delta_K\,\star\,0)\). The result concerns **fixed interior transition parameters**, not a regime in which parameters move toward the boundary with \(K\) or \(n\). The external source proves existence of the three limits; their identification with these fringe probabilities is recalled below.

An explicit finite formula uses binary strings \(u,v\in\{0,1\}^{K+1}\). Define
\[
W_K(u;p,q)=\pi_{u_0}(p,q)\prod_{i=0}^{K-1}P_{u_i,u_{i+1}}(p,q),
\qquad
F_K^\star(p,q)=\sum_{u,v\in\{0,1\}^{K+1}}W_K(u;p,q)W_K(v;p,q)\,\mathbf 1\{\Delta_K(u,v)\,\star\,0\}.
\]
Thus every \(F_K^\star\) is rational in \(p,q\), with possible denominator powers only of \(2-p-q\), and is holomorphic near each interior real parameter point.

## Proof
**1. Identification of the limiting probabilities.** The stationary binary chain has spectral second eigenvalue \(p+q-1\), whose modulus is strictly below one. Two endpoint blocks at a separation tending to infinity therefore converge in law to independent stationary blocks. For a finite set \(A_n\), the difference \(\lvert A_n+A_n\rvert-\lvert A_n-A_n\rvert\) equals the finite fringe score \(\Delta_K\) whenever every sum and difference outside the two length-\(K\) endpoint fringes occurs. The latter full-middle event has probability at least \(1-C(p,q)\theta(p,q)^K\), uniformly for \(n>2K\), by positive-transition conditional bounds and disjoint sum/difference representations (He--Daniewski--Miller, Lemmas 2.3--2.4). Consequently, letting \(n\to\infty\) first and \(K\to\infty\) afterward gives
\[
\rho_\star(p,q)=\lim_{K\to\infty}F_K^\star(p,q)
\quad(\star\in\{>,<,=\}).
\]
The same conclusion follows directly by the uniform estimate between finite-sample probabilities and \(F_K^\star\), together with the Markov mixing limit. This step only identifies an already-defined arithmetic density; the analyticity is established independently below.

**2. A uniform two-coordinate finite-energy bound.** Fix an interior base point \(z_0=(p_0,q_0)\). Every transition probability and both stationary probabilities are strictly positive. Put \(m>0\) equal to their minimum, and take \(\delta=m^8/8\). For either one or two distinct coordinates in one finite stationary chain, conditioning on **all other** coordinates leaves at most four assignments. The relative conditional weights involve at most four transition factors and, at the initial coordinate, one stationary factor; each nontrivial factor lies in \([m,1]\). The specified all-one assignment therefore has conditional probability at least \(\delta\), uniformly in the length, indices, and conditioning. The same conservative lower bound works when one coordinate comes from each of two independent stationary chains. This is a finite-state local positivity argument, not an independence assumption between adjacent states.

**3. Exponentially rare changes of the fringe score.** For every \(K\ge1\), its increment is exactly
\[
\Delta_K-\Delta_{K-1}
=\mathbf1\{K\in L_K+L_K\}+\mathbf1\{K\in R_K+R_K\}-2\mathbf1\{K\in L_K+R_K\}.
\]
If each of these three sums is represented, the increment vanishes. For the first two sums, the pairs \((0,K),(1,K-1),\ldots\) with distinct endpoints give \(r_K=\lfloor(K+1)/2\rfloor\) disjoint two-coordinate representations; any central diagonal representation may be discarded. For the cross sum, the pairs \((L_i,R_{K-i})\) provide at least \(r_K\) disjoint representations across the two chains. Exposing the failure events sequentially and using the finite-energy lower bound of Step 2 gives, for each sum, a missing probability at most \((1-\delta)^{r_K}\). Hence, at the fixed real base point,
\[
\Pr_{z_0}(\Delta_K\ne\Delta_{K-1})\le3(1-\delta)^{r_K}.
\]
The conclusion is uniform over all sign comparisons: \(\mathbf1\{\Delta_K\,\star\,0\}-\mathbf1\{\Delta_{K-1}\,\star\,0\}\) can be nonzero only when the score changes. In particular, each \(F_K^\star(z_0)\) converges geometrically; this independently verifies the convergence of the finite-fringe scheme.

**4. Complexification, rather than merely real uniform convergence.** Write \(z=(p,q)\in\mathbb C^2\). Choose a sufficiently small closed complex polydisc \(D\) about \(z_0\) avoiding \(2-p-q=0\). Since all entries of \(P(z_0)\) and \(\pi(z_0)\) are positive, for any preassigned \(\varepsilon>0\) we may shrink \(D\) until
\[
\left\lvert\frac{P_{ij}(z)}{P_{ij}(z_0)}\right\rvert\le e^\varepsilon,
\qquad
\left\lvert\frac{\pi_i(z)}{\pi_i(z_0)}\right\rvert\le2
\quad(z\in D).
\]
For two length-\((K+1)\) paths the modulus of their joint complex weight is therefore at most \(4e^{2\varepsilon K}\) times its positive weight at \(z_0\). Marginalizing the last coordinate gives precisely the length-\(K\) path weights, **also for complex** \(z\), because the rows of \(P(z)\) sum to one. Thus, after writing \(F_K^\star-F_{K-1}^\star\) over the same length-\((K+1)\) path pairs, every surviving summand corresponds to a score change. Step 3 gives the genuine complex-mass bound
\[
\sup_{z\in D}\lvert F_K^\star(z)-F_{K-1}^\star(z)\rvert
\le 12e^{2\varepsilon K}(1-\delta)^{\lfloor(K+1)/2\rfloor}.
\]
Take \(\varepsilon< -\frac14\log(1-\delta)\); then the right side is summable in \(K\). Hence
\[
F_0^\star(z)+\sum_{K=1}^{\infty}\bigl(F_K^\star(z)-F_{K-1}^\star(z)\bigr)
\]
converges normally on \(D\) to a holomorphic function. For real parameters it equals \(\rho_\star\) by Step 1. As the base point was arbitrary, all three limiting probabilities are jointly real analytic throughout \((0,1)^2\).

**5. Derivatives and geometric approximations.** The preceding estimate controls the holomorphic tail geometrically on \(D\). Cauchy's integral formula on a smaller polydisc then bounds the error in every fixed mixed partial derivative by \(C_{a,b}\vartheta^K\) for some \(0<\vartheta<1\), uniformly on compact subsets of that smaller polydisc. Finite approximants and their derivatives are rational and can be obtained directly from the displayed binary-string formula. No positivity, monotonicity, or maximizer of any derivative is asserted.

## Verification
Run `python verify.py` with Python 3 (standard library only). It enumerates exact rational probabilities \(F_K^\star\) for three interior transition pairs and \(0\le K\le5\), plus \(K=6\) for the symmetric pair. For every one of the enumerated \(2^{2(K+1)}\) fringe configurations it checks that a change in \(\Delta_K\) requires one of the three new sums to be missing. It separately checks the full-middle/fringe-score identity exhaustively for \((n,K)=(8,2),(10,3),(12,4)\). The recorded output is in `CHECKS.txt`.

These finite tests do not establish analyticity. The infinite quantifiers and complex-uniform bounds are proved in Steps 2--5. The verifier has no external data or packages.

## Relationship to prior work
He, Daniewski and Miller (arXiv:2610.08394v1, first posted 2026-10-06) introduce exactly this stationary two-state Markov model and prove existence and strict positivity of the three limiting probabilities (Theorem 1.7, Proposition 2.5). Their paper studies a rational formula for the limiting **expected** cardinality gap, which is a different function from the three event probabilities, and proposes that \(\rho_+\) is maximized at \(p=q=1/2\). It does not establish parameter analyticity or convergence of derivatives for these event probabilities.

Do, Kulkarni, Miller, Moon and Wellens (arXiv:1401.2588v1; Journal of Number Theory 147 (2015), 44--68) prove continuity of a limiting probability for a **different**, independently indexed correlated-pair model; their conclusion explicitly raises further analytic properties as a question. Zhao (arXiv:0911.2292) proves limiting probabilities and a deterministic approximation scheme in the **uniform** single-set model. Iyer, Lazarev, Miller and Zhang (arXiv:1107.2719) survey and extend earlier finite/fringe constructions. None of these results gives the joint analytic dependence on the transition probabilities of a stationary Markov-generated single set. The new mechanism is a complex-uniform bound on differences of finite fringe probabilities, obtained by combining local finite energy with a complex likelihood-ratio estimate.

## Limitations
The result is an interior regularity theorem: it gives no analytic extension to edges or corners of the parameter square, no resolution of the proposed maximizer, and no polynomial-time numerical algorithm. The geometric constants may deteriorate sharply near the boundary. The finite experiment is evidence for finite algebraic identities only. A broader abstract theorem for analyticity of parametric rare-event functionals, or unindexed prior work on this precise Markov MSTD model, could subsume this conclusion; no such coverage was identified in the inspected primary literature. Independent validation has not been performed.

## References
1. F. He, K. Daniewski, S. J. Miller, *Generating and generalizing MSTD sets through Markov processes*, arXiv:2610.08394v1, first posted 2026-10-06; §§1--5, especially Lemmas 2.3--2.4, Proposition 2.5, and Conjecture 5.1.
2. T. Do, A. Kulkarni, S. J. Miller, D. Moon, J. Wellens, *Sums and differences of correlated random sets*, arXiv:1401.2588v1; J. Number Theory 147 (2015), 44--68; §§2--3, 6.
3. Y. Zhao, *Sets characterized by missing sums and differences*, arXiv:0911.2292; J. Number Theory 131 (2011), 2107--2134; §§1--3, 6.
4. G. Iyer, O. Lazarev, S. J. Miller, L. Zhang, *Finding and Counting MSTD sets*, arXiv:1107.2719; §§1--3.
