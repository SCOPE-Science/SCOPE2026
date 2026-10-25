# Four-block Bernoulli mimicry and a sharp fifth-block interaction in the cat map

## Finding

Let \(T:\mathbb T^2\to\mathbb T^2\) be Arnold's standard cat automorphism
\[
T(x,y)=(2x+y,x+y)\pmod 1,
\]
let \((x,y)\) have normalized Haar measure, and let \(Z_n=s(\pi_1 T^n(x,y))\), where \(s(u)=+1\) for \(0\leq\{u\}<1/2\) and \(s(u)=-1\) for \(1/2\leq\{u\}<1\). The stationary binary process has the following **complete five-observation law**: for every \((\varepsilon_0,\ldots,\varepsilon_4)\in\{-1,+1\}^5\),
\[
\mathbb P(Z_0=\varepsilon_0,\ldots,Z_4=\varepsilon_4)
=\frac1{32}\left(1+\frac{\varepsilon_0\varepsilon_1\varepsilon_3\varepsilon_4}{21}\right).
\]
In particular every block of four consecutive observations consists of independent fair signs, whereas every block of five has a nonzero fourth-order interaction:
\[
\mathbb E(Z_0Z_1Z_3Z_4)=\frac1{21}.
\]
The two possible five-word probabilities are \(11/336\) and \(5/168\), each attained by sixteen words. The first conditional predictive-information defect is exactly
\[
I(Z_0;Z_4\mid Z_1,Z_2,Z_3)
=\frac12\left[\frac{22}{21}\log\frac{22}{21}
+\frac{20}{21}\log\frac{20}{21}\right]>0
\]
(in nats), while \(I(Z_0;Z_3\mid Z_1,Z_2)=0\).

## Assumptions and scope

The torus is \(\mathbb T^2=(\mathbb R/\mathbb Z)^2\) with its probability Haar measure. The map \(T\) is invertible, integer-linear, and has determinant one, hence preserves Haar measure and makes the observed process stationary. All probability statements are exact for this partition at the half-circle threshold. Boundary points lie in a Haar-null set and do not affect the law. The result concerns consecutive times \(0,1,2,3,4\) and their translates, not arbitrary five time indices or all observation thresholds.

## Proof

**1. Reduce the dynamics to two independent circle coordinates.** Put \(u=\pi_1(x,y)=x\) and \(v=\pi_1 T(x,y)=2x+y\pmod 1\). The coordinate change \((x,y)\mapsto(u,v)\) is an integer torus automorphism of determinant one, hence \(u,v\) are jointly Haar-uniform. From the characteristic polynomial of \(T\), \(a_{n+2}=3a_{n+1}-a_n\pmod1\) for the first-coordinate orbit. Therefore its first five entries are the linear forms
\[
L_0=u,\quad L_1=v,\quad L_2=-u+3v,\quad
L_3=-3u+8v,\quad L_4=-8u+21v\pmod1.
\]

**2. Establish the vanishing Walsh moments.** Except on null boundaries, \(s(-t)=-s(t)\) and \(s(t+1/2)=-s(t)\). The first identity, coupled with Haar invariance under \((u,v)\mapsto(-u,-v)\), makes every odd-order moment of distinct observations vanish. Every two linear forms among the displayed five have nonzero determinant as row vectors. Consequently their joint evaluation map from \(\mathbb T^2\) onto \(\mathbb T^2\) sends Haar to Haar, and each two-sign moment also vanishes.

Modulo two, the coefficient vectors of \((L_0,L_1,L_2,L_3,L_4)\) are
\[
(1,0),\ (0,1),\ (1,1),\ (1,0),\ (0,1).
\]
Translating \((u,v)\) by \((a/2,b/2)\) multiplies a product of selected signs by the character of the sum of its coefficient vectors modulo two. Such a moment must be zero unless that sum is \((0,0)\). Among the five four-element subsets of \(\{0,1,2,3,4\}\), **only** \(\{0,1,3,4\}\) has zero sum. This proves that all nonconstant Walsh moments of the five-sign law vanish except potentially \(\mathbb E(Z_0Z_1Z_3Z_4)\). In particular any four consecutive signs are independent fair signs, provided the exceptional moment is treated separately.

