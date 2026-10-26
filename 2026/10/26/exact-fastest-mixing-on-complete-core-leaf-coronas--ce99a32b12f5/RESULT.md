# Exact fastest mixing on complete-core leaf coronas

## Finding

For an integer \(m\ge3\), let \(H_m=K_m\circ K_1\) be the graph formed by attaching a separate pendant leaf to every vertex of a complete graph \(K_m\). Among **all** symmetric, entrywise nonnegative, row-stochastic matrices \(P\) on its \(2m\) vertices with off-diagonal support contained in the edges of \(H_m\), the optimal second-largest eigenvalue modulus (SLEM) is
\[
\boxed{\mu_m^*=\frac{d+c\sqrt{2c}}{1+c^2}},\qquad
c=\frac{m}{2(m-1)},\quad d=1-c.
\]
An optimal matrix assigns the same leaf-edge transition probability and the same complete-core edge transition probability, respectively,
\[
\boxed{b_m=\frac{c+d\sqrt{2c}}{2+d\sqrt{2c}}},\qquad
\boxed{a_m=\frac{1-b_m}{m-1}}.
\]
Every core-vertex self-loop probability in this optimal matrix is zero, and each leaf self-loop probability is \(1-b_m\). This is the **unique** optimizer among matrices invariant under simultaneous permutations of the \(m\) core-leaf pairs. No uniqueness claim is made for all non-invariant matrices.

The optimal SLEM and the leaf-edge probability have nontrivial finite limits,
\[
\lim_{m\to\infty}\mu_m^*=\frac45,\qquad
\lim_{m\to\infty}b_m=\frac25.
\]
For comparison, both the maximum-degree and Metropolis edge-probability prescriptions give probability \(1/m\) on every edge of \(H_m\). Their exact SLEM is
\[
\mu_m^{\rm heur}=\frac12-\frac1m+\sqrt{\frac14+\frac1{m^2}},
\]
and their ratio of spectral gaps is unbounded:
\[
\boxed{\lim_{m\to\infty}\frac1m\frac{1-\mu_m^*}{1-\mu_m^{\rm heur}}=\frac15.}
\]
The member \(m=2\) is the four-vertex path; the same formulas give its known optimum \(1/\sqrt2\).

## Assumptions and scope

The chain has uniform stationary distribution, enforced by symmetry \(P=P^{\mathsf T}\). Self-loops are allowed; transitions between different vertices are allowed only on the edges of \(H_m\) and may be zero. The objective is the asymptotic \(\ell^2\) contraction \(\mu(P)=\|P-J_{2m}\|_2\), with \(J_{2m}=\mathbf1\mathbf1^{\mathsf T}/(2m)\). The theorem concerns discrete-time reversible chains, not continuous-time spectral-gap maximization or arbitrary nonuniform stationary distributions. The minimization is over *all* supported symmetric stochastic matrices, not only the symmetric two-parameter family.

## Proof

**1. Reduction is globally valid.** The finite automorphism group \(\mathfrak S_m\) permutes the \(m\) core-leaf pairs simultaneously. If \(P\) is feasible, then each relabeled \(U_g P U_g^{\mathsf T}\) is feasible and has the same objective because \(U_g J_{2m}U_g^{\mathsf T}=J_{2m}\). Convexity of the spectral norm shows that the group average is feasible with no greater objective. Thus at least one globally optimal chain is invariant. Invariant chains have a common transition probability \(a\) on every core edge and \(b\) on every leaf edge, with
\[
0\le b\le1,\qquad 0\le a\le\frac{1-b}{m-1}.
\]
Their core-vertex and leaf self-loop probabilities are \(1-(m-1)a-b\) and \(1-b\).

**2. Full invariant-chain spectrum.** Split the state space into core and leaf coordinates in matching order. The invariant transition matrix is
\[
P(a,b)=\begin{pmatrix}
(1-b-ma)I_m+a\mathbf1\mathbf1^{\mathsf T}&bI_m\\
bI_m&(1-b)I_m
\end{pmatrix}.
\]
On the two-dimensional subspace constant within each layer the eigenvalues are \(1\) and \(1-2b\). On each of the \(m-1\) orthogonal core-contrast/leaf-contrast pairs, the symmetric matrix is
\[
M(a,b)=\begin{pmatrix}1-b-ma&b\\b&1-b\end{pmatrix},
\]
with eigenvalues
\[
\lambda_{\pm}(a,b)=1-b-\frac{ma}{2}\pm\sqrt{b^2+\left(\frac{ma}{2}\right)^2}.
\]
Each has multiplicity \(m-1\). This decomposition accounts for all \(2m\) eigenvalues. The larger contrast eigenvalue is nonnegative, since \(\lambda_+(a,b)\ge1-b\ge0\), and is a lower bound for the SLEM.

**3. Sharp one-dimensional lower bound.** For fixed \(0<b<1\), the derivative of \(\lambda_+(a,b)\) with respect to \(a\) is strictly negative. Hence
\[
\mu(P(a,b))\ge\lambda_+(a,b)\ge f(b):=\lambda_+\left(\frac{1-b}{m-1},b\right).
\]
For \(b=0\) or \(b=1\), the chain has SLEM \(1\), so minimizers are interior. Set \(c=m/[2(m-1)]\), \(d=1-c\) and \(t=b/(1-b)\ge0\). Then
\[
f(b)=\frac{d+\sqrt{t^2+c^2}}{1+t}.
\]
The derivative with respect to \(t\) has the sign of
\[
g(t)=\frac{t-c^2}{\sqrt{t^2+c^2}}-d,
\qquad
g'(t)=\frac{c^2(1+t)}{(t^2+c^2)^{3/2}}>0.
\]
Because \(g(0)=-1\) and \(\lim_{t\to\infty}g(t)=c>0\), there is exactly one minimizer. Solving \(g(t)=0\) with its required sign yields
\[
t_*=\frac{c+d\sqrt{2c}}{2-c},\qquad
b_* =\frac{t_*}{1+t_*}=\frac{c+d\sqrt{2c}}{2+d\sqrt{2c}}.
\]
Writing \(s=f(b_*)\), the tangency condition is \(s=d+c\sqrt{1-s^2}\). Solving the resulting quadratic, and taking the root \(s>d\), gives
\[
s=\frac{d+c\sqrt{2c}}{1+c^2}=\mu_m^*.
\]

