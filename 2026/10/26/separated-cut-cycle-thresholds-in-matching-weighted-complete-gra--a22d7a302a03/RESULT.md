# Separated cut–cycle thresholds in matching-weighted complete graphs

## Finding
Let \(N=2m\ge8\) be even. Give each edge of a fixed perfect matching in the complete graph \(K_N\) conductance \(x^2\), with \(x>0\), and give every other edge conductance \(1\). On the real Euclidean edge-coordinate space let \(Q\) be the canonical orthogonal weighted cut projection and \(P=I-Q\) the cycle projection, with the square roots of conductances built into the edge incidence matrix. Set \(b=N-2+2x^2\). For an edge belonging to the matching, the absolute column sums of \(Q\) and \(P\), respectively, are
\[
q_M=\frac{2x^2+2(N-2)x}{b},\qquad
p_M=1+\frac{-2x^2+2(N-2)x}{b}.
\]
For an edge outside the matching, the absolute column sums are
\[
(q_C,p_C)=\begin{cases}
\left(\dfrac2N+\dfrac{2N-6+2x}{b},\;1+\dfrac{2N-8+2x}{b}\right),&0<x\le1,\\[4pt]
\left(2-\dfrac4N+\dfrac{2x}{b},\;3-\dfrac6N+\dfrac{2(x-1)}{b}\right),&x\ge1.
\end{cases}
\]
The two displayed branches agree when \(x=1\). Thus \(\|Q\|_{1\to1}=\|Q\|_{\infty\to\infty}=\max(q_M,q_C)\) and \(\|P\|_{1\to1}=\|P\|_{\infty\to\infty}=\max(p_M,p_C)\).

Define two positive thresholds
\[
\xi_P=\frac{N^2-6N+6}{3(N-2)},\qquad
\xi_Q=\frac{(N-2)^2}{N-4}.
\]
For every even \(N\ge8\), \(1<\xi_P<\xi_Q\), and the maximizing edge types have the complete phase diagram:

* \(0<x<1\): both projections maximize on nonmatching edges;
* \(x=1\): every edge column ties;
* \(1<x<\xi_P\): both projections maximize on matching edges;
* \(x=\xi_P\): the cycle columns all tie, while the cut maximum is on matching edges;
* \(\xi_P<x<\xi_Q\): cut maximizers are matching edges, but cycle maximizers are nonmatching edges;
* \(x=\xi_Q\): cut columns all tie, while the cycle maximum is on nonmatching edges;
* \(x>\xi_Q\): both projections maximize on nonmatching edges.

The thresholds have exact separation
\[
\xi_Q-\xi_P=\frac{2N(N-3)(N-1)}{3(N-4)(N-2)}>0,
\qquad\lim_{N\to\infty}\frac{\xi_Q}{\xi_P}=3.
\]
In particular, the complementary projections have different maximizing edge classes throughout a nonempty interval for every eligible dimension.

Put \(R_N=(1+\sqrt{2N-3})/2\). Across the entire conductance range \(x>0\), for every even \(N\ge8\),
\[
\sup_{x>0}\|Q\|=R_N,
\]
and this maximum is uniquely attained at \(x=R_N\). For every even \(N\ge10\),
\[
\sup_{x>0}\|P\|=R_N,
\]
uniquely attained at \(x=R_N-1\). The two globally optimized projection norms therefore have the same value but different optimizing conductances, and \(R_N\sim\sqrt{N/2}\). In the exceptional dimension \(N=8\), the global cycle norm maximum is instead \(29/12\), uniquely attained at \(x=3\) on nonmatching edges.

## Assumptions and scope
A perfect matching partitions the \(N\) vertices into \(N/2\) disjoint pairs. The graph contains **all** \(\binom N2\) edges; only their conductances differ. Fix arbitrary edge orientations, let \(D\) be the ordinary signed vertex–edge incidence matrix and \(W\) the diagonal conductance matrix. Define \(B=DW^{1/2}\), \(L=BB^{\mathsf T}\), and \(Q=B^{\mathsf T}L^+B\) on the real edge-coordinate space. The superscript \(+\) denotes the Moore–Penrose pseudoinverse. Consequently \(Q\) and \(P=I-Q\) are symmetric orthogonal projections. Their endpoint operator norms are maxima of absolute column sums (or, equally, row sums). No claim concerns arbitrary nonorthogonal projections.

## Proof
**1. Orthogonal spectral splitting.** Let \(R\) be the involutive permutation interchanging the two vertices in every matching pair, and let \(J\) be the all-ones matrix. The weighted Laplacian is exactly
\[
L=NI-J+(x^2-1)(I-R).
\]
The zero-sum vertex space is an orthogonal direct sum of (i) vectors constant on every pair, with eigenvalue \(N\), and (ii) vectors antisymmetric within every pair, with eigenvalue \(b=N-2+2x^2>0\). This is an exact statement for all positive \(x\).

