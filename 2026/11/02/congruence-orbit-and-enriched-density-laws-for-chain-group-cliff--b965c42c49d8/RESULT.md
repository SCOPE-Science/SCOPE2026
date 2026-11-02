# Congruence-orbit and enriched-density laws for chain–group Clifford monoids

## Finding

Let \(G\) be a finite group, let \(m\geq 1\), and put \(C_m=\{0,\ldots,m-1\}\) with multiplication \(i\wedge j=\min(i,j)\). In the Clifford monoid \(S=C_m\times G\), write \(\mu(i,g)=(m-1,g)\) for the maximum-element operation of its minimum group-congruence class. An *enriched congruence* means a multiplication congruence also preserving \(\mu\), called an \(F\)-congruence in the literature.

**Complete normal form.** Every ordinary congruence is determined uniquely by an interval partition \(I_1<\cdots<I_b\) of \(C_m\) and a decreasing weak chain of normal subgroups \(N_1\supseteq\cdots\supseteq N_b\trianglelefteq G\). Its classes satisfy
\[
(i,g)\mathrel{\rho}(j,h)\quad\Longleftrightarrow\quad
\text{for some }a:\ i,j\in I_a\text{ and }gh^{-1}\in N_a.
\]
It preserves \(\mu\) precisely when all the \(N_a\) are equal. If \(\mathcal N(G)\) is the set of normal subgroups and \(F_b(G)\) is the number of weak chains of length \(b\) in it, then
\[
|\operatorname{Con}(S)|=\sum_{b=1}^{m}\binom{m-1}{b-1}F_b(G),\qquad
|\operatorname{FCon}(S)|=2^{m-1}|\mathcal N(G)|.
\]

**Orbit refinement.** If \(G=(C_p)^d\) for a prime \(p\) and \(d\geq1\), the automorphism group of \(S\) is \(\operatorname{GL}_d(\mathbb F_p)\). The numbers of automorphism orbits of ordinary and enriched congruences, respectively, are
\[
\mathcal O_{m,d}=\sum_{b=1}^{m}\binom{m-1}{b-1}\binom{d+b}{b},\qquad
\mathcal O^F_{m,d}=2^{m-1}(d+1).
\]
For fixed \(m\geq2\), the fraction of enriched orbits among all congruence orbits is
\[
\frac{\mathcal O^F_{m,d}}{\mathcal O_{m,d}}
\sim 2^{m-1}m!\,d^{1-m}\quad(d\to\infty).
\]

**Sharp density.** Write \(\Phi_p=\prod_{j\geq1}(1-p^{-j})\) and, for integers \(k\geq2\), \(0\leq s<k\), define the convergent theta sum
\[
\Theta_{k,s}(p)=\sum_{\substack{z_1,\ldots,z_k\in\mathbb Z\\\sum_i z_i=s}}
 p^{-\frac12(\sum_i z_i^2-s^2/k)}.
\]
For every fixed prime \(p\) and fixed \(m\geq2\), as \(d\to\infty\),
\[
\boxed{\frac{|\operatorname{FCon}(C_m\times (C_p)^d)|}{|\operatorname{Con}(C_m\times (C_p)^d)|}
\sim 2^{m-1}\Phi_p^{m-1}
\frac{\Theta_{2,d\bmod2}(p)}{\Theta_{m+1,d\bmod(m+1)}(p)}
\,p^{-\frac{m-1}{4(m+1)}d^2}.}
\]
The displayed positive prefactor is periodic in \(d\). Thus the proportion of enriched congruences decreases at a quadratic-exponential rate in rank, whereas the corresponding automorphism-orbit proportion decreases polynomially.

## Assumptions and scope

Here a congruence is an equivalence relation preserved by multiplication on both sides, not an arbitrary reflexive relation. The ordinary and enriched counts are counts of distinct relations on the labeled monoid; the orbit counts identify relations only under automorphisms of that monoid. A normal-subgroup chain is weak: equal adjacent terms are allowed. All formulas for finite groups are exact, including the trivial group and \(m=1\). The orbit and asymptotic statements require elementary abelian groups; asymptotic limits hold for fixed \(p\) and \(m\) with \(d\) increasing. Neither limit is uniform when \(m\) or \(p\) also increases.

## Proof

**1. The enriched operation.** The projection \((i,g)\mapsto g\) is a surjective group quotient of \(S\). For each \(g\), every \((i,g)\) lies below \((m-1,g)\) in the natural order, and two elements having distinct group coordinates cannot belong to the same minimum group-congruence class. Hence \(S\) is \(F\)-inverse and the maximum-element map is exactly \(\mu(i,g)=(m-1,g)\).

