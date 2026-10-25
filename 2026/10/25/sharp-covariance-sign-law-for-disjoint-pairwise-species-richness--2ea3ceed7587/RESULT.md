# Sharp covariance sign law for disjoint pairwise species-richness surveys

## Finding
Consider a finite census of \(N\ge4\) **labeled individuals** partitioned among \(S\ge1\) species with positive integer abundances \(a_1,\ldots,a_S\) and \(\sum_i a_i=N\). Choose two **disjoint, ordered** uniform samples \(A,B\) of two individuals each: choose \(A\) uniformly among the two-subsets, then \(B\) uniformly among two-subsets of the remaining individuals. Let \(K_A,K_B\) be their represented-species counts and let \((z)_r=z(z-1)\cdots(z-r+1)\) be the falling factorial. Define the census collision totals \(T_2=\sum_i(a_i)_2\) and \(T_3=\sum_i(a_i)_3\). Then
\[
\operatorname{Cov}(K_A,K_B)=\frac{\frac{4N-6}{N(N-1)}T_2^2-4T_3-2T_2}{(N)_4}.
\]
This provides a necessary and sufficient census-level sign test. In particular, if all species are singletons or doubletons and exactly \(d\) species are doubletons, then for \(d>0\)
\[
\operatorname{sgn}\operatorname{Cov}(K_A,K_B)=\operatorname{sgn}\bigl((4N-6)d-N(N-1)\bigr).
\]
For \(d=0\), the covariance is zero. Thus an explicit *sharp* doubleton-frequency boundary holds for every \(N\ge4\), not just asymptotically.

For **every** \(N\ge4\), some census with \(N\) individuals gives strictly positive covariance (take \(\lfloor N/2\rfloor\) doubleton species and, for odd \(N\), one singleton), while another gives strictly negative covariance (take one doubleton and \(N-2\) singletons). Four individuals are the minimum possible population allowing two disjoint two-individual samples and both signs. At \(N=4\), profile \((2,2)\) gives covariance \(2/9\) and correlation \(+1\); profile \((3,1)\) gives covariance \(-1/4\) and correlation \(-1\). With \((2,2)\), both sample richnesses always agree; with \((3,1)\), their sum is deterministically three. Hence assuming independence between the two samples can either **halve the correct variance** of their mean (profile \((2,2)\)) or report a positive variance when the true variance is zero (profile \((3,1)\)).

A general exact joint covariance formula holds for all sample sizes \(m,n\ge1\) with \(m+n\le N\). Write \(u_i(m)=\binom{N-a_i}{m}/\binom Nm\), interpret out-of-range binomial coefficients as zero, and set
\[
q_{ij}(m,n)=\begin{cases}
\displaystyle\frac{\binom{N-a_i}{m+n}}{\binom N{m+n}},&i=j,\\[5pt]
\displaystyle\frac{\sum_{h=0}^{m}\binom{a_j}{h}\binom{N-a_i-a_j}{m-h}\binom{N-m-a_j+h}{n}}{\binom Nm\binom{N-m}{n}},&i\ne j.
\end{cases}
\]
Then
\[
\operatorname{Cov}(K_A,K_B)=\sum_{i=1}^S\sum_{j=1}^S\bigl(q_{ij}(m,n)-u_i(m)u_j(n)\bigr).
\]
The two-pair sign law is a simplification of this exact finite-population joint-distribution identity.

## Assumptions and scope
The census is fixed (not sampled from a superpopulation). Individuals are distinguishable, species labels are fully observed without error, and the two samples are uniformly drawn **without replacement across the two surveys**. When the sizes are general, \(A\) and \(B\) are disjoint uniform subsets of respective sizes \(m,n\), with \(m,n\ge1\) and \(m+n\le N\). This is an individual-based design, not two spatially correlated field quadrats; the term *survey* does not imply independent sampling. The exact sign classification requires the special two-individual sample design. No assumption of independent richness counts is made.

## Proof
For each species \(i\), let \(U_i^A\) indicate its absence from \(A\). Since \(K_A=S-\sum_iU_i^A\) and similarly for \(B\), their covariance is the sum of all absence-indicator covariances. The one-sample absence probability is \(u_i(m)\). For \(i=j\), the union \(A\cup B\) is a uniform \((m+n)\)-subset, giving \(q_{ii}\). For \(i\ne j\), first choose \(h\) individuals of species \(j\) into \(A\), no individuals of species \(i\), and \(m-h\) from the remaining \(N-a_i-a_j\) individuals. The residual available pool that is not species \(j\) has \(N-m-a_j+h\) members; choosing all \(n\) of \(B\) from it produces the stated summand. Summing \(h\), normalizing by \(\binom Nm\binom{N-m}{n}\), and then summing covariances proves the general formula.

