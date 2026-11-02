# Scientific review: induced forests of crown graphs

## Correctness

**PASS.** With selected shores \(X,Y\), the exact edge count \(|X||Y|-|X\cap Y|\), together with the forest edge bound, leaves only shore sizes \((0,b)\), \((1,b)\), \((2,2)\) with a common index, and \((2,3)\) with full containment (plus symmetric cases). The exceptional cases are directly verified to be paths, matchings, or stars. Inclusion-maximality eliminates all but two types when \(n\ge4\), and only the path type remains when \(n=3\). The counting and complementation steps are exact; no asymptotic assumption enters. Independent exhaustive graph construction, cycle checks, and maximality tests agree for \(3\le n\le9\).

## Originality

**PASS, provisional publication priority.** The nearest prior result by Ghalavand and Li provides the size of a largest induced forest in dense balanced bipartite graphs, which implies the scalar value \(n+1\) for crown graphs at \(n\ge4\). It neither enumerates all induced forests nor the inclusion-maximal ones. Lampis, Melissinos, and Vasilakis analyze the complexity of inclusion-minimal feedback vertex sets, rather than the complete cardinality spectrum on this graph family. Melo and Ribeiro focus on optimization formulations; Hertz on decycling properties. Searches for crown, deleted matching, minimal feedback vertex sets, induced forest polynomials, and decycling polynomials did not identify a duplicate result. Search absence does not certify global uniqueness.

## Mathematical value

**PASS.** The two polynomial identities completely describe all forest-inducing subsets and all locally non-extendible solutions for a natural highly symmetric graph family. They refine an already known scalar maximum, and the exact gap of \(n-5\) missing maximal cardinalities (for \(n\ge6\)) persists under complementation to minimal feedback vertex sets. Complete distributions provide a structural fact beyond optimizing one cardinality.

## Closest literature and limits

Melo–Ribeiro (arXiv:2102.09194); Hertz (doi:10.7155/jgaa.00567); Lampis–Melissinos–Vasilakis (arXiv:2302.09604); Ghalavand–Li (arXiv:2501.05145). The exact family-specific counting remains subject to residual unindexed-publication risk, and exhaustive computation is limited to seven graph orders.

Self-review: passed. Independent audit: not yet performed.
