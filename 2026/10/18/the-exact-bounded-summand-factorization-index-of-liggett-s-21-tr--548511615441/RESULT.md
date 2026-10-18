# The exact bounded-summand factorization index of Liggett’s 21-trial example

## Finding

Let \(X\sim\operatorname{Bin}(21,1/2)\), and define \(Y=\lfloor 3X/5\rfloor\). For an integer \(j\ge1\), say that a probability law is \(P_j\) if it is a convolution of finitely many probability laws supported on \(\{0,\dots,j\}\). Equivalently, its probability-generating polynomial is a product of polynomials of degree at most \(j\) with nonnegative real coefficients.

**The exact index is \(\min\{j:Y\text{ is }P_j\}=5\).** More specifically, the generating polynomial admits a product of one strictly positive quadratic and two strictly positive quintics, and cannot be expressed as a product of nonnegative-coefficient polynomials of degrees at most four.

This determines the minimal possible maximum support value in an independent-summand representation of the canonical counterexample studied by Liggett. His published calculation established the failure of \(P_4\) and an example in \(P_6\), leaving the intermediate property \(P_5\) undecided.

## Assumptions and scope

All statements concern the single, explicitly specified law \(Y=\lfloor 3X/5\rfloor\) for a fair 21-trial binomial parent. No conclusion is asserted for other trial counts, success parameters, or arbitrary strongly Rayleigh parents. Independence refers to summands in a representation in distribution, not the original Bernoulli trials.

Put \(F(t)=2^{21}\mathbb E[t^Y]\). The exact coefficient list in ascending powers is

\[
(22,1540,5985,74613,319770,293930,705432,497420,116280,74613,7315,210,22).
\]

Indeed, \([t^r]F(t)=\sum_{0\le h\le21:\,\lfloor3h/5\rfloor=r}\binom{21}{h}\), and \(F(1)=2^{21}\).

## Proof

**Step 1: isolate every root.** The four real root centers (largest absolute value first) and four upper-half-plane root centers (in ascending real part) are, respectively,

\[
\begin{aligned}
(w_1,w_2,w_3,w_4)&\approx(-9.237621391,-1.376162279,-0.258889384,-0.015007664),\\
(z_1,z_2,z_3,z_4)&\approx(0.010417789+0.144062467i,\\
&\qquad 0.059525176+0.675632118i,\\
&\qquad 0.229170259+2.541421787i,\\
&\qquad 0.371999864+17.995777456i).
\end{aligned}
\]

Treat each displayed decimal as an *exact rational center*, not as a verified approximation. Let \(r=10^{-5}\). The standalone checker verifies for each of these eight centers \(c\) the strict rational inequality

\[
\|F(c)\|_1+\sum_{k=2}^{12}\left\|\frac{F^{(k)}(c)}{k!}\right\|_1 r^k
<r\max\bigl( |\operatorname{Re}F'(c)|,|\operatorname{Im}F'(c)|\bigr),
\]

where \(\|a+ib\|_1=|a|+|b|\). Rouché's theorem therefore guarantees exactly one root of \(F\), counted with multiplicity, in each disk \(|t-c|<r\). For each nonreal center the complex conjugate disk likewise contains one root, by real coefficients. All twelve disks are pairwise disjoint. As \(\deg F=12\), these are all roots, each simple; the four real disks contain real roots.

**Step 2: construct positive factors.** With these roots, form the three real monic polynomials

\[
\begin{aligned}
A(t)&=(t-w_1)(t-w_4),\\
B(t)&=(t-w_3)\prod_{k=1}^{2}(t-z_k)(t-\overline z_k),\\
C(t)&=(t-w_2)\prod_{k=3}^{4}(t-z_k)(t-\overline z_k).
\end{aligned}
\]

They have degrees \(2,5,5\), and \(F(t)=22A(t)B(t)C(t)\). Outward exact-rational interval arithmetic on the above root disks verifies that *every coefficient* of each monic factor is positive. The smallest certified coefficient lower bounds are, respectively, greater than \(0.1385\), \(0.00248\), and \(0.1737\). Normalizing each factor at \(t=1\) produces probability-generating functions for independent summands with respective supports contained in \(\{0,1,2\}\), \(\{0,\dots,5\}\), and \(\{0,\dots,5\}\); their product is \(\mathbb E[t^Y]\). Thus \(Y\) is \(P_5\).

**Step 3: rule out all smaller degrees.** Every real polynomial divisor of \(F\) is, up to a scalar, obtained by choosing any subset of its four real linear factors and four conjugate-pair quadratic factors. The checker enumerates all \(2^8-1\) nonempty subsets. For each subset of total degree at most four, exact-rational coefficient intervals are computed using the root disks. If some coefficient interval has strictly negative upper endpoint, that subset cannot yield a nonnegative-coefficient polynomial. All other subsets, *including every inconclusive interval*, are conservatively marked as possible. There are 41 such optimistic subsets. An exhaustive bitmask-cover dynamic program establishes that no partition of the eight irreducible real factors into these possible subsets exists. Therefore no representation using only degree-at-most-four nonnegative factors is possible. This excludes \(P_4\), and hence excludes all \(P_j\) for \(j\le4\). Combined with Step 2, the minimum is exactly five.

## Verification

The accompanying standalone `p5_checker.py` uses only the Python standard library. It independently constructs the integer coefficients from binomial counts, certifies the twelve root disks by exact-rational Taylor estimates and Rouché's inequality, checks the positive quadratic/quintic grouping, and checks all degree-four factor partitions with conservative interval bounds. Run `python p5_checker.py`. No floating-point root approximations are trusted in the proof: all root centers, disk bounds, and coefficient comparisons are rational.

## Relationship to prior work

Liggett's 2021 article, *Approximating multiples of strong Rayleigh random variables*, Section 3, explicitly uses \(X\sim\operatorname{Bin}(21,1/2)\) and \(\lfloor3X/5\rfloor\) as a failure of property \(P_3\). He also states it is not \(P_4\) and is \(P_6\). The present classification supplies the missing constructive \(P_5\) bound, with a separate exact exclusion certificate for \(P_4\).

Tang and Tang's *The Poisson Binomial Distribution—Old & New* (arXiv 2019; Statistical Science 2023), Section 4, states a general conjecture about bounding independent summands for rounded rational multiples; it does not establish the exact five-versus-six index in this case. The established degree-two theorem for \(\lfloor2X/3\rfloor\) is not applicable to \(\lfloor3X/5\rfloor\). The novelty claim is **only** the exact index five for this specific 21-trial law, not the already published fact that this example disproves degree-three factorization.

## Limitations

The result is an exact, parameter-specific decomposition threshold, not a classification of all rational roundings. The decomposition factors are defined through isolated algebraic roots and verified by an exact rational certificate; simple rational-coefficient factorization is neither asserted nor needed. Literature searches cannot exclude all unindexed earlier work. Independent external mathematical validation has not been performed.

## References

1. T. M. Liggett, *Approximating multiples of strong Rayleigh random variables*, Celebratio Mathematica (2021), https://celebratio.org/Liggett_T/article/858/ (Sections 1 and 3, especially the 21-trial example).
2. W. Tang and F. Tang, *The Poisson Binomial Distribution—Old & New*, arXiv:1908.10024, first submitted August 27, 2019, https://arxiv.org/abs/1908.10024; *Statistical Science* **38** (2023), 108–119, https://www.columbia.edu/~wt2319/PB.pdf (Theorems 4.3–4.4 and Conjecture 4.5).
