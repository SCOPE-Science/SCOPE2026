# Separated sharp dimension peaks for cut–cycle endpoint norms of rank-three Kneser graphs

## Finding
For each integer \(n\ge7\), let \(G_n=KG(n,3)\) have the three-element subsets of \([n]\) as vertices and edges joining disjoint subsets. Fix any reference orientation of the edges, write \(D_n\) for the vertex–edge incidence matrix, and set
\[
Q_n=D_n^{\mathsf T}(D_nD_n^{\mathsf T})^+D_n,
\qquad P_n=I-Q_n.
\]
These are the canonical Euclidean-orthogonal projections of the real edge-coordinate space onto the cut and cycle spaces, respectively. The induced real \(\ell_1\)- and \(\ell_\infty\)-norms of each projection agree. Put
\[
F(n)=n^7-13n^6-74n^5+2810n^4-26525n^3+122879n^2-275982n+224208,
\]
\[
H(n)=n^6-11n^5-39n^4+1373n^3-10024n^2+30732n-29808,
\quad W(n)=n^2-10n+27.
\]
Then for every integer \(n\ge7\) the exact endpoint norms are
\[
\boxed{\|Q_n\|_{1\to1}=\|Q_n\|_{\infty\to\infty}
=\frac{2F(n)}{n(n-5)(n-4)(n-2)(n-1)W(n)}}
\]
and
\[
\boxed{\|P_n\|_{1\to1}=\|P_n\|_{\infty\to\infty}
=\frac{3H(n)}{n(n-4)(n-2)(n-1)W(n)}}.
\]
Every edge column has the stated absolute column sum. The sharp, distinct global dimension peaks are
\[
\boxed{\sup_{n\ge7}\|Q_n\|=\frac{257}{77}\quad\text{at exactly }n=8},
\qquad
\boxed{\sup_{n\ge7}\|P_n\|=\frac{143}{35}\quad\text{at exactly }n=9}.
\]
The norms strictly decrease for every successive \(n\ge9\), and their large-dimension expansions are
\[
\|Q_n\|=2+\frac{18}{n}-\frac{144}{n^2}+O(n^{-3}),
\qquad
\|P_n\|=3+\frac{18}{n}-\frac{144}{n^2}+O(n^{-3}).
\]

## Assumptions and scope
All edges have unit conductance. The domain is the real edge space equipped with either endpoint coordinate norm; the projections are the canonical Euclidean-orthogonal ones, not minimizers over all possible projections. The graph \(KG(n,3)\) is connected for \(n\ge7\): any two triples differing in one element have a common disjoint neighbor, and such one-element exchanges connect all triples. There are \(N=\binom n3\) vertices and degree \(d=\binom{n-3}{3}\). The upper and lower endpoint norms coincide because the projection matrices are symmetric; edge transitivity makes every absolute column sum equal.

## Proof
**Dipole reduction.** Fix disjoint triples \(A=\{1,2,3\}\) and \(B=\{4,5,6\}\). Let \(f\) be the unique mean-zero solution to
\[
L_G f=\mathbf1_A-\mathbf1_B,
\qquad L_G=D_nD_n^{\mathsf T}.
\]
For an edge oriented from \(A\) to \(B\), the corresponding column of \(Q_n\), up to its irrelevant overall sign, comprises the differences \(f(S)-f(T)\) on all graph edges. Consequently its absolute column sum is the graph total variation
\[
\mathcal T(f)=\sum_{\{S,T\}\in E(G_n)}|f(S)-f(T)|.
\]
For a triple \(S\), set \(a=|S\cap A|\), \(b=|S\cap B|\), \(c=3-a-b\), and write \(f_{a,b}\) for its potential. Permutation symmetry and interchange of \(A,B\) imply \(f_{b,a}=-f_{a,b}\) and \(f_{a,a}=0\). A triple of type \((a,b,c)\) has exactly
\[
\binom{3-a}{a'}\binom{3-b}{b'}\binom{n-6-c}{3-a'-b'}
\]
neighbors of type \((a',b',3-a'-b')\), where a binomial coefficient with an impossible choice is zero.

