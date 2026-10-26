# Exact bipartiteness entropy and conditioned matching laws of randomly twisted hypercubes

## Finding

For every integer \(n\geq1\), construct a graph on \(2^n\) vertices by recursively joining two graphs of dimension \(n-1\) with one independent, uniformly chosen perfect matching. The dimension-one graph is a single edge. In the **independent model**, the two child graphs are independent; in the **duplicube model**, they are identical copies of one sampled child graph, with a new independent matching at the parent.

Write \(B_n^{\mathrm I}\) and \(B_n^{\mathrm D}\) for the probabilities that the respective graphs are bipartite. For every integer \(k\geq2\), define

\[
p_k=\frac{2}{\binom{2^{k-1}}{2^{k-2}}}.
\]

Then the following exact finite-dimensional identities hold:

\[
B_n^{\mathrm I}=\prod_{k=2}^n p_k^{\,2^{n-k}},\qquad
B_n^{\mathrm D}=\prod_{k=2}^n p_k,
\]

where the empty product at \(n=1\) equals one. In particular, \(B_3^{\mathrm I}=B_3^{\mathrm D}=1/3\), whereas \(B_4^{\mathrm I}=1/315\) and \(B_4^{\mathrm D}=1/105\).

The rare-event logarithms have **different exponential scales**:

\[
\lim_{n\to\infty}\frac{-\log B_n^{\mathrm I}}{n2^n}=\frac{\log 2}{2},
\qquad
\lim_{n\to\infty}\frac{-\log B_n^{\mathrm D}}{2^n}=\log 2.
\]

More precisely, the convergent constant

\[
\gamma=\sum_{k=2}^{\infty}2^{-k}\left(
\log\frac{\binom{2^{k-1}}{2^{k-2}}}{2}-2^{k-1}\log 2\right)
\]

satisfies

\[
-\log B_n^{\mathrm I}
=2^n\left(\frac{n-1}{2}\log 2+\gamma\right)+O(n),
\]

and

\[
-\log B_n^{\mathrm D}
=2^n\log 2-\frac{\log 2}{4}n^2
-\left(\frac{\log 2}{4}+\frac{\log\pi}{2}\right)n+O(1).
\]

There is also an exact **conditional sampling law**: conditioned on the final graph being bipartite, **and conditional on the graph-realizations of the two children**, each newly sampled matching is uniform among the permutations consistent with the fixed, balanced child bipartitions. Relative to fixed canonical two-colorings of the children, its color-orientation choice is a fair bit, and conditional on that bit its two within-color bijections are independent and uniform. The fresh random seeds for these conditional kernels can be sampled independently at distinct genuinely sampled recursion nodes; in particular all relative-orientation bits are independent fair bits. **The resulting raw matching permutations need not be unconditionally independent of matchings inside their children.** For a duplicube there is one distinct matching at each dimension, and its child graphs are copied rather than resampled.

Every realized graph is connected and \(n\)-regular. Consequently the above numbers also give the exact probability that the non-lazy simple random walk has period two, or, equivalently, that its adjacency matrix has eigenvalue \(-n\) (equivalently the walk matrix has eigenvalue \(-1\)). When present, the eigenvalue \(-n\) is simple.

## Assumptions and scope

Each uniform matching is a bijection between the labeled vertex sets of the two child graphs. In the independent model, all matching choices at different vertices of the binary recursion tree are independent, and the two children at each internal node are sampled independently. In the duplicube model, the two children at a given step are exact copies of one graph and the new matching is uniform and independent of all earlier matchings. All probabilities are annealed over the specified matching randomness. Dimensions are positive integers. Logarithms are natural. No assumption of asymptotic independence between distinct copied graph instances is made or needed.

For the conditional law, choose any deterministic canonical orientation of each connected bipartite child's unique bipartition, such as assigning color zero to the lexicographically first vertex. The condition 'consistent matching' then means that all cross edges receive opposite colors after choosing one of two possible relative child orientations.

## Proof

**1. Regularity, connectivity, and balance.** The base edge is connected and one-regular. Joining two connected \((n-1)\)-regular children by a perfect matching gives a connected \(n\)-regular graph, for either dependence model. If a child on \(m=2^{n-1}\) vertices is bipartite, counting edges from both sides shows that each bipartition class has exactly \(m/2\) vertices. Connectedness makes the bipartition unique up to global interchange of its two colors.

**2. The exact matching count.** If either child contains an odd cycle, then the parent contains that same odd cycle and cannot be bipartite. Assume both children are bipartite. Fix one two-coloring of each child. A proper two-coloring of the parent restricts to these child colorings, up to one interchange on each child. Therefore all cross-matching edges must join the two children either with the same canonical color or with opposite canonical colors; there are precisely two mutually exclusive possibilities. For either, choose arbitrary bijections between two prescribed classes of size \(m/2\), giving \(((m/2)!)^2\) permutations. Of the \(m!\) equiprobable bijections, exactly \(2((m/2)!)^2\) work. Hence the conditional compatibility probability is \(p_n=2/\binom{m}{m/2}\), independent of the internal shapes of the children.

**3. Probability recurrences and products.** Independence of the child graphs in the independent model gives \(B_n^{\mathrm I}=p_n(B_{n-1}^{\mathrm I})^2\). Exact duplication gives \(B_n^{\mathrm D}=p_n B_{n-1}^{\mathrm D}\), not the square. Since both probabilities equal one at dimension one, iteration yields the displayed products for every \(n\).

