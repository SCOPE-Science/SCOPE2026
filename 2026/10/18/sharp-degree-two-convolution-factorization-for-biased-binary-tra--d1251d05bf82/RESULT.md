# Sharp degree-two convolution factorization for biased binary transition counts

## Finding
For each integer \(n\ge 2\) and \(0<p<1\), let \(X_1,\ldots,X_n\) be independent Bernoulli variables with success probability \(p\), and let
\[
T_n=\sum_{j=1}^{n-1}\mathbf 1\{X_j\ne X_{j+1}\}.
\]
The probability-generating polynomial \(Z_{n,p}(z)=\mathbb E[z^{T_n}]\) has every zero in the **strict open left half-plane** \(\{z:\operatorname{Re}z<0\}\). Consequently, \(T_n\) is distributed as a sum of independent nonnegative integer-valued random variables, each supported on \(\{0,1,2\}\).

Define the *bounded-summand factorization index* \(d(T_n)\) as the least integer \(d\ge 1\) for which this law is a convolution of finitely many independent laws supported on \(\{0,1,\ldots,d\}\). Its exact value is
\[
d(T_n)=\begin{cases}1,&n=2\text{ or }p=1/2,\\2,&n\ge3\text{ and }p\ne1/2.\end{cases}
\]
In particular, every biased sample of length at least three needs a genuinely quadratic convolution factor; it cannot be a Poisson-binomial distribution, despite its original representation as a sum of locally dependent Bernoulli transition indicators.

## Assumptions and scope
The observations are independent, identically distributed bits, the sample length is finite and at least two, and both letter probabilities are strictly positive. The parameter \(p\) is an arbitrary real number in \((0,1)\). The distribution is unconditional on the number of successes. The statistic counts **both** changes from zero to one and changes from one to zero, so the total number of runs of either symbol is \(T_n+1\). The auxiliary summands in the factorization need not be identically distributed or coupled to the observed transition indicators.

## Proof
Write \(r=p(1-p)\) and \(a=1-p\). A two-state transfer matrix for the probability-generating polynomial is
\[
M(z)=\begin{pmatrix}a&pz\\az&p\end{pmatrix},\qquad
Z_{n,p}(z)=(a,p)M(z)^{n-1}(1,1)^\mathsf T.
\]
Its trace is one and its determinant is \(r(1-z^2)\). The Cayley–Hamilton identity therefore yields, for \(n\ge1\),
\[
Z_{n+2,p}(z)=Z_{n+1,p}(z)-r(1-z^2)Z_{n,p}(z),
\]
with \(Z_{1,p}=1\) and \(Z_{2,p}(z)=1-2r+2rz\).

Define \(f_0(s)=f_1(s)=1\) and \(f_k(s)=f_{k-1}(s)-s f_{k-2}(s)\) for integers \(k\ge2\). The preceding recurrence implies, by induction, that for \(n\ge2\),
\[
Z_{n,p}(z)=f_{n-1}(s)-2r(1-z)f_{n-2}(s),\qquad s=r(1-z^2).
\]
We first exclude every imaginary-axis zero, for every admissible \(n,p\). Set \(z=it\) with real \(t\), so \(s=r(1+t^2)>0\) is real. Then
\[
\operatorname{Im}Z_{n,p}(it)=2rt\,f_{n-2}(s).
\]
If \(t\ne0\) and \(Z_{n,p}(it)=0\), the imaginary part implies \(f_{n-2}(s)=0\), while its real part gives \(f_{n-1}(s)=0\). Adjacent polynomials in this recurrence have no common zero: a common zero forces the preceding one to vanish because \(s>0\), and backwards iteration contradicts \(f_0=f_1=1\). If \(t=0\), then
\[
Z_{n,p}(0)=p^n+(1-p)^n>0,
\]
again excluding a zero.

The coefficient of \(z^{n-1}\) is the strictly positive probability of a perfectly alternating binary sequence, so \(Z_{n,p}\) always has degree exactly \(n-1\). Its coefficients vary continuously with \(p\), hence its roots vary continuously as an unordered multiset. At \(p=1/2\), the map from the original bits to the first bit and the successive exclusive-OR bits is bijective, so the changes are independent fair Bernoulli variables and
\[
Z_{n,1/2}(z)=\bigl((1+z)/2\bigr)^{n-1}.
\]
All roots therefore initially equal \(-1\). Moving \(p\) through the connected interval \((0,1)\) cannot transfer any root to the closed right half-plane without crossing the imaginary axis, which was excluded. This establishes strict left-half-plane location for every admissible \(n,p\).

