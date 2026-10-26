# Finite-three-source peeling law and necessity of degree-three packets

## Finding

Consider three binary information symbols sampled through independent random linear equations, uniformly over supports of each chosen degree. Let the probabilities of degrees one, two, and three be \(p_1,p_2,p_3\), respectively. For any prescribed information symbol, the expected number \(E\) of sampled equations needed for recovery by **iterative peeling** admits a closed rational formula for the entire probability simplex (infinite when \(p_1=0\)). In particular, for \(a=p_1/3\), \(b=p_2/3\), and \(c=p_3\), whenever \(p_1>0\),

\[
E=\frac{2}{3a+3b+c}-\frac1{3a+2b+c}-\frac2{3a+2b}+\frac1{3a}-\frac2{2a+3b+c}+\frac2{2a+2b}+\frac1{a+2b+c}.
\]

A sharp qualitative distinction appears between packets of degree at most two and those permitting degree three. Every degree-at-most-two distribution obeys the strict, uniform lower bound

\[
E>\frac{27921}{10000}=2.7921.
\]

In contrast, the explicitly realizable fully symmetric length-\(100\) binary generator matrix with 24 copies of **each** singleton-support column, nine copies of **each** two-coordinate-support column, and one all-three-coordinate-support column has

\[
E=\frac{13700419}{4906902}\approx2.7920710460<\frac{27921}{10000}.
\]

Consequently, any fully symmetric generator matrix globally minimizing peeling random-access expectation over **all finite lengths** must contain a weight-three column if such a minimum exists; more concretely, the optimal expected peeling time within length \(100\) is strictly smaller than the expectation attainable by any fully symmetric matrix whose columns have weight at most two, even if its length is unrestricted. No assertion of global optimality of the displayed witness is made.

## Assumptions and scope

The source alphabet is binary, there are exactly three information coordinates, equations are noiseless, and samples are drawn independently with replacement. A degree \(i\) equation is the XOR of \(i\) distinct source coordinates chosen uniformly among all \(\binom3i\) supports, after selecting degree \(i\) with probability \(p_i\). Nonnegative probabilities sum to one. Repeated equations provide no additional peeling capability. A symbol is decoded only by iteratively exploiting equations with precisely one currently unknown coordinate; arbitrary Gaussian elimination on pairs of undecoded equations is not allowed. The target information coordinate is fixed, but symmetry makes its expected retrieval time independent of the choice. A finite matrix realization requires rational degree probabilities compatible with equal multiplicities within each degree, which holds for the displayed witness. The infimum statement compares finite fully symmetric matrices of any lengths.

## Proof

**The seven-term survival law.** Couple the draws to a unit-rate Poisson arrival process. The first appearance times of the seven nonzero support types are independent exponential variables with respective rates \(a\) for each of the three singleton types, \(b\) for each of the three pair types, and \(c\) for the unique triple type. Let \(\tau\) be the continuous time when peeling first recovers target coordinate \(A\), and set

\[
u=e^{-at},\qquad v=e^{-bt},\qquad w=e^{-ct}.
\]

A singleton \(A\) must be absent for failure, contributing the factor \(u\). Condition on the number of the two target-incident pair types \(AB,AC\) already present. If neither is present (probability \(v^2\)), then only the triple equation can recover \(A\), and it does so precisely when both \(B,C\) have already been recovered from their singleton types and, optionally, their mutual pair \(BC\). The probability that \(B,C\) are both recovered without \(A\) is \((1-u)^2+2u(1-u)(1-v)\). Thus the failure factor in this case is \(1-(1-w)[(1-u)^2+2u(1-u)(1-v)]\).

If exactly one target-incident pair is present (probability \(2v(1-v)\)), the two coordinates in that pair form a connected component; failure occurs precisely when it has no available singleton seed, with conditional probability \(u[v+(1-v)u]\). In this situation the triple equation cannot create the missing singleton seed. If both target-incident pairs are present (probability \((1-v)^2\)), all three source coordinates belong to one pair-component, which fails only if both other singleton types are absent (probability \(u^2\)). The triple equation again cannot produce an initial singleton seed. Combining the cases gives the manifestly nonnegative expression

\[
\Pr(\tau>t)=u\Bigl\{v^2\bigl[1-(1-w)((1-u)^2+2u(1-u)(1-v))\bigr]
+2v(1-v)u[v+(1-v)u]+(1-v)^2u^2\Bigr\}.
\]

Expanding this expression yields the exact seven-monomial form

\[
\Pr(\tau>t)=2u^3v^3w-u^3v^2w-2u^3v^2+u^3-2u^2v^3w+2u^2v^2+uv^2w.
\]

By integration over \(t\ge0\) we obtain the displayed rational formula for \(E\). The equality \(\mathbb E T=\mathbb E\tau\), where \(T\) counts the original number of discrete draws, holds because the independent exponential interarrival times have mean one and the number of arrivals needed is determined solely by the independently sampled support labels. When \(p_1=0\), no peeling step can ever begin, so \(T=\infty\) almost surely. The formula is continuous at all other simplex boundaries with \(p_1>0\).