For two-individual samples, define \(H_A=2-K_A\), the indicator that the two members of \(A\) are conspecific, and similarly \(H_B\). Consequently \(\operatorname{Cov}(K_A,K_B)=\operatorname{Cov}(H_A,H_B)\). The collision probability is \(\Pr(H_A=1)=T_2/(N)_2\). Counting ordered sequences of four *distinct* individuals whose first two and last two have matching species gives
\[
\Pr(H_A=H_B=1)=\frac{T_2^2-\sum_i(a_i)_2^2+\sum_i(a_i)_4}{(N)_4}.
\]
The identity \((a)_2^2-(a)_4=4(a)_3+2(a)_2\), valid also at small \(a\) by falling-factorial convention, reduces this to \((T_2^2-4T_3-2T_2)/(N)_4\). Subtracting \(T_2^2/(N)_2^2\) and using \((N)_2^2-(N)_4=(4N-6)(N)_2\) gives the displayed covariance law.

When there are exactly \(d\) doubletons and all other species are singletons, \(T_2=2d\) and \(T_3=0\). Substitution gives
\[
\operatorname{Cov}(K_A,K_B)=\frac{4d\bigl((4N-6)d-N(N-1)\bigr)}{N(N-1)(N)_4},
\]
so its sign criterion is exact, including equality. For \(d=1\), \((4N-6)-N(N-1)=-(N-2)(N-3)<0\) when \(N\ge4\). For \(d=\lfloor N/2\rfloor\), the sign is positive, since for even \(N\) the required inequality simplifies to \(N>2\), and for odd \(N\) to \(N>3\). This proves the all-size witnesses and the sharp population-size cutoff. The small examples follow by direct substitution; for \((2,2)\) the two unordered pairs have the same collision status, while for \((3,1)\) exactly one is conspecific, proving correlations \(+1\) and \(-1\) respectively. With one sampled individual per survey, richness is deterministically one, so two sampled individuals are also the smallest nontrivial per-survey size.

## Verification
The standalone `verify.py` uses exact integer combinatorics and `fractions.Fraction`, with no external dependencies. It independently enumerates every disjoint sample pair for all \(60\) integer-partition abundance profiles of census size \(4\) through \(8\) to confirm the closed pair formula; verifies the general covariance sum against full subset enumeration in \(591\) sample-size/profile cases of size up to \(7\); and checks the doubleton sign threshold in \(2595\) parameter combinations through population size \(100\). It also verifies exact values \(2/9,-1/4,-1/36,2/75,-7/75\) for the listed benchmark census profiles. `certificate.json` is the exact output; rerun with `python3 verify.py`. The symbolic counting proof, not finite enumeration, establishes validity at arbitrary sizes.

## Relationship to prior work
Individual-based rarefaction and its hypergeometric sampling basis are classical; Gotelli and Colwell (2001) discuss the fixed-size, no-replacement richness expectation and single-sample variance. Chao and colleagues (2014) develop a rich single-sample rarefaction and extrapolation framework, largely based on with-replacement abundance sampling and single-reference-sample variation. Chao and Lin (2012) study lower bounds on total/shared richness under sampling without replacement, rather than the signed covariance of **two disjoint random subsamples from a single fixed census**. General finite-population hypergeometric theory underlies the counting proof, but the exact two-pair sign threshold, all-census-size two-sided witnesses, and extremal \(N=4\) inference examples were not established in the accessible inspected material. The closest published mathematical-record comparisons concern iid-with-replacement discovery increments or richness–diversity covariance in one sample; these are different random variables and sampling laws. See `REVIEW.md` for the self-review originality comparison and limitations.

## Limitations
The formulas apply to a *known fixed census*, not an unobserved species pool or stochastic spatial process. Fully independent resampling **with** replacement has zero cross-sample covariance, and two field quadrats may have additional habitat-driven dependence not represented here. The pairwise sharp sign criterion does not characterize all general \((m,n)\) cases. No estimate of ecological species-abundance uncertainty is made. Existing work may contain an equivalent formula under finite-population \(U\)-statistics or dual-sampling terminology; independent literature and scientific assessment remain outstanding.

## References
1. N. J. Gotelli and R. K. Colwell (2001), *Quantifying biodiversity: procedures and pitfalls in the measurement and comparison of species richness*, Ecology Letters **4**, 379–391. DOI: 10.1046/j.1461-0248.2001.00230.x. Full-text author copy: https://www.robertkcolwell.org/publications/7086.pdf.
2. A. Chao and C.-W. Lin (2012), *Nonparametric lower bounds for species richness and shared species richness under sampling without replacement*, Biometrics **68**, 912–921. DOI: 10.1111/j.1541-0420.2011.01739.x.
3. A. Chao et al. (2014), *Rarefaction and extrapolation with Hill numbers: a framework for sampling and estimation in species diversity studies*, Ecological Monographs **84**, 45–67. DOI: 10.1890/13-0133.1. Full-text author copy: https://www.robertkcolwell.org/publications/6842.pdf.
