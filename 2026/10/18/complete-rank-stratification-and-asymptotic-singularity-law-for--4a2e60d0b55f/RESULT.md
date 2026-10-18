# Complete rank stratification and asymptotic singularity law for dyadic three-by-three Fourier minors

## Finding

Let \(m\ge2\) be an integer, \(N=2^m\), \(\omega=e^{2\pi i/N}\), and \(F_N=(\omega^{rc})_{r,c\in\mathbb Z_N}\). For any three-element set \(T\subset\mathbb Z_N\), the valuations of its three differences, sorted increasingly, are uniquely \((u,u,v)\) with \(0\le u<v\le m-1\). Call \((u,v)\) its dyadic type. For row and column triples of types \((u,v)\) and \((s,t)\), respectively, the corresponding Fourier minor has rank

\[
\operatorname{rank}F_N[R,C]=\begin{cases}
1,&u+s\ge m,\\
2,&u+s<m\text{ and }(v+s\ge m\text{ or }u+t\ge m),\\
3,&v+s<m\text{ and }u+t<m.
\end{cases}
\]

All three ranks are realized for sufficiently large \(m\). The number of unordered three-point sets of type \((u,v)\) is exactly \(B_m(u,v)=N^3/2^{u+v+3}\). Consequently the complete rank census is the following explicit finite arithmetic formula, involving no matrix ranks or roots of unity:

\[
\mathcal N_j(m)=\sum_{0\le u<v<m}\sum_{0\le s<t<m}
\frac{N^6}{2^{u+v+s+t+6}}\,\mathbf1\{r_m(u,v;s,t)=j\},\qquad j=1,2,3,
\]

where \(r_m\) is the displayed rank rule. In particular \(\sum_j\mathcal N_j(m)=\binom N3^2\). If \(\mathcal S_m=\mathcal N_1(m)+\mathcal N_2(m)\) counts singular minors, then

\[
\lim_{m\to\infty}\frac{\mathcal S_m}{N^5}=\frac1{12},\qquad
\lim_{m\to\infty}\frac{N\mathcal S_m}{\binom N3^2}=3,\qquad
\mathcal N_1(m)=o(N^5).
\]

Thus a uniformly random pair of three-element row and column sets has singular Fourier minor with probability asymptotic to \(3/N\); almost all of those singular minors have rank two.

## Assumptions and scope

All ranks and determinants are over \(\mathbb C\); row and column index sets are independently selected without replacement and their ordering does not affect rank. The valuation \(\nu_2(d)\) for \(d\in\mathbb Z_N\setminus\{0\}\) is the unique integer \(e\in\{0,\ldots,m-1\}\) such that \(2^e\mid d\) but \(2^{e+1}\nmid d\), interpreted on any integer representative. The theorem concerns cyclic groups of order a power of two, not general finite abelian groups or higher-order minors. It gives exact counts for every integer \(m\ge2\) and asymptotics along dyadic orders.

## Proof

**1. Dyadic triple geometry.** Of the three nonzero differences of any three distinct residues, exactly one has a strictly larger two-adic valuation than the other two. Indeed, if two differences have the same least valuation, their difference is divisible by one further power of two; a difference with larger valuation plus one with smaller valuation has the smaller valuation. Label the unique close pair \(x_1,x_2\), with \(\nu_2(x_1-x_2)=v\), and the outsider \(x_0\), with \(\nu_2(x_1-x_0)=\nu_2(x_2-x_0)=u\).

**2. Normalized minor.** Translate both triples and multiply rows and columns by nonzero phases, so the minor becomes

\[
M=\begin{pmatrix}1&1&1\\1&\omega^{ac}&\omega^{ad}\\1&\omega^{bc}&\omega^{bd}\end{pmatrix},
\]

where \(\nu_2(a)=\nu_2(b)=u\), \(\nu_2(a-b)=v\), \(\nu_2(c)=\nu_2(d)=s\), and \(\nu_2(c-d)=t\). If \(u+s\ge m\), all four nontrivial phases are one and \(M\) has rank one. If \(u+s<m\), the minor formed by its first two rows and first two columns equals \(\omega^{ac}-1\ne0\), so its rank is at least two.

**3. Exact determinant obstruction.** In the latter case each of \(\omega^{ac}-1\), \(\omega^{ad}-1\), \(\omega^{bc}-1\), and \(\omega^{bd}-1\) is nonzero. If the determinant vanishes, the equality

\[
(\omega^{ac}-1)(\omega^{bd}-1)=(\omega^{ad}-1)(\omega^{bc}-1)
\]

implies equality of product arguments modulo \(\pi\). Since \(e^{i\theta}-1=2i e^{i\theta/2}\sin(\theta/2)\), this forces \(N\mid(a-b)(c-d)\). Under this congruence we have \(\omega^{a(c-d)}=\omega^{b(c-d)}\), and expansion of the determinant gives the exact factorization

\[
\det M=(1-\omega^{a(c-d)})(\omega^{ad}-\omega^{bd}).
\]