**Uniform obstruction for degrees at most two.** Write \(x=p_1\) and set \(p_2=1-x\), \(p_3=0\), where \(0<x\le1\). Substitution and exact rational simplification give

\[
E_2(x)=\frac{5x^4-20x^3+25x^2-4x+12}{x(x-3)(x-2)(x+2)}.
\]

All four denominator factors multiply to a strictly positive product on this domain. Hence \(E_2(x)>27921/10000\) is equivalent to strict positivity of

\[
Q(x)=22079x^4-116237x^3+361684x^2-375052x+120000.
\]

Indeed, \(E_2(x)-27921/10000=Q(x)/(10000x(x-3)(x-2)(x+2))\). On the whole interval \([0,1]\), the derivative \(Q^{(3)}(x)=529896x-697422<0\), and therefore \(Q''(x)\ge Q''(1)=290894>0\). Taylor's convex lower bound about \(r=363/500\), followed by completing the square, gives **at every real** \(x\in[0,1]\)

\[
Q(x)\ge Q(r)+Q'(r)(x-r)+145447(x-r)^2
\ge Q(r)-\frac{Q'(r)^2}{581788}
=\frac{71305991069476208741}{35509521484375000000}>0.
\]

This establishes the stated uniform strict lower bound for all degree-one/two mixtures. The endpoint \(x=0\) has infinite expectation instead.

**Exact finite witness.** The 100 columns described in the Finding have degree probabilities \((p_1,p_2,p_3)=(18/25,27/100,1/100)\) and include all three coordinate singletons, hence they span the information space. Inserting these rational probabilities into the seven-denominator formula and reducing gives

\[
E=\frac{13700419}{4906902},\quad
\frac{27921}{10000}-E=\frac{710371}{24534510000}>0.
\]

Thus a strictly positive degree-three component beats every purely degree-one/two distribution, including every such finite fully symmetric generator matrix of arbitrary length. The global support-necessity conclusion follows directly.

## Verification

The accompanying standard-library Python program `verify_peeling.py` independently enumerates all 128 observation patterns of the seven possible equation supports and performs exact peeling in each. It obtains 28 failure patterns and derives exactly the seven monomials by expansion of their appearance probabilities. Separately, a rational first-appearance dynamic program evaluates the discrete expected draw count for six probability distributions, agreeing with the integral. Exact rational arithmetic checks the degree-one/two polynomial identity, positivity certificate and length-100 witness. Run `python3 verify_peeling.py`; expected completion marker is `CHECK_OK`. Finite checks corroborate, but do not replace, the infinite-parameter algebraic proof above.

## Relationship to prior work

Hofmeister, Bitar and Yaakobi (first public version May 11, 2026) identify the equivalence between fully symmetric binary generator matrices and LT degree distributions, and analyze peeling access in the large-number-of-information-symbols regime. The result above applies this model at exactly **three** information symbols, derives the finite-case failure law and proves a strict degree-three support requirement. Wang and Yaakobi (January 2026) establish a general exact recovery expectation under unrestricted linear decoding; its rank-based recoverability criterion differs from iterative peeling and does not imply the asserted strict peeling-degree obstruction. Boruchovsky and collaborators (January 2025) investigate random access constructions and solve the unrestricted two-information-symbol case. Those contributions are not claimed as new here.

## Limitations

The quantitative improvement beyond the degree-one/two uniform bound is small. No physical sequencing performance claim or practical significance of that numerical gap is asserted. The formula assumes binary coefficients, equal frequency within each support weight, independent noiseless sampling, and peeling-only decoding. It does not identify the optimal three-coordinate degree distribution, treat nonbinary fields or nonsymmetric matrices, or establish analogous necessity for larger source dimension. A 2005 technical report by Tirronen on small-case LT degree distributions is plausibly related, but its full text could not be inspected; it remains a specifically identified priority risk. Priority against unindexed or unpublished finite-parameter results is not independently certified.

## References

1. C. Hofmeister, R. Bitar and E. Yaakobi, *Random Access Expectation in DNA Storage and Fountain Codes*, arXiv:2605.10919, first submitted 2026-05-11. https://arxiv.org/abs/2605.10919
2. C. Wang and E. Yaakobi, *Random Access in DNA Storage: Algorithms, Constructions, and Bounds*, arXiv:2601.07053, first submitted 2026-01-11. https://arxiv.org/abs/2601.07053
3. A. Boruchovsky, O. Elishco, R. Gabrys, A. Gruica, I. Tamo and E. Yaakobi, *Making it to First: The Random Access Problem in DNA Storage*, arXiv:2501.12274, first submitted 2025-01-21. https://arxiv.org/abs/2501.12274

4. T. Tirronen, *Optimal Degree Distributions for LT Codes in Small Cases*, Helsinki University of Technology, 2005. Full text not inspected.
