# Exact statistical-period spectrum of decoupled delayed tent dynamics

## Finding

Consider the generalized tent map
\[
T_\beta(x)=\beta+1-\beta|x|,\qquad 1<\beta\le2,
\]
and its zero-coupling \(d\)-delay system
\[
F_{d,\beta}(x_0,\ldots,x_{d-1})=(x_1,\ldots,x_{d-1},T_\beta(x_0)),\qquad d\ge2.
\]
Work on the product of the natural compact absolutely continuous invariant cores, not on the entire real phase space. Let \(n\ge0\) be the unique integer satisfying
\[
2^{1/2^{n+1}}<\beta\le2^{1/2^n},\qquad p=2^n.
\]
The classical one-dimensional band theorem supplies \(p\) cyclic positive-measure bands with exact return dynamics, recalled below. The new delayed-system conclusion is a complete formula for its statistical-period spectrum and ergodic-component count.

The natural product invariant probability has exactly \(p^d\) phase cells, labeled by \(a\in(\mathbb Z/p\mathbb Z)^d\). Their exact one-step permutation is
\[
R(a_0,\ldots,a_{d-1})=(a_1,\ldots,a_{d-1},a_0+1\pmod p).
\]
**Each cycle of this affine permutation corresponds to exactly one ergodic component**, whose cyclic statistical period is the cycle length. No further splitting of these components occurs. For \(0\le k\le dp\), define \(g=\gcd(d,k)\) (so \(g=d\) for \(k=0\)). The number of fixed phase cells of the \(k\)-th iterate is exactly
\[
H_{d,p}(k)=\#\operatorname{Fix}(R^k)=
\begin{cases}
p^{g},&p\mid k/g,\\
0,&p\nmid k/g.
\end{cases}
\]
Consequently the number \(C_{d,p}\) of ergodic components is
\[
\boxed{C_{d,p}=\frac1{dp}\sum_{k=0}^{dp-1}H_{d,p}(k).}
\]
For every positive divisor \(\ell\mid dp\), the number of ergodic components with **least cyclic statistical period exactly** \(\ell\) is
\[
\boxed{N_{d,p}(\ell)=\frac1\ell\sum_{m\mid\ell}
\mu_{\mathrm{Mob}}(\ell/m)H_{d,p}(m),}
\]
where \(\mu_{\mathrm{Mob}}\) is the arithmetic Möbius function, not the invariant probability measure.

In particular, for a two-coordinate delay and \(p\ge2\), there are precisely \(p/2\) ergodic components, all of period \(2p\), despite \(p^2\) distinct positive-measure phase cells. At \(\beta=11/10\), the four bands in one dimension produce 16 two-dimensional phase cells but **two eight-phase ergodic components**. In a three-coordinate delay with \(p=4\), exactly one component has period 4 and five have period 12.

## Assumptions and scope

For a fixed \(\beta\), let \(K_\beta\subset\mathbb R\) be the natural compact invariant support of the standard absolutely continuous invariant probability \(\nu_\beta\) of \(T_\beta\). The source's previously established one-dimensional statistical-period theorem yields measurable bands \(I_0,\ldots,I_{p-1}\subset K_\beta\), disjoint modulo \(\nu_\beta\)-null sets, satisfying \(T_\beta(I_j)=I_{j+1\bmod p}\) modulo null sets and exactness of \(T_\beta^p\) on each conditional band probability \(p\nu_\beta|_{I_j}\). These known one-dimensional facts, including the slope window, are inputs and are **not** claimed here as new.

The theorem is for \(F_{d,\beta}:K_\beta^d\to K_\beta^d\), with invariant probability \(\nu_\beta^{\otimes d}\), and for densities absolutely continuous with respect to this probability. The formulas are exact for every integer \(d\ge2\) and every admissible slope, with the a.e. convention at boundaries and turning points. It does not concern nonzero coupling, dynamics outside the invariant core, singular invariant measures, or the global Lebesgue initial-condition basin of attraction.

By *cyclic statistical period* we mean the least number \(\ell\) of mutually singular cyclic limiting density states for an ergodic component, equivalently the least return time of its positive-mass exact phase pieces. The ergodic stationary measure itself remains invariant at every time. The formula counts periods of components, not the number of connected visible patches in a single numerical snapshot.

## Proof

