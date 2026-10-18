# Dense atomic singular laws for normalized ancestor sums on homogeneous trees

## Finding
Fix any integer \(b\ge 2\). On the complete \(b\)-ary rooted tree of height \(h\), the normalized vertex-ancestor summation operator has a completely explicit singular spectrum, and the dimension-normalized empirical singular distributions converge to a dense pure-point probability law. Unlike a typical bounded-spectrum finite-matrix limit, its largest singular value diverges logarithmically with dimension while the limiting measure retains finite moments of every nonnegative order.

For \(L\ge1\) and \(1\le j\le L\), put
\[
\sigma_{L,j}=\frac{1}{2\sin\bigl((2j-1)\pi/(4L+2)\bigr)}.
\]
The operator on the height-\(h\) tree has singular values \(\sigma_{L,j}\) with multiplicity \((b-1)b^{h-L}\) for every \(1\le L\le h\), and also has one copy of each \(\sigma_{h+1,j}\) for \(1\le j\le h+1\). These multiplicities count *occurrences*; if numerical values from different blocks coincide, their multiplicities must be added.

Write \(N_h=(b^{h+1}-1)/(b-1)\), and let \(\nu_{b,h}\) be the empirical distribution of all \(N_h\) singular values, counting multiplicity. Then, as \(h\to\infty\),
\[
\nu_{b,h}\Longrightarrow\nu_b
=(b-1)^2\sum_{L=1}^{\infty} b^{-(L+1)}
\sum_{j=1}^{L}\delta_{\sigma_{L,j}}.
\]
For each fixed real \(p\ge0\), \(\int s^p\,d\nu_{b,h}(s)\to\int s^p\,d\nu_b(s)\), with error at most \(O_{b,p}((h+1)^{p+1}b^{-h})\). The measure is purely atomic, every listed atom has positive mass, and its *topological support* is the whole interval \([1/2,\infty)\). Its upper tail satisfies the sharp exponential large-deviation rate
\[
\lim_{t\to\infty}\frac{1}{t}\log\nu_b((t,\infty))
=-\frac{\pi}{2}\log b.
\]
A distinguished exactly computable mass is
\[
\nu_b(\{1\})=\frac{(b-1)^2}{b^2(1-b^{-3})}.
\]
Finally,
\[
\|\mathcal A_{b,h}\|=
\frac{1}{2\sin(\pi/(4h+6))}
=\frac{2}{\pi\log b}\log N_h+O_b(1),
\]
\[
\|\mathcal A_{b,h}\|_{S_2}^{2}
=\frac{b}{b-1}N_h-\frac{h+1}{b-1},\qquad
\int s^2\,d\nu_b(s)=\frac{b}{b-1}.
\]
Here \(\mathcal A_{b,h}\) denotes the operator defined below. The principal finding is the explicit tree-dependent *full spectral law and its tail*, not a claim that the singular values of a single triangular summation block or its shift decomposition were previously unknown.

## Assumptions and scope
Let \(V_{b,h}\) consist of all finite words over \(\{0,\ldots,b-1\}\) of lengths from \(0\) to \(h\). The empty word is the root; \(|v|\) is depth; \(u\preceq v\) means that \(u\) is a prefix of \(v\). Equip \(\ell^2(V_{b,h})\) with counting measure, with both real and complex scalars permitted, and define
\[
(\mathcal A_{b,h}f)(v)
=\sum_{u\preceq v} b^{-(|v|-|u|)/2}f(u).
\]
The results hold for every \(h\ge0\) and every integer \(b\ge2\). The limit holds with \(b\) fixed, not with \(b\) growing with \(h\). Singular values are the nonnegative square roots of the eigenvalues of \(\mathcal A_{b,h}^{*}\mathcal A_{b,h}\); \(S_p\) for a finite matrix denotes its Schatten power sum. An \(O_{b,p}\) bound may depend on the fixed indicated parameters, but is independent of \(h\).

