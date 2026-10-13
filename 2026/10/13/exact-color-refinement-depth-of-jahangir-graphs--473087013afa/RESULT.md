# Exact color-refinement depth of Jahangir graphs
## Finding
For integers \(n\ge2\) and \(m\ge3\), let \(J_{n,m}\) be the Jahangir graph obtained from a cycle \(C_{nm}\) by adjoining a center \(c\) adjacent to \(m\) equally spaced cycle vertices, so consecutive neighbors of \(c\) are \(n\) cycle edges apart.

Run ordinary color refinement from the uniform coloring, and let \(\operatorname{Stab}(G)\) be the least round at which the induced vertex partition stops changing. Then
\[
\operatorname{Stab}(J_{n,m})=
\begin{cases}
\max\{2,\lfloor n/2\rfloor\},&m=3,\\
\lfloor n/2\rfloor,&m\ge4.
\end{cases}
\]

Moreover, for every \(n\ge2\) and \(m\ge3\), the stable color partition is exactly the automorphism-orbit partition.

The exceptional term at \(m=3\) has a simple structural origin: only then does the center have degree \(3\), the same as the \(m\) attachment vertices on the cycle. Color refinement needs one additional round to separate these two degree-\(3\) roles when the sector length is too short to dominate the process.

## Assumptions and scope
All graphs are finite, simple, undirected, and initially uncolored. The convention for \(J_{n,m}\) is the standard one in which the rim is \(C_{nm}\) and the center is adjacent to \(m\) rim vertices spaced by \(n\) rim edges. The statement assumes \(n\ge2\) and \(m\ge3\); the wheel boundary \(n=1\) is not included.

Round \(0\) is the uniform coloring. In every later round, a vertex receives a color determined by its previous color together with the multiset of previous colors on its neighbors. Stabilization refers to the induced partition, not to literal color names.

Call the \(m\) neighbors of the center attachment vertices. Between consecutive attachment vertices on the rim lies a sector consisting of an \(n\)-edge path with \(n-1\) internal degree-\(2\) vertices.

## Proof
First suppose \(m\ge4\). The center has degree \(m\), every attachment vertex has degree \(3\), and every internal sector vertex has degree \(2\). Thus round \(1\) separates these three roles.

Fix one sector and number its internal positions \(1,\ldots,n-1\) from one attachment endpoint. Since all attachment endpoints have the same color, later refinement inside every sector is the same as simultaneous refinement of an \(n\)-edge path whose two endpoints already have the same distinguished color. In round \(r\ge1\), two internal positions remain in the same color class exactly when their distances to the two attachment endpoints agree after truncation at the radius visible by that round, up to reversal of the sector. Consequently one new distance layer can split per round, and the final possible split inside a sector occurs in round
\[
\left\lfloor\frac n2\right\rfloor.
\]

This bound is sharp. For \(n\ge4\), immediately before that round the central unresolved positions in a sector still have identical truncated endpoint-distance data, while the next refinement separates the last distinct distance class. For \(n=2,3\), no nontrivial internal split is needed and the degree partition from round \(1\) is already stable; this agrees with \(\lfloor n/2\rfloor=1\). Hence
\[
\operatorname{Stab}(J_{n,m})=\left\lfloor\frac n2\right\rfloor
\]
for \(m\ge4\).

Now let \(m=3\). The center and the three attachment vertices all have degree \(3\), so round \(1\) does not separate them. However, in the round-\(1\) partition the center has three degree-\(3\) neighbors, whereas each attachment vertex has one degree-\(3\) neighbor and two degree-\(2\) neighbors. Therefore round \(2\) separates the center from the attachments.

The sector refinement occurs in parallel exactly as above. The new distinction between center and attachment changes color labels on later rounds but cannot split an attachment orbit, because every attachment sees the same center and two symmetric sectors. Therefore the only possible stabilization bottlenecks are round \(2\) for separating the two degree-\(3\) roles and round \(\lfloor n/2\rfloor\) for resolving positions inside a sector. Thus
\[
\operatorname{Stab}(J_{n,3})=
\max\left\{2,\left\lfloor\frac n2\right\rfloor\right\}.
\]

It remains to identify the stable classes. The center is a singleton orbit. The attachment vertices form one orbit under rotations of the rim by \(n\) positions. For each
\[
1\le d\le\left\lfloor\frac n2\right\rfloor,
\]
all internal sector vertices whose nearer attachment endpoint is at distance \(d\) form one orbit: rotations permute sectors and a reflection reverses every sector. Distinct values of \(d\) are separated by the endpoint-distance refinement above. When \(m=3\), the center and attachments are also separated in round \(2\). Hence the stable partition is precisely the automorphism-orbit partition.

## Verification
The accompanying standalone checker constructs \(J_{n,m}\) directly and implements ordinary color refinement without graph-library dependencies. It tests every
\[
2\le n\le60,\qquad 3\le m\le30.
\]
For each of the \(1652\) parameter pairs it verifies the exact depth formula and compares the stable partition with the explicit orbit partition described in the proof.

It returns:

`VERIFY_OK depth_checks=1652 orbit_checks=1652 n=2..60 m=3..30`

The computation is corroborative only. The all-parameter theorem rests on the proof above.

## Relationship to prior work
Jahangir graphs are a standard generalized-wheel family. Mojdeh and Ghameshlou studied domination on \(J_{2,m}\) in 2007, and Bhatti studied chromatic properties of Jahangir graphs in the same year. Later work treats Ramsey numbers, metric invariants, graph burning, and other structural parameters of the family.

Krebs and Verbitsky formalize color-refinement stabilization and relate refinement rounds to rooted universal-cover information. That general local-propagation viewpoint explains why the present calculation reduces to distance waves along the equal rim sectors.

Targeted searches using Jahangir/generalized-wheel terminology together with color refinement, \(1\)-WL, Weisfeiler--Leman, equitable partitions, stabilization depth, and automorphism orbits did not locate the formula above. Published-result searches likewise returned no Jahangir-specific color-refinement theorem. The exact \(m=3\) exception is not supplied by the general framework: it arises from the degree coincidence between the hub and the rim attachments.

## Limitations
The theorem treats ordinary one-dimensional color refinement from the uniform coloring and the standard equally spaced Jahangir family with \(n\ge2\) and \(m\ge3\). It does not cover arbitrary wheels with irregular spoke placement, higher-dimensional Weisfeiler--Leman refinement, or exact graph-pair distinguishing depth. The literature search was targeted rather than exhaustive, so an unindexed family-specific occurrence remains a residual priority risk.

## References
1. D. A. Mojdeh and A. N. Ghameshlou, *Domination in Jahangir Graph \(J_{2,m}\)*, International Journal of Contemporary Mathematical Sciences 2 (2007), 1193--1199, DOI: 10.12988/IJCMS.2007.07122.
2. A. A. Bhatti, *On Some Chromatic Properties of Jahangir Graph*, Ars Combinatoria 84 (2007), 269--279.
3. K. Ali and E. T. Baskoro, *On the Ramsey numbers for a combination of paths and Jahangirs*, arXiv:0711.2571, first posted 16 November 2007.
4. A. Krebs and O. Verbitsky, *Universal covers, color refinement, and two-variable counting logic: Lower bounds for the depth*, arXiv:1407.3175, first posted 11 July 2014.
5. V. Arvind, J. Köbler, G. Rattan, and O. Verbitsky, *Graph Isomorphism, Color Refinement, and Compactness*, arXiv:1502.01255, first posted 4 February 2015.
