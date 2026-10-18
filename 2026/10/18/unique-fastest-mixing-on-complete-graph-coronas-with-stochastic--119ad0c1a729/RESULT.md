# Unique fastest mixing on complete-graph coronas with stochastic boundary saturation

## Finding
For every integer \(m\ge3\), form the graph \(G_m=K_m\circ K_1\) by attaching one private leaf to each vertex of a complete graph of order \(m\). Among **all** symmetric, entrywise nonnegative, row-stochastic \(2m\)-by-\(2m\) matrices supported on the edges and vertex loops of \(G_m\), the unique matrix minimizing the second-largest eigenvalue modulus is given by the following transition probabilities:

\[
D_m=5m^2-8m+4,\qquad s_m=\sqrt{m(m-1)},
\]
\[
p_m=\frac{m^2+(m-2)s_m}{D_m}\quad\text{(each core--leaf edge)},
\qquad q_m=\frac{1-p_m}{m-1}\quad\text{(each core--core edge)}.
\]
All core vertices have zero holding probability; each leaf holds with probability \(1-p_m\). The exact optimal eigenvalue modulus is
\[
\mu_m=\frac{2\bigl((m-2)(m-1)+m s_m\bigr)}{D_m}.
\]
Thus \(p_m\to2/5\), \(m q_m\to3/5\), and \(\mu_m\to4/5\) as \(m\to\infty\). The uniqueness assertion applies to **every feasible matrix**, including those without permutation symmetry.

## Assumptions and scope
Order the vertices as the \(m\) core vertices followed by their paired leaves. Self-loop probabilities may be zero. Every matrix \(P\) is real, symmetric, nonnegative entrywise, satisfies \(P\mathbf 1=\mathbf1\), and has off-diagonal zeros outside the \(m\) pendant edges and the \(\binom m2\) clique edges. The stationary measure is uniform. Write \(J=\mathbf1\mathbf1^{T}/(2m)\). The objective is \(\mu(P)=\lVert P-J\rVert_2\); this equals the maximum modulus of the eigenvalues other than the fixed eigenvalue \(1\), with multiplicities properly accounted for even at reducible boundary points.

## Proof
**1. Symmetry reduction.** Simultaneously permute the \(m\) core--leaf pairs. Conjugation leaves the feasible set and the convex objective \(\lVert P-J\rVert_2\) invariant. Averaging any feasible matrix over the permutations gives a feasible invariant matrix with no larger objective. Each invariant matrix has a pendant-edge probability \(p\ge0\), a core-edge probability \(q\ge0\), and constraints \(p+(m-1)q\le1\), \(p\le1\). Its block matrix is
\[
P(p,q)=\begin{pmatrix}(1-p-mq)I_m+q\mathbf1_m\mathbf1_m^T&pI_m\\pI_m&(1-p)I_m\end{pmatrix}.
\]
Its constant-core/constant-leaf block has eigenvalues \(1\) and \(1-2p\). Each of the other \(m-1\) orthogonal core directions contributes the two eigenvalues
\[
\lambda_\pm=1-p-\frac{mq}{2}\pm\sqrt{p^2+\frac{m^2q^2}{4}}.
\]
Since \(mq\le m(1-p)/(m-1)\le2(1-p)\), the sum \(\lambda_++\lambda_-=2(1-p)-mq\) is nonnegative and \(\lambda_+\ge |\lambda_-|\). Moreover \(\lambda_+\ge1-p\), and \(\lambda_+\ge 1-mq/2\ge p\). If \(p\le1/2\), the first inequality gives \(\lambda_+\ge1-2p\); if \(p\ge1/2\), the second gives \(\lambda_+\ge2p-1\). Therefore for **every** feasible invariant \((p,q)\),
\[\mu(P(p,q))=\lambda_+(p,q).\]
At \(p=0\) the objective is \(1\), whereas positive \(p,q\) give an irreducible aperiodic chain of objective below \(1\). For \(p>0\), \(\lambda_+\) is strictly decreasing in \(q\), since
\[
\frac{\partial\lambda_+}{\partial q}=-\frac m2+\frac{m^2q}{4\sqrt{p^2+m^2q^2/4}}<0.
\]
Consequently **every invariant minimizer** saturates the core row-sum constraint:
\[q=\frac{1-p}{m-1}.\]

**2. Exact scalar optimum.** Set \(c=m/[2(m-1)]\in(1/2,3/4]\), \(a=1-c\), and \(t=1-p\). Along the saturated boundary the objective is
\[
F(t)=at+\sqrt{(1-t)^2+c^2t^2},\qquad0\le t\le1.
\]
This is strictly convex: the vector \((1-t,ct)\) traces a segment not contained in any ray from the origin. Its derivatives at the endpoints are \(F'(0)=-c\) and \(F'(1)=1\); therefore there is a unique minimizer in \((0,1)\). Writing its value as \(\mu\), the equation \(F(t)=\mu\), after squaring, is
\[
0=(\mu-at)^2-((1-t)^2+c^2t^2)
  =(\mu^2-1)+2(1-a\mu)t-2ct^2.
\]
Tangency at the interior minimum forces \((1-a\mu)^2=2c(1-\mu^2)\), equivalently
\[
(1+c^2)\mu^2-2a\mu+(1-2c)=0.
\]
Its sole positive root is \(\mu=(a+\sqrt{2c^3})/(1+c^2)\); the other root is nonpositive because \(c>1/2\). The double-root position is \(t=(1-a\mu)/(2c)\). Elementary simplification yields the stated radical formulas for \(p_m=1-t\) and \(\mu_m\), and the saturated equation gives \(q_m\). These values lie in the strict feasible range \(0<p_m<1\), \(q_m>0\). This proves the globally optimal **value**, by Step 1, and uniqueness of the invariant minimizer.

