# Exact stationary correlation hierarchy and two noise scales on clique windmills

## Finding

Let \(W_{n,m}=K_1\vee(nK_m)\) be the generalized windmill graph: one central vertex joined to every vertex of \(n\) disjoint cliques, each of order \(m\), where \(n,m\ge2\). Consider the asynchronous, rate-one, binary noisy voter model on this graph. At an update of vertex \(x\), with probability \(p\in(0,1)\) set its spin to an independent fair \(\{-1,+1\}\) spin, and otherwise copy a uniformly selected neighbor's spin. Denote expectations under its unique stationary distribution by \(\mathbb E\).

Let \(h\) be the hub, and let \(x,y,z\) be rim vertices such that \(x,y\) are distinct members of one clique and \(z\) is in a different clique. Write
\[
U=\mathbb E[\sigma_h\sigma_x],\qquad
V=\mathbb E[\sigma_x\sigma_y],\qquad
W=\mathbb E[\sigma_x\sigma_z].
\]
Put \(s=1-p\), and define
\[
a=\frac{s}{2+(m-2)p},\quad b=\frac{s}{1+(m-1)p},\quad
F=\frac1m+\frac{1+(m-1)a}{nm},\quad
G=\frac{m-1}{m}+\frac{(m-1)a}{nm}+\frac{n-1}{n}b.
\]
**Exact finite-graph law and strict hierarchy:** for all integers \(n,m\ge2\) and all \(0<p<1\),
\[
\boxed{U=\frac{sF}{2-sG},\qquad V=a(1+U),\qquad W=bU,\qquad V>U>W>0.}
\]
Thus two different vertices inside a petal are more strongly correlated than the hub and a rim vertex, despite the latter being adjacent; different petals are least correlated.

**First scaling window:** suppose \(m\to\infty\), \(n/m\to\rho\in(0,\infty)\), and \(p=\lambda/m^2\) with fixed \(\lambda>0\). Then
\[
\boxed{(U,V,W)\longrightarrow
\left(\frac{1+2\rho}{1+2\rho+2\lambda\rho},
\frac{1+2\rho+\lambda\rho}{1+2\rho+2\lambda\rho},
\frac{1+2\rho}{1+2\rho+2\lambda\rho}\right).}
\]
**Second scaling window:** under the same joint growth, if \(p=\lambda/m\) with \(\lambda>0\), then
\[
\boxed{(U,V,W)\longrightarrow\left(0,\frac1{2+\lambda},0\right).}
\]
Moreover, for any sequence with \(m^{-2}\ll p\ll m^{-1}\), the limit is \((U,V,W)\to(0,1/2,0)\). These are stationary two-point statements, not claims about the entire spin-configuration law.

## Assumptions and scope

All cliques are complete, internally vertex-disjoint, and identically sized. The graph is finite and simple. Different vertex clocks, refreshed coins, and neighbor selections are independent. Every vertex updates at rate one; this is equivalent for stationary distributions to selecting one uniformly random vertex per discrete update. Each refresh chooses either spin with probability \(1/2\). The parameter \(p\) is strictly positive, guaranteeing an irreducible spin-flip chain and a unique stationary law. An undirected edge is used uniformly when a neighbor is copied, rather than with a common per-edge clock. No assertion is made at \(p=0\), where stationary uniqueness fails.

## Proof

**(1) First moments and second-moment balance.** Let \(C_{ij}=\mathbb E[\sigma_i\sigma_j]\). Global spin-flip symmetry of the unique stationary law gives \(\mathbb E[\sigma_i]=0\), and \(C_{ii}=1\). For distinct vertices \(i\ne j\), apply the stationary generator to \(\sigma_i\sigma_j\). Only updates of \(i\) or \(j\) matter; their refresh expectations vanish. With \(P(i,k)=1/\deg(i)\) for neighbors \(k\), the exact equation is
\[
2C_{ij}=s\sum_k P(i,k)C_{kj}+s\sum_kP(j,k)C_{ik}.
\tag{1}
\]
The automorphism group of the graph acts transitively on each of the three types of distinct unordered pairs, so there are exactly the three unknown correlations \(U,V,W\).

**(2) Resolve the orbit equations.** The hub has degree \(nm\), and each rim vertex has degree \(m\). Counting copies to the partner itself, to the hub, to other members of the same petal, and to other petals in (1) gives
\[
\begin{aligned}
2U&=s\left(\frac1{nm}+\frac{m-1}{nm}V+\frac{n-1}{n}W+\frac1m+\frac{m-1}{m}U\right),\\
V&=\frac{s}{m}\bigl(1+U+(m-2)V\bigr),\\
W&=\frac{s}{m}\bigl(U+(m-1)W\bigr).
\end{aligned}
\tag{2}
\]
The last two equations imply \(V=a(1+U)\) and \(W=bU\). Substitution into the first gives \((2-sG)U=sF\), proving the displayed exact formulas. Their denominator is positive: \(0<s<1\) and
\[
0<G\le\frac{m-1}{m}+\frac{m-1}{2nm}+\frac{n-1}{n}<2,
\]
since \(0<a\le1/2\), \(0<b\le1\). Thus \(U,V,W>0\).

