# The six-vertex entropy obstruction for online learning of rooted-tree ideals

## Finding
For a finite rooted tree \(T\), order its vertices by ancestry and let \(\mathcal I(T)\) be all order ideals. A membership query asks whether a particular vertex belongs to the unknown ideal. The usual cardinality (entropy) upper bound is
\[
\operatorname{Ldim}(\mathcal I(T))\le E(T):=\lfloor\log_2|\mathcal I(T)|\rfloor.
\]
The bound is attained by **every** rooted tree having at most five vertices. It is attained by eighteen of the twenty rooted isomorphism types on six vertices. Precisely two exceptional shapes first obstruct equality:

| Canonical rooted shape | Number of ideals | Littlestone dimension | Entropy upper bound |
|---|---:|---:|---:|
| `((()())(()))` | 16 | 3 | 4 |
| `((())(())())` | 19 | 3 | 4 |

Canonical shapes encode the root as a pair of parentheses containing, in sorted order, the encodings of the child subtrees; `()` denotes a single vertex. The first exceptional root has a three-vertex two-leaf fork and a two-vertex chain as children. The second has two two-vertex chains and one leaf as children.

Moreover, for each integer \(s\ge1\), adjoining a new common minimum below \(s\) disjoint copies of the first exceptional rooted tree produces a **connected rooted tree** \(R_s\) with \(1+6s\) vertices and
\[
|\mathcal I(R_s)|=1+16^s,\quad E(R_s)=4s,\quad
3s\le\operatorname{Ldim}(\mathcal I(R_s))\le3s+1.
\]
Consequently its entropy deficit is at least \(s-1\) and tends to infinity.

## Assumptions and scope
All graphs are finite, undirected, simple, and rooted. The associated poset has \(u\le v\) precisely when \(u\) is an ancestor of \(v\), including equality. An ideal is an ancestor-closed vertex set; the empty set is included. The Littlestone dimension is the maximum depth of a complete binary membership-query decision tree such that every root-to-leaf answer sequence is realized by some ideal. The value for any nonempty singleton concept class is zero. \(E(T)\) is a *bound based solely on concept count*, not the optimal number of queries required to identify an ideal. The six-vertex classification is a sharp finite cutoff, not a claim about all larger tree shapes. The infinite-family result asserts an interval for its Littlestone dimension, not an exact formula.

## Proof
**1. Elementary dimension principles.** For a finite nonempty concept class \(C\), let \(C_0(v)\) and \(C_1(v)\) be its restrictions to concepts assigning vertex \(v\) the indicated label. The exact recurrence is
\[
\operatorname{Ldim}(C)=\max_{v:C_0(v),C_1(v)\ne\varnothing}
\bigl(1+\min\{\operatorname{Ldim}(C_0(v)),\operatorname{Ldim}(C_1(v))}\bigr),
\]
with maximum of the empty set defined as zero. Each depth-\(d\) shattered tree requires at least \(2^d\) distinct concepts; hence \(\operatorname{Ldim}(C)\le\lfloor\log_2|C|\rfloor\). If \(C,D\) have disjoint query domains, induction in the recurrence gives
\(\operatorname{Ldim}(C\times D)=\operatorname{Ldim}(C)+\operatorname{Ldim}(D)\): one direction concatenates optimal trees, and the other splits on whichever factor contains the first query. Adjoining one concept raises Littlestone dimension by **at most one**: if the enlarged class shatters depth \(d\), the root child not containing the newly added concept shatters depth \(d-1\) using the old class.

**2. Exact finite exhaustion.** All rooted trees up to six vertices are generated independently by (i) all Prüfer sequences for labeled unrooted trees, with every possible distinguished root, and (ii) all recursive parent arrays, with each nonroot parent carrying a smaller label. Every rooted finite tree admits such a parent labeling. A recursively sorted parenthesis code identifies rooted isomorphism types, giving by order \(n=1,2,3,4,5,6\) the exact counts \(1,1,2,4,9,20\). For each representative, enumerating the \(2^n\) vertex subsets and checking ancestor closure gives \(\mathcal I(T)\). Two independent algorithms compute its exact dimension: a memoized max–min recurrence on subsets of concepts and a depth-by-depth feasibility predicate for complete mistake trees. Both enumerations and algorithms agree for all **37** rooted types through six vertices. The full output `rooted_census.tsv` shows equality with \(E(T)\) on all seventeen types through five vertices and on precisely eighteen of twenty six-vertex types. Because both tree generations are exhaustive and every dimension computation follows the exact recurrence, this verifies the finite assertion, rather than extrapolating from samples. Full standard-library executable source is `verify_rooted_entropy.py`.

