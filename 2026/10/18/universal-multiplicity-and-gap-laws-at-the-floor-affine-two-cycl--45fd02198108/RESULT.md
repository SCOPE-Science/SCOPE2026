# Universal multiplicity and gap laws at the floor-affine two-cycle explosion

## Finding

Consider the floor-affine dynamical system \(f_{\lambda,\mu}(x)=\lfloor\lambda x+\mu\rfloor\) on \(\mathbb R\). Fix \(0<\varepsilon<1\), a sign \(s\in\{-1,1\}\), \(\lambda=-1+s\varepsilon\), and \(q=1-\lambda=2-s\varepsilon\). Let \(U\) be uniform on \([0,q)\); write \(N\) for the number of *distinct primitive period-two orbits* of \(f_{\lambda,U}\) (unordered two-element integer cycles). For every integer \(m\ge1\),

\[
\boxed{\Pr(N\ge m)=\frac{(1-2m\varepsilon)_+ +(1-(2m-1)\varepsilon)_+}{2-s\varepsilon}},\qquad (v)_+=\max\{v,0\}.
\]

In particular, whenever \(1\le m\le\lfloor (2\varepsilon)^{-1}\rfloor-1\), the mass is exactly \(\Pr(N=m)=4\varepsilon/(2-s\varepsilon)\). Define the triangular phase profile \(\tau(u)=\operatorname{dist}(u,\{0,1,2\})\) for \(0\le u\le2\), with \(\tau(u)=0\) for \(u>2\). The stronger pointwise profile estimate
\[
\boxed{\sup_{0\le u<q}|\varepsilon N(u)-\tau(u)|\le\varepsilon}
\]
holds for both signs, with \(N(u)\) the deterministic two-cycle count at offset \(u\). For both approaches to the singular slope \(-1\),

\[
\boxed{\varepsilon N\ \xrightarrow[\varepsilon\downarrow0]{\ \mathrm{law}\ }\ \operatorname{Uniform}[0,1/2]}. 
\]

Writing \(F_\varepsilon\) for the CDF of \(\varepsilon N\), the quantitative bound
\[
\boxed{\sup_{t\in\mathbb R}|F_\varepsilon(t)-F_{\mathrm{unif}[0,1/2]}(t)|\le\frac{6\varepsilon}{2-\varepsilon}}
\]
holds for every \(0<\varepsilon<1\) and either sign. Consequently \(\varepsilon\mathbb E[N]\to1/4\), \(\varepsilon^2\operatorname{Var}(N)\to1/48\), and every fixed positive moment of \(\varepsilon N\) converges to the corresponding uniform moment. The finite-parameter level-set *lengths* are the same on both sides of \(-1\); the denominators differ because the natural phase periods have different lengths.

There is also an **orbit-gap law**. Conditional on \(N>0\), select one of the \(N\) primitive two-cycles uniformly and let \(K\) be the positive difference of its integer coordinates. As \(\varepsilon\downarrow0\), the joint distribution converges:
\[
\boxed{(\varepsilon N,\varepsilon K)\ \xrightarrow{\mathrm{law}}\ (T,2TV)},
\qquad T\sim\operatorname{Uniform}[0,1/2],\quad V\sim\operatorname{Uniform}[0,1],
\]
with \(T\) and \(V\) independent. Consequently the limiting rescaled gap \(G=2TV\) has the exact density
\[
\boxed{p_G(g)=-\log g,\qquad 0<g<1},
\]
and \(\mathbb E[G^r]=(r+1)^{-2}\) for every \(r>0\). This law distinguishes the *geometry* of the proliferating cycles from their mere number.

## Assumptions and scope

All maps use the exact mathematical floor function; no rounding or floating-point dynamics is assumed. Every periodic point belongs to \(\mathbb Z\), because the first image of any real point is an integer. By the exact identity
\[
f_{\lambda,\mu+q}(x+1)=f_{\lambda,\mu}(x)+1,
\]
\([0,q)\) is a natural parameter interval modulo integer-translation conjugacy. The phase measure is *uniform parameter sampling*, not an invariant probability distribution of the map. The statement counts only prime two-cycles, not fixed points, basins, or all infinite-orbit behavior. Both parameter signs are admitted throughout \(0<\varepsilon<1\), i.e. \(-2<\lambda<0\) excluding \(\lambda=-1\).

## Proof

