# Weakly almost-square geometry of countable two-terminal metric networks

## Finding
Let \(\ell_n\in(0,\infty)\) be a countably infinite sequence, with \(L:=\inf_{n\ge1}\ell_n>0\). Form a two-terminal length network \(M\) by taking the disjoint closed intervals \(I_n=[0,\ell_n]\) and identifying all zero endpoints to \(a\) and all other endpoints to \(b\). Give the quotient the intrinsic shortest-path metric (infimum of path lengths), and use \(a\) as base point. The following equivalence holds for the real Lipschitz-free space:

\[
\mathcal F(M)\text{ is weakly almost square} \quad\Longleftrightarrow\quad
\exists n\ge1:\;\ell_n=L.
\]

When the infimum is not attained, even the unit molecule \(x=(\delta_b-\delta_a)/L\) fails the pointwise weakly almost-square test. When the infimum is attained, every unit vector, including infinitely supported vectors, admits the required weakly null perturbations. Every such \(M\) is a complete length space; the two-terminal graph is geodesic exactly when its shortest arc exists.

## Assumptions and scope
All spaces and Lipschitz functions are **real**. Every arc is an actual closed length interval, with distinct interiors. The family is countably infinite, with no upper bound on the arc lengths, and \(0<L<\infty\). The metric is the infimum of lengths of finite paths; its endpoints satisfy \(d(a,b)=L\), even if no path realizes this infimum. Weak almost squareness (WASQ) means that for every \(z\in S_X\) there are \(u_k\in B_X\) with \(u_k\rightharpoonup0\), \(\|u_k\|\to1\), and \(\|z\pm u_k\|\to1\). The result is not a characterization of WASQ for arbitrary length spaces.

