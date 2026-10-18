# A gain-independent three-phase two-leader law on \(K_{1,m,m+1}\)

## Finding

Let \(G_m=K_{1,m,m+1}\) be the simple, unweighted, complete tripartite graph, with parts \(U,B,C\) of sizes \(1,m,m+1\), respectively. For every integer \(m\ge1\) and every finite real gain \(\kappa>0\), select **two distinct vertices** \(S\) to minimize
\[
 J_m(S;\kappa)=\operatorname{tr}\!\left( L(G_m)+\kappa\sum_{v\in S}e_ve_v^{\mathsf T}\right)^{-1}.
\]
The unique minimizing orbit under graph automorphisms is
\[
\begin{array}{c|c}
 m & \text{two-leader placement}\\ \hline
 1 & \text{both vertices of }C\\
 2,3 & \text{two distinct vertices of }B\\
 m\ge4 & \text{the vertex of }U\text{ and one vertex of }B.
\end{array}
\]
Every other orbit has strictly greater objective for every \(\kappa>0\). In particular, the universal vertex of \(U\) is absent from every optimal pair at \(m=1,2,3\) and present in every optimal pair for \(m\ge4\): the topology threshold does **not** depend on the feedback gain.

## Assumptions and scope

All graph edges have unit conductance; each node experiences independent unit-intensity additive white noise in the corresponding noisy-consensus interpretation. Both chosen leaders have exactly the same positive, finite gain, and the other nodes have zero direct gain. The graph is connected. For \(m=1\), the two singleton parts \(U,B\) are interchangeable, and the only three pair orbits are singleton--singleton, singleton--\(C\), and \(C\)--\(C\). For \(m\ge2\), the five possible orbits, denoted \(UB,UC,BB,BC,CC\), exhaust all distinct two-vertex selections. We minimize the trace of the inverse itself, not the trace multiplied by the irrelevant positive noise factor \(1/2\).

## Proof

**1. A two-leader trace identity.** Let \(L\) be the Laplacian of any connected graph with unit electrical edge resistances, and let \(r\ne t\) be the leaders. Set \(R_{uv}=(e_u-e_v)^{\mathsf T}L^+(e_u-e_v)\), \(R=R_{rt}\), and
\[
 A=\sum_vR_{vr},\quad S=\frac12\sum_v(R_{vr}+R-R_{vt}),\quad
 Q=\frac14\sum_v(R_{vr}+R-R_{vt})^2,\quad g=1+\frac{\kappa R}{2}.
\]
Then the exact identity is
\[
 \boxed{J(\{r,t\};\kappa)=\frac{n}{2\kappa}+A+
 \frac{-S+nR/4-\kappa Q/2}{g}.}\tag{1}
\]
To prove it, set \(z_v=x_v-x_r\), with \(z_r=0\). The quadratic form of \(L+\kappa e_re_r^{\mathsf T}+\kappa e_te_t^{\mathsf T}\) becomes
\[
 z^{\mathsf T}Kz+\frac{\kappa}{2}z_t^2+2\kappa(x_r+z_t/2)^2,
\]
where \(K\) is \(L\) with row and column \(r\) deleted. The grounded Green matrix is \(G=K^{-1}\), and its entries are \(G_{uv}=(R_{ur}+R_{vr}-R_{uv})/2\); in particular \(G_{tt}=R\). The conditional variance of \(x_r\) given \(z\) is \(1/(2\kappa)\); the covariance of \(z\) is
\[
 (K+\kappa e_te_t^{\mathsf T}/2)^{-1}
 =G-\frac{\kappa}{2g}G_{\cdot t}G_{t\cdot}.
\]
Summing \(\operatorname{Var}(x_v)=1/(2\kappa)+\operatorname{Var}(z_v-z_t/2)\) over all vertices, including \(z_r=0\), yields (1). No independence of the \(z_v\)'s is assumed.

