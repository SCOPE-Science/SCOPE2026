# Exact optimal strong odd coloring census of wheel graphs

## Finding
For each integer \(n\ge3\), let \(W_n=K_1\vee C_n\) be the wheel with a distinguished hub and a cyclically indexed rim of length \(n\). A strong odd coloring is proper and every color appearing in any open neighborhood appears there an odd number of times. Let \(N_n\) count all such colorings using exactly \(\chi_{\mathrm{so}}(W_n)\) named colors, with the hub and each rim vertex distinguished. Two colorings related by a color permutation are different.

The following **complete all-order census** holds:
\[
N_n=\begin{cases}
(n+1)!,&3\le n\le8,\\
24,&n\ge9,\ n\equiv3\pmod6,\\
65{,}409{,}120,&n=14,\\
5A_4(n),&n\ge10\text{ even},\ n\ne14,\\
6A_5(n),&n\ge11\text{ odd},\ n\not\equiv3\pmod6.
\end{cases}
\]
The integer-valued sequences \(A_4\) and \(A_5\) have explicit closed algebraic formulas described below. This is a count of *optimal configurations*, not a new determination of the optimal number of colors: the latter was obtained by Manattu, Vinay, and Lakshmanan (2026).

For each polynomial \(P_{k,r}(t)\) displayed below, define its integer power sum \(s_{k,r}(n)\) as the sum of the \(n\)-th powers of all complex roots, **with algebraic multiplicity**. Define
\[
A_4(n)=\frac{s_{4,0}(n)-4s_{4,1}(n)+3s_{4,2}(n)}8,
\qquad
A_5(n)=\frac{s_{5,0}(n)-5s_{5,1}(n)+10s_{5,2}(n)}{16}.
\]
All six factored polynomials are fully explicit:
\[
\begin{aligned}
P_{4,0}(t)&=(t-2)(t-1)^3(t+1)^2(t^2+t+2)^3,\\
P_{4,1}(t)&=(t-1)(t^3-t^2+4)(t^4+t^3+t^2+t+2)^2,\\
P_{4,2}(t)&=(t^2+1)(t^3-t-2)(t^3-t+2)(t^4+t^2-4),\\[3pt]
P_{5,0}(t)&=(t-3)(t-1)^6(t+1)^5(t^2+t+3)^4,\\
P_{5,1}(t)&=(t-1)^3(t+1)^2(t^3-2t^2+9)(t^4+t^3+2t^2+t+3)^3,\\
P_{5,2}(t)&=(t-1)(t^2+1)^2(t^3-2t-3)(t^4+t^3+t+3)^2\\
&\hspace{1cm}\cdot(t^4-t^3+2t^2+3t-9).
\end{aligned}
\]
In particular, as \(n\) tends to infinity through even integers,
\[
N_n\sim\frac58\,2^n.
\]
As \(n\) tends to infinity through either odd residue class \(1\) or \(5\) modulo \(6\),
\[
N_n\sim\frac6{16}\,3^n,
\]
whereas \(N_n=24\) for every \(n\equiv3\pmod6\). Thus three equally spaced odd residue classes have radically different optimizer multiplicities: two grow exponentially and one stays constant.

## Assumptions and scope
All graphs are finite, simple, and their vertices are labeled. The rim of \(W_n\) is \(C_n\), not a cycle with \(n+1\) vertices. A palette of exactly \(\chi_{\mathrm{so}}(W_n)\) named colors is fixed and all its colors necessarily occur. No quotient is taken by graph automorphisms or by color permutations.

Write \(B_k(n)\) for the number of cyclic rim words \((c_0,\ldots,c_{n-1})\in[k]^n\) for which every one of the \(k\) colors occurs an odd positive number of times and \(c_i,c_{i+1},c_{i+2}\) are pairwise distinct for all cyclic indices. A wheel strong odd coloring is exactly a word counted by \(B_k(n)\) plus an independently chosen hub color different from all rim colors. For the optimal cases of the theorem, \(k=\chi_{\mathrm{so}}(W_n)-1\) and \(N_n=(k+1)B_k(n)\).

