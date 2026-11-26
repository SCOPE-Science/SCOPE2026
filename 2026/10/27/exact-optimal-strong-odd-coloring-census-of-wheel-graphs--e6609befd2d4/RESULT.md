# Exact optimal strong odd coloring census of wheel graphs

## Finding

Let \(W_n=K_1\vee C_n\), where \(n\ge3\) is the rim length. A strong odd coloring is proper, and every color present in an open neighborhood occurs there an odd number of times. Let \(N_n\) count colorings from a fixed palette of exactly \(\chi_{\rm so}(W_n)\) named colors, with all vertices distinguished. No quotient by graph automorphisms or color permutations is taken. Then
\[
N_n=\begin{cases}
(n+1)!,&3\le n\le8,\\
24,&n\ge9,\ n\equiv3\pmod6,\\
65{,}409{,}120,&n=14,\\
5A_4(n),&n\ge10\text{ even},\ n\ne14,\\
6A_5(n),&n\ge11\text{ odd},\ n\not\equiv3\pmod6.
\end{cases}
\]
For the polynomials below, let \(s_{k,r}(n)\) be the sum of the \(n\)-th powers of their roots, counted with algebraic multiplicity. The integer-valued functions used in the census have the following parity domains:
\[
\begin{aligned}
A_4(n)&=\tfrac18\bigl(s_{4,0}(n)-4s_{4,1}(n)+3s_{4,2}(n)\bigr),&&n\ge3\text{ even},\\
A_5(n)&=\tfrac1{16}\bigl(s_{5,0}(n)-5s_{5,1}(n)+10s_{5,2}(n)\bigr),&&n\ge3\text{ odd}.
\end{aligned}
\]
\[
\begin{aligned}
P_{4,0}(t)&=(t-2)(t-1)^3(t+1)^2(t^2+t+2)^3,\\
P_{4,1}(t)&=(t-1)(t^3-t^2+4)(t^4+t^3+t^2+t+2)^2,\\
P_{4,2}(t)&=(t^2+1)(t^3-t-2)(t^3-t+2)(t^4+t^2-4),\\
P_{5,0}(t)&=(t-3)(t-1)^6(t+1)^5(t^2+t+3)^4,\\
P_{5,1}(t)&=(t-1)^3(t+1)^2(t^3-2t^2+9)(t^4+t^3+2t^2+t+3)^3,\\
P_{5,2}(t)&=(t-1)(t^2+1)^2(t^3-2t-3)(t^4+t^3+t+3)^2(t^4-t^3+2t^2+3t-9).
\end{aligned}
\]
On even orders \(N_n\sim(5/8)2^n\); on either odd class \(1\) or \(5\bmod6\) it is asymptotic to \((6/16)3^n\). On the odd class \(3\bmod6\) it is constant, including \(N_3=24\).

## Proof

**Rim characterization and optimal palettes.** The hub has a color not used on the rim. At each rim vertex its two rim neighbors must have distinct colors (otherwise their common color occurs twice in its neighborhood), and properness forces both to differ from the vertex's own color. Conversely these local conditions make the three neighbor colors distinct at each rim vertex; the hub then requires each used rim color to have odd multiplicity. Let \(B_k(n)\) count cyclic words on \(k\) named rim colors in which all colors occur with odd multiplicity and each cyclic consecutive triple has distinct entries. If the optimal palette has \(k+1\) colors, the required count is \((k+1)B_k(n)\).

For \(n\le8\) a rim color occurs on at most two vertices because consecutive occurrences must be at least three steps apart; odd multiplicity forces one occurrence. This gives \((n+1)!\). Exactly three rim colors are possible precisely at \(n\equiv3\pmod6\), by the forced period-three pattern and the odd-multiplicity condition. There are \(3!\) words on the fixed rim palette in that case. For even \(n\) the number of rim colors is even, so at least four are needed. At \(n=14\) each color occurs at most \(\lfloor14/3\rfloor=4\) times, hence at most three times by oddness; four cannot suffice, so six are needed. Odd \(n\ge11\) outside the period-three case needs at least five. The following witnesses attain the lower bounds:

| \(n\) | Rim word |
|---:|:---|
| 10 | `0120120123` |
| 11 | `01201201234` |
| 12 | `012013023123` |
| 13 | `0120123013243` |
| 14 | `01201203123453` |
| 18 | `012012012013023123` |
| 20 | `01201203103123023123` |

The cyclic triples and odd multiplicities can be checked in each word. For the recurrence in length, insert `012012` after the first `012` in any of the witnesses beginning `012012`. The boundary two-letter contexts repeat unchanged and each of the three inserted colors gains two occurrences. Use lengths \(10,18,20\) for the even progressions, with 12 and 14 treated separately, and 11 and 13 for the two remaining odd progressions.

