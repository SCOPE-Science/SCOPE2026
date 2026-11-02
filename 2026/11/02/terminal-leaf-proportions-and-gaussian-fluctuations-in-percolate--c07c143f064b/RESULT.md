# Terminal-leaf proportions and Gaussian fluctuations in percolated recursive trees

## Finding

Grow a uniform random recursive tree on vertices labelled \(1,\ldots,n\): vertex \(j\ge2\) independently chooses a parent uniformly in \(\{1,\ldots,j-1\}\). Retain each parent edge independently with fixed probability \(p\in(0,1]\). Let \(C_n\) be the number of vertices in the retained-edge component of vertex \(1\), and let \(L_n\) be the number of vertices in that component which have **no children in the original, unpercolated rooted tree**. In particular, \(L_n\) does not count leaves created by deleting edges, and the root is a leaf only when \(n=1\).

Set
\[
 a_n=\frac{\Gamma(n+p)}{\Gamma(1+p)\Gamma(n)},\qquad
 \theta_p=\frac{p}{1+p},\qquad
 v_p=\frac{p(2-p)}{(1+p)^2(p+2)}.
\]
Then the following four statements hold simultaneously:

1. For every integer \(n\ge2\), \(\mathbb EC_n=a_n\) and \(\mathbb EL_n=\theta_p a_n\).
2. For every integer \(n\ge3\), the **exact**, not merely asymptotic, identity is
   \[
     \mathbb E(L_n-\theta_p C_n)^2=v_p\,\mathbb EC_n.
   \]
3. There exists a strictly positive, finite random variable \(W_p\) such that
   \[
     \frac{C_n}{n^p}\longrightarrow W_p,\qquad
     \frac{L_n}{C_n}\longrightarrow\theta_p
     \quad\text{almost surely}.
   \]
4. If \(Z\) is a standard Gaussian independent of \(W_p\), then
   \[
   \left(\frac{C_n}{n^p},\frac{L_n-\theta_p C_n}{n^{p/2}}\right)
     \Longrightarrow (W_p,\sqrt{v_pW_p}\,Z),
   \qquad
   \frac{L_n-\theta_p C_n}{\sqrt{C_n}}
     \Longrightarrow N(0,v_p).
   \]

At \(p=1\), \(C_n=n\), \(W_1=1\), \(\theta_1=1/2\), and \(v_1=1/12\). Thus the result also recovers the classical random-recursive-tree leaf mean and variance, while for \(0<p<1\) the relevant component has a random sublinear size and the Gaussian scaling is its realized square root.

## Assumptions and scope

The coupling across all \(n\) uses independent uniform parents and independent Bernoulli edge-retention marks. Retention probability \(p\) remains fixed as \(n\to\infty\); the endpoint \(p=1\) is included but \(p=0\) is not. Leaves are defined by zero **original-tree outdegree**, and the component is connected to the original root by retained edges. Probabilities and expectations are over both independent random mechanisms. All limits refer to the same nested tree coupling.

## Proof

**1. Exact transitions.** Conditional on the current tree, suppose its root component has \(c\) vertices, of which \(\ell\) are leaves of the whole rooted tree. The next parent is respectively outside the component, one of its \(\ell\) leaves, or one of its \(c-\ell\) nonleaves, with probabilities \((n-c)/n\), \(\ell/n\), and \((c-\ell)/n\). A retained edge to a component leaf replaces that leaf by the new leaf, changing \((C,L)\) by \((1,0)\); a rejected edge there destroys that original-tree leaf and changes it by \((0,-1)\). A retained edge to a component nonleaf changes \((C,L)\) by \((1,1)\); a rejected edge there changes neither count. An attachment outside the component changes neither count. Therefore
\[
 \mathbb E(\Delta C\mid\mathcal F_n)=\frac{pC_n}{n},\qquad
 \mathbb E(\Delta L\mid\mathcal F_n)=\frac{pC_n-L_n}{n}.
\]
These transitions account for the case \(n=1\), where \((C_1,L_1)=(1,1)\).

**2. Exact first and second moments.** The first recurrence yields \(\mathbb EC_n=a_n\). At \(n=2\), \(\mathbb EC_2=1+p\) and \(\mathbb EL_2=p=\theta_p\mathbb EC_2\). Induction in the displayed recurrences gives \(\mathbb EL_n=\theta_p a_n\) for all \(n\ge2\).

Let \(D_n=L_n-\theta_p C_n\). Directly from the four possible component-parent outcomes,
\[
 \mathbb E(\Delta D\mid\mathcal F_n)=-\frac{D_n}{n},\qquad
 \mathbb E((\Delta D)^2\mid\mathcal F_n)
 =\frac1n\left(\frac{pC_n}{(1+p)^2}
             +\frac{(1-p)L_n}{1+p}\right).
\]
The second equality uses the squared increments \(-\theta_p,-1,1-\theta_p,0\) respectively. Consequently \(\mathbb ED_n=0\) for \(n\ge2\), and, setting \(c_p=p(2-p)/(1+p)^2\),
\[
 V_{n+1}=\left(1-\frac2n\right)V_n+\frac{c_p}{n}a_n,
 \qquad V_n=\mathbb E D_n^2,\quad n\ge2.
\]
The \(n=2\) coefficient vanishes, so \(V_3=c_pa_2/2\). Since \(a_{n+1}=(1+p/n)a_n\), induction gives \(V_n=c_pa_n/(p+2)=v_pa_n\) for all \(n\ge3\). The smallest cases are explicitly part of the domain restrictions; the variance identity need not hold at \(n=2\).

