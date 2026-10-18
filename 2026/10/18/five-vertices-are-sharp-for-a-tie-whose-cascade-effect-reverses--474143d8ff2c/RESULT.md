# Five vertices are sharp for a tie whose cascade effect reverses with adoption threshold

## Finding

In the progressive, uniform fractional-threshold adoption model, **five vertices are necessary and sufficient** for one added social tie to increase the final cascade at one adoption threshold but decrease it at another, from the *same single initiator*. At five vertices there are exactly **five** isomorphism classes of connected graph, added nonedge, and distinguished initiator realizing both signs. All five have the same response law: the tie changes the final adopter count by \(0\) for \(0<\phi\le 1/3\), by \(+3\) for \(1/3<\phi\le 1/2\), and by \(-1\) for \(1/2<\phi\le1\).

The beneficial effect can be arbitrarily large: for each integer \(n\ge5\), one connected \(n\)-vertex tree, one nonedge, and one fixed initiator have the exact edge-response law
\[
\Delta_n(\phi)=\begin{cases}
0,&0<\phi\le 1/3,\\
n-2,&1/3<\phi\le 1/2,\\
-1,&1/2<\phi\le1.
\end{cases}
\]
The addition therefore turns a two-adopter cascade into complete adoption for intermediate thresholds but suppresses the only secondary adopter at higher thresholds.

## Assumptions and scope

Let \(G=(V,E)\) be a finite connected, undirected, loopless simple graph with \(|V|=n\ge2\). Fix an initiator \(s\in V\) and a homogeneous adoption threshold \(\phi\in(0,1]\). Start with only \(s\) active. All active vertices stay active. At each synchronous round, any inactive vertex \(v\) becomes active when the fraction of its active neighbors is at least \(\phi\):
\[
|N_G(v)\cap A|\ge\phi\,\deg_G(v).
\]
Let \(C_G(s,\phi)\) be the final number of active vertices. For a missing edge \(e\), set \(\Delta_{G,e,s}(\phi)=C_{G+e}(s,\phi)-C_G(s,\phi)\). A *response reversal* means strict positivity for one threshold and strict negativity for another. Both graph and graph-plus-edge are connected. Classification equivalence permits a single vertex relabeling that carries the base graph, distinguished missing edge, and initiator together to their counterparts.

Because activations are permanent and the update map is monotone in active sets, eventual closure is unchanged by any fair asynchronous update schedule, although intermediate activation times may differ. The theorem concerns final adopter counts, not times, likelihoods, or heterogeneous thresholds.

## Proof

**Exact threshold reduction.** For a fixed graph of order \(n\), whether an inactive vertex activates at a given state changes only at a rational number \(k/d\), with \(1\le k\le d\le n-1\). Thus the whole closure is constant on each half-open cell bounded by consecutive critical fractions (and at its right endpoint), except possibly at the leftmost open boundary. Testing the critical fractions and one rational representative inside each open interval is exhaustive for \(\phi\in(0,1]\). Each activation decision is the exact integer comparison \(a q\ge p d\) when \(\phi=p/q\).

**Small-order classification.** Enumerate all \(2^{\binom n2}\) labeled undirected graphs for each \(2\le n\le5\), retain the connected ones, enumerate every missing edge \(e\), and every distinguished single initiator \(s\). Compute both monotone activation closures at the exact threshold representatives. The accompanying standalone `verify.py` implements these finite exhaustive steps, and reduces reversal triples under all \(n!\) relabelings. Connected labeled graph counts for orders \(2,3,4,5\) are respectively \(1,4,38,728\). There are no response reversals through four vertices. At five vertices there are \(420\) labeled graph/edge/initiator reversal triples, partitioning into exactly five orbits with sizes \(60,120,60,120,60\). The five canonical representatives, using vertices \(0,1,2,3,4\), are:

| Base edges | Added edge | Initiator |
| --- | --- | --- |
| 01, 03, 04, 12 | 02 | 1 |
| 01, 03, 04, 12 | 23 | 1 |
| 01, 04, 12, 13, 23 | 14 | 0 |
| 01, 02, 04, 12, 13, 23 | 14 | 0 |
| 01, 02, 03, 04, 12, 13, 23 | 14 | 0 |

Here a two-digit string such as `03` denotes the undirected edge joining vertices \(0\) and \(3\), not a decimal number. In every representative, exhaustive exact closure gives the stated same three-cell response law. Exhaustion of masks, nonedges, initiators, threshold cells, and relabelings proves both minimality and the complete five-vertex classification. This is a finite, transparent computation, not an inference from random sampling or a finite experiment about larger graphs.