**Exact counts.** For \(\epsilon\in\{-1,1\}^k\), index an integer matrix \(T(\epsilon)\) by ordered distinct-color pairs. Its entry from \((a,b)\) to \((b,c)\) is \(\epsilon_c\) if \(c\notin\{a,b\}\) and zero otherwise. The trace of the \(n\)-th power counts indexed cyclic words by their sign product; the state at index 0 is determined by the word, so no extra factor of \(n\) occurs. For each individual color the projection onto odd occurrences gives a factor \((1-(-1)^{m})/2\) at multiplicity \(m\). Expanding the product,
\[
B_k(n)=2^{-k}\sum_{\epsilon\in\{-1,1\}^k}\Bigl(\prod_c\epsilon_c\Bigr)\operatorname{tr}(T(\epsilon)^n).
\]
Signs with \(r\) negative entries give similar matrices by relabeling; write \(T_{k,r}\) for one representative. The six displayed \(P_{k,r}\) are \(\det(tI-T_{k,r})\). The coefficients can be reproduced by Newton identities: if \(P(t)=\sum_{j=0}^d a_jt^{d-j}\), with \(a_0=1\), then \(ja_j=-\sum_{i=1}^j a_{j-i}\operatorname{tr}(T_{k,r}^i)\), where \(d=k(k-1)\). Also \(\operatorname{tr}(T_{k,r}^n)=s_{k,r}(n)\), including repeated roots. Complementing all signs negates the matrix and multiplies the prefactor by \((-1)^k\), so for \(n\equiv k\pmod2\) the \(r\) and \(k-r\) terms add when distinct. Grouping with weights \((-1)^r\binom kr\) gives exactly \(B_4(n)=A_4(n)\) and \(B_5(n)=A_5(n)\) on the specified domains, proving integrality there. The same projection at \((k,n)=(6,14)\) gives \(B_6(14)=9{,}344{,}160\), hence \(N_{14}=7B_6(14)\).

**Growth.** For \(k=4,5\) the all-positive matrix is irreducible. Every ordered edge \((a,b)\) can advance to \((b,c)\) for \(c\ne a,b\), and can reach \((b,a)\) by the sequence \((a,b),(b,c),(c,d),(d,b),(b,a)\) using four distinct colors. Thus all ordered edges communicate. Cycles of lengths three and four make the matrix primitive, and its row sum \(k-2\) is its simple dominant eigenvalue. In the equality case of Perron–Frobenius comparison, a signed matrix with spectral radius \(k-2\) would be a unit complex scalar times a diagonal-unitary conjugate of the unsigned matrix. Then every directed 3-cycle would have the same sign product. These products are \(\epsilon_a\epsilon_b\epsilon_c\) for all distinct \(a,b,c\). Comparing triples containing the same two colors forces equality of the signs of any two remaining colors, possible only for a uniform sign vector. The mixed-sign terms are therefore exponentially smaller. On the parity-matched lengths the two uniform terms add and give \(B_k(n)\sim 2^{1-k}(k-2)^n\). The growth statements follow with the hub factor.

## Verification

The accompanying `verify.py` recomputes the six characteristic polynomials with exact integer arithmetic, checks the resulting trace-power formulas against a parity-state dynamic program, and checks the exceptional count by both signed traces and dynamic programming. In the latter method one fixes the initial ordered colors, extends by a color distinct from the last two, toggles that color in the odd-occurrence mask, and retains only all-odd masks and endings with both wraparound triples distinct. The script also checks the witnesses and small wheel orders. Sample values are \(A_4(10)=240\), \(A_4(12)=1416\), \(A_4(16)=6144\), \(A_5(11)=11880\), and \(A_5(13)=145080\). The unbounded claims use the proof rather than extrapolation from tested lengths.

## Relationship to prior work and limitations

Kwon and Park introduced strong odd coloring ([arXiv:2401.11653](https://arxiv.org/abs/2401.11653)); Caro, Petruševski, Škrekovski and Tuza developed the theory, including adjoining a universal vertex ([arXiv:2410.02336](https://arxiv.org/abs/2410.02336)). Manattu, Vinay and Lakshmanan, [arXiv:2602.03259](https://arxiv.org/abs/2602.03259), Observations 1–2 and Theorem 1, already give the rim parity and distance-two conditions and determine the optimal palette, including the exceptional order 14. The contribution here is the exact number of optimal named colorings and its growth laws, not these structural facts. A general chromatic symmetric function encodes color-class sizes, but using that definition without evaluating the relevant odd-size profiles of the cycle square does not give the explicit census. These comparisons do not establish absolute publication priority.

The formula concerns optimal palettes on wheels with distinguished vertices, not nonoptimal colorings or dihedral orbits. The leading asymptotics differ among the odd congruence classes; there is no single one of the stated asymptotics on all odd orders.