Each negative real root contributes, after normalization at \(z=1\), a linear polynomial with two strictly positive coefficients. Each nonreal conjugate pair \(\alpha,\bar\alpha\), having \(\operatorname{Re}\alpha<0\), contributes the quadratic factor
\[
(z-\alpha)(z-\bar\alpha)=z^2-2\operatorname{Re}(\alpha)z+|\alpha|^2,
\]
whose three coefficients are strictly positive. Normalize all factors to value one at \(z=1\). Since \(Z_{n,p}(1)=1\), their product equals \(Z_{n,p}\). The normalized factors are probability-generating polynomials on \(\{0,1\}\) or \(\{0,1,2\}\), proving \(d(T_n)\le2\).

To show sharpness, let \(I_j=\mathbf1\{X_j\ne X_{j+1}\}\). Direct enumeration of triples gives
\[
\mathbb E I_j=2r,\quad \operatorname{Var}(I_j)=2r(1-2r),\quad
\operatorname{Cov}(I_j,I_{j+1})=r(1-4r).
\]
Nonadjacent transition indicators are independent, because they involve disjoint original bits. Consequently,
\[
\mu:=\mathbb E T_n=2r(n-1),\qquad
\operatorname{Var}(T_n)=2r(n-1)(1-2r)+2r(n-2)(1-4r).
\]
If \(T_n\) were a sum of independent Bernoulli variables, then, because its minimum is zero and maximum is \(n-1\), exactly \(n-1\) summands would be nondegenerate, with success probabilities \(b_1,\ldots,b_{n-1}\). In particular \(\sum b_j=\mu\), and Cauchy–Schwarz would give
\[
\operatorname{Var}(T_n)=\mu-\sum b_j^2\le\mu-\frac{\mu^2}{n-1}=2r(n-1)(1-2r).
\]
For \(n\ge3\) and \(p\ne1/2\) the displayed exact variance exceeds this bound by \(2r(n-2)(1-4r)>0\), a contradiction. At \(p=1/2\) the exclusive-OR argument already gives a binomial sum, and at \(n=2\) the transition count itself is Bernoulli with success probability \(2r\). Therefore the stated index is exact for all admissible parameters.

## Verification
Run `python3 check.py` using the included standard-library source. It independently computes exact rational generating polynomials by the transfer matrix, the recurrence, and explicit enumeration of binary words. It checks the displayed moments and exact Routh–Hurwitz determinants for rational parameter examples. The successful replay reports 594 polynomial coefficient comparisons, 396 strictly positive Hurwitz leading minors, and 132 exact moment comparisons through sample size twelve. These finite diagnostics are not used to infer the universal root-location theorem, which follows from the analytic argument above.

## Relationship to prior work
Shuldiner and Oldford develop general generating-function and moment methods for sums of potentially dependent Bernoulli indicators [1], motivating direct study of the locally dependent transition indicators here. Kim and Park prove an independent-Bernoulli representation for the number of **success runs conditioned on a fixed number of successes** [2, Theorem 2], not for the unconditional count of **both** change types studied here. Conditioning and removing that conditioning do not preserve real-rootedness or independent-summand factorizations in general. Kim's one-dimensional Potts-model zeros concern a **periodic** transfer-trace partition function [3], unlike the open-chain two-endpoint matrix product and left-half-plane zero theorem established here. These works supply relevant context, not an asserted proof of the present conclusion.

## Limitations
The result is finite-sample and assumes independent identically distributed binary symbols with positive probabilities; neither Markov dependence nor multiletter alphabets are treated. The degree-two factorization is distributional and need not correspond to independent functions of the observed bit sequence. No explicit closed formula for every quadratic-factor probability is supplied; existence follows from zero location. A relevant classical factorization of the open-chain partition polynomial could remain unindexed; the relationship to earlier one-dimensional spin-chain literature warrants further bibliographic scrutiny. Self-review is not independent mathematical validation.

## References
[1] P. Shuldiner and R. W. Oldford, *Bernoulli Sums: The only random variables that count*, arXiv:2110.02363, first submitted October 5, 2021. https://arxiv.org/abs/2110.02363

[2] S. Kim and C. J. Park, *An Asymptotic Conditional Test of Independence in Bernoulli Sequences Using the Number of Runs Given the Number of Successes*, 2019. https://www.researchgate.net/publication/334637316_An_Asymptotic_Conditional_Test_of_Independence_in_Bernoulli_Sequences_Using_the_Number_of_Runs_Given_the_Number_of_Successes

[3] S.-Y. Kim, *Fisher zeros and Potts zeros of the \(Q\)-state Potts model for nonzero external magnetic field*, arXiv:cond-mat/0307010, 2003. https://arxiv.org/abs/cond-mat/0307010
