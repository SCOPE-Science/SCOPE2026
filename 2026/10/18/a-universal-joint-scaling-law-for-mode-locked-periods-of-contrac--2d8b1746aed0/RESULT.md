# A universal joint scaling law for mode-locked periods of contracted rotations

## Finding
For \(0<\lambda<1\), put \(f_{\lambda,\delta}(x)=\{\lambda x+\delta\}\) on \([0,1)\), with \(\delta\) sampled uniformly from \([0,1)\). Let \(R_\lambda\in[0,1)\) be its rotation number, and let \(Q_\lambda\) be the least period of its attracting orbit where one exists. These are defined almost surely: the exceptional parameter set has Lebesgue measure zero. If \(R_\lambda=p/q\) in lowest terms, with the convention \(0=0/1\), then \(Q_\lambda=q\) almost surely.

Set \(h=-\log\lambda>0\), let \(\varphi\) be Euler's totient with \(\varphi(1)=1\), and write \(C_h=2(\cosh h-1)\). The exact period law is
\[
\Pr(Q_\lambda=q)=\frac{C_h\varphi(q)}{e^{hq}-1},\qquad q=1,2,\ldots.
\]
The individual rational rotation plateaux have the previously known widths used to obtain this law; these widths and the classical complete-staircase property are **not** asserted as new results.

**Joint neutral-contraction scaling theorem.** As \(h\downarrow0\), the pair \((R_\lambda,hQ_\lambda)\) converges weakly to independent random variables \((U,Z)\), where \(U\) is uniform on \([0,1]\) and \(Z\) has density
\[
 f_Z(t)=\frac{6}{\pi^2}\frac{t}{e^t-1}\,\mathbf1_{\{t>0\}}.
\]
In particular, for every nonnegative integer \(r\),
\[
\lim_{h\downarrow0}\mathbb E[(hQ_\lambda)^r]
=\frac{6\,\Gamma(r+2)\zeta(r+2)}{\pi^2}.
\]
Thus \(h\,\mathbb E Q_\lambda\to12\zeta(3)/\pi^2\), and \(h^2\operatorname{Var}(Q_\lambda)\to2\pi^2/5-(12\zeta(3)/\pi^2)^2\). The limiting density, its moments, and asymptotic independence of reduced winding fraction and scaled least period form a single distributional claim.

## Assumptions and scope
The contraction factor varies through real \(0<\lambda<1\); the parameter \(\delta\) has normalized Lebesgue distribution on \([0,1)\). The circle is represented by its standard interval, and \(\{y\}=y-\lfloor y\rfloor\). A rotation number is the average lift displacement per iterate (equivalently the asymptotic fraction of integer wraps), known to exist for these monotone contracted rotations. A periodic orbit has **least** period \(q\), not an arbitrary multiple. The statements are annealed over \(\delta\); they make no claim about a fixed exceptional \(\delta\), other map families, or the time to reach a periodic orbit. The limit is for \(h=-\log\lambda\downarrow0\); using \(1-\lambda\) as scale gives the same weak limit since \((1-\lambda)/h\to1\).

The oldest explicitly dated motivating open manuscript used for the dynamical classification is Nogueira--Pires, arXiv:1206.5676v1, initially public on 2012-06-25, which treats piecewise interval contractions with primary MSC 37E05. The explicit one-dimensional plateau formula used here appears in Laurent--Nogueira, arXiv:1704.05130, Theorem 3(ii), tracing its origins to Ding--Hemmer (1987) and Bugeaud--Conze (1999). Those historical inputs are credited rather than claimed as new.

## Proof
**1. Exactly weighted rational plateaux.** For coprime integers \(1\le p<q\), the classical contracted-rotation plateau formula says that the set of \(\delta\) with \(R_\lambda=p/q\) is the closed interval
\[
 \frac{1-\lambda}{1-\lambda^q}c_{p,q}(\lambda)
 \;\le\;\delta\;\le\;
 \frac{1-\lambda}{1-\lambda^q}
 \bigl(c_{p,q}(\lambda)+\lambda^{q-1}-\lambda^q\bigr),
\]
where
\[
 c_{p,q}(\lambda)=1+\sum_{j=1}^{q-2}
 \bigl(\lfloor (j+1)p/q\rfloor-\lfloor jp/q\rfloor\bigr)\lambda^j.
\]
The empty sum is zero. Every such interval has length
\[
 w_q(\lambda)=\frac{(1-\lambda)^2\lambda^{q-1}}{1-\lambda^q},
\]
independent of \(p\). At rotation number zero, the plateau \(0\le\delta\le1-\lambda\) has length \(1-\lambda=w_1(\lambda)\). Standard symbolic coding of these positive rational plateaux gives one attracting orbit of least period \(q\) in every plateau interior: the itinerary makes \(p\) wraps in \(q\) steps, and relative primeness excludes any smaller least period. Endpoints are a countable exceptional set, irrelevant to uniform \(\delta\).

