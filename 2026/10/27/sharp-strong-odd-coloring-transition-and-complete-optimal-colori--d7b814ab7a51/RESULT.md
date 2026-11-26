# Exact census of named minimum strong odd colorings of fan graphs

## Finding

Let \(F_n=K_1\vee P_n\), where \(n\ge2\) is the number of vertices in the ordered path. A strong odd coloring is a proper coloring in which every color that occurs in an open neighborhood occurs there an odd number of times. Let \(N_n\) be the number of strong odd colorings of \(F_n\) using a fixed named palette of minimum size. We give an exact labeled census. The minimum palette size and characterization of admissible path words are prior results, used here to select which coefficients to count.

Let \(A_{n,k}\) count words of length \(n\) on a fixed named alphabet of \(k\) colors in which every color occurs an odd positive number of times and no equal symbols are at distance one or two. From the known exact minimum for clique–path joins [1], the number of path colors in an optimal coloring is \(n\) for \(2\le n\le6\); for \(n\ge7\), it is \(3\) if \(n\equiv3\pmod6\), \(4\) if \(n\) is even, and \(5\) otherwise. With \(k\) denoting this number for \(n\ge7\),
\[
N_n=\begin{cases}
(n+1)!,&2\le n\le6,\\
(k+1)A_{n,k},&n\ge7.
\end{cases}
\]
Writing \(H_k(t)=\sum_{n\ge2}A_{n,k}t^n\), the required coefficients are given by
\[
H_3(t)=\frac{6t^3}{1-t^6},\qquad
H_4(t)=\frac{24t^4(1-2t^2)^2}
{(1-4t^2)\bigl(1-(4t^3-t)^2\bigr)(1+t^2-4t^4)},
\]
\[
H_5(t)=\frac{120t^5(1-3t^2)^3}
{(1-9t^2)\bigl(1-(9t^3-2t)^2\bigr)
\bigl((1+2t^2-9t^4)^2-(t-3t^3)^2\bigr)}.
\]
For example, the exact counts \((N_7,N_8,N_9,N_{10},N_{11},N_{12})\) are \((720,120,24,2400,142560,13080)\).

## Assumptions and scope

Graphs are finite, undirected and simple. The apex is distinguished, path vertices are labeled and ordered, and colors are named. The census counts full colorings, not classes under reversal, graph automorphisms or color permutations. Optimal palettes are fully used. Each \(H_k\) is a formal power series and counts path words, not full-graph colorings.

## Proof

**Reduction to words.** The apex color is private by properness, and the condition at the apex requires each used path color to have odd multiplicity on the path. Adjacent path vertices must have distinct colors. Equal colors at distance two would occur twice in the open neighborhood of their middle path vertex, which otherwise sees only the private apex color. Conversely, under these conditions each path vertex sees a collection of distinct neighbor colors, and the apex sees the required odd multiplicities. This is the fan case of the admissible-word characterization in [1]. Fix the named full palette. Choosing its apex color determines the named path alphabet, and each admissible path word on that alphabet gives one coloring. This proves the factor \(k+1\); for \(2\le n\le6\) all vertices have different colors by the known minimum, giving \((n+1)!\).

**Parity projection.** For each sign assignment \(\varepsilon\in\{+1,-1\}^k\), the signed weight of a word \(w\) is \(\prod_i\varepsilon_{w_i}\). Averaging these weights with multiplier \(\prod_j\varepsilon_j\) projects onto words with every color odd: the average factors into \(\prod_j [2^{-1}\sum_{\varepsilon_j=\pm1}\varepsilon_j^{1+c_j(w)}]\), with \(c_j(w)\) the color count. In particular an absent color contributes zero.

