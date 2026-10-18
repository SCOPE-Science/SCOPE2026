# Minimum-weight Italian domination profiles of paths and cycles

## Finding
Let \(d_I(G,k)\) count functions \(f:V(G)\to\{0,1,2\}\) of weight \(k=\sum_v f(v)\) such that every zero-labelled vertex has sum of neighbour labels at least \(2\). Write \(\gamma_I(G)=\min\{k:d_I(G,k)>0\}\). For all paths \(P_n\), \(n\ge1\), and all cycles \(C_n\), \(n\ge3\), the *lowest nonzero coefficient* of the Italian domination polynomial is exactly
\[
 d_I(P_n,\gamma_I(P_n))=\begin{cases}
 2,&n=3,\\
 n/2+3,&n=6,\\
 n/2+2,&n\text{ even and }n\ne6,\\
 1,&n\text{ odd and }n\ne3,
 \end{cases}
\]
and
\[
 d_I(C_n,\gamma_I(C_n))=\begin{cases}
 6,&n=3,\\
 2,&n\ge4\text{ even},\\
 n,&n\ge5\text{ odd}.
 \end{cases}
\]
The respective minimum weights are \(\gamma_I(P_n)=\lfloor n/2\rfloor+1\) and \(\gamma_I(C_n)=\lceil n/2\rceil\). Both values were known; the new result here is the complete minimizer classification and the closed lowest-coefficient formulas for all orders. The path \(P_6\) has one exceptional minimum labeling with two labels equal to \(2\), namely \((0,2,0,0,2,0)\).

## Assumptions and scope
Graphs are simple and have the usual path ordering or fixed labelled cyclic ordering; reversal/rotation does not identify distinct functions. Each \(C_n\) has \(n\ge3\). Every statement concerns standard Italian (equivalently Roman \(\{2\}\)) domination, not perfect, secure, signed, or double Italian domination. The coefficient counts assignments to named vertices, not orbits under graph automorphisms.

An equivalent exact classification is:

* On \(P_{2m+1}\) for \(m\ge2\), exactly the alternating binary labeling beginning and ending with \(1\); on \(P_1\) only \((1)\); on \(P_3\), \((1,0,1)\) and \((0,2,0)\).
* On \(P_{2m}\), \(m\ge1\), exactly the \(m\) binary labelings whose \(m-1\) zeros are a nonadjacent subset of the \(2m-2\) internal vertices, and the two nonbinary patterns \(02(01)^{m-1}\) and its reversal (here string exponent means literal repeated concatenation). In addition \(P_6\) admits \(020020\). The notation \(02(01)^{m-1}\) describes a word of length \(2m\); it is not multiplication.
* On \(C_{2m}\), \(m\ge2\), exactly the two alternating binary labelings. On \(C_{2m+1}\), \(m\ge2\), exactly the \(2m+1\) binary labelings with an independent zero set of cardinality \(m\). On \(C_3\), the three labelings with exactly one zero and the other two entries one, and the three with exactly one two and the other two entries zero.

## Proof
Write \(Z=\{v:f(v)=0\}\), \(O=\{v:f(v)=1\}\), \(T=\{v:f(v)=2\}\), with cardinalities \(z,o,t\), and weight \(w=o+2t\). Every zero has neighbour-weight at least \(2\), while a nonzero vertex contributes at most twice its label toward the summed zero-neighbour weights because paths and cycles have maximum degree two. Thus
\[
2z\le\sum_{v\in Z}\sum_{u\sim v} f(u)\le2o+4t=2w.
\]
Since \(n=z+o+t=z+w-t\), we have \(t\le2w-n\). Equality \(z=w\) in the inequalities forces *every nonzero vertex to have two zero-neighbours* and *every zero vertex to receive neighbour-weight exactly two*. This is the key equality rigidity, and includes the restriction that an endpoint cannot be nonzero when equality holds.

First establish the minimum weights without assuming them. For \(C_n\), \(w\ge\lceil n/2\rceil\), attained by choosing a maximum independent zero set and assigning \(1\) elsewhere. For odd paths the same binary pattern attains \(\lceil n/2\rceil=\lfloor n/2\rfloor+1\). If \(n=2m\) is even, \(w\le m\) would force \(w=m\), \(t=0\), \(z=m\). Without any \(2\)-label a zero cannot be at a degree-one endpoint, and zeros cannot be consecutive. But the \(2m-2\) interior path vertices contain at most \(m-1\) nonconsecutive vertices, a contradiction. Therefore \(w\ge m+1\); alternating \(1,0,1,0,\ldots,1,1\) attains it. For \(P_1\), the minimum is \(1\).

