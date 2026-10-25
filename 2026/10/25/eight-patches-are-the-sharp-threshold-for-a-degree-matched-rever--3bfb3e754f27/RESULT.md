# Eight patches are the sharp threshold for a degree-matched reversal in isolation-free reliability

## Finding
A habitat is represented by a finite undirected tree \(T\) whose patches (vertices) independently survive with common probability \(p\in(0,1)\). Let \(S\) be the set of surviving patches. Define its **nonempty isolation-free reliability** by
\[
R_T(p)=\Pr\{\text{every }v\in S\text{ has a neighbor in }S\mid S\ne\varnothing\}.
\]
Thus a surviving habitat is successful when no surviving patch has lost all of its adjacent surviving patches. A connected pair of survivors is successful; a single survivor is not; a network may have multiple surviving components of size at least two.

**Sharp degree-matched comparison theorem.** For every \(2\le n\le7\), every two nonisomorphic \(n\)-vertex trees \(T,H\) with identical degree multisets have the property that \(R_T(p)-R_H(p)\) has one fixed weak sign for all \(0<p<1\). Among the \(23\) degree-matched unordered pairs of nonisomorphic eight-vertex trees, exactly one pair, up to exchanging its members, has a strict ranking reversal. A labeled representative of that pair is
\[
\begin{aligned}
E(T)&=\{01,05,07,12,14,23,56\},\\
E(H)&=\{01,04,06,12,13,45,67\}.
\end{aligned}
\]
Here \(ij\) denotes an undirected edge between vertices \(i,j\in\{0,\ldots,7\}\). Both degree multisets are \((1,1,1,1,2,2,3,3)\), but
\[
\boxed{R_T(p)-R_H(p)=\frac{p^5(1-p)(1-2p)}{1-(1-p)^8}.}
\]
Consequently \(T\) has greater reliability for \(0<p<1/2\), the two are equal at \(p=1/2\), and \(H\) has greater reliability for \(1/2<p<1\). Eight is the least possible tree order exhibiting this disagreement at any two survival probabilities.

The two trees nevertheless have **equal expected numbers of isolated surviving patches** at every \(p\), because this expectation depends only on the degree multiset. Thus degree counts and expected isolation do not determine the direction of the all-patches-supported reliability ordering.

## Assumptions and scope
All graphs are finite simple unweighted undirected trees with no vertex weights; two graphs are compared only if they have equal order and the same entire degree multiset. Survival indicators are independent and identically Bernoulli with probability \(p\). An isolated survivor is a selected vertex having no selected graph-neighbor. Empty-survivor realizations are excluded by conditioning; this is a probabilistic network statistic, not a claim that isolated patches necessarily imply ecological extinction. Trees of order one give no nonisomorphic degree-matched pairs. The classification is asserted only through eight vertices, without a claim for larger trees or heterogeneous survival rates.

## Proof
**Step 1 (isolation-free set polynomial).** For any \(n\)-vertex graph, let \(c_j(T)\) be the number of \(j\)-vertex subsets \(S\subseteq V(T)\) for which every selected vertex has a selected neighbor. The empty subset is included only as an algebraic convention, so \(c_0=1\) and \(c_1=0\) for any nonempty simple graph. Put
\[
C_T(t)=\sum_{j=0}^n c_j(T)t^j,\qquad t=\frac p{1-p}>0.
\]
Independent survival gives the unconditional identity
\[
U_T(p)=\Pr\{\text{no isolated survivor, allowing }S=\varnothing\}=(1-p)^n C_T\!\left(\frac p{1-p}\right).
\]
Removing the empty event and conditioning on at least one survivor therefore gives
\[
R_T(p)=\frac{(1-p)^n[C_T(t)-1]}{1-(1-p)^n}.
\]
For a pair of equal order, its reliability difference is a strictly positive factor times \(C_T(t)-C_H(t)\). Consequently any coefficientwise nonnegative (or nonpositive) difference of these set polynomials proves an all-probability weak ordering. If the coefficient difference contains both signs, one must instead analyze its roots.

**Step 2 (complete small-tree classification).** Start with the unique one-vertex tree; obtain every unlabeled tree of size \(n+1\) by adjoining one new leaf to each vertex of every size-\(n\) representative, identifying duplicates by the standard canonically sorted rooted-parenthesis code at the one or two tree centers. This is complete because every tree of order at least two has a leaf, whose deletion leaves a tree, and the center code identifies exactly unrooted-tree isomorphisms. For each representative enumerate all \(2^n\) subsets, incrementing \(c_j\) only when no selected vertex is isolated, and compare every unordered pair in each identical-degree-multiset class.

The exact exhaustive integer census, recorded in `certificate.json`, is:

| \(n\) | Tree types | Degree-matched pairs | Coefficientwise ordered pairs | Mixed-sign pairs |
|---:|---:|---:|---:|---:|
| 1 | 1 | 0 | 0 | 0 |
| 2 | 1 | 0 | 0 | 0 |
| 3 | 1 | 0 | 0 | 0 |
| 4 | 2 | 0 | 0 | 0 |
| 5 | 3 | 0 | 0 | 0 |
| 6 | 6 | 1 | 1 | 0 |
| 7 | 11 | 5 | 5 | 0 |
| 8 | 23 | 23 | 22 | 1 |

All \(29\) comparisons and their complete signed coefficient vectors are recorded, not merely the summary. The \(22\) eight-vertex and all \(6\) smaller-order coefficientwise comparisons cannot reverse because \(t>0\).

**Step 3 (the sole exceptional pair).** Direct subset enumeration for the displayed pair yields
\[
\begin{aligned}
(c_0(T),\ldots,c_8(T))&=(1,0,7,8,15,14,10,4,1),\\
(c_0(H),\ldots,c_8(H))&=(1,0,7,8,15,13,10,5,1).
\end{aligned}
\]
Thus
\[
C_T(t)-C_H(t)=t^5-t^7=t^5(1-t^2).
\]
Substitute \(t=p/(1-p)\) in Step 1 and cancel the common empty-realization term. This gives the displayed exact formula. The denominator is strictly positive for \(0<p<1\); the only interior zero is \(p=1/2\), where the sign reverses strictly. This proves both existence and minimality, and the census proves uniqueness up to tree isomorphism and exchange of members at order eight.

**Step 4 (matching first moments).** If \(I_T\) is the number of isolated surviving vertices, linearity and independence imply
\[
\mathbb E[I_T]=p\sum_{v\in V(T)}(1-p)^{\deg_T(v)}.
\]
The sum depends only on the degree multiset and is therefore identical for the witness pair. The probability that \(I_T=0\), after excluding the all-empty outcome, is not determined by that expectation.

## Verification
Run `python3 verify.py > reproduced.json`, then compare `reproduced.json` byte for byte with `certificate.json`. Only Python 3 standard-library modules are used. The program independently derives each tree's set polynomial in two different ways: exhaustive subsets and a rooted-tree dynamic program with absent, selected/supported, and selected/parent-needing states. It also checks the labeled witness against the unique exceptional pair found by a separate unlabeled leaf-extension census.

The mathematical completeness of the census follows from the leaf-deletion induction and the completeness of the center-based tree isomorphism code; the integer output is not an extrapolation to larger trees. Polynomial positivity follows analytically from coefficient signs, and the exceptional reversal from its displayed factorization. Both the source and machine-readable certificate are embedded with this report.

## Relationship to prior work
Urban and Keitt (2001) motivate graph-based habitat-patch connectivity and conservation decisions. The present model is a deliberately simplified independent site-retention model; their empirical/metapopulation analysis is not an eight-tree risk classification. Tittmann, Averbouch, and Makowsky (2008 preprint) study the bivariate subgraph-component polynomial, which records number of components of each induced subset but does not itself provide the current eight-tree coefficientwise comparisons for the event of having **no singleton component**. Brown and Mol (2016 preprint) study *node reliability*, which requires the nonempty retained subset to be connected; our property instead permits several surviving components if none is a singleton. These events and their comparison polynomials are different. Existing small-tree studies of largest surviving-component expectation and isolation-count variance concern different statistics, with no implication giving the present exact probability law or unique eight-tree exception.

## Limitations
The theorem is an exact finite-tree classification only through order eight, with homogeneous independent site survival. Network edges represent potential adjacency, not conditional dispersal success. A patch may have a surviving neighbor without any actual successful dispersal, and the model does not predict species persistence or empirical effects. The degree-matched pair comparison is not a claim about optimizing a realistic habitat network. Prior bibliographic coverage cannot be proven complete; earlier equivalent statements under graph-polynomial or reliability terminology are a residual novelty risk. Independent external scientific validation has not been performed.

## References
1. D. Urban and T. Keitt, “Landscape connectivity: a graph-theoretic perspective,” *Ecology* **82** (2001), 1205–1218, DOI: `10.1890/0012-9658(2001)082[1205:LCAGTP]2.0.CO;2`. The publisher records first public online availability on 2001-05-01.
2. P. Tittmann, I. Averbouch, and J. A. Makowsky, “The enumeration of vertex induced subgraphs with respect to the number of components,” arXiv:`0812.4147` (2008 public preprint), later *European Journal of Combinatorics* (2011).
3. J. Brown and L. Mol, “On the roots of the node reliability polynomial,” arXiv:`1607.08496` (first submitted 2016-07-28), later *Networks* (2016).
