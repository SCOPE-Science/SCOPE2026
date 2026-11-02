# Parity-sharp VC and Littlestone dimensions of antihole geodesic convexity

## Finding

For each integer \(n\ge 7\), let \(G_n=\overline{C_n}\) be the simple graph on \(V=\mathbb Z/n\mathbb Z\) whose edges join exactly the pairs that are **not** consecutive in the standard cycle. Let \(\mathcal C_n\) consist of **all** vertex subsets that are geodesically convex in \(G_n\), including \(\varnothing\) and \(V\). Its hypotheses are evaluated by vertex-membership queries.

Then \(\mathcal C_n=\operatorname{Ind}(C_n)\cup\{V\}\), where \(\operatorname{Ind}(C_n)\) is the family of all independent vertex sets of the ordinary cycle. The entire polynomial enumerating VC-shattered supports is

\[
\Phi_n(z)=1+nz+\binom n2z^2+\sum_{k=3}^{\lfloor n/2\rfloor}\frac{n}{n-k}\binom{n-k}{k}z^k.
\]

Equivalently, if \(I(C_n;z)\) is the ordinary cycle independence polynomial, then \(\Phi_n(z)=I(C_n;z)+nz^2\). Thus **every** support of size at most two is shattered, and a support of size at least three is shattered exactly when it is an independent set of \(C_n\). Furthermore,

\[
\operatorname{VCdim}(\mathcal C_n)=\left\lfloor\frac n2\right\rfloor,
\qquad
\operatorname{Ldim}(\mathcal C_n)=\left\lceil\frac n2\right\rceil.
\]

In particular, the exact adaptive-minus-static difference equals one for odd \(n\) and zero for even \(n\). The graph order range \(n\ge7\) is essential to the convex-hypothesis classification; smaller complements are not covered by this theorem.

## Assumptions and scope

All graphs are finite, simple, undirected and unweighted. A subset \(S\) is geodesically convex if, for any \(u,v\in S\), it contains *every* vertex on *every* shortest \(u\)-\(v\) path. A support \(T\subseteq V\) is VC-shattered by a concept family \(\mathcal H\subseteq2^V\) if \(\{H\cap T:H\in\mathcal H\}=2^T\). Its Littlestone dimension is the largest depth of a complete binary tree whose internal nodes are vertex-membership queries and whose each root-to-leaf answer path agrees with at least one hypothesis; terminal hypotheses may vary with the leaf. Both dimensions refer to these exact conventions.

For a graph \(F\), \(\operatorname{Ind}(F)\) denotes **all** independent sets, not only maximal ones, and \(\alpha(F)\) is the maximum size of an independent set. The empty set is included. A path \(P_m\) has \(m\) vertices, including the empty path \(P_0\).

## Proof

**1. Convexity classification.** In \(G_n\), only consecutive cycle vertices are nonadjacent. They have graph distance two, and the common neighbors of \(0,1\) are exactly \(3,4,\ldots,n-2\). A geodesically convex set containing \(0,1\) therefore contains all of \(V\) except possibly \(2\) and \(n-1\). Since \(n\ge7\), it also contains the consecutive pairs \(3,4\) and \(4,5\). The pair \(3,4\) has \(n-1\) as a common neighbor in \(G_n\), and the pair \(4,5\) has \(2\) as a common neighbor. Their shortest paths force both missing vertices. Rotating indices shows that the geodesic hull of every nonedge of \(G_n\) is the full vertex set. Thus every proper convex set is a clique of \(G_n\), i.e. an independent set of \(C_n\). Conversely, every clique is geodesically convex (its internal pair distances are one), and the full set is convex. This establishes the classification.

