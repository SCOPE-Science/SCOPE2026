# Exact rank-two probability spectra for independent random successor orders

## Finding

Fix an integer \(k\geq1\). On \([n]\), choose \(k\) independent uniform linear orders and interpret \(S_i(x,y)\) as immediate succession in the \(i\)-th order. The language consists **only** of equality and \(S_1,\ldots,S_k\); it has no order symbols, parameters, additional predicates, or counting quantifiers. Let \(\mathcal L_{k,2}\) be the closed two-variable first-order sentences of quantifier rank at most two. Put \(m=k(k-1)\) and \(u=e^{-1}\).

Every limit \(\lim_{n\to\infty}\Pr(\mathcal M_n\models\varphi)\) with \(\varphi\in\mathcal L_{k,2}\) exists, and the **entire set** of possible limits is exactly
\[
\left\{\sum_{j=0}^{m} a_j u^j(1-u)^{m-j}:\quad a_j\in\mathbb Z,\quad 0\leq a_j\leq\binom mj\right\}.
\]
Its cardinality is exactly
\[
\prod_{j=0}^{m}\left(\binom mj+1\right).
\]
For \(k=1,2,3\), respectively, the cardinalities are \(2\), \(12\), and \(1{,}053{,}696\). In particular, quantifier rank two has a zero-one law for a single successor, but not for two successors.

A stronger probabilistic assertion underlies the classification: for each \(i<j\), count the directed edges common to \(S_i\) and \(S_j\), and those common to \(S_i\) and the reversal of \(S_j\). These \(m\) counts converge **jointly** to independent rate-one Poisson variables.

## Assumptions and scope

A uniform linear order on \([n]\) is a uniformly random permutation of its elements. For distinct \(a,b\), the binary relation \(S_i(a,b)\) means that \(b\) immediately follows \(a\). All \(k\) orders are independent. The integer \(k\) is fixed while \(n\to\infty\). The number \(m\) counts two relative orientations for each unordered pair of order indices. Quantifier rank is maximum nesting depth of quantifiers, not the total number of quantifier occurrences. Sentences may have arbitrary finite Boolean complexity but only variables \(x,y\). The theorem does not assert the same spectrum for higher quantifier rank, extra predicates, or varying \(k\).

For \(1\leq i<j\leq k\), define
\[
X_{ij}^{+}=|S_i\cap S_j|,\qquad
X_{ij}^{-}=|S_i\cap S_j^{-1}|,
\]
where these are sets of directed ordered pairs. Define the event variables \(B_{ij}^{\pm}=\mathbf 1\{X_{ij}^{\pm}>0\}\).

## Proof

**1. Joint Poisson limit.** Fix nonnegative integer factorial-moment orders for all \(m\) categories, of total order \(R\). Expand the corresponding mixed falling factorial moment as a sum over selections of \(R\) distinct directed-pair adjacency requirements. A selected requirement specifies that one ordered vertex pair is an edge in each of two designated orders, in equal or opposite directions. For each order \(i\), if its \(r_i\) required directed edges form vertex-disjoint directed paths, exactly \((n-r_i)!\) of the \(n!\) permutations realize them. Inconsistent requirements (cycles, branching, or contradictory orientations) have probability zero. Hence any compatible constraint pattern has probability
\[
\prod_{i=1}^{k}(n)_{r_i}^{-1}=O(n^{-\sum_i r_i}),
\]
where \((n)_r\) is a falling factorial.

If the \(R\) selected requirements use pairwise vertex-disjoint geometric edges, they involve \(2R\) distinct vertices and exactly \(2R\) order-edge requirements. There are \(n^{2R}(1+O(n^{-1}))\) ways to select their oriented vertex pairs, and their total contribution tends to one. All other compatible selections contribute \(O(n^{-1})\): group selected requirements by their shared vertex sets. A connected group with \(h\geq2\) distinct geometric edges spans at most \(h+1\) vertices, but imposes at least \(2h\) order-edge requirements, losing at least one power of \(n\). If a connected group has one geometric edge and at least two *distinct* selected requirements, it imposes at least three order-edge requirements on two vertices; otherwise the constraints are contradictory. For any fixed mixed factorial moment, the number of combinatorial patterns is finite. Thus every mixed factorial moment tends to one. The multivariate factorial-moment criterion (equivalently, the probability-generating-function method near the origin) yields joint convergence to \(m\) independent \(\operatorname{Poisson}(1)\) variables. Accordingly, the presence indicators converge jointly to independent Bernoulli variables with success probability \(1-u\).