**3. Positive component-size limit.** Embed the growth in a continuous-time Yule tree, each vertex giving birth at rate \(1\). At its successive birth times, uniform parent selection exactly reproduces the recursive tree. Independently marking each birth edge retained with probability \(p\) makes the root-component population itself a Yule process of per-capita birth rate \(p\), even though it is coupled to the total population. The standard Yule martingales \(e^{-t}N(t)\) and \(e^{-pt}C(t)\) converge almost surely to finite strictly positive limits (their individual limit laws are unit-mean exponentials). At the time \(\tau_n\) of the \(n\)-th birth, \(N(\tau_n)=n\), so
\[
 \frac{C_n}{n^p}=\frac{e^{-p\tau_n}C(\tau_n)}{(e^{-\tau_n}N(\tau_n))^p}
 \longrightarrow W_p\in(0,\infty)\quad\text{almost surely}.
\]
For \(p=1\), this limit equals \(1\).

**4. Almost-sure terminal-leaf proportion.** For \(n\ge2\), \(U_n=(n-1)D_n\) is a martingale, because \(\mathbb E(D_{n+1}\mid\mathcal F_n)=(1-1/n)D_n\). Its increment is \(D_n+n\Delta D\). The previous conditional second-moment formula, \(\mathbb EC_n=a_n=O(n^p)\), and \(\mathbb ED_n^2=O(n^p)\) imply
\[
 \mathbb E(U_{n+1}-U_n)^2=O(n^{p+1}).
\]
Hence \(\sum_{n\ge2}\mathbb E[(U_{n+1}-U_n)/n^{p+1}]^2<\infty\). The weighted martingale series converges almost surely; Kronecker's lemma implies \(U_n/n^{p+1}\to0\), equivalently \(D_n/n^p\to0\). Division by the strictly positive limit of \(C_n/n^p\) proves \(L_n/C_n\to\theta_p\) almost surely.

**5. Gaussian residual and independence from component scale.** Let \(\langle U\rangle_n\) denote the predictable quadratic variation of the martingale, starting at \(n=2\). The exact increment identities give
\[
 \mathbb E[(U_{j+1}-U_j)^2\mid\mathcal F_j]
 =j\left(\frac{pC_j}{(1+p)^2}
   +\frac{(1-p)L_j}{1+p}\right)-D_j^2.
\]
Using \(C_j/j^p\to W_p\), \(L_j/j^p\to\theta_pW_p\), and a weighted Cesàro sum,
\[
 \frac{\langle U\rangle_n}{n^{p+2}}
 \longrightarrow\frac{p(2-p)}{(1+p)^2(p+2)}W_p=v_pW_p
 \quad\text{in probability}.
\]
The contribution \(\sum_{j<n}D_j^2/n^{p+2}\) tends to zero in \(L^1\), using the exact second-moment formula and \(\sum_{j<n}\mathbb ED_j^2=O(n^{p+1})\). Moreover, \(|U_{j+1}-U_j|\le2j\) because \(|D_j|\le j\) and \(|\Delta D|\le1\). The maximal normalized increment is at most \(2n^{-p/2}\), so the conditional Lindeberg condition holds. The stable martingale central limit theorem now gives the joint limit of \((W_p,U_n/n^{1+p/2})\) as \((W_p,\sqrt{v_pW_p}\,Z)\), with \(Z\) independent of the limiting environment \(W_p\). Since \(U_n=(n-1)D_n\), the asserted joint and self-normalized Gaussian limits follow by Slutsky's theorem.

## Verification

The accompanying `root_cluster_leaf_checker.py` is standalone Python 3. It computes the complete finite \((C_n,L_n)\) Markov law in exact rational arithmetic for several retention probabilities and independently enumerates parent selections and edge-retention patterns on small labelled trees. It checks the finite mean and variance identities. It also produces a seeded simulation diagnostic of the self-normalized Gaussian scale; that diagnostic is not used as a proof of the infinite limit. Run `python root_cluster_leaf_checker.py` in the same directory.

## Relationship to prior work

Desmarais, Holmgren and Wagner [1] study this broadcast/percolation model for preferential-attachment trees and, in the uniform-recursive-tree case, report known root-cluster size asymptotics. They also establish global counts of leaves by color. Those global counts include descendants whose ancestral root-to-vertex path changes color and later returns; they are **not** the number of original-tree leaves within the connected root-color cluster. Their root-cluster results count all component vertices without testing original-tree leaf status. Our theorem concerns the joint component-size/terminal-leaf observable, its exact residual variance, and its self-normalized fluctuations. Known root-component-size convergence is credited as background, not presented as new. Baur [2] examines a different percolation regime with retention probability tending to one; Gu and Yuan [3] study site percolation and cluster size distributions rather than this fixed-parameter bond-percolated terminal-leaf observable.

## Limitations

The statement is restricted to uniform recursive trees and fixed, independent Bernoulli bond retention. It does not cover preferential-attachment parameters other than uniform attachment, site percolation, retention probability varying with tree size, or the number of leaves of the **induced percolation component**. The theorem is mathematical; no inference about empirical tree networks is asserted. Independent verification of literature priority has not been performed.

## References

[1] C. Desmarais, C. Holmgren, S. Wagner, *Broadcasting induced colourings of random recursive trees and preferential attachment trees*, arXiv:2110.15050v1, first publicly submitted 2021-10-28; subsequently *Random Structures & Algorithms* 63 (2023), 364–405. https://arxiv.org/html/2110.15050v1

[2] E. Baur, *Percolation on random recursive trees*, arXiv:1407.2508, first submitted 2014-07-09. https://arxiv.org/abs/1407.2508

[3] C. Gu, L. Yuan, *Size distribution of clusters in site-percolation on random recursive tree*, arXiv:2408.12515, first submitted 2024-08-22. https://arxiv.org/abs/2408.12515
