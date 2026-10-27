# Sharp logarithmic covering law for irrational rotation parameters of two-slope interval maps

## Finding
Fix the two-branch interval family and admissibility conditions below. For each nondegenerate compact rotation window \([u,v]\) strictly inside the allowed rotation interval, let \(E_{u,v}\) be the set of translation parameters with irrational rotation number in that window. Write \(N_\varepsilon(E)\) for the smallest number of closed real intervals, each of length \(\varepsilon\), whose union contains \(E\). There are constants \(0<C_1<C_2<\infty\), depending only on the fixed parameters and \([u,v]\), and \(\varepsilon_0>0\) such that
\[
 C_1(\log(1/\varepsilon))^2\le N_\varepsilon(E_{u,v})\le C_2(\log(1/\varepsilon))^2
 \qquad(0<\varepsilon<\varepsilon_0).
\]
Consequently the logarithmic covering exponent is exactly \(2\):
\[
 \lim_{\varepsilon\downarrow0}
 \frac{\log N_\varepsilon(E_{u,v})}{\log\log(1/\varepsilon)}=2.
\]
In particular, every such slice has both upper and lower box dimension zero. The union of all irrational-rotation parameters over the full admissible translation interval has Hausdorff dimension zero. All assertions include systems with an expanding right branch (\(\lambda\mu>1\)) provided the stated parameter conditions hold. This is a uniform-scale covering statement, not a claim about the sharpness of Hausdorff gauge measures.

## Assumptions and scope
Take real numbers \(0<\lambda<1\), \(\mu>0\), and \(0\le c<b\le1\), with either \(\lambda\mu\le1\) or \((1-b)\mu\le1-c\). Define
\[
 d=\begin{cases} b-c\lambda,&\lambda\mu<1,\\
 (1-\lambda)(\mu b-c)/(\mu-1),&\lambda\mu\ge1,
 \end{cases}
 \qquad
 r=\begin{cases}1,&\lambda\mu<1,\\
 -\log\lambda/\log\mu,&\lambda\mu\ge1.
 \end{cases}
\]
For \(a\in(b-b\lambda,d)\), put \(\eta=(b-a)/\lambda\) and
\[
 f_a(x)=\begin{cases}
 \lambda x+a,&0\le x<\eta,\\
 \lambda\mu(x-\eta)+c,&\eta\le x<1.
 \end{cases}
\]
This is the admissible two-interval family of Gaivão, Laurent and Nogueira. Denote its rotation number by \(\rho(a)\in(0,r)\). Choose arbitrary fixed \(0<u<v<r\), and set
\[
 E_{u,v}=\{a\in(b-b\lambda,d):\rho(a)\in[u,v]\setminus\mathbb Q\}.
\]
The bounds concern the parameter \(a\), not the spatial invariant Cantor set for a particular map. All logarithms are natural; intervals in \(N_\varepsilon\) have *length* \(\varepsilon\), not radius \(\varepsilon\).

## Proof
**1. The inverse staircase and its rational gaps.** Write \(e_k(t)=\lfloor(k+1)t\rfloor-\lfloor kt\rfloor\in\{0,1\}\), and define the convergent series
\[
 S(t)=\sum_{k\ge1}e_k(t)\lambda^k\mu^{\lfloor kt\rfloor},
 \qquad
 A(t)=\frac{(1-\lambda)[b+(\mu b-c)S(t)]}{1+(\mu-1)S(t)}.
\]
By [1, Definition 5.1, Theorem 5.2, Proposition 7.1], \(A\) is strictly increasing, right-continuous, continuous at irrationals, and \(a\in E_{u,v}\) precisely when \(a=A(t)\) for an irrational \(t\in[u,v]\). At any reduced rational \(p/q\in(u,v)\), \(0<p<q\), the entire parameter interval \([A((p/q)^-),A(p/q)]\) has rational rotation number \(p/q\), and its endpoints are outside \(E_{u,v}\). With \(S_+=S(p/q)\) and \(S_-=S((p/q)^-)\), the source gives
\[
 S_+-S_-=\frac{(1-\lambda)\lambda^{q-1}\mu^{p-1}}
 {1-\lambda^q\mu^p}>0.
\]
The rational plateaux are disjoint and ordered by \(p/q\).

