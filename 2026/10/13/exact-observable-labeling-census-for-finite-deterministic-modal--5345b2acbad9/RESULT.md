# Exact observable-labeling census for finite deterministic modal frames
## Finding
Let \(W\) be any nonempty finite set and \(f:W\to W\) any total function. Consider the Boolean modal powerset algebra \(\mathcal A_f=(\mathcal P(W),\cup,\cap,{}^c,\varnothing,W,\Diamond)\), where \(\Diamond U=f^{-1}(U)\). For any integer \(r\ge0\), the ordered generators \(U_1,\ldots,U_r\) define a letter \(a(w)=(\mathbf1_{U_1}(w),\ldots,\mathbf1_{U_r}(w))\) in an alphabet of size \(q=2^r\) at each state.

**Complete criterion.** These generators yield \(\mathcal A_f\) in full if and only if both conditions hold:

1. On every directed cycle of \(f\), the cyclic label word is primitive (aperiodic), and distinct cycles of any common length receive different primitive necklaces (cyclic-rotation classes).
2. For each \(v\in W\), the letters at the distinct states of the immediate fiber \(f^{-1}(\{v\})\) are pairwise different.

Write \(C\) for the set of cycle vertices, \(c_\ell\) for the number of directed cycles of length \(\ell\), \(d_v=|f^{-1}(\{v\})|\), and \((z)_{\underline t}=\prod_{j=0}^{t-1}(z-j)\), with the empty product equal to one. Put
\[
P_q(\ell)=\sum_{d\mid\ell}\mu(d)q^{\ell/d},
\]
the number of primitive words of length \(\ell\) on a \(q\)-letter alphabet. The **exact number of ordered generating \(r\)-tuples** is
\[
\boxed{N_f(r)=\left(\prod_{\ell\ge1}\prod_{j=0}^{c_\ell-1}\big(P_{2^r}(\ell)-j\ell\big)\right)
\left(\prod_{v\in C}(2^r-1)_{\underline{d_v-1}}\right)
\left(\prod_{v\notin C}(2^r)_{\underline{d_v}}\right).}
\]
All products involve finitely many nontrivial factors. If a requested number of distinct letters exceeds the available nonnegative alphabet capacity, the corresponding falling factorial vanishes; empty products equal one.

**Sharp generator rank.** With \(\Delta=\max_{v\in W}d_v\), the least number of propositional generators is
\[
\boxed{\operatorname{rank}(\mathcal A_f)=\min\big\{r\ge0:2^r\ge\Delta\text{ and }P_{2^r}(\ell)\ge\ell c_\ell\ \text{for every }\ell\ge1\big\}.}
\]
The minimum always exists. If a generating labeling uses \(s\) distinct alphabet letters across its states, then each singleton is definable by a Boolean modal formula of depth at most \(|W|-s\). This uniform depth bound is attained, for each \(|W|\ge2\), by a rooted self-loop preceded by a linear chain, with the root of color zero and every nonroot state of color one.

For example, for \(f=(0,0,0)\) on three labeled states, no one-predicate marking generates the full algebra; exactly \(24\) ordered pairs of predicates do. For two disjoint directed three-cycles, exactly \(18\) single-predicate valuations generate the full algebra.

## Assumptions and scope
The accessibility relation is **functional and total**: each state has exactly one successor, namely \(f(w)\). The modal operation is the preimage of a set under \(f\), i.e. ordinary diamond and box coincide on this frame. Boolean constants and complements are included. The finite set \(W\) has cardinality \(n\ge1\); no connectedness or injectivity of \(f\) is assumed. The integer \(r\) may be zero. Results count labeled states and ordered tuples; there is no quotient by graph automorphisms. If \(f\) is supplied by a tuple of successor indices, the formula can be evaluated from its directed-cycle lengths and indegrees.

## Proof
**1. Equivalence by forward itineraries.** For a label \(a:W\to\{0,1\}^r\), associate to \(w\) its infinite itinerary \(I(w)=(a(f^t(w)))_{t\ge0}\). Every modal term is a Boolean combination of sets of the form \(f^{-t}(U_i)\): this is proved by induction because preimages preserve finite Boolean unions, intersections, and complements. Two states therefore lie in the same atom of the generated Boolean algebra precisely when their itineraries agree. Conversely, if all \(n\) itineraries are distinct, then for each pair of states a finite index distinguishes them; taking finite conjunctions of corresponding indexed literals isolates each singleton. Hence the full powerset algebra is generated exactly when the itinerary map is injective.

**2. Necessary local and cycle constraints.** Two equally colored predecessors \(x\ne y\) of the same vertex \(v\) satisfy \(I(x)=I(y)\) and therefore are forbidden. A periodic word on a cycle of length \(\ell\) with proper period gives the same itinerary at two distinct cycle points. Likewise two different cycles bearing cyclic rotations of the same primitive word give identical itineraries. This proves necessity.

