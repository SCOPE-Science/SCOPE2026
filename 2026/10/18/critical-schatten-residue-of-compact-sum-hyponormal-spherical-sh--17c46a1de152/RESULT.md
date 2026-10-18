# Critical Schatten residue of compact sum-hyponormal spherical shifts

## Finding

Let \(d\ge 2\) be an integer, \(H=\ell^2(\mathbb N_0^d)\), and let \((u_k)_{k\ge0}\) be a bounded sequence of nonnegative real numbers. Define a commuting radial spherical shift by
\[
T_j e_\alpha=u_{|\alpha|}\sqrt{\frac{\alpha_j+1}{|\alpha|+1}}\,e_{\alpha+e_j},\qquad j=1,\ldots,d.
\]
Put \(D_k=\binom{k+d-1}{d-1}\), \(b_k=D_{k+1}u_k^2\), \(b_{-1}=0\), \(Q=\sum_{j=1}^d[T_j^*,T_j]\), and \(q_d=2d/(d-1)\). The following is a complete endpoint classification within this radial family.

**Defect and endpoint theorem.** The tuple is sum-hyponormal precisely when \((b_k)\) is nondecreasing. Under that hypothesis, \(Q\) is positive and
\[
Qe_\alpha=\frac{b_{|\alpha|}-b_{|\alpha|-1}}{D_{|\alpha|}}e_\alpha,
\qquad \operatorname{Tr}Q=\lim_{k\to\infty}b_k\in[0,\infty].
\]
Here trace class is equivalent to finiteness of the displayed trace. For every nonzero sum-hyponormal tuple, each coordinate fails \(\mathcal S_p\) for all \(0<p\le q_d\). More sharply,
\[
Q\in\mathcal S_1\quad\Longleftrightarrow\quad
T_j\in\mathcal S_{q_d,\infty}\quad(\text{for one, equivalently every }j),
\]
where \(\mathcal S_{q_d,\infty}\) is the weak Schatten ideal; either condition makes every coordinate compact. If the finite defect trace is \(b=\operatorname{Tr}Q>0\), then every coordinate belongs to \(\mathcal S_p\) precisely for \(p>q_d\), and its singular-value counting function has the exact limit
\[
\lim_{t\downarrow0}t^{q_d}\#\{n:s_n(T_j)>t\}=C_{d,b},
\]
with
\[
C_{d,b}=\frac{[b(d-1)!]^{d/(d-1)}}{d!}
\frac{\Gamma(1+d/(d-1))\Gamma(d)}{\Gamma(d+d/(d-1))}.
\]
Thus \(\lim_{n\to\infty}n^{1/q_d}s_n(T_j)=C_{d,b}^{1/q_d}\) and
\[
\boxed{\lim_{N\to\infty}\frac1{\log N}\sum_{n=1}^Ns_n(T_j)^{q_d}=C_{d,b}.}
\]
The coefficient depends only on the dimension and the total trace of the positive summed self-commutator, not on its distribution among homogeneous degrees. For \(d=2\), this coefficient is \(b^2/6\); for \(d=3\), it is \(4(2b)^{3/2}/105\), equivalently \(8\sqrt6/35\) at \(b=3\).

For arbitrary bounded nonnegative \((u_k)\), without sum-hyponormality, the exact strong-ideal membership criterion is
\[
T_j\in\mathcal S_p\quad\Longleftrightarrow\quad
\sum_{k\ge0}D_ku_k^p<\infty\qquad(p>0).
\]

## Assumptions and scope

All operators act on the complex Hilbert space \(H\). The multiindex set is \(\mathbb N_0^d\), \(e_\alpha\) is its standard orthonormal basis, and \([A,B]=AB-BA\). Coordinates \(j\) are arbitrary but fixed. The sequence \((u_k)\) is bounded and nonnegative; zeros are allowed. The counting function counts singular values with multiplicities, including all positive singular values. For noncompact operators, weak-Schatten membership is understood to fail. Nonzero sum-hyponormality means at least one \(u_k>0\); then \(\lim b_k>0\), possibly infinite. The statement does not assert any such law for arbitrary nonspherical or nonradial commuting tuples.

## Proof

### 1. Commutation and diagonal positive defect

On degree \(k=|\alpha|\), the squared weight in direction \(j\) is \(u_k^2(\alpha_j+1)/(k+1)\). Two possible degree-two paths in different coordinate directions have squared products
\[
u_k^2u_{k+1}^2\frac{(\alpha_i+1)(\alpha_j+1)}{(k+1)(k+2)},
\]
so positivity of weights gives \(T_iT_j=T_jT_i\); if a weight is zero both paths vanish. The outgoing square norms at \(e_\alpha\) sum to \(u_k^2(k+d)/(k+1)\). For \(k\ge1\), the incoming square norms sum to \(u_{k-1}^2\) because \(\sum_j\alpha_j=k\). There is no incoming term at \(k=0\). Since \(D_{k+1}/D_k=(k+d)/(k+1)\), the diagonal formula follows:
\[
\langle Qe_\alpha,e_\alpha\rangle
=\frac{b_k-b_{k-1}}{D_k}.
\]
Consequently \(Q\ge0\) exactly when \(b_k\ge b_{k-1}\) for every \(k\). There are exactly \(D_k\) basis elements of degree \(k\), so the positive trace over degrees \(0,\ldots,K\) is \(\sum_{k=0}^K(b_k-b_{k-1})=b_K\). Monotone convergence for the positive diagonal trace proves the asserted trace formula, including the infinite case.