Therefore \(\det M=0\) if and only if \(N\mid a(c-d)\) or \(N\mid(a-b)d\), i.e. \(u+t\ge m\) or \(v+s\ge m\). Conversely, either of these congruences implies \(N\mid(a-b)(c-d)\), so the factorization applies and the determinant vanishes. This proves all three mutually exclusive rank cases, including the boundary equalities.

**4. Multiplicities.** Fix \(0\le u<v<m\). There are \(N\cdot (N/2^{v+1})/2=N^2/2^{v+2}\) unordered pairs \(\{x_1,x_2\}\) of valuation \(v\). For each such pair, exactly \(N/2^{u+1}\) choices of outsider have valuation \(u\) relative to either pair point. The close pair is unique, so no configuration is counted twice. Thus \(B_m(u,v)=N^3/2^{u+v+3}\). Multiplying the row and column multiplicities proves the rank census. The identity \(\sum_{0\le u<v<m}B_m(u,v)=\binom N3\) follows equally from the partition of all triples into types.

**5. Singularity asymptotic.** Put \(w(u,v;s,t)=2^{-(u+v+s+t)}\) and define the finite sums

\[
X_m=\sum_{u<v,\ s<t}w(u,v;s,t)\mathbf1\{v+s\ge m\},\qquad
I_m=\sum_{u<v,\ s<t}w(u,v;s,t)\mathbf1\{v+s\ge m,\ u+t\ge m\}.
\]

Symmetry between row and column types gives \(\mathcal S_m=N^6(2X_m-I_m)/64\). For the first sum, parameterize \(v=m-h\) with \(1\le h\le m-1\) and use geometric summation:

\[
NX_m=\sum_{h=1}^{m-1}2^h
\Big(\sum_{u=0}^{m-h-1}2^{-u}\Big)
\Big(\sum_{s=h}^{m-2}2^{-s}\sum_{t=s+1}^{m-1}2^{-t}\Big).
\]

For each fixed \(h\), its summand tends to \((8/3)2^{-h}\) as \(m\to\infty\); it is bounded by the same summable quantity, since the first sum is at most \(2\) and the final double sum is at most \((4/3)4^{-h}\). By dominated summation \(NX_m\to\sum_{h\ge1}(8/3)2^{-h}=8/3\). For the intersection, each fixed pair \((u,s)\) contributes at most \(O(N^{-2})\), because \(v\ge m-s\) and \(t\ge m-u\) force both geometric tails to start that far out; there are at most \(m^2\) possible \((u,s)\). Thus \(I_m=O(m^2/N^2)=o(1/N)\). The same tail bound gives the rank-one weight \(O(m^2/N^2)\). It follows that \(\mathcal S_m/N^5\to (1/64)(16/3)=1/12\) and \(\mathcal N_1=o(N^5)\). Finally, \(\binom N3^2\sim N^6/36\), giving the limiting probability constant \(3\).

## Verification

The accompanying standard-library Python script `verify_dyadic_minors.py` performs exact cyclotomic arithmetic in \(\mathbb Z[X]/(X^{N/2}+1)\), determines matrix rank using independent determinant and two-by-two minor calculations, and compares against the dyadic rank rule. It exhaustively checks every pair of three-element index sets for \(N\in\{4,8,16\}\), plus 18,000 deterministic seeded tests at \(N=32\) and 8,000 at \(N=64\). In all, 342,752 exact rank comparisons passed; counts for \(N=16\) were \((\mathcal N_1,\mathcal N_2,\mathcal N_3)=(256,26624,286720)\). The proof above, not the finite tests, establishes the all-order assertions.

## Relationship to prior work

Gu–Zhou–Wang (2026) resolve principal nonsingularity for Fourier matrices of orders \(70\) and \(143\) using exact finite-field checks. Caragea–Lee (2024) establish a squarefree-order criterion for nonvanishing of three-by-three **principal** Fourier minors. Here both triples vary independently, the modulus ranges over every dyadic order, and the output is a complete three-rank census and asymptotic singularity density. Delvaux–Van Barel (2006/2008) study rank-deficient submatrices for prime-power Fourier matrices; the present census should be read in light of that broader structural literature, with priority of any implicit equivalent rank criteria left open.

## Limitations

The asymptotic concerns a uniformly sampled pair of unordered three-element index sets, not independent entries of an abstract random matrix. The criterion uses divisibility special to dyadic cyclic orders and does not automatically generalize to other prime powers. While the exact census follows from the proof, the extent to which the explicit rank classification could be derived as a special case of earlier general work on rank-deficient Fourier submatrices remains a historical-priority risk; no claim of independent priority certification is made. Only self-review and finite exact verification have been performed, not independent audit.

## References

1. J. Gu, L. Zhou and Y. Wang, *Principal nonsingularity of the Fourier matrices of orders 70 and 143*, arXiv:2608.17746 (first publicly available 2026-08-18), https://arxiv.org/abs/2608.17746.
2. A. Caragea and D. G. Lee, *On the principal minors of Fourier matrices*, arXiv:2409.09793 (2024), https://arxiv.org/abs/2409.09793.
3. S. Delvaux and M. Van Barel, *Rank-deficient submatrices of Fourier matrices*, technical report TW 470 (2006), later published in Linear Algebra and its Applications (2008).
