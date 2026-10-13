# A sharp two-draw infinite-divisibility cutoff for geometric sample maxima

## Finding
For every integer \(m\ge1\) and parameter \(0<q<1\), let \(X_1,\ldots,X_m\) be independent, identically distributed nonnegative geometric random variables with \(\Pr(X_i=k)=(1-q)q^k\), for integer \(k\ge0\), and set \(M_m=\max_{1\le i\le m}X_i\). Then **\(M_m\) is infinitely divisible under ordinary addition on the nonnegative integers if and only if \(m\le2\)**. For two observations its compound-Poisson jump intensities are explicit:
\[
\nu_k=\frac{q^{2k}+(1+(-1)^{k+1})q^k}{k}>0\qquad(k=1,2,\ldots).
\]
For every integer \(m\ge3\), the quadratic Taylor coefficient in the logarithm of the probability-generating function is strictly negative; in particular, no such distribution is ordinarily infinitely divisible.

## Assumptions and scope
Infinite divisibility means that, for every positive integer \(r\), the law equals the convolution of \(r\) identical laws on \(\mathbb Z_{\ge0}\). The geometric law includes zero in its support. This is **ordinary additive**, not max-geometric or max-infinite divisibility. The conclusion holds for all \(0<q<1\) and all positive integers \(m\); it does not assert anything for an arbitrary real exponent outside the sample-maximum construction.

## Proof
Write \(G_m(z)=\mathbb E z^{M_m}\) for the probability-generating function. Independence gives, for every integer \(k\ge0\),
\[
\Pr(M_m\le k)=(1-q^{k+1})^m,
\qquad \Pr(M_m=k)=(1-q^{k+1})^m-(1-q^k)^m.
\]
In particular \(p_0=(1-q)^m>0\). The discrete Lévy–Khintchine criterion says that a nonnegative-integer-valued law with positive mass at zero is infinitely divisible if and only if its generating function has the compound-Poisson representation
\[
G(z)=\exp\!\biggl(\sum_{k\ge1}\nu_k(z^k-1)\biggr),
\quad\nu_k\ge0,\quad\sum_{k\ge1}\nu_k<\infty.
\]
This standard equivalence is recalled in Geng and Xia (2020), Section 2.1. Consequently, every positive-order coefficient of the analytic Taylor series \(\log G_m(z)\) around zero must be nonnegative for infinite divisibility.

For \(m=1\), \(G_1(z)=(1-q)/(1-qz)\). Expanding its logarithm gives \(\nu_k=q^k/k>0\), whose sum is \(-\log(1-q)\). For \(m=2\), direct summation of the mass formula gives
\[
G_2(z)=\frac{(1-q)^2(1+qz)}{(1-qz)(1-q^2z)}.
\]
Expanding the three logarithms gives
\[
\log G_2(z)=2\log(1-q)+\sum_{k\ge1}
\frac{q^{2k}+[1+(-1)^{k+1}]q^k}{k}\,z^k.
\]
All coefficients are positive, and the sum of their values is \(-2\log(1-q)\), as also follows from \(G_2(1)=1\). Thus this is a valid explicit compound-Poisson law, proving infinite divisibility for \(m=2\).

For \(m\ge3\), put \(u=1+q\) and \(v=1+q+q^2\). The first three probabilities satisfy
\[
\frac{p_1}{p_0}=u^m-1,\qquad
\frac{p_2}{p_0}=v^m-u^m.
\]
The coefficient of \(z^2\) in \(\log G_m(z)\) is therefore
\[
c_2=\frac{p_2}{p_0}-\frac12\biggl(\frac{p_1}{p_0}\biggr)^2
=v^m-\frac{u^{2m}+1}{2}.
\]
An exact polynomial identity shows
\[
u^6+1-2v^3=q^2(3+6q+3q^2-q^4)>0\qquad(0<q<1).
\]
Hence \(v^3<(u^6+1)/2\). Since \(x\mapsto x^{m/3}\) is nondecreasing and convex on the positive real axis for \(m\ge3\), Jensen's inequality implies
\[
v^m<\biggl(\frac{u^6+1}{2}\biggr)^{m/3}
\le\frac{u^{2m}+1}{2}.
\]
Thus \(c_2<0\), contradicting the compound-Poisson necessary condition for every \(m\ge3\). Both directions are proved.

## Verification
Run `python3 geometric_verify.py` with Python 3 and no third-party dependencies. It checks 16,830 exact-rational logarithmic quadratic coefficients, 144 independently computed generating-function coefficients, and the exact cubic polynomial identity and strict-sign certificate. The expected final line is `VERIFY_OK log_coeff_exact=16830 generating_coeff_exact=144 positive_cubic_certificate=True`. Finite grids cannot establish the all-parameter result; the preceding analytic argument does.

## Relationship to prior work
The elementary sample-maximum cumulative distribution and related exponentiated-geometric constructions are not claimed new. The older *discrete generalized exponential* model of Nekoukhou, Alamatsaz and Bidram instead has a different normalized mass function on strictly positive integers, so its nondivisibility theorem based on zero mass at zero does **not** apply to the present zero-based sample maximum. Geng and Xia discuss the ordinary additive infinite-divisibility criterion for count laws, showing that among Conway–Maxwell–Poisson laws the geometric and Poisson boundaries have a special role. Their criterion applies here, but their result does not classify sample maxima. A generalized weighted-geometric distribution studied by Najarzadegan and Alamatsaz is not additively infinitely divisible because it has zero mass at zero; that shifted-support obstruction does not apply here since \(\Pr(M_m=0)=(1-q)^m>0\). Geometric-maximum infinite divisibility under max-based operations is also logically different from the ordinary additive convolution property determined here. The contribution is the sharp, complete cutoff at two observations with an explicit compound-Poisson representation.

## Limitations
The argument covers independent identically distributed, zero-based geometric inputs and integer sample sizes; it makes no claim for arbitrary nonintegral exponent parameters, heterogeneous geometric variables, or maximum-based notions of infinite divisibility. The primary 2012 discrete-generalized-exponential article was inspected in full and concerns a different normalized distribution; the complete 2015 exponentiated-geometric article remained unavailable, so unrecognized equivalent prior classification remains a bibliographic risk. Independent audit has not been performed.

## References
1. Xi Geng and Aihua Xia, *When Is the Conway–Maxwell–Poisson Distribution Infinitely Divisible?*, arXiv:2011.04852v1 (first public 2020-11-10); Section 2.1 for the count-law criterion and Theorem 1 for the CMP boundary.
2. Nekoukhou, Alamatsaz and Bidram, *A Discrete Analog of the Generalized Exponential Distribution*, DOI:10.1080/03610926.2011.555044 (full primary text inspected; distinct normalized distribution, especially Definition 2.1 and Theorem 2.5).
3. S. Chakraborty and R. D. Gupta, *Exponentiated Geometric Distribution: Another Generalization of Geometric Distribution*, DOI:10.1080/03610926.2012.763090 (accessible author-hosted material inspected; completeness limited).
4. Najarzadegan and Alamatsaz, *A New Generalization of Weighted Geometric Distribution and its Properties*, *Journal of Statistical Theory and Applications* 16 (2017), 522–546 (full text inspected; different shifted-support family).
