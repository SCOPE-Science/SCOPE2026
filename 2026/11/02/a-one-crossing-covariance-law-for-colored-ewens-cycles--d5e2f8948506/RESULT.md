# A one-crossing covariance law for colored Ewens cycles

## Finding
Fix a population with colors \(1,\ldots,q\), with \(n_i\) labeled objects of color \(i\), and sample a permutation with weight proportional to \(\theta^{K}\) where \(\theta>0\) and \(K\) is its number of cycles. For a nonzero vector \(\mathbf a=(a_1,\ldots,a_q)\), write \(C_{\mathbf a}\) for the count of cycles using exactly \(a_i\) objects of each color. For distinct feasible types \(\mathbf a\) and \(\mathbf b\) that can appear simultaneously, put \(r=\sum_i a_i\), \(s=\sum_i b_i\), and use falling factorials \((x)_{\underline k}=\prod_{j=0}^{k-1}(x-j)\). Then

\[
\frac{\operatorname{Cov}(C_{\mathbf a},C_{\mathbf b})}
{\mathbb EC_{\mathbf a}\,\mathbb EC_{\mathbf b}}
=F_{\mathbf a,\mathbf b}\,G_{r,s}(\theta)-1,
\quad F_{\mathbf a,\mathbf b}=\prod_{i=1}^q\frac{(n_i)_{\underline{a_i+b_i}}}{(n_i)_{\underline{a_i}}(n_i)_{\underline{b_i}}},
\quad G_{r,s}(\theta)=\prod_{j=1}^{s}\frac{\theta+n-j}{\theta+n-r-j}.
\]

The normalized covariance is strictly decreasing in the bias \(\theta\). Disjoint color supports give positive covariance at every positive bias; overlapping supports allow at most one positive-to-negative crossing, with the precise existence test \(F_{\mathbf a,\mathbf b}G_{r,s}(0+)>1\). At equality in that test the covariance is negative for every positive \(\theta\).

For \(n=2m\), \(m\ge3\), with exactly \(m\) red and \(m\) blue labels, let \(X\) count three-cycles with two red labels and one blue label, and let \(Y\) count three-cycles with one red and two blue labels. Their covariance has a unique zero \(\theta_m>0\), is positive below that zero, and negative above it, with

\[
\theta_m=\frac m4+\frac54+O(m^{-1})=\frac n8+\frac54+O(n^{-1}).
\]

For each fixed \(\gamma>0\), at \(\theta=\gamma n\) we obtain the signed macroscopic profile

\[
\lim_{n\to\infty}\frac{\operatorname{Cov}(X,Y)}n
=\frac{\gamma^2(1-8\gamma)}{64(1+\gamma)^7}.
\]

## Assumptions and scope
The colors are fixed deterministic labels, not random independent colors after permutation sampling. The law is the ordinary Ewens law on permutations of \(n\) labels with mass \(\theta^{K}/(\theta)_{\overline n}\), where the rising factorial is \((x)_{\overline k}=\prod_{j=0}^{k-1}(x+j)\). The two signatures are distinct, nonzero, and simultaneously feasible: \(a_i+b_i\le n_i\) for all \(i\). Therefore \(n\ge r+s\), all expectations used in the normalization are strictly positive, and the displayed formulas are finite for \(\theta>0\). For the balanced specialization \(m\ge3\) and the parameter \(\theta_m\) is the unique positive zero at each such \(m\).

## Proof
**Marked-cycle factorial moments.** For a fixed set of \(r\) labeled objects, requiring it to form a single permutation cycle permits \((r-1)!\) cyclic arrangements, supplies a factor \(\theta\), and leaves an Ewens permutation on the other \(n-r\) labels. Therefore

\[
\mathbb E C_{\mathbf a}
=\theta\frac{(r-1)!}{\prod_i a_i!}\prod_i(n_i)_{\underline{a_i}}\;
\frac{(\theta)_{\overline{n-r}}}{(\theta)_{\overline n}}.
\]

For two distinct, separately marked cycle types, the selected object sets must be disjoint. Repeating the argument gives

\[
\mathbb E[C_{\mathbf a}C_{\mathbf b}]
=\theta^2\frac{(r-1)!(s-1)!}{\prod_i a_i!b_i!}
\prod_i(n_i)_{\underline{a_i+b_i}}\;
\frac{(\theta)_{\overline{n-r-s}}}{(\theta)_{\overline n}}.
\]

Dividing by the product of the marginal expectations cancels the combinatorial prefactors and gives \(FG\). The rising-factorial quotient simplifies to \(G\) as stated; its formula is symmetric in \(r,s\) despite the displayed asymmetric indexing.