**2. Matching-edge columns.** Take a matching edge joining \(u\) and \(u'\). The voltage induced by its square-root-conductance source is
\[
 h=\frac{x}{b}(\mathbf e_u-\mathbf e_{u'}).
\]
The source-edge current has absolute value \(2x^2/b\), and each of the \(2(N-2)\) cross edges incident to \(u\) or \(u'\) has absolute current \(x/b\); all other currents vanish. Thus \(q_M\) follows. The diagonal projection entry equals \(2x^2/b\le1\), so \(p_M=1+q_M-4x^2/b\), proving the stated formula.

**3. Nonmatching-edge columns.** For endpoints \(u,v\) in distinct matching pairs, label their partners \(u',v'\). Splitting the unit source into pair-symmetric and pair-antisymmetric pieces gives voltages
\[
 h_u=p=\frac1{2N}+\frac1{2b},\quad h_{u'}=q=\frac1{2N}-\frac1{2b},\quad
 h_v=-p,\quad h_{v'}=-q,
\]
and zero voltage on all other vertices. The two matching edges incident to these pairs contribute \(2x/b\) to the absolute column sum. The four cross edges among \(u,u',v,v'\) contribute \(2p+2|q|+2(p+q)\). Cross edges joining one of these four vertices to any of the other \(N-4\) vertices contribute \(2(N-4)(p+|q|)\). Since \(q\) changes sign precisely at \(x=1\), these counts give exactly the two formulas for \(q_C\). Its diagonal is \(2p=1/N+1/b<1\), hence \(p_C=1+q_C-2(1/N+1/b)\). No other edge classes exist.

**4. Sharp thresholds.** Direct subtraction, with positive denominator \(Nb\), gives, for \(x\ge1\),
\[
q_M-q_C=\frac{2(x-1)\big((N-2)^2-(N-4)x\big)}{Nb},
\qquad
p_M-p_C=\frac{2(x-1)\big(N^2-6N+6-3(N-2)x\big)}{Nb}.
\]
For \(0<x\le1\), the corresponding factorizations are
\[
q_M-q_C=\frac{2(x-1)\big(N^2-2N-2+(N-2)x\big)}{Nb},
\quad p_M-p_C=\frac{-2(x-1)(x-(N-4))}{b}.
\]
Both are strictly negative for \(0<x<1\) and \(N\ge8\). The displayed factorizations prove every asserted maximizing-edge regime, including all boundary ties. The threshold inequality and difference follow by elementary rational simplification; \(\xi_P>1\) follows from \(N^2-9N+12>0\) for even \(N\ge8\).

**5. Global amplification.** Differentiating \(q_M\) yields a unique maximum at \(x=R_N\), where \(q_M=R_N\). Differentiating \(p_M\) yields a unique maximum at \(x=R_N-1\), where \(p_M=R_N\). For \(x\le1\), \(q_C\le2+2/N\le9/4<R_8\le R_N\); for \(x\ge1\),
\[
q_C\le2+\frac1{\sqrt{2(N-2)}}\le2+\frac1{\sqrt{12}}<R_8.
\]
Thus the global cut maximum is attained uniquely as claimed.

The global nonmatching-cycle maximum for \(0<x\le1\) is, writing \(s=N-2\),
\[
1+\frac{s-2+\sqrt{(s-2)^2+s/2}}s<3,
\]
attained at \(x=-(s-2)+\sqrt{(s-2)^2+s/2}\), which lies in \((0,1)\). For \(x\ge1\), it is
\[
3-\frac6N+\frac1{2(1+\sqrt{N/2})},
\]
attained at \(x=1+\sqrt{N/2}\). In dimension \(N=8\), these two bounds and \(\sup p_M=R_8\) are respectively smaller than, equal to, and smaller than \(29/12\), proving the exception. For \(N=10\), both nonmatching-cycle maxima are below \(64/25<R_{10}\); for \(N=12\), both are below \(27/10<R_{12}\). When \(14\le N\le18\), both are below \(3\le R_N\). For all even \(N\ge20\), both are below \(7/2<R_N\). Hence \(\sup_{x>0}\|P\|=R_N\) for every even \(N\ge10\), and its unique optimizer is the matching-column optimizer \(x=R_N-1\).

## Verification
The accompanying Python standard-library program `check.py` constructs the actual weighted grounded Laplacian and inverts it with exact rational arithmetic; it then compares **every** cut and cycle column with the analytical formulas at 32 configurations (four graph orders and eight rational square roots of matching conductance per order). The independent reconstruction checked 1,840 columns. It also tests both exact equality thresholds and the strict maximizing-edge regimes. Successful executable output:

`MATCHING_WEIGHTED_COMPLETE_EXACT_OK graphs=32 full_columns=1840 boundary_graphs=12`

These finite tests are corroboration. Steps 1–5 above prove the theorem for all eligible dimensions and all real positive conductances.

## Relationship to prior work
Dilworth, Kutzarova and Ostrovskii's study of invariant cycle-space projections includes exact unweighted hypercube projection calculations and general representation-theoretic methods, but does not state or imply this matching-weighted complete-graph phase diagram. The modern weighted electrical-flow localization literature employs the same symmetrized transfer-current matrix, but proves general spectral norm bounds rather than exact \(\ell_1\) operator-column formulas or weight-maximizer transitions. Weighted effective-resistance optimization concerns aggregate vertex-pair resistance, a different functional. The claims here concern canonical projections only, not minimum norms over all projections.

## Limitations
The result is restricted to positive conductances that agree on one perfect matching and agree separately off the matching, and to real Euclidean-orthogonal cut/cycle projections on square-root-conductance edge coordinates. Nothing is established for heterogeneous weights on individual matching edges, arbitrary edge-weight patterns, or induced intermediate \(\ell_p\) norms. This is not an independent novelty certification. Equivalent explicit calculations in less-indexed electrical-network literature remain a possibility.

## References
1. S. J. Dilworth, D. Kutzarova, and M. I. Ostrovskii, *Cycle spaces: invariant projections and applications to transportation cost*, arXiv:2305.12582, first posted 21 May 2023; Sections 1 and 2.1–2.7.
2. O. Gurel-Gurevich, A. Nachmias, and S. Sachdeva, *A Tight Bound on Localization of Electrical Flows*, arXiv:2605.24130, first posted 22 May 2026; Theorem 1.3 and Section 1.1.
3. A. Ghosh, S. Boyd, and A. Saberi, *Minimizing Effective Resistance of a Graph*, SIAM Review 50 (2008), 37–66, DOI:10.1137/050645452; distinguished aggregate-resistance objective.
