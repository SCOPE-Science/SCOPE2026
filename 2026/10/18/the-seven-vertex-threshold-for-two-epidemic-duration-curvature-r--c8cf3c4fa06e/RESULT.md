# The seven-vertex threshold for two epidemic-duration curvature reversals

## Finding

Let \((G,r)\) be a finite simple tree with a distinguished initially infected vertex \(r\). In a synchronous, one-generation infectious SIR process, each infectious vertex attempts to infect every still-susceptible neighbor independently with probability \(p\in(0,1)\), then recovers permanently. Write \(T_{G,r}\) for the last generation with a newly infected vertex, counting the original infection as generation zero, and set \(F_{G,r}(p)=\mathbb E[T_{G,r}]\).

**Theorem.** For every rooted tree with at most six vertices, \(F_{G,r}''(p)\) changes sign at most once as \(p\) ranges over \((0,1)\). Among the rooted trees with exactly seven vertices, up to root-preserving isomorphism exactly one has two sign changes of \(F_{G,r}''\): the three-armed spider rooted at its branch point, whose arms have lengths \(1,2,3\). For this tree,

\[
F_{G,r}(p)=3p-p^2+2p^3-p^4,\qquad F_{G,r}''(p)=-2+12p-12p^2.
\]

Its two and only two strict inflection parameters are

\[
p_-=\frac{3-\sqrt3}{6},\qquad p_+=\frac{3+\sqrt3}{6}.
\]

The expected-duration curve is concave on \((0,p_-)\), convex on \((p_-,p_+)\), and concave on \((p_+,1)\). Thus seven vertices are necessary and sufficient for *two* reversals in the marginal sensitivity of expected epidemic duration to transmission probability.

## Assumptions and scope

The graph is a finite, connected, undirected, loopless tree. Exactly one fixed vertex \(r\) is initially infected. Every infected vertex is infectious for exactly one discrete generation, makes one independent Bernoulli transmission attempt with success probability \(p\) along each incident edge toward a susceptible vertex, and then recovers permanently. Infections cannot return to recovered vertices. The expectation is unconditional, including outbreaks infecting only the root, for which \(T_{G,r}=0\). For fixed \((G,r)\), \(F_{G,r}\) is a polynomial in \(p\); a *strict inflection* is a point in \((0,1)\) across which \(F_{G,r}''\) changes sign. The theorem classifies rooted trees only through seven vertices, not larger trees or cyclic networks.

## Proof

**1. Coupling and a general exact recursion.** Root the contact tree at \(r\). Since there is a unique path to each vertex, the epidemic can be coupled to independent Bernoulli-open edges: a vertex is infected in generation \(k\) if and only if its unique root path has length \(k\) and all its edges are open. Thus \(T_{G,r}\) is the height of the root's open-edge component, with an isolated root having height zero. For each rooted subtree at vertex \(v\), let \(Q_k(v;p)\) be the probability that some open path of length at least \(k\) starts at \(v\), with \(Q_0(v;p)=1\). For every \(k\ge1\), independence of different child branches yields

\[
Q_k(v;p)=1-\prod_{u\text{ child of }v}\bigl(1-pQ_{k-1}(u;p)\bigr).
\]

The empty product is \(1\). If \(h\) is the maximal distance from \(r\) to any vertex, the tail-sum identity gives the exact polynomial

\[
F_{G,r}(p)=\sum_{k=1}^{h}Q_k(r;p).
\]

These formulas have no approximation or asymptotic assumption.

**2. Complete exact finite classification.** For each \(n=2,\ldots,7\), enumerate all \(n^{n-2}\) labeled trees using Prüfer words of length \(n-2\), and every possible choice of root. A recursive root-preserving canonical parenthesis code sorts the child-subtree codes, thereby merging exactly the isomorphic rooted trees. The numbers of resulting rooted isomorphism types are \(1,2,4,9,20,48\) respectively. For each representative compute \(F_{G,r}\) by the recursion in step 1, differentiate twice, and count distinct real roots *strictly* between \(0\) and \(1\) by exact Sturm root counting. A zero of the second derivative is only a potential strict inflection, so counting all its interior roots is a valid upper bound on sign changes. Identically zero derivatives contribute none. Endpoint roots are excluded.

