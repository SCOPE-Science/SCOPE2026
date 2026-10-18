# Logarithmic race laws and arbitrary-length orderings of palindromic numeral counts

## Finding

Let \(A_b(n)\) be the number of positive integers not exceeding \(n\) whose standard base-\(b\) expansions are palindromes. For any finite collection of distinct bases \(b_1,\ldots,b_k\ge2\), suppose that the real numbers
\[
\frac1{\log b_1},\ldots,\frac1{\log b_k}
\]
are linearly independent over \(\mathbb Q\). Under logarithmic averaging over positive integers, the random vector
\[
\left(\frac{A_{b_i}(n)}{\sqrt n}\right)_{i=1}^{k}
\]
converges in distribution to a vector of independent random variables
\[
Y_i=2\cosh\!\left(\frac{\log b_i}{2}U_i\right),
\qquad U_1,\ldots,U_k\ \text{independent and uniform on }[0,1].
\]
For every permutation \(\pi\) of \(\{1,\ldots,k\}\), the set of positive integers satisfying
\[
A_{b_{\pi(1)}}(n)<\cdots<A_{b_{\pi(k)}}(n)
\]
has the following strictly positive logarithmic density:
\[
\boxed{d_\pi=\frac1{\prod_{i=1}^{k}\log b_i}
\int_{\substack{0<t_i<\log b_i\ (1\le i\le k)\\
 t_{\pi(1)}<\cdots<t_{\pi(k)}}}
 dt_1\cdots dt_k>0.}
\]
The set of equality ties between any two counting functions has logarithmic density zero. Hence each strict ordering occurs infinitely often.

For two bases \(b<c\) with \(\log b/\log c\notin\mathbb Q\), the density simplifies to
\[
\boxed{\delta_{\log}\{n:A_b(n)>A_c(n)\}=\frac{\log b}{2\log c}.}
\]
In particular the fraction in the logarithmic sense for \(A_2(n)>A_3(n)\) is \(\log2/(2\log3)\), approximately \(0.3154648767857\).

For every integer \(k\ge2\), the explicitly prescribed bases
\[
\boxed{b_j=3\cdot2^j\quad (1\le j\le k)}
\]
satisfy the independence hypothesis. Thus *all* \(k!\) strict orderings occur with positive, explicitly computable logarithmic densities for an arbitrarily long family of bases. This supplies an unconditional infinite collection of cases of the multibase race problem posed by Phunphayap and Pongsriiam.

## Assumptions and scope

The logarithmic density of a set \(S\subseteq\mathbb N\), when it exists, is
\[
\delta_{\log}(S)=\lim_{X\to\infty}\frac1{\log X}
\sum_{\substack{1\le n\le X\\ n\in S}}\frac1n.
\]
Here \(X>1\), all bases are integers at least two, and all logarithms are natural. The asserted frequency is logarithmic density, not ordinary natural density. Only the full rational independence of reciprocal logarithms gives the general joint-law conclusion; pairwise irrational ratios alone are not assumed sufficient when \(k\ge3\). All ordering statements use *strict* inequalities.

## Proof

**1. Exact palindromic counting identity.** Fix \(b\ge2\) and \(n\ge1\). Let \(m=\lfloor\log_b n\rfloor\), \(H=b^{\lceil m/2\rceil}\), and \(P=\lfloor n/H\rfloor\). Let \(\varepsilon\in\{0,1\}\) indicate whether the unique length-\(m+1\) palindrome formed by reflecting the first \(\lceil(m+1)/2\rceil\) digits of \(n\) does not exceed \(n\). Then
\[
\boxed{A_b(n)=H+P+\varepsilon-2.}\tag{1}
\]
Indeed there are \((b-1)b^{\lfloor(\ell-1)/2\rfloor}\) palindromes of length \(\ell\ge1\). When \(m=2r\), summing lengths up to \(2r\) gives \(2(b^r-1)\); the palindromes of length \(2r+1\) not exceeding \(n\) number \(P-b^r+\varepsilon\). When \(m=2r+1\), summing lengths up to \(2r+1\) gives \((b+1)b^r-2\); palindromes of length \(2r+2\) not exceeding \(n\) number \(P-b^r+\varepsilon\). Both yield (1), including \(m=0\). Consequently,
\[
\left|A_b(n)-\left(H+\frac nH\right)\right|\le3.\tag{2}
\]

**2. Exact phase profile up to a uniform bounded error.** Put \(s_b(n)=\log_b n\) and let
\[
\Delta_b(n)=\operatorname{dist}\bigl(s_b(n),2\mathbb Z\bigr)\in[0,1].
\]
If \(s_b(n)\in[2r,2r+1]\), then \(H/\sqrt n=b^{-\Delta_b(n)/2}\). If \(s_b(n)\in[2r+1,2r+2]\), then \(H/\sqrt n=b^{\Delta_b(n)/2}\). In both cases,
\[
\boxed{\frac{A_b(n)}{\sqrt n}=
2\cosh\!\left(\frac{\log b}{2}\Delta_b(n)\right)+O_b(n^{-1/2}).}\tag{3}
\]
The implied constant can be chosen as \(3\), uniformly for each fixed base.

