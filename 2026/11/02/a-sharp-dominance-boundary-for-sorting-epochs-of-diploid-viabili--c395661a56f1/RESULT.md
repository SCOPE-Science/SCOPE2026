# A sharp dominance boundary for sorting epochs of diploid viability selection

## Finding

Consider deterministic, one-locus, two-allele viability selection in an infinite, randomly mating diploid population. Each generation has genotype relative viabilities \(1+s\), \(1+hs\), and \(1\) for \(AA\), \(Aa\), and \(aa\), with an epoch-specific strength \(s>0\) and a common dominance coefficient \(h\geq0\). Let \(x\in(0,1)\) be the focal \(A\)-allele frequency before selection. Its one-generation update is

\[
F_s(x)=\frac{x[1+s(h+(1-h)x)]}{1+s[2hx+(1-2h)x^2]}.
\]

**Universal finite-horizon rearrangement.** For every integer \(m\geq2\), every finite multiset of positive strengths \(s_1,\ldots,s_m\), every initial \(x\in(0,1)\), and every fixed \(h\in[0,1]\), the terminal frequency \(F_{s_m}\circ\cdots\circ F_{s_1}(x)\) is maximized by applying strengths in nonincreasing order, and minimized by nondecreasing order. Every swap of two adjacent, unequally ordered strengths strictly changes the terminal frequency in the indicated direction. Thus the extremizing strength sequences are unique up to permutation of equal strengths.

**Sharp dominance boundary and exact two-epoch reversal.** If \(h>1\) and \(a>b>0\), put

\[
Q_{h,a,b}(x)=(1-h)(1-x)+hx\left[1+a+b+ab\bigl(h(1-x)+x\bigr)\right].
\]

This concave quadratic has exactly one root \(x_c\) in \((0,1)\), lying strictly below the common interior equilibrium \(x_*=h/(2h-1)\). For \(0<x<x_c\), the weaker-first order produces *more* \(A\)-alleles after two generations; for \(x_c<x<1\), the stronger-first order produces more, except that both orders agree at \(x=x_*\). They also agree at \(x=x_c\). Consequently \(h=1\) is the sharp upper boundary of the universal strongest-first rule among nonnegative dominance coefficients.

For \(h=2\), \(a=2\), and \(b=1\), the crossover is \(x_c=(17-\sqrt{273})/8\). At \(x=1/20\), stronger-first gives a strictly smaller terminal allele frequency; at \(x=1/4\) it gives a strictly larger one.

## Assumptions and scope

The population is infinite, diploid, randomly mating each generation, and at Hardy–Weinberg proportions immediately before genotype viability selection. Viability is strictly positive. There is no mutation, migration, drift, segregation distortion, or density-dependent fitness; each epoch lasts one discrete generation. The genotype fitness convention is \((w_{AA},w_{Aa},w_{aa})=(1+s,1+hs,1)\). A sequence lists its strengths in chronological application order; \(F_b(F_a(x))\) means strength \(a\) acts first. The universal ordering theorem assumes common \(0\leq h\leq1\); the boundary analysis assumes common \(h>1\) and exactly two unequal positive strengths. It concerns *finite-horizon deterministic allele frequency*, not fixation probabilities for finite populations.

## Proof

**1. Exact update and monotonicity.** The relative mean viability of Hardy–Weinberg genotypes is \(D_s(x)=1+s[2hx+(1-2h)x^2]>0\), while the surviving \(A\)-allele numerator is \(N_s(x)=x[1+s(h+(1-h)x)]\). Thus \(F_s=N_s/D_s\). For any fixed positive genotype viabilities \(w_0,w_1,w_2\), let \(K\sim\mathrm{Binomial}(2,x)\) represent the number of \(A\) copies before selection, and let \(\mathbb E_w\) mean expectation tilted by the positive viability \(w_K\). Then \(F_s(x)=\mathbb E_w[K]/2\), and direct differentiation of the binomial probabilities gives

\[
F_s'(x)=\frac{\operatorname{Var}_w(K)}{2x(1-x)}>0
\quad(0<x<1).
\]

Hence every viable epoch is strictly increasing in its incoming allele frequency, and its output remains in \((0,1)\).

**2. Exact adjacent-epoch commutator.** Define

\[
U_h(x)=h+(1-2h)x,\qquad
Z_{a,b}(x)=D_a(x)^2+b\bigl[2hN_a(x)D_a(x)+(1-2h)N_a(x)^2\bigr].
\]

Notice that \(Z_{a,b}(x)=D_a(x)^2D_b(F_a(x))>0\). Substitution of the rational formulas followed by a common-denominator expansion gives the exact identity

\[
F_b(F_a(x))-F_a(F_b(x))=
\frac{ab(a-b)x^2(1-x)^2U_h(x)^2 Q_{h,a,b}(x)}{Z_{a,b}(x)Z_{b,a}(x)}.
\tag{1}
\]

For \(0\leq h\leq1\) and \(0<x<1\), \(U_h(x)=h(1-x)+(1-h)x>0\). Moreover

\[
Q_{h,a,b}(x)=(1-h)(1-x)+hx\left[1+a+b+ab\bigl(h(1-x)+x\bigr)\right]>0.
\]

