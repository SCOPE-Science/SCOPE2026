# A zero-or-half relative numerical-index dichotomy for positive Hilbert contractions

## Finding

Let \(H\) be a separable, infinite-dimensional **complex** Hilbert space, and let \(G\in\mathcal B(H)\) be a positive contraction with \(\|G\|=1\). For \(T\in\mathcal B(H)\), define the near-norm-attainment operator seminorm and relative numerical radius by
\[
p_G(T)=\inf_{\delta>0}\sup_{\substack{\|x\|=1\\\|Gx\|>1-\delta}}\|Tx\|,
\qquad
v_G(T)=\inf_{\delta>0}\sup_{\substack{\|x\|=\|y\|=1\\\operatorname{Re}\langle Gx,y\rangle>1-\delta}}|\langle Tx,y\rangle|.
\]
The inner product is linear in its first variable; both suprema are taken over nonempty sets. Define the relative numerical index even when \(p_G\) is only a seminorm:
\[
\eta(G)=\inf\{v_G(T)/p_G(T):T\in\mathcal B(H),\ p_G(T)>0\}.
\]
Then, writing \(D=I-G^2\),
\[
\boxed{\displaystyle
\eta(G)=\begin{cases}
\frac12,&D=0\ \text{or}\ D\ \text{is compact and injective},\\
0,&\text{otherwise}.
\end{cases}}
\]
Both values are attained by explicit test operators. In the compact-injective case, for every bounded \(T\),
\[
p_G(T)=\|T\|_{\mathrm{ess}},\qquad
v_G(T)=w_{\mathrm{ess}}(T),
\]
where \(\|T\|_{\mathrm{ess}}\) is the Calkin essential norm and \(w_{\mathrm{ess}}(T)\) the maximal modulus of its essential numerical range. In particular, a positive norm-one contraction has no relative numerical index strictly between zero and one-half. **The index here is relative to \(p_G\), not the older index relative to the full operator norm.**

## Assumptions and scope

Throughout, \(H\) is infinite-dimensional, separable and complex, \(0\le G\le I\), and \(\|G\|=1\). The operator \(D=I-G^2\) is a positive contraction with spectral infimum zero. Write \(E_J=\mathbf1_J(D)\) for its spectral projections. A unit sequence \((x_n)\) is *near norming* for \(G\) when \(\|Gx_n\|\to1\), equivalently \(\|D^{1/2}x_n\|\to0\). We write \(x_n\rightharpoonup0\) for weak convergence to zero.

The essential norm is \(\|T\|_{\mathrm{ess}}=\inf_{K\in\mathcal K(H)}\|T-K\|\). The essential numerical radius may be defined without choosing a quotient representation:
\[
w_{\mathrm{ess}}(T)=\sup_{\substack{\|x_n\|=1\\x_n\rightharpoonup0}}\limsup_{n\to\infty}|\langle Tx_n,x_n\rangle|.
\]
This equals the numerical radius of the image of \(T\) in the Calkin algebra. The definitions and result do **not** presume that the seminorm \(p_G\) is a norm; when \(D\) is compact injective, every compact operator is in its kernel.

## Proof

**1. Replace admissible pairs by near-norming vectors.** The spectral inequality \((I-G)^2\le I-G^2=D\) holds since \(0\le G\le I\). Thus, when \(\|Gx_n\|\to1\) for unit vectors, \(\|(I-G)x_n\|\to0\). If unit vectors \(x,y\) satisfy \(\operatorname{Re}\langle Gx,y\rangle>1-\delta\), then \(\|Gx\|>1-\delta\) and
\[
\|y-Gx\|^2=1+\|Gx\|^2-2\operatorname{Re}\langle Gx,y\rangle<2\delta.
\]
Consequently \(y-x\to0\) along every sequence of admissible pairs with \(\delta\to0\). Conversely, a near-norming sequence satisfies \(\langle Gx_n,x_n\rangle\to1\), so taking \(y_n=x_n\) makes the pairs admissible asymptotically. By diagonal selection in the defining suprema,
\[
\begin{aligned}
p_G(T)&=\sup_{\|x_n\|=1,\ \|Gx_n\|\to1}\limsup_n\|Tx_n\|,\\
v_G(T)&=\sup_{\|x_n\|=1,\ \|Gx_n\|\to1}\limsup_n|\langle Tx_n,x_n\rangle|.
\end{aligned}
\tag{1}
\]
The formulas remain valid if the suprema are not achieved; choose approximate maximizers for \(\delta=1/n\). Both functionals are bounded by \(\|T\|\), and \(v_G(T)\le p_G(T)\).

