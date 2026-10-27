# Exact Littlestone dimension of triangular-graph open neighborhoods

## Finding

For every integer \(n\ge 2\), let \(T_n=L(K_n)=J(n,2)\) be the *triangular graph*. Its vertex set is \(X_n=\binom{[n]}2\); distinct vertices are adjacent if and only if their two-element subsets intersect in exactly one point. Define the Boolean concept class
\[
\mathcal H_n=\{h_e:e\in X_n\},\qquad
h_e(q)=\mathbf 1[|e\cap q|=1].
\]
In particular, \(h_e(e)=0\): these are **open**, not closed, neighborhoods. Its exact Littlestone dimension is
\[
\boxed{\operatorname{Ldim}(\mathcal H_n)=
\begin{cases}
0,&n=2,\\
1,&n\in\{3,4\},\\
3,&n\in\{5,6\},\\
4,&n\ge7.
\end{cases}}
\]
Thus the optimal worst-case number of mistakes in realizable deterministic online learning of these neighborhoods is four for every \(n\ge7\), although there are \(\binom n2\) potential edge-indexed hypotheses. The exceptional jump from one to three at \(n=5\), and stabilization at \(n=7\), are both sharp.

## Assumptions and scope

The parameter \(n\) is an arbitrary integer at least two. The query domain and the hypothesis index set are both the unordered edges of \(K_n\). A depth-\(d\) Littlestone tree is a full binary tree of depth \(d\) whose internal nodes carry edge queries, with each of its \(2^d\) paths realized by at least one *single* function \(h_e\). Distinct indices are allowed to define identical functions; the dimension concerns the functions, not their multiplicity. The empty tree has depth zero. No randomness, computational restriction, or distributional assumption is imposed.

For any finite version space \(V\) of these functions, denote its dimension by \(L(V)\). Splitting a query \(q\) into \(V_0(q)\) and \(V_1(q)\) gives the standard recurrence
\[
L(V)=\max_{q:\,V_0(q),V_1(q)\ne\varnothing}
\left(1+\min\{L(V_0(q)),L(V_1(q))\}\right),
\]
with value zero when no query separates the remaining functions. For a version space with at most \(m\) distinct functions, \(L(V)\le\lfloor\log_2m\rfloor\). Both facts follow directly from the definition of shattered binary trees.

## Proof

**1. A four-round upper bound for all \(n\).** Fix a first query \(q=\{a,b\}\), and put \(R=[n]\setminus\{a,b\}\). The positive version space is indexed by
\[
P=\{\{a,i\},\{b,i\}:i\in R\}.
\]
We show \(L(P)\le3\), independently of the size of \(R\).

First consider a family of the form
\[
F=\{\{a,j\}:j\in R\setminus\{i\}\}\cup\{\{b,i\}\},
\]
with \(a,b\notin R\) distinct and \(i\in R\). **Claim: \(L(F)\le2\).** For any query \(q\), either all hypotheses in \(F\) give the same answer, or one answer retains at most three indexed hypotheses:

* If \(q=\{a,b\}\), every answer is positive.
* If \(q=\{a,k\}\) with \(k\in R\), either \(k=i\) and all answers are positive, or the negative answer retains precisely \(\{a,k\}\) and \(\{b,i\}\).
* If \(q=\{b,k\}\) with \(k\in R\), either \(k=i\) and all answers are negative, or the positive answer retains precisely \(\{a,k\}\) and \(\{b,i\}\).
* If \(q\subseteq R\) has size two, the positive answer retains at most two members of the star plus possibly \(\{b,i\}\), hence at most three.

No child containing at most three functions can support a depth-two full binary tree, because such a tree needs at least four distinct functions. Hence no query can support a depth-three tree on \(F\), proving the claim.

Now consider any query on \(P\). The query \(\{a,b\}\) does not split \(P\). A query \(\{a,i\}\) with \(i\in R\) splits \(P\) into two families each of the just-proved star-plus-one form (one uses \(a\), the other \(b\)), so both children have dimension at most two. The analogous statement holds for queries \(\{b,i\}\). Finally, a query \(\{i,j\}\subseteq R\) has exactly four positive hypotheses in \(P\), namely \(\{a,i\},\{a,j\},\{b,i\},\{b,j\}\), so its positive child has dimension at most two. Thus every informative query on \(P\) has some child of dimension at most two, giving \(L(P)\le3\).

Every depth-five tree on \(\mathcal H_n\) would require a depth-four tree after both labels of its first query. The positive label has dimension at most three, a contradiction. Therefore \(\operatorname{Ldim}(\mathcal H_n)\le4\) for all \(n\).

**2. Exceptional upper bounds.** For \(n=2\) there is only one function. For \(n=3\) there are at most three, so the dimension is at most one. For \(n=4\), the two complementary edges of \(K_4\) have identical open-neighborhood functions: the query equal to either is adjacent to neither, while every other query is adjacent to both. The six edges therefore give only three distinct functions, so the dimension is at most one. For \(n=5,6\), there are respectively ten and fifteen indexed hypotheses; each is fewer than sixteen, hence the dimension is at most three.

**3. A depth-three tree at \(n=5\).** Use the vertex names \(0,1,2,3,4\) and abbreviate \(\{i,j\}\) by \(ij\) in the following *query descriptions only*. Choose query \(01\) at the root. On its positive branch the surviving hypotheses are \(\{02,03,04,12,13,14\}\). Query \(02\), obtaining the children \(\{03,04,12\}\) and \(\{02,13,14\}\). Query \(03\) in each child; its two answers are nonempty in both cases. On the root's negative branch the hypotheses are \(\{01,23,24,34\}\). Query \(23\), obtaining children \(\{24,34\}\) and \(\{01,23\}\). Queries \(02\) and \(04\), respectively, split these two pairs. Thus every one of the eight root-to-leaf paths is realized. This proves \(\operatorname{Ldim}(\mathcal H_5)=3\).

