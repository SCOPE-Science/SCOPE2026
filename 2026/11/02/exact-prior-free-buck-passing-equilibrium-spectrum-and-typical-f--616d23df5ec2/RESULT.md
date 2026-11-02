# Exact prior-free buck-passing equilibrium spectrum and typical fairness on \(K_{a,b}\)

## Finding

Consider the deterministic cost-minimizing buck-passing game on the bidirected, loopless complete bipartite graph \(K_{a,b}\), for any integers \(a,b\geq1\). Every player commits to sending the buck to exactly one vertex in the opposite part. A profile is a *prior-free Nash equilibrium* (PFNE) precisely when its functional digraph consists of a single directed even cycle with every noncycle vertex pointing directly into that cycle. If \(2k\) is the cycle length, the exact number of labeled PFNE profiles is

\[
N_k(a,b)=\binom ak\binom bk\,k!(k-1)!\,k^{a+b-2k},\qquad 1\le k\le\min(a,b).
\]

In particular the complete equilibrium polynomial is

\[
P_{a,b}(z)=\sum_{k=1}^{\min(a,b)}N_k(a,b)z^k,
\]

where the exponent \(k\) records half the length of the recurrent cycle. For the balanced network \(K_{m,m}\), choose uniformly from all PFNE profiles and denote half the cycle length by \(K_m\). Let \(\omega>0\) be the unique solution of \(\omega e^\omega=1\), and put \(\alpha=(1+\omega)^{-1}=0.638103743365\ldots\). Then

\[
\frac{K_m}{m}\xrightarrow[m\to\infty]{\Pr}\alpha.
\]

The worst individual long-run buck-holding cost in such a profile is \(1/(2K_m)\). The minimum attainable worst individual cost on \(K_{m,m}\) is \(1/(2m)\), so the equilibrium fairness ratio \(m/K_m\) converges in probability to \(1+\omega=1.567143290409\ldots\). Thus a uniformly sampled equilibrium typically has a linear-sized but non-Hamiltonian recurrent cycle, with a definite asymptotic fairness penalty.

## Assumptions and scope

The graph has labeled vertices partitioned into two nonempty parts of cardinalities \(a\) and \(b\), and contains both directed arcs across each pair of opposite-part vertices and no within-part arcs or self-loops. A pure strategy at vertex \(i\) is one selected out-neighbor \(s(i)\); the resulting directed graph has out-degree one everywhere. Initially Nature draws one vertex from any probability distribution \(\mu\). The buck follows the selected arcs forever, and each player's cost is the expected limiting proportion of time spent at that player. PFNE means Nash equilibrium for **every** initial distribution \(\mu\), not merely for a uniform or fixed prior. All probabilities in the asymptotic conclusion are taken over the finite set of PFNE strategy profiles with equal probability, not over the random initial buck position.

A functional digraph has one directed cycle per weak component; a vertex outside a cycle has *depth* \(d\) if its selected outgoing path enters a directed cycle in exactly \(d\) steps. With a single cycle of length \(L\), every cycle vertex has cost \(1/L\) and all noncycle vertices have cost zero, independently of \(\mu\). For a functional digraph with multiple components and an initial prior of full support, a cycle vertex in component \(H\) has cost \(\mu(H)/L_H>0\), where \(L_H\) is that component's cycle length.

## Proof

**1. Equilibrium structure.** Suppose there are two or more cycle components. Every directed cycle contains vertices from both bipartition parts. Choose a cycle vertex \(i\) in one component, and redirect its outgoing arc to a vertex of the opposite part on another cycle. This removes \(i\) from every recurrent cycle, giving it cost zero instead of a strictly positive cost under any full-support initial prior. Consequently the original profile is not PFNE.