**Single-crossing property.** Every factor in \(G\) is larger than one and strictly decreases with \(\theta\), since \((\theta+n-j)/(\theta+n-r-j)=1+r/(\theta+n-r-j)\). Thus \(G\) strictly decreases to one. Each factor in \(F\) is in \((0,1]\), and it is strictly below one exactly when \(a_i b_i>0\) for at least one color. If the supports are disjoint then \(F=1\), giving strictly positive covariance. Otherwise \(F<1\), so at large \(\theta\) the covariance is negative; monotonicity establishes the stated sign test and uniqueness of a zero if the zero-bias limit is above one. If the zero-bias limit equals one the strict decrease makes all positive-bias values less than one.

**Balanced opposing mixed cycles.** Taking \(\mathbf a=(2,1)\), \(\mathbf b=(1,2)\), \(n_1=n_2=m\) yields

\[
\mathbb EX=\mathbb EY=\frac{\theta m^2(m-1)}{(\theta+2m-3)(\theta+2m-2)(\theta+2m-1)},
\]

\[
R_m(\theta):=\frac{\mathbb E[XY]}{\mathbb EX\mathbb EY}
=\left(\frac{m-2}{m}\right)^2
\frac{(\theta+2m-1)(\theta+2m-2)(\theta+2m-3)}{(\theta+2m-4)(\theta+2m-5)(\theta+2m-6)}.
\]

At \(m=3\), \(R_m(0+)=+\infty\); for every \(m\ge4\), direct simplification gives

\[
R_m(0+)-1=\frac{2m^3+5m^2-25m+6}{2m^2(m-3)(2m-5)}>0.
\]

The numerator is already positive at \(m=4\) and strictly increasing thereafter. Moreover \(R_m(+\infty)=(m-2)^2/m^2<1\). Thus the crossing exists and is unique for every \(m\ge3\). For bounded real \(c\), a rational Taylor expansion uniformly on bounded \(c\)-sets gives

\[
R_m(m/4+c)-1=\frac{20-16c}{9m^2}+O(m^{-3}).
\]

By strict monotonicity the unique zero lies in a bounded \(c\)-interval around \(5/4\), and the expansion plus the nonzero leading derivative yields \(c=5/4+O(m^{-1})\).

**Macroscopic limit.** With \(n=2m\) and \(\theta=\gamma n\), for fixed \(\gamma>0\), direct expansion of the exact ratio gives

\[
n(R_m(\gamma n)-1)\longrightarrow \frac9{1+\gamma}-8,
\qquad \frac{\mathbb EX}{n}\longrightarrow\frac{\gamma}{8(1+\gamma)^3}.
\]

Since \(\operatorname{Cov}(X,Y)=(\mathbb EX)^2(R_m-1)\), the claimed signed limit follows.

## Verification
The companion standalone `checker.py` reproduces cycle counts directly from all permutations on six and eight labels (respectively \(720\) and \(40320\) objects) at four rational bias parameters, and checks exact rational expectations, mixed moments, covariance-ratio identities and monotonicity of the ratio across further integer population sizes. It prints `PASS 622 assertions permutation_cases= 41040`. The independent exhaustive finite comparison checks formulas but is not a proof for unbounded \(m\); the marked-cycle argument and monotonic algebra are the general proof. The Taylor coefficients were also reconstructed symbolically from the displayed rational function.

## Relationship to prior work
Dello Schiavo and Quattrocchi (arXiv:2309.11292, version 1 dated 20 September 2023) introduce the polychromatic Ewens framework. Their Lemma 4.3 and Proposition 4.4 give the conditional fixed-color law used here; the later version's Proposition 4.5 gives an even more general generating function, which already mathematically determines all joint moments. This result does **not** claim originality for the colored law, moments obtainable by differentiation, or Ewens cycle enumeration. The proposed incremental contribution is the strict one-crossing sign classification for every pair of feasible different color signatures, the support-disjoint positivity dichotomy, and the exact balanced mixed-cycle transition with sharp location and limiting signed profile. A previously published extraction of these features from the generating function has not been excluded absolutely. Strahov's refined Ewens model has color-class-specific mutation rates and was compared as a related, not identical, construction.

## Limitations
This is a result about covariance signs for **distinct** cycle signatures under one common Ewens weight and a deterministic fixed color population. It does not assert stochastic independence, negative association of all cycles, covariance signs for identically typed pairs, or fluctuations under other random-partition models. Full historical priority remains uncertain; independent mathematical checking has not been performed.

## References
1. L. Dello Schiavo and F. Quattrocchi, *Multivariate Dirichlet Moments and a Polychromatic Ewens Sampling Formula*, arXiv:2309.11292v1 (first public 2023-09-20), Section 4, especially Lemma 4.3 and Proposition 4.4. https://arxiv.org/html/2309.11292v1
2. L. Dello Schiavo and F. Quattrocchi, *Polychromatic Partitions, Kingman Theory, and Ewens Sampling Formula*, arXiv:2309.11292v2 (revised 2026-08-30), Section 4 and Proposition 4.5. https://arxiv.org/html/2309.11292v2
3. E. Strahov, *A refinement of the Ewens sampling formula*, arXiv:2403.05077v1 (2024-03-08), related model. https://arxiv.org/abs/2403.05077