**3. Compute the exceptional moment exactly.** The remaining integral is
\[
C=\int_{[0,1]^2}s(u)s(v)s(-3u+8v)s(-8u+21v)\,du\,dv.
\]
Here is a finite, wholly rational area certificate. For any integer pair \((a,b)\), the value of \(s(au+bv)\) in the half-open strip
\[
k\leq 2(au+bv)<k+1\qquad(k\in\mathbb Z)
\]
is \((-1)^k\). Starting from the unit square, successively intersect each current convex polygon with every strip that meets its interior. For intersections with an affine half-plane, each new vertex is the exact line-segment intersection of two rational points, and area is the absolute shoelace sum divided by two. The strip interiors partition the preceding polygon, so this procedure computes the integral *exactly*, with no sampling approximation. All line coordinates here are rational.

For the four forms \((1,0),(0,1),(-3,8),(-8,21)\), the successive numbers of positive-area polygons are \(2,4,44,156\); the sum of their areas is exactly one, and their signed area sum is
\[
C=1/21.
\]
As a separate complete finite partition check, inserting the intermediate form \((-1,3)\) produces polygon counts \(2,4,16,56,168\). Grouping the 168 exact rational polygon areas by all thirty-two five-sign words produces precisely sixteen word cells of measure \(11/336\) and sixteen of measure \(5/168\), with the former exactly those for which \(\varepsilon_0\varepsilon_1\varepsilon_3\varepsilon_4=+1\). The included `verify.py` specifies every clipping inequality and carries out both exact rational certificates; its mathematical correctness follows from the elementary polygon-partition and shoelace identities just established.

**4. Recover probabilities and information.** Walsh inversion on \(\{-1,+1\}^5\) gives the claimed joint distribution because all other nonconstant moments vanish. Marginalizing any terminal or initial coordinate gives a uniform distribution on sixteen four-sign words. For the information identity, conditioned on \((Z_1,Z_2,Z_3)\), the two fair signs \((Z_0,Z_4)\) have joint law \(\tfrac14[1+(Z_1Z_3/21)Z_0Z_4]\); its mutual information is the displayed positive expression. The four-block independence gives the zero preceding term. Stationarity transfers every assertion to any consecutive observation window.

## Verification

Run `python verify.py` with a standard Python 3 interpreter, without external packages. It checks the mod-two symmetry table and nonparallelism of every pair; computes the exact five-word probability table using `fractions.Fraction`; checks each of the thirty-two exact word probabilities and both four-block uniform marginals; and independently clips the four-form region to recover \(1/21\). The exact partition sizes are \([2,4,16,56,168]\) for the five-word law and \([2,4,44,156]\) for the four-form moment. All tests passed when executed from the packaged script. The computation is finite and exhaustive because every strip meeting the unit square is included; no probability is inferred from approximate experiments.

## Relationship to prior work

Cafaro, Lord, Sun, and Bollt (arXiv:1507.07262, first version 11 July 2015) study the way finite symbolic partitions affect dependence and Markov-order diagnostics, primarily for the tent map. Hu and Rosenhaus (arXiv:2204.13655, first version 28 April 2022), especially their Section 3, give a Fourier treatment of cat-map correlation functions and the integer recurrence coefficients \(1,3,8,21\), focusing on two-point correlation formulas. These frameworks motivate the present finite-block question but do not explicitly supply the five-sign law or the rational fourth moment above in the inspected relevant sections. Crawford and Cary (Physica D 6, 1983) studied two-point cat-map correlations earlier; their complete paper was not available for page-level inspection here. The new claim is restricted to the exact half-strip binary observation and the sharply specified five-observation distribution, not a new general theory of correlations or coding.

## Limitations

No claim is made about higher block lengths, the Markov order of the full process, general five-time subsets, or a generating property of this partition. General Fourier approaches might imply the result after a nontrivial specialization and exact integration; historical priority remains to be independently established. The finite rational clipping certificate verifies the exact arithmetic for this explicitly defined planar integral, while the vanishing moments and Walsh reconstruction are proved analytically. The scientific review accompanying this result is not an independent validation.

## References

1. C. Cafaro, W. M. Lord, J. Sun, E. M. Bollt, *Causation entropy from symbolic representations of dynamical systems*, arXiv:1507.07262v1 (11 July 2015), https://arxiv.org/abs/1507.07262.
2. X.-Y. Hu and V. Rosenhaus, *Correlation functions in linear chaotic maps*, arXiv:2204.13655v1 (28 April 2022), https://arxiv.org/abs/2204.13655.
3. J. D. Crawford and J. R. Cary, *Decay of correlations in a chaotic measure-preserving transformation*, Physica D 6 (1983), 223–232, doi:10.1016/0167-2789(83)90007-6 (background; full text not inspected).
