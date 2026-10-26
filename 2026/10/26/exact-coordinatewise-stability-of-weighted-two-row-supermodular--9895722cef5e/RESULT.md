# Exact coordinatewise stability of weighted two-row supermodular regression

## Finding
Fix an integer \(m\geq 2\). For strictly positive weights \(a_j,b_j\), define the weighted least-squares projection \(\Pi_{a,b}\) of real \(2\times m\) arrays \(y\) onto the closed convex cone
\[
\mathcal M_m=\{x:x_{1,j}+x_{2,j+1}-x_{1,j+1}-x_{2,j}\geq0\ \text{for all }1\leq j<m\},
\]
where the loss minimized is
\[
\sum_{j=1}^m\left(a_j(x_{1,j}-y_{1,j})^2+b_j(x_{2,j}-y_{2,j})^2\right).
\]
The input and output error are measured in the ordinary coordinatewise maximum norm, **without weighting**. Set
\[
c_j=\frac{a_jb_j}{a_j+b_j},\qquad C=\sum_{i=1}^m c_i,\qquad
\alpha_j=\frac{\max(a_j,b_j)}{a_j+b_j}.
\]
Then the **exact global Lipschitz constant**, including attainment by a finite pair of arrays, is
\[
\boxed{\operatorname{Lip}_\infty(\Pi_{a,b})
=1+2\max_{1\leq j\leq m}\alpha_j\left(1-\frac{c_j}{C}\right).}
\]
For every fixed \(m\geq2\), the entire set of constants attainable over all positive weight arrays is
\[
\boxed{\left[2-\frac1m,\ 3\right).}
\]
The lower endpoint is attained **if and only if** all \(2m\) weights are equal. The upper endpoint is not attained by any strictly positive weights. For example, taking \(a_1=M\), \(b_1=1/M\), and \(a_j=b_j=1\) for \(j>1\) makes the constant tend to \(3\) as \(M\to\infty\). For equal weights the exact constant is \(2-1/m\). For \(m=1\), with no supermodularity constraint, the projector is the identity and its constant is \(1\).

## Assumptions and scope
All arrays are real and all observation weights are finite and strictly positive. The cone concerns **supermodularity** (also called the anti-Monge condition) with fixed row and column order. No unknown permutations, extra nonnegativity constraints, or statistical distributional assumptions are imposed. The metric projection is unique by strict convexity of the weighted quadratic loss. Stability is worst-case deterministic coordinatewise error, not a statistical mean-squared risk.