### 2. Singular-value multiset and all strong ideals

For fixed \(j\), the images of distinct basis vectors under \(T_j\) have distinct supports. Hence \(T_j^*T_j\) is diagonal, with eigenvalues \(u_k^2(\alpha_j+1)/(k+1)\) for \(|\alpha|=k\). Its operator norm is \(\sup_k u_k\): the upper bound is immediate, and the vector \(e_{ke_j}\) attains the weight \(u_k\). Norm truncations to finitely many degrees show that \(T_j\) is compact precisely when \(u_k\to0\). Define \(x_\alpha=(\alpha_j+1)/(k+1)\in[0,1]\). By symmetry of the \(D_k\) multiindices,
\[
\frac1{D_k}\sum_{|\alpha|=k}x_\alpha
=\frac{k+d}{d(k+1)}\ge\frac1d.
\]
For \(0<p\le2\), \(x_\alpha^{p/2}\ge x_\alpha\); for \(p\ge2\), Jensen's inequality gives \(D_k^{-1}\sum x_\alpha^{p/2}\ge d^{-p/2}\). Always \(x_\alpha^{p/2}\le1\). Thus, with \(c_{d,p}=\min\{d^{-1},d^{-p/2}\}\),
\[
c_{d,p}D_ku_k^p\le\sum_{|\alpha|=k}\left(u_k\sqrt{x_\alpha}\right)^p\le D_ku_k^p.
\]
Summing proves the asserted \(\mathcal S_p\) criterion for every \(p>0\).

If \(Q\ge0\) and the tuple is nonzero, then \(b_k\) is eventually bounded below by a positive constant, whence \(u_k^2=b_k/D_{k+1}\ge c/D_{k+1}\). As \(D_k\asymp k^{d-1}\), the criterion contains the divergent series \(\sum_k k^{(d-1)(1-p/2)}\) whenever \(p\le 2d/(d-1)\). Thus no nonzero such coordinate lies in \(\mathcal S_p\) for \(p\le q_d\). If \(b_k\to b<\infty\), the corresponding upper bound yields \(T_j\in\mathcal S_p\) for every \(p>q_d\); it also yields compactness.

### 3. Trace class is equivalent to the weak critical ideal