Two elementary local observations now classify the minimizers. When \(t=0\), every zero must be internal and have two neighbours labelled \(1\); hence the zero vertices form an independent set avoiding endpoints in a path. The number of size-\(r\) independent subsets of a path with \(s\) vertices is \(\binom{s-r+1}{r}\), obtained by removing the required gaps. On \(P_{2m+1}\), the required \(z=m\) zeros have only one possible internal independent set. On \(P_{2m}\), the required \(z=m-1\) zeros give \(\binom{m}{m-1}=m\) possibilities. On \(C_{2m}\), the required \(m\) zeros give two alternating choices; on \(C_{2m+1}\), the required \(m\) zeros give \(2m+1\) choices. On \(C_3\), the \(t=0\) case gives three choices.

If \(t=1\) on a path, two consecutive zeros are impossible: each would require an external neighbour labelled \(2\), which would require two distinct twos; consecutive zeros at an endpoint are also impossible. On an even path \(P_{2m}\), any \(m\)-vertex independent zero set must meet at least one endpoint (the interior contains at most \(m-1\) independent vertices). Both endpoints cannot be zero since they would demand two distinct neighbouring twos, so precisely one endpoint is zero. For a fixed zero endpoint the only independent \(m\)-set is the alternating set containing it. Its immediate neighbour must be the unique \(2\), proving exactly the two mirror patterns specified above. On odd \(P_{2m+1}\), \(t=1\) requires \(z=m+1\), the unique maximum independent set of the path, containing both endpoints. Both ends need a neighbouring \(2\); these neighbours coincide only when \(n=3\). This yields the exceptional \(020\).

If \(t=2\) on an even path, the equality \(z=w\) applies. Its first and last vertices must be zero and their immediate neighbours must both be two. The left end therefore begins \(0,2,0,0\): the third zero has its already-required neighbour-weight \(2\) from the second vertex, hence its other neighbour is zero. The fourth zero must have its next neighbour equal to two. Since there are exactly two twos, this next neighbour must also be the penultimate vertex. Thus \(n=6\), with unique labeling \(020020\). The case \(t\ge3\) is excluded by \(t\le 2w-n\). For odd paths \(t\ge2\) is excluded by the same inequality.

For cycles, the inequality gives \(t=0\) at even order. At odd order it gives \(t\le1\). If \(t=1\) on \(C_n\), then \(z=(n+1)/2\) and at least two zeros are adjacent. On a cycle of length \(n\ge4\), the two zeros would need *two distinct external neighbours* labelled \(2\), contradicting \(t=1\). The exception \(C_3\) has the same other vertex adjacent to both zeros, so the three rotations of \(200\) are valid. Combining the cases proves the classification and every coefficient formula.

## Verification
The accompanying standalone `verify.py` directly enumerates labelled assignments and checks the original Italian condition, without using any classification, for paths of orders \(1\) through \(11\) and cycles of orders \(3\) through \(11\). It also uses an independently implemented two-step boundary-conditioned transfer recurrence for orders through \(120\). The code asserts minimum weights and coefficient formulas in all these tests. Execute `python3 verify.py`; its previously observed output is in `verify_output.txt`. These finite tests corroborate, but do not substitute for, the unrestricted proof above.

## Relationship to prior work
Shao and Zhao (2026, arXiv:2610.00108v1) define the Italian domination polynomial and provide a dynamic program computing every coefficient of paths and cycles. They also tabulate complete coefficient lists for paths through order \(10\) and cycles through order \(12\), and give closed formulas for coefficients **near the maximum weight**; their work is acknowledged as covering numerical instances and the general coefficient-computation algorithm. The present contribution extracts explicit all-order formulas and a complete structural classification **at the minimum weight**, including the unique \(P_6\) double-two exception. The minimum-weight values themselves are established in earlier Italian/Roman \(\{2\}\) domination literature and are not claimed new. The older Roman \(\{2\}\) paper concerns minimum weights and properties of optimal functions rather than providing the stated pair of all-order counting formulas in the material inspected.

## Limitations
No result is asserted for trees other than paths or for graph families other than paths and cycles. This does not give the whole Italian domination polynomial: the recent dynamic programs already do that algorithmically. Priority could be affected by an uncatalogued enumeration of minimum Roman \(\{2\}\)/Italian dominating functions or a result implicit in earlier work. Independent scholarly validation has not been performed.

## References
1. P. Shao and C. Zhao, *Counting Weight-\(k\) Italian Dominating Sets on Trees and Cycles*, arXiv:2610.00108v1, publicly posted September 9, 2026. https://arxiv.org/abs/2610.00108 . Sections 1, 2, 7, 8.
2. M. Chellali, T. W. Haynes, S. T. Hedetniemi, A. A. McRae, *Roman \(\{2\}\)-domination*, Discrete Applied Mathematics 204 (2016), 22–28, https://doi.org/10.1016/j.dam.2015.11.013 .
