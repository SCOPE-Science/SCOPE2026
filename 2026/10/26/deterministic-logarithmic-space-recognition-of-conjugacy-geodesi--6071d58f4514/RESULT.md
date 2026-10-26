# Deterministic logarithmic-space recognition of conjugacy geodesics in free inverse monoids

## Finding

**Theorem.** Fix an integer \(r\geq 1\) and the standard symmetric generating alphabet of the free inverse monoid \(\mathrm{FIM}_r\). There is a deterministic logarithmic-work-space algorithm which, given any input word \(w\) of length \(n\), outputs in binary the minimum length of a word representing an element \(i\)-conjugate to the element represented by \(w\). Consequently the conjugacy-geodesic language \(\mathrm{ConjGeo}(\mathrm{FIM}_r)\) is in deterministic \(\mathrm{L}\).

More explicitly, let \(g_i\) be the freely reduced group element represented by the prefix of \(w\) of length \(i\), for \(0\leq i\leq n\). Let \(T\) be the union of edges traversed by the prefix walk in the free-group Cayley tree, with \(E\) distinct undirected edges, and let \(d_T\) denote its graph distance. Define
\[
M(w)=\max\bigl\{d_T(g_i,g_j):0\leq i,j\leq n,\quad g_0^{-1}g_i=g_n^{-1}g_j\text{ in the free group}\bigr\}.
\]
The set is nonempty: \((i,j)=(0,n)\) is admissible. The conjugacy-class minimum equals \(2E-M(w)\); all three integers \(E,M(w),2E-M(w)\) can be computed in deterministic logarithmic work space. For \(r\geq2\), combining this algorithmic upper bound with the previously proved non-context-freeness and non-co-context-freeness gives \(\mathrm{ConjGeo}(\mathrm{FIM}_r)\in\mathrm{L}\) although this language belongs to neither of those two grammar classes.

The displayed extremal *geometric formula* is already implicit in the earlier Munn-tree conjugacy criterion and in the prior root-shift observation. The contribution asserted here is the rigorous deterministic-logarithmic-space implementation of that extremum, without explicitly materializing a Munn tree or storing reduced prefixes.

## Assumptions and scope

The alphabet consists of \(r\) free generators and their formal inverses; \(r\) is fixed (not part of the input). The input tape is read-only and may be rescanned; binary indices and counters use writable work tape. We use the conventional definition of \(\mathrm{L}\) with \(O(\log(n+2))\) work cells. By \(i\)-conjugacy we mean the natural conjugacy relation on inverse monoids used in Carvalho--Monteiro (2026). This is not a statement about other non-equivalent semigroup conjugacy relations. All distances and lengths are in the unweighted standard generating alphabet.

The Munn tree is represented inside the left Cayley graph of the free group on the same generators. It has vertex set \(\{g_0,\ldots,g_n\}\), contains each successive edge \(\{g_{k-1},g_k\}\), and is a finite tree. Each vertex has a prefix occurrence, so two vertex variables can always be named by indices between \(0\) and \(n\), even if several indices denote one vertex. Distances satisfy \(0\leq d_T\leq E\leq n\). The empty word has \(E=M=0\) and is handled by the same rule.

## Proof

**1. Geometric minimum.** Fix any two vertices \(s,t\) of \(T\). Every walk starting at \(s\), ending at \(t\), and covering every edge of \(T\) traverses an edge on the unique \(s\)-to-\(t\) path at least once and every other edge at least twice. Conversely, depth-first traversals of branches off the unique \(s\)-to-\(t\) path attain equality. Thus the minimum walk length between those roots, while covering the entire finite tree, is precisely \(2E-d_T(s,t)\). In the Munn-tree representation these walks are exactly words representing the corresponding element of the free inverse monoid.

The cited \(i\)-conjugacy theorem characterizes conjugates by keeping the same underlying labelled Munn tree and simultaneously shifting its initial and final roots from \((g_0,g_n)\) to \((s,t)\), with the labels of the simple paths from \(g_0\) to \(s\) and from \(g_n\) to \(t\) equal as elements of the free group. Writing \(s=g_i,t=g_j\), this equality is exactly \(g_0^{-1}g_i=g_n^{-1}g_j\). Each allowed root pair therefore determines a conjugate, and every conjugate determines such a pair. Minimizing \(2E-d_T(s,t)\) over the allowed pairs yields \(2E-M(w)\), with no approximation and for every input length.

**2. A logarithmic-space equality primitive.** For fixed free rank the free-group word problem is in deterministic logarithmic space, by the classical linear-group word-problem theorem. For two prefix occurrences \(g_i,g_j\), equality \(g_i=g_j\) can therefore be decided in logarithmic space on the virtual word consisting of the inverse of the first prefix followed by the second prefix. Similarly, equality of products of a constant number of such prefixes and inverse prefixes, including \(g_0^{-1}g_i=g_n^{-1}g_j\), is a deterministic logarithmic-space predicate. A virtual input symbol can be fetched by a logarithmic-space indexed scan of the original input. Standard closure under logarithmic-space reductions applies; no reduced word needs to be stored. The word lengths supplied to the primitive are at most a constant multiple of \(n\).

**3. Counting distinct tree edges.** Number the original word's steps by \(1,\ldots,n\). Let \(e_k\) be the undirected edge with endpoints \(g_{k-1},g_k\). To determine if \(e_k=e_l\), compare the endpoint pairs either in the same or reversed orientation, using four applications of the equality primitive. Call a step \(k\) a *first occurrence* if \(e_k\ne e_l\) for all \(l<k\). Testing this property by iterating \(l\), and then counting the first occurrences as \(k\) increases, computes \(E\). Only \(k,l\), a fixed number of flags, and an integer counter up to \(n\) are maintained. Hence \(E\) is logarithmic-space computable.