**3. Direct proofs for the two exceptions.** Let \(F\) be a three-vertex rooted fork, and \(L\) a two-vertex rooted chain. The class \(\mathcal I(F)\) has five concepts and Littlestone dimension two; \(\mathcal I(L)\) has three and dimension one (directly by their small membership trees). The first exceptional rooted tree has \(1+5\cdot3=16\) ideals; conditioning on inclusion of its root produces \(\mathcal I(F)\times\mathcal I(L)\), of dimension three. On its six possible first queries the numbers of positive concepts are \(15,12,10,6,6,5\). None is eight, so none divides sixteen concepts into two groups large enough for a depth-four shattered tree. Its dimension is therefore exactly three.

For the second exceptional rooted tree the three rooted child components are \(L,L\), and a singleton. It has \(1+3\cdot3\cdot2=19\) ideals and contains a root-present product subfamily of dimension \(1+1+1=3\). First-query counts are eighteen at the global root, twelve at either chain top, six at either chain bottom, and nine at the singleton leaf. A depth-four shattered tree requires at least eight concepts in *both* first-query branches. Only the singleton-leaf query passes this cardinality test, but its positive branch is exactly \(\mathcal I(L)\times\mathcal I(L)\), of Littlestone dimension two, so even this query cannot root a depth-four tree. Thus its dimension is exactly three.

**4. Connected unbounded deficit.** Let \(R_s\) be formed by introducing a new least vertex below \(s\) disjoint copies of the first exceptional tree. The empty ideal is the unique ideal missing the new root. Every ideal including it corresponds independently to an ideal in each six-vertex component. Hence \(|\mathcal I(R_s)|=1+16^s\), and \(E(R_s)=4s\). The root-present subfamily is a product of \(s\) classes each of Littlestone dimension three, so it has dimension \(3s\). Adding the one missing-root concept can raise the dimension by at most one. Thus \(3s\le\operatorname{Ldim}(\mathcal I(R_s))\le3s+1\). For \(s\ge2\) the deficit is at least \(s-1\), and the connected tree sizes increase as \(1+6s\).

## Verification
From this package, run `python verify_rooted_entropy.py` with the working directory containing the script. It writes `rooted_census.tsv` and prints exactly the seven lines stored in `rooted_checks.txt`. It uses no third-party dependencies. The Prüfer enumerator visits every labeled tree and all roots; the recursive-parent generator independently covers every rooted isomorphism type. Different dimension solvers give the same dimensions for all 37 types. The two exceptional root-branch proofs and the product argument above additionally check the pivotal conclusions symbolically. Logs by themselves are not substitutes for these reasoning steps.

## Relationship to prior work
Manurangsi and Rubinstein (2017) develop the explicit-matrix setting and general computational complexity of VC and Littlestone dimensions, not this restricted enumeration. Walker (2022) studies decision-tree leaf structures and generalized Sauer–Shelah bounds, not ancestry-closed ideals of rooted posets. Thiessen and Gärtner (2022) study online learning of geodesically convex sets and halfspaces of graphs, with structural mistake bounds; the present order-ideal family is a different, more tightly constrained concept class, and their graph-convexity results do not state the two rooted six-vertex exceptions. Earlier work by Gärtner and Garriga (2007) considers online learning of directed cuts with path-cover parameters; it is relevant background, but not a claim to priority over that paper. Existing exact results on ideals of finite weak orders and two-chain interleavings concern different poset families and do not imply the rooted-tree cutoff. The evidence establishes a specific comparison, **not absolute historical uniqueness**.

## Limitations
Minimality and exact classification are proved only through six vertices using finite exhaustive computation. The connected infinite family has bounds, not a stated exact Littlestone dimension. The supporting prior-art search was limited to reachable sources; work on directed cuts or online monotone predicates outside the inspected sources might contain equivalent statements. Independent mathematical audit has not been performed.

## References
1. P. Manurangsi and A. Rubinstein, *Inapproximability of VC Dimension and Littlestone's Dimension*, arXiv:1705.09517v1 (first public version May 26, 2017); COLT 2017. https://arxiv.org/abs/1705.09517.
2. R. Walker, *Tree Dimension and the Sauer–Shelah Dichotomy*, arXiv:2203.12211 (first public March 23, 2022). https://arxiv.org/abs/2203.12211.
3. M. Thiessen and T. Gärtner, *Online Learning of Convex Sets on Graphs*, ECML PKDD 2022, DOI 10.1007/978-3-031-26412-2_22. https://ecmlpkdd-storage.s3.eu-central-1.amazonaws.com/preprints/2022/lncs13716/lncs13716354.pdf.
4. T. Gärtner and G. C. Garriga, *The Cost of Learning Directed Cuts*, ECML 2007, DOI 10.1007/978-3-540-74958-5_17 (background, earlier than the focal source window).