**2. Resistances of complete multipartite graphs.** In any unweighted \(K_{s_1,\ldots,s_q}\), write \(n=\sum_i s_i\). Distinct vertices in the same part of size \(a\) have resistance \(2/(n-a)\). Vertices in different parts of sizes \(a,b\) have resistance
\[
 R(a,b)=\frac{a-1}{a(n-a)}+\frac{b-1}{b(n-b)}+
 \frac{1/a+1/b}{n}.\tag{2}
\]
Indeed, the Laplacian acts by \(n-a\) on the within-part zero-sum subspace for a part of size \(a\), by \(n\) on the global-zero-sum part-constant subspace, and by zero on constants. Orthogonally projecting \(e_u-e_v\) to these spaces and dividing squared projection norms by their eigenvalues gives (2).

**3. The case \(m=1\).** The graph is the four-vertex complete graph with one missing edge; the missing edge joins the two vertices in \(C\). Direct substitution of (2) into (1), or exact inversion of the three representative matrices, gives
\[
\begin{aligned}
 J_{UU}&=\frac{\kappa^2+7\kappa+8}{\kappa(\kappa+4)},\\
 J_{UC}&=\frac{5\kappa^2+32\kappa+32}{\kappa(5\kappa+16)},\\
 J_{CC}&=\frac{3\kappa^2+18\kappa+16}{4\kappa(\kappa+2)}.
\end{aligned}
\]
The label \(UU\) means the pair of the two singleton vertices, not two vertices in the same singleton part. Both strict gaps are
\[
 J_{UU}-J_{CC}=\frac{\kappa(\kappa+6)}{4(\kappa+2)(\kappa+4)}>0,
 \qquad
 J_{UC}-J_{CC}=\frac{5\kappa^2+30\kappa+16}{4(\kappa+2)(5\kappa+16)}>0.
\]

**4. The cases \(m=2,3\).** Formulae (1)--(2) reduce the other four pair orbits to the following *strictly positive* gaps relative to \(BB\):

| Competing orbit | \(m=2:\ J_{\mathrm{other}}-J_{BB}\) | \(m=3:\ J_{\mathrm{other}}-J_{BB}\) |
|---|---|---|
| \(UB\) | \(\frac{\kappa^2+10\kappa+12}{3(\kappa+4)(3\kappa+16)}\) | \(\frac{\kappa(3\kappa+55)}{40(\kappa+5)(3\kappa+20)}\) |
| \(UC\) | \(\frac{(\kappa+3)(\kappa+8)}{4(\kappa+4)(2\kappa+9)}\) | \(\frac{19\kappa^2+391\kappa+1120}{40(\kappa+5)(11\kappa+64)}\) |
| \(BC\) | \(\frac{7\kappa^2+62\kappa+132}{(\kappa+4)(35\kappa+144)}\) | \(\frac{423\kappa^2+4555\kappa+12000}{40(\kappa+5)(63\kappa+320)}\) |
| \(CC\) | \(\frac{\kappa^2+7\kappa+24}{12(\kappa+3)(\kappa+4)}\) | \(\frac{\kappa^2+9\kappa+30}{10(\kappa+4)(\kappa+5)}\) |

**5. Every \(m\ge4\).** Write \(D_T=J_T-J_{UB}\). Substituting (2) into (1) and cancelling gives the exact quotient \(D_T=N_T/H_T\), with the following integer polynomials (here \(k=\kappa\) abbreviates only inside the display):
\[
\begin{aligned}
N_{UC}&=2[k^2(m^2-m)+k(4m^3+6m^2-m)+4m^4+18m^3+28m^2+18m+4],\\
H_{UC}&=(m+1)(m+2)(3k+4m+8)(3km+2k+4m^2+8m+4),\\[2pt]
N_{BB}&=k^2(2m^2-5m-6)+k(4m^3-3m^2-36m-28)
 +2m^4+4m^3-14m^2-40m-24,\\
H_{BB}&=2(m+1)(m+2)(k+m+2)(3k+4m+8),\\[2pt]
N_{BC}&=2m[k^2(2m^2+m-3)+k(4m^3+11m^2+2m-8)
 +2m^4+12m^3+26m^2+24m+8],\\
H_{BC}&=(m+1)(3k+4m+8)(4km^2+8km+3k+4m^3+16m^2+20m+8),\\[2pt]
N_{CC}&=k^2(2m^2+m-12)+k(4m^3+9m^2-23m-44)
 +2m^4+10m^3+10m^2-10m-12,\\
H_{CC}&=2(m+1)(m+2)(k+m+1)(3k+4m+8).
\end{aligned}\tag{3}
\]
For \(m\ge4\) and \(k>0\), every denominator is strictly positive. The numerators of \(UC\) and \(BC\) are visibly positive term by term for \(m\ge4\). For the remaining two, set \(u=m-4\ge0\). The coefficients of \(k^2,k,1\) in \(N_{BB}\) are respectively
\[
 2u^2+11u+6,\qquad4u^3+45u^2+132u+36,\qquad
 2u^4+36u^3+226u^2+552u+360,
\]
and those in \(N_{CC}\) are
\[
 2u^2+17u+24,\qquad4u^3+57u^2+241u+264,\qquad
 2u^4+42u^3+322u^2+1062u+1260.
\]
All six are strictly positive for \(u\ge0\). Thus all four competing orbits have strictly larger objective than \(UB\), completing the proof for every \(m\ge1\) and every \(\kappa>0\).

