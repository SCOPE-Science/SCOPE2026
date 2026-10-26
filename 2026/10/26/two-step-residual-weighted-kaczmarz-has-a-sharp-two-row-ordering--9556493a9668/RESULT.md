# Two-step residual-weighted Kaczmarz has a sharp two-row ordering boundary

## Finding

Residual-powered row sampling for Kaczmarz can improve conditional one-step expected error while worsening the **unconditional two-step expected squared error**. With exactly two normalized independent rows, that two-step expected error is nonincreasing in every positive sampling exponent and never exceeds the uniform-with-replacement baseline. With three normalized independent rows, this guarantee fails at the finite exponent \(p=40\): a fully rational consistent system has
\[
\mathbb E\|x_2^{(40)}-x_*\|_2^2>\frac{21}{2}>10>
\mathbb E\|x_2^{(0)}-x_*\|_2^2=\frac{65572}{6561}.
\]
The row-count boundary is sharp for the stated two-step comparison; no claim about optimal exponents at longer horizons is made.

## Assumptions and scope

Let \(A\in\mathbb R^{m\times n}\) have nonzero, unit-norm rows \(u_i^\mathsf T\), full column rank, and a consistent right-hand side \(b=Ax_*\). At each step choose row \(i\) with probability proportional to \(|u_i^\mathsf T(x_k-x_*)|^p\), then apply the exact orthogonal projection
\[
x_{k+1}=x_k-(u_i^\mathsf T(x_k-x_*))u_i.
\]
For \(p=0\), rows are selected uniformly, independently at each iteration, **including zero-residual rows**. For \(p>0\), zero-residual rows have zero probability. If all residuals vanish, the method terminates at \(x_*\). All expectations refer to the row choices in two updates, from a common deterministic \(x_0\). The two-row assertion has \(m=n=2\) and independent rows; the counterexample has \(m=n=3\). This is the \(\lambda=0\) specialization of residual-weighted randomized sparse Kaczmarz and the weighted randomized Kaczmarz algorithm itself.

## Proof

Put \(e=x_0-x_*\), \(a_i=u_i^\mathsf Te\), and \(c_{ij}=u_i^\mathsf Tu_j\). Choosing \(i\) then \(j\) gives the exact identity
\[
F_{ij}:=\|e_2\|_2^2
=\|e\|_2^2-a_i^2-(a_j-c_{ij}a_i)^2.\tag{1}
\]
For two rows write \(a=a_1\), \(d=a_2\), and \(c=c_{12}\). Subtraction of the two possible nonrepeating orders gives
\[
F_{12}-F_{21}=c^2(d^2-a^2).\tag{2}
\]
Suppose \(|a|\ge|d|>0\). At exponent \(p>0\), after the first nonterminal projection only the other row has nonzero residual, so
\[
\mathbb E_p\|e_2\|_2^2
=\frac{|a|^pF_{12}+|d|^pF_{21}}{|a|^p+|d|^p}.\tag{3}
\]
The weight of \(F_{12}\), the smaller of the two values by (2), is nondecreasing in \(p\). Therefore (3) is nonincreasing in \(p\). The case \(|a|=|d|\) gives equality, and a zero initial residual is handled by the unique positive-residual choice. At \(p=0\), independent uniform sampling can repeat its first selected row. Such a repetition leaves the first-projected vector unchanged and cannot improve on applying the other row, so its expectation is at least \((F_{12}+F_{21})/2\). Equation (3), or its one-sided zero-residual limit, is no larger. This proves the universal two-row statement.

