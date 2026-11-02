# Critical logarithmic Bergman–Szegő separation on finitely smooth Hartogs domains

## Finding
For each integer \(m\ge 2\) there exists a bounded pseudoconvex complete Reinhardt domain \(\Omega_m\subset\mathbb C^2\) with \(C^m\) boundary and a sequence of normal points \(z_k\to p\in\partial\Omega_m\) such that
\[
\liminf_{k\to\infty}\frac{\delta_{\Omega_m}(z_k)K_{\Omega_m}(z_k,z_k)}{S_{\Omega_m}(z_k,z_k)\log(1/\delta_{\Omega_m}(z_k))}>0.
\]
Here \(K\) is the unweighted Bergman diagonal kernel (Lebesgue-volume normalization), \(S\) is the Hardy–Szegő diagonal kernel for Euclidean surface measure, and \(\delta\) is Euclidean distance to the boundary. In fact, the construction has boundary not of class \(C^{m+1}\) at \(p\). Thus the power-one logarithm can be realized on a single bounded \(C^m\) pseudoconvex domain, despite the much weaker conclusion available from arbitrary fixed sublinear logarithmic gauges on smooth domains.

## Assumptions and scope
Fix an integer \(m\ge2\) and put \(c=m+1\). Define integers \(T_1=10\), \(T_{k+1}=\lceil e^{T_k}\rceil\), and positive quantities
\[
G_k=e^{-cT_{k+1}},\quad N_k=T_{k+1}-T_k-1,\quad b_k=e^{-T_k},\quad a_k=b_ke^{-N_k}=e^{1-T_{k+1}}.
\]
Let \(\chi\in C^\infty(\mathbb R)\) be nondecreasing, equal to zero on \(( -\infty,0]\) and one on \([1,\infty)\). For \(0<r\le1\) set
\[
q(r)=\sum_{\ell\ge1}(G_\ell-G_{\ell+1})\chi(\log r+T_{\ell+1}),\qquad q(0)=0,
\quad \varphi(r)=\int_0^r\frac{q(u)}{u}\,du.
\]
Choose \(\psi\in C^\infty([0,1))\), nonnegative, convex, nondecreasing, zero on \([0,1/4]\), and of the form \(C_*-\tfrac12\log(1-u)\) near \(u=1\). Define
\[
\Phi(\zeta)=\varphi(|\zeta|)+\psi(|\zeta|^2),\qquad
\Omega_m=\{(\zeta,w):|\zeta|<1,\ |w|<e^{-\Phi(\zeta)}\}.
\]
The boundary point is \(p=(0,1)\) and \(z_k=(0,w_k)\) with \(w_k=e^{-\varphi(b_k)}\). The construction uses ordinary Euclidean volume and surface measure, not normalized measures. The result is existential separately for each fixed \(m\); no constant uniform in \(m\) is asserted.

