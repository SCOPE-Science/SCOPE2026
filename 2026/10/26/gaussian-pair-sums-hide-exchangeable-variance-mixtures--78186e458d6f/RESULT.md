# Gaussian pair sums hide exchangeable variance mixtures

## Finding

For any Borel probability measure \(\rho\) on \((0,\tfrac12)\), let \(V\sim\rho\) and let \(Z,\varepsilon_1,\varepsilon_2,\ldots\) be mutually independent standard normal variables, independent of \(V\), and set \(X_i=\frac{\sqrt{1-2V}}{2}Z+\sqrt V\,\varepsilon_i\). Then \((X_i)_{i\ge1}\) is infinitely exchangeable and \(X_i+X_j\sim N(0,1)\) for every \(i\ne j\), regardless of \(\rho\); its covariance matrix depends on \(\rho\) only through \(\mathbb EV\), while the characteristic function of \(X_i-X_j\) is \(\int e^{-vt^2}\rho(dv)\), which uniquely identifies \(\rho\). If \(\rho\) is nondegenerate, the process is not Gaussian because its marginal fourth cumulant is \(3\operatorname{Var}(V)/4>0\). In particular, \(\rho_1=\delta_{1/4}\) and \(\rho_2=\tfrac12\delta_{1/8}+\tfrac12\delta_{3/8}\) yield the same Gaussian pair-sum law and identical covariance matrices, but respectively a Gaussian and a non-Gaussian exchangeable process.

## Assumptions and scope

Let \(\rho\) be any Borel probability measure on \((0,\tfrac12)\). The non-Gaussian conclusion requires that \(\rho\) not be a point mass. The variables \(Z,\varepsilon_1,\varepsilon_2,\ldots\) are mutually independent standard normal variables and are independent of \(V\sim\rho\). Exchangeability is infinite exchangeability, not merely finite exchangeability.

The observation under study is the one-dimensional distribution of each single pair sum \(X_i+X_j\). No claim is made that the joint distribution of the entire array of pair sums is independent of \(\rho\), nor that the marginal law of \(X_i\) is Gaussian when \(\rho\) is nondegenerate.

## Proof

Put \(M=\frac{\sqrt{1-2V}}{2}Z\). Conditional on \((V,Z)\), the sequence is iid with common law \(N(M,V)\); hence it is exchangeable.

For distinct \(i,j\),
\[
X_i+X_j=\sqrt{1-2V}\,Z+\sqrt V(\varepsilon_i+\varepsilon_j).
\]
Conditional on \(V\), the two terms are independent centered Gaussian variables with variances \(1-2V\) and \(2V\). Their sum therefore has law \(N(0,1-2V+2V)=N(0,1)\), which does not depend on \(V\). Thus every pair sum is standard normal and is independent of \(V\).

Conditional on \(V\), the marginal \(X_i\) is centered normal with variance
\[
s(V)=\frac{1-2V}{4}+V=\frac{1+2V}{4}.
\]
Consequently,
\[
\operatorname{Var}(X_i)=\frac14+\frac12\mathbb EV,
\qquad
\operatorname{Cov}(X_i,X_j)=\frac14-\frac12\mathbb EV
\quad(i\ne j).
\]
So the full covariance matrix depends on \(\rho\) only through its mean.

A centered normal variance mixture has fourth moment \(\mathbb E[X_i^4]=3\mathbb E[s(V)^2]\). Therefore its fourth cumulant is
\[
\mathbb E[X_i^4]-3(\mathbb E[X_i^2])^2
=3\operatorname{Var}(s(V))
=\frac34\operatorname{Var}(V).
\]
This is strictly positive when \(\rho\) is nondegenerate, so \(X_i\) is not Gaussian and the process is not a Gaussian process.

Finally,
\[
X_i-X_j=\sqrt V(\varepsilon_i-\varepsilon_j),
\qquad
\mathbb E[e^{it(X_i-X_j)}]=\int_{(0,1/2)}e^{-vt^2}\,\rho(dv).
\]
The right-hand side gives the Laplace transform of \(\rho\) at every argument \(u=t^2\ge0\). Uniqueness of the Laplace transform for finite measures on the bounded interval \([0,1/2]\) identifies \(\rho\) from the pair-difference law.

For an explicit covariance-matched pair, take \(\rho_1=\delta_{1/4}\) and \(\rho_2=\tfrac12\delta_{1/8}+\tfrac12\delta_{3/8}\). Both have mean \(1/4\), so both give marginal variance \(3/8\), off-diagonal covariance \(1/8\), and pair-sum law \(N(0,1)\). The first process is Gaussian because \(V\) is constant. For the second, \(\operatorname{Var}(V)=1/64\), so the marginal fourth cumulant is exactly \(3/256\). Their pair-difference characteristic functions, respectively \(e^{-t^2/4}\) and \(\tfrac12e^{-t^2/8}+\tfrac12e^{-3t^2/8}\), are different.

## Verification

The proof uses exact conditional Gaussian calculations and the uniqueness of the Laplace transform; it does not infer a distributional identity from simulation. The standalone script `verify_pair_sum_family.py` checks the rational moment and covariance calculations for the two explicit mixing laws. Its finite arithmetic checks supplement rather than replace the proof.

## Relationship to prior work

Zheng and Zhou prove that if one pair \((X_i,X_j)\) of an infinite exchangeable real-valued sequence is jointly Gaussian, then the entire sequence is a Gaussian process. The present construction does not contradict that theorem: only the scalar projection \(X_i+X_j\) is Gaussian, while the pair law is not jointly Gaussian for nondegenerate \(\rho\).

Newman's work on rigidity and identifiability for infinite exchangeable sequences supplies closely related context. Evans and Zhou already showed that, in general, the distributions of all partial sums need not identify an exchangeable sequence. Their published counterexample is a different construction and does not state the Gaussian pair-sum family above. The present claim is limited to the exact Gaussian sum law, its covariance-matched Gaussian/non-Gaussian pair, and recovery of the mixing law from pair differences.

## Limitations

- The result is an explicit family, not a classification of all exchangeable sequences with Gaussian pair sums.
- For nondegenerate \(\rho\), the one-dimensional marginal is non-Gaussian; no claim is made about examples with Gaussian marginals.
- Only the marginal law of each individual pair sum is fixed. The joint law of several overlapping pair sums is not claimed to be independent of \(\rho\).
- The difference-law identification applies within this constructed family; it is not a uniqueness theorem for arbitrary directing measures.

## References

1. Y. Zheng and Q. Zhou, “Gaussian rigidity for infinite exchangeable sequences,” arXiv:2606.25976 (submitted 24 June 2026).
2. M. Newman, “On rigidity of infinite exchangeable sequences,” arXiv:2610.18992 (submitted 13 October 2026).
3. S. N. Evans and X. Zhou, “Identifiability of exchangeable sequences with identically distributed partial sums,” *Electronic Communications in Probability* 4 (1999), 9–13. DOI:10.1214/ECP.v4-1000.
