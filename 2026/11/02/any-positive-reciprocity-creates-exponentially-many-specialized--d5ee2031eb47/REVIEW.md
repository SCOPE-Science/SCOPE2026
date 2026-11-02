# Scientific review

## Correctness — PASS

The claim concerns specialized public-good equilibria, identified precisely with digraph kernels. For each ring edge the probabilities of clockwise-only, counterclockwise-only and bidirectional status are respectively \((1-r)/2,(1-r)/2,r\); different undirected edges are independent. A noncoherent strict orientation of a cycle is acyclic and therefore has a unique kernel. Restoring reverse arcs preserves kernels, which identifies the only kernel-free configurations exactly. A kernel's cyclic gaps have lengths two or three, giving probabilities \(u=a(2-a)\) and \(v=a^2\). Marked cyclic-gap enumeration proves the expectation, and a logarithmic generating function proves the cubic trace formula. Primitivity of the companion matrix proves the Perron asymptotics; implicit differentiation gives the crossover coefficient \(4/9\). An eight-edge gadget has two interchangeable internal kernel patterns, independent across disjoint nine-edge windows; a binomial Chernoff argument yields the typical exponential bound. Direct enumeration from `verify.py` passed all \(9828\) three-state rings through eight vertices, 60 exact rational aggregate comparisons, and three explicit gadget-flip tests.

**Risks/limits:** finite verification cannot prove statements for every ring size; the proof itself supplies the general argument. The result says nothing about nonspecialized Nash equilibria, noncyclic architectures, asymmetric direction laws, or a distributional limit in the vanishing-reciprocity window.

## Originality — PASS (qualified)

Huang, Sun, Xu and Zhao (2025), arXiv:2512.23193, establish the specialized-equilibrium/kernel correspondence, a qualitative monotonicity principle for converting one-way edges to reciprocal edges, and large dense-random-digraph existence results. The model-specific probability, weighted expectation, crossover, and typical exponential multiplicity on a fixed cycle are not results of those statements. Bisdorff and Marichal (2008) identify maximal-independent-set counts of undirected cycles with Perrin numbers; that explicitly covers the fully reciprocal endpoint, which is not claimed as original. Earlier literature on weighted independent dominating set polynomials may imply the first-moment identity but not automatically the constructive high-probability exponential transition.

Public research-record and literature searches did not identify an implication covering the combined stochastic ring theorem. This is a best-knowledge comparison, not a uniqueness or priority certificate. Relevant full primary sections of the 2025 paper were inspected; the 2008 publisher page and abstract were accessible but not its full PDF/text. Unindexed results and stronger weighted-enumeration techniques remain residual risks.

## Mathematical value — PASS

The motivated gap is *how many* specialist equilibria network reciprocity creates, rather than the previously known fact that it cannot remove an equilibrium. The exact probability law distinguishes existence from multiplicity, and the doubling-gadget proof establishes that any fixed positive reciprocity changes the typical equilibrium count from bounded to exponential. The weighted spectral formula separately identifies the \(1/n\) scale at which the mean first departs from one, a quantitative prediction distinct from fixed-reciprocity typical behavior. These are structural and asymptotic laws for a canonical sparse network game rather than an arbitrary small-case calculation.

## Prior work and residual limitation

- Huang, Sun, Xu, Zhao, *Public Goods Provision in Directed Networks: A Kernel Approach*, arXiv:2512.23193 (first posted December 29, 2025): theorem on kernels and reciprocity monotonicity, but not the random ring distribution.
- Bisdorff, Marichal, *Counting Non-Isomorphic Maximal Independent Sets of the n-Cycle Graph*, Journal of Integer Sequences 11 (2008), Article 08.5.7: known Perrin endpoint and cycle enumeration.

The weighted-Perrin relation is close to known cyclic independence enumerators; priority for that component alone is not asserted. The high-probability doubling transition is the main structural contribution. All claims remain subject to independent scientific scrutiny.

Self-review: passed. Independent audit: not yet performed.