**Exact orbit solution.** For \(n\ge8\), denote the four positive-side orbit variables (not all are positive numbers) by
\[
(u_{30},u_{21},u_{20},u_{10})=(f_{3,0},f_{2,1},f_{2,0},f_{1,0}).
\]
Writing \(d=\binom{n-3}{3}\), the orbit Laplacian equations are exactly
\[
\begin{pmatrix}
 d+1&0&3(n-6)&\frac32(n-6)(n-7)\\
 0&d+1&n-6&\frac12(n-6)(n-7)\\
 1&3&d+3(n-7)&(n-7)(n-8)\\
 1&3&2(n-8)&d+\frac12(n-8)(n-9)
\end{pmatrix}
\begin{pmatrix}u_{30}\\u_{21}\\u_{20}\\u_{10}\end{pmatrix}
=\begin{pmatrix}1\\0\\0\\0\end{pmatrix}.
\]
Set \(h=n(n-5)(n-4)(n-2)(n-1)\) and \(w=n^2-10n+27\). Direct rational substitution gives its solution
\[
 u_{30}=\frac{6(n^2+2)}h,\quad
 u_{21}=\frac{108}{hw},\quad
 u_{20}=-\frac{36(n^2-10n+36)}{h(n-6)w},\quad
 u_{10}=-\frac{36(n^2-7n+18)}{h(n-6)w}.
\]
The graph at \(n=7\) lacks the type \((1,0)\). Its three-variable orbit matrix is
\[
\begin{pmatrix}5&0&3\\0&5&1\\1&3&4\end{pmatrix},
\]
whose solution is \((u_{30},u_{21},u_{20})=(17/70,1/70,-1/14)\). The first three displayed rational formulas agree with these values at \(n=7\).

**Absolute-current signs.** For \(n\ge8\), the strict ordering is
\[
 u_{30}>-u_{10}>-u_{20}>u_{21}>0.
\]
Indeed \(w=(n-8)^2+6(n-8)+11>0\), while
\[
 -u_{20}-u_{21}=\frac{36(n^2-13n+54)}{h(n-6)w}>0,
\quad u_{20}-u_{10}=\frac{108}{hw}>0.
\]
Finally the numerator of \(u_{30}+u_{10}\), apart from its positive denominator and factor \(6\), is
\[
 K(n)=n^5-16n^4+89n^3-200n^2+216n-432.
\]
With \(t=n-8\), it equals
\[
 K(t+8)=t^5+24t^4+217t^3+912t^2+1816t+1296>0.
\]
Thus the positive-potential orbit types, in descending potential order, are \((3,0),(0,1),(0,2),(2,1)\). For \(j=1,2,3,4\), let \(S_j\) respectively be the sets of vertices in the first four, first three, first two, and first one of these orbits, and let \(C_j=|E(S_j,V\setminus S_j)|\). Computing edge incidences using the displayed neighbor counts yields
\[
\begin{aligned}
12C_1&=3n^5-87n^4+1151n^3-8577n^2+34582n-57792,\\
12C_2&=3n^5-87n^4+1133n^3-8145n^2+31144n-48936,\\
12C_3&=3n^5-93n^4+1277n^3-9615n^2+38524n-63624,\\
 C_4&=\frac{(n-5)(n-4)(n-3)}6=d.
\end{aligned}
\]
The discrete coarea identity, paired with the interchange symmetry \(A\leftrightarrow B\), now gives
\[
\mathcal T(f)=2\left[u_{21}C_1+(-u_{20}-u_{21})C_2
 +(u_{20}-u_{10})C_3+(u_{30}+u_{10})C_4\right].
\]
Substitution and polynomial cancellation yield the stated closed formula for \(\|Q_n\|\) for \(n\ge8\). At \(n=7\), the explicit three-orbit solution and direct edge-incidence counts give \(\mathcal T(f)=116/35\), which also equals the same rational expression evaluated at \(7\).

**Complementary projection.** The diagonal edge entry of \(Q_n\) is the effective resistance \(R_n=f(A)-f(B)=2u_{30}\). As the graph is edge-transitive, the identity \(\operatorname{tr}Q_n=N-1\), together with \(|E|=Nd/2\), independently gives
\[
 R_n=\frac{2(N-1)}{Nd}.
\]
For every edge \(e\), \(0<R_n<1\), and the absolute column sum of \(I-Q_n\) is that of \(Q_n\) plus \(1-2R_n\). Therefore
\[
\|P_n\|=\|Q_n\|+1-\frac{4(N-1)}{Nd},
\]
which reduces to the displayed expression involving \(H(n)\).

