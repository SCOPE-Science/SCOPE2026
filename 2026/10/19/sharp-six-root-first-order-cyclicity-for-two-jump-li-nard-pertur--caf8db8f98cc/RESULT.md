# Sharp six-root first-order cyclicity for two-jump Liénard perturbations

## Finding

Consider a real-valued function \(F\) that is affine on each of three intervals separated by precisely two nonzero jump locations \(\xi_1<\xi_2\), with no additional continuous corner. Neither switching location equals zero. For the perturbation of the linear center
\[
\dot x=y-\varepsilon F(x),\qquad \dot y=-x,
\]
define the first-order radial displacement coefficient
\[
D_F(r)=\frac{2}{r^2}\int_0^r\frac{x\,[F(x)-F(-x)]}{\sqrt{r^2-x^2}}\,dx,\qquad r>0.
\]
The first-order return displacement at any regular radius is \(-\varepsilon rD_F(r)+O(\varepsilon^2)\). **The number of positive simple zeros of \(D_F\), excluding the radii \(|\xi_1|,|\xi_2|\), is at most six, and six is attainable.** Hence the exact maximal first-order *simple-zero cyclicity* within this class is six. This concerns limit cycles persisting from fixed regular circles as \(\varepsilon\to0\), and is not a bound on all cycles for fixed nonzero perturbation or on grazing/sliding cycles.

When \(0<a<b\) are the two distinct absolute switching radii, no simple zero lies in \((0,a)\), at most two lie in \((a,b)\), and at most four in \((b,\infty)\). In any configuration attaining six, the distribution is forced to be exactly two and four, respectively. If the absolute radii coincide, at most two simple zeros are possible.

## Assumptions and scope

The two one-sided values of \(F\) genuinely differ at each switching location; the three restrictions of \(F\) to its open affine pieces are otherwise arbitrary, including arbitrary slopes and intercepts. The switching locations must be different and nonzero, but may be positive, negative, or of opposite signs. The value of \(F\) *on* a switching line does not affect \(D_F\). This statement concerns classical transversal first-order averaging at positive radii different from every absolute switching location. Roots at these excluded radii and higher-order bifurcations from multiple or flat zeros are not asserted to be counted.