**2. A clean high-probability local normal form.** With probability tending to one, (a) all \(2k\) initial/terminal vertices of the individual paths are distinct; (b) no successor edge is shared by three orders; (c) distinct shared geometric edges have no common vertex; and (d) no shared edge touches an endpoint. For (a), endpoint collisions have probability \(O(k^2/n)\). For (b), a triple-overlap count has mean \(O(k^3/n)\). For (c), summing over pairs of candidate overlapping edges sharing a vertex gives \(O_k(n^{-1})\); each event imposes four directed-successor constraints on at most three vertices. For (d), fix one of the \(2k\) endpoints and use the same edge-counting bound conditionally. Every asserted error is \(O_k(n^{-1})\). Also \(\sum X_{ij}^{\pm}=O_{\mathsf P}(1)\), so all but \(O_{\mathsf P}(1)\) vertices are ordinary interior vertices.

For each vertex \(a\), write \(T(a)\) for the set of quantifier-free ordered-pair types realized by \((a,b)\) as \(b\) ranges over all vertices. Since \(n>2k+1\), the equality type and the type having no edge in either direction are present at every \(a\). An ordinary interior vertex has one pure outgoing and one pure incoming type for each \(S_i\). The initial or terminal vertex of \(S_i\), provided it is otherwise ordinary, has the corresponding incoming or outgoing type missing. There are always exactly \(2k\) such endpoint profiles. A vertex incident to one shared edge replaces two pure directed types (one from each participating order) by a single double-edge type. There are exactly two possible local profiles per overlap category \((i,j,+)\) or \((i,j,-)\), corresponding to the two endpoints of the shared edge. By cleanliness these are distinct from ordinary and endpoint profiles and from profiles of other categories. Consequently, the **set** of realized rooted pair-type profiles \(\{T(a):a\in[n]\}\) is, with probability tending to one, determined exactly by the \(m\)-bit vector \(B\) of overlap-category presence, regardless of the positive counts. Conversely, each bit of \(B\) can be read as existence of its corresponding double-edge pair type.

**3. Why rank two sees precisely these presence bits.** A formula \(\rho(x)\) of quantifier rank at most one in the two-variable language is determined at \(x=a\) by the set \(T(a)\): an innermost quantified variable tests the existence (or universal inclusion) of a quantifier-free ordered-pair type, and Boolean connectives preserve this property. Bound-variable shadowing and closed rank-one subformulas do not change the conclusion, since their truth is itself determined by the realized profiles. Hence a closed sentence of rank at most two is determined by the set of realized \(T(a)\)'s, by induction on its Boolean structure and outer quantifiers. On the clean event, its truth is therefore some Boolean function \(F_\varphi(B)\).

Every Boolean function of \(B\) is realized at quantifier rank two: the bits are the respective sentences
\[
\exists x\exists y\, (S_i(x,y)\wedge S_j(x,y)),\qquad
\exists x\exists y\,(S_i(x,y)\wedge S_j(y,x)),
\]
and arbitrary finite Boolean combinations preserve rank two.

**4. Spectrum and distinctness.** For a Boolean function on \(m\) independent Bernoulli\((1-u)\) bits, a vector with exactly \(j\) absent bits has probability \(u^j(1-u)^{m-j}\). Choosing a subset of accepting vectors gives the displayed expression with a coefficient \(a_j\) counting accepted vectors with \(j\) absent bits, where \(0\le a_j\le\binom mj\). Conversely, every allowed coefficient vector can be obtained by accepting any prescribed number of vectors in each Hamming layer. The polynomials \(u^j(1-u)^{m-j}\), \(0\le j\le m\), are linearly independent over \(\mathbb Q\) as polynomials in \(u\) (Bernstein basis). Since \(e^{-1}\) is transcendental, unequal integer coefficient vectors yield unequal real limits. Multiplying the independent numbers of coefficient choices gives the claimed exact cardinality.