**2. Congruence normal form: necessity.** Let \(\rho\) be a multiplication congruence. The idempotents are exactly \((i,1_G)\), so their restrictions form a semilattice congruence on \(C_m\). If \(i<k<j\) and \(i\) is equivalent to \(j\), multiplying both idempotents by \((k,1_G)\) shows that \(i\) is equivalent to \(k\); thus the equivalence classes are convex intervals \(I_1<\cdots<I_b\). For each level \(i\), the restriction of \(\rho\) to \(\{i\}\times G\) is a group congruence and therefore has the form \(gh^{-1}\in N_i\) for a unique normal subgroup \(N_i\trianglelefteq G\).

If \(i\leq j\), multiplying \((j,g)\mathrel{\rho}(j,h)\) by \((i,1_G)\) yields \((i,g)\mathrel{\rho}(i,h)\); hence \(N_j\subseteq N_i\). If \(i,j\) lie in the same idempotent interval, then \((i,1_G)\mathrel{\rho}(j,1_G)\). Multiplying by \((m-1,g)\) gives \((i,g)\mathrel{\rho}(j,g)\) for every \(g\), forcing \(N_i=N_j\). Finally, if \((i,g)\mathrel{\rho}(j,h)\), raising the relation to any common positive multiple of the orders of \(g\) and \(h\) yields \((i,1_G)\mathrel{\rho}(j,1_G)\); thus cross-level relations occur only inside one idempotent interval. Together these properties force the displayed normal form and its uniqueness.

**3. Sufficiency.** Given intervals and normal subgroups as stated, the relation is visibly an equivalence. If \((i,g)\) is related to \((i',g')\) through block \(a\), then left or right multiplication by \((j,h)\) moves both level coordinates into block \(\min(a,c)\), where \(c\) is the block of \(j\). Normality and \(N_a\subseteq N_{\min(a,c)}\) ensure that the resulting group-coordinate difference remains in the required normal subgroup. Thus the relation is a congruence. Interval partitions of a chain into \(b\) blocks number \(\binom{m-1}{b-1}\), giving the total formula.

**4. Preservation of maximum.** If \(gh^{-1}\in N_a\), preserving \(\mu\) requires \((m-1,g)\mathrel{\rho}(m-1,h)\), namely \(gh^{-1}\in N_b\). Hence \(N_a\subseteq N_b\) for all \(a\). With the already-proved decreasing chain, this is equivalent to \(N_1=\cdots=N_b\). The converse is immediate. There are \(2^{m-1}\) interval partitions, proving the enriched count.

**5. Automorphism orbits.** Every automorphism fixes the chain of idempotents pointwise: a finite total order has no nontrivial order automorphism. Its restrictions to the group at each level give automorphisms \(\varphi_i\in\operatorname{Aut}(G)\). The identity \((i,g)=(i,1_G)(j,g)\) for \(i\leq j\) forces \(\varphi_i=\varphi_j\); conversely, every diagonal group automorphism extends to \(S\). Hence \(\operatorname{Aut}(S)=\operatorname{Aut}(G)\). For \(G=(C_p)^d\), subgroups are vector subspaces and two weak flags lie in the same \(\operatorname{GL}_d(\mathbb F_p)\)-orbit exactly when their dimension vectors agree. A weak chain of \(b\) subspaces is equivalent to a composition of \(d\) into \(b+1\) nonnegative dimension increments, giving \(\binom{d+b}{b}\) orbits. The enriched case has one subspace and \(d+1\) possible dimensions. Since the term \(b=m\) has degree \(m\) in \(d\), its leading term is \(d^m/m!\), proving the orbit-density asymptotic.

