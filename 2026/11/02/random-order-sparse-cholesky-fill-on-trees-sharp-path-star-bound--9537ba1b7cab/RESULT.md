# Random-order sparse Cholesky fill on trees: sharp path-star bounds and an exact path law

## Finding

**Theorem.** Let \(T=(V,E)\) be a tree on \(n\ge2\) vertices and let \(A\) be a real symmetric positive-definite \(M\)-matrix whose strictly negative off-diagonal entries occur exactly on the edges of \(T\). Choose an independent uniformly random permutation \(\pi\) of \(V\); use it as the row-and-column elimination order in exact unpivoted Cholesky. Write \(F_T\) for the number of distinct *new unordered off-diagonal positions* in the elimination fill graph, excluding the original tree edges.

For any nonadjacent vertices \(u,v\), with graph distance \(d=d_T(u,v)\),

\[
\Pr(\{u,v\}\text{ is a fill edge})=\frac{2}{d(d+1)}.
\]

Consequently,

\[
\mathbb E F_T=\sum_{\substack{\{u,v\}\subseteq V\\d_T(u,v)\ge2}}\frac{2}{d_T(u,v)(d_T(u,v)+1)},
\qquad
n+1-2H_n\le\mathbb E F_T\le\frac{(n-1)(n-2)}6,
\]

where \(H_n=\sum_{j=1}^n1/j\). For \(n\ge4\), equality holds on the left exactly for paths and on the right exactly for stars (up to graph isomorphism). For \(n=2,3\), the path and star are the same tree, so both bounds agree.

For the path \(P_n\), the entire distribution satisfies

\[
\boxed{\mathbb E z^{F_{P_n}}=\prod_{k=3}^{n}\frac{2+(k-2)z}{k}}.
\]

Here and below an empty product is \(1\). Thus \(F_{P_n}\) is *equal in distribution* to a sum of independent Bernoulli variables with probabilities \((k-2)/k\), for \(k=3,\ldots,n\); this representation is a distributional identity, not an independence assertion about individual elimination events. It follows that

\[
\mathbb EF_{P_n}=n+1-2H_n,\quad
\operatorname{Var}(F_{P_n})=2H_n-4H_n^{(2)}+2,
\quad H_n^{(2)}=\sum_{j=1}^n j^{-2},
\]

and

\[
\frac{F_{P_n}-(n+1-2H_n)}{\sqrt{2\log n}}
\xrightarrow{\mathrm d}N(0,1).
\]

In particular \(\Pr(F_{P_n}=0)=2^{n-1}/n!\) and \(\Pr(F_{P_n}=n-2)=2/[n(n-1)]\) for \(n\ge3\). For the star, \(F_{K_{1,n-1}}\) has the law of \(\binom K2\), where \(K\) is uniform on \(\{0,1,\ldots,n-1\}\). Its mean is \((n-1)(n-2)/6\).

## Assumptions and scope

The count is symbolic undirected fill: each newly introduced unordered pair is counted once, independently of how often a Schur-complement entry is updated. Equivalently it is the number of new strictly triangular factor positions, not the total floating-point operation count or both symmetric matrix entries. A sufficient concrete matrix is \(A=I+L_T\), with \(L_T\) the unit-weight tree Laplacian. More generally, the symmetric positive-definite \(M\)-matrix sign pattern ensures all graph-fill Schur updates have a definite nonzero sign, so there are no accidental numeric cancellations. No graph weights enter the formulas.

All randomness is from the uniformly chosen ordering; \(T\), \(A\), and \(n\) are fixed. An arbitrary deterministic *leaf-elimination order* yields zero fill for any tree, so the theorem quantifies the penalty of an unstructured random ordering rather than asserting unavoidable fill.

## Proof

**1. Pair inclusion criterion.** When eliminating a vertex, the surviving neighbors are joined into a clique, and no edge between two still-surviving vertices is subsequently deleted. Fix distinct nonadjacent \(u,v\), and let their unique tree path have \(d-1\) internal vertices. A fill edge between \(u,v\) occurs if and only if all these internal vertices precede both endpoints in the elimination order. This is the unique-path specialization of the standard elimination fill-path condition: if the condition holds, eliminate the internal path vertices in any order and the endpoints eventually become adjacent; conversely, any later-created adjacency has an original path with only earlier-eliminated interior vertices, and a tree admits only the indicated path. Restricting a uniform permutation to these \(d+1\) vertices produces a uniform relative ordering, so the endpoints must occupy the last two positions, in either order. The probability is \(2(d-1)!/(d+1)!=2/[d(d+1)]\). Since every nonedge appears at most once, linearity of expectation proves the displayed tree-distance sum.

**2. Sharp upper bound.** A tree has exactly \(n-1\) edges, hence \((n-1)(n-2)/2\) nonedges. The function \(2/[d(d+1)]\) is at most \(1/3\) for integer \(d\ge2\), with equality precisely at \(d=2\). Thus the upper bound follows. For \(n\ge4\), equality requires every nonadjacent pair to have distance two, i.e. tree diameter two; this characterizes the star.

**3. Sharp lower bound.** Define \(g(d)=2/[d(d+1)]\), decreasing on positive integers. Remove an arbitrary leaf \(v\) of \(T\); distances among remaining vertices are unchanged. Enumerate the distances from \(v\) to other vertices in nondecreasing order \(d_1\le\cdots\le d_{n-1}\). Because there is an initial segment of a path from \(v\) to a farthest vertex, \(d_j\le j\) for every \(j\) (if the maximum distance is shorter than \(j\), the inequality is automatic). Also \(d_1=1\). Therefore

\[
\mathbb EF_T-\mathbb EF_{T-v}=\sum_{j=2}^{n-1}g(d_j)
\ge\sum_{j=2}^{n-1}\frac{2}{j(j+1)}=1-\frac2n.
\]

