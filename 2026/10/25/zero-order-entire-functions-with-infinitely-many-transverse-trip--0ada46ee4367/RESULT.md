# Zero-order entire functions with infinitely many transverse triple maximum-modulus circles

## Finding

There is a transcendental entire function \(f\) with real Taylor coefficients, \(f(0)=1\), \(f'(0)=-3/2\), and growth order \(\rho(f)=0\), and infinitely many distinct radii \(r_j\to\infty\) such that the circle \(|z|=r_j\) contains **exactly three** global maximum-modulus points: the positive real point \(r_j\) and one nonreal conjugate pair. Across each radius, the maximum points switch transversely: on a nonempty radius interval just below it only the conjugate pair maximizes, and on an interval just above it only the positive-axis point maximizes. The construction is by explicitly prescribed inductive choices of sparse polynomial blocks.

## Assumptions and scope

For entire \(f\), write \(M_f(r)=\max_{|z|=r}|f(z)|\) and \(\nu_f(r)=\#\{z:|z|=r,\ |f(z)|=M_f(r)\}\). Order is \(\rho(f)=\limsup_{r\to\infty}\log\log^+M_f(r)/\log r\), with the usual convention for small moduli. The assertion is one **existence** theorem, not a prescription of arbitrary radii. The radii are allowed to depend on the inductive construction. No assertion is made about connected components of the global maximum-modulus set.

Set
\[
P(z)=1-\frac32z+3z^2+2z^3,
\quad c_0=1,\ c_1=-\frac32,\ c_2=3,\ c_3=2.
\]
Begin with \(F_1=P\). For each \(j\ge2\), let \(d_{j-1}=\deg F_{j-1}\) and choose the integer \(m_j=2d_{j-1}+10\). Select \(R_j>0\) inductively, increasingly large, and put
\[
H_j(z)=R_j^{-m_j/2}z^{m_j}P(z/R_j),\qquad F_j=F_{j-1}+H_j.
\]
At each step choose \(R_j\) large enough to satisfy all finite strict inequalities in the proof, including \(R_j\ge(m_j+3)^j\), and ensure the future perturbation budgets on earlier annuli. Then \(f=\lim_{j\to\infty}F_j\) locally uniformly.

## Proof

**1. An explicit stable three-peak crossing.** Put \(x=\cos\theta\), \(\mathcal Q(r,x)=|P(re^{i\theta})|^2\). It is a real cubic in \(x\), with the exact identity
\[
\mathcal Q(1,x)=\frac{81}{4}-16(1-x)(x+\tfrac12)^2,\qquad -1\le x\le1.
\]
Its global maximum therefore occurs precisely at \(x=1\) and \(x=-1/2\). The latter corresponds to two angles, \(\theta=\pm2\pi/3\). Both angular peaks are nondegenerate: \(\partial_x\mathcal Q(1,1)=36>0\) makes \(\theta=0\) an angular strict maximum, while \(\partial_x^2\mathcal Q(1,-1/2)=-48<0\) makes the conjugate pair strict maxima. The analytic implicit function theorem gives a unique smooth branch \(x_-(r)\) of strict interior maxima for \(r\) near one, with \(x_-(1)=-1/2\). The axis remains an angular strict local maximum. On a sufficiently small closed annulus around radius one, these three are the only *possible global* maxima: away from disjoint neighborhoods of the three angular peaks, the strict inequality above has a uniform gap, while strict negative angular second derivatives give uniqueness within the neighborhoods.

The crossing gap is
\[
G(r)=\mathcal Q(r,1)-\mathcal Q(r,x_-(r)).
\]
Direct differentiation of the exact finite polynomial gives
\[
G(1)=0,\qquad G'(1)=\left.\partial_r\mathcal Q(r,1)\right|_{r=1}-\left.\partial_r\mathcal Q(r,-\tfrac12)\right|_{r=1}=27.
\]
Thus for some fixed \(0<\delta<1/10\), \(G(1-\delta)<0<G(1+\delta)\) and \(G'\) remains positive between those radii. This gives exactly one transverse three-peak radius for the base cubic, with two maxima below and one above.

**2. Stability under real-symmetric perturbations.** Fix the annulus \(1-\delta\le|z|\le1+\delta\). Consider the real-valued function \(|P(re^{i\theta})|^2\) on its radius-angle rectangle. A sufficiently small perturbation in the real \(C^2\) norm, together with smallness of its radius derivative and of the angular derivative of that radius derivative, preserves: (a) an axis critical-point strict maximum, using conjugation symmetry; (b) a unique strict interior positive-angle maximum and its negative-angle conjugate; (c) a uniform gap excluding other global maxima; (d) strict positivity of the radial derivative of their value difference. This follows directly from the implicit function theorem, compactness of the angular complement, and uniform continuity of derivatives. Hence every sufficiently small **real-coefficient holomorphic perturbation** of \(P\) on that annulus has a unique transverse radius where exactly those three points maximize. After multiplying by a nonvanishing radial modulus \(c r^m\) and by \(e^{im\theta}\), angular maxima are unchanged. This statement is valid uniformly under the corresponding normalized real-symmetric perturbations.

**3. Sparse-block induction.** Suppose \(F_{j-1}\) and protected disjoint compact annuli for its first \(j-1\) transverse crossings have been chosen. Choose \(R_j\) arbitrarily large, subject to the conditions below. On the new annulus \(r=R_j u\), \(1-\delta\le u\le1+\delta\), factor
\[
F_j(R_j u e^{i\theta})=R_j^{-m_j/2}(R_j u)^{m_j}e^{im_j\theta}
\left[P(ue^{i\theta})+E_j(u,\theta)\right],
\]
where
\[
E_j(u,\theta)=R_j^{m_j/2}(R_j u)^{-m_j}e^{-im_j\theta}F_{j-1}(R_j u e^{i\theta}).
\]
Since \(m_j>2d_{j-1}\), every mixed derivative \(\partial_u^a\partial_\theta^b E_j\), for \(a+b\le3\), tends uniformly to zero as \(R_j\to\infty\); explicitly each monomial of \(F_{j-1}\) yields \(O(R_j^{d_{j-1}-m_j/2})\) times a fixed polynomial in \(m_j\), uniformly for \(u\) in the fixed interval. Its coefficients are real, so the required reflection symmetry holds. By Step 2, the new annulus contains one stable transverse triple crossing. It is disjoint from old protected annuli when \(R_j\) is large.

Simultaneously, \(H_j\) and all its derivatives of total order at most three can be made arbitrarily small on each previously protected compact annulus and on \(|z|\le j-1\): here the factor \(R_j^{-m_j/2}\) dominates every fixed compact power of \(z\). On every protected annulus choose a positive stability margin supplied by Step 2; at step \(j\), demand its perturbation there is less than \(2^{-j}\) times an appropriately preallocated margin. This finite set of requirements is possible by enlarging \(R_j\). Inductively reserve half of the available stability margin for all subsequent perturbations, so that the sum of future real \(C^3\) changes to each protected annulus remains smaller than its allowed margin. Likewise impose \(\sup_{|z|\le j-1}|H_j(z)|\le2^{-j}\). Every stage imposes finitely many open inequalities and can be realized by a sufficiently large \(R_j\). Therefore \(F_j\to f\) locally uniformly, with the first \(j\) crossings preserved in the limit. By selecting \(R_j>4R_{j-1}\) the triple-circle radii are distinct and tend to infinity. The base cubic's first two Taylor coefficients are untouched because \(m_j\ge16\).

**4. Order zero.** The supports of the added blocks are disjoint and strictly increasing, because \(m_j>d_{j-1}\). For \(0\le\ell\le3\), the coefficient of \(z^{m_j+\ell}\) in \(f\) is exactly \(c_\ell R_j^{-m_j/2-\ell}\), and every sufficiently high coefficient not in these blocks is zero. Take \(R_j\ge(m_j+3)^j\). For large \(j\), \(\log(1/|a_{m_j+\ell}|)\ge (m_j/2)j\log(m_j+3)-O(1)\), so
\[
\limsup_{n\to\infty,\,a_n\ne0}\frac{n\log n}{\log(1/|a_n|)}=0.
\]
The standard coefficient characterization of entire-function order proves \(\rho(f)=0\). The coefficient at \(z^{m_j+3}\) is nonzero for each \(j\), so \(f\) is transcendental. This completes the proof.

## Verification

The standalone standard-library program `verify.py` expands the finite cubic identity exactly over rational numbers, checks the endpoint and interior second-derivative signs and the exact transverse slope \(27\), and verifies the degree inequalities for representative induction stages. Its checks are finite algebraic corroboration; the compactness and induction arguments establish the infinite claim. To reproduce, execute `python verify.py` alongside this file. The arbitrary-size choices of \(R_j\) are existential and the proof does not specify numerical values for all stages.

## Relationship to prior work

Li, *Maximum-modulus points on concentric circles* (2026, first submitted October 10), bounds \(\nu_f(r)\) generically by twice the first nonzero Taylor gap, outside a locally finite exceptional set. Here that gap is one, while the exceptional set is infinite even under the strongest finite order constraint, \(\rho(f)=0\). The current finding does not challenge Li's generic bound: its triple maxima occur only at separated exceptional radii. Only Li's abstract and bibliographic information were accessible, so overlap in inaccessible full-text details remains a specific priority risk.

Pardo-Simón and Sixsmith, *Variations on a theme of Hardy concerning the maximum modulus* (2019/2020), construct transcendental functions with prescribed discontinuity radii in class B, necessarily of order at least one half, and explicitly raise the possibility of order-zero discontinuities. The current theorem **does not resolve that open discontinuity question** because transverse local switching alone does not prove anything about connected components of the maximum-modulus set. Their 2020 polynomial paper prescribes finitely many discontinuity radii, without imposing the new zero-order infinite-circle property. Their 2026 work constructs finite-order examples with unbounded maximum counts using class B, which cannot contain functions of order zero. The older Herzog–Piranian phenomenon supplies unbounded maximum counts but the inspected descriptions do not control order or the first Taylor gap. These are comparisons of logical claims, not assertions of exhaustive priority searches.

## Limitations

The radii are chosen recursively rather than in advance; their spacing can be arbitrarily large. This is an existence theorem, not a finite algorithm outputting the whole function. The first two Taylor coefficients and exact triple-count structure are fixed. Neither discontinuities in the component-theoretic sense nor a prescribed density of exceptional radii are established. Possible coverage in inaccessible primary texts and older unindexed literature remains unresolved; independent audit is not available.

## References

1. Y. Li, *Maximum-modulus points on concentric circles*, arXiv:2610.15067, first posted 2026-10-10.
2. L. Pardo-Simón and D. J. Sixsmith, *Variations on a theme of Hardy concerning the maximum modulus*, arXiv:1911.05408, first posted 2019-11-13; Bull. Lond. Math. Soc. 52 (2020).
3. L. Pardo-Simón and D. J. Sixsmith, *The Maximum Modulus Set of a Polynomial*, arXiv:2007.07529, first posted 2020-07-15; Comput. Methods Funct. Theory 22 (2022).
4. L. Pardo-Simón and D. J. Sixsmith, *A finite-order answer to a problem of Erdős on maximum modulus points*, arXiv:2607.09462, first posted 2026-07-10.
