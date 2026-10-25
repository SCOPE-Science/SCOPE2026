# Exact forced four-colouring polynomial and minimum seeds of wheel graphs \(K_1\vee C_n\)

## Finding
For every integer \(n\ge5\), let \(W_n=K_1\vee C_n\) be a wheel with one hub and a rim of \(n\) cyclically ordered vertices. With four **named** colours, denote by \(b_{n,j}\) the number of partial proper colour assignments on exactly \(j\) vertices that become a complete proper four-colouring by repeatedly colouring an uncoloured vertex when its coloured neighbours exhibit exactly three distinct colours. The entire seed-size enumerator \(B_n(z)=\sum_j b_{n,j}z^j\) equals
\[
B_n(z)=4\sum_{h=0}^{\lfloor n/2\rfloor}I_{n,h}\left[P_{n-h}(3)z^{n-h+1}+\big(P_{n-h}(3)-3P_{n-h}(2)\big)z^{n-h}\right],
\]
where
\[
I_{n,0}=1,\qquad I_{n,h}=\frac{n}{n-h}\binom{n-h}{h}\quad(h\ge1),
\qquad P_k(q)=(q-1)^k+(q-1)(-1)^k.
\]
The minimum seed size is \(\lceil n/2\rceil\), attained by exactly
\[
4 I_{n,\lfloor n/2\rfloor}\left(2^{\lceil n/2\rceil}-3-(-1)^{\lceil n/2\rceil}\right)
\]
labelled partial assignments. Thus, for \(n=5,6,7,8\), the minimum-set counts are respectively \(120,48,336,96\).

The equivalent four-colour forcing probability polynomial, for independent vertex probabilities \(p\) of each named colour and \(r=1-4p\) of being uncoloured (with \(0\le p\le1/4\)), is
\[
FC_4(W_n;p)=4\sum_{h=0}^{\lfloor n/2\rfloor}I_{n,h}p^{n-h}r^h
\left[(p+r)P_{n-h}(3)-3rP_{n-h}(2)\right].
\]

## Assumptions and scope
All graphs are finite and simple. The four available colours are distinguishable; no quotient by colour permutation is taken. The forcing step assigns the unique missing colour whenever three distinct colours already occur in a currently uncoloured vertex's neighbourhood. The starting partial assignment is counted only if it is proper on all initially coloured adjacent pairs and can reach a proper total assignment via repeated forcing. Order does not matter: each forced vertex's colour is unique when a forcing move is legal. The wheel parameter \(n\) is the number of rim vertices, not the total vertex count, and \(n\ge5\) throughout. The graph may be three-chromatic for even \(n\), but the palette is always four named colours.

## Proof
Fix an initially proper partial colouring and consider the two possible states of the hub.

**Hub initially coloured.** Fix its colour. Every initially coloured rim vertex must use one of the remaining three colours. An uncoloured rim vertex can be forced only once both its rim neighbours are coloured with distinct colours, because the coloured hub contributes the third distinct neighbour colour. An adjacent pair of uncoloured rim vertices can never be resolved: in any nonempty run of length at least two, no vertex has both rim neighbours coloured, so no first forcing move within the run is possible. It follows that the rim holes must be isolated. Conversely, isolated holes between differently coloured seeded rim neighbours are all immediately forceable. The initially seeded rim colours must be proper across edges with two seeded ends.

**Hub initially uncoloured.** No rim vertex can force before the hub, since it then has only its two rim neighbours potentially coloured, too few to determine a colour from a four-colour palette. Hence the first move must force the hub. This is possible precisely when the seeded rim uses exactly three distinct colours; the missing fourth becomes the unique hub colour. Afterward the preceding isolated-hole criterion applies. Thus the rim must have isolated unseeded vertices flanked by differently coloured seeds, and its seeded colours must use all three colours different from the forced hub colour. Conversely, these conditions force the hub first and all rim holes afterward.