**2. Compact injective defect.** Assume \(D\) is compact and \(\ker D=\{0\}\). For unit sequences, near norming is equivalent to weak nullity. Indeed, \(D^{1/2}\) is compact, so weak-null vectors satisfy \(\|D^{1/2}x_n\|\to0\). Conversely, \(\|D^{1/2}x_n\|\to0\) implies \(x_n\rightharpoonup0\): the range of \(D^{1/2}\) is dense (its orthogonal complement is its kernel), and
\[
|\langle x_n,D^{1/2}z\rangle|
=|\langle D^{1/2}x_n,z\rangle|\to0
\]
for every fixed \(z\). Thus (1) gives
\[
p_G(T)=\sup_{x_n\rightharpoonup0,\ \|x_n\|=1}\limsup_n\|Tx_n\|=\|T\|_{\mathrm{ess}},
\qquad v_G(T)=w_{\mathrm{ess}}(T).
\tag{2}
\]
The operator-norm identity follows directly: compact operators send bounded weak-null sequences to norm-null sequences, giving the upper estimate. Conversely, if \(P_N\) are projections onto the first \(N\) basis vectors, choose unit \(x_N\in(I-P_N)H\) nearly attaining \(\|T(I-P_N)\|\). These vectors are weak-null, and \(\|T(I-P_N)\|\to\|T\|_{\mathrm{ess}}\) because \(TP_N\) is finite rank and \(\|K(I-P_N)\|\to0\) for each compact \(K\).

For completeness, the essential numerical radius is the tail-compression limit
\[
w_{\mathrm{ess}}(T)=\lim_{N\to\infty}w\big((I-P_N)T(I-P_N)\big),
\tag{3}
\]
where the compression is regarded as an operator on \((I-P_N)H\). Every weak-null unit sequence is asymptotically contained in the tail for each fixed \(N\), proving the upper bound in (3). Conversely, choose near-maximizing unit vectors in successive tails; these form a weak-null sequence and prove the reverse inequality. Similarly,
\[
\|T\|_{\mathrm{ess}}=\lim_{N\to\infty}\|(I-P_N)T(I-P_N)\|.
\tag{4}
\]
Indeed, the difference between \(T\) and each compression is finite rank, while the double-tail compression of every compact perturbation tends to zero in norm. The classical complex-Hilbert numerical-radius inequality \(\frac12\|S\|\le w(S)\) applied to every tail and then (3)--(4) gives
\[
v_G(T)\ge\tfrac12 p_G(T)\quad\text{for every }T.
\tag{5}
\]
To see sharpness, decompose \(H=H_0\oplus H_0\) with \(H_0\) infinite-dimensional and use the square-zero partial isometry \(T(u,v)=(v,0)\). It has essential norm one and essential numerical radius exactly one-half: the elementary bound \(|\langle v,u\rangle|\le(\|u\|^2+\|v\|^2)/2\) is sharp on infinitely many mutually orthogonal two-dimensional blocks. Therefore \(\eta(G)=1/2\).

**3. Vanishing defect.** If \(D=0\), then \(G=I\), \(p_G(T)=\|T\|\), and \(v_G(T)=w(T)\). The classical numerical-radius inequality gives \(\eta(G)\ge1/2\), and the preceding square-zero operator gives equality.

**4. A nonzero defect kernel forces index zero.** Suppose \(\ker D\ne\{0\}\) and \(D\ne0\). Choose a unit \(u\in\ker D\) and \(\varepsilon>0\) such that \(F=E_{[\varepsilon,1]}\ne0\). Pick a unit \(v\in FH\), and let \(T x=\langle x,u\rangle v\). Since \(Gu=u\), \(p_G(T)=1\). Every near-norming unit sequence satisfies
\[
\|Fx_n\|\le\varepsilon^{-1/2}\|D^{1/2}x_n\|\to0.
\]
Hence \(|\langle Tx_n,x_n\rangle|\le\|Fx_n\|\to0\), so (1) gives \(v_G(T)=0\). Thus \(\eta(G)=0\).

**5. Noncompact defect with trivial kernel forces index zero.** Suppose \(\ker D=0\) and \(D\) is not compact. Some \(\varepsilon>0\) has \(F=E_{[\varepsilon,1]}\) infinite-dimensional; otherwise finite-rank approximants \(DE_{[\varepsilon,1]}\) would converge to \(D\). The lower spectral subspace \(L=E_{[0,\varepsilon/2)}H\) is also infinite-dimensional. Indeed, \(0=\inf\sigma(D)\), but a finite-dimensional such spectral subspace, together with \(\ker D=0\), would give a positive lower spectral bound for \(D\), a contradiction. Because \(H\) is separable, there is a partial isometry \(T\) with initial space \(L\) and final space \(FH\), so \(\|T\|=1\) and \(\operatorname{ran}T\subseteq FH\). There are unit vectors in \(LH\) with arbitrarily small \(\langle Dx,x\rangle\), which give \(p_G(T)=1\). For every near-norming unit sequence,
\[
|\langle Tx_n,x_n\rangle|
=|\langle Tx_n,Fx_n\rangle|
\le\|Fx_n\|\le\varepsilon^{-1/2}\|D^{1/2}x_n\|\to0.
\]
Thus \(v_G(T)=0\) by (1), proving \(\eta(G)=0\) and exhausting all cases.