## Verification

Run `python3 verify.py` from the directory containing this file and the standalone script. It uses only standard-library exact rational arithmetic. The current script checks **320** effective-resistance versus closed-form evaluations on \(1\le m\le13\) at five exact gains, plus **87** independently formed matrix inversions on \(1\le m\le6\) at three exact gains. It also checks the four exact gap formulas at the tested parameters and their expected strict orderings. The infinite-parameter assertion rests on the derivations and coefficient positivity in Steps 1--5, not on finite enumeration.

## Relationship to prior work

Fitch and Leonard (first posted 7 July 2014; arXiv:1407.1569) derived general joint-centrality formulae for one and two noisy leaders and explicit optimization on paths and cycles. The trace identity in Step 1 is a compatible resistance-based rederivation of a special case of that general machinery. The new assertion here is **not** a new generic leader-selection identity; it is the full all-gain, all-size, strictly classified \(K_{1,m,m+1}\) optimizer, including the two topology thresholds. Patterson, Yi, and Zhang (arXiv:1708.06873) obtained general resistance-based expressions and explicit solutions for paths, cycles, and trees, not the displayed tripartite classification. Clark, Bushnell, and Poovendran (arXiv:1208.0946) study a supermodular leader-selection framework with noisy links and fixed leaders, a different noise model. Patterson, McGlohon, and Dyagilev (arXiv:1412.6595) solve path/ring cases. Neither the cited general formula nor these topological special cases states the three-phase optimizer law. General algorithms can of course numerically recover any fixed finite instance; that fact alone does not supply a single gain-uniform closed classification.

## Limitations

The classification is for a specific natural one-parameter family and exactly two equally weighted leaders. It does not cover arbitrary unbalanced multipartite graphs, directed edges, heterogeneous weights or feedback gains, or other control objectives. The algebraic strictness is established for finite \(\kappa>0\); endpoint limits are not asserted as uniqueness statements. This is a self-contained mathematical proof with reproducibility checks, but it has not undergone independent audit. The literature comparison cannot logically exclude inaccessible or unindexed publications stating an equivalent classification.

## References

1. K. E. Fitch and N. E. Leonard, *Joint Centrality Distinguishes Optimal Leaders in Noisy Networks*, arXiv:1407.1569 (first public version 2014-07-07), Sections II, V-B--V-D. https://arxiv.org/abs/1407.1569
2. A. Clark, L. Bushnell, and R. Poovendran, *A Supermodular Optimization Framework for Leader Selection under Link Noise in Linear Multi-Agent Systems*, arXiv:1208.0946 (2012-08-04). https://arxiv.org/abs/1208.0946
3. S. Patterson, N. McGlohon, and K. Dyagilev, *Efficient, Optimal k-Leader Selection for Coherent, One-Dimensional Formations*, arXiv:1412.6595 (2014-12-20). https://arxiv.org/abs/1412.6595
4. S. Patterson, Y. Yi, and Z. Zhang, *A Resistance Distance-Based Approach for Optimal Leader Selection in Noisy Consensus Networks*, arXiv:1708.06873 (2017-08-23), Sections III--IV. https://arxiv.org/abs/1708.06873