## Proof
**1. Exact branching chains.** Let \(G_d\) be the coordinate subspace of vertices at depth \(d\). Define \(S e_u=b^{-1/2}\sum_{v:\,\operatorname{parent}(v)=u} e_v\) for nonterminal vertices \(u\), and \(S e_v=0\) for terminal vertices. On \(G_d\) for \(d<h\), \(S\) is an isometry into \(G_{d+1}\), since distinct children sets are disjoint. Thus \(S^{h+1}=0\) and the matrix of \(S^k\) is \(b^{-k/2}\) precisely on ancestor/descendant pairs at distance \(k\). Consequently
\[
\mathcal A_{b,h}=I+S+\cdots+S^h=(I-S)^{-1}.
\]
Put \(W_0=G_0\) and \(W_d=G_d\ominus S G_{d-1}\) for \(1\le d\le h\). Orthogonality and the isometry property imply that each \(W_d\) has an orthonormal basis whose forward shifts generate mutually orthogonal chains \(w,Sw,\ldots,S^{h-d}w\). Indeed, for different starting depths the later-starting seed is orthogonal to the shifted lower-depth chain because the latter lies in \(S G_{d-1}\); equal-depth seeds stay orthogonal under equal powers. Induction over levels shows these chains span all \(G_0\oplus\cdots\oplus G_h\). The dimensions are \(\dim W_0=1\) and \(\dim W_d=b^d-b^{d-1}=(b-1)b^{d-1}\) for \(d\ge1\). Each chain of length \(L=h-d+1\) carries \(\mathcal A_{b,h}\) as the \(L\)-by-\(L\) lower-triangular all-ones matrix \(Q_L\). This proves the asserted block multiplicities.

**2. Singular values of a chain.** The inverse of \(Q_L\) is \(D_L=I-J_L\), where \(J_L\) is the lower nilpotent unit shift. The positive symmetric matrix \(D_L^*D_L\) is tridiagonal with off-diagonals \(-1\), diagonal \(2\) except the final entry \(1\) (for \(L=1\), the only entry is \(1\)). The discrete sine eigenvectors with Dirichlet condition at index \(0\) and free/Neumann condition at index \(L+1\) give eigenvalues
\[
4\sin^2\left(\frac{(2j-1)\pi}{4L+2}\right),\quad1\le j\le L.
\]
Since \((Q_L^*Q_L)^{-1}=D_LD_L^*\), which has the same eigenvalues as \(D_L^*D_L\), taking reciprocal square roots establishes the exact \(\sigma_{L,j}\). The largest block singular value strictly increases with \(L\); hence the stated global norm is the one of the unique length-\(h+1\) chain. The small-angle expansion and \(\log N_h=(h+1)\log b+O_b(1)\) give its logarithmic asymptotic.

**3. Empirical distribution and all fixed moments.** For every \(L\le h\), the proportion of length-\(L\) chains is
\[
\frac{(b-1)b^{h-L}}{N_h}
=\frac{(b-1)^2 b^{-(L+1)}}{1-b^{-(h+1)}}.
\]
The exceptional length-\(h+1\) chain has proportion \(1/N_h\). The total proposed limiting mass is
\[
(b-1)^2\sum_{L\ge1}L b^{-(L+1)}=1.
\]
For \(p\ge0\), \(\max_j\sigma_{L,j}\le L+1/2\), by the concavity lower bound on sine on \([0,\pi/2]\), so \(\sum_j\sigma_{L,j}^p\le L(L+1/2)^p\). In the finite-height and limiting fixed-\(p\) moment formulas, the discrepancy from the factor \((1-b^{-(h+1)})^{-1}\), the omitted tail \(L>h\), and the exceptional long chain is bounded by a constant times \((h+1)^{p+1}b^{-h}\). This proves moment convergence, and in particular weak convergence, since the limiting law has unit mass and uniformly bounded second (hence first) moments. Directly, the same chain formula for bounded continuous test functions and geometric summability proves weak convergence without moment determinacy.

**4. Dense atomic support and a special atom.** Each of the positive coefficients in the law multiplies an atom. For \(1\le j\le L\), the angles \((2j-1)\pi/(4L+2)\), over all \(L\), are dense in \((0,\pi/2)\); the map \(\theta\mapsto(2\sin\theta)^{-1}\) maps this interval continuously onto \((1/2,\infty)\). The limit \(1/2\) is approached as \(j=L\), so the support is \([1/2,\infty)\). The equality \(\sigma_{L,j}=1\) requires the angle to be \(\pi/6\), or equivalently \(L=3j-2\), and geometric summation gives the displayed mass of \(\{1\}\).