## Verification

The standalone `CHECK.py` uses no third-party packages. It checks exact finite-dimensional matrix and probability inequalities behind the two zero witnesses, the polarization bound for square-zero blocks, and the quantitative spectral estimates on a family of increasingly near-norming vectors. Run it using `python3 CHECK.py`; successful execution prints the actual number of assertions. The infinite-dimensional dichotomy is proved by the spectral arguments above, **not** by finite numerical experiments. In particular, no finite matrix has the compact-injective infinite-dimensional branch by itself; the examples in the checker are finite truncations of the stated infinite models.

Two explicit infinite families illustrate the discontinuity. On \(\ell^2(\mathbb N)\), the diagonal positive contraction \(G_{\varepsilon}e_n=\sqrt{1-\varepsilon/(n+1)}\,e_n\), for \(0<\varepsilon<1\), has compact injective defect and index one-half. In contrast, \(F_{\varepsilon}=(I-\varepsilon P_{e_1})^{1/2}\) has a nonzero finite-rank defect and index zero. Both approach the identity in operator norm as \(\varepsilon\downarrow0\).

## Relationship to prior work

Dey and Pal introduced the relative numerical index and studied its geometry in *On the geometry of \(G\)-norm*, arXiv:2603.20796v1 (first public March 21, 2026). Theorems 3.12--3.14 cover partial-isometry necessity for finite Hilbert spaces, a norm-attainment gap criterion, and comparison of relative seminorms; their Question 1 asks about the infinite-dimensional analogue. They do not state the present all-positive-contraction numerical-index dichotomy. Their paper works primarily where the relative seminorm is a norm, whereas the genuinely different compact-injective case here naturally has a seminorm with compact kernel.

Kadets, Martín, Merí, Pérez, and Quero, *On the numerical index with respect to an operator*, arXiv:1905.12257v1 (2019), study the index normalized by the **full** operator norm. Their Proposition 4.12 establishes a zero-or-half phenomenon in complex Hilbert settings for that different index. In our compact-injective branch the full-operator-norm index is zero, because rank-one operators can have vanishing relative radius, whereas the present seminorm-relative index is exactly one-half. Thus the two classifications are not equivalent.

Kadets, Martín, Merí, and Quero, *Generating operators between Banach spaces*, arXiv:2306.02645v1 (2023; published 2024), analyze when \(p_G\) equals the **full** norm. The published note *Compact-defect characterization of the essential norm among relative operator seminorms* (2026, online research record) characterizes when \(p_G\) equals the essential norm; that characterization is acknowledged in (2) and is not claimed as new here. The new assertion instead identifies \(v_G\) in that branch, proves the entire complementary zero-index classification, and yields the exact sharp numerical-index phase diagram. Essential numerical ranges and weak-null formulas are classical (Stampfli--Williams and subsequent work).

## Limitations

The theorem requires positivity, complex scalars, infinite-dimensional separable Hilbert space, and the seminorm-based normalization explicitly defined above. It does not classify nonpositive operators, Banach-space analogues, or a relative numerical index obtained by dividing by the full operator norm. In the compact-injective case, \(p_G\) is not a norm, so any interpretation imposing a norm hypothesis must exclude that case. No independent mathematical audit has been performed. Literature searches cannot rule out unindexed equivalent statements.

## References

1. L. K. Dey and S. Pal, *On the geometry of \(G\)-norm*, arXiv:2603.20796v1, March 21, 2026. https://arxiv.org/html/2603.20796
2. V. Kadets, M. Martín, J. Merí, A. Pérez and A. Quero, *On the numerical index with respect to an operator*, arXiv:1905.12257v1, May 29, 2019. https://arxiv.org/abs/1905.12257
3. V. Kadets, M. Martín, J. Merí and A. Quero, *Generating operators between Banach spaces*, arXiv:2306.02645v1, June 5, 2023. https://arxiv.org/html/2306.02645v1
4. *Compact-defect characterization of the essential norm among relative operator seminorms*, online mathematical research record (2026). https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-compact-defect-characterization-of-the-essential-norm-among-rela--668d42891382
5. J. G. Stampfli and J. P. Williams, *Growth conditions and the numerical range in a Banach algebra*, Tohoku Math. J. 20 (1968), 417--424; see also the classic essential-numerical-range literature by Fillmore, Stampfli and Williams.
