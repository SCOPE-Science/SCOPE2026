# Exact monotone ordinal-run probabilities and Dirichlet selection of fixed-point measures

## Finding
For every integer \(b\ge 2\), let \(T_b(x)=bx\bmod 1\) on \([0,1)\), and let \(X\) have normalized Lebesgue law. For every integer \(m\ge1\), the probability of a strictly increasing orbit segment of \(m+1\) observations is exactly
\[
\mathbb P\{X<T_bX<\cdots<T_b^{m}X\}
 =\frac{\binom{m+b-1}{b-2}}{(b-1)b^m}
 \sim \frac{m^{b-2}}{(b-1)(b-2)!\,b^m}\quad(m\to\infty).
\]
The displayed asymptotic holds for each fixed \(b\). In particular, polynomial corrections of degree \(b-2\) accompany the exponential rarity.

There is also a limiting law *for the orbit selected by this rare event*. Put \(\alpha_j=j/(b-1)\) for \(j=0,\ldots,b-2\), the \(b-1\) distinct fixed points of \(T_b\) in \([0,1)\), and let
\[
\eta_m=\frac1m\sum_{t=0}^{m-1}\delta_{T_b^t X}.
\]
Conditionally on the strictly increasing orbit event, the random probability measure \(\eta_m\) converges in distribution for the weak topology to
\[
\eta_\infty=\sum_{j=0}^{b-2}D_j\,\delta_{\alpha_j},
\qquad (D_0,\ldots,D_{b-2})\sim\operatorname{Dirichlet}(1,\ldots,1).
\]
For \(b=2\), the one-dimensional Dirichlet law is understood as the point mass at \(D_0=1\). In particular, for independent \(U_1,\ldots,U_{b-2}\sim\operatorname{Uniform}(0,1)\),
\[
\frac1m\sum_{t=0}^{m-1}T_b^t X
\ \xrightarrow{\mathrm{law}}\
\frac{U_1+\cdots+U_{b-2}}{b-1},
\]
with the empty sum equal to zero when \(b=2\). This limit has mean \((b-2)/(2(b-1))\) and variance \((b-2)/(12(b-1)^2)\).

More precisely, for \(m\ge b-1\), the conditional probability that the successive orbit points visit all \(b-1\) order-increasing branches is
\[
\frac{\binom{m-1}{b-2}}{\binom{m+b-1}{b-2}}=1-O_b(m^{-1}).
\]
On this event their positive branch occupancy counts are *exactly uniform* among compositions of \(m\) into \(b-1\) positive parts. The measure-convergence proof has the pathwise quantitative bound \(W_1(\eta_m,\nu_m)\le b/m\), where \(\nu_m\) replaces each observed state by its branch's fixed point.

## Assumptions and scope
The base \(b\) is a fixed integer at least two. The starting point is sampled from normalized Lebesgue measure on \([0,1)\). Strict inequalities define the ordinal event; discontinuity and endpoint cases form a null set and have no influence on probabilities or conditional limits. All limits are as the number \(m\) of adjacent comparisons tends to infinity with \(b\) fixed. There is no assertion for noninteger multipliers, other initial laws, or arbitrary ordinal permutations.

