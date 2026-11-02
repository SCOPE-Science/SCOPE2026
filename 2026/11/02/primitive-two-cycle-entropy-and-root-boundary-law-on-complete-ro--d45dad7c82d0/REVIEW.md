# Scientific review: rooted-tree primitive two-cycles

## Correctness

**PASS.** The domain is the finite, loopless, sink-free, labelled complete rooted \(d\)-ary tree, with arbitrary nonnegative integer initial chip heights and \(d\ge2,h\ge1\). A two-step return forces the two-step firing count to be constant on the connected graph. A nonfixed return therefore alternates firing at every vertex. The finite intervals of allowable heights are both necessary and sufficient, with exactly \(\deg_H(v)\) choices at each vertex. On a tree each edge subset is the cut of a unique two-coloring up to global reversal, so the sum over vertex-covering edge subsets counts temporal orbits without double counting. The subtree external-edge recursion, root-binomial law, convergent entropy series, and finite-height asymptotics are algebraic consequences checked line by line. Standalone integer computations independently enumerate the weighted edge subsets and direct microscopic states on small trees. Numerical checks are corroboration, not the infinite proof.

## Originality

**PASS, with historical-access risk.** Bitar–Goles (1992) establishes only the allowable eventual periods on trees in the available abstract and subsequent citations; the complete 1992 manuscript was not accessible for a definitive full-text comparison. Jiang (arXiv:1003.0943, Section 2) gives a general equal-firing-count criterion, a premise correctly treated as known, but does not state the full rooted-tree exact orbit recurrence, limiting per-vertex orbit entropy or distribution of opposite-phase root edges. Scully–Jiang–Zhang (2014, Sections 3–5) studies firing words and passive tree-like attachments, rather than weighted orbit enumeration. Inagaki–Khovanova–Luo (arXiv:2410.00039) addresses an infinite binary tree with a looped root, a root-origin chip input and eventual stability rather than finite-tree synchronous temporal orbits. Searches for the exact binary sequence and associated weighted edge-cover model located no dominating theorem. Absence of search matches is not proof of uniqueness; a historical equivalent remains possible.

## Mathematical value

**PASS.** A period-length theorem alone does not measure the multiplicity of recurrent modes. The two-boundary subtree recursion gives the complete nonfixed orbit count for every finite \(d\)-ary tree, and the entropy constant quantifies recurrence as depth grows. The root size-biased binomial law adds a natural local order parameter under the uniform recurrent-orbit measure. The asymptotic decay \(\rho_d\to1\) under increasing branching is structurally informative: increasing the number of forced terminal edges suppresses recurrent-orbit multiplicity per vertex. The object, invariant, probability measure and limiting regimes are intrinsic to a standard graph and dynamical process rather than arbitrary numerical slices.

## Limits and closest literature

The result does not enumerate fixed configurations, transients, or spatial-isomorphism orbits, and it does not claim an independently certified decimal. The Bitar–Goles 1992 full text was not obtained; the accessible abstract and citations are not treated as whole-document exclusion evidence. The 2014 and 2024 sources differ either in invariant or model; their precise results and domains are compared in `RESULT.md`. All checks are a self-review, not independent external validation.

Self-review: passed. Independent audit: not yet performed.