**2. Uniform exponential estimates.** Put \(\theta=\lambda\max\{1,\mu^v\}<1\), \(s_*=\lambda\min\{\mu^u,\mu^v\}\in(0,1)\), and \(D(t)=1+(\mu-1)S(t)\). For every \(t\in[u,v]\), \(0\le S(t)\le\theta/(1-\theta)\), and the series tail obeys
\[
 0\le S(t)-S_N(t)\le\frac{\theta^{N+1}}{1-\theta},
 \quad S_N(t)=\sum_{k=1}^Ne_k(t)\lambda^k\mu^{\lfloor kt\rfloor}.
\]
All denominators \(D\), including one-sided values and denominators using \(S_N\), have the positive uniform lower bound \(1-\lambda\). Indeed if \(\mu\ge1\) then \(D\ge1\); when \(\mu<1\), putting \(h_k=\mu^{\lfloor kt\rfloor}\) gives the telescoping identity
\[
 1+(\mu-1)S(t)=(1-\lambda)
 \sum_{k\ge1}\lambda^{k-1}h_k\ge1-\lambda.
\]
For finite truncations with \(\mu<1\), the denominator is larger. On the segments between \(S_N(t)\) and \(S(t)\), and on the interval between either pair of rational one-sided values, the function
\[
 B(s)=\frac{(1-\lambda)[b+(\mu b-c)s]}{1+(\mu-1)s}
\]
has derivative \(B'(s)=(1-\lambda)(b-c)/(1+(\mu-1)s)^2>0\) and a uniform Lipschitz constant \(L=(b-c)/(1-\lambda)\). This follows from the denominator lower bound on these segments (no such bound is asserted for arbitrary nonattained values of \(s\)). On these segments its denominator is also uniformly bounded above by some \(D_*<\infty\). Therefore, writing \(G_{p/q}=A(p/q)-A((p/q)^-)\),
\[
 G_{p/q}=\frac{(1-\lambda)(b-c)(S_+-S_-)}
 {[1+(\mu-1)S_-][1+(\mu-1)S_+]}
 \ge C_*s_*^q,
\]
where one may take \(C_*=(1-\lambda)^2(b-c)/(\lambda\mu D_*^2)>0\), since \(1-\lambda^q\mu^p\in(0,1)\) and \(\lambda^q\mu^p\ge s_*^q\).

**3. Upper bound by finite symbolic thresholds.** The partial sum \(S_N(t)\) is constant on each connected component of \([u,v]\) after removal of all reduced rationals having denominator at most \(N+1\). There are at most \(1+\sum_{q=1}^{N+1}q=O(N^2)\) such components. On each component, \(A(t)=B(S(t))\) differs from the common value \(B(S_N)\) by at most \(L\theta^{N+1}/(1-\theta)\). Hence one \(\varepsilon\)-interval covers the image of all irrational \(t\) in that component whenever \(L\theta^{N+1}/(1-\theta)\le\varepsilon\). At most two more intervals account for irrational endpoints \(u,v\). Taking \(N=O(\log(1/\varepsilon))\) proves the desired upper bound.

**4. Lower bound from distinct rational tongues.** Let \(Q\ge1\) and count reduced rationals \(p/q\in(u,v)\) with \(q\le Q\). The classical Farey-fraction estimate, obtained by counting lattice points and applying Möbius inversion, gives
\[
 M(Q)=\frac{3(v-u)}{\pi^2}Q^2+O_{u,v}(Q\log Q).
\]
Set \(h=-\log s_*>0\) and \(Q=\lfloor\log(1/\varepsilon)/(2h)\rfloor\). By Step 2 every counted rational plateau has length at least \(C_*s_*^Q=C_*\exp(-hQ)\ge C_*\sqrt\varepsilon>\varepsilon\) for sufficiently small \(\varepsilon\). Order these \(M(Q)\) plateaux. Between each successive pair choose an irrational rotation number and its associated point in \(E_{u,v}\). By the strict monotonicity of \(A\), consecutive chosen parameter points are separated by an intervening rational plateau longer than \(\varepsilon\). Thus no closed interval of length \(\varepsilon\) contains two chosen points, implying \(N_\varepsilon(E_{u,v})\ge M(Q)-1\gg(\log(1/\varepsilon))^2\). Together with Step 3 this completes the proof.

**5. Dimensions and a genuinely expanding example.** Since the covering count grows more slowly than \(\varepsilon^{-s}\) for every \(s>0\), each \(E_{u,v}\) has upper box dimension zero, hence Hausdorff dimension zero. A countable exhaustion of \((0,r)\) by compact windows yields zero Hausdorff dimension for the entire irrational-rotation parameter set. For an explicit expanding-branch instance, take \(\lambda=1/2\), \(\mu=3\), \(b=1\), \(c=0\); its right slope is \(3/2>1\), \(r=\log 2/\log 3\), and the law applies on \([u,v]=[1/5,3/5]\). Its reduced half-rotation plateau is exactly \([2/3,7/10]\).

## Verification
The independent exact-rational script `verify.py` checks \(7,139\) finite symbolic and rational identities, including the Möbius derivative, the rational plateau-width formula, geometric truncations, finite symbolic threshold cells, and two-slope parameters with \(\lambda\mu>1\). To replay: run `python verify.py` with Python 3 and SymPy. The proof of the universal lower bound uses the explicit rational-plateau formula and the Farey asymptotic, not finite sampling. The proof of the upper bound uses the global series-tail estimate, not numerical approximations.

## Relationship to prior work
[1] determines the exact inverse rotation staircase, its rational plateau endpoints, and the allowed parameter range for arbitrary two slopes; these foundational statements are used without claiming them as new. [2] had already obtained this inverse staircase for the normalized three-parameter two-slope family. [3, Theorem 7.1] proved gauge-Hausdorff bounds for the uniformly contracting single-slope map and used a related \(O(N^2)\)-component upper covering argument; it neither gives a matching uniform-scale lower covering law nor treats a right branch of slope greater than one. [4] proves Hausdorff dimension zero in a different uniform-contraction parameter family. The present contribution combines a **matching** lower bound from exponentially large Farey plateau separations with an upper bound valid under average (rather than branchwise) contraction. A rational-plateau representation alone is not the asserted logarithmic cover law.

## Limitations
The constants depend on the compact window and need not stay bounded as \(u\downarrow0\) or \(v\uparrow r\). In particular no global full-interval box-counting bound is asserted at the limiting rotation endpoint when \(\lambda\mu\ge1\). The estimate is up to multiplicative constants; it does not assert existence or an explicit value of \(\lim N_\varepsilon/(\log(1/\varepsilon))^2\), nor settle optimal Hausdorff gauge measures. The first-publication priority of this quantitative formulation is subject to possible unindexed equivalent work.

## References
[1] J. P. Gaivão, M. Laurent, A. Nogueira, *Rotation number of 2-interval piecewise affine maps*, arXiv:2212.10944v1 (2022), Definition 5.1, Theorem 5.2 and Proposition 7.1; https://arxiv.org/abs/2212.10944.

[2] M. Laurent, A. Nogueira, *Dynamics of 2-interval piecewise affine maps and Hecke–Mahler series*, arXiv:1907.08655v1 (2019), Theorem 1; https://arxiv.org/abs/1907.08655.

[3] S. Janson, A. Öberg, *A piecewise contractive dynamical system and election methods*, arXiv:1709.06398v1 (2017), Section 7, Theorem 7.1; https://arxiv.org/abs/1709.06398. Journal version: *Bull. Soc. Math. France* 147 (2019), 395–441.

[4] J. P. Gaivão, *Hausdorff dimension of the exceptional set of interval piecewise affine contractions*, arXiv:2211.14140v1 (2022), Theorem A; https://arxiv.org/abs/2211.14140.

[5] G. H. Hardy and E. M. Wright, *An Introduction to the Theory of Numbers*, chapters on Farey fractions and Euler's totient function (classical reduced-fraction asymptotics).