Fix a pattern of \(h\) isolated rim holes. Since \(n\ge5\) and \(0\le h\le\lfloor n/2\rfloor\), there are \(k=n-h\ge3\) seeded rim vertices. Read them around the cycle and connect successive seeded vertices, allowing an original intervening hole to be traversed by one compressed edge. Properness across an original edge and the distinct-flank criterion across a hole together say exactly that the \(k\) seeded rim colours give a proper colouring of the compressed \(k\)-cycle. Its chromatic polynomial at \(q\) colours is \(P_k(q)=(q-1)^k+(q-1)(-1)^k\). For a fixed implied hub colour, there are \(P_k(3)\) assignments if the hub was seeded. If it was not, all three remaining colours must occur; inclusion–exclusion leaves \(P_k(3)-3P_k(2)\) possibilities, because a proper cycle of length at least three has no one-colour assignment. Four hub colours are possible.

There are \(I_{n,h}=\frac{n}{n-h}\binom{n-h}{h}\) hole sets of cardinality \(h\) with no adjacent vertices: count the cyclic positive gaps between holes, equivalently mark one hole, choose the \(h\) intervening positive zero-excess gaps summing to \(n-h\), and divide by the \(h\) choices of a distinguished hole; the case \(h=0\) is unique. Each seeded-hub assignment uses \(k+1\) seeds; each unseeded-hub assignment uses \(k\). Summing these disjoint cases proves the enumerator. Weighting a seed assignment on \(j\) of the \(n+1\) vertices by \(p^jr^{n+1-j}\) gives the probability expression.

At most \(\lfloor n/2\rfloor\) rim vertices can be unseeded, so every successful assignment has at least \(\lceil n/2\rceil\) seeds. Equality requires the hub unseeded and a maximum independent rim-hole pattern. Such patterns exist for all \(n\), and the compressed cycle has \(k=\lceil n/2\rceil\ge3\) vertices; it admits a proper surjective three-colouring, of which there are
\(P_k(3)-3P_k(2)=2^k-3-(-1)^k>0\). Substitution into the enumerator proves the exact minimum and multiplicity.

## Verification
Run `python3 verify.py` with a standard Python 3 interpreter. The program performs three checks from distinct descriptions: symbolic cycle-colouring/binomial coefficients versus direct enumeration of seeded rim patterns for \(5\le n\le9\); formula hole-support coefficients versus independent-set bitmask enumeration for \(5\le n\le12\); and full brute-force simulation of the original four-colour local forcing process for every one of the \(5^{n+1}\) partial assignments when \(5\le n\le7\). It separately checks the minimum coefficients through \(n=12\). The run returned `VERIFY_OK (64 independently cross-checked identities)`. Finite exhaustive tests support but do not replace the infinite combinatorial proof above.

## Relationship to prior work
G. E. Farr's 2026 article develops the forced colouring function, its fundamental identities, and computational hardness (arXiv:2609.17108v1), building on the 2024 general graph-polynomial programme of G. E. Farr and K. Morgan (arXiv:2406.15746). The present formula studies the wheel family, not the general computational problem. Other previously reported exact formulas for three-colour forcing on paths/cycles concern a different graph and palette; their statements alone do not supply the unseeded-hub surjectivity criterion or the complete four-colour wheel coefficient enumeration. No historical-priority assertion beyond the sources actually compared is warranted.

## Limitations
The result concerns four **named** colours and the specified local forced-colouring rule, not ordinary precolouring extension without local forces. It covers \(n\ge5\) and does not treat other wheel conventions or arbitrary cones. The originality comparison cannot rule out an unlocated equivalent statement, such as a cycle-independent-set weighted formula.

## References
1. G. E. Farr, *The forced colouring function of a graph*, first publicly posted 2026-09-15, arXiv:2609.17108v1, https://arxiv.org/abs/2609.17108.
2. G. E. Farr and K. Morgan, *Graph polynomials: some questions on the edge*, arXiv:2406.15746, https://arxiv.org/abs/2406.15746.