**Arbitrarily large positive response with simultaneous negative response.** For each \(n\ge5\) let \(G_n\) have vertices \(0,1,\ldots,n-1\), with edges \(01,03,04,12\). When \(n\ge6\), also include \(35\) and consecutive edges \((5,6),(6,7),\ldots,(n-2,n-1)\). This is a tree. Add the one nonedge \(e=02\), and choose the unique initiator \(s=1\). In \(G_n\), vertex \(2\) is a leaf adjacent to the seed, while vertex \(0\) has degree three and only one initially active neighbor. Hence for \(1/3<\phi\le1\), only vertices \(1,2\) activate in \(G_n\). For \(0<\phi\le1/3\), vertex \(0\) also activates; then the degree-one and degree-two branches activate successively, so the whole tree adopts.

In \(G_n+02\), vertex \(2\) has degree two and vertex \(0\) degree four. For \(1/3<\phi\le1/2\), vertex \(2\) first activates from its one seed neighbor, then \(0\) activates from the two neighbors \(1,2\). Subsequently every branch, including the long path through \(3\), activates because its internal degrees are two. For \(1/2<\phi\le1\), neither \(0\) nor \(2\) has the requisite active-neighbor fraction, so no other vertex activates. For \(0<\phi\le1/3\), both graphs already reach complete adoption. The three cases prove the stated exact \(\Delta_n\) formula for every \(n\ge5\).

## Verification

Run `python3 verify.py` using Python 3.10 or newer; only the standard library is required. The checker regenerates all connected graphs through five vertices and all candidate missing edges and initiators, checks exact rational critical thresholds and interior representatives, computes canonical representatives by all vertex permutations, and asserts the five-class step profile and orbit sizes. It independently checks the explicit family for every order from \(5\) through \(40\); the family theorem for arbitrary order is proved above and does not rely on this bounded check. The checker was run successfully against this package's source file.

## Relationship to prior work

Watts (2002) introduced and analyzed progressive fractional-neighbor threshold cascades on large random networks, including the distinction between highly connected but resistant individuals and easily influenced low-degree individuals. Its original article, including its model and random-network results, was examined. Singh et al. (2013) investigated the same homogeneous threshold mechanism with multiple initiators, network clustering and rewiring; its full accessible article was examined. Both establish the relevance of threshold and network architecture, but neither examined work supplies the fixed-seed, single-edge, all-threshold small-order classification here. Waniek and Hidalgo (2022) studied bridge placement and homophily in other diffusion formulations; their full article was examined, and its links and varying homophily parameters do not imply the present exact result.

The previously published explanation that extra neighbors can dilute influence is a foundational observation, **not** claimed here as new. The mathematically distinct claims are the simultaneous sign reversal for the *same added edge*, its exact minimum order and complete first-layer census, and the all-order amplified-response construction. Relevant index searches did not reveal a covering result; bibliographic absence is not a proof of novelty.

## Limitations

The conclusion requires homogeneous inclusive fractional-neighbor thresholds, progressive irreversible adoption, one fixed seed and a single added undirected edge. A discrete five-vertex census does not establish higher-order uniqueness. The all-size tree family proves arbitrarily large *positive* differences but only a one-adopter negative difference; no unbounded negative magnitude is asserted. No prediction for observed human diffusion is claimed. A covering result under alternate cascade, complex-contagion or network-game terminology cannot be definitively ruled out without independent bibliographic review.

## References

1. D. J. Watts, “A simple model of global cascades on random networks,” *Proceedings of the National Academy of Sciences* 99 (2002), 5766–5771. DOI: 10.1073/pnas.082090499. First public date used here: 2002-04-30. Open full text: https://snap.stanford.edu/class/cs224w-readings/watts02randomnetworks.pdf.
2. P. Singh, S. Sreenivasan, B. K. Szymanski and G. Korniss, “Threshold-limited spreading in social networks with multiple initiators,” *Scientific Reports* 3 (2013), 2330. DOI: 10.1038/srep02330. https://www.nature.com/articles/srep02330.
3. M. Waniek and C. A. Hidalgo, “Bridging the polarization gap: Maximizing diffusion among dissimilar communities,” *Collective Intelligence* (2022). DOI: 10.1177/26339137221128542. https://journals.sagepub.com/doi/10.1177/26339137221128542.