## Proof
Write the two input rows at column \(j\) as \(u_j=y_{1,j}\) and \(v_j=y_{2,j}\), and introduce the weighted column mean and row difference
\[
s_j=\frac{a_ju_j+b_jv_j}{a_j+b_j},\qquad d_j=v_j-u_j.
\]
Every candidate output has a unique corresponding mean \(s_j'\) and difference \(d_j'\), and direct completion of the square gives the identity
\[
a_j(x_{1,j}-u_j)^2+b_j(x_{2,j}-v_j)^2
=(a_j+b_j)(s'_j-s_j)^2+c_j(d'_j-d_j)^2.
\]
The supermodular inequalities become exactly \(d'_{j+1}\geq d'_j\). Hence optimal means remain \(s'_j=s_j\), while \(\widehat d\) is the **weighted isotonic projection** of \(d\) with weights \(c_j\). The projected array is
\[
\widehat x_{1,j}=s_j-\frac{b_j}{a_j+b_j}\widehat d_j,
\qquad
\widehat x_{2,j}=s_j+\frac{a_j}{a_j+b_j}\widehat d_j.
\]

The weighted isotonic solution partitions columns into consecutive pooled blocks. On each open affine cell with a fixed block partition, the fitted difference at \(j\) is
\[
\widehat d_j=\frac{\sum_{i\in B}c_id_i}{C_B},\qquad C_B=\sum_{i\in B}c_i,
\]
where \(B\) is the block containing \(j\). The row of the Jacobian corresponding to top output coordinate \(j\) has two same-column coefficients which are nonnegative and sum to \(1\). Every other column \(i\in B\setminus\{j\}\) contributes coefficients of opposite signs and total absolute magnitude \(2\,b_jc_i/((a_j+b_j)C_B)\); columns outside \(B\) contribute zero. Consequently its exact absolute row sum is
\[
1+2\frac{b_j}{a_j+b_j}\left(1-\frac{c_j}{C_B}\right).
\]
The corresponding bottom-row sum is
\[
1+2\frac{a_j}{a_j+b_j}\left(1-\frac{c_j}{C_B}\right).
\]
Since \(C_B\leq C\), both sums are bounded above by the displayed global constant. A continuous map with finitely many affine pieces has a global Lipschitz modulus no greater than the maximum of the piecewise linear operator norms: split any connecting line segment at its finitely many cell boundaries, using continuity for degenerate segments. Thus this is a global upper bound.

For sharpness choose strictly decreasing input differences, for example \(d_j=m-j\). Then every proper initial weighted prefix has mean strictly above the full weighted mean, so the unique isotonic fit is one pooled block of all \(m\) columns, with strictly positive KKT multipliers at every internal inequality. This pooling region has nonempty interior. Choose the row and column realizing the maximum in the formula, perturb the input in the signs of the corresponding Jacobian coefficients by a sufficiently small positive amount, and stay within that open region. The output/input maximum-norm quotient is **exactly** the claimed row sum. This yields a finite-pair equality, not merely a derivative supremum.

For the weight-design classification, \(\alpha_j\geq1/2\), so
\[
\operatorname{Lip}_\infty(\Pi_{a,b})
\geq 1+\max_j(1-c_j/C)
=2-\min_jc_j/C\geq2-1/m.
\]
Equality forces all \(c_j\) equal and every \(\alpha_j=1/2\), hence \(a_j=b_j\) and all their common values equal. Conversely these weights attain the lower endpoint. Strict positivity gives \(\alpha_j<1\) and \(c_j/C>0\), so the constant is strictly below \(3\). In the stated one-parameter family the first-column contribution approaches \(2\) and the full modulus approaches \(3\). The modulus is continuous in all positive weights; connecting equal weights to arbitrarily large members of this family and applying the intermediate value theorem proves the complete attainable interval.

## Verification
`checker.py` uses only Python 3 standard-library exact fractions. Its independent contiguous-partition enumeration agrees with a separately implemented weighted pool-adjacent-violators algorithm on random rational samples, and it verifies the closed-form Jacobian, all coordinate finite differences in a strictly pooled cell, the attained row-sum norm, feasibility, and near-extremal weight families. It prints `EXACT_RATIONAL_CHECKS_PASSED=12883` upon success. Run using `python3 checker.py` in the extracted package directory. These finite tests are supporting checks; the preceding argument proves the theorem for every \(m\) and every positive weight array.

## Relationship to prior work
Chatterjee, Guntuboyina, and Sen (2013, arXiv:1311.3765) study risk bounds for isotonic and other shape-constrained least squares. Hütter, Mao, Rigollet, and Robeva (2019, arXiv:1904.03136) study estimation of Monge and anti-Monge matrices, including the adjacent mixed-difference cone and a least-squares projection algorithm. The exact coordinatewise perturbation modulus, its explicit heteroscedastic weight dependence, and the sharp complete range of weight-design values are not stated in those examined texts. The result uses weighted isotonic pooling as a mechanism but concerns the **reconstructed two-row supermodular projector**, which is not the isotonic projector acting in its own input coordinates.

## Limitations
Only two-row arrays are covered, with no additional constraints or missing cells. The theorem does not determine maximum-norm stability for arbitrary larger rectangular anti-Monge arrays. Originality is assessed against the cited and specifically queried literature, not certified against every historical source. Reproducible finite tests do not constitute independent mathematical certification.

## References
1. S. Chatterjee, A. Guntuboyina, and B. Sen, *On risk bounds in isotonic and other shape restricted regression problems*, arXiv:1311.3765, first publicly submitted 15 November 2013; https://arxiv.org/abs/1311.3765.
2. J.-C. Hütter, C. Mao, P. Rigollet, and E. Robeva, *Estimation of Monge Matrices*, arXiv:1904.03136, first publicly submitted 5 April 2019; https://arxiv.org/abs/1904.03136.