## Proof
**1. Reduction to a parity-restricted square coloring.** The hub has its own color by properness. At a rim vertex, its two rim neighbors cannot share a color: that color would occur exactly twice among its three neighbors, as the hub color is distinct. The two rim neighbors and their common rim vertex therefore have pairwise distinct colors. Conversely, if the rim is properly colored at cyclic distances one and two, every rim vertex sees three distinct colors; the hub sees each rim color as often as that color occurs on the rim. Hence the stated parity and local-distinctness conditions are both necessary and sufficient.

**2. Identification of the optimal palette size.** For \(3\le n\le8\), a color can appear on at most two rim vertices at pairwise cyclic distance at least three, so the odd-size requirement forces each color class to be a singleton. Consequently every vertex has a distinct color. For \(n\ge9\), any three-color square coloring is forced to repeat a pattern of three colors, and it has all three rim class sizes odd exactly when \(n\equiv3\pmod6\). If \(n\) is even, the number of used rim colors is even, so at least four are required; at \(n=14\), four odd color classes have size at most three each and cannot cover 14 vertices, forcing six. If \(n\) is odd but not \(3\pmod6\), the number of used rim colors is odd and at least five. These lower bounds are attained by the following rim words, where a digit denotes one named color:

| Rim order | Explicit witness |
| --- | --- |
| \(10\) | `0120120123` |
| \(11\) | `01201201234` |
| \(12\) | `012013023123` |
| \(13\) | `0120123013243` |
| \(14\) | `01201203123453` |
| \(18\) | `012012012013023123` |
| \(20\) | `01201203103123023123` |

Every witness satisfies the cyclic distance-two restriction and has all class sizes odd. For any displayed witness beginning `012012`, insert `012012` immediately after its first three digits. The resulting cyclic word remains distance-two proper, while each of the first three class sizes increases by two. Repeating gives the needed witnesses in every congruence class of all sufficiently large orders. The three-periodic word supplies all \(n\equiv3\pmod6\). Thus the indicated palette sizes are optimal in all cases. (This scalar classification is also in Manattu–Vinay–Lakshmanan, Theorem 1; it is included here only to establish the exact domain of the counting claim.)

**3. Exact root-sum enumeration.** For any \(k\ge3\), take the \(k(k-1)\) ordered distinct-color pairs \((a,b)\) as states. For a sign vector \(\boldsymbol\epsilon\in\{-1,1\}^k\), let \(T(\boldsymbol\epsilon)\) have entry \(\epsilon_c\) from \((a,b)\) to \((b,c)\) when \(c\notin\{a,b\}\), and zero otherwise. A directed closed walk of length \(n\) is exactly a cyclic distance-two proper rim coloring, and its transition-weight product is \(\prod_i\epsilon_{c_i}\). Expanding the indicator that every color class is odd gives the exact parity projection
\[
B_k(n)=\frac1{2^k}\sum_{\boldsymbol\epsilon\in\{-1,1\}^k}
\left(\prod_{c=1}^k\epsilon_c\right)
\operatorname{tr}\!\left(T(\boldsymbol\epsilon)^n\right).
\]
Grouping sign vectors by the number \(r\) of negative entries, write \(T_{k,r}\) for the corresponding matrix. Its characteristic polynomial is \(P_{k,r}\), and its trace powers equal the root sums \(s_{k,r}(n)\). The six displayed factorizations follow from direct determinant computation of the concrete \(12\)- and \(20\)-dimensional integer matrices; the standalone verifier independently recomputes every characteristic coefficient from exact Newton identities, not floating-point roots. As \(T_{k,k-r}\) is permutation-similar to \(-T_{k,r}\), the parity sum for even \(n\) with \(k=4\) becomes exactly \(A_4(n)\), and for odd \(n\) with \(k=5\) becomes exactly \(A_5(n)\). Multiplying by the \(k+1\) choices of hub color proves the two infinite formulas.

For \(n=14\), the same parity projection using all \(64\) sign vectors of the \(30\)-state transfer matrix gives \(B_6(14)=9{,}344{,}160\), hence \(N_{14}=7B_6(14)=65{,}409{,}120\). The attached independent parity-dynamic-program calculation yields the identical integer. For \(3\le n\le8\), all \(n+1\) vertices have distinct colors, giving \((n+1)!\). For \(n\equiv3\pmod6\), the three-periodic rim has exactly \(3!\) labeled colorings and the hub has four choices, giving \(24\).