## Verification

The standalone standard-library Python script `checker.py` directly enumerates every triple of independent paths for \(n=3,4,5\), after fixing the first path by label symmetry, representing \(36\), \(576\), and \(14{,}400\) equiprobable labelled configurations. It checks two independently implemented edge-overlap count routines, the six exact finite means \((n-1)/n\), and the full six-dimensional finite count distributions. It also verifies the explicit local-profile normal form on \(391\) randomly sampled *clean* three-order models on \(50\) vertices, and checks the spectrum cardinalities for \(k=1,2,3\). Output: `ALL_CHECKS_OK`. The infinitely many \(n\) assertion comes solely from the proof, not these finite experiments.

## Relationship to prior work

Jeż, Michaliszyn, and Witkowski (arXiv:2610.19943, first posted 2026-10-14) study finite satisfiability for exactly the same designated independent successor-path semantics, but allow extra relation symbols and focus on decision bounds rather than random structures or rank-two limiting probability spectra. Their Section 2 provides the path semantics used here. The related Michaliszyn–Witkowski preprint (arXiv:2610.09758) studies satisfiability of a similar signature, not asymptotic probabilities. Tóth and coauthors (arXiv:2608.10877) study weighted model counts for ordered domains but do not state this exact asymptotic spectrum for arbitrary fixed \(k\).

Classical combinatorics overlaps nontrivially: Diaconis, Evans and Graham, *Unseparated Pairs and Fixed Points in Random Permutations*, prove a one-permutation exact adjacency distribution and hence a single Poisson(1) limit. Bender and Canfield, *Intersections of Randomly Embedded Sparse Graphs are Poisson* (1999), prove a broad unmarked common-edge Poisson theorem. Those stronger *marginal* results already explain individual Poisson coincidences and are not claimed as new here. They do not state or imply purely by their displayed theorems the complete joint orientation-resolved \(k\)-order event law plus the exact rank-two logical spectrum and its cardinality. This distinction is substantive: marginal Poisson convergence alone would not establish independence of all overlap categories. Priority in uninspected probability/model-theory literature remains open.

## Limitations

The theorem concerns fixed \(k\), the pure successor/equality vocabulary, and quantifier rank at most two; there is no claim for first-order logic of unbounded rank, full order predicates, extra unary colours, or growing \(k\). It is not a finite-model enumeration formula. The proof's multivariate moment argument assumes that a fixed finite number of constraints is tested before \(n\to\infty\). Classical overlap results are acknowledged as prior results, not new consequences of this proof. Historical priority remains subject to further literature comparison.

## References

1. A. Jeż, J. Michaliszyn, P. Witkowski, *Finite Satisfiability of Two-Variable Logic with Arbitrarily Many Successors*, arXiv:2610.19943 (v1 submitted 2026-10-14), https://arxiv.org/abs/2610.19943.
2. J. Michaliszyn, P. Witkowski, *Two-Variable Logic with Arbitrarily Many Successor Relations*, arXiv:2610.09758 (2026-10-07), https://arxiv.org/abs/2610.09758.
3. J. Tóth et al., *Weighted First-Order Model Counting over Ordered Domains*, arXiv:2608.10877 (2026-08-11), https://arxiv.org/abs/2608.10877.
4. P. Diaconis, S. N. Evans, R. Graham, *Unseparated Pairs and Fixed Points in Random Permutations*, https://statistics.berkeley.edu/sites/default/files/tech-reports/unseparated_pairs.pdf.
5. E. A. Bender, E. R. Canfield, *Intersections of Randomly Embedded Sparse Graphs are Poisson*, Electron. J. Combin. 6 (1999), R36, doi:10.37236/1468.
