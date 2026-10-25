# Uniform Poisson collision profiles and sharp avoidance probabilities for random equivalence relations on forests

## Finding
Let \(F_n\) be **any** simple forest on a labelled \(n\)-element set and let \(e_n\) be its edge count, with \(0\le e_n\le n-1\). Independently choose \(r\ge1\) uniform equivalence relations on this set, each chosen from all \(B_n\) set partitions; \(r\) is fixed as \(n\to\infty\). For relation \(E_i\), let \(X_{i,n}\) be the number of forest edges whose endpoints are \(E_i\)-equivalent, and write \(w_n=W(n)\), \(\lambda_n=e_n w_n/n\). Then, **uniformly over all forests and edge counts**, 

\[
 d_{\mathrm{TV}}\!\left(\mathcal L(X_{1,n},\ldots,X_{r,n}),\ \mathrm{Poisson}(\lambda_n)^{\otimes r}\right)\longrightarrow0.
\]

The stronger *relative*, rare-event conclusion is
\[
\sup_{F_n\,\mathrm{forest}}\left|\frac{\Pr\{X_{1,n}=\cdots=X_{r,n}=0\}}{\exp(-r e_n W(n)/n)}-1\right|\longrightarrow0.
\]

In particular, on every labelled spanning tree this probability is \((W(n)/n)^r(1+o(1))\), even though it tends to zero. The result is a quantitative first-order probability law: the sentence \(\bigwedge_{i=1}^{r}\forall x\forall y\,(F(x,y)\to\neg E_i(x,y))\), interpreted with a fixed symmetric irreflexive forest predicate \(F\), has exactly that asymptotic probability under independent uniformly random equivalence-relation expansions.

For **every finite** \(n\) and every forest with \(e\) edges, the entire single-relation law depends on \(n,e\), not the shape of the forest, and satisfies
\[
 \mathbb E[(X)_j]=(e)_j\frac{B_{n-j}}{B_n}\quad(0\le j\le e),\qquad
 \Pr(X=0)=\frac1{B_n}\sum_{j=0}^{e}(-1)^j\binom ej B_{n-j}.
\]
These finite identities are contextual exact enumerations; the new quantitative claim is the *uniform moving-parameter Poisson approximation and sharp relative avoidance asymptotic*, together with its forest characterization.

## Assumptions and scope
A graph is simple, undirected, and loop-free. A forest may have isolated vertices and need not be connected. Every equivalence relation is chosen uniformly among all \(B_n\) partitions of the same labelled vertex set; different relations are independent. No fixed-block-count conditioning is imposed. The forest is deterministic and may vary arbitrarily with \(n\); \(r\) is fixed. The parameter \(W(n)>0\) uniquely solves \(W(n)e^{W(n)}=n\). For the exact identities \((z)_j=z(z-1)\cdots(z-j+1)\), and \(B_0=1\). Total variation is the supremum of the difference of probabilities of measurable events.

## Proof
**1. Conditional forest factorization and its sharp graph boundary.** Apply Stam's construction: choose an integer \(K\ge1\) with
\[
 \Pr(K=k)=\frac{k^n}{e^{1}B_n k!},\qquad k=1,2,\ldots,
\]
and then assign each of the \(n\) vertices independently and uniformly to one of \(K\) boxes; equal boxes define equivalence classes. Dobinski's identity normalizes the weights, and the induced partition is uniform. For any graph edge set \(S\), requiring all edges of \(S\) to have equal endpoint labels has conditional probability \(K^{-|V(S)|+c(S)}\), where isolated vertices are omitted from \(V(S)\) and \(c(S)\) is its number of connected components. If the graph is a forest this equals \(K^{-|S|}\). Since every subset of its edge-indicator family has these product moments, the full family consists of independent \(\mathrm{Bernoulli}(1/K)\) indicators. Hence
\[
 X_{i,n}\mid K_i\sim\mathrm{Binomial}(e_n,1/K_i),
\]
with independently drawn \(K_i\)'s. Conversely, for a graph containing a cycle, taking all edges of that cycle yields a product moment \(K^{-(\ell-1)}\ne K^{-\ell}\) when \(K>1\), so conditional independence of all edge indicators characterizes forests. The finite factorial moments follow by counting ordered distinct edge subsets and merging each forest edge into one vertex; inclusion-exclusion yields the exact avoidance count.