## Proof
**1. Exact quotient model.** Set
\[
E=\Big(\bigoplus_{n\ge1}L^1(0,\ell_n)\Big)_{\ell_1}.
\]
A function \(f\in\operatorname{Lip}_0(M)\) is equivalent to its family of almost-everywhere derivatives \(g_n=f'|_{I_n}\), subject to \(\sup_n\|g_n\|_\infty<\infty\) and the common-integral condition
\[
\int_0^{\ell_n}g_n(s)\,ds=c\qquad(\text{the same }c=f(b)\text{ for all }n).
\]
The Lipschitz norm is \(\sup_n\|g_n\|_\infty\): edgewise Lipschitz continuity with matching endpoint values is equivalent to global Lipschitz continuity under the path metric. Consequently, pairing \(h=(h_n)\in E\) with these derivatives defines a contractive, surjective map \(Q:E\to\mathcal F(M)\). Its kernel is exactly
\[
K=\{(c_n\mathbf1_{I_n})_n\in E:\;\sum_n c_n=0\}.
\]
Indeed, testing against zero-integral derivatives one arc at a time forces each kernel component to be constant; testing common endpoint differences then forces the sum to vanish. Conversely, any such constant family annihilates all admissible derivatives. Hahn--Banach duality gives the **isometric** identification \(E/K\cong\mathcal F(M)\). The image includes every \(\delta_p\) because the indicator of the initial subinterval from \(a\) to \(p\) is a lift; thus no additional predual elements are missing.

Write \(\bar h_n=\ell_n^{-1}\int h_n\), \(P_nh=h_n-\bar h_n\mathbf1_{I_n}\), and
\[
Y=\Big(\bigoplus_n L^1_0(0,\ell_n)\Big)_{\ell_1},\qquad
L^1_0(0,\ell_n)=\{v:\int v=0\}.
\]
The maps \(P(Qh)=(P_nh)_n\) and \(\theta(Qh)=\sum_n\bar h_n\) are well-defined bounded operators, since \(P\) annihilates \(K\), \(\|P_nh\|_1\le2\|h_n\|_1\), and \(\sum|\bar h_n|\le L^{-1}\|h\|_E\). With \(m=\delta_b-\delta_a=Q(\mathbf1_{I_1})\), every \(u\in\mathcal F(M)\) has the unique bounded direct-sum representation
\[
u=\theta(u)m+Q(Pu),\qquad Pu\in Y.
\]
This is a topological, not necessarily isometric, direct sum.

**2. A minimal-length arc gives norm-attaining lifts.** Suppose \(\ell_j=L\) for some \(j\). For arbitrary \(h\in E\), minimize \(\|h+c\|_E\) over the closed subspace of constant families \(c=(c_n\mathbf1_{I_n})\in K\). A minimizing sequence \(c^{(k)}\in K\) is bounded in \(E\). By diagonal extraction the coefficients converge coordinatewise to a constant family \(c\in E\). Put \(r=-\sum_n c_n\); mass may have escaped to high coordinates, so \(r\) need not vanish. The elementary \(\ell_1\)-sum splitting fact gives
\[
\liminf_k\|h+c^{(k)}\|_E
\ge \|h+c\|_E+\liminf_k\|c^{(k)}-c\|_E
\ge\|h+c\|_E+L|r|.
\]
For completeness, the first inequality follows by splitting into the first \(N\) arc coordinates (where the difference tends to zero) and a tail, then taking \(N\to\infty\); the second follows from \(\ell_n\ge L\) and \(\sum_nc_n^{(k)}=0\). Correct the lost total coefficient on a minimum-length arc: \(c'=c+r\mathbf1_{I_j}\in K\). The triangle inequality gives \(\|h+c'\|_E\le\|h+c\|_E+L|r|\). Thus \(c'\) is a minimizer. Hence every \(z\in\mathcal F(M)\) has a lift \(h\in E\) satisfying \(Qh=z\) and \(\|h\|_E=\|z\|\).

Take a unit vector \(z\) and such a norm-one lift \(h\). On each \(I_n\), let \(r_{k,n}\) be the sign alternating on successive dyadic half-open cells of relative length \(2^{-k}\). Let \(u_k=Q((r_{k,n}h_n)_n)\). For each fixed integrable \(v\) on an arc, \(\int r_{k,n}v\to0\). Dominated summation over the countable arcs therefore proves \((r_{k,n}h_n)_n\rightharpoonup0\) in \(E\), hence \(u_k\rightharpoonup0\) in the quotient. Moreover
\[
\|z\pm u_k\|
\le\sum_n\int (1\pm r_{k,n})|h_n|
=1\pm\sum_n\int r_{k,n}|h_n|\longrightarrow1.
\]
For the lower bound on the perturbation norm, let
\[
a_{k,n}=\ell_n^{-1}\int r_{k,n}\operatorname{sgn}(h_n),\qquad
\psi_{k,n}=\frac{r_{k,n}\operatorname{sgn}(h_n)-a_{k,n}}{1+|a_{k,n}|}.
\]
Every \(\psi_{k,n}\) has integral zero and essential sup norm at most one; hence the family is an admissible dual Lipschitz derivative family of norm at most one. For each fixed \(n\), its pairing with \(r_{k,n}h_n\) tends to \(\|h_n\|_1\). Dominated summation yields \(\liminf_k\|u_k\|\ge\sum_n\|h_n\|_1=1\), while the quotient contraction gives \(\|u_k\|\le1\). Hence \(\|u_k\|\to1\); the two signed norms also tend to one by the triangle inequality \(2=2\|z\|\le\|z+u_k\|+\|z-u_k\|\). This proves WASQ for **all** unit vectors.

**3. Without a minimum arc, the endpoint molecule obstructs WASQ.** Suppose every \(\ell_n>L\), and set \(x=m/L\in S_{\mathcal F(M)}\). Let \(f_0\in S_{\operatorname{Lip}_0(M)}\) have constant derivative \(L/\ell_n\) on each arc. Thus \(f_0(x)=1\). For fixed \(N\), put
\[
\sigma_N=1-\max_{1\le n\le N}L/\ell_n>0.
\]
For any family \(H=(H_n)\) supported in the first \(N\) arcs, with \(\int H_n=0\) and \(\|H_n\|_\infty\le\sigma_N\), the derivative families of \(f_0\pm H\) are admissible with norm at most one and \(H(x)=0\). Suppose \(u_k\in B_{\mathcal F(M)}\) is weakly null and \(\|x\pm u_k\|\le1+\varepsilon_k\), where \(\varepsilon_k\downarrow0\). Each norm-one functional of the form \(f_0+H\), evaluated on both signs, gives \(|(f_0+H)(u_k)|\le\varepsilon_k\); the case \(H=0\) gives \(|f_0(u_k)|\le\varepsilon_k\). Hence
\[
|H(u_k)|\le2\varepsilon_k.
\]
For \(v_n=(Pu_k)_n\in L^1_0(I_n)\), the mean-zero test function \(\tfrac12(\operatorname{sgn}v_n-\overline{\operatorname{sgn}v_n})\) has sup norm at most one and pairing \(\tfrac12\|v_n\|_1\). Optimizing these tests independently on the first \(N\) arcs gives
\[
\sum_{n\le N}\|(Pu_k)_n\|_1\le\frac{4\varepsilon_k}{\sigma_N}\longrightarrow0
\qquad(\text{each fixed }N).
\]

We use the following standard **uniform-tail lemma**: if \(w_k\rightharpoonup0\) in an \(\ell_1\)-sum \(\bigoplus_1 Z_n\), then \(\lim_{N\to\infty}\sup_k\sum_{n>N}\|(w_k)_n\|=0\). To prove it, otherwise choose a subsequence and successively disjoint finite coordinate blocks carrying uniformly positive mass. Choose norming functionals on each block. By weak nullness, choose subsequent indices so the already selected block functionals are negligible; choose block endpoints so future tails of each selected vector are negligible. Gluing the norming functionals produces one bounded functional taking uniformly positive values along the subsequence, a contradiction.

Since \(P\) is bounded, \(Pu_k\rightharpoonup0\) in \(Y\). The uniform-tail lemma and the displayed finite-coordinate estimate yield \(\|Pu_k\|_Y\to0\). Likewise \(\theta(u_k)\to0\) by weak nullness. The direct-sum representation therefore forces
\[
\|u_k\|\le L|\theta(u_k)|+\|Pu_k\|_Y\longrightarrow0.
\]
No weakly null sequence can both be almost square at \(x\) and have norm tending to one. Thus \(\mathcal F(M)\) is not WASQ.

**4. Metric boundaries.** Completeness follows because points in distinct arc interiors at distance at least \(\varepsilon\) from both terminals are at mutual distance at least \(2\varepsilon\): a Cauchy sequence either approaches a terminal or eventually lies on one compact arc. The path metric is a length metric. Any shortest route between points on two arcs is a combination of subarcs and, if necessary, a minimum-length connecting arc; hence \(M\) is geodesic if a minimum-length arc exists. Without one, \(d(a,b)=L\) is not realized by any path, so it is not geodesic.

## Verification
The proof is analytic and uses no finite enumeration as a substitute for an infinite argument. The critical checks are (i) the common-integral derivative description and exact annihilator \(K\), (ii) the lost-mass correction at an arc of length \(L\) when finding norm-minimizing lifts, (iii) dual mean-zero norming families proving perturbation norms approach one, and (iv) the disjoint-block proof of uniform tails in an \(\ell_1\)-sum. A concrete nonattaining example is \(\ell_n=1+1/n\) for \(n\ge1\); its free space is LASQ by the cited length-space theorem, but fails WASQ by part 3. With any arc of length one added, the corresponding space is WASQ by part 2.

## Relationship to prior work
Kaasik and Veeorg, *Weakly almost square Lipschitz-free spaces*, arXiv:2210.09158, first public version 17 October 2022, construct another complete length-space example that is LASQ but not WASQ (their Section 2 uses horizontal levels and two vertical boundary lines). Their corrected version 2, Proposition 3.2, proves weakly almost-square perturbations for finitely supported unit elements of a geodesic free space, but explicitly leaves a general metric characterization open; it does **not** establish WASQ for arbitrary infinitely supported elements. The present countable parallel-arc criterion is for a different metric family and proves the all-vector positive direction by a separate norm-minimizing-lift argument.

Haller, Kaasik and Ostrak, arXiv:2205.02685, prove LASQ for length spaces (and the equivalence for complete spaces), but not WASQ. Abrahamsen et al., *Delta-points and their implications for the geometry of Banach spaces* (2024), characterize certain \(\Delta\)-molecules, a different pointwise property. These results neither state nor immediately imply the two-way WASQ criterion here.

## Limitations
This is a special-family theorem for two-terminal networks made of disjoint closed intervals; no arbitrary graph, uncountable family, zero infimum, complex scalar, or general nongeodesic length-space assertion is made. The proof is internal rather than independently certified. Potential earlier work on proximinal subspaces of \(\ell_1\)-sums or on countable metric theta graphs remains a bibliographic originality risk.

## References
1. J. K. Kaasik and T. Veeorg, *Weakly almost square Lipschitz-free spaces*, arXiv:2210.09158 (first posted 2022-10-17; version 2 dated 2023-04-21), especially Sections 2--3 and Proposition 3.2. https://arxiv.org/abs/2210.09158
2. R. Haller, J. K. Kaasik and A. Ostrak, *The Lipschitz-free space over length space is locally almost square but never almost square*, arXiv:2205.02685 (first posted 2022-05-05), Theorem 3.1. https://arxiv.org/abs/2205.02685
3. T. A. Abrahamsen, R. J. Aliaga, V. Lima et al., *Delta-points and their implications for the geometry of Banach spaces*, Journal of the London Mathematical Society (2024), DOI:10.1112/jlms.12913, Section 6.
