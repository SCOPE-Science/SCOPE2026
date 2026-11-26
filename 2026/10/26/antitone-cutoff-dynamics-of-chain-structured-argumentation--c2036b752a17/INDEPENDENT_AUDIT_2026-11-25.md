# Independent mathematical audit

## correctness

PASS

In the stated SAF semantics, an attacker in row i hits the subarguments of j exactly when its first target is <=j. Thus attacks by E_k form the suffix starting after h(k), conflict-freeness is h(k)>=k, and undefended arguments are those hit by a row not counterattacked by E_k, namely a row through h(k). Their complement is E_{h(h(k))}. Closure forces all admissible sets to be prefixes, and stability combines coverage of the outside suffix with conflict-freeness, so h(k)=k. A nonincreasing map of n+1 states has at most one fixed point, and its square's fixed points are just fixed points and two-cycle pairs. Only the lower index of a nontrivial pair passes conflict-freeness. Iterating the nondecreasing h^2 from 0 gives a fixed point k; taking min(k,h(k)) establishes existence of a complete prefix. The disjoint cycles give the bound and the ordered prefixes give a unique largest complete extension. The antidiagonal attack realizes h(k)=n-k, attaining the bound also at n=1. Every weakly decreasing n-tuple in [0,n] is realized by the one-target/empty-row construction. For a stable profile at k, choose the k-1 preceding values from [k,n] and the n-k trailing values from [0,k] as multisets; this gives the stated binomial product. The unique fixed-point property makes the summation disjoint, and Vandermonde gives the half count.

## originality

PASS

The SAF semantics, general defense fixed-point theorem, Ferrers row nesting, and binomial identities are not new. The supported distinct result is their chain-specific reduction to an antitone state variable with an exact sharp extension census and position-refined profile census. The strongest inspected SAF and nested-neighborhood literature supplies ingredients but no equivalent combined law or directly covering result. This conclusion is limited by incompletely accessible older Ferrers literature.

## value

PASS

A total subargument chain is a natural test case for how closure and attack projection constrain extensions. One cutoff gives all three semantics, makes the largest complete extension unique despite potentially many complete extensions, and quantifies exactly how stable existence varies across realizable profiles. This replaces reasoning over arbitrary attack matrices by a complete, sharp classification. The elementary binomial evaluation is not the sole contribution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