**1. Invariant product measure and phase permutation.** Every \(T_\beta\)-invariant probability produces an invariant product probability for the delay map: applying \(F\) cyclically permutes coordinates and applies \(T_\beta\) to exactly one independent coordinate. Write \(Q_a=I_{a_0}\times\cdots\times I_{a_{d-1}}\). The partition consists of \(p^d\) cells with equal product probability \(p^{-d}\). The shift-and-apply rule proves exactly that \(F(Q_a)=Q_{R(a)}\) modulo null sets. One has \(R^d(a)=a+(1,\ldots,1)\), so \(R^{dp}=\operatorname{id}\).

**2. Exhaustion of ergodic components.** The identity
\[
F^{dp}=(T_\beta^p)\times\cdots\times(T_\beta^p)
\]
holds coordinatewise, and its restriction to each \(Q_a\) preserves the conditional product probability. Exactness of the \(d\) factors implies exactness of their finite product: for product functions, the transfer operators tensorize and converge to the product of the integrals in \(L^1\); finite linear combinations of such functions are dense in product \(L^1\), and transfer operators are contractions. Thus \(F^{dp}\) is exact on every \(Q_a\). For an \(R\)-cycle \(\mathcal O\) of length \(\ell\mid dp\), \(F^\ell\) is itself exact on any one \(Q_a\) in the orbit, since a positive integer power of \(F^\ell\) equals \(F^{dp}\). Hence \(\bigcup_{a\in\mathcal O}Q_a\) is a single \(F\)-ergodic component with \(\ell\) exact phase densities, and distinct orbits cannot communicate. This proves both existence and completeness, not merely the existence of a finite invariant partition. On each phase cell, the normalized conditional measure is pushed exactly to the normalized conditional measure on the next cell; the phase period really is \(\ell\). Density convergence along each phase class follows from exactness.

**3. Fixed point calculation.** Let \(k=qd+r\), with \(0\le r<d\), and let \(g=\gcd(d,r)=\gcd(d,k)\). A power of the affine permutation is
\[
(R^k a)_j=a_{(j+r)\bmod d}+q+\left\lfloor\frac{j+r}{d}\right\rfloor\pmod p,
\]
for \(0\le j<d\). The index shift \(j\mapsto j+r\) has \(g\) cycles, each of length \(d/g\). Summing the increments around any such cycle gives \(q(d/g)+r/g=k/g\). A solution to \(R^k a=a\) exists precisely when this increment is divisible by \(p\). When it is, one initial label may be chosen independently on each of the \(g\) cycles, providing \(p^g\) fixed points. At \(k=0\), use \(g=d\) and all labels are fixed. This proves \(H_{d,p}(k)\) including its boundary cases.

**4. Entire period histogram.** Burnside's orbit-counting lemma applied to the cyclic group generated by \(R\), of order \(dp\), proves the displayed \(C_{d,p}\). If \(E(\ell)\) counts cells with minimal orbit length \(\ell\), then \(H_{d,p}(k)=\sum_{\ell\mid k}E(\ell)\). Möbius inversion gives \(E(\ell)=\sum_{m\mid\ell}\mu_{\mathrm{Mob}}(\ell/m)H_{d,p}(m)\). Each \(\ell\)-cycle comprises \(\ell\) cells, so \(N_{d,p}(\ell)=E(\ell)/\ell\).

**5. Two-coordinate rigidity and examples.** When \(d=2\) and \(p\) is even, no \(0<k<2p\) satisfies the divisibility criterion. For odd \(k\), \(\gcd(2,k)=1\) and \(p\mid k\) would force \(k\) even; for even \(k\), \(\gcd(2,k)=2\) and \(p\mid k/2\) requires \(k\ge2p\). Thus every orbit has length \(2p\) and there are \(p^2/(2p)=p/2\) such cycles. For \(d=3,p=4\), only \(H(4)=4\) is nonzero among proper positive divisors of 12; \(H(12)=64\). Therefore \(N(4)=1\) and \(N(12)=5\).

For the concrete slope \(\beta=11/10\), conjugating the original tent map by \(x=(\beta+1)u\) gives \(u\mapsto1-\beta|u|\). The exact critical orbit \(r_{j+1}=1-\beta|r_j|\), \(r_0=0\), yields the four disjoint intervals
\[
I_0=[-1/10,-7459/100000],\quad
I_2=[89/100,917951/1000000],
\]
\[
I_1=[-97461/10000000,21/1000],\quad
I_3=[9769/10000,1].
\]
Their exact images follow \(I_0\to I_2\to I_1\to I_3\to I_0\), confirming the four-band phase geometry independently of an image. The general orbit count then gives two cycles, both of length eight.

