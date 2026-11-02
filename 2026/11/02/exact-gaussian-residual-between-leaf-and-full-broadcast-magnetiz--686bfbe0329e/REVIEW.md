# Scientific review

## Correctness — PASS
The parent and sign variables are independent, so a single new vertex gives \(\Delta X=\zeta B_U\), \(\Delta Y=(\zeta-I)B_U\), and \(\Delta Z=(\zeta/(1+t)-I)B_U\) exactly. Conditional drift is \(-Z/n\) and the unconditional leaf mean is \(n/2\). The exact residual second-moment recursion has coefficient \(1-2/n\) and forcing \((3-t^2)/(2(1+t)^2)\); this yields \(\mathbb E Z_n^2=n(3-t^2)/(6(1+t)^2)\) for every \(n\ge3\). The martingale \((n-1)Z_n\) has deterministic limiting quadratic variation after scaling by \(n^{3/2}\), and satisfies Lindeberg through uniform step-size bounds. Stable martingale convergence gives asymptotic independence from the \(L^2\) martingale limit of the full-spin sum in the superdiffusive regime. The independent rational checker on complete small state spaces passes 5,622 assertions; no finite test is substituted for an infinite argument.

## Originality — PASS, with residual priority risk
The 2020 broadcasting paper studies recursive-tree voting including leaves, and Desmarais–Holmgren–Wagner (2023), Theorems 2.1 and 2.4, already derive the shared leading superdiffusive amplitude for vertex and leaf color totals. That leading relation is prior knowledge. The inspected relevant sections and appendices did not state the *finite-size exact centered residual variance*, the residual \(\sqrt n\) Gaussian law valid across the entire parameter interval, or joint asymptotic independence after removal of the leading mode. The 2024 recursive-walk reconstruction work does not give that residual theorem. General multitype urn limit results, including Janson (2004), plausibly encompass the Gaussian limiting mechanism, so priority and scope beyond those general theorems require external historical review. Relevant semantically indexed research records on uncolored leaf covariance and on squared full-spin sums do not imply this joint colored-leaf residual theorem.

## Value — PASS
Full-tree and leaf-only broadcast observables are two naturally different data channels in root reconstruction. Subtracting the established common leading mode isolates how much genuinely separate information and variance the leaves retain. An exact \(n\)-scale variance coefficient for *every* sample size and an independent normal second-order mode identify noise invisible in first-order laws; the coefficient also contains the known ordinary recursive-tree leaf variance at zero noise. This is a structurally motivated observable, not a selected numerical exception or a renaming of an established limit.

## Closest literature and limits
- Addario-Berry, Devroye, Lugosi and Velona, *Broadcasting on random recursive trees*, arXiv:2006.11787, first posted 2020-06-21: broadcasting and leaf-only reconstruction framework.
- Desmarais, Holmgren and Wagner, *Broadcasting-induced colorings of preferential attachment trees*, DOI 10.1002/rsa.21142, 2023: known first-order laws, including the same dominant superdiffusive variable in vertex and leaf counts; the strongest direct overlap.
- Althaus, Hartung and Steiner, *A Random Walk Approach to Broadcasting on Random Recursive Trees*, arXiv:2405.04385, 2024: majority reconstruction context.
- Janson, *Functional limit theorems for multitype branching processes and generalized Pólya urns*, DOI 10.1016/j.spa.2003.12.002, 2004: abstract-level comparison only; general theory is a priority risk.

The result does not cover the singular endpoint \(q=1\), different attachment kernels, a finite-\(n\) independence assertion, or reconstruction-error estimates. Independent audit and definitive priority certification remain outstanding.

Self-review: passed. Independent audit: not yet performed.
