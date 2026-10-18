# A sample-size-invariant cherry–external-length covariance in Kingman's coalescent

## Finding

In the standard Kingman coalescent of every integer sample size \(n\ge4\), let \(C_n\) be the number of terminal cherries (unordered pairs of sample leaves sharing an immediate parent), and let \(L_n\) be the total length of the terminal/external branches in coalescent time units, with each pair of active lineages merging at rate one. Then

\[
\boxed{\operatorname{Cov}(C_n,L_n)=-\frac29}\qquad(n\ge4).
\]

The constant is independent of sample size. More precisely, let \(S_{n,k}\) be the count of ancestral blocks containing exactly one sampled leaf immediately after the coalescent first reaches \(k\) blocks. For every \(2\le k\le n\) and \(n\ge4\),

\[
\boxed{\operatorname{Cov}(C_n,S_{n,k})
=-\frac{k(k-1)(n-k)(n-k-1)}{3(n-1)(n-2)(n-3)}.}
\]

Thus the stage covariance is strictly negative at all \(2\le k\le n-2\), and zero at \(k=n-1,n\). For \(n=2,3\), \(C_n=1\) identically and the covariance with external length is zero. Together with the known asymptotic variances of the two statistics, the exact identity yields

\[
\operatorname{Corr}(C_n,L_n)\sim-\frac{\sqrt5}{6\sqrt{\log n}}\quad(n\to\infty).
\]

## Assumptions and scope

Start with \(n\) labeled singleton ancestral lineages. When \(k\) lineages remain, each unordered pair merges at rate \(1\), so the independent waiting time \(\tau_k\) is exponential with mean \(2/[k(k-1)]\). Which pair merges is independent of the waiting times and uniform among the \(\binom{k}{2}\) pairs. The genealogy is binary almost surely. A cherry is created precisely when two still-singleton lineages merge; its status as a cherry remains fixed. A singleton lineage has one original descendant. Set \(S_k=S_{n,k}\), and let \(H_k\) count cherries already created by the stage with \(k\) lineages, so \(H_n=0\) and \(C_n=H_1\). Then \(L_n=\sum_{k=2}^n S_k\tau_k\). All expectations and covariances are unconditional under this Kingman model.

For nonnegative integer \(j\), denote the falling factorial by \((x)_{\underline j}=x(x-1)\cdots(x-j+1)\), with \((x)_{\underline0}=1\). Here the expression is a notation definition, not a rising factorial.

## Proof

**1. Singleton factorial moments.** For \(j\in\{1,2,3\}\) and \(n\ge4\), track an ordered set of \(j\) designated original leaves. Conditional on all surviving as singleton lineages when \(\ell\) lineages remain, their probability of surviving the next merger is \(\binom{\ell-j}{2}/\binom\ell2\). Telescoping over \(\ell=n,n-1,\ldots,k+1\) yields

\[
F_j(k):=\mathbb E[(S_k)_{\underline j}]
=\frac{(k)_{\underline j}(k-1)_{\underline j}}{(n-1)_{\underline j}}
\quad(1\le j\le3,\ 2\le k\le n).
\]

The right side is interpreted as zero if \(k-1<j\). In particular, \(F_1(k)=k(k-1)/(n-1)\).

**2. Cherries still to come.** For two designated distinct surviving singleton lineages, let \(q_k\) be the probability that they merge with each other before either merges with any other lineage. At \(k=3\) this is \(q_3=1/3\). For \(k\ge4\), a first-step decomposition gives

\[
q_k=\frac1{\binom k2}+\frac{\binom{k-2}2}{\binom k2}q_{k-1}
=\frac{2}{3(k-1)}.
\]

The displayed closed form is valid for all \(k\ge3\). Consequently, for a history at stage \(k\ge3\),

\[
\mathbb E[C_n\mid\mathcal F_k]
=H_k+\frac{2}{3(k-1)}\binom{S_k}{2}.
\]

No cherry can be created at the final \(2\to1\) merger for \(n\ge3\), since two surviving original singletons cannot be the only two blocks then. In particular, \(C_n=H_2\), and for \(k=2\), \(\mathbb E[S_k C_n]=\mathbb E[S_kH_k]\). At \(k=n\), the displayed conditional expectation gives \(\mathbb E[C_n]=\binom n2[2/(3(n-1))]=n/3\).

**3. Mixed cherry-stage moment.** Write \(z_k=\mathbb E[S_kH_k]\), and let \(D=(n-1)(n-2)(n-3)\). If \(d\in\{0,1,2\}\) singleton lineages participate in the next merger, then \(S_{k-1}=S_k-d\), and \(H_{k-1}=H_k+\mathbf1_{\{d=2\}}\). Direct conditional counting of pairs gives, for \(k=3,\ldots,n\),

\[
z_{k-1}=\frac{k-2}{k}z_k+
\frac{F_3(k)}{k(k-1)},\qquad z_n=0.
\]

The unique solution, checked by substitution into this recursion and its terminal value, is

\[
z_k=\frac{k(k-1)}3
\left[1-\frac{(k-1)(k-2)(k-3)}{D}\right]
\qquad(2\le k\le n).
\]

For \(k\ge3\), use the preceding conditional expectation and \(S_k\binom{S_k}{2}=\bigl((S_k)_{\underline3}+2(S_k)_{\underline2}\bigr)/2\) to obtain