## Verification

The standalone pure-Python program `verify_cycles.py` and its recorded stdout `verification_output.txt` are included. It exhaustively enumerates all states of the finite phase permutation in 18 separate \((d,p)\) cases, checks \(230\) distinct predicted fixed-point counts against enumerated powers, independently recovers every cycle histogram, verifies Burnside and divisor-wise Möbius inversion, and checks the four rational invariant intervals for \(\beta=11/10\) using exact fractions. It requires only Python 3's standard library and is run with `python3 verify_cycles.py`.

The finite checks verify the phase arithmetic and the rational example; they do not certify the one-dimensional all-slope theorem, the product exactness theorem, or the infinite \(d\) quantifier. Those are established by the cited one-dimensional theorem and the proof above.

## Relationship to prior work

Nakamura and Mackey introduced the two-dimensional delayed map, observed numerical statistical-period phenomena for nonzero coupling, and explicitly identified its generalized tent component and its known one-dimensional period windows. Their Section 4 notes higher-order delay systems, and Figure 1(a) displays 16 visible regions at zero coupling for slope \(11/10\). The earlier one-dimensional spectral and band literature already proves the \(2^n\)-band law, so the present work does not claim it. The present result instead distinguishes **how many product bands exist** from **how they organize into exact ergodic density cycles**, and gives an all-dimension formula for every exact cycle length at zero coupling.

Losson and Mackey studied two **synchronously and diffusively coupled** tent maps, including the zero-coupling product, and observed in-phase/out-of-phase density cycles. That supplies a related precedent for product components, but their two-variable update \((S(x),S(y))\) at zero coupling is not the delayed update \((y,S(x))\); it does not imply the affine-carry permutation and its all-delay period histogram without a new comparison argument. Burnside's lemma, Möbius inversion, and product exactness are classical tools, not novel mathematical techniques claimed here.

## Limitations

The scope is exactly zero coupling. Nonzero coupling can destroy the product measure, the phase rectangles, or their arithmetic cycle structure, and no perturbative persistence is claimed. At exceptional endpoints, measure-zero contacts of band boundaries do not constitute extra ergodic components. Ergodic decomposition is relative to the natural product absolutely continuous invariant probability, rather than a classification of every invariant probability or of escaping real initial conditions. The historical originality claim concerns the application of the complete phase-period census to the delayed family, not the classical one-dimensional band law or classical orbit-counting identities. Although the directly inspected primary and closely related works do not give the displayed all-delay classification, an earlier unindexed equivalent calculation is possible and independent priority verification remains appropriate.

## References

1. F. Nakamura and M. C. Mackey, *Asymptotic (statistical) periodicity in two-dimensional maps*, Discrete and Continuous Dynamical Systems B **27** (2022), 4285–4303, DOI 10.3934/dcdsb.2021227; publicly available preprint arXiv:2011.10689 (first submitted 2020-11-21), https://arxiv.org/abs/2011.10689 . The model, known one-dimensional band windows, and higher-delay motivation are in Section 4; Figure 1 shows the zero-coupling visible geometry.
2. N. Provatas and M. C. Mackey, *Asymptotic periodicity and banded chaos*, Physica D **53** (1991), 295–318, DOI 10.1016/0167-2789(91)90067-J; lawful author-hosted text: https://www.mcgill.ca/mathematical-physiology-lab/files/mathematical-physiology-lab/1999jun_provatas_mcm_asymptotic_periodicity_banded_chaos.pdf . This and its cited earlier one-dimensional tent-map work supply the established band/exact-return theory.
3. J. Losson and M. C. Mackey, *Coupling induced statistical cycling in two diffusively coupled maps*, Physica D **75** (1994), 324–342, DOI 10.1016/0167-2789(94)90236-4; lawful author-hosted text: https://www.mcgill.ca/mathematical-physiology-lab/files/mathematical-physiology-lab/1994may_losson_mcm_coupling_induced_stat_cycling_two_diffusively_coupled_maps.pdf . This treats synchronous rather than delayed coupling.