| Vertices | Rooted types | No interior curvature roots | One interior root | Two interior roots |
|---:|---:|---:|---:|---:|
| 2 | 1 | 1 | 0 | 0 |
| 3 | 2 | 2 | 0 | 0 |
| 4 | 4 | 3 | 1 | 0 |
| 5 | 9 | 5 | 4 | 0 |
| 6 | 20 | 12 | 8 | 0 |
| 7 | 48 | 28 | 19 | 1 |

For \(n=1\), \(F_{G,r}=0\), hence there is no strict inflection. The sole seven-vertex type with two interior roots has canonical rooted code `(((()))(())())`, describing branch lengths \(3,2,1\) from the root. `verify.py` supplies the complete exhaustive enumeration, exact root counts, and a second independent probability calculation. `CENSUS.csv` gives a one-row-per-rooted-type exact certificate for all \(84\) classes.

**3. Exact witness and sign changes.** On the rooted spider with lengths \(1,2,3\), the probabilities of reaching generations one, two, and three are respectively

\[
Q_1=1-(1-p)^3,\quad Q_2=1-(1-p^2)^2,\quad Q_3=p^3.
\]

Summation yields \(F_{G,r}(p)=3p-p^2+2p^3-p^4\). The second derivative factors as

\[
F_{G,r}''(p)=-12(p-p_-)(p-p_+).
\]

Both roots are simple and lie in \((0,1)\). The signs are negative, positive, negative on the three intervening ranges. All other rooted trees with at most seven vertices have at most one interior zero of the second derivative, and therefore cannot have two strict inflections. This completes the claim.

## Verification

Run `python verify.py CENSUS.csv` with Python 3.9 or later and SymPy 1.10 or later. The verifier enumerates labeled trees directly from every Prüfer word, canonicalizes every root, computes the epidemic duration polynomial by independent child-branch probability recursion and by exhaustive open-edge-mask summation, and compares the two polynomials for every rooted class. It then performs exact Sturm root counts including explicit endpoint exclusion. The run completed with the table above, one unique seven-vertex rooted witness, and no disagreement between the two polynomial methods. Source code and the generated certificate are supplied alongside this result. Finite enumeration proves only the stated sharp finite threshold; it is not presented as evidence for any unrestricted larger-graph classification.

## Relationship to prior work

Karrer and Newman (2010) develop exact message passing for SIR epidemic dynamics on trees and analyze transmissibility, while Sharkey, Kiss, Wilkinson, and Simon (2012 preprint) establish exact finite-tree SIR equations for Markovian infection and recovery. These are foundational frameworks for network epidemic dynamics. The present discrete one-generation model is simpler and measures the maximum occupied infection generation; the new conclusion concerns the *number of curvature sign changes as transmissibility varies*, its sharp smallest rooted network, and uniqueness at that size. The inspected sections of those papers do not state this curvature classification. Picard and Lefèvre (1990) study Reed–Frost final size and severity in a collective population model; their accessible abstract concerns different statistics and does not establish this rooted-tree classification. Its full technical text was unavailable for inspection, leaving bibliographic uncertainty.

## Limitations

The curvature statement is exact for homogeneous, independent one-step transmission on rooted trees up to seven vertices. It does not classify larger rooted trees, arbitrary graphs with cycles, continuous-time infection/recovery, multiple initial infections, or heterogeneous edge probabilities. The distinct parameter ranges should not be construed as a clinical recommendation or an estimate of outbreak duration in real populations. Despite targeted literature comparisons, an unlocated equivalent earlier finite classification remains possible; independent bibliographic review has not been performed.

## References

1. B. Karrer and M. E. J. Newman, *A message passing approach for general epidemic models*, first arXiv version March 29, 2010, arXiv:1003.5673, https://arxiv.org/abs/1003.5673.
2. K. J. Sharkey, I. Z. Kiss, R. R. Wilkinson, and P. L. Simon, *Exact equations for SIR epidemics on tree graphs*, first arXiv version December 10, 2012, arXiv:1212.2172, https://arxiv.org/abs/1212.2172.
3. P. Picard and C. Lefèvre, *A unified analysis of the final size and severity distribution in collective Reed–Frost epidemic processes*, *Advances in Applied Probability* **22** (1990), 269–294, https://doi.org/10.1017/S0001867800019571. Accessible abstract inspected; complete text unavailable.