If \(b_k\) is bounded, \(u_k^2\le b/D_{k+1}\le C(k+1)^{-(d-1)}\). Hence a singular value above \(t\) must come from some degree \(k\lesssim t^{-2/(d-1)}\). The number of multiindices of these degrees is \(O(t^{-q_d})\). Thus \(\sup_{t>0}t^{q_d}\#\{n:s_n(T_j)>t\}<\infty\), which is equivalent to \(T_j\in\mathcal S_{q_d,\infty}\).

Conversely, suppose \(b_k\) is nondecreasing but unbounded. For each degree \(k\), the mean of \(x_\alpha\) above is at least \(1/d\), and \(0\le x_\alpha\le1\). Thus at least \(D_k/(2d-1)\) of its values satisfy \(x_\alpha\ge 1/(2d)\). Among degrees \(K/2\le k\le K\), these multiindices number at least \(c_dK^d\). By monotonicity of \(b_k\), each corresponding singular value is at least
\[
\tau_K=\sqrt{\frac{b_{\lfloor K/2\rfloor}}{2dD_{K+1}}}.
\]
Consequently, \(\#\{n:s_n(T_j)>\tau_K/2\}\ge c_dK^d\), and
\[
(\tau_K/2)^{q_d}\#\{n:s_n(T_j)>\tau_K/2\}
\ge c_d' b_{\lfloor K/2\rfloor}^{q_d/2}\longrightarrow\infty,
\]
because \(D_{K+1}\asymp K^{d-1}\) and \((d-1)q_d/2=d\). Therefore the coordinate is not in weak \(\mathcal S_{q_d}\). This proves both directions of the endpoint equivalence.

### 4. Exact counting constant and logarithmic residue

Suppose \(b_k\nearrow b\in(0,\infty)\), and put \(\delta=d/(d-1)\). For small \(t>0\), set
\[
L_t=\left(\frac{b(d-1)!}{t^2}\right)^{1/(d-1)}.
\]
On any compact region of rescaled multiindices \(x=\alpha/L_t\) with \(h=\sum_i x_i>0\), the squared singular weight divided by \(t^2\) tends uniformly, away from coordinate boundaries, to \(x_j/h^d\): indeed \(D_{k+1}\sim k^{d-1}/(d-1)!\), \(b_k\to b\), and \((\alpha_j+1)/(k+1)\to x_j/h\). Moreover, for large degrees \(k>(1+\varepsilon)L_t\), the maximal squared weight is below \(t^2\); finitely many small degrees contribute negligibly to \(t^{q_d}\) times the counting function. The boundary \(x_j=h^d\) has zero \(d\)-dimensional volume. Standard bounded-region lattice Riemann sums therefore imply
\[
\lim_{t\downarrow0}\frac{\#\{n:s_n(T_j)>t\}}{L_t^d}
=\operatorname{vol}\{x\in[0,\infty)^d:x_j>(\sum_i x_i)^d\}.
\]
Write \(h=\sum_i x_i\) and \(v=x/h\) in the standard simplex. At each fixed \(h\), the coordinate fraction \(V=v_j\) is distributed as \(\mathrm{Beta}(1,d-1)\) with respect to normalized simplex volume, and the degree-\(d\) volume element is \(h^{d-1}dh/(d-1)!\) times the simplex probability. The region is \(0<h<V^{1/(d-1)}\), so its volume is
\[
\frac1{(d-1)!}\mathbb E\int_0^{V^{1/(d-1)}}h^{d-1}\,dh
=\frac1{d!}\mathbb E(V^\delta)
=\frac1{d!}\frac{\Gamma(1+\delta)\Gamma(d)}{\Gamma(d+\delta)}.
\]
Since \(L_t^d=t^{-q_d}[b(d-1)!]^\delta\), the counting limit equals the specified \(C_{d,b}\). Standard monotone inversion of counting functions then gives \(s_n\sim C_{d,b}^{1/q_d}n^{-1/q_d}\). Raising to the power \(q_d\), summing, and using \(\sum_{n\le N}n^{-1}\sim\log N\) proves the logarithmic residue.

## Verification

The standalone standard-library script `verify.py` checks rational formulas for commutation squares, outgoing and incoming defects, and degree-by-degree telescoping for dimensions \(2,3,4\), several nondecreasing coefficient profiles, and finite degree cutoffs. It also counts exact finite singular weights at small thresholds for the constant-defect cases in dimensions \(2\) and \(3\), comparing their scaled counts with the independently derived beta-integral coefficient. Its output is `SPHERICAL_SUM_DEFECT_SPECTRAL_FINITE_CHECKS_OK assertionsets=231`. These finite calculations are not proofs of the infinite-dimensional counting limit; that limit is proved by the bounded-region Riemann-sum argument above.

## Relationship to prior work

Chavan, Reza and Sequeira's September 16, 2026 paper introduces the sum-hyponormal problem and analyzes structural decompositions of compact tuples, but its inspected main results and examples do not give a weak-Schatten classification of coordinates or the critical spectral residue. Chavan and Yakubovich's 2014/2015 treatment classifies Schatten membership of **cross-commutators** of spherical shifts (not the singular values of the coordinate operators themselves); see their Theorem 4.2 and Corollaries 4.5–4.6. Kim, Kim and Yoon characterize spherical \(p\)-hyponormality of two-variable weighted shifts; this agrees with positivity being a weight inequality but does not imply the new coordinate Weyl coefficient.

A prior published explicit compact, quasinilpotent, rank-one summed-defect multishift realizes the special profile \(b_k=d\) in the notation here. That construction supplies one example but does not state the present classification for **every** nondecreasing radial profile, the equivalence of finite defect trace and the weak critical ideal, or the universal leading singular-value and logarithmic-residue constants. The present statement includes that example as one boundary test, and makes no new existence claim about it.

## Limitations

The theorem covers the specified radial spherical multishifts, not general sum-hyponormal commuting tuples, general nonradial weights, or the Schatten properties of mixed commutators. It does not determine second-order terms in singular-value asymptotics. The finite verifier checks algebra and sampled counts only. Novelty is assessed against the cited accessible sources and published research records; a stronger result in unlocated literature could affect originality.

## References

1. S. Chavan, M. R. Reza and S. S. Sequeira, *Sum of self-commutators of commuting operators*, arXiv:2609.19287v1 (first public posting September 16, 2026), https://arxiv.org/abs/2609.19287.
2. S. Chavan and D. Yakubovich, *Spherical Tuples of Hilbert Space Operators*, arXiv:1401.0487 (2014), Indiana University Mathematics Journal 64 (2015), https://repositorio.uam.es/bitstream/10486/676124/1/Spherical_Chavan_iumj_2015.pdf.
3. H. W. Kim, J. Kim and J. Yoon, *Spherical Aluthge transform, spherical p and log-hyponormality of commuting pairs of operators*, Linear and Multilinear Algebra 70 (2022), 2047–2064, https://doi.org/10.1080/03081087.2020.1781040.
4. *Compact quasinilpotent sum-hyponormal multishifts with rank-one defect*, publicly released research note (September 18, 2026), https://github.com/published-finding corpus/2026/tree/main/2026/9/18/SCOPE-compact-quasinilpotent-sum-hyponormal-multishifts--17493782d86c.
