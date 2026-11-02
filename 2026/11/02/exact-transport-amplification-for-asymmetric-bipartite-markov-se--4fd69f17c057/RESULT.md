# Exact transport amplification for asymmetric bipartite Markov semigroups

## Finding
Let \(K_{m,n}\) be a complete bipartite graph with \(m,n\ge 2\). Equip its vertices with shortest-path distance \(d\). From a vertex in the first part, a continuous-time chain jumps at total rate \(\alpha>0\) to a uniformly chosen vertex in the second part; from the second part it jumps at total rate \(\beta>0\) to a uniform vertex in the first. Write \(H_t=\exp(tQ)\) for its Markov semigroup and define its exact Wasserstein-one amplification
\[
 C(t)=\sup_{\mu\ne\nu}\frac{W_1(\mu H_t,\nu H_t)}{W_1(\mu,\nu)}\qquad(t\ge0).
\]
Then, for every choice of the integers, rates, and time,
\[
\boxed{C(t)=\max\left\{\frac{2(m-1)}{m}e^{-\alpha t}-\frac{m-2}{m}e^{-(\alpha+\beta)t},\quad
\frac{2(n-1)}{n}e^{-\beta t}-\frac{n-2}{n}e^{-(\alpha+\beta)t}\right\}.}
\]
In particular, the exact infinitesimal coarse Wasserstein curvature is
\[
\boxed{\kappa=-C'_+(0)=\min\left\{\alpha-\frac{m-2}{m}\beta,\ \beta-\frac{n-2}{n}\alpha\right\}.}
\]
The semigroup is nonexpansive in \(W_1\) for **all** \(t\ge0\) if and only if
\[
 \alpha\ge\frac{m-2}{m}\beta\quad\text{and}\quad\beta\ge\frac{n-2}{n}\alpha.
\]
If either inequality fails, its norm exceeds one for sufficiently small positive times, attains a **unique global maximum greater than one**, and decays to zero at long times. For example, \(m=n=4\), \(\alpha=1\), and \(\beta=4\) give an amplification maximum of approximately \(1.056134084152072\) at time \(\log(5/3)/4\), although the chain is irreducible and reversible.

More explicitly, put \(p_k=2(k-1)/k\) and \(q_k=(k-2)/k\). If \(\alpha<q_m\beta\), the unique peak is at
\[
 t_*=\frac1\beta\log\!\left(\frac{q_m(\alpha+\beta)}{p_m\alpha}\right),\qquad
 C(t_*)=\frac{p_m\beta}{\alpha+\beta}
 \left(\frac{p_m\alpha}{q_m(\alpha+\beta)}\right)^{\!\alpha/\beta}.
\]
If \(\beta<q_n\alpha\), interchange the two parts and rates. The two failures cannot coexist.

## Assumptions and scope
All measures are real signed measures on the finite vertex set when extended linearly, and \(W_1\) refers to the standard transportation cost with unit length on every edge. Probability measures have mass one. Same-part distinct vertices have distance two. The generator acts on functions by
\[
 (Qf)(x)=\alpha\left(\frac1n\sum_{y\in Y}f(y)-f(x)\right)\ (x\in X),\qquad
 (Qf)(y)=\beta\left(\frac1m\sum_{x\in X}f(x)-f(y)\right)\ (y\in Y).
\]
The chain is reversible with stationary mass \(\beta/(\alpha+\beta)\) on \(X\) and \(\alpha/(\alpha+\beta)\) on \(Y\), distributed uniformly within each part. Its nonconstant generator eigenvalues are \(-\alpha\), \(-\beta\), and \(-\alpha-\beta\), with multiplicities \(m-1\), \(n-1\), and one respectively.

## Proof
**Reduction to Dirac pairs.** On every finite metric space, the Kantorovich–Rubinstein norm of a zero-total-mass vector \(\sigma\) can be expressed as the minimum cost of decomposing it into elementary transports \(\delta_u-\delta_v\). A linear map preserving total mass thus has Wasserstein norm bounded by
\[
 \max_{u\ne v}\frac{\|H_t^*(\delta_u-\delta_v)\|_{W_1}}{d(u,v)},
\]
while each Dirac pair is an admissible lower-bound test. Thus this maximum is **exact**. Equivalently, use the dual characterization of the Lipschitz seminorm and its edge constraints.

**Three eigenspaces.** Write \(U_X\) and \(U_Y\) for the two uniform probability measures. Within each part, fluctuations \(\delta_x-U_X\) and \(\delta_y-U_Y\) evolve by scalar factors \(a=e^{-\alpha t}\) and \(c=e^{-\beta t}\), while the part imbalance \(U_X-U_Y\) evolves by \(b=e^{-(\alpha+\beta)t}=ac\). Therefore, for a cross-edge \(x\in X\), \(y\in Y\),
\[
 H_t^*(\delta_x-\delta_y)=a(\delta_x-U_X)-c(\delta_y-U_Y)+b(U_X-U_Y).
\]
Because \(0\le b\le a,c\le1\), this signed measure has positive mass \(S+b\) at \(x\), negative total mass \(S\) over the other \(m-1\) vertices of \(X\), negative mass \(T+b\) at \(y\), and positive total mass \(T\) over the other \(n-1\) vertices of \(Y\), where
\[
 S=\frac{m-1}{m}(a-b),\qquad T=\frac{n-1}{n}(c-b).
\]
**Exact transport cost.** If \(S\ge T\), send \(T+b\) units from \(x\) to \(y\) across an edge, send \(T\) from the other vertices of \(Y\) to the other vertices of \(X\) across edges, and send the remaining \(S-T\) within \(X\) at distance two. The cost equals \(b+2S\). The dual Lipschitz potential taking values \(2\) at \(x\), \(0\) on the other vertices of \(X\), and \(1\) on all of \(Y\) gives exactly \(b+2S\), so this cost is optimal. If \(T\ge S\), the symmetric plan and a potential taking values \(0\) at \(y\), \(2\) on the other vertices of \(Y\), and \(1\) throughout \(X\) give optimal cost \(b+2T\). Consequently
\[
 W_1(H_t^*\delta_x,H_t^*\delta_y)=\max\{b+2S,b+2T\}
 =\max\{p_m a-q_m b,p_n c-q_n b\}.
\]
For two distinct starting vertices of \(X\), the difference is simply \(a(\delta_x-\delta_{x'})\), so its Wasserstein ratio is \(a\); the analogous ratio in \(Y\) is \(c\). But \(p_m a-q_m b-a=q_m(a-b)\ge0\) and \(p_n c-q_n b-c=q_n(c-b)\ge0\). Thus the cross-edge ratio already dominates every same-part ratio. The claimed global norm formula follows.

**The sharp rate transition.** Let \(A_m(t)=p_m e^{-\alpha t}-q_m e^{-(\alpha+\beta)t}\) and define \(A_n\) by switching \(m,\alpha\) with \(n,\beta\). Both equal one at time zero. Their right derivatives there are \(-\alpha+q_m\beta\) and \(-\beta+q_n\alpha\), so taking the right derivative of their maximum gives the stated curvature. Moreover,
\[
 A_m'(t)=e^{-\alpha t}\left[-p_m\alpha+q_m(\alpha+\beta)e^{-\beta t}\right].
\]
The bracket is nonincreasing (strictly decreasing when \(m>2\)). Accordingly \(A_m\) is decreasing for all time exactly when \(\alpha\ge q_m\beta\); otherwise its derivative changes sign exactly once, at the displayed \(t_*\). The same applies to \(A_n\). Since \(q_mq_n<1\), the inequalities \(\alpha<q_m\beta\) and \(\beta<q_n\alpha\) cannot both hold. Hence in the expansive case one branch has a unique peak above one and the other branch is strictly decreasing from one, making that peak the unique global maximum. Substitution into the critical-point equation gives its exact magnitude. In the remaining case both branches decrease from one and so their maximum never exceeds one. Positivity of \(\alpha,\beta\) implies both branches vanish at infinity.

## Verification
The independent numerical reproduction script `verify.py` constructs the full generator and its matrix exponential, computes every pairwise Wasserstein distance by a standalone linear-program dual, and compares the maximum with the formula. Its specified suite comprises 60 size/rate/time combinations, together with tests of the peak and the contractivity boundary. The checks passed locally. These are finite numerical diagnostics only; the proof above is analytic for every admissible integer, positive real rate, and time.

## Relationship to prior work
The Kantorovich–Rubinstein duality and Dirac-pair reduction are classical; no novelty is claimed for them. The correspondence between graph coarse Ricci curvature and exponential heat-flow Lipschitz bounds is developed by Münch and Wojciechowski (2017 preprint, Theorem 3.8), and Pedrotti (2023 preprint, Section 5) develops continuous-time Markov-chain coupling and Wasserstein curvature methods. These works give general curvature estimates and semigroup contraction frameworks. The statement here is an exact **all-time, two-rate** transport norm for complete bipartite chains, including its parameter-sharp temporary expansion, maximizing time, and peak amplification. General curvature bounds alone do not determine that exact nonexponential function, and no equivalent calculation was located in the material inspected. This is a best-knowledge originality assessment, not a priority certification.

## Limitations
The result is specific to homogeneous rates within each part, strictly positive rates, at least two vertices per part, and the unweighted complete bipartite graph metric. It does not classify arbitrary rates on edges, larger multipartite graphs, or transport distances \(W_p\) for \(p\ne1\). The all-time formula is established analytically, while the finite computational checks are supplementary. Equivalent historical formulas under other normalizations or older coupling terminology remain possible; independent literature and mathematical review have not been performed.

## References
1. F. Pedrotti, *Contractive coupling rates and curvature lower bounds for Markov chains*, arXiv:2308.00516, initial public submission 2023-08-01, especially Section 5; https://arxiv.org/abs/2308.00516.
2. F. Münch and R. K. Wojciechowski, *Ollivier Ricci curvature for general graph Laplacians: Heat equation, Laplacian comparison, non-explosion and diameter bounds*, arXiv:1712.00875, initial public submission 2017-12-04, especially Theorem 3.8; https://arxiv.org/abs/1712.00875.
3. L. Veysseire, *Coarse Ricci curvature for continuous-time Markov processes*, arXiv:1202.0420, initial public submission 2012-02-02; https://arxiv.org/abs/1202.0420.
4. Kantorovich–Rubinstein duality, standard finite-metric transport form, used in the proof.