**2. An adequate moderate-deviation bound for Stam's box count.** Set \(w=W(n)\), \(t=n/w=e^w\), and \(a_k=k^n/k!\). The successive log-weight ratio is
\[
 g(x)=n\log(1+1/x)-\log(x+1),\qquad
 g'(x)=-\frac{n/x+1}{x+1}<0.
\]
At \(x=t\), expansion using \(\log t=w\) gives \(g(t)=O(w^2/n)\); on \([t/2,2t]\), \(-g'(x)\ge c w^2/n\) for some absolute \(c>0\) for large \(n\). An integer mode \(k_0\) of the unimodal weights therefore satisfies \(|k_0-t|=O(1)\). Summing the decreasing log ratios on either side of this mode shows that whenever \(h=n^{3/4}/w\), every integer \(k\in[t/2,2t]\) with \(|k-t|>h\) obeys
\[
 a_k/a_{k_0}\le \exp(-c' w^2h^2/n)=\exp(-c'\sqrt n).
\]
There are \(O(n)\) such integers. Beyond \(2t\) the ratios decrease geometrically (in fact \(g(2t)<-w/3\) for large \(n\)); below \(t/2\) monotonicity gives an even smaller finite tail. Because \(\sum_k a_k\ge a_{k_0}\), this proves
\[
\Pr\{|K-t|>n^{3/4}/w\}=O(n\exp(-c''\sqrt n)). \tag{1}
\]
This derivation uses the exact box weights, not an unjustified extrapolation of a central limit theorem to vanishing-probability events.

**3. Moving-parameter Poisson approximation.** On the event complementary to (1), \(K=t(1+O(n^{-1/4}))\). Uniformly for \(0\le e\le n-1\), elementary expansions give
\[
\left|\frac{e}{K}-\frac{e w}{n}\right|=O(w n^{-1/4}),\qquad e/K^2=O(w^2/n).
\]
Le Cam's binomial-to-Poisson inequality and the standard Poisson coupling therefore yield
\[
 d_{\mathrm{TV}}(\mathcal L(X_{i,n}),\mathrm{Poisson}(e w/n))
 \le O(w^2/n+w n^{-1/4})+O(n e^{-c''\sqrt n})=o(1).
\]
Independence of different equivalence relations and the tensor-product total-variation bound prove the asserted joint law for each fixed \(r\), uniformly in the forest.

**4. Relative avoidance, including spanning trees.** On the same event, using \(e\le n-1\),
\[
 e\log(1-1/K)=-e w/n+O(w n^{-1/4}+w^2/n)
\]
uniformly. Thus \((1-1/K)^e=e^{-e w/n}(1+o(1))\) there. The discarded event contributes at most the probability in (1), while \(e^{-e w/n}\ge e^{-w}=w/n\). Therefore its contribution is negligible **relative to the smallest claimed main term**. This proves the relative single-relation probability and, by exact independence of the relations, its \(r\)-th power. For \(e=n-1\), \(e^{-(n-1)w/n}=e^{-w}(1+o(1))=w/n(1+o(1))\). All bounds are uniform in forest shape and edge count.

## Verification
Run `python checker.py` with Python 3, using only the standard library. It enumerates the complete set-partition space for \(1\le n\le7\) and compares \(75\) forest collision histograms, including paths, stars and matchings, to the exact Bell-transform law; it also detects the failure on a graph containing a triangle. Successful output begins `FINITE_CHECKS_OK 75`. These are finite checks of exact identities, **not** proofs of the limiting statements. The analytic proof above supplies the required infinite bounds.

## Relationship to prior work
Koponen (2026) studies conditions for first-order convergence in random finite-structure expansions, motivating explicit quantitative laws in a fixed-structure expansion. Chern--Diaconis--Kane--Rhoades (2015, §§2--3) give Stam's sampling method, the box-count estimates, and the adjacent-pair level statistic; in particular their conditional binomial description of levels strongly anticipates forest-edge factorization, and that precursor is not claimed as new. Galvin--Thanh (2012, §§1--2) establish the shape-independent graphical Stirling polynomial for forests, making the finite counting formulas known consequences, and study Gaussian block-count behavior subject to a component-count condition. Their results are not the stated **uniform total-variation Poisson approximation of constraint violations** or the **relative asymptotic for rare zero-violation events** across all forests. The new step is to control the mixing distribution at a moderate-deviation scale strong enough to preserve a probability as small as \(W(n)/n\). Searching for equivalent statements and consequences remains a priority-risk limitation, not a claim of proved uniqueness.

## Limitations
The graph must be a forest: cycles destroy the conditional independence argument. For general graphs, the conclusion is not established. The number of independent equivalence relations \(r\) is fixed; no uniformity in growing \(r\) is proved. The Poisson mean \(e_nW(n)/n\) may diverge, so the claim is a moving-target approximation, not convergence to a fixed distribution. The result does not imply a universal convergence law for arbitrary first-order sentences on forest expansions. The conditional sampling technique and graphical-Stirling enumeration are prior knowledge; older literature may contain an equivalent rare-event asymptotic.

## References
1. V. Koponen, *A characterization of the finite model property for \(\omega\)-categorical theories*, arXiv:2610.16163, first public 12 October 2026. https://arxiv.org/html/2610.16163v1
2. B. Chern, P. Diaconis, D. M. Kane, R. C. Rhoades, *Central limit theorems for some set partition statistics*, Advances in Applied Mathematics 70 (2015), 92--105. arXiv:1502.00938; https://arxiv.org/abs/1502.00938
3. D. Galvin, D. T. Thanh, *Stirling numbers of forests and cycles*, Electronic Journal of Combinatorics 20 (2013), P73; first arXiv version 15 June 2012. arXiv:1206.3591; https://arxiv.org/abs/1206.3591