Whenever \(m\le n\), restricting hypotheses and queries to the edges of a fixed \(K_m\subseteq K_n\) preserves every adjacency label, so \(\operatorname{Ldim}(\mathcal H_m)\le\operatorname{Ldim}(\mathcal H_n)\). Consequently, the dimension is at least three for all \(n\ge5\). The upper bound in step 2 settles \(n=5,6\).

**4. A depth-four tree for every \(n\ge7\).** Again query \(ab\) at the root and let \(R=[n]\setminus\{a,b\}\), which now has at least five points. The negative branch contains all edge hypotheses on \(R\); choosing five points of \(R\) embeds the depth-three tree from step 3, so this branch has dimension at least three.

The positive branch is the family \(P\) from step 1. Choose \(i\in R\) and query \(\{a,i\}\). On the positive branch of this second query are all \(\{a,j\}\) with \(j\in R\setminus\{i\}\), and on its negative branch are all \(\{b,j\}\) with \(j\in R\setminus\{i\}\). Each contains a star with at least four spokes. Any four-spoke star supports a depth-two tree: a query connecting two spoke endpoints divides the four star hypotheses two against two, and then querying the appropriate spoke itself distinguishes the hypotheses in either pair. Hence the positive branch of the root has dimension at least three. Both branches of the root therefore admit depth-three trees; \(\mathcal H_n\) admits a depth-four tree. Combined with step 1, this proves the formula for every \(n\ge7\).

**5. Remaining lower bounds.** For \(n=3\) or \(4\) there are at least two distinct open-neighborhood functions, so a depth-one tree exists. For \(n=2\), the unique function has dimension zero. All cases are complete.

## Verification

The standalone Python 3 program `verify_triangular.py` implements a direct version-space recursion from the full incidence matrix and compares exact computed dimensions with the theorem for every \(2\le n\le11\). It separately checks two explicit complete shattered-tree certificates stored in `witness_trees.json`: a depth-three tree for \(n=5\) and a depth-four tree for \(n=7\). For every leaf it independently recomputes the membership labels of the named witnessing edge along the complete path, checking all eight and sixteen leaf paths respectively. The recorded run `verification_output.txt` terminates with `ALL_CHECKS_PASS`.

To replay from these files using the Python standard library, run `python3 verify_triangular.py --check witness_trees.json`. The exact computation is a finite stress test only. The all-\(n\) conclusion follows from the proof above; the transcript is not a proof for infinitely many \(n\).

## Relationship to prior work

The 2020 preprint of Adler, Benediktsson and Macpherson studies *exactly the same Johnson-graph open-neighborhood set systems* but computes VC dimension and VC density, not Littlestone dimension. In particular, its \(J(7,2)\) VC-shattering witness **already implies the lower bound** \(\operatorname{Ldim}(\mathcal H_n)\ge4\) for all \(n\ge7\). That published result does **not** imply the dimension-four upper bound or the exact smaller-parameter values: generally \(\operatorname{VCdim}\le\operatorname{Ldim}\), without an upper implication. Its Johnson-graph adjacency definition directly matches this finding's object, so it is the closest paper checked.

Ghazi, Golowich, Kumar and Manurangsi (2020/2021) establish general Littlestone-dimension closure bounds under Boolean aggregation; these are not exact ranks for the triangular-graph adjacency relation. Malliaris and Moran (2021) identify finite Littlestone dimension with stable behavior and study excellent sets, but do not determine the present finite Johnson-graph dimensions. Existing results on the topology of neighborhood complexes of triangular graphs concern different invariants; shared graph notation and a threshold near seven do not imply the stated online-shattering result. A search and comparison of equivalently named graph families (triangular graphs, Johnson graphs \(J(n,2)\), and line graphs \(L(K_n)\)) found no checked result stating or logically implying this four-case formula; historical priority beyond the inspected sources is not certified.

## Limitations

The statement is restricted to **open** neighborhoods of the complete-graph line graph, i.e. Johnson level two. Closed neighborhoods, higher Johnson levels, arbitrary induced subgraphs, other graph families, and randomized/agnostic learning are not classified. The bound four is for deterministic realizable online mistakes; it is not a bound for other error models. The finite calculations do not establish the infinite-family theorem independently of the structural argument. No independent scientific audit or exhaustive global publication-priority search has been performed.

## References

1. I. Adler, B. G. Benediktsson and D. Macpherson, *Vapnik-Chervonenkis Dimension and Density on Johnson and Hamming Graphs*, arXiv:2007.16042, first public July 31, 2020; subsequently *Discrete Applied Mathematics* 312 (2022), 29–44. https://arxiv.org/abs/2007.16042
2. B. Ghazi, N. Golowich, R. Kumar and P. Manurangsi, *Near-tight Closure Bounds for the Littlestone and Threshold Dimensions*, arXiv:2007.03668, first public July 7, 2020; *Proceedings of Machine Learning Research* 132 (2021), 686–696. https://arxiv.org/abs/2007.03668
3. M. Malliaris and S. Moran, *Agnostic Online Learning and Excellent Sets*, arXiv:2108.05569, first public August 12, 2021; later revisions under *Model Theory and Agnostic Online Learning via Excellent Sets*. https://arxiv.org/abs/2108.05569