**2. Static traces and counting.** If \(T\) is independent in \(C_n\), every subset of \(T\) belongs to \(\mathcal C_n\), so \(T\) is shattered. If \(|T|=2\), whether independent or not, the full-set hypothesis realizes both positives, the two singletons realize the one-positive traces, and the empty hypothesis realizes the zero trace. If \(|T|\ge3\) contains a consecutive cycle pair \(u,v\), only the full hypothesis contains both \(u,v\), and hence no hypothesis has trace exactly \(\{u,v\}\) on \(T\). This proves the characterization. For \(1\le k\le\lfloor n/2\rfloor\), counting the \(k\) positive cyclic gaps of sizes at least two gives

\[
|\{S\in\operatorname{Ind}(C_n):|S|=k\}|=\frac nk\binom{n-k-1}{k-1}=\frac{n}{n-k}\binom{n-k}{k}.
\]

There are exactly \(n\) nonindependent two-element supports, accounting for the extra \(nz^2\). A largest independent cycle support has size \(\lfloor n/2\rfloor\ge3\), proving the VC formula. The number of hypotheses is \(1+\sum_{k=0}^{\lfloor n/2\rfloor}[z^k]I(C_n;z)\).

**3. A general online bound.** For any finite graph \(F\), the hereditary concept class \(\operatorname{Ind}(F)\) has Littlestone dimension exactly \(\alpha(F)\). The lower bound follows by shattering a maximum independent set. For the upper bound, at any first query \(v\), the positive branch is equivalent to \(\operatorname{Ind}(F-N_F[v])\), with independent-set number at most \(\alpha(F)-1\); induction on the latter number completes the argument. More generally, take a family of independent subsets of \(F\) with any additional marker coordinates fixed negative, and add one exceptional hypothesis positive on all coordinates (including the markers). This augmented family has Littlestone dimension at most \(\alpha(F)+1\): on the all-positive path of a putative deeper tree, after \(\alpha(F)+1\) distinct positive vertex queries (or after any positive marker query), only the exceptional hypothesis survives, so the next query cannot split. A shattered tree cannot repeat a query on a root-to-leaf path.

**4. Augmented-path lemma.** Let \(\mathcal A_m\) have domain the vertices of \(P_m\) and one additional marker \(\star\). Its hypotheses are all independent subsets of \(P_m\) (marker negative) and one top hypothesis positive on all \(m+1\) coordinates. We claim, for every integer \(m\ge0\),

\[
\operatorname{Ldim}(\mathcal A_m)=\left\lfloor\frac m2\right\rfloor+1.
\]

For \(m=0\), there are two hypotheses separated by the marker, so the answer is one. If \(m=2a+1\) is odd, independent sets already shatter a support of size \(a+1\). To bound the dimension, consider the first queried path vertex \(i\), with vertices numbered \(1,\ldots,m\). If \(i\) is odd, the negative branch consists of independent sets of two disjoint even paths on \(i-1\) and \(m-i\) vertices, and hence has dimension \(a\). If \(i\) is even, the positive branch reduces to independent sets of paths on \(i-2\) and \(m-i-1\) vertices, both even, together with an exceptional top and marker coordinates; their combined independent-set number is \(a-1\), so its dimension is at most \(a\). A marker query has a singleton positive branch. In all cases the first split has one branch of depth at most \(a\), giving the upper bound \(a+1\).

If \(m=2a\ge2\) is even, querying a path vertex \(i\) leaves on the positive side independent sets of \(P_m-N[i]\) (whose independent-set number is at most \(a-1\)) plus one top, hence positive-branch dimension at most \(a\). A marker query has a singleton positive branch, so every first split gives the upper bound \(a+1\). For the lower bound query endpoint \(1\). The negative branch is \(\operatorname{Ind}(P_{2a-1})\) of dimension \(a\). The positive branch is \(\mathcal A_{2a-2}\) on vertices \(3,\ldots,2a\), with vertex \(2\) serving as a marker; the original marker is a duplicate, which does not change Littlestone dimension. By induction this positive branch also has dimension \(a\). A first query combining two depth-\(a\) branches proves depth \(a+1\). The lemma follows.