Therefore (1) has strictly the sign of \(a-b\) for distinct strengths. If a later strength is greater than its immediate predecessor, interchanging the two strengthens the terminal \(A\)-frequency. Any preceding epochs leave the state inside \((0,1)\); any following epochs preserve this strict ordering by Step 1. Repeated adjacent exchanges sort any strength list, proving both extrema and uniqueness up to equal strengths.

**3. Sharp overdominance crossover.** For \(h>1\), expand \(Q_{h,a,b}\) as

\[
Q_{h,a,b}(x)=(1-h)+\bigl[(2h-1)+h(a+b)+abh^2\bigr]x+abh(1-h)x^2.
\]

Its leading coefficient is negative, \(Q(0)=1-h<0\), and \(Q(1)=h(1+a+b+ab)>0\); hence exactly one zero \(x_c\) lies in \((0,1)\). The identity

\[
F_s(x)-x=\frac{sx(1-x)U_h(x)}{D_s(x)}
\]

shows that \(x_*=h/(2h-1)\) is fixed by *every* epoch. Direct evaluation gives \(Q(x_*)>0\), so \(x_c<x_*<1\). Formula (1) now shows the strict sign reversal at \(x_c\), with equality also at \(x_*\) because \(U_h(x_*)=0\). No universal strong-first order can hold over all initial frequencies when \(h>1\). This establishes sharpness.

## Verification

The accompanying `check_selection.py` uses exact symbolic rational functions to confirm identity (1), the composition denominators and the single-generation drift, then checks exact-rational sample grids and all \(4!\) orderings of a natural four-strength example. It passed 673 assertions using Python and SymPy. This finite testing is not offered as an infinite-domain proof; the algebraic identity, positivity argument, and adjacent-swap proof above establish the quantified claims.

For the concrete non-overdominant instance \((h,a,b,x)=(1/2,2,1,1/3)\), identity (1) gives \(F_b(F_a(x))-F_a(F_b(x))=1/440\). At \((h,a,b)=(2,2,1)\), \(Q(x)=-1+17x-4x^2\): at \(x=1/20\) the difference is \(-7907344/26731501383\), whereas at \(x=1/4\) it is \(100/47117\). All these are exact fractions.

## Relationship to prior work

The classical viability-selection genotype-fitness convention, the distinction between incomplete dominance and overdominance, and temporal environmental variation are established theory. Hedrick (1974, 1976) studies maintenance of genetic variation under temporally heterogeneous selection. Teshima and Przeworski (first publicly indexed 2005) and Ewing et al. (arXiv 2010) analyze directional selection and dominance in stochastic selective-sweep and fixation settings. Cvijović et al. (2015) studies mutation fate under fluctuating environments. Wittmann, Mousset and Hermisson (2023) analyzes periodic reversal of the favored allele and linked genetic diversity; its full model uses a related genotype-viability update but targets a different question.

The present exact finite-horizon permutation inequality concerns fixed lists of *positive strengths favoring the same allele*, with a common dominance coefficient, and identifies a sharp failure under overdominance. It does not follow from the cited fixation-time, diversity, or alternating-favored-allele conclusions as stated. Full historical priority over other possible rearrangement results remains unverified; relevant older Hedrick PDFs were not accessible in full during this investigation.

## Limitations

The result neither models drift nor estimates fixation probability, selective-sweep duration, linkage, mutation, or finite-sample uncertainty. It does not prescribe an optimal intervention policy when selection strengths may be changed adaptively or when dominance varies by epoch. For \(h>1\) the complete reversal classification concerns two epochs, not an arbitrary-length globally optimal schedule. The source comparisons establish best-knowledge noncoverage, not an independent proof of historical uniqueness.

## References

1. P. W. Hedrick (1974), *Genetic Variation in a Heterogeneous Environment. I. Temporal Heterogeneity and the Absolute Dominance Model*, *Genetics* 78, 757–770. https://doi.org/10.1093/genetics/78.2.757 (public date 1974-10-01).
2. P. W. Hedrick (1976), *Genetic Variation in a Heterogeneous Environment. II. Temporal Heterogeneity and Directional Selection*, *Genetics* 84, 145–157. https://doi.org/10.1093/genetics/84.1.145.
3. K. M. Teshima and M. Przeworski (2006), *Directional Positive Selection on an Allele of Arbitrary Dominance*, *Genetics* 172, 713–718. https://doi.org/10.1534/genetics.105.044065 (electronically published 2005-10-11).
4. G. Ewing, J. Hermisson, P. Pfaffelhuber and J. Rudolf (2010), *Selective sweeps for recessive alleles and for other modes of dominance*, arXiv:1005.5536, first posted 2010-05-30. https://arxiv.org/abs/1005.5536.
5. I. Cvijović, B. H. Good, E. R. Jerison and M. M. Desai (2015), *Fate of a mutation in a fluctuating environment*, *PNAS* 112, E5021–E5028. https://doi.org/10.1073/pnas.1505406112.
6. M. J. Wittmann, S. Mousset and J. Hermisson (2023), *Modeling the genetic footprint of fluctuating balancing selection: from the local to the genomic scale*, *Genetics* 223, iyad022. https://doi.org/10.1093/genetics/iyad022.
