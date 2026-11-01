# Sharp nonlattice two-coset Gabor frames for the entire power-tent family

## Finding
For any real \(p\ge1\) let \(g_p(t)=(1-|t|)_+^p\). With \(T_n f(t)=f(t-n)\) and \(M_\xi f(t)=e^{2\pi i\xi t}f(t)\), form the indexed family
\[\mathcal G_{p,\delta}=\{M_mT_ng_p,M_{m+\delta}T_ng_p:n,m\in\mathbb Z\}.\]
Every real offset \(\delta\) is permitted, with two copies retained if the branches coincide. The *optimal* constants in
\[A_p(\delta)\|f\|_2^2\le \sum_{m,n\in\mathbb Z}\big(|\langle f,M_mT_ng_p\rangle|^2+|\langle f,M_{m+\delta}T_ng_p\rangle|^2\big)\le B_p(\delta)\|f\|_2^2\]
for every \(f\in L^2(\mathbb R)\) are
\[\boxed{A_p(\delta)=4^{1-p}(1-|\cos(\pi\delta)|),\qquad B_p(\delta)=2.}\]
Consequently these two-coset systems are frames precisely for \(\delta\notin\mathbb Z\). Modulo integers, the unique offset maximizing the lower bound (equivalently minimizing the sharp condition number) is \(\delta=1/2\), where \(\kappa_{p,\min}=2\cdot4^{p-1}\). As \(d=\operatorname{dist}(\delta,\mathbb Z)\downarrow0\),
\[A_p(\delta)=\frac{\pi^2}{2}4^{1-p}d^2+O_p(d^4).\]
The upper bound is independent of the offset and of the concentration exponent. This gives a complete two-parameter sharp conditioning classification for a continuum of power-tent windows, including nonlattice frequency cosets.

## Assumptions and scope
The window is compactly supported on \([-1,1]\), continuous and nonnegative, and its exponent \(p\) is any real at least one. The parameter \(\delta\) is an arbitrary real, reduced modulo one only when discussing uniqueness. Translation spacing equals one. The union of integer and shifted-integer modulation cosets need not form a frequency lattice. We do not claim analogous formulas for a third coset, different translation spacings, or exponents below one.

## Proof
For the unitary Zak transform \(Zf(x,\omega)=\sum_{k\in\mathbb Z}f(x+k)e^{-2\pi ik\omega}\), the critical Gabor frame operator with shifts \(\{M_mT_n\}\) acts as multiplication by \(|Zg|^2\). A modulation by \(\delta\) transforms the Zak variable by \(Z(M_\delta f)(x,\omega)=e^{2\pi i\delta x}Zf(x,\omega-\delta)\). Therefore the sum of the two critical frame operators acts as multiplication by
\[\mathsf S(x,\omega)=|Zg_p(x,\omega)|^2+|Zg_p(x,\omega-\delta)|^2.\]
Its essential infimum and supremum on the Zak unit square are exactly the optimal frame bounds.

For \(0\le x\le1\), only two translates of \(g_p\) are nonzero. Put \(a=(1-x)^p\), \(b=x^p\) and \(\theta=2\pi\omega\). Then \(Zg_p(x,\omega)=a+b e^{2\pi i\omega}\), up to replacing the phase by its conjugate, so
\[\mathsf S(x,\theta)=2(a^2+b^2)+2ab\big(\cos\theta+\cos(\theta-2\pi\delta)\big).\]
The cosine-sum ranges exactly over \([-2c,2c]\), where \(c=|\cos(\pi\delta)|\). Thus its minimum at fixed \(x\) is \(2(a^2+b^2)-4cab\). Convexity of the map \(s\mapsto s^{2p}\) yields
\[a^2+b^2=x^{2p}+(1-x)^{2p}\ge 2^{1-2p},\]
while \(ab=(x(1-x))^p\le 4^{-p}\). Hence for all \(x\) and \(\theta\),
\[\mathsf S\ge2^{2-2p}-4^{1-p}c=4^{1-p}(1-c).\]
Both inequalities are equalities at \(x=1/2\), and a phase \(\theta\) exists for which the cosine-sum is \(-2c\). The continuous Zak symbol therefore attains the stated global minimum.

For the upper bound, \(|a+b e^{i\theta}|\le a+b\), and since \(p\ge1\), \(a+b=(1-x)^p+x^p\le1\). Thus \(\mathsf S\le2\) everywhere. At the boundary fibre \(x=0\) one has \(a=1,b=0\), hence \(\mathsf S=2\) at every phase. Continuity makes this the essential supremum, proving sharpness. Positivity, uniqueness of the half-offset, and the collision expansion follow directly from the explicit formula. No finite enumeration is used to prove the all-parameter result.

## Verification
The proof reduces the infinite frame operator to a scalar continuous Zak multiplier. Both extremizers are exact: the lower symbol is attained at the central translation fibre with an appropriate frequency, and the upper symbol at either endpoint translation fibre. A supplied standalone script checks sampled parameter values directly against a two-dimensional grid; this is only a numerical consistency test, not the proof of the infinite assertions.

## Relationship to prior work
The frame-set theorem of de Dios Pont, Gröchenig, Liehr, Shafkulovska and Taylor (2026) addresses rectangular Gabor lattices for continuous totally positive windows. The power-tent family includes the ordinary hat B-spline at \(p=1\), but the present theorem also covers \(p>1\) and, crucially, nonlattice unions of *two modulation cosets*. Kloos and Stöckler (2013) studied exponential B-splines and computed sharp bounds in selected rectangular-lattice regimes. Faulhuber and Shafkulovska (2023) optimized bounds over rectangular lattices for several other window families. None of these inspected results provides the displayed sharp two-coset, all-real-\(p\) formula. The exact bounds answer a frequency-offset design question left outside those lattice models; this does not establish absolute historical novelty.

## Limitations
The result is special to support width two, spacing-one translations, the specified power-tent profile and two cosets. The case \(p=1,\delta=1/2\) is a standard lattice benchmark; novelty is claimed only for the combined nonlattice two-parameter classification, not for this specialization or the general Zak representation. A relevant earlier treatment of nonlattice multiwindow splines may give implicit coverage; independent scholarly verification is not yet performed.

## References
1. J. de Dios Pont, K. Gröchenig, L. Liehr, I. Shafkulovska, M. A. Taylor, *Gabor Frames of Totally Positive Functions: A Complete Characterization*, arXiv:2608.04992v1 (first posted 2026-08-05), https://arxiv.org/abs/2608.04992.
2. T. Kloos, J. Stöckler, *Zak transforms and Gabor frames of totally positive functions and exponential B-splines*, arXiv:1311.7359 (2013), https://arxiv.org/abs/1311.7359.
3. M. Faulhuber, I. Shafkulovska, *Gabor frame bound optimizations*, arXiv:2204.02917, 2023 version, https://arxiv.org/abs/2204.02917.
