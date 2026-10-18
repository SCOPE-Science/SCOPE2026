# A sharp infinite-divisibility cutoff for maxima of geometric samples

## Finding
Let \(X_1,\ldots,X_n\) be independent zero-based geometric variables with \(\Pr(X_i=k)=(1-q)q^k\), where \(n\ge1\) is an integer, \(0<q<1\), and \(k\in\{0,1,2,\ldots\}\). Let \(M_n=\max_{1\le i\le n}X_i\).

**Theorem.** The law of \(M_n\) is infinitely divisible under convolution **if and only if** \(n\in\{1,2\}\), independently of \(q\). For \(n=2\) it is compound Poisson, with probability-generating function and exact jump intensities
\[
G_2(z)=\frac{(1-q)^2(1+qz)}{(1-qz)(1-q^2z)},\qquad
\nu_k=\frac{q^{2k}+[1+(-1)^{k-1}]q^k}{k}\quad(k\ge1).
\]
Thus all \(\nu_k\) are strictly positive, their sum is \(-2\log(1-q)\), and \(G_2(z)=\exp\bigl(\sum_{k\ge1}\nu_k(z^k-1)\bigr)\). For every \(n\ge3\), the coefficient of \(z^2\) in \(\log G_n(z)\) is strictly negative:
\[
[z^2]\log G_n(z)=\frac{2(1+q+q^2)^n-(1+q)^{2n}-1}{2}<0.
\]
This is a sharp sample-size threshold in the integer-resilience subfamily of the exponentiated geometric, also called discrete generalized exponential type II, family.

## Assumptions and scope
The claim is exact for every integer sample size \(n\ge1\) and every real \(0<q<1\), with independent identically distributed input variables. The convention is zero-based geometric support \(\mathbb N_0\). Infinite divisibility means that for each positive integer \(m\) the distribution can be expressed as an \(m\)-fold convolution of some probability measure on the real line. No claim is made about noninteger exponentiation parameters, heterogeneous geometric variables, or maxima of other parent laws. Degenerate endpoints \(q=0\) and \(q=1\) are excluded: the latter does not define the stated geometric probability law.

## Proof
**1. Exact probabilities.** The elementary maximum CDF is
\[
\Pr(M_n\le k)=(1-q^{k+1})^n,\qquad k\ge0,
\]
with the value zero at \(k=-1\). Hence
\[
p_k:=\Pr(M_n=k)=(1-q^{k+1})^n-(1-q^k)^n,
\qquad p_0=(1-q)^n>0.
\]
Write \(G_n(z)=\sum_{k\ge0}p_kz^k\), analytic for \(|z|<1/q\). In particular \(G_n(0)=p_0>0\), so its analytic logarithm near zero is well-defined.

**2. Positive compound-Poisson cases.** For \(n=1\),
\[
G_1(z)=\frac{1-q}{1-qz}
=\exp\left(\sum_{k\ge1}\frac{q^k}{k}(z^k-1)\right).
\]
For \(n=2\), the exact coefficient formula from Step 1 simplifies to \(p_k=(1-q)q^k[2-(1+q)q^k]\), so summing the geometric series gives
\[
G_2(z)=(1-q)\left(\frac{2}{1-qz}-\frac{1+q}{1-q^2z}\right)
=\frac{(1-q)^2(1+qz)}{(1-qz)(1-q^2z)}.
\]
Expanding three ordinary logarithms in a neighborhood of zero yields
\[
\log G_2(z)=2\log(1-q)+\sum_{k\ge1}\frac{q^{2k}+q^k[1+(-1)^{k-1}]}{k}\,z^k.
\]
For odd \(k\), the numerator is \(q^{2k}+2q^k\), and for even \(k\) it is \(q^{2k}\); both are positive. Evaluating at \(z=1\) (permitted since \(q<1\)) gives \(\sum_{k\ge1}\nu_k=-\log G_2(0)=-2\log(1-q)<\infty\). Therefore the displayed exponential is the probability-generating function of a compound-Poisson sum with independent Poisson counts of jumps of size \(k\), and \(M_2\) is infinitely divisible.

**3. Negative quadratic logarithmic coefficient for every larger sample.** By Step 1, with \(A=1+q\), \(B=1+q+q^2\),
\[
\frac{p_1}{p_0}=A^n-1,\qquad
\frac{p_2}{p_0}=B^n-A^n.
\]
Consequently, writing \(\log G_n(z)=\log p_0+\lambda_1z+\lambda_2z^2+O(z^3)\), we have
\[
\lambda_1=A^n-1>0,\qquad
2\lambda_2=2B^n-A^{2n}-1.
\]
Set \(C=A^2\) and \(D_n=C^n+1-2B^n=-2\lambda_2\). Direct expansion gives
\[
D_3=q^2(3+6q+3q^2-q^4)>0,
\]
because \(0<q<1\). A direct rearrangement gives, for every \(n\ge3\),
\[
D_{n+1}=C D_n+2qB^n-(2q+q^2).
\]
Since \(B^n\ge B=1+q+q^2\), the final correction is at least \(q^2+2q^3>0\). Induction proves \(D_n>0\) for all integers \(n\ge3\). Thus \(\lambda_2=-D_n/2<0\).