For \(j=0,\ldots,b-2\), define the open increasing branches
\[
E_j=\left(\frac{j}{b-1},\frac{j+1}{b}\right),
\qquad \ell_j=|E_j|=\frac{b-1-j}{b(b-1)}.
\]
At each time \(0\le t<m\) of a strictly increasing orbit segment, there is a unique branch label \(J_t=j\) such that \(T_b^tX\in E_j\). Let \(L_j=\#\{t:J_t=j\}\) and define \(\nu_m=\sum_{j=0}^{b-2}(L_j/m)\delta_{\alpha_j}\). The distance \(W_1\) is the usual 1-Wasserstein distance on probability measures on \([0,1]\) with absolute-value cost.

## Proof
**1. Geometry and allowed itineraries.** On the digit interval \((j/b,(j+1)/b)\), the map is \(T_b(x)=bx-j\). The strict inequality \(x<T_b(x)\) is equivalent to \(x>j/(b-1)\). It is therefore satisfied exactly on the union of \(E_0,\ldots,E_{b-2}\). (For \(j=b-1\) this inequality has no solution in the digit interval.) Every branch \(T_b:E_j\to(\alpha_j,1)\) is affine with slope \(b\). Since \(E_k\subset(\alpha_j,1)\) exactly when \(k\ge j\), and is disjoint from this image when \(k<j\), a surviving label path must be nondecreasing:
\[
0\le J_0\le J_1\le\cdots\le J_{m-1}\le b-2.
\]
Conversely, every such path occurs on an open interval of positive length. Starting with the final interval \(E_{J_{m-1}}\) and pulling it backward along the specified branches gives exactly one inverse image per earlier time, of slope \(1/b\). Its measure is
\[
\mathbb P\{J_0=j_0,\ldots,J_{m-1}=j_{m-1}\}
=\frac{\ell_{j_{m-1}}}{b^{m-1}}.
\]
These intervals are disjoint up to endpoints, so no multiplicities are hidden in the probability sum.

**2. Exact counting.** The number of weakly increasing paths of length \(m\) ending at label \(k\) equals \(\binom{m+k-1}{k}\). Thus
\[
\mathbb P\{X<T_bX<\cdots<T_b^mX\}
 =\frac1{(b-1)b^m}\sum_{k=0}^{b-2}(b-1-k)\binom{m+k-1}{k}.
\]
Rewrite \(b-1-k\) as the number of integers \(h\) with \(k\le h\le b-2\). Interchange the sums and use the hockey-stick identity twice:
\[
\sum_{k=0}^{b-2}(b-1-k)\binom{m+k-1}{k}
 =\sum_{h=0}^{b-2}\sum_{k=0}^{h}\binom{m+k-1}{k}
 =\sum_{h=0}^{b-2}\binom{m+h}{h}
 =\binom{m+b-1}{b-2}.
\]
The fixed-base binomial asymptotic gives the stated polynomial-times-exponential estimate, including \(b=2\).

**3. Uniform occupancy compositions.** A nondecreasing path uses all branches precisely when it is a word consisting of \(L_0\ge1\) zeros, then \(L_1\ge1\) ones, and so forth, ending in \(L_{b-2}\ge1\) copies of \(b-2\), with \(\sum_j L_j=m\). There are \(\binom{m-1}{b-2}\) such compositions. Their terminal label is the same, so by the inverse-image formula they each have probability \(1/((b-1)b^m)\). Division by the exact event probability yields the asserted probability of full visitation. Since the numerator and denominator are monic polynomials of equal degree \(b-2\), this ratio tends to one with deficit \(O_b(1/m)\). Conditional on full visitation, all positive compositions have equal probability.

A uniformly sampled positive composition of \(m\) into \(b-1\) parts is equivalent to uniformly choosing \(b-2\) distinct cut positions from \(\{1,\ldots,m-1\}\). Their ordered, rescaled locations converge jointly to the order statistics of \(b-2\) independent uniform points in \([0,1]\). The vector of limiting spacings is \(\operatorname{Dirichlet}(1,\ldots,1)\). The probability of not visiting all branches vanishes; hence the same occupancy convergence holds without the additional conditioning.

**4. Concentration at fixed points and the orbit mean.** If labels equal \(j\) throughout a contiguous block of \(L\) times, then \(\alpha_j=j/(b-1)\) is a fixed point for that affine branch and
\[
T_b^{t+1}X-\alpha_j=b(T_b^tX-\alpha_j)
\]
inside the block. Consequently, measured backward from the last point, the nonnegative deviations form a geometric progression and their sum is at most \(\sum_{s=0}^{L-1}b^{-s}<b/(b-1)\). Since a nondecreasing path uses at most \(b-1\) blocks, for every permitted starting point
\[
0\le\sum_{t=0}^{m-1}(T_b^tX-\alpha_{J_t})\le b.
\]
Couple the empirical measure with the atomic measure \(\nu_m\) by pairing each observed state to its branch fixed point. The preceding bound gives \(W_1(\eta_m,\nu_m)\le b/m\). Since \(\nu_m\) is the continuous image of the occupancy proportions and these converge to the uniform-simplex law, \(\eta_m\) converges in distribution to \(\eta_\infty\) in the weak topology. Equivalently, for every Lipschitz test function, the empirical integral differs from its fixed-point mixture by at most \(b\operatorname{Lip}(f)/m\); density extends the conclusion to continuous functions.

Finally, if \(V_1<\cdots<V_{b-2}\) are the order statistics of the uniform cut points, then the spacing identity gives
\[
\sum_{j=0}^{b-2}jD_j=(b-2)-\sum_{i=1}^{b-2}V_i.
\]
The last expression has the same law as a sum of \(b-2\) independent uniform variables by the symmetry \(U\stackrel d=1-U\). Dividing by \(b-1\) proves the stated orbit-average limit. Its mean and variance follow from those of independent uniforms.

## Verification
The accompanying standalone Python 3 program `verify.py` enumerates fine base-adic intervals for the first \(m+1\) map iterates, intersects the affine inequalities using exact `fractions.Fraction` arithmetic independently of the inverse-branch proof, reconstructs every nondecreasing label path and its exact interval measure, and checks the complete-branch composition probability and geometric orbit-deviation bound. The saved-program result is recorded in `VERIFICATION.md`. These finite enumerations do not establish the all-length formula or the limiting law; those follow from the preceding proof.

## Relationship to prior work
Amigó, Elizalde and Kennel developed forbidden/allowed order-pattern theory for finite-alphabet shifts and explicitly identified the integer sawtooth map with the uniform-symbol Bernoulli shift. Their focus is *which* patterns occur and related combinatorics, not the Lebesgue probability of arbitrarily long increasing patterns or a conditional random occupation measure. Elizalde subsequently counted the number of distinct realizable permutations as a function of alphabet size, rather than the measure of the monotone pattern. The later work on \(\beta\)-shifts and negative shifts determines realization thresholds of patterns, again not the conditional Dirichlet law. These foundational results are credited here. A literature comparison cannot exclude all unpublished or unindexed specializations; independent historical-priority confirmation remains outstanding.

## Limitations
The result relies on integer expansion, the standard order on \([0,1)\), normalized Lebesgue initialization, and strictly consecutive increasing observations. It does not classify probabilities of arbitrary permutations, noninteger \(\beta\)-transformations, or arbitrary invariant initial measures. The Dirichlet limit is weak convergence under conditioning on a probability that decays to zero; it is not an unconditioned orbit law. Endpoint configurations have probability zero but may not obey the strict-branch label description pointwise. No independent scientific audit has been performed.

## References
1. J. M. Amigó, S. Elizalde and M. B. Kennel, *Forbidden patterns and shift systems*, arXiv:0707.4628, first posted 31 July 2007; Journal of Combinatorial Theory, Series A 115 (2008), 485–504.
2. S. Elizalde, *The Number of Permutations Realized by a Shift*, arXiv:0909.2274, first posted 11 September 2009; SIAM Journal on Discrete Mathematics 23 (2009), 765–786.
3. S. Elizalde, *Permutations and \(\beta\)-shifts*, arXiv:1008.4167, first posted 24 August 2010.
4. S. Elizalde and K. Moore, *Patterns of Negative Shifts and Beta-Shifts*, arXiv:1512.04479, first posted 14 December 2015.