## Proof
**1. Smoothness and pseudoconvexity.** Since \(G_{\ell+1}<G_\ell\) and \(\chi\) is nondecreasing, \(q\ge0\) and \(q'\ge0\). On each interval \(e^{-T_{k+1}}\le r\le e^{-T_k}\), \(0\le q(r)\le G_k\), and differentiation of the single active transition yields for every fixed integer \(j\ge0\)
\[
|q^{(j)}(r)|\le C_jG_kr^{-j}.
\]
On the adjoining plateau the same estimate is immediate. Differentiating \(\varphi'=q/r\) and converting radial derivatives to partial derivatives gives for \(1\le j\le m\)
\[
|D^j\varphi(|\zeta|)|\le C'_jG_k|\zeta|^{-j}
\le C'_j e^{-(c-j)T_{k+1}}\longrightarrow0,
\]
whenever \(e^{-T_{k+1}}\le|\zeta|\le e^{-T_k}\). The same holds for the function itself. Therefore \(\varphi(|\zeta|)\) extends as a \(C^m\) function with vanishing derivatives of orders at most \(m\) at \(0\). Since \(q'\ge0\), \(\Delta\varphi=q'/r\ge0\) away from \(0\), and continuity extends subharmonicity across \(0\). The cap \(\psi\) is subharmonic, so \(\Phi\) is subharmonic. Its Hartogs subgraph is pseudoconvex and complete Reinhardt. Near \(|\zeta|=1\), its boundary has the smooth defining equation \(|\zeta|^2+e^{2C_*+2\varphi(|\zeta|)}|w|^2=1\); elsewhere \(|w|e^{\Phi(\zeta)}=1\) gives a \(C^m\) defining equation with nonzero normal derivative. It is bounded and star-shaped.

Moreover, on \([a_k,b_k]\) we have \(q=G_k\) and hence \(\varphi'(r)=G_k/r\). At its left endpoint \(a_k=e^{1-T_{k+1}}\), the transition is flat, so
\[
\varphi^{(m+1)}(a_k)=(-1)^m m!G_ka_k^{-(m+1)}=(-1)^m m!e^{-(m+1)}.
\]
At \(b_k\), the same radial derivative tends to zero because \(G_kb_k^{-(m+1)}\to0\). Thus the radial \((m+1)\)-st derivative has no continuous extension to zero. The boundary is not \(C^{m+1}\) at \(p\).

**2. Plateau geometry.** Write \(G=G_k\), \(N=N_k\), \(a=a_k\), \(b=b_k\). Telescoping the definition of \(q\) gives, for sufficiently large \(k\),
\[
q=G\ \text{on }[a,b],\qquad q\ge4G\ \text{on }[eb,1],\qquad \varphi(a)\le CG,
\qquad \varphi(b)=\varphi(a)+NG\asymp NG.
\]
For the third inequality the contribution of later shelves is bounded by \(\sum_{\ell>k}T_{\ell+1}G_\ell\), which is \(o(G_k)\) because \(T_{\ell+1}\) grows at least exponentially and \(G_\ell=e^{-cT_{\ell+1}}\). On \([a,b]\), \(\varphi(r)=\varphi(b)+G\log(r/b)\). The normal points therefore satisfy
\[
\delta_k:=\delta_{\Omega_m}(z_k)=1-w_k\asymp NG,
\quad \log(1/\delta_k)=cT_{k+1}-\log N+O(1)
\sim cT_{k+1},\quad N/T_{k+1}\to1.
\]
The equality of the Euclidean distance with \(1-w_k\) holds for sufficiently large \(k\) by the tubular-neighborhood normal projection at the \(C^2\) boundary point \(p\).

**3. Bergman lower and Szegő upper bounds.** Introduce the radial moments
\[
M(\lambda)=\int_{\mathbb D}e^{-2\lambda\Phi}\,dA,\qquad
\widetilde M(\lambda)=\int_{\mathbb D}e^{-2\lambda\Phi}\sqrt{1+e^{-2\Phi}|\nabla\Phi|^2}\,dA.
\]
Orthogonality of Reinhardt monomials and radial approximation in the star-shaped domain give on the normal axis
\[
K(0,w)=\frac1\pi\sum_{\nu\ge0}\frac{(\nu+1)|w|^{2\nu}}{M(\nu+1)},\qquad
S(0,w)=\frac1{2\pi}\sum_{\nu\ge0}\frac{|w|^{2\nu}}{\widetilde M(\nu+1/2)}.
\]
These formulas require only the established \(C^2\) regularity; the surface factor satisfies \(\widetilde M\ge M\). For \(1/2\le\lambda G\le3/4\), split the radial integral at \(a,b,eb\), use \(q=G\) on \([a,b]\), \(q\ge4G\) on \([eb,1]\), \(\varphi(a)\le CG\), and \(\psi\ge0\). The four pieces yield the uniform estimate
\[
M(\lambda)\le C b^2e^{-2\lambda\varphi(b)}.
\]
For example, on \([a,b]\) the exact radial integral is
\[
\int_a^b re^{-2\lambda\varphi(r)}dr=
 b^2e^{-2\lambda\varphi(b)}
\frac{1-e^{-2N(1-\lambda G)}}{2(1-\lambda G)};
\]
the inner part is bounded by \(\tfrac12e^{-2N(1-\lambda G)+2\lambda\varphi(a)}\) times the same normalization, and the two outer pieces are bounded by integrable exponentials with exponents \(2(1-\lambda G)\) and \(2(1-4\lambda G)\), respectively. There are \(\asymp G^{-1}\) integers \(\nu\) with \(1/2\le (\nu+1)G\le3/4\), for which \(\nu+1\asymp G^{-1}\). Consequently
\[
K(z_k)\ge\frac{c_0}{G^2b^2}.
\]

For the Hardy kernel, \(\psi=0\) on the relevant annulus and \(\widetilde M\ge M\), so for \(y=(\nu+1/2)G\),
\[
\widetilde M(\nu+1/2)\ge\pi b^2w_k^{2\nu+1}
\frac{1-e^{-2N(1-y)}}{1-y},
\]
with the continuous value \(2N\) at \(y=1\). Put \(R_N(y)=(1-y)/(1-e^{-2N(1-y)})\). Then \(R_N(y)\le C\) for \(0\le y\le1\), while \(R_N(y)\le CN^{-1}e^{-N(y-1)}\) for \(y>1\). Summation over \(\nu\), using \(NG\to0\), gives
\[
S(z_k)\le\frac{C_0}{b^2}\sum_{\nu\ge0}R_N((\nu+1/2)G)
\le \frac{C_1}{Gb^2}.
\]
These are the same elementary moment estimates underlying the published smooth-shelf construction; only the scale choice has changed.

**4. Endpoint conclusion.** The three bounds give
\[
\frac{\delta_k K(z_k)}{S(z_k)\log(1/\delta_k)}
\ge c_1\frac{N_k}{cT_{k+1}-\log N_k+O(1)}.
\]
Since \(N_k/T_{k+1}\to1\), the right side has positive limit inferior. This proves the finding for every fixed integer \(m\ge2\).

## Verification
The proof's critical equalities are exact consequences of the shelf definition: \(a_k=e^{1-T_{k+1}}\), \(\varphi(b_k)-\varphi(a_k)=N_kG_k\), and \(G_ka_k^{-(m+1)}=e^{-(m+1)}\). Each moment estimate was checked against the explicit inequalities in Section 4, equations (4.1)–(4.11), of Xing (2026). The changed exponential factor leaves all such estimates valid. No finite experimental sample is used as a proof of a limit. A check of the decoded package against its required files and checksums is recorded in the accompanying verification document.

## Relationship to prior work
Xing (2026), arXiv:2610.31043v1, Theorem 1.1 gives \(K/S\le C_\varepsilon\delta^{-1}(\log(1/\delta))^{1+\varepsilon}\) for all bounded \(C^2\) pseudoconvex domains. Its Proposition 4.1 constructs, for each increasing \(H=o(s)\), a **smooth** domain with \(\delta K/(S H(\log(1/\delta)))\to\infty\). These quantifiers do not imply that a **single domain** has \(\delta K/(S\log(1/\delta))\) bounded below by a positive constant. Indeed, the smooth scale \(G_k=e^{-kT_{k+1}}\) used there gives \(\log(1/\delta_k)\asymp kT_{k+1}\), whereas its lower estimate remains of order \(T_{k+1}\). The present fixed finite-smoothness choice \(G_k=e^{-(m+1)T_{k+1}}\) produces a genuine exponent-one endpoint on one domain for each regularity order \(m\). Chen–Fu (2010), arXiv:1006.4169v1, gives general comparison inequalities and no such critical lower construction in its inspected results. No uniqueness of the construction or universal optimal constants are claimed.

## Limitations
The logarithmic lower bound is along a particular inward-normal sequence at an infinite-type point; it is not a uniform lower bound throughout the domain. The examples are of finite differentiability and deliberately fail the next differentiability class. Therefore they do **not** settle whether a \(C^\infty\) example saturating the critical exponent exists. The comparison is conditional on the published normal-axis moment formulas and their standard Hardy surface normalization, which have been inspected; a separate independent audit remains unperformed. Earlier implicit coverage beyond the inspected sources cannot be categorically excluded.

## References
1. Xu Xing, *Comparison of the Bergman and Szegő kernels on arbitrary bounded pseudoconvex domains with C² boundary*, arXiv:2610.31043v1 (first public 2026-10-22), especially Proposition 4.1 and equations (4.1)–(4.11), https://arxiv.org/abs/2610.31043.
2. Bo-Yong Chen and Siqi Fu, *Comparison of the Bergman and Szegő kernels*, arXiv:1006.4169v1 (2010), especially Theorem 1.1, https://arxiv.org/abs/1006.4169.