\[
\mathbb E[S_kC_n]=z_k+\frac{F_3(k)+2F_2(k)}{3(k-1)}.
\]

For \(k=2\) its second term vanishes (both factorial moments zero) and the same identity still holds. Substituting the factorial-moment formulas, \(z_k\), \(\mathbb E[S_k]=F_1(k)\), and \(\mathbb E[C_n]=n/3\), then factoring the numerator yields

\[
\operatorname{Cov}(C_n,S_k)=
-\frac{k(k-1)(n-k)(n-k-1)}{3D}.
\]

This proves the full signed stage profile, including the endpoints.

**4. Integrating along waiting times.** Because \(C_n\) depends only on which pairs merged and is independent of all \(\tau_k\),

\[
\operatorname{Cov}(C_n,L_n)
=\sum_{k=2}^n\frac2{k(k-1)}\operatorname{Cov}(C_n,S_k)
=-\frac2{3D}\sum_{k=2}^{n-2}(n-k)(n-k-1).
\]

The sum equals \(D/3\), by the falling-factorial summation identity \(\sum_{j=2}^{n-2}j(j-1)=(n-2)(n-1)(n-3)/3\). Hence the covariance equals \(-2/9\).

**5. Correlation asymptotics.** Established marginal results give \(\operatorname{Var}(C_n)=2n/45\) for \(n\ge5\) and \(\operatorname{Var}(L_n)\sim8\log n/n\) (the latter in Janson–Kersting). Their product has square root asymptotic to \(4\sqrt{\log n/45}\). Dividing \(-2/9\) by this expression establishes the stated correlation asymptotic; no joint central limit theorem is asserted.

## Verification

The included pure-Python `verify_covariance.py` independently propagates the exact joint distribution of singleton counts and cherry counts through all pair-merger events and carries the accumulated conditional mean of the external length. It performs exact-fraction computations for every \(4\le n\le23\), checking \(\mathbb E[C_n]=n/3\), \(\mathbb E[L_n]=2\), \(\operatorname{Cov}(C_n,L_n)=-2/9\), and the cherry variance (for \(n\ge5\)). This program does not assume the derived covariance formula inside its transition recurrence. It is a finite test, not an infinite proof; the preceding algebra proves the all-\(n\) identity.

The stage formula was separately reduced by symbolic factorization and tested through \(n=20\) with exact rational falling-factorial moments. The only rate normalization is that each pair merges at rate one; rescaling coalescent time by a constant rescales the length and covariance by that constant.

## Relationship to prior work

The standard Kingman model and total external length appear in Janson and Kersting, *The external lengths in Kingman's coalescent* (arXiv:1004.5011, original submission 2010-04-28), which studies external-length moments, limiting distributions, and a singleton-count urn chain; the inspected paper does not treat cherries or their mixed moment with length. Disanto and Wiehe, *Exact enumeration of cherries and pitchforks in ranked trees under the coalescent model* (arXiv:1112.1295, originally submitted 2011-12-06), provides cherry distribution methods but explicitly restricts attention to topology rather than branch lengths. Dahmer and Kersting, *The internal branch lengths of the Kingman coalescent* (arXiv:1303.4562, originally submitted 2013-03-19), studies lengths indexed by descendant counts, not the cherry-count cross-moment.

François and Mioland, *Gaussian approximations for phylogenetic branch length statistics under stochastic models of biodiversity* (2007, DOI 10.1016/j.mbs.2007.01.005), analyzes **total height of cherries** and external branch length: cherry height is a different statistic from the **number** of cherries here. Only bibliographic material and the abstract could be confirmed, so complete coverage in that paper cannot be excluded. The contribution claimed here is precisely the finite-stage cross-covariance profile and the sample-size-invariant cross-covariance, not either marginal formula or a general assertion that coalescent statistics correlate.

## Limitations

The theorem assumes the constant-population, contemporaneously sampled Kingman binary coalescent with pairwise merger rate one, and is not stated for varying population sizes, multiple-merger coalescents, or conditioned reconstructed species trees. For \(n=2,3\) the cherry count is constant and the covariance is zero; the displayed rational stage formula is only defined for \(n\ge4\). An equivalent joint moment may have appeared in older genealogical literature not accessible in full; literature comparison does not establish absolute priority. The correlation asymptotic uses previously established marginal variance results and implies decorrelation, not asymptotic independence.

## References

1. S. Janson and G. Kersting, *The external lengths in Kingman's coalescent*, arXiv:1004.5011 (initial posting 2010-04-28); *Electronic Journal of Probability* **16** (2011), 2203–2218. https://arxiv.org/abs/1004.5011 .
2. F. Disanto and T. Wiehe, *Exact enumeration of cherries and pitchforks in ranked trees under the coalescent model*, arXiv:1112.1295 (initial posting 2011-12-06). https://arxiv.org/abs/1112.1295 .
3. I. Dahmer and G. Kersting, *The internal branch lengths of the Kingman coalescent*, arXiv:1303.4562 (initial posting 2013-03-19). https://arxiv.org/abs/1303.4562 .
4. O. François and C. Mioland, *Gaussian approximations for phylogenetic branch length statistics under stochastic models of biodiversity*, *Mathematical Biosciences* **209** (2007), 108–123. https://doi.org/10.1016/j.mbs.2007.01.005 .