**Sharp optimizing dimensions.** The exact initial values are
\[
(\|Q_7\|,\|Q_8\|,\|Q_9\|)
=\left(\frac{116}{35},\frac{257}{77},\frac{197}{60}\right),
\]
\[
(\|P_7\|,\|P_8\|,\|P_9\|)
=\left(\frac{117}{35},\frac{1215}{308},\frac{143}{35}\right).
\]
To establish global rather than sampled extrema, let \(t=n-9\ge0\) and set
\[
\begin{aligned}
D_Q(n)&=n(n-5)(n-4)(n-3)(n-2)(n-1)(n+1)W(n)(n^2-8n+18),\\
D_P(n)&=n(n-4)(n-3)(n-2)(n-1)(n+1)W(n)(n^2-8n+18).
\end{aligned}
\]
Exact subtraction of the rational formulas yields
\[
\|Q_n\|-\|Q_{n+1}\|=\frac{R_Q(t)}{D_Q(n)},
\qquad
\|P_n\|-\|P_{n+1}\|=\frac{R_P(t)}{D_P(n)},
\]
where
\[
\begin{aligned}
R_Q(t)={}&18t^9+576t^8+9396t^7+110088t^6+961470t^5\\
 &+5787648t^4+22279356t^3+51060888t^2+62130240t+30373056,\\
R_P(t)={}&18t^8+504t^7+7308t^6+77616t^5+589590t^4\\
 &+2793168t^3+7206300t^2+8019000t+1399680.
\end{aligned}
\]
Every coefficient is strictly positive, and both denominators are positive for \(n\ge9\). Thus both sequences strictly decrease from \(n=9\) onward. Comparing the three displayed initial values proves the unique, distinct peaks. Expansion of the two rational functions at infinity gives the stated asymptotics.

## Verification
The accompanying standard-library checker `verify_rank3_kneser.py` uses exact rational arithmetic. It reconstructs all vertices and edges for \(7\le n\le13\), verifies the full source-sink Laplacian equation at every vertex, evaluates the total variation over every edge, and checks both closed formulas. It also checks all orbit equations at \(8\le n\le25\), all four level-set capacities at \(8\le n\le39\), and the precise rational difference identities at \(9\le n\le39\). The latter checks prove polynomial identities, not merely numerical agreement: after clearing the explicitly displayed denominators the numerator degrees are at most \(25\), so agreement at \(31\) distinct integers forces equality. The unrestricted proof is the explicit orbit reduction and polynomial identities above; the finite full-graph tests are supporting cross-checks.

## Relationship to prior work
Dilworth, Kutzarova, and Ostrovskii (2023), *Cycle Spaces: Invariant Projections and Applications to Transportation Cost*, studies invariant projections and derives endpoint values for Hamming cubes; its primary graph-family calculations are Hamming graphs and discrete tori. Their statements do not give the absolute electrical-current sums on \(KG(n,3)\). Ducey, Hill, and Sin (2017), *The Critical Group of the Kneser Graph on 2-Subsets of an \(n\)-Element Set*, studies integral Laplacian invariants of the rank-two disjointness graph; rank three is not strongly regular and its edge-current orbit problem has additional potential levels. Related known formulas for the Johnson graph concern adjacency by exchanging one element, not adjacency by disjointness. These distinctions are mathematical nonimplications, not a claim that unpublished or unindexed equivalent calculations are impossible.

## Limitations
The result concerns the canonical real Euclidean-orthogonal projections on finite unweighted rank-three Kneser graphs. It does not prove minimal projection norms among all nonorthogonal projections, intermediate \(\ell_p\) norms, weighted disjointness graphs, or arbitrary subset rank. Search coverage cannot establish absolute novelty; an unindexed electrical-network equivalent is a residual bibliographic risk. Finite rational checks alone would not establish the infinite-parameter theorem.

## References
1. Stephen J. Dilworth, Denka Kutzarova, Mikhail I. Ostrovskii, *Cycle Spaces: Invariant Projections and Applications to Transportation Cost*, arXiv:2305.12582v1, first publicly posted 2023-05-21, https://arxiv.org/abs/2305.12582.
2. Joshua E. Ducey, Ian Hill, Peter Sin, *The Critical Group of the Kneser Graph on 2-Subsets of an \(n\)-Element Set*, arXiv:1707.09115v1, first publicly posted 2017-07-28, https://arxiv.org/abs/1707.09115.
