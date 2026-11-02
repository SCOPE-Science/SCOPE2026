# Scientific review

## Correctness — PASS

The one-vertex attachment rules were reconstructed from the original rooted tree and independent bond marks. The \(C,L\) transition system gives the centered residual \(D_n=L_n-pC_n/(1+p)\) conditional drift \(-D_n/n\); its conditional squared-increment identity yields the exact relation
\[\mathbb E D_n^2=\frac{p(2-p)}{(1+p)^2(p+2)}\mathbb EC_n,\quad n\ge3.\]
A Yule embedding proves a strictly positive root-component scaling limit. A weighted martingale convergence argument proves the almost-sure terminal-leaf ratio, while direct predictable-quadratic-variation and vanishing-maximal-increment checks permit the stable martingale central limit theorem. Exact independent full-tree enumeration and state-space propagation passed 313 checker assertions; numerical simulation is only a diagnostic. The standard martingale CLT is used as a theorem, not re-proved from first principles.

## Originality — PASS (qualified)

Desmarais, Holmgren and Wagner (2021, arXiv:2110.15050v1) calculate global leaves by broadcast colour and root-cluster size separately; their root-cluster statements and leaf-colour covariance appendix were inspected. In their model, being coloured like the root need not mean being connected to it by retained edges, because two flips can return to the root colour. The new statistic counts original-tree leaves inside the fully retained-path component. Baur (arXiv:1407.2508) concerns a near-one retention regime and cluster size statistics; Gu and Yuan (arXiv:2408.12515v1) study site-percolation cluster-size distributions and a bond/site coupling. Searches of accessible published mathematical claims identified the closest root-degree/component-size dependence and all-tree leaf/broadcast-spin residual results but not the joint original-terminal-leaf/root-cluster observable. These comparisons support originality without establishing absolute historical priority. The risk of a previously published general marked-branching result implying the theorem remains.

## Value — PASS

The source's separate cluster-size and leaf-colour analyses leave a natural structural question: what fraction of the connected root lineage is genuinely terminal in the complete tree, rather than becoming a leaf merely by deletion of edges? The theorem supplies the exact proportion \(p/(1+p)\), an exact finite-size centered variance, and a Gaussian limit normalized by the realized random sublinear component size. It gives meaningful second-order information on a natural nonlocal population characteristic, not a renaming of the global leaf/broadcast residual.

## Scope and limitations

Only fixed \(p\in(0,1]\), independent Bernoulli bond retention and uniform random recursive trees are covered. Terminality is measured in the original tree, not the percolation-induced subgraph. Normal convergence is asymptotic; finite checker and simulation outcomes do not certify infinite statements. Related preferential-attachment and site-percolation cases remain unproved. No independent mathematical audit has been performed.

## Primary references

- Desmarais, Holmgren and Wagner, *Broadcasting induced colourings of random recursive trees and preferential attachment trees*, arXiv:2110.15050v1 (2021), https://arxiv.org/html/2110.15050v1.
- Baur, *Percolation on random recursive trees*, arXiv:1407.2508 (2014), https://arxiv.org/abs/1407.2508.
- Gu and Yuan, *Size distribution of clusters in site-percolation on random recursive tree*, arXiv:2408.12515v1 (2024), https://arxiv.org/html/2408.12515v1.

Self-review: passed. Independent audit: not yet performed.
