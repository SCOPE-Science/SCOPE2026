# Review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

PASS.

For \(a_n=\Pr(T>n)\), conditioning on how many of the first \(n\) observations fall on atoms gives

\[
a_n=\sum_{k=0}^n\frac{n!}{(n-k)!}e_k(p)q^{n-k}.
\]

The exponential generating function therefore factors as

\[
B(z)=e^{qz}\prod_i(1+p_i z).
\]

The infinite product is legitimate because \(\sum_i p_i<\infty\), and \(B\) is entire also directly from \(0\le a_n\le1\). Its zeros are exactly \(-1/p_i\), with multiplicity, so equality of first-repeat laws forces equality of atomic mass multisets; normalization then recovers the nonatomic mass. The converse is immediate.

The logarithmic coefficient identity

\[
\log B(z)=z+\sum_{r\ge2}(-1)^{r-1}C_rz^r/r
\]

follows from absolute convergence near zero and \(C_r=\sum_i p_i^r\). Exact rational checks reproduce both the survival coefficients and the collision-power coefficients in a mixed example.

For the finite-horizon corollary, \(C_2,\ldots,C_{2m+1}\) are moments \(0,\ldots,2m-1\) of \(\rho=\sum_i p_i^2\delta_{p_i}\). If two candidate \(\rho\)'s each arise from at most \(m\) atoms, their signed difference has support on at most \(2m\) distinct points. Vanishing of the first \(2m\) moments yields an invertible Vandermonde system on that union support, hence equality. Multiplicities are then \(\rho(\{x\})/x^2\).

Adversarial checks considered the purely nonatomic case, repeated equal atom masses, finite and countably infinite atomic supports, and mixed atomic/nonatomic laws. The proof continues to hold in each case.

## Originality

PASS, to the best of our knowledge, with a deliberately narrow novelty claim.

The forward generalized-birthday formulas are classical and are not claimed as new. Stein (1990) explicitly connects Newton identities with a generalized birthday problem. Camarri–Pitman (2000) studies the first repeat time under arbitrary countable unequal discrete probabilities and derives exact and asymptotic formulas. Skorski (2023) and Gates (2026) treat collision probabilities and Rényi-information recovery; Gates explicitly notes that sufficiently many power sums determine a finite probability vector up to permutation.

Searches using combinations of “first repeat time”, “first collision time”, “inverse birthday problem”, “unequal probabilities”, “identify distribution”, “atomic masses”, “dust/nonatomic component”, “collision power sums”, “Newton identities”, and synonymous occupancy formulations did not locate the present complete inverse classification for arbitrary mixed laws or the finite-horizon at-most-\(m\)-atom statement.

The most important residual priority risk is C. Stein's 1990 Technical Report 354. Its bibliographic record and title were verified, but the full report was not available for theorem-level inspection. Because its title directly names Newton identities and the generalized birthday problem, it may contain an explicit finite-discrete inverse statement. For that reason the record does not claim novelty for finite-discrete Newton inversion.

Camarri–Pitman (2000) is another close source. The accessible primary article record confirms that exact first-repeat formulas are derived for arbitrary countable discrete distributions, but theorem-level full text was not successfully inspected from the available copy. This leaves residual uncertainty over whether an inverse corollary is stated there. No concrete evidence of prior coverage of the mixed atomic-plus-nonatomic classification was found.

The recent phrase “inverse birthday problem” is also used for a different task—estimating a population size from counts of distinct observed birthdays—so those results do not cover the present inverse mass-spectrum question.

## Value

PASS.

The result identifies an unexpectedly information-rich one-dimensional statistic: the full law of a single first-repeat stopping time determines every positive atom probability of an arbitrary probability measure. The factorization gives a simple complete observational-equivalence class, while the logarithmic transform makes the relation to all integer collision/Rényi orders explicit. The finite-horizon corollary shows that a bounded number of first-repeat survival probabilities suffices when the number of atoms is bounded, even in the presence of arbitrary nonatomic dust.

## Limitations

This is population-level structural identification, not a stable estimator or minimax-rate theorem. Inverting estimated entire functions can be ill-conditioned, especially for small or clustered atoms. Atom locations and the internal law of the nonatomic component are not identifiable. The finite-horizon \(2m+1\) bound is sufficient rather than claimed optimal. Stein (1990) and the theorem-level content of Camarri–Pitman (2000) leave the principal residual originality uncertainty.

No independent audit has yet been performed.
