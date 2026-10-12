# Exact plurality number of signed stars
## Finding
Let \(\Gamma=(K_{1,m},\sigma)\) be a signed star with \(m\ge3\) leaves, centre \(c\), \(p=d^+_\sigma(c)\) positive incident edges, and \(q=m-p=d^-_\sigma(c)\) negative incident edges. Then its plurality number is \[ Y(\Gamma)=\begin{cases} m,&p=0,\\ \max\{p+2,q+1\},&1\le p\le m-1,\\ m+1,&p=m. \end{cases} \] Consequently, because every signing of a tree lies in the switching class of the all-positive signing, \[ \min_{\Gamma'\sim K_{1,m}^+}Y(\Gamma')=\left\lceil\frac{m+3}{2}\right\rceil. \] Equivalently, the reachable-colouring code of the all-positive signed star has covering radius \(\lfloor(m-1)/2\rfloor\).

## Assumptions and scope
Graphs are finite, simple, and undirected. A signed graph assigns a sign in \(\{+1,-1\}\) to each edge. The signed burning process and plurality number \(Y(\Gamma)\) are those introduced by Fallat, Gupta, Khodamoradi, and Zilles: spreading occurs before each ignition, positive edges preserve a fire colour, negative edges reverse it, and an unburned vertex reached with equal yellow and green influence remains unburned.

The theorem concerns stars with at least three leaves. The two-leaf star is a path and belongs to the signed-path family already treated in the initiating paper. For the star write \(c\) for the centre, let \(p=d^+_\sigma(c)\), and put \(q=m-p=d^-_\sigma(c)\).

## Proof
At the first time step no spreading occurs, so the first action is one ignition.

If the centre \(c\) is ignited first, then at the next spread every leaf has exactly one burned neighbour. Every positive leaf edge transmits the colour of \(c\), and every negative leaf edge transmits the opposite colour. All vertices are then burned before another ignition can occur. The two final colour-class sizes are therefore \(p+1\) and \(q\).

Now suppose a leaf \(x\) is ignited first. At the next spread, the centre has exactly one burned neighbour, so it burns with the colour obtained by transmitting the colour of \(x\) across \(cx\). In particular, relative to the colour of the centre, the first leaf already lies in its natural class: it agrees with the centre if \(cx\) is positive and disagrees if \(cx\) is negative. Because \(m\ge3\), at least one other leaf is still unburned after this spread, so exactly one such leaf may be ignited before the next spread. At the following spread every remaining leaf has the centre as its unique burned neighbour, and therefore takes its natural colour determined by the sign of its incident edge.

Hence a leaf-first process can differ from the natural centre-propagated colouring at only the second ignited leaf. The natural classes have sizes \(p+1\) on the centre side and \(q\) on the opposite side. If \(p=0\), a second ignition can move at most one negative leaf into the centre colour, so no colour class exceeds \(m\); igniting the centre first already attains \(m\). If \(p=m\), igniting the centre first burns all \(m+1\) vertices in one colour. Finally suppose \(1\le p\le m-1\). By choosing the first leaf so that a leaf of the desired sign remains available for the second ignition, one may flip one negative leaf into the centre colour, attaining \(p+2\), or flip one positive leaf into the opposite colour, attaining \(q+1\). No sequence can alter more than this one natural leaf, so
\[
Y(\Gamma)=\max\{p+2,q+1\}.
\]
This proves the three cases.

Every signed tree is balanced and hence switching-equivalent to its all-positive signing. Thus minimizing over the switching class amounts to minimizing the displayed formula over \(0\le p\le m\). The interior expression \(\max\{p+2,m-p+1\}\) is minimized when the two terms are as equal as possible, and its minimum is
\[
\left\lceil\frac{m+3}{2}\right\rceil
\]
for \(m\ge3\); the endpoint values \(m\) and \(m+1\) are no smaller. The general coding relation in the initiating paper says that the minimum plurality number over a switching class equals the order minus the covering radius of its reachable-colouring code. Since the star has \(m+1\) vertices, the covering radius is therefore
\[
(m+1)-\left\lceil\frac{m+3}{2}\right\rceil
=\left\lfloor\frac{m-1}{2}\right\rfloor.
\]

## Verification
The accompanying `verify.py` implements the signed burning rule directly. For every one of the \(504\) signatures on stars with between three and eight leaves, it enumerates all possible ignition choices and colours, computes every reachable final colouring, and compares the resulting plurality number with the theorem. It checks \(8160\) reachable final colourings in total. It also independently takes the minimum over every signing in this exhaustive range and compares it with \(\lceil(m+3)/2\rceil\). The finite computation corroborates the theorem; the proof above establishes the statement for arbitrary \(m\).

## Relationship to prior work
Fallat, Gupta, Khodamoradi, and Zilles introduced signed graph burning and the plurality number in arXiv:2610.02506v1, first public on 2026-10-01. Their Definition 2.5 defines \(Y(\Gamma)\), Proposition 2.9 and Remark 2.10 relate switching to Hamming distance and covering radius, and Section 3 determines exact values for special classes of signed paths. Their introduction states that more structurally complex graph classes remain open, and their conclusion specifically proposes bounds for classes of signed trees. The full text contains no star theorem or \(K_{1,m}\) specialization.

Targeted searches for the plurality number of signed stars, signed-burning stars, the \(K_{1,m}\) family, and the corresponding covering radius found no statement implying the formula above. Nearby search results concern different burning processes or unrelated invariants on stars and therefore do not cover this claim.

## Limitations
The theorem is restricted to signed stars with at least three leaves. It does not classify arbitrary signed trees, signed complete bipartite graphs, or directed variants. The exhaustive computation is finite and is not used as a proof of the infinite statement. Because the initiating invariant is very recent, a not-yet-indexed equivalent calculation remains a residual literature risk.

## References
1. S. Fallat, H. Gupta, K. Khodamoradi, and S. Zilles, “Burning Signed Graphs,” arXiv:2610.02506v1, first public 2026-10-01, MSC 05C57, 05C22.