**4. The lower bound is attained without a negative-eigenvalue obstruction.** Choose \(a=a_m=(1-b_m)/(m-1)\) and \(b=b_m\). Since \(\sqrt{2c}<2\) and \(c+d=1\), the displayed formula gives \(0<b_m<1/2\) for \(m\ge3\). Then \(|1-2b_m|=1-2b_m\le1-b_m\le\lambda_+(a_m,b_m)\). Moreover,
\[
\lambda_+(a_m,b_m)+\lambda_-(a_m,b_m)
=2(1-b_m)-ma_m
=\frac{m-2}{m-1}(1-b_m)>0,
\]
so \(\lambda_+(a_m,b_m)\ge|\lambda_-(a_m,b_m)|\). Thus the achieved SLEM equals the lower bound \(f(b_m)=\mu_m^*\), proving global optimality after Step 1. Since the lower-bound minimizer \(b_m\) is unique and \(a\mapsto\lambda_+(a,b_m)\) is strictly decreasing, \((a_m,b_m)\) is the unique automorphism-invariant optimizer.

**5. Standard heuristics and asymptotics.** Every edge of \(H_m\) meets a core vertex of degree \(m\), so both the maximum-degree rule and the Metropolis rule assign \(a=b=1/m\). Here the larger contrast eigenvalue equals
\[
\lambda_+\left(\frac1m,\frac1m\right)
=\frac12-\frac1m+\sqrt{\frac14+\frac1{m^2}}.
\]
It dominates the other nontrivial eigenvalue magnitudes by the inequalities of Step 4 (with \(b\le1/2\)), giving the exact heuristic SLEM. Finally, \(c\to1/2\), \(d\to1/2\), so the closed forms yield \(b_m\to2/5\) and \(\mu_m^*\to4/5\). A rationalization or Taylor expansion gives \(1-\mu_m^{\rm heur}=1/m+O(m^{-2})\), proving the ratio limit.

## Verification

Run `python verify.py` with the packages specified in `requirements.txt`. The checker independently assembles the full transition matrices (without using the displayed spectral reduction to build them), verifies the full eigenvalue lists for \(2\le m\le16\), computes SLEM and stochasticity, and compares finite feasible competitors including nonsymmetric edge allocations. It also checks the maximum-degree formula, the four-vertex path boundary and large-\(m\) limits. The analytic proof above establishes the universal quantifiers; numerical experiments are not a substitute for that proof.

## Relationship to prior work

Boyd, Diaconis and Xiao introduced the globally convex fastest-mixing Markov-chain problem and compared its optimum with degree-based heuristics [1]. Boyd, Diaconis, Parrilo and Xiao developed automorphism reduction and exact results on several graph families [2]. The present calculation builds on their convexity principle but evaluates a different graph family, including its exact closed-form optimum for every \(m\ge3\) and the sharp asymptotic heuristic gap.

Jafarizadeh's study of complete-cored symmetric star (CCS star) networks explicitly includes a complete core with one private leaf per core vertex [3, Section 7.4 and Appendix E]. Its displayed simple optimal weights are subject to the hypothesis \((m-1)\pi_1\le\pi_0\). For equal stationary masses, that hypothesis reduces to \(m\le2\), whereas this theorem treats \(m\ge3\). The more general reduction to a path-related optimization in [3] provides important structural prior coverage; the present contribution is the explicit all-\(m\ge3\) boundary-regime solution and its exact asymptotic comparison with standard heuristics. The prior papers also already demonstrate unbounded heuristic spectral-gap ratios for other graph families: that qualitative phenomenon is not claimed as new.

## Limitations

The full set of optimal *non*-invariant matrices is not characterized; only the existence and uniqueness of an invariant optimum are proved. The formula applies to uniform equilibrium and one pendant leaf per complete-core vertex; unequal masses, longer arms, and other mixing metrics are outside the claim. Primary sources establish general FMMC methodology and a conditional CCS-star solution; independently reviewing their broader implicit algorithms could reveal an equivalent unstated algebraic specialization, so historical originality has a residual risk. No independent mathematical audit is represented here.

## References

[1] S. Boyd, P. Diaconis and L. Xiao, *Fastest Mixing Markov Chain on a Graph*, SIAM Review 46 (2004), 667–689. DOI: 10.1137/S0036144503423264. Author-hosted manuscript: https://web.stanford.edu/~boyd/papers/pdf/fmmc.pdf.

[2] S. Boyd, P. Diaconis, P. A. Parrilo and L. Xiao, *Fastest Mixing Markov Chain on Graphs with Symmetries*, arXiv:0709.0955v1 (first public version 2007-09-06), subsequently SIAM Journal on Optimization 20 (2009), 792–819. https://arxiv.org/abs/0709.0955.

[3] S. Jafarizadeh, *Fastest Mixing Reversible Markov Chain: Clique Lifted Graphs and Subgraphs*, IEEE Transactions on Signal and Information Processing over Networks 6 (2020), 88–104, DOI: 10.1109/TSIPN.2020.2964211; accessible author version https://arxiv.org/abs/2501.02421, Section 7.4 and Appendix E.