The exact two-jump bound applies to the function \(D_F\). A simple zero \(r_0\) produces a hyperbolic crossing cycle of the perturbed system for all sufficiently small \(\varepsilon>0\), with return multiplier \(1-\varepsilon r_0 D_F'(r_0)+O(\varepsilon^2)\). This local statement uses transversality to switching lines at the limiting circle and the implicit function theorem. No claim is made about a common perturbation size valid uniformly over all \(F\).

## Proof

**Step 1: radial reduction.** Put \(h(x)=F(x)-F(-x)\) for \(x>0\). Because zero is not a switching location, \(h(x)=2u x\) for all sufficiently small \(x>0\), where \(u\) is the slope of \(F\) on the piece containing zero. Each jump at \(\xi_j>0\) contributes \((k_jx+c_j)\mathbf1_{x>|\xi_j|}\) to \(h\). A jump at \(\xi_j<0\) contributes \((k_jx+c_j)\mathbf1_{x>\xi_j}-(-k_jx+c_j)\mathbf1_{-x>\xi_j}\); this is \(2k_jx+(-k_jx+c_j)\mathbf1_{x>|\xi_j|}\). Thus, after absorbing baseline slopes, \(h\) is always of the form
\[
h(x)=2ux+\sum_{j=1}^{q}(k_jx+c_j)\mathbf1_{x>a_j},\qquad 1\le q\le2,
\]
where \(a_j>0\) are distinct absolute switching radii in increasing order. For \(q=2\), write \(a_1=a\), \(a_2=b\). If the two absolute radii coincide, their contributions combine and \(q\le1\). The step coefficient at a distinct radius is nonzero because the original jump is nonzero.

**Step 2: exact Abel integral.** Direct integration gives
\[
D_F(r)=\pi u+\sum_{a_j<r}\left[k_j\left(\arccos\frac{a_j}{r}+\frac{a_j}{r}\sqrt{1-\frac{a_j^2}{r^2}}\right)+\frac{2c_j}{r}\sqrt{1-\frac{a_j^2}{r^2}}\right].
\]
Each displayed contribution vanishes continuously at its threshold. On every interval not meeting a threshold,
\[
D_F'(r)=-\frac{2}{r^3}\sum_{a_j<r}\frac{p_j(r^2)}{\sqrt{r^2-a_j^2}},\qquad
p_j(s)=c_j(s-2a_j^2)-k_ja_j^3.
\]
These identities may be checked by differentiating the exact integral; the enclosed checker independently verifies the derivative identity and quadratures.

**Step 3: the sharp upper bound.** Suppose \(q=2\) and \(a<b\). On \((0,a)\), \(D_F\) is constant and has no simple zeros (even if the constant is zero). On \((a,b)\), its derivative has at most one root because \(p_1\) is affine in \(s=r^2\). By Rolle's theorem, \(D_F\) has at most two distinct zeros on this interval. For \(r>b\), every critical point gives a positive root \(s>b^2\) of
\[
\mathcal P(s)=p_1(s)^2(s-b^2)-p_2(s)^2(s-a^2).
\]
This polynomial has degree at most three. It cannot vanish identically when the two radial jumps are genuine and \(a\ne b\): at \(s=a^2\), the multiplicity on the first side of the polynomial identity would be even while the multiplicity on the second side would be odd, a contradiction (both \(p_j\) are nonzero polynomials). Thus there are at most three distinct critical points beyond \(b\), and Rolle gives at most four distinct zeros there. The total number of positive simple zeros away from the switching radii is at most \(2+4=6\). For \(q=1\), the same affine-numerator argument gives at most two simple zeros beyond the lone threshold and none below it. The conclusion also applies when the zero-order constant happens to vanish, since a flat interval has no *simple* zeros.

**Step 4: attaining six with exactly two jumps.** A concrete realization is
\[
h(x)=\begin{cases}
2x,&0<x\le1,\\
\frac{10}{109}x-\frac{81}{218}+\delta,&1<x\le5,\\
\alpha x+\beta,&x>5,
\end{cases}
\]
where
\[
\alpha=\frac8{109\pi\,50^5},\qquad
\beta=-\frac{239}{3270\,50^4},\qquad
\delta=\frac{115}{19620000}+\frac{125\alpha}{36}+\frac{25\beta}{24}.
\]
Set \(F(x)=x\) when \(x\le0\), and \(F(x)=h(x)-x\) when \(x>0\). Both breaks at one and five are nonzero jumps, and no fold points are introduced. The exact Abel formula has strictly alternating signs at the six disjoint ordered pairs of radii
\[
(19/10,21/10),\ (9/2,24/5),\ (14,16),\ (46,48),\ (100,102),\ (149,151).
\]
The first, third and fifth pairs give positive-to-negative signs; the others give negative-to-positive signs. The accompanying `verify.py` certifies each of these twelve signs with enclosing interval evaluations of \(\pi\), square roots and inverse trigonometric functions, using exact rational input parameters. Intermediate-value continuity gives two distinct zeros in \((1,5)\) and four in \((5,\infty)\). The six-root upper bound leaves exactly these six zeros in the two open regions. Moreover, one critical point is required between the two inner zeros and three between the four outer zeros; these already exhaust the allowed critical points. Any of the six zeros being multiple would create an additional critical point. All six are therefore simple. Independently, the full Section 2 construction and Theorem 1.1 of Chen–Jin–Li–Lu establish six simple roots for the two-jump case, consistent with this explicit witness.

**Step 5: correspondence with cycles.** The radial return map on compact regular amplitude intervals has the expansion \(P_\varepsilon(r)=r-\varepsilon rD_F(r)+O(\varepsilon^2)\), including the first derivative in \(r\). The implicit function theorem provides one hyperbolic crossing limit cycle near each of the six simple roots of the constructed example, for all sufficiently small positive \(\varepsilon\). Conversely the upper bound counts all cycles that arise by this *first-order simple-zero mechanism* from regular finite radii; it does not exclude cycles created by mechanisms outside this scope.

## Verification

Run `python verify.py` with Python, SymPy and mpmath available. The script verifies the exact Abel derivative identity, the degree-three eliminant, radial reduction for mixed-sign jump positions, nine high-precision independent quadratures, and six pairwise disjoint sign-changing brackets using interval arithmetic. In the checked execution, all tests passed. Interval input parameters are rational expressions and \(\pi\), not fitted numerical coefficients. The upper-bound proof is analytical and requires no finite scan of radii. The attaining example is also independently supported by the primary paper's proved construction. Exact radii of its six roots are not claimed.

## Relationship to prior work

Chen, Jin, Li and Lu (arXiv:2610.11916v1, 8 October 2026) derive this first-order Abel integral and prove the lower bound of six simple roots for two positive jumps as a case of their general \(4m-2\) construction. Their upper bound controls all crossing, grazing, sliding and composite cycles but is extremely large. **The new statement is the matching six-root upper bound for first-order regular-circle bifurcations with two nonzero jumps of either sign**, together with the forced two/four radial distribution and an elementary cubic critical-point certificate. The lower bound itself, the Abel integral, and the general first-order return-map expansion are not claimed as new.

Chen, Li, Zhang and Zhang (arXiv:2608.19542) give the earlier weaker two-jump lower bound of four and investigate infinity. Tonnelier (2005) describes constructions in the piecewise-linear Liénard class, but its accessible abstract does not provide a matching first-order six-root upper bound. The 2026 one-switching-line classification gives a global two-cycle bound for one discontinuity, which does not imply the result for two. Other piecewise Hamiltonian switching geometries and higher-order Melnikov functions differ in their integrands and hypotheses.

## Limitations

This is **not** a solution to the unrestricted maximum-cycle problem for two discontinuities. It does not count singular radii coinciding with jump moduli, sliding/grazing cycles, multiple-root higher-order bifurcations, cycles escaping to infinity as \(\varepsilon\to0\), or all limit cycles at a fixed finite perturbation. One-sided switching at the origin is excluded. The interval checker supplies a reproducible finite sign certificate, not an infinite-domain numerical proof; the latter is given by the Rolle/cubic argument. A matching result hidden in inaccessible historical literature remains a priority risk. No independent audit has been performed.

## References

1. H. Chen, J. Jin, S. Li and Y. Lu, *Bounds on the maximum number of limit cycles of piecewise linear Liénard systems II. The discontinuous case*, arXiv:2610.11916v1 (2026-10-08), https://arxiv.org/html/2610.11916v1. In particular Section 2, Lemma 2.1 and Theorem 1.1.
2. H. Chen, Z. Li, R. Zhang and X. Zhang, *The number of limit cycles of piecewise linear Liénard systems*, arXiv:2608.19542v1 (2026-08-20), https://arxiv.org/abs/2608.19542.
3. A. Tonnelier, *On the number of limit cycles in piecewise-linear Liénard systems*, International Journal of Bifurcation and Chaos 15 (2005), 1417–1422, https://doi.org/10.1142/S0218127405012624.
4. H. Chen, D. Dai, Z. Feng and Z. Zheng, *Maximum number of limit cycles of the discontinuous piecewise linear Liénard system with one switching line*, Journal of the London Mathematical Society 113 (2026), e70612, https://doi.org/10.1112/jlms.70612.