**4. Why negativity rules out ordinary infinite divisibility.** Suppose \(M_n\), which has \(\Pr(M_n=0)>0\), were the sum of \(m\) independent identically distributed real variables with common law \(H_m\). Because the sum is nonnegative, \(H_m\) cannot assign positive probability to negative values (otherwise all \(m\) could be negative). Hence its variables are nonnegative. Positivity of \(\Pr(M_n=0)\) then forces \(\Pr(H_m=0)=p_0^{1/m}>0\). If \(H_m\) charged a noninteger nonnegative value, the event that one summand lies in a small interval disjoint from integers and all others equal zero would give noninteger positive probability for \(M_n\), a contradiction. So \(H_m\) is supported on \(\mathbb N_0\).

Its generating function must therefore be the branch \(G_n(z)^{1/m}\) analytic near zero with positive constant coefficient. Its second Taylor coefficient is
\[
[z^2]G_n(z)^{1/m}=p_0^{1/m}\left(\frac{\lambda_2}{m}+\frac{\lambda_1^2}{2m^2}\right).
\]
For sufficiently large positive integers \(m\), this coefficient is negative since \(\lambda_2<0\). No probability-generating function can have a negative coefficient. Thus \(M_n\) is not infinitely divisible for \(n\ge3\). Combining Steps 2--4 completes the proof.

## Verification
The accompanying standard-library script `verify.py` uses exact rational arithmetic. It checks 1,008 distribution identities, rational generating-function coefficients, negative quadratic-log obstructions and the induction recurrence across a finite diagnostic parameter grid. The exhaustive analytical sign argument above, not this finite grid, proves the theorem for every real \(q\in(0,1)\) and every integer \(n\ge1\). Run with `python verify.py`.

## Relationship to prior work
Badiella, del Castillo and Puig (2023) prove preservation of log-concavity and ultra-log-concavity under discrete order statistics. Geometric distributions are log-concave, and their theorem consequently covers the maxima here, but their preservation theorem concerns probability-mass shape, not additive infinite divisibility. The exact integer-resilience family here appears under the aliases **exponentiated geometric** and **discrete generalized exponential of the second type (DGE2/DGEII)**; see Nekoukhou, Alamatsaz and Bidram (2013) and Chakraborty and Gupta (2015). Bidram, Roozegar and Nekoukhou (2016) establish that a broader exponentiated generalized geometric family is *not infinitely divisible in general*, using a different parameter example; their inspected statement does not provide the universal sharp integer-sample cutoff or the positive two-sample jump law. Geng and Xia (2020) establish an infinite-divisibility classification for the different Conway--Maxwell--Poisson family and explain the compound-Poisson criterion.

## Limitations
This theorem neither characterizes noninteger DGEII exponents nor asserts uniqueness in the literature. A full-text comparison with the original DGEII paper and the exponentiated-geometric paper remains incomplete because those publications were not fully accessible through the sources available for inspection; they are pertinent originality risks. The result is a scientific claim with ordinary reproducibility checks, not independently certified. No finite computation can prove the all-real-parameter statement by itself.

## References
1. L. Badiella, J. del Castillo and P. Puig, *Ultra log-concavity of discrete order statistics*, Statistics & Probability Letters 201 (2023), 109900, doi:10.1016/j.spl.2023.109900 (available online 26 June 2023).
2. V. Nekoukhou, M. H. Alamatsaz and H. Bidram, *Discrete generalized exponential distribution of a second type*, Statistics 47 (2013), 876--887, doi:10.1080/02331888.2011.633707.
3. S. Chakraborty and R. D. Gupta, *Exponentiated geometric distribution: Another generalization of geometric distribution*, Communications in Statistics--Theory and Methods 44 (2015), 1143--1157, doi:10.1080/03610926.2012.763090.
4. H. Bidram, R. Roozegar and V. Nekoukhou, *Exponentiated generalized geometric distribution: A new discrete distribution*, Hacettepe Journal of Mathematics and Statistics 45 (2016), 1767--1779, doi:10.15672/HJMS.20159013119.
5. X. Geng and A. Xia, *When Is the Conway--Maxwell--Poisson Distribution Infinitely Divisible?*, 2020, arXiv:2011.04852.
6. S. Chakraborty, *Generating discrete analogues of continuous probability distributions: A survey of methods and constructions*, Journal of Statistical Distributions and Applications (2015), doi:10.1186/s40488-015-0028-6.