Starting at \(n=2\), induction gives \(\mathbb EF_T\ge\sum_{m=3}^{n}(1-2/m)=n+1-2H_n\). Equality when \(n\ge4\) implies equality in every distance inequality, so all \(d_j=j\); in particular the distance from \(v\) to some vertex is \(n-1\), forcing \(T\) to be a path with \(v\) an endpoint. A path attains equality, proving uniqueness.

**4. Path distribution.** Label the path consecutively. Rank its vertices by elimination time, with a larger rank corresponding to later elimination. At the instant a path vertex is eliminated, the surviving path is again a path on the uneliminated vertices, and the eliminated vertex generates one fill edge if and only if it has at least one later-eliminated vertex on *each* side. Hence it generates no fill if it is a left-to-right maximum or a right-to-left maximum in the rank permutation. Let \(L\) and \(R\) be the numbers of these respective record maxima. Their only common member is the global maximum, and therefore

\[
F_{P_n}=n-(L+R-1)=n+1-L-R.
\]

For a uniform permutation of length \(m\), the number of left-to-right maxima has generating function \(A_m(z)=z(z+1)\cdots(z+m-1)/m!\), with \(A_0(z)=1\). One elementary proof inserts the largest value into the permutation: the first position introduces a record, and the other \(m-1\) insertion locations do not affect the number of left records; this gives the rising-factorial recurrence. The generating series is \(\sum_{m\ge0}A_m(z)u^m=(1-u)^{-z}\).

Condition on the location of the global maximum, uniformly one of the \(n\) positions. The relative permutations on the two sides are independent and uniform, and their record-maxima counts contribute \(L+R-1\) (with one deterministic record for the global maximum). Thus

\[
\mathbb E z^{L+R-1}=
\frac z n\sum_{j=0}^{n-1}A_j(z)A_{n-1-j}(z)
=\frac{z(2z)(2z+1)\cdots(2z+n-2)}{n!},
\]

using the coefficient of \(u^{n-1}\) in \((1-u)^{-2z}\). Substitution \(z\mapsto z^{-1}\) into \(z^n\mathbb E z^{-(L+R-1)}\), followed by polynomial simplification, gives \(\prod_{k=3}^n[2+(k-2)z]/k\). Each factor is the generating function of a Bernoulli variable with success probability \((k-2)/k\). The formulas for mean, variance and extreme probabilities follow by multiplying these factors. Since the variance is \(2\log n+O(1)\), while all Bernoulli summands are bounded, the Lindeberg theorem gives the stated normal limit.

**5. Star distribution.** If the center is eliminated when exactly \(K\) leaves remain, it creates all \(\binom K2\) leaf-leaf fill edges; subsequent eliminations create no additional distinct edges among them. The center's rank is uniformly distributed among \(n\) possible positions, so \(K\) is uniform on \(\{0,\ldots,n-1\}\). Averaging \(\binom K2\) produces the sharp upper-bound mean.

## Verification

The standalone Python standard-library verifier `verify.py` recomputes the fill graph by clique elimination, cross-checks path probabilities against every elimination order for \(2\le n\le8\), verifies formulas for all labelled trees through six vertices, and checks Cholesky Schur-complement signs and patterns on explicit rational positive-definite \(M\)-matrices. It also checks independent exact rational generating functions and the two extrema. The executed verifier reported `VERIFICATION_OK 258852 assertions`. These finite checks corroborate the proof but are not an exhaustive proof for unbounded \(n\).

## Relationship to prior work

The fill-path characterization is classical, developed in the sparse-elimination literature by Rose, Tarjan and Lueker; it is not asserted here as a new fill-in criterion. Scott and Tůma explain symbolic Cholesky and fill-path behavior, including dependence on ordering. Chen, Liang and Biros study approximate randomized Cholesky for SDD systems, but the algorithm samples clique edges and differs from the exact random-order experiment here. The path calculation reduces to the established combinatorics of left-to-right and right-to-left record maxima, for which Jin gives broader joint generating-function results; neither basic record statistics nor general fill paths are claimed as original. The combined distance-weighted tree formula, sharp tree-class extrema and explicit numerical-factorization interpretation are the substantive claim; the path law is supplied as an exact specialization and benchmark. The relationship may be more implicit in earlier specialized sources than was possible to establish from accessible material.

## Limitations

Uniform random ordering may be far inferior to well-designed leaf or fill-reducing orders. The theorem does not evaluate arithmetic operation counts, finite-precision cancellation outside the stated sign class, arbitrary cyclic graphs, sampling-based approximate Cholesky, or higher-order statistics of fill on general trees. Stronger formulae from classical record theory already encompass part of the path calculation; publication-priority assessment of the complete package remains qualified, and no independent scientific audit is claimed.

## References

1. D. J. Rose, R. E. Tarjan, and G. S. Lueker, “Algorithmic Aspects of Vertex Elimination on Graphs,” *SIAM Journal on Computing* 5 (1976), 266–283. https://doi.org/10.1137/0205021
2. J. A. Scott and M. Tůma, “Sparse Cholesky Solver: The Symbolic Phase,” in *Algorithms for Sparse Linear Systems* (2023), Chapter 4. https://doi.org/10.1007/978-3-031-25820-6_4
3. C. Chen, T. Liang, and G. Biros, “RCHOL: Randomized Cholesky Factorization for Solving SDD Linear Systems,” initial public preprint 16 November 2020, arXiv:2011.07769v1. https://arxiv.org/abs/2011.07769
4. E. Y. Jin, “Symmetric generating functions and Euler-Stirling statistics on permutations,” initial public preprint 17 October 2022, arXiv:2210.08789v1. https://arxiv.org/abs/2210.08789