**4. Computing distance without reduced paths.** Fix any two prefix indices \(i,j\), and assume initially \(i\le j\). Their intervening input segment is a walk along the edges \(e_{i+1},\ldots,e_j\), starting at \(g_i\) and ending at \(g_j\). In *any* tree, the number of crossings of a fixed undirected edge by this walk is odd if and only if the edge separates its endpoints. Therefore \(d_T(g_i,g_j)\) equals the number of *distinct* tree edges which occur an odd number of times in the intervening segment. To calculate this, iterate over the first-occurrence indices \(k\) from step 3. For each such \(k\), scan \(l=i+1,\ldots,j\) and toggle a parity bit whenever \(e_l=e_k\). Increment a distance counter when the parity is odd. If \(i>j\), reverse their order before scanning. Each scan uses only indices, a parity bit, and counters of \(O(\log(n+2))\) bits. This yields the exact distance \(d_T(g_i,g_j)\) in deterministic logarithmic space even when the input revisits vertices arbitrarily often.

**5. Root-shift maximization and recognition.** Enumerate all \((n+1)^2\) pairs \((i,j)\). Use step 2 to test \(g_0^{-1}g_i=g_n^{-1}g_j\). For every admissible pair compute the distance via step 4 and update a counter storing the largest distance seen. This computes \(M(w)\); the pair \((0,n)\) ensures the maximum exists. All outer and nested loop indices, counters, and the finitely many equality-predicate simulations consume \(O(\log(n+2))\) work space: they are invoked sequentially and their work tapes can be reused. Calculate \(2E-M(w)\) with binary integer arithmetic, and accept \(w\) precisely if \(n=2E-M(w)\). This proves both assertions. The enumeration may take polynomially many rescans; no linear-time bound is claimed.

## Verification

The included `VERIFY.py` exhaustively enumerates all 5,461 words of length at most six over the two-generator symmetric alphabet and groups them by canonical unrooted labelled Munn-tree shape. It directly computes the shortest representative among each word's permitted conjugates **by independent enumeration** and checks equality against the formula from the theorem. The recorded output is

```text
VERIFY_OK rank=2 exhaustive_word_length<= 6 tested_words= 5461 distinct_shape_classes= 986 geodesics_shortened_by_conjugacy= 32
SAMPLE_SHORTENING ('aAbaA', 3, 5, 3, 3)
```

Run `python3 VERIFY.py` from the directory containing this file. The script intentionally uses explicit sets and lists: it verifies finite cases and **is not a logarithmic-space implementation**. The general resource bound follows from the indexed-edge/parity algorithm in the proof, not from those experiments. The example `aAbaA` has conjugacy-class minimum three although the word is an ordinary geodesic of length five.

## Relationship to prior work

Carvalho and Monteiro (arXiv:2608.10379, first posted 2026-08-11), Theorem 2.4 and Remark 3.4, give respectively the underlying root-shift conjugacy characterization and the geometric criterion for conjugacy geodesics. Their Theorems 3.5--3.6 establish non-context-freeness and non-co-context-freeness in rank at least two. In particular the combinatorial extremum here is **not** claimed as a new geometric theorem. Our claim is an explicit deterministic logarithmic-work-space upper bound for evaluating that extremum and deciding its associated language, not stated in the inspected manuscript.

Araújo, Kinyon and Konieczny (arXiv:1810.03208, 2018 preprint/2019 paper) establish free-inverse-semigroup conjugacy decision and the geometric criterion (cited as Theorem 7.9 by the 2026 paper), but the inspected conjugacy algorithm enumerates canonical conjugates rather than asserting this space bound. Diekert, Kausch and Lohrey (arXiv:1201.3174) treat logarithmic-space word and normal-form problems for groups and free partially commutative inverse monoids, not these conjugacy-minimal representative languages. Bodart, Carvalho and Monteiro (arXiv:2609.35251) classify several Green-relation geodesic languages, which are *different equivalence relations*. Together these results supply mathematical ingredients and context but do not state the proved conjunctive algorithmic result in the inspected materials.

## Limitations

The rank \(r\) is fixed; no uniform complexity in a rank encoded as part of input is asserted. There is no assertion of a time-optimal algorithm or of \(\mathrm{L}\)-hardness, no enumeration of shortest conjugates, and no claim about other notions of conjugacy. The geometric Munn-tree minimum is inherited from existing structural results; the new assertion is the space complexity. The experimental certificate covers only rank two and input lengths at most six. Literature comparison is bounded and cannot exclude an unindexed equivalent logarithmic-space algorithm. Independent audit and external validation have not been performed.

## References

1. A. Carvalho and A.-C. C. Monteiro, *Conjugacy languages in free inverse monoids*, arXiv:2608.10379, first posted 2026-08-11. https://arxiv.org/abs/2608.10379
2. J. Araújo, M. Kinyon and J. Konieczny, *Conjugacy in inverse semigroups*, arXiv:1810.03208 (2018 preprint; 2019 journal version). https://arxiv.org/abs/1810.03208
3. C. Bodart, A. Carvalho and A.-C. C. Monteiro, *Green languages and growth of free inverse monoids*, arXiv:2609.35251, first posted 2026-09-28. https://arxiv.org/abs/2609.35251
4. V. Diekert, J. Kausch and M. Lohrey, *Logspace Computations in Coxeter Groups and Graph Groups*, arXiv:1201.3174 (2012). https://arxiv.org/abs/1201.3174
5. R. J. Lipton and Y. Zalcstein, *Word Problems Solvable in Logspace*, Journal of the ACM 24 (1977), 522--526, DOI:10.1145/322017.322031.