**5. Sharp upper-tail rate.** Define \(L_*(t)\) as the least integer \(L\ge1\) with \(\sigma_{L,1}>t\). Since \(\sigma_{L,1}=(2L+1)/\pi+O(L^{-1})\), \(L_*(t)=(\pi/2)t+O(1)\). A block contributes no singular values larger than \(t\) when \(L<L_*(t)\), and contributes at least one when \(L\ge L_*(t)\). Therefore, writing \(w_L=(b-1)^2b^{-(L+1)}\),
\[
\sum_{L\ge L_*(t)}w_L
\le\nu_b((t,\infty))
\le\sum_{L\ge L_*(t)}Lw_L.
\]
The left sum is a positive constant times \(b^{-L_*(t)}\), and the right is at most a positive constant times \((L_*(t)+1)b^{-L_*(t)}\). Dividing their logarithms by \(t\) proves the exact exponential rate.

**6. Exact quadratic energy.** In a row indexed by a vertex at depth \(d\), the sum of squares of entries is \(\sum_{k=0}^{d}b^{-k}\). There are \(b^d\) such rows. Summing gives
\[
\sum_{d=0}^{h}b^d\sum_{k=0}^{d}b^{-k}
=\frac{b}{b-1}N_h-\frac{h+1}{b-1}.
\]
Divide by \(N_h\) and apply established moment convergence at \(p=2\) to obtain the limiting quadratic energy.

## Verification
The standalone file `artifacts/check.py` constructs the actual full ancestor matrix on every tested tree and compares its complete numerically computed singular list with the analytic block multiset (including multiplicities). It also compares direct Frobenius energy against the exact closed form and checks the limiting second moment by independently summing the limiting law. Execute `python3 artifacts/check.py` with Python 3 and NumPy. The finite checks cover \(b\in\{2,3,4\}\) and depths \(0\le h\le4\) when \(b=2\), and \(0\le h\le3\) otherwise. These checks are not a substitute for the proof of the all-height statements.

## Relationship to prior work
Evans, Harris and Lang (2000) study Hardy-type integration operators on metric trees, including approximation-number asymptotics at large spectral index on a given operator; their continuous-tree setting and limit differ from the present finite **vertex**-tree sequence and height-dependent all-singular-value measure. The balanced-shift Wold decomposition in Budzyński, Dymek, Płaneta and Ptak (2017) supplies an important related structural viewpoint; orthogonal shift-chain decompositions themselves are not asserted to be new. Kaarnioja (2020) treats extreme spectra of triangular \(0\)-\(1\) matrices, encompassing related one-chain extremal behavior, but not the full tree-dependent mixture or its limiting tail. Andriantiana, Dadedzi and Wagner (2018) study the leaf-indexed ancestral/common-ancestor Gram matrix, which is not the present all-vertices normalized ancestor operator. Allen and Jackson (2022) consider differentiation on tree function spaces with different norms/operators. The claimed contribution is the explicit branching-weighted singular measure, its dense atomic support, sharp large-value tail, and spectral-energy behavior.

## Limitations
This is a statement for complete regular \(b\)-ary *finite* trees at fixed branching factor and the precise level normalization above; it does not establish corresponding laws for irregular trees, other weights, metric-edge Hardy integration, or joint limits with branching varying. Singular-value coincidences can cause masses to combine. The proof establishes no claim of absolute bibliographic priority: other equivalent formulations may exist. The numerical checker samples finitely many trees, while the infinite height conclusions rest on the analytic argument.

## References
1. W. D. Evans, D. J. Harris, J. Lang, *The approximation numbers of Hardy-type operators on trees*, arXiv:math/0003215, first posted 2000-03-30. https://arxiv.org/abs/math/0003215
2. P. Budzyński, Z. Dymek, A. Płaneta, M. Ptak, *Weighted shifts on directed trees. Their multiplier algebras, reflexivity and decompositions*, arXiv:1702.00765 (2017), Section 6, Theorem 16. https://arxiv.org/abs/1702.00765
3. V. Kaarnioja, *Bounds on the spectrum of nonsingular triangular (0,1)-matrices*, arXiv:2002.03337 (2020). https://arxiv.org/abs/2002.03337
4. E. O. D. Andriantiana, K. Dadedzi, S. Wagner, *The ancestral matrix of a rooted tree*, arXiv:1809.03364 (2018). https://arxiv.org/abs/1809.03364
5. R. F. Allen, N. Jackson, *The differentiation operator on discrete function spaces of a tree*, arXiv:2207.10211 (2022). https://arxiv.org/abs/2207.10211