Now suppose there is a unique directed cycle \(C\) of even length \(L=2k\). Let \(v\) be a noncycle vertex of depth \(d\ge2\), and let \(r\) be the first cycle vertex reached from \(v\). A cycle vertex \(i\) of the opposite bipartition part to \(v\) is allowed to redirect its outgoing arc to \(v\). The new cycle follows \(i\to v\), then the length-\(d\) path from \(v\) to \(r\), then the original forward cycle path from \(r\) to \(i\). Writing \(\operatorname{dist}_C(r,i)\) for the latter path length, its new length is

\[
L'=1+d+\operatorname{dist}_C(r,i).
\]

If \(d\) is even, the two vertices \(v,r\) are in the same part, so take \(i\) to be the immediate predecessor of \(r\) on \(C\). It is of the opposite part to \(v\), and \(\operatorname{dist}_C(r,i)=L-1\); thus \(L'=L+d>L\). If \(d\) is odd, then \(d\ge3\) and \(v,r\) are in opposite parts. Choose \(i\) to be the vertex two predecessors before \(r\), so \(i\) lies opposite \(v\) and \(\operatorname{dist}_C(r,i)=L-2\). The construction also works for \(L=2\), when that vertex equals \(r\). Therefore \(L'=L+d-1>L\). As all initial mass reaches the unique cycle, the deviating vertex's cost strictly decreases from \(1/L\) to \(1/L'\), so depth greater than one is impossible at PFNE.

Conversely, suppose the functional graph has exactly one cycle \(C\) and all other vertices have depth one. An off-cycle player has cost zero, so cannot strictly improve. For a cycle vertex \(i\), a legal redirect to a different vertex \(j\in C\) produces a cycle of length \(1+\operatorname{dist}_C(j,i)\le L\). A legal redirect to a depth-one vertex \(v\) produces a cycle of length \(2+\operatorname{dist}_C(r,i)\), where \(r=s(v)\in C\). Because \(v\) lies opposite \(i\), its target \(r\) lies in the same part as \(i\); hence \(\operatorname{dist}_C(r,i)\) is even and at most \(L-2\). Therefore the new cycle has length at most \(L\), and the deviator's new cost is not less than \(1/L\). Thus no player profits under any initial distribution, proving the if-and-only-if classification.

**2. Exact counting.** Every cycle in \(K_{a,b}\) alternates between the parts. Choose \(k\) vertices in each part: \(\binom ak\binom bk\) possibilities. On these fixed \(2k\) labeled vertices there are \((k-1)!k!\) directed alternating cycles: anchor one distinguished vertex of the first part, order its remaining \(k-1\) vertices, and place the \(k\) vertices from the second part in the alternating gaps. Each of the \(a+b-2k\) remaining vertices independently chooses one of the \(k\) opposite-part cycle vertices. These choices are all legal and yield precisely the equilibria classified above. Multiplication yields \(N_k(a,b)\), with no overcounting since the unique cycle is determined by the profile.

**3. Balanced asymptotics.** Set \(a=b=m\). Algebra gives

\[
N_k(m,m)=\frac{(m!)^2}{((m-k)!)^2k}\,k^{2(m-k)}.
\]

For \(0<x\le1\) define

\[
F(x)=-2x-2(1-x)\log(1-x)+2(1-x)\log x,
\]

with the continuous value \(F(1)=-2\). Extend \(F\) to \(x=0\) by the limit \(-\infty\). The uniform Stirling estimate \(\log(j!)=j\log j-j+O(\log(j+2))\), including \(j=0\), gives, uniformly for every integer \(1\le k\le m\),

\[
\log N_k(m,m)=2m\log m+mF(k/m)+O(\log(m+2)).
\]

Direct differentiation for \(0<x<1\) gives

\[
F'(x)=2\left[\log\!\left(\frac{1-x}{x}\right)+\frac{1-x}{x}\right],\qquad
F''(x)=-2\left(\frac1{1-x}+\frac1x+\frac1{x^2}\right)<0.
\]