**3. Sufficiency.** Assume both constraints and suppose \(I(x)=I(y)\). For sufficiently large \(T\), both \(f^T(x)\) and \(f^T(y)\) belong to cycles, with identical forward infinite itineraries. Such an eventually periodic sequence has minimal period equal to the length of its primitive labeled cycle. The cycle constraint therefore forces these iterates to be the *same vertex* rather than distinct cyclic shifts or distinct cycles. Let \(t\) be the least index at which \(f^t(x)=f^t(y)\). If \(t>0\), the distinct states \(f^{t-1}(x)\) and \(f^{t-1}(y)\) share a successor and the same initial letter, contrary to the fiber constraint. Thus \(t=0\), proving \(x=y\) and sufficiency.

**4. Counting.** Standard Möbius inversion counts primitive words of length \(\ell\) as \(P_q(\ell)\). Each primitive necklace contains exactly \(\ell\) distinct rotations. For \(c_\ell\) distinct, labeled directed cycles, fill them successively: the first has \(P_q(\ell)\) choices; after \(j\) cycles, precisely \(j\ell\) cyclic words are excluded. This gives \(\prod_{j=0}^{c_\ell-1}(P_q(\ell)-j\ell)\) for each length. All cyclic letters are then fixed. Each cycle vertex \(v\) has one predecessor on its cycle, already labeled, leaving \(d_v-1\) other predecessors to receive distinct letters different from that cyclic letter: \((q-1)_{\underline{d_v-1}}\) ways. An off-cycle vertex has no prescribed predecessor, so its \(d_v\) predecessors receive arbitrary distinct letters in \((q)_{\underline{d_v}}\) ways. As every noncycle state is exactly one immediate predecessor of a successor, these assignments partition all noncycle vertices, and the factors are independent. Multiplication gives the census.

**5. Rank and depth.** Every factor in the count is nonzero exactly when \(q\ge\Delta\) and the number \(P_q(\ell)/\ell\) of primitive necklaces is at least \(c_\ell\) for each \(\ell\). These conditions are also jointly sufficient by the same independent construction. Restrict to \(q=2^r\) to obtain the rank.

For the depth bound, at depth zero the partition by initial letters has \(s\) classes. Depth \(t+1\) refines by the pair consisting of the initial letter and the depth-\(t\) class of the unique successor. If this refinement does not split any class, it is stable under every later round. For a generating labeling, the stable partition is discrete with \(n\) classes. Hence strictly increasing class counts give discreteness by depth \(n-s\). On a chain feeding a self-loop, with only its root labeled zero, there are exactly two depth-zero classes and the successive depth rounds distinguish precisely one additional distance-to-root class until depth \(n-2\); thus equality is attained.

## Verification
Run `python verify.py` using Python 3 and no third-party packages. The independent tests compute Moore-style itinerary partitions, evaluate the cycle/fiber criterion, count successful markings, and directly build Boolean modal term closures. The verified output is:

```
VERIFY_OK exhaustive_colorings 196579 full_census_graphs 7402 direct_boolean_modal_closures 26122 random_colorings 12000 rank_boundaries 9000 examples (24, 18)
```

Exhaustive enumeration covers all maps on up to five states for binary and single-letter alphabets, and all maps on up to four states for three- and four-letter alphabets; additional deterministic randomized checks span up to 25 states. Tests are corroborating finite computations, not an exhaustive proof for arbitrary finite cardinalities. The structural proof above is the basis of the unrestricted theorem.

## Relationship to prior work
Wißmann, Milius, and Schröder develop general constructions of modal witnesses that distinguish behaviorally inequivalent states. The itinerary viewpoint here is a deterministic, single-successor specialization of that expressiveness foundation. Their inspected discussion of deterministic automata and separating certificates does not provide the fixed-transition count of **all generator valuations** or this factorization into primitive-necklace and incoming-fiber factors. Davies studies uniform minimality of permutation DFAs across choices of final states, a related but different quantifier structure and a different object: she does not classify all observable output labelings of arbitrary (possibly noninjective) one-letter transition graphs. Shea's graph-labeling study concerns factors and entropy in symbolic dynamics, not the finite labeled-state census considered here. Classical primitive-necklace and Möbius formulas are used as ingredients, not claimed as discoveries. Similar formulations may occur in unary-automaton observability, symbolic coding, or finite dynamical-systems literature.

## Limitations
The result concerns finite total deterministic relations only, not nondeterministic transition systems. It counts labeled state valuations rather than isomorphism classes. It does not assert novelty of partition refinement, primitive necklaces, or the basic equivalence between modal distinguishability and observable traces. Existence of a specialized historical antecedent to the combined census remains possible. No independent mathematical or originality audit has been performed.

## References
1. T. Wißmann, S. Milius, and L. Schröder, *Quasilinear-time Computation of Generic Modal Witnesses for Behavioural Inequivalence*, arXiv:2203.11175, first public 2022-03-21; *Logical Methods in Computer Science* 18(4), 6:1–6:48 (2022), DOI:10.46298/lmcs-18(4:6)2022. https://arxiv.org/abs/2203.11175
2. S. Davies, *Primitivity, Uniform Minimality and State Complexity of Boolean Operations*, arXiv:1702.00877 (2017). https://arxiv.org/abs/1702.00877
3. S. Shea, *Graph Labelings and Continuous Factors of Dynamical Systems*, *Electronic Journal of Combinatorics* (2013), DOI:10.37236/2213. https://doi.org/10.37236/2213
