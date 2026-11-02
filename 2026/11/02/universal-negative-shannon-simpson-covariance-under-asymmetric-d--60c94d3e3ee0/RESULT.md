# Universal negative Shannon–Simpson covariance under asymmetric Dirichlet laws

## Finding
For every finite-dimensional Dirichlet law with **at least two** strictly positive concentration parameters, natural-log Shannon entropy and Simpson concentration have strictly negative covariance. Even for unequal parameters, the covariance has the exact weighted-digamma decomposition
\[
\operatorname{Cov}(H,Q)
=-\frac{\displaystyle (A^2-\sum_{i=1}^{m}\alpha_i^2)/(A+1)
+2A\operatorname{Cov}_{w}(\alpha_i,\psi(\alpha_i+1))}
{A(A+1)(A+2)}<0.
\]
The two contributions are independently nonnegative before the leading minus sign. A distinct feature is that balancing the prior concentrations does **not** necessarily strengthen the dependence: with two categories and fixed total concentration two,
\[
\operatorname{Cov}_{\operatorname{Dirichlet}(1,1)}(H,Q)=-\frac1{36},
\qquad
\operatorname{Cov}_{\operatorname{Dirichlet}(1/2,3/2)}(H,Q)=-\frac1{24}.
\]
Thus the asymmetric example has covariance magnitude \(3/2\) times the symmetric example at the same total concentration.

## Assumptions and scope
Fix any integer \(m\ge2\) and positive real concentrations \(\alpha_1,\ldots,\alpha_m\). Put \(A=\sum_i\alpha_i\), \(w_i=\alpha_i/A\), and sample the simplex vector \(X=(X_i)\sim\operatorname{Dirichlet}(\alpha_1,\ldots,\alpha_m)\). Define
\[
H=-\sum_i X_i\log X_i,\quad Q=\sum_iX_i^2,\quad
\overline a=\sum_iw_i\alpha_i,\quad
\overline b=\sum_iw_i\psi(\alpha_i+1),
\]
where \(\psi\) is the digamma function. Use natural logarithms and the convention \(0\log0=0\), although strictly positive Dirichlet parameters put the vector in the simplex interior almost surely. The weighted covariance is
\[
D=\sum_iw_i(\alpha_i-\overline a)(\psi(\alpha_i+1)-\overline b).
\]
The theorem concerns population functionals of a random probability vector, **not** finite-sample estimators or their sampling covariance. Gini–Simpson diversity \(1-Q\) has the opposite (positive) covariance with \(H\). No stochastic ordering is asserted.

## Proof
The Dirichlet moment identity, for nonnegative real exponents, is
\[
\mathbb E\prod_iX_i^{r_i}
=\frac{\prod_i\Gamma(\alpha_i+r_i)/\Gamma(\alpha_i)}
{\Gamma(A+\sum_i r_i)/\Gamma(A)}.
\]
Differentiating with respect to \(r_i\) is valid for strictly positive parameters and gives an expectation containing \(\log X_i\). Introduce the abbreviations
\[
B=\sum_i\alpha_i(\alpha_i+1),\qquad
T=\sum_i\alpha_i\psi(\alpha_i+1),\qquad
U=\sum_i\alpha_i(\alpha_i+1)\psi(\alpha_i+1),\qquad
J=\sum_i\alpha_i^2.
\]
The elementary first moments are
\[
\mathbb EH=\psi(A+1)-\frac TA,\qquad
\mathbb EQ=\frac{B}{A(A+1)}.
\]
For the mixed moment, separate terms with matching indices from terms with distinct indices. The derivative of \(\mathbb E[X_iX_j^2]\) contributes \(\psi(A+3)\), and the matching-index correction uses
\(\psi(\alpha_i+3)-\psi(\alpha_i+1)=1/(\alpha_i+1)+1/(\alpha_i+2)\). Summing gives
\[
\mathbb E[HQ]
=\frac{B\psi(A+3)}{A(A+1)}
-\frac{BT+2U+2J+3A}{A(A+1)(A+2)}.
\]
Subtracting the product of the first moments, and applying \(\psi(A+3)-\psi(A+1)=1/(A+1)+1/(A+2)\), yields
\[
\operatorname{Cov}(H,Q)
=\frac{(J-A^2)/(A+1)+2(BT/A-U)}{A(A+1)(A+2)}.
\]
Since \(B=A\sum_iw_i(\alpha_i+1)\), \(T=A\sum_iw_i\psi(\alpha_i+1)\), and \(U=A\sum_iw_i(\alpha_i+1)\psi(\alpha_i+1)\), one has \(BT/A-U=-AD\), proving the displayed identity.