**Period-two feasibility.** Write a primitive two-cycle as \(x<y=x+k\) with \(x\in\mathbb Z\), \(k\in\mathbb N\). The necessary and sufficient equations \(f(x)=x+k\), \(f(x+k)=x\) mean, with \(q=1-\lambda\),
\[
\mu\in[qx+k,qx+k+1)\ \cap\ [qx-\lambda k,qx-\lambda k+1).
\]
The intersection is empty for \(k\varepsilon\ge1\), and otherwise has length \(1-k\varepsilon\). Its exact form is
\[
\begin{cases}
[qx+k,qx+k+1-\varepsilon k),&s=1,\\
[qx+(1+\varepsilon)k,qx+k+1),&s=-1.
\end{cases}
\]
The half-open endpoint convention follows from that of \(\lfloor\cdot\rfloor\); even at a boundary there is no double counting of cycles.

**Two nested parameter towers.** For \(k=2j\), \(j\ge1\), translate the interval by \(qj\) (equivalently choose \(x=-j\)) to obtain
\[
E_j=[j\varepsilon,1-j\varepsilon),
\]
nonempty exactly when \(2j\varepsilon<1\). For \(k=2j+1\), \(j\ge0\), similarly obtain
\[
O_j=\begin{cases}
[1+j\varepsilon,2-(j+1)\varepsilon),&s=1,\\
[1+(j+1)\varepsilon,2-j\varepsilon),&s=-1,
\end{cases}
\]
nonempty exactly when \((2j+1)\varepsilon<1\). Every nonempty interval is wholly contained in \([0,q)\). For each \(k\), at most one integer translate intersects that fundamental interval, so \(E_j\) and \(O_j\) enumerate all cycles without multiplicity. The \(E_j\) are nested and lie in \([0,1)\); the \(O_j\) are nested and lie in \([1,q)\). Hence the set of phases with at least \(m\) cycles is precisely \(E_m\cup O_{m-1}\). Its Lebesgue length is
\[
(1-2m\varepsilon)_+ +(1-(2m-1)\varepsilon)_+.
\]
Dividing by \(q\) proves the survival law. Subtracting the survival probabilities at \(m\) and \(m+1\) proves the interior constant-mass identity.

**Uniform triangular phase profile.** In \([0,1)\), the number of nested even-gap intervals containing \(u\) differs from \(\min\{u,1-u\}/\varepsilon\) by at most one: compare the strict and weak inequalities \(j\varepsilon<u\) and \(j\varepsilon\le u\) and likewise at \(1-u\). On the odd-gap half, put \(v=u-1\) and \(w=2-u\). For \(s=1\), admissible \(j\ge0\) satisfy \(j\varepsilon\le v\), \(j\varepsilon<w-\varepsilon\); the resulting count differs from \(\min\{v,w\}/\varepsilon\) by at most one. For \(s=-1\), the conditions are \((j+1)\varepsilon\le v\) and \(j\varepsilon<w\), with the same one-count error. If \(s=-1\), the extra phase strip \([2,q)\) has no cycles. Multiplying by \(\varepsilon\) proves the pointwise phase-profile estimate, including all endpoints.

**Critical scaling.** Let \(t\ge0\), \(m=\lfloor t/\varepsilon\rfloor+1\), and \(a=\varepsilon m\), so \(t<a\le t+\varepsilon\). Write \(h(t)=(1-2t)_+\), which is the survival function of \(\operatorname{Uniform}[0,1/2]\). Since positive-part is 1-Lipschitz,
\[
|(1-2a)_+-h(t)|\le2\varepsilon,
\qquad |(1-2a+\varepsilon)_+-h(t)|\le3\varepsilon.
\]
Using \(|q-2|=\varepsilon\), \(q\ge2-\varepsilon\), and \(0\le h(t)\le1\), we conclude
\[
\left|\Pr(\varepsilon N>t)-h(t)\right|\le\frac{6\varepsilon}{q}\le\frac{6\varepsilon}{2-\varepsilon}.
\]
For \(t<0\), the two distribution functions agree. This proves the CDF bound and the limit law. The survival formula also implies \(\varepsilon N<(1+\varepsilon)/2\) almost surely, hence the scaled family is uniformly bounded. Convergence of each fixed positive moment follows; the mean and variance limits are \(1/4\) and \(1/48\), respectively.