Thus \(F\) is strictly concave and has a unique maximum at the unique \(\alpha\in(0,1)\) satisfying \(\frac{1-\alpha}{\alpha}\exp(\frac{1-\alpha}{\alpha})=1\), equivalently \(\alpha=(1+\omega)^{-1}\). For every \(\delta>0\), strict maximality and the endpoint limits yield a fixed \(\eta_\delta>0\) such that \(F(x)\le F(\alpha)-\eta_\delta\) whenever \(0<x\le1\) and \(|x-\alpha|\ge\delta\). The uniform Stirling estimate bounds all such terms of the equilibrium sum by \(\exp(2m\log m+mF(\alpha)-m\eta_\delta+O(\log m))\). At least one term near \(k=\alpha m\) has exponent \(2m\log m+mF(\alpha)+o(m)\); summing at most \(m\) terms proves exponentially small tail probability. This establishes \(K_m/m\to\alpha\) in probability.

A balanced graph has a directed Hamiltonian cycle, so the optimal maximal individual cost is exactly \(1/(2m)\): no cost vector whose entries sum to one can have maximum below that. In every equilibrium with a single cycle of length \(2K_m\), precisely those \(2K_m\) recurrent vertices incur positive cost \(1/(2K_m)\). The continuous mapping theorem applied to \(m/K_m\) gives the stated fairness-ratio limit.

## Verification

The standalone `verify.py` enumerates all pure strategies on eight small complete bipartite graphs, evaluates every admissible unilateral deviation using exact rational costs from the functional graph, compares the Nash property against the depth-one structural criterion, and compares observed counts to \(N_k(a,b)\) for each \(k\). It checked 71,799 complete strategy profiles including 65,536 profiles on \(K_{4,4}\); every comparison passed. It also numerically checks the expected saddle-point location of the enumerator for selected balanced sizes. For instance, \(P_{3,3}(z)=9z+72z^2+12z^3\) and \(P_{4,4}(z)=16z+1152z^2+1728z^3+144z^4\). The asymptotic and all-size results follow from the preceding proof; finite enumeration is corroboration only.

Run `python verify.py` with Python 3.10 or later. It uses only the Python standard library.

## Relationship to prior work

Cominetti, Quattropani and Scarsini introduced deterministic and stochastic buck-passing games and proved the prior-free equilibrium existence theorem using a generalized ordinal potential. Their Theorem 3.9 characterizes profitable changes of the functional digraph via cycle enlargement or component merger; their complete-graph example yields Hamiltonian equilibria, and their bidirected-cycle example exhibits small recurrent cycles. Those statements provide the general framework used in Step 1 but do not explicitly give the complete-bipartite depth-one characterization, the exact cycle-size polynomial, or the uniform-equilibrium concentration and fairness constant. The latter two are the principal quantitative additions. The same paper appeared in *Mathematics of Operations Research*; the full freely accessible arXiv text was used for substantive comparison. This is not a claim to introduce the game, the prior-free concept, or the cycle-length improvement criterion.

## Limitations

The count is of *labeled, pure, deterministic, prior-free* equilibria. It is not a count of stochastic or mixed equilibria, of directed graphs with unavailable reciprocal links, or of equilibria for a fixed non-full-support initial distribution. Uniform sampling is over equilibria, not over all strategies or over strategic dynamics and does not describe how improvement paths select their terminal equilibrium. The asymptotic concentration and fairness constant are proved only for equal bipartition sizes; the exact polynomial holds for all positive part sizes. A specialist derivation of the same enumerator or limit outside the inspected literature cannot be excluded; independent literature validation has not been performed.

## References

1. R. Cominetti, M. Quattropani, M. Scarsini, *The Buck-Passing Game*, arXiv:1808.03206, first posted 2018-08-09, full text https://arxiv.org/html/1808.03206v4 , especially Section 3 and Theorem 3.9. Published in *Mathematics of Operations Research* 47(3), 1731–1756 (2022), DOI: https://doi.org/10.1287/moor.2021.1186 .