**3. Global uniqueness, without imposing symmetry.** Let \(Q\) be any globally optimal feasible matrix. The permutation average of \(Q\) is invariant and optimal, hence equals the uniquely determined \(P^*=P(p_m,q_m)\). Let \(E=\{(u,ru):u\in\mathbb R^m,\ \mathbf1_m^Tu=0\}\), where
\[
r=\frac{p_m}{\mu_m-1+p_m}>1.
\]
The denominator is positive because \(\mu_m>1-p_m\), and \(r>1\) because \(\mu_m<1\). The transverse block in Step 1 shows that every vector in \(E\) is a \(\mu_m\)-eigenvector of \(P^*\). For each simultaneous core--leaf permutation \(\sigma\), the matrix
\[
\mu_m I-(\sigma Q\sigma^T-J)
\]
is positive semidefinite, because \(\lVert Q-J\rVert_2=\mu_m\). Their average is \(\mu_m I-(P^*-J)\), which annihilates all of \(E\). As an average of positive-semidefinite matrices can have a zero quadratic form only if each summand does, every \(v\in E\) also satisfies \(Qv=\mu_m v\).

Write \(p_i\) for the pendant probability incident to core \(i\). The leaf equation in \(Q(u,ru)=\mu_m(u,ru)\) is \(p_i u_i+(1-p_i)r u_i=\mu_m r u_i\). For each \(i\), choose \(u\perp\mathbf1_m\) with \(u_i\ne0\); this forces
\[
p_i=\frac{(1-\mu_m)r}{r-1}=p_m
\]
independently of \(i\). Let \(L\) be the weighted Laplacian of the arbitrary clique-edge probabilities in \(Q\). The core equations now force
\[
Lu=(1+p_m(r-1)-\mu_m)u\quad\text{for every }u\perp\mathbf1_m.
\]
Since \(L\mathbf1_m=0\), this implies \(L=d(I_m-\mathbf1_m\mathbf1_m^T/m)\) for some \(d\); every off-diagonal clique-edge probability therefore equals \(d/m\). Thus \(Q\) is invariant, so it equals \(P^*\). This proves uniqueness over the full feasible set.

## Verification
Run the included `verify.py` with Python 3, NumPy and SymPy. It independently verifies three symbolic identities underlying the radical formulas, constructs full \(2m\)-vertex transition matrices and compares their dense spectra with the theorem for each \(3\le m\le60\) (58 orders), and checks 400 additional nonsymmetric-weight but symmetric-matrix feasible random examples. The program reports `VERIFY_OK`. Finite tests do **not** prove an infinite-family claim; the analytical steps above do.

## Relationship to prior work
Boyd--Diaconis--Xiao (2004) formulated the entrywise-nonnegative fastest-mixing problem, and Boyd--Diaconis--Parrilo--Xiao (2009) established the symmetry reduction method. Neither inspected article supplies these corona-specific formulas and full-optimizer uniqueness. Jafarizadeh--Jamalipour (2010) treated **exactly the same graph** as a complete-cored symmetric star with one-edge branches, but optimized a signed distributed-consensus weight matrix without imposing entrywise nonnegativity. Its solution assigns \(1/2\) to pendant edges and \(1/m\) to core edges; when \(m\ge3\), the resulting core diagonal \(1/m-1/2\) is **negative** (equivalently \(1-1/2-(m-1)/m=1/m-1/2<0\)), so it does not solve the Markov-chain problem here. Jafarizadeh (2020, Section 7.4 and Appendix E) directly studies reversible fastest mixing on complete-cored symmetric stars but states its one-edge-branch formula under \((m-1)\pi_1\le\pi_0\). Under uniform vertex probabilities this condition fails for all \(m\ge3\); its alternative boundary formula addresses two-edge branches, not the one-edge case. The exact stochastic boundary and global uniqueness above address that uncovered parameter regime.

## Limitations
The statement assumes undirected equal-per-direction transitions, uniform stationary distribution, free vertex holding probabilities, and a **single** leaf per core vertex; it does not classify arbitrary stationary distributions, multiple leaves per core, or asymmetric Markov chains. The published-literature comparison cannot exclude an unindexed equivalent result. The analytical proof has not undergone an independent external audit.

## References
1. S. Boyd, P. Diaconis, L. Xiao, *Fastest Mixing Markov Chain on a Graph*, SIAM Review 46 (2004), 667--689. DOI: 10.1137/S0036144503423264. Public electronic publication: October 29, 2004.
2. S. Boyd, P. Diaconis, P. A. Parrilo, L. Xiao, *Fastest Mixing Markov Chain on Graphs with Symmetries*, SIAM J. Optimization 20 (2009), 792--819. DOI: 10.1137/070689413.
3. S. Jafarizadeh, A. Jamalipour, *Weight Optimization for Distributed Average Consensus Algorithm in Symmetric, CCS & KCS Star Networks*, arXiv:1001.4278 (first posted January 24, 2010), Section IV-B and constrained optimization formulation in Section III.
4. S. Jafarizadeh, *Fastest Mixing Reversible Markov Chain: Clique Lifted Graphs and Subgraphs*, IEEE Trans. Signal Inform. Process. Networks 6 (2020), 88--104, Section 7.4, Appendix E. DOI: 10.1109/TSIPN.2020.2964211; full-text arXiv:2501.02421.