**4. Asymptotics.** The unsigned transition matrix \(T(\boldsymbol1)\) is the adjacency matrix of an irreducible directed graph of ordered distinct color pairs. This graph has directed cycles of lengths three and four, so it is primitive for \(k=4,5\). Every row has exactly \(k-2\) ones, hence its simple Perron eigenvalue is \(k-2\). If a mixed-sign matrix had spectral radius \(k-2\), equality in the Perron–Frobenius comparison would make all signed products along directed three-cycles have the same complex phase. These products are \(\epsilon_a\epsilon_b\epsilon_c\) for every triple of distinct colors. When \(k\ge4\), their equality forces every \(\epsilon_c\) to have the same sign, contradicting the mixed-sign assumption. Thus every mixed-sign matrix has strictly smaller spectral radius. Only the all-positive and all-negative terms contribute the leading exponential to the parity projection. For \(n\) of the same parity as \(k\), these two contributions add, giving
\[
B_k(n)\sim 2^{1-k}(k-2)^n
\quad(k=4,5).
\]
The asserted optimizer-count asymptotics follow by multiplying by the hub-color choices.

## Verification
The included standalone `verify.py` uses integer arithmetic only. It recomputes all six matrix characteristic polynomials by Newton identities; checks the root-sum formulas against a separately implemented parity-state dynamic program for 26 even and 25 odd orders; independently computes the exceptional \(n=14\) count by both signed traces and dynamic programming; and directly enumerates canonical rim set partitions for orders \(3\) through \(11\), evaluating the original wheel neighborhood condition. It also verifies the seven displayed construction words and forty length-\(6\) insertion instances. The verifier prints `VERIFICATION_OK` only if every assertion succeeds. Small-case sample values are \(A_4(10)=240\), \(A_4(12)=1416\), \(A_4(16)=6144\), \(A_5(11)=11880\), and \(A_5(13)=145080\).

## Relationship to prior work
Kwon and Park (2024, arXiv:2401.11653) introduced strong odd coloring. Caro, Petruševski, Škrekovski, and Tuza (2024, arXiv:2410.02336) developed the notion further, including the effect of adjoining a universal vertex. Most importantly, Manattu, Vinay, and Lakshmanan (2026, arXiv:2602.03259, Theorem 1) **already determine the exact strong odd chromatic number of every wheel** and explicitly identify the odd-class and distance-two conditions. That scalar theorem is not claimed here. It does not provide the optimizer counts, their six explicit algebraic characteristic polynomials, the exceptional 14-rim count, or the optimizer-growth asymptotics in this result. The general chromatic symmetric function of a graph formally encodes color-class sizes, but a general definition or deletion–contraction method is not an evaluated all-order formula for these particular parity restrictions on the squared cycles.

## Limitations
The all-order census concerns wheel graphs only, with named colors and distinguished vertices. The formula does not count non-optimal strong odd colorings nor identify dihedral orbits. The spectral asymptotics describe the indicated congruence classes; there is no single growth law along all odd orders. Source inspection and research-record searches cannot establish absolute publication priority; an undiscovered formula for the relevant chromatic symmetric functions of cycle squares could subsume the enumerative claim. All independent external scientific validation remains unperformed.

## References
1. H. Kwon and B. Park, *Strong odd coloring of sparse graphs*, arXiv:2401.11653, initially public 22 January 2024, https://arxiv.org/abs/2401.11653.
2. Y. Caro, M. Petruševski, R. Škrekovski, and Z. Tuza, *On strong odd colorings of graphs*, arXiv:2410.02336, initially public 3 October 2024, https://arxiv.org/abs/2410.02336.
3. A. J. Manattu, A. Vinay, and A. Lakshmanan S., *On a conjecture about the strong odd chromatic number of planar graphs*, arXiv:2602.03259, initially public 3 February 2026, https://arxiv.org/abs/2602.03259.
4. R. P. Stanley, *A symmetric function generalization of the chromatic polynomial of a graph*, Advances in Mathematics 111 (1995), 166–194.