For the three-row obstruction take
\[
A=\frac13\begin{pmatrix}2&-1&2\\2&-2&-1\\1&2&2\end{pmatrix},
\qquad x_0=(0,0,0)^\mathsf T,
\qquad x_*=(0,-4,1)^\mathsf T,
\qquad b=(2,7/3,-2)^\mathsf T.\tag{4}
\]
Every row has unit Euclidean norm and \(\det A=13/27\ne0\), so the system is full-rank and consistent. Here \(e=(0,4,-1)^\mathsf T\), \(\|e\|^2=17\),
\[
(a_1,a_2,a_3)=(-2,-7/3,2),\qquad
AA^\mathsf T=\begin{pmatrix}1&4/9&4/9\\4/9&1&-4/9\\4/9&-4/9&1\end{pmatrix}.
\]
Using (1), the complete table of the **nine exact squared errors** for the row pair \((i,j)\) is
\[
(F_{ij})=
\begin{pmatrix}
13&884/81&377/81\\
7748/729&104/9&7748/729\\
377/81&884/81&13
\end{pmatrix}.\tag{5}
\]
Uniform-with-replacement sampling gives their arithmetic mean,
\[
\mathbb E_0\|e_2\|_2^2=\frac19\sum_{i,j=1}^3F_{ij}
=\frac{65572}{6561}<10.\tag{6}
\]
For exponent \(40\), the probability that row \(2\) is selected first is
\[
P_2=\frac{7^{40}}{7^{40}+2\cdot6^{40}}.
\]
Conditioned on that event, the three residuals become \((-26/27,0,26/27)\); the next row is either \(1\) or \(3\), and either choice yields the exact error \(7748/729\). All other paths contribute nonnegative squared errors. Since \(7^{40}>200\cdot6^{40}\),
\[
\mathbb E_{40}\|e_2\|_2^2
\ge P_2\frac{7748}{729}
>\frac{100}{101}\frac{7748}{729}
=\frac{774800}{73629}>\frac{21}{2}.\tag{7}
\]
This proves a strict finite-exponent two-step reversal. Nevertheless, the **first-step** conditional expected squared error is nonincreasing in \(p\), since the expected decrease is the weighted mean \(\sum_i|a_i|^{p+2}/\sum_i|a_i|^p\), which grows with \(p\). Thus the reversal is genuinely a two-step interaction, not a one-step deterioration.

## Verification

The accompanying standalone `verify.py` uses Python's standard-library exact rational arithmetic. It reconstructs (4)–(7), computes the exact full expectation at exponent \(40\), checks the first-step improvement, verifies the determinant and all residuals, and tests the algebraic two-row identity on a rational grid. Run `python verify.py`. The entire rational table and the lower bound in (7) are independently reconstructible without floating-point arithmetic. Finite grid tests do not substitute for the algebraic two-row proof.

## Relationship to prior work

Steinerberger, *A Weighted Randomized Kaczmarz Method for Solving Linear Systems* (arXiv:2007.02910, first public 2020-07-06) introduced precisely this residual-power sampling and proved a one-step-derived global geometric **rate bound** at least as favorable as the uniform-method bound. That is not a pointwise stochastic ordering of the exact two-step risks, and (7) does not contradict the published rate result. Zhang, Yuan, Wang, and Zhang, *A Weighted Randomized Sparse Kaczmarz Method for Solving Linear Systems* (arXiv:2306.06813, first public 2023-06-12), extended the sampling to Bregman and sparse iterates; its \(\lambda=0\) case is the ordinary projection update in (4). Nutini et al., *Convergence Rates for Greedy Kaczmarz Algorithms, and Faster Randomized Kaczmarz Rules Using the Orthogonality Graph* (arXiv:1612.07838, 2016-12-22), developed multi-step convergence-rate bounds using an orthogonality graph, but do not state the present exact two-row finite-horizon ordering and three-row exponent reversal. The statements compared are rate bounds versus actual two-step expected squared errors, not merely similar terminology.

## Limitations

The reverse inequality is shown for a single fully specified three-row initial-value problem and one finite exponent, not for every three-row matrix or every exponent. The two-row theorem is exclusively a two-step expected-squared-error statement, not a stochastic pathwise ordering or an all-horizon theorem. The examples are exact arithmetic, consistent full-column-rank systems, with no positive sparsity regularization. Published-equivalence risk outside the inspected literature remains. No independent scientific audit has been performed.

## References

1. S. Steinerberger, *A Weighted Randomized Kaczmarz Method for Solving Linear Systems*, arXiv:2007.02910, 2020-07-06. https://arxiv.org/abs/2007.02910
2. L. Zhang, Z. Yuan, H. Wang, H. Zhang, *A Weighted Randomized Sparse Kaczmarz Method for Solving Linear Systems*, arXiv:2306.06813, 2023-06-12. https://arxiv.org/abs/2306.06813
3. J. Nutini, B. Sepehry, I. Laradji, M. Schmidt, H. Koepke, A. Virani, *Convergence Rates for Greedy Kaczmarz Algorithms, and Faster Randomized Kaczmarz Rules Using the Orthogonality Graph*, arXiv:1612.07838, 2016-12-22. https://arxiv.org/abs/1612.07838