For each \(q\ge2\), there are \(\varphi(q)\) reduced fractions in \((0,1)\), so \(\Pr(Q_\lambda=q)=\varphi(q)w_q(\lambda)\). The normalization does not require assuming the complement has measure zero: the elementary divisor identity \(\sum_{d\mid n}\varphi(d)=n\) gives, for \(0<\lambda<1\),
\[
 \sum_{q\ge1}\varphi(q)\frac{\lambda^q}{1-\lambda^q}
 =\sum_{n\ge1}n\lambda^n=\frac{\lambda}{(1-\lambda)^2}.
\]
Multiplication by \((1-\lambda)^2/\lambda\) shows the total length of all rational plateaux is one, and their interiors are disjoint because rotation number is single valued. Finally
\[
 w_q(\lambda)=\frac{(1-e^{-h})^2e^{-(q-1)h}}{1-e^{-qh}}
 =\frac{2(\cosh h-1)}{e^{hq}-1},
\]
which proves the exact probability formula.

**2. Totient averaging.** Möbius inversion gives
\[
 \varphi(q)=q\sum_{d\mid q}\frac{\mu(d)}d,
 \qquad
 \sum_{q\le X}\varphi(q)=\frac{3}{\pi^2}X^2+O(X\log(2X)).
\]
For completeness, the second statement follows by summing \(\sum_{d\mid q}\mu(d)q/d\) first over multiples of \(d\), and using \(\sum_{d\ge1}\mu(d)/d^2=6/\pi^2\); the floor errors contribute \(O(X\log(2X))\). Consequently, for continuous \(g\) supported in a compact subinterval of \((0,\infty)\), partial summation and \(C_h/h^2\to1\) yield
\[
 C_h\sum_{q\ge1}\frac{\varphi(q)}{e^{hq}-1}\,g(hq)
 \longrightarrow\frac6{\pi^2}\int_0^\infty\frac{t}{e^t-1}g(t)\,dt.
\]
The endpoint at zero is controlled uniformly by \(\varphi(q)\le q\) and \(e^{hq}-1\ge hq\): for \(0<a\le1\), the probability of \(hQ_\lambda\le a\) is \(O(a+h)\). For \(b\ge1\), the probability of \(hQ_\lambda\ge b\) is \(O((1+b)e^{-b})\), uniformly for small \(h\), by geometric summation. This proves tightness and extends the convergence to bounded continuous \(g\). The limiting density integrates to one because \(\int_0^\infty t/(e^t-1)\,dt=\zeta(2)=\pi^2/6\).

**3. Angular equidistribution and independence.** For \(q\ge2\), let \(A_q(u)\) be the number of reduced numerators \(1\le p<q\) with \(p/q\le u\), where \(0\le u\le1\). A second use of Möbius inversion gives
\[
 A_q(u)=u\varphi(q)+O(\tau(q)),
\]
uniformly in \(u\), where \(\tau\) is the divisor-counting function. In particular, the difference between the joint plateau mass of \(\{R_\lambda\le u,\;hQ_\lambda\in I\}\) and \(u\) times the period mass on any fixed compact interval \(I\subset(0,\infty)\) is bounded by
\[
 C_h\sum_{q\ge1}\frac{\tau(q)}{e^{hq}-1}
 =O\bigl(h\log^2(1/h)\bigr).
\]
Indeed, for \(q\le h^{-1}\), bound the denominator below by \(hq\) and use \(\sum_{q\le X}\tau(q)/q=O(\log^2(2X))\); for larger \(q\), split into geometric slabs and use \(\sum_{q\le X}\tau(q)=O(X\log(2X))\). The \(q=1\) plateau carries mass \(1-e^{-h}=O(h)\) and contributes nothing to the limit. By rectangle approximation and the tightness from Step 2, \((R_\lambda,hQ_\lambda)\) converges to the product of the uniform law and the density \(f_Z\).