**Critical orbit-gap geometry.** At a fixed phase \(u\), either only the even gaps \(2,4,\ldots,2N(u)\) occur or only the odd gaps \(1,3,\ldots,2N(u)-1\) occur, as follows from the two disjoint towers. Conditional on that phase and a uniformly chosen cycle, a quantile coupling to \(V\sim\operatorname{Uniform}[0,1]\) satisfies
\[
|\varepsilon K-2\varepsilon N(u)V|\le2\varepsilon.
\]
The triangular phase estimate gives \(|\varepsilon K-2\tau(u)V|\le4\varepsilon\). The probability of \(N=0\) is at most \(4\varepsilon/(2-\varepsilon)\) for \(0<\varepsilon<1/2\), by the survival formula, so conditioning on \(N>0\) does not change the weak limit of the phase distribution. Couple the uniform phase on \([0,2-s\varepsilon)\) to a uniform phase \(U_0\in[0,2)\) by rescaling, an error at most \(\varepsilon\). Since \(\tau\) is 1-Lipschitz and \(\tau(U_0)\sim\operatorname{Uniform}[0,1/2]\), the joint limit is \((T,2TV)\). Finally \(2T\) and \(V\) are independent uniform random variables on \([0,1]\). Their product has distribution function \(g(1-\log g)\) on \(0<g<1\), density \(-\log g\), and moments \(1/(r+1)^2\).

## Verification

The standalone standard-library program `verify.py` independently counts genuine period-two cycles by evaluating \(f(x)\) and \(f(f(x))\) with exact rational arithmetic. It tests both parameter signs, ten rational values of \(\varepsilon\), interior offsets, and both sides and the exact values of every predicted interval endpoint. The pointwise triangular profile error bound is also checked for every sampled phase. Separately it integrates the integer-cycle census over the exact partition of the phase interval and checks every nonzero survival probability. Further exact-rational tests evaluate the first two moments of the rescaled gap obtained by selecting a cycle uniformly within each nonempty phase; these approach the proved limits \(1/4\) and \(1/9\). A completed run reported **3,208 exact-rational assertions** passed. The finite test supports endpoint handling; it does not replace the proof for arbitrary real parameters or the asymptotic limit.

## Relationship to prior work

Hoseana's *The dynamics of one-dimensional quasi-affine maps* (arXiv:2406.14055v1, 20 June 2024), Theorem 2, already gives the complete two-cycle census for each fixed pair \((\lambda,\mu)\), and Theorem 3 describes limiting orbits. That exact fixed-parameter classification is **prior work and not claimed as new**. The present result concerns instead the parameter-conjugacy quotient, its exact cycle-count distribution, the nearly flat finite-parameter probability spectrum, the triangular singular profile, and the joint critical orbit-gap law with a logarithmic density. The proof derives these explicitly from the basic two-cycle inequalities; its novelty depends on absence of an equivalent published parameter-ensemble analysis. Rozikov, Sattarov, and Usmonov's earlier unshifted floor-affine dynamics consider the narrower zero-offset family. A related published result on quantized affine contractions describes basin selection and settling times, rather than the phase-law of cycle multiplicities.

## Limitations

This is a *parameter-ensemble theorem*. Uniformly sampling the additive phase does not model a randomly forced orbit. The conditional cycle-gap law samples one cycle uniformly at a random parameter; it does not sample all cycles globally with equal weight. The law is not an all-parameter classification of other periods; the fixed-parameter two-cycle census is previously known. An unindexed equivalent averaging or asymptotic consequence of earlier census formulas cannot be excluded; in particular the main novelty is a new quantitative synthesis of an existing complete periodic-orbit formula, not a new count at individual parameters. Numerical checks used a finite parameter sample, while the proof covers the continuum.

## References

1. J. Hoseana, *The dynamics of one-dimensional quasi-affine maps*, arXiv:2406.14055v1 (20 June 2024), https://arxiv.org/html/2406.14055v1. Theorem 2 and its proof, and Theorem 3.
2. U. A. Rozikov, I. A. Sattarov, and J. B. Usmonov, *The dynamical system generated by the floor function* \(\lfloor\lambda x\rfloor\), arXiv:1503.07129 (2015), https://arxiv.org/abs/1503.07129.
3. *Outermost-cycle basin selection and logarithmic settling for quantized affine contractions*, publicly indexed mathematical record b81ca333b81c (summary only inspected).
