# Sharp identifiability boundary for singleton slices of Bernoulli products
## Finding
For an integer \(n\ge2\), let \(\operatorname{Ber}(\mathbf p)\) denote the product law of independent Bernoulli coordinates with parameter vector \(\mathbf p=(p_1,\ldots,p_n)\in[0,1)^n\). Define its singleton fingerprint
\[
F_i(\mathbf p)=p_i\prod_{j\ne i}(1-p_j),\qquad i=1,\ldots,n.
\]
These are exactly the probabilities of the Hamming-weight-one atoms.

The map \(F\) is injective on
\[
\mathcal D_n=\left\{\mathbf p\in[0,1)^n:\sum_{i=1}^n p_i\le1\right\}.
\]
Hence, for every \(0\le\lambda<1\), the restriction of \(F\) to the cube \([0,\lambda]^n\) is injective if and only if \(\lambda\le1/n\).

The threshold has a sharper stability interpretation. At \(\lambda=1/n\), injectivity survives but no finite constant \(C\) can satisfy
\[
\operatorname{TV}(\operatorname{Ber}(\mathbf p),\operatorname{Ber}(\mathbf q))
\le C\,\|F(\mathbf p)-F(\mathbf q)\|_1
\]
uniformly over \(\mathbf p,\mathbf q\in[0,1/n]^n\). For every \(\lambda>1/n\), there are distinct homogeneous vectors \(\mathbf p\ne\mathbf q\) in \([0,\lambda]^n\) with \(F(\mathbf p)=F(\mathbf q)\), while their product laws have positive total variation. Thus \(1/n\) is the exact identifiability boundary for the singleton slice, and the boundary itself is already too ill-conditioned for a uniform total-variation upper bound based only on singleton discrepancy.

## Assumptions and scope
The statement concerns finite Bernoulli product measures and the labeled singleton probabilities, not merely the distribution of the total number of successes. The parameter cube is restricted to \(0\le\lambda<1\), so all odds are finite. The result is deterministic and finite-dimensional for every \(n\ge2\).

The fresh motivating literature gives a dimension-free analytic proxy for total variation of arbitrary product measures and explicitly places the earlier Bernoulli small-parameter singleton-slice theorem in that program. The earlier Bernoulli theorem proves a uniform upper bound from singleton discrepancy on \([0,1/(2n)]^n\). The present claim does not extend that upper bound to the full interval below \(1/n\); it identifies the exact point at which singleton information ceases to be stably or even uniquely informative.