**4. Law under conditioning.** For each fixed pair of bipartite children the set of admissible cross permutations has the same cardinality, irrespective of the child geometry. Thus conditioning on the parent being bipartite only conditions its children to be bipartite and restricts its new independent uniform matching to this fixed-size admissible set. In the independent model, the two conditional child samples factor as independent copies of the corresponding smaller conditioned model. In the duplicube model, the unique conditional child is sampled once and copied. Within the admissible set, the two disjoint classes of relative orientations have equal size, so the orientation bit is fair; conditional on this bit the two within-class bijections are independent and uniform. Recursing proves the exact conditional construction: the relative-orientation bits and the fresh auxiliary bijection seeds can be taken independent across genuinely sampled nodes, while each raw permutation remains a function of its child bipartitions and hence may depend on earlier graph randomness.

**5. Asymptotics.** Set \(\ell_k=-\log p_k\). Stirling's formula with its uniformly summable remainder at dyadic arguments yields

\[
\ell_k=2^{k-1}\log 2-\frac{k}{2}\log 2-\frac12\log\pi+O(2^{-k})
\quad(k\to\infty).
\]

Consequently \(\ell_k-2^{k-1}\log2=O(k)\), and the series defining \(\gamma\) converges absolutely. The independent product gives

\[
-\log B_n^{\mathrm I}=
\sum_{k=2}^n2^{n-k}\ell_k
=(n-1)2^{n-1}\log2+2^n\gamma
-2^n\sum_{k>n}2^{-k}(\ell_k-2^{k-1}\log2).
\]

The omitted tail is \(O(n)\) after multiplication by \(2^n\), giving the stated independent expansion. For the duplicube, summing \(\ell_k\) from \(k=2\) through \(n\) gives \((2^n-2)\log2\) from the leading term; the sums of \(k\) and of constants give the stated quadratic and linear terms. The \(O(2^{-k})\) remainders sum to \(O(1)\). Dividing these expansions by the asserted scales proves both limits.

**6. Markov-chain and spectral interpretation.** A simple nearest-neighbor walk on a finite connected graph without self-loops has period two exactly when the graph is bipartite; otherwise an odd cycle makes its period one. Since the adjacency matrix here is irreducible, symmetric, and \(n\)-regular, its eigenvalue \(n\) is simple, and it has eigenvalue \(-n\) exactly in the bipartite case. For a connected bipartite graph the alternating-sign eigenvector gives that eigenvalue and its simplicity follows from Perron–Frobenius applied to the irreducible nonnegative adjacency matrix.

## Verification

Run `python verify.py` using Python 3.10 or later; only the standard library is required. The checker enumerates all 24 dimension-three top matchings, all 40,320 top matchings for each of two bipartite dimension-three child-pairs, confirms exact conditional counts \(8/24\) and \(1152/40320\), tests a nonbipartite-child obstruction, checks rational recurrence/product identities through dimension six, and checks numerically evaluated logarithmic expansions through dimension fourteen. It outputs `PASS` or raises an assertion.

These finite computations independently check representative combinatorial cases; the proofs above establish every dimension and both asymptotic limits. The \(O(n)\) and \(O(1)\) conclusions use the analytic Stirling remainder rather than finite extrapolation.

## Relationship to prior work

Benjamini, Dikstein, Gross, and Zhukovskii defined both independent twisted hypercubes and duplicubes and demonstrated that many **typical** geometric and spectral properties are shared between them. Their discussion of chromatic number notes that bipartiteness fails with high probability, but does not provide these exact probabilities, rare-event logarithmic asymptotics, or conditional sampling laws. Baran and Šarković subsequently studied mixing and cover times of simple and lazy walks and proved strong nonbipartiteness properties with high probability; these are typical-event estimates, rather than exact probability laws for the exceptional period-two event. The present comparison quantifies how different recursion dependencies cause a factor-\(n\) separation in the leading rarity exponent despite the models' similar typical properties.

## Limitations

The formula concerns exact bipartiteness, not the full chromatic-number distribution, mixing times on the nonbipartite majority, or conditional expansion of the rare bipartite graphs. The conditional matching representation is not an independence assertion about two children of a duplicube. No claim is made about analogous probabilities for arbitrary dependent couplings of the child graphs. The event is extremely rare as dimension grows; exact enumeration cannot efficiently sample it by naive Monte Carlo. A broader published theorem about random matching compatibility could yield the counting step as a corollary; the combined specific model comparison and sharp expansions require a source-sensitive priority check.

## References

1. Z. Baran and A. Šarković, *Mixing time of the lazy and simple random walk on a randomly twisted hypercube*, arXiv:2610.21976v1, publicly posted October 15, 2026. https://arxiv.org/html/2610.21976v1
2. I. Benjamini, Y. Dikstein, R. Gross and M. Zhukovskii, *Randomly twisted hypercubes -- between structure and randomness*, arXiv:2211.06988v1, publicly posted November 13, 2022; later in *Random Structures & Algorithms*, DOI:10.1002/rsa.21267. https://arxiv.org/abs/2211.06988
3. Standard binomial Stirling asymptotics, \(\binom{2m}{m}=4^m/\sqrt{\pi m}\,(1+O(m^{-1}))\), and standard irreducible finite Markov-chain periodicity / Perron–Frobenius criteria; proved or applied in the relevant steps above.