**5. Cycle online dimension.** For \(\operatorname{Ind}(C_n)\cup\{V\}\), any first query \(v\) has a negative branch \(\operatorname{Ind}(P_{n-1})\), of dimension \(\lceil(n-1)/2\rceil\). Its positive branch consists of independent subsets containing \(v\) plus the full hypothesis. The two cycle neighbors of \(v\) are negative in every proper surviving hypothesis and positive in the full one, acting as duplicate markers; the remaining vertices form \(P_{n-3}\). Therefore the positive-branch dimension is \(\lfloor(n-3)/2\rfloor+1\) by the lemma. Rotational symmetry makes this split computation independent of \(v\). The exact first-query recurrence is

\[
\operatorname{Ldim}(\mathcal C_n)=1+\min\left\{\left\lceil\frac{n-1}{2}\right\rceil,\left\lfloor\frac{n-3}{2}\right\rfloor+1\right\}=\left\lceil\frac n2\right\rceil.
\]

All equalities are for the complete binary-tree definition, not for a restricted deterministic query order.

## Verification

The standalone file `verify_antihole.py` implements a separate finite test: it reconstructs shortest-path distances on \(\overline{C_n}\), enumerates every convex vertex subset and every VC support for \(7\le n\le13\), and independently runs the exact version-space Littlestone recurrence for \(7\le n\le14\). It also verifies the augmented-path lemma for \(0\le m\le14\). Execute with Python 3 using `python3 verify_antihole.py` from the directory containing the file. The program prints `ALL_ANTIHOLE_GEODESIC_LEARNING_CHECKS_PASS` only if all assertions hold. No third-party packages or data files are required.

## Relationship to prior work

The setting of online learning of geodesically convex sets, general VC and mistake bounds, and the description of Littlestone dimension as the optimal adversarial mistake bound are treated in Thiessen and Gärtner (2022), particularly its Section 4 and Propositions 11, 12, and 15. Those propositions are more general but supply neither this antihole hypothesis classification nor its precise odd/even Littlestone values. Dourado and collaborators' graph-convexity survey (first public preprint in March 2022) surveys path-convexity and structural graph classes but does not establish the present exact antihole online-learning law. The cycle independence polynomial and its coefficients are classical: their appearance here is through the geodesic-convexity/shattering identification, not a claim of inventing that polynomial. Graph families and concepts on the ordinary cycle differ from those on its complement; the distinction is essential for the current theorem.

## Limitations

The theorem is restricted to \(n\ge7\); it asserts nothing about the smaller complements, whose hull structure changes. The result concerns geodesic convexity with all shortest paths and all convex subsets, not only geodesic halfspaces, induced-path convexity or open-neighborhood concepts. It does not address computational learning efficiency, private learning, or other graph families. Historical priority under other nomenclature for a universal top hypothesis adjoined to independent-set systems has not been conclusively established.

## References

1. M. Thiessen and T. Gärtner, *Online Learning of Convex Sets on Graphs*, ECML PKDD (2022), DOI `10.1007/978-3-031-26412-2_22`; accessible conference preprint: `https://ecmlpkdd-storage.s3.eu-central-1.amazonaws.com/preprints/2022/lncs13716/lncs13716354.pdf`.
2. M. C. Dourado, M. Gutierrez, F. Protti, R. Sampaio, and S. Tondato, *Characterizations of graph classes via convex geometries: a survey*, arXiv `2203.15878`, first posted 2022-03-29, `https://arxiv.org/abs/2203.15878`.
3. E. Kranakis, D. Krizanc, B. Ruf, J. Urrutia, and G. J. Woeginger, *The VC-dimension of set systems defined by graphs*, Discrete Applied Mathematics 77 (1997), 237–257, DOI `10.1016/S0166-218X(96)00137-0` (graph-defined set systems, not the current convexity family).