For a fixed assignment with \(a\) positive and \(b\) negative colors, let \(m_+=a,m_-=b\) and \(s_+=1,s_-=-1\). A four-state transfer records the signs \((g,h)\) of the last two letters. Put
\[
v_{g,h}=s_gs_h m_g(m_h-\mathbf1_{g=h}),\qquad
M_{(g,h),(h,u)}=s_u(m_u-\mathbf1_{u=g}-\mathbf1_{u=h}),
\]
with all other matrix entries zero. The last two letters are distinct, so the two subtractions exclude distinct colors even when their signs coincide. Infeasible pairs have initial weight zero and are not reached from feasible pairs: whenever the proposed sign has no legal new letter the transition weight is zero. The signed series is therefore \(T_{a,b}(t)=t^2 v(I-tM)^{-1}\mathbf1\), where \(v\) is a row and \(\mathbf1\) is the all-ones column. Grouping assignments by the number of negative colors yields
\[
H_k(t)=2^{-k}\sum_{b=0}^k(-1)^b\binom{k}{b}T_{k-b,b}(t).
\]
For \(k=3\) each word is a prefix of a three-letter repetition and all counts are odd precisely for \(n\equiv3\pmod6\), giving the stated series directly. For \(k=4,5\) the displayed rational expressions follow by polynomial simplification of the transfer identity. For an exact check, for each summand put \(D_b=\det(I-tM)\) and \(R_b=t^2(\det(I-tM+\mathbf1 v)-D_b)\). The determinant lemma gives \(T_{k-b,b}=R_b/D_b\). If \(P_k/Q_k\) denotes the displayed formula, the polynomial identity to check is
\[
Q_k\sum_{b=0}^k(-1)^b\binom{k}{b}R_b\!\prod_{j\ne b}D_j=2^kP_k\prod_{b=0}^k D_b.
\]
The accompanying verifier checks that identity exactly. Each \(D_b\) and \(Q_k\) has constant term one, so this proves the stated simplification for formal series, not just for a finite range of coefficients.

## Verification

From the directory containing the result and companion script, run `python3 verify.py` (standard library only). The script forms the exact polynomial cross-products for all three series, checks the corresponding coefficients against a last-two-colors/parity-mask enumeration through length 25, and tests illustrative minimum-color templates and their six-step extensions through length 42. The coefficient and template tests are finite; the counting proof uses the parity projection and exact polynomial identities.

## Relationship to prior work and limitations

The exact threshold for every fan order, and the distance-two and parity characterization used in the reduction, are covered by the clique–path-join theorem [1], which explicitly takes fans as the case \(r=1\). That record's Limitations section excludes labeled optimum counts. Caro et al. [2, Prop. 3.2] already proved the individual seven-color example \(K_1\vee P_6\). The contribution here is the closed rational enumeration of named optima, not a new chromatic number theorem or a new general parity projection method. The wheel theorem of Manattu et al. [3, Theorem 1] concerns a cycle with wrap-around distance-two conditions and does not give the path-word census above. The full text of Pang–Miao–Fan [4] was not inspected, so specialized coverage there or in other unindexed work remains possible. No publication-priority claim or census of nonoptimal colorings is made.

## References

1. *Exact strong odd chromatic numbers of fan graphs and clique–path joins*, Resultary record `2026/10/18/SCOPE-exact-strong-odd-chromatic-numbers-of-fan-graphs-and-clique-path--0669234beb00`, [Finding and Limitations](https://github.com/Resultary/2026/blob/main/2026/10/18/SCOPE-exact-strong-odd-chromatic-numbers-of-fan-graphs-and-clique-path--0669234beb00/RESULT.md).
2. Y. Caro, M. Petruševski, R. Škrekovski and Z. Tuza, *On strong odd colorings of graphs*, [arXiv:2410.02336](https://arxiv.org/html/2410.02336v1).
3. A. J. Manattu, A. Vinay and A. Lakshmanan S., *On a conjecture about the strong odd chromatic number of planar graphs*, [arXiv:2602.03259](https://arxiv.org/html/2602.03259).
4. Pang, Miao and Fan, *On odd and strong odd colorings of graphs*, *Discrete Mathematics*, [DOI 10.1016/j.disc.2025.114683](https://doi.org/10.1016/j.disc.2025.114683).