For every \(m\ge2\) and every positive parameter vector, \(A^2-J=2\sum_{i<j}\alpha_i\alpha_j>0\). Moreover
\[
D=\sum_{i<j}w_iw_j(\alpha_i-\alpha_j)
\bigl(\psi(\alpha_i+1)-\psi(\alpha_j+1)\bigr)\ge0
\]
because \(\psi\) is strictly increasing on \((0,\infty)\). This proves strict negativity for the entire stated domain.

When all \(\alpha_i=t\), the weighted covariance \(D\) vanishes; simplification produces
\(\operatorname{Cov}(H,Q)=-(m-1)t/((mt+1)^2(mt+2))\).
For \(m=2\), \(\alpha=(1/2,3/2)\), the digamma recurrence gives
\(\psi(5/2)-\psi(3/2)=2/3\), so \(D=1/8\), \(A=2\), \(J=5/2\). Direct substitution gives \(-1/24\), versus \(-1/36\) at \((1,1)\). No optimization over all asymmetric parameters is claimed.

## Verification
Run `python3 verify_dirichlet.py` from the directory containing the supplied standalone script. It independently evaluates the mixed moment by summing every \(\mathbb E[X_i\log X_i\,X_j^2]\), and compares against the closed form by exact \(\operatorname{Fraction}\) arithmetic for all 3,900 parameter vectors with \(2\le m\le5\) and integer concentrations in \(\{1,2,3,4,5\}\). It also tests exact strict signs, symmetric specializations, and the two half-integer comparison cases. These finite checks do not replace the analytical proof for arbitrary positive real parameters.

## Relationship to prior work
Shannon entropy and Simpson/Gini–Simpson indices are established, distinct diversity functionals. Wolpert and Wolf (1994, Part I) calculate Bayesian Shannon-entropy moments and discuss Dirichlet priors; their companion Part II treats estimators for variance and covariance *as functionals of an underlying distribution*, not the covariance between the Shannon and Simpson functionals across Dirichlet draws. Cerquetti (2014) develops marginal moments of individual Tsallis diversity indices, with Shannon and Simpson as different orders, in a broader random-partition framework. The inspected statements do not give this arbitrary-asymmetric finite-Dirichlet mixed covariance, its universal sign decomposition, or the fixed-total asymmetry comparison. Standard Dirichlet monomial moments enable the calculation but do not by themselves state the sign inequality. Historical priority beyond the inspected works is unresolved.

## Limitations
This is an exact covariance identity, not an assertion of independence, monotonic regression, negative association of all diversity indices, or stochastic dominance. It does not identify the concentration vector that maximizes the magnitude for fixed total \(A\), and does not address infinite-dimensional or hierarchical Dirichlet mixtures. Searches do not establish absolute historical novelty; specialized older joint-diversity literature could contain an equivalent result. The verifier tests finite rational parameter sets only; the proof handles all strictly positive real concentrations.

## References
1. D. H. Wolpert and D. R. Wolf, *Estimating Functions of Probability Distributions from a Finite Set of Samples, Part I: Bayes Estimators and the Shannon Entropy*, arXiv:comp-gas/9403001 (first submitted 1994-03-08). https://arxiv.org/abs/comp-gas/9403001
2. D. R. Wolf and D. H. Wolpert, *Estimating Functions of Distributions from a Finite Set of Samples, Part II: Bayes Estimators for Mutual Information, Chi-Squared, Covariance, and other Statistics*, arXiv:comp-gas/9403002 (first submitted 1994-03-08). https://arxiv.org/abs/comp-gas/9403002
3. A. Cerquetti, *Bayesian nonparametric estimation of Tsallis diversity indices under Gnedin–Pitman priors*, arXiv:1404.3441 (first submitted 2014-04-14). https://arxiv.org/abs/1404.3441