## Proof
Put
\[
P_0(\mathbf p)=\prod_{i=1}^n(1-p_i),\qquad
o_i(\mathbf p)=\frac{p_i}{1-p_i}.
\]
Then
\[
F_i(\mathbf p)=P_0(\mathbf p)o_i(\mathbf p).
\]
Suppose first that \(F(\mathbf p)=F(\mathbf q)\ne0\). The ratios of the nonzero coordinates of \(F\) show that the odds vectors lie on the same positive ray. Thus for some fixed nonzero \(\mathbf r\ge0\) and positive scalars \(s,t\),
\[
o_i(\mathbf p)=s r_i,\qquad o_i(\mathbf q)=t r_i.
\]
Along this ray write
\[
p_i(u)=\frac{u r_i}{1+u r_i},\qquad
h(u)=\frac{u}{\prod_j(1+u r_j)}.
\]
Then \(F_i(\mathbf p(u))=r_i h(u)\), and direct differentiation gives
\[
\frac{h'(u)}{h(u)}=
\frac1u-\sum_j\frac{r_j}{1+u r_j}
=\frac1u\left(1-\sum_j p_j(u)\right).
\]
The function \(u\mapsto\sum_j p_j(u)\) is strictly increasing unless all \(r_j=0\). Therefore \(h\) is strictly increasing while \(\sum_jp_j(u)<1\), has at most one stationary point when the sum equals one, and is strictly decreasing afterward. If both endpoints lie in \(\mathcal D_n\), the entire ray segment between them remains in the increasing region, with a possible zero derivative only at its final endpoint. Hence \(h(s)=h(t)\) implies \(s=t\), and therefore \(\mathbf p=\mathbf q\). If \(F(\mathbf p)=0\), then \(P_0(\mathbf p)>0\) forces every odds coordinate to vanish, so \(\mathbf p=0\); this handles the remaining case. Thus \(F\) is injective on \(\mathcal D_n\).

If \(\lambda\le1/n\), every point of \([0,\lambda]^n\) lies in \(\mathcal D_n\), proving injectivity on the cube. Conversely, suppose \(\lambda>1/n\). Choose \(b\in(1/n,\min\{\lambda,1\})\) and consider
\[
\phi(u)=u(1-u)^{n-1}.
\]
Since
\[
\phi'(u)=(1-u)^{n-2}(1-nu),
\]
\(\phi\) is strictly increasing on \([0,1/n]\) and strictly decreasing immediately afterward. Therefore there is a unique \(a\in(0,1/n)\) with \(\phi(a)=\phi(b)\). For the homogeneous vectors \(\mathbf p=a\mathbf1\) and \(\mathbf q=b\mathbf1\), every singleton probability equals \(\phi(a)=\phi(b)\), so \(F(\mathbf p)=F(\mathbf q)\) although \(\mathbf p\ne\mathbf q\). Their product distributions are distinct; indeed total variation is at least the total variation of a single marginal, namely \(|a-b|>0\). This proves the exact cube threshold and the impossibility of any singleton-based upper bound when \(\lambda>1/n\).

It remains to examine the boundary. Let \(u_*=1/n\), \(\mathbf q=u_*\mathbf1\), and \(\mathbf p_\varepsilon=(u_*-\varepsilon)\mathbf1\) with \(0<\varepsilon<u_*\). Then
\[
\|F(\mathbf q)-F(\mathbf p_\varepsilon)\|_1
=n\{\phi(u_*)-\phi(u_*-\varepsilon)\}.
\]
Because \(\phi'(u_*)=0\) and
\[
\phi''(u_*)=-n(1-1/n)^{n-2},
\]
Taylor expansion yields
\[
\|F(\mathbf q)-F(\mathbf p_\varepsilon)\|_1
=\frac{n^2}2(1-1/n)^{n-2}\varepsilon^2+O(\varepsilon^3).
\]
On the other hand, projecting the product measures onto one coordinate gives
\[
\operatorname{TV}(\operatorname{Ber}(\mathbf p_\varepsilon),\operatorname{Ber}(\mathbf q))
\ge\varepsilon.
\]
The ratio of total variation to singleton discrepancy therefore diverges at least on the order of \(1/\varepsilon\). No finite uniform constant exists at \(\lambda=1/n\).

## Verification
The argument is analytic. The accompanying `verify.py` checks the homogeneous fold numerically for several dimensions and verifies the divergence of the boundary ratio. Its role is supplementary; the proof does not rely on finite experiments.

The proof also gives a direct falsification check for each boundary statement: below \(1/n\), every odds ray stays on the increasing branch; above \(1/n\), the homogeneous ray crosses the unique maximum of \(u(1-u)^{n-1}\); at \(1/n\), the first derivative vanishes and the singleton change is quadratic while a marginal total-variation change is linear.

## Relationship to prior work
Avital, Kontorovich, Vershynin and Zou give a universal constant-factor analytic proxy for total variation of arbitrary product measures and cite the Bernoulli small-parameter work as a complementary specialized result. Their proxy uses the full marginal midpoint scores and does not state an injectivity or stability threshold for the labeled singleton slice.

Avital, Kontorovich and Salafatinos prove that, on \([0,1/(2n)]^n\), total variation is bounded above and below by constant multiples of the singleton discrepancy. Their Lemma 4.3 proves parameter control from the singleton slice on that same cube, using the small-odds condition needed by their later recursion. The present result identifies the exact larger injectivity boundary \(1/n\), proves that uniform Lipschitz control already fails at the boundary, and gives exact nonidentifiability immediately beyond it. Thus it is neither a restatement nor a corollary of their stated \(1/(2n)\) theorem.

Targeted searches for singleton-slice injectivity, conditional exactly-one-success odds, inverse Poisson-binomial parameterization, and the \(1/n\) threshold did not locate a published statement of this trichotomy. The closest retrieved literature concerns total-variation proxies or asymptotic rare-Bernoulli behavior rather than exact injectivity of the singleton fingerprint.

## Limitations
The result gives an identifiability and stability barrier, not a sharp positive total-variation comparison throughout \(0\le\lambda<1/n\). In particular, it does not determine the largest \(\lambda\) for which a dimension-free constant can control total variation by singleton discrepancy. The exact threshold concerns labeled singleton atom probabilities; coarser observations, such as only the total probability of one success, contain less information.

A residual originality risk remains because the ray calculation is elementary and could appear under different inverse-problem terminology. Searches covered the main aliases and the highly relevant recent and precursor papers, but absence from those searches is not a proof of global novelty.

## References
1. A. Avital, A. Kontorovich, R. Vershynin, G. Zou, *Total Variation Distance between Product Distributions: an Analytic Proxy*, arXiv:2609.21049v1, 2026.
2. A. Avital, A. Kontorovich, G. Salafatinos, *TV over Bernoulli products: the small parameter regime*, arXiv:2602.21828v1, 2026.