**(3) Prove the strict hierarchy.** Because \(0<b<1\), \(U-W=(1-b)U>0\). A direct rearrangement gives
\[
V-U=(1-a)(b-U).
\tag{3}
\]
The identity is valid because \(a/(1-a)=b\). Furthermore, simplification of the rational definitions yields
\[
b(2-sG)-sF=\frac{p(n-1)(1-p)(m+1-p)}{n[1+(m-1)p]^2}>0.
\tag{4}
\]
Dividing by \(2-sG>0\) proves \(b>U\). As \(a<1\), equations (3) and (4) imply \(V>U\), completing \(V>U>W>0\).

**(4) Asymptotics at the first scale.** Write \(n/m\to\rho\in(0,\infty)\) and set \(p=\lambda/m^2\). Direct expansions, uniform when \(\lambda\) and \(\rho\) stay in compact positive ranges, give
\[
a\to\frac12,\quad b\to1,\quad
mF\to1+\frac1{2\rho},\quad
m(2-sG)\to1+\lambda+\frac1{2\rho}.
\]
Therefore
\[
U\to\frac{1+1/(2\rho)}{1+\lambda+1/(2\rho)}
=\frac{1+2\rho}{1+2\rho+2\lambda\rho}.
\]
The limits of \(V=a(1+U)\) and \(W=bU\) follow immediately.

**(5) Asymptotics at and between the scales.** For \(p=\lambda/m\), we have \(a\to1/(2+\lambda)\), \(b\to1/(1+\lambda)<1\), \(F=O(m^{-1})\), and \(G\to1+1/(1+\lambda)<2\). Hence \(U\to0\), \(W\to0\), and \(V\to1/(2+\lambda)\). If \(m^{-2}\ll p\ll m^{-1}\), then \(a\to1/2\), \(F=\Theta(m^{-1})\), \(1-b\sim mp\), and \(2-sG\asymp mp\); indeed \(1/m=o(mp)\) and \(p=o(mp)\). Thus \(U=O((m^2p)^{-1})\to0\), \(W=bU\to0\), and \(V=a(1+U)\to1/2\). This completes the proof.

## Verification

The accompanying standard-library Python program `verify.py` constructs the three pair-balance equations independently of the closed formulas and solves them with exact rational arithmetic over \(n=2,\ldots,7\), \(m=2,\ldots,6\), and five rational noise levels. It checks the strict inequalities and gap identity; separately it enumerates and iterates the full configuration Markov chain for four graphs of at most seven vertices, comparing stationary correlations with the formulas. It also checks the first, second and intermediate scaling-window predictions numerically. The program prints `VERIFY_OK 512` if all 512 assertions pass. Its finite calculations corroborate, but do not substitute for, the symbolic proof for all \(n,m,p\).

## Relationship to prior work

Pymar and Rivera [1] establish the noisy voter model's general stationary framework and global density limit theorems, with graph examples including the complete graph, cycle, torus, and hypercube. The full accessible preprint and its main theorems do not state the exact three-orbit correlations or two noise-scale limits on clique windmills. Their general process definition and stationary construction are shared ingredients, not claimed new. Benjamini, Helman Tov and Zhukovskii [2] study local temporal repetition statistics for a parallel-update noisy voter model; that statistic and update rule differ from the asynchronous stationary spatial pair correlations here. Peralta and coauthors [3] develop stochastic pair approximations for noisy voter models on heterogeneous networks, rather than the exact windmill-specific finite solution; only bibliographic/abstract material was accessible for direct comparison. Classical noisy-voter duality or general pair balance equations may provide alternative derivations, and no claim of exhaustive historical priority is made.

## Limitations

The result is specific to equal-clique windmills, uniform-neighbor copying, fair reset spins and a positive refresh probability. The limits require both the number of cliques and their order to tend to infinity at a finite positive ratio. They give pairwise second moments only, not independence, Gaussianity or the complete stationary law. The strict inequalities hold for finite parameters but can become equalities in singular limits. An inaccessible potentially related full text and the possibility of equivalent formulas dispersed in earlier stochastic-network literature remain priority risks.

## References

[1] R. Pymar and N. Rivera, *On the stationary distribution of the noisy voter model* (2021 preprint; later *Asymptotic behaviour of the noisy voter model density process*), arXiv:2112.01478, first publicly posted 2021-12-02. https://arxiv.org/abs/2112.01478

[2] I. Benjamini, H. Helman Tov and M. Zhukovskii, *Global information from local observations of the noisy voter model on a graph* (2022 preprint), arXiv:2207.01224. https://arxiv.org/abs/2207.01224

[3] A. F. Peralta, A. Carro, M. San Miguel and R. Toral, *Stochastic pair approximation treatment of the noisy voter model* (2018), arXiv:1807.04615. https://arxiv.org/abs/1807.04615