**4. Moments.** The exponential-tail bound from Step 2 implies uniform integrability of every nonnegative integral power of \(hQ_\lambda\). For \(r\ge0\), expanding the geometric series and integrating termwise gives
\[
 \int_0^\infty t^r f_Z(t)\,dt
 =\frac6{\pi^2}\sum_{j\ge1}\int_0^\infty t^{r+1}e^{-jt}\,dt
 =\frac{6\Gamma(r+2)\zeta(r+2)}{\pi^2}.
\]
This proves the stated moment and variance asymptotics.

## Verification
The self-contained Python checker `verify.py` uses only the standard library plus an optional scientific special-functions module for a numerical \(\zeta(3)\) benchmark. Its exact-arithmetic portion verifies \(1000\) divisor identities and \(90\) independent rational plateau endpoint/width identities at slopes \(1/2\) and \(2/3\). The checker also follows \(90\) plateau-midpoint orbits to compare observed winding numbers with their coprime numerators, and verifies finite-distribution normalization and scaled first two moments at four contraction scales. Observed output:

`VERIFY_OK 90 exact rational tongues; 90 midpoint rotation simulations; 1000 totient-divisor identities; 4 limiting-law mass/moment checks`

The exact mathematical proof is Steps 1–4, not the finite experiments. The checker independently reconstructs plateau endpoints and iterate counts, but numerical evidence alone cannot certify convergence or bibliographic priority.

## Relationship to prior work
Ding--Hemmer (1987) and Bugeaud--Conze (1999) developed exact piecewise-linear mode-locking formulas. Laurent--Nogueira (arXiv:1704.05130, first submitted 2017-04-17), Theorem 3(ii), reproduces the equal-width rational plateaux, proves the zero-dimensional irrational exceptional set, and studies arithmetic properties of the parameters; their full arXiv manuscript is the operative original formula checked here. Nogueira--Pires (arXiv:1206.5676v1, 2012-06-25) gives the wider interval-contraction dynamics framework, including sharp periodic-orbit-count bounds.

The exact individual plateau widths, their Farey parameterization, and the totient divisor identity are known ingredients. The assessed claim combines them into a joint weak limit for a uniformly chosen control parameter as contraction vanishes, identifies the limiting scaled least-period density and all its moments, and proves asymptotic independence of rotation fraction and period. The prior materials inspected do not explicitly give this combined asymptotic statistical law. A paper with different terminology could subsume it; no claim of exhaustive historical priority is made.

## Limitations
The theorem assumes a uniform parameter \(\delta\); a parameter-dependent nonuniform law can change both limits. It applies only to the standard one-dimensional contracted-rotation family, not arbitrary monotone circle maps, nonlinear contractions, or independently randomized forcing. It gives no rates of convergence for the joint weak law and no basin-entry-time distribution. The 1987 source was accessible only as a publisher abstract, and a full copy of the 1999 Bugeaud--Conze source could not be inspected because the available download endpoint denied access. These are explicit historical-priority risks; neither is used as an unverified mathematical lemma, because the needed plateau formula was checked in the accessible full text of Laurent--Nogueira.

## References
1. A. Nogueira and B. Pires, *Dynamics of piecewise contractions of the interval*, arXiv:1206.5676v1 (initial public posting 2012-06-25), https://arxiv.org/abs/1206.5676.
2. M. Laurent and A. Nogueira, *Rotation number of interval contracted rotations*, arXiv:1704.05130v1 (initial public posting 2017-04-17); particularly Theorem 3(ii), https://arxiv.org/abs/1704.05130.
3. E. J. Ding and P. C. Hemmer, *Exact treatment of mode locking for a piecewise linear map*, Journal of Statistical Physics 46 (1987), 99–110, https://doi.org/10.1007/BF01010333.
4. Y. Bugeaud and J.-P. Conze, *Calcul de la dynamique de transformations linéaires contractantes mod 1 et arbre de Farey*, Acta Arithmetica 88 (1999), 201–218, https://doi.org/10.4064/aa-88-3-201-218.