**3. Weighted torus equidistribution.** Define the torus phases
\[
\theta_i(n)=\frac{\log n}{2\log b_i}\pmod1.
\]
For every nonzero integer vector \(h\in\mathbb Z^k\), the independence hypothesis gives \(\omega_h=\pi\sum_i h_i/\log b_i\ne0\). By comparison with the integral (for fixed \(h\)),
\[
\sum_{n\le X}\frac{e^{2\pi i\sum_i h_i\theta_i(n)}}n
=\int_1^X x^{i\omega_h-1}\,dx+O_h(1)
=\frac{X^{i\omega_h}-1}{i\omega_h}+O_h(1)=O_h(1).
\]
Dividing by \(\log X\) and invoking the trigonometric-polynomial form of Weyl's criterion gives Haar equidistribution of \((\theta_i(n))\) under logarithmic weights. The map \(\theta\mapsto2\operatorname{dist}(\theta,\mathbb Z)\) sends uniform measure on the unit circle to uniform measure on \([0,1]\). Applying this map independently in the coordinates, then (3), proves the asserted product joint law for bounded continuous test functions. To pass from the phase profile to (3), disregard any fixed finite initial interval and note that the sup-norm error tends to zero on its complement.

**4. Strict rankings and absence of ties.** Since \(u\mapsto2\cosh(u/2)\) is strictly increasing for \(u\ge0\), rankings of the limiting variables are the same as rankings of the independent uniforms \(T_i=(\log b_i)U_i\) on \([0,\log b_i]\). Their joint density is constant \(1/\prod_i\log b_i\) on the product box. Integrating over the ordering chamber gives the displayed formula for \(d_\pi\). The chamber contains a nonempty open simplex in \((0,\min_i\log b_i)^k\), hence has strictly positive volume. Equality hypersurfaces \(T_i=T_j\) have zero product measure. The boundary-zero form of weak convergence, together with (3), therefore proves the density of each strict ranking and the zero density of pairwise ties, even though each finite count is integer-valued. For \(b<c\), direct integration for independent \(T_b\sim\operatorname{Unif}[0,\log b]\), \(T_c\sim\operatorname{Unif}[0,\log c]\) yields
\[
\Pr(T_b>T_c)=\frac1{\log b}\int_0^{\log b}\frac t{\log c}\,dt=\frac{\log b}{2\log c}.
\]

**5. An explicit family in arbitrarily many bases.** Put \(\alpha=\log2/\log3\). This number is irrational since an equality \(2^q=3^p\), with positive integers \(p,q\), is impossible. If \(\alpha\) were irrational algebraic, the Gelfond--Schneider theorem would make \(3^\alpha=2\) transcendental, a contradiction. Thus \(\alpha\) is transcendental. For \(b_j=3\cdot2^j\),
\[
\frac1{\log b_j}=\frac1{\log3}\cdot\frac1{1+j\alpha}.
\]
Any rational linear relation among these reciprocals would give a rational function \(\sum_{j=1}^k q_j/(1+jz)\), with coefficients \(q_j\in\mathbb Q\), vanishing at the transcendental \(z=\alpha\). After clearing denominators, its numerator is a rational polynomial vanishing at a transcendental number, so is identically zero. Distinct simple poles at \(z=-1/j\) then force every \(q_j=0\). The reciprocal logarithms are therefore linearly independent over \(\mathbb Q\), as claimed.

## Verification

The accompanying `palindrome_checker.py` independently counts palindromes by digit reversal and compares them with (1) for each \(1\le n\le5000\) and bases \(2,3,4,5,6,7,8,10,12\), giving \(45{,}000\) exact count comparisons. It additionally checks the sharp bounded-error estimate, the rational ordered-volume identity over finite integer ranges, normalization over permutations, and the two-base formula. The resulting suite produces `CERTIFICATE_PASS` with \(45{,}082\) comparisons. These computations check finite identities; the joint distribution and infinite family follow from the proof above, not from enumeration.

## Relationship to prior work

Phunphayap and Pongsriiam (2021 public release, 2022 volume) established asymptotic extremal orders and infinitely many sign changes between any two counting functions; their Corollary 14 also proves that pairwise equalities recur infinitely often, consistent with the present zero-*logarithmic-density* tie theorem. Their concluding Problem 2 proposed studying arbitrarily long strict multibase orderings. Phunphayap and Pongsriiam (2023) completed a two-base difference comparison and posed Question 4.1, conjecturing infinite occurrences of arbitrary orderings when all pairwise logarithm ratios are irrational. The inspected full papers do not provide the joint logarithmic distribution, the explicit ordering densities, or the unconditional arbitrarily long family of bases here. This theorem establishes the conjectured ordering property for the displayed family, **not** for every family with pairwise irrational ratios. Standard exact digit-prefix counting and classical Weyl equidistribution and Gelfond--Schneider are used as inputs; no priority is claimed for those ingredients. A stronger general theorem may subsume the application, and publication priority requires independent literature review.

## Limitations

The densities are logarithmic; ordinary natural densities may not exist. The independence hypothesis is stronger than pairwise irrationality for collections of at least three bases. No uniform error estimates in the number of bases, effective rates of equidistribution, or general solution to the multibase question are established. Potentially broader published theorems could imply some or all of the stated consequences. Independent validation has not been performed.

## References

[1] P. Phunphayap and P. Pongsriiam, “Extremal orders and races between palindromes in different bases,” *AIMS Mathematics* 7 (2022), 2237–2254. Published online 10 November 2021. DOI: 10.3934/math.2022127. Full text: https://www.aimspress.com/aimspress-data/math/2022/2/PDF/math-07-02-127.pdf

[2] P. N. Phunphayap and P. Pongsriiam, “A complete comparison for the number of palindromes in different bases,” *AIMS Mathematics* 8 (2023), 9924–9932. Published online 23 February 2023. DOI: 10.3934/math.2023502. Full text: https://www.aimspress.com/aimspress-data/math/2023/4/PDF/math-08-04-502.pdf

[3] P. Pongsriiam and K. Subwattanachai, “Exact formulas for the number of palindromes up to a given positive integer,” *International Journal of Mathematics and Computer Science* 14 (2019), 27–46 (bibliographic context).