**6. Flag enumeration and sharp density.** In the elementary abelian case, \(F_b(G)\) is the number of weak subspace chains of length \(b\). Writing their successive dimension increments as \(r_0,\ldots,r_b\geq0\), with total \(d\), gives the known Gaussian-multinomial expression
\[
F_b((C_p)^d)=\sum_{r_0+\cdots+r_b=d}
\begin{bmatrix}d\\r_0,\ldots,r_b\end{bmatrix}_p,
\qquad
\begin{bmatrix}d\\r_0,\ldots,r_b\end{bmatrix}_p
=p^{\frac12(d^2-\sum r_i^2)}
\frac{\prod_{j=1}^{d}(1-p^{-j})}{\prod_{i=0}^{b}\prod_{j=1}^{r_i}(1-p^{-j})}.
\]
Let \(k=b+1\), and write \(d=kt+s\) with \(0\leq s<k\). Every summand has \(r_i=t+z_i\), \(\sum_i z_i=s\), so its exponent of \(p\) equals
\[
\frac{k-1}{2k}d^2-
\frac12\left(\sum_i z_i^2-\frac{s^2}{k}\right).
\]
For each fixed integer offset vector \((z_i)\), the Euler-product factor tends to \(\Phi_p^{1-k}\). Its absolute value is bounded uniformly by \(\Phi_p^{-k}\). The weighted sum of offsets is dominated by a convergent discrete Gaussian, so dominated convergence gives
\[
F_b((C_p)^d)\sim \Phi_p^{-b}\Theta_{b+1,d\bmod(b+1)}(p)
\,p^{\frac{b}{2(b+1)}d^2}.
\]
For fixed \(m\geq2\), \(b/(b+1)\) increases strictly with \(b\), so the \(b=m\) term dominates the ordinary-congruence sum. In the enriched numerator, \(F_1\) is the total number of subspaces. Dividing its asymptotic by that for \(F_m\) produces the boxed density law. The theta constants are strictly positive, so the asymptotic equivalence is well-defined.

## Verification

The self-contained file `verify.py` enumerates all set partitions of the underlying finite monoid, checks left and right compatibility directly, checks preservation of \(\mu\), and compares these totals with independent subspace-chain enumeration. For the cases with underlying size at most nine it also enumerates group automorphisms and checks the congruence-orbit formulas. The exhaustive cases \((p,d,m)=(2,1,2),(2,1,3),(2,2,2),(3,1,2),(3,1,3),(5,1,2)\) all agree. For example, at \((2,2,2)\) the four totals (ordinary, enriched, ordinary orbits, enriched orbits) are \((17,10,9,6)\). Separate exact-arithmetic flag calculations compare finite densities with the theta-prefactor prediction for three larger ranks. Those comparisons demonstrate convergence but are not used as proof of the infinite asymptotic. Run `python verify.py`; the recorded result is `VERIFY_OK`.

## Relationship to prior work

Ajda Lemut Furlani's 2026 work introduced the enriched-congruence problem in the maximum-element signature of \(F\)-inverse monoids. Its Example 3.3 considers a two-level semilattice times \(C_2\), and its principal results give general kernel/congruence-pair criteria. Those criteria do not themselves supply the exact normal form, orbit enumeration, or prevalence laws for the present chain-group family.

Classical Clifford-semigroup congruence theory already provides a broad framework for normal-subgroup and semilattice data. The unrestricted flag counts are generalized Galois numbers: Bliem–Kousidis and Vinroot study their combinatorics; Kousidis's 2011 preprint (published 2013) already gives theta-function limits of generalized Galois numbers. **Neither the subspace-flag enumeration nor its theta asymptotics in isolation is claimed as new.** The specific contribution is the precise identification of which congruences of this semigroup family preserve the additional maximum map, together with exact ordinary/enriched orbit counts and the contrast between their polynomial orbit-density and quadratic-exponential raw-density laws.

## Limitations

The structural result is a direct, specialized refinement of established congruence machinery; a sufficiently general earlier account of chain Clifford monoids could imply its normal form. The theta analysis is an elementary rederivation of a known general flag-asymptotic phenomenon, applied here to the enriched-congruence ratio. The checked literature did not reveal an explicit prior result for this combined statistic, but priority against every historical semigroup source is not guaranteed. No statement is made for non-chain semilattices, non-elementary abelian orbit laws, or simultaneous growth of the chain length and group rank. The computations are finite confirmation, not a substitute for the full proof.

## References

1. A. Lemut Furlani, *F-congruences on F-inverse monoids*, arXiv:2608.15114, first public version 2026-08-15, https://arxiv.org/abs/2608.15114 .
2. S. Kousidis, *Asymptotics of generalized Galois numbers via affine Kac-Moody algebras*, arXiv:1109.2546 (2011), Proc. Amer. Math. Soc. 141 (2013), 3313–3326, https://arxiv.org/pdf/1109.2546 .
3. T. Bliem and S. Kousidis, *The number of flags in finite vector spaces: Asymptotic normality and Mahonian statistics*, arXiv:1109.4624 (2011), https://arxiv.org/abs/1109.4624 .
4. C. Ryan Vinroot, *An Enumeration of Flags in Finite Vector Spaces*, Electronic Journal of Combinatorics 19(3) (2012), P5, https://doi.org/10.37236/2481 .
5. C. Spitznagel, *The lattice of congruences on a band of groups*, Glasgow Mathematical Journal 14 (1973), 187–197, https://doi.org/10.1017/S0017089500001956 .
