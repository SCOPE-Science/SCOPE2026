# Exact endpoint growth of the alternating-level martingale transform on regular trees

## Finding
For integers \(b\ge2\) and \(m\ge1\), let \(\Omega=\{0,\ldots,b-1\}^m\) carry uniform probability measure. Let \(E_k\) be conditional expectation onto the partition by the first \(k\) coordinates (\(0\le k\le m\)); thus \(E_0\) is global averaging and \(E_m\) is the identity. Define the real alternating-level martingale transform
\[
T_{b,m}=\sum_{k=1}^{m}(-1)^{k-1}(E_k-E_{k-1}).
\]
Then its sharp, attained endpoint norm is
\[
\boxed{\|T_{b,m}\|_{L^\infty\to L^\infty}
=\|T_{b,m}\|_{L^1\to L^1}
=\frac{2(b-1)}{b+1}\,m
+\frac{2(b-1)}{(b+1)^2}\bigl(1-(-1/b)^m\bigr).}
\]
At every chosen terminal word, all norm-attaining real inputs of unit supremum norm are precisely the two signs of its nonzero kernel row. In particular the sharp depth increment is
\[
\|T_{b,m+1}\|_\infty-\|T_{b,m}\|_\infty
=\frac{2(b-1)}{b+1}\left(1+\frac{(-1)^m}{b^{m+1}}\right)>0,
\]
and the sharp growth slope at fixed branching number is \(2(b-1)/(b+1)\). The ordinary \(L^2\) operator norm is exactly \(1\).

## Assumptions and scope
The tree has exactly \(b\) children at every nonterminal vertex and exactly \(m\) levels of splitting, with equal measure \(b^{-m}\) at each leaf. All functions are real-valued. The coefficients alternate by depth and are constant across nodes at the same depth. All conditional expectations are taken with respect to the same uniform measure. This is a finite-dimensional theorem, valid simultaneously for every integer pair \((b,m)\) in the stated range.

The endpoint norm is the largest absolute row sum of the matrix of \(T_{b,m}\). Equality for an individual row means choosing the input sign of every entry in that row; because no entry vanishes, this choice is unique up to overall sign at that row. The theorem makes no claim that the alternating sign pattern maximizes the norm among *all* possible martingale-transform sign patterns.

## Proof
Fix a terminal word \(x\in\Omega\), write \(\epsilon_k=(-1)^{k-1}\), and let \(r(x,y)\) be the length of the common initial prefix of words \(x,y\). Conditional expectation has kernel \(b^k\mathbf1_{r(x,y)\ge k}\) relative to uniform probability. Summation by parts gives the transform kernel
\[
K(x,y)=-\epsilon_1+\sum_{k=1}^{m-1}b^k(\epsilon_k-\epsilon_{k+1})\mathbf1_{r(x,y)\ge k}
+\epsilon_m b^m\mathbf1_{y=x}.
\]
If \(0\le r=r(x,y)<m\), the geometric sum evaluates exactly to
\[
K_r=-1+2\sum_{k=1}^r(-1)^{k-1}b^k
=\frac{b-1-2b(-b)^r}{b+1}.
\]
On the diagonal it is
\[
K_m=\frac{b-1}{b+1}\bigl(1+(-1)^{m-1}b^m\bigr).
\]
For every integer \(b\ge2\), the signs are strict and consequently
\[
|K_r|=\frac{2b^{r+1}-(b-1)(-1)^r}{b+1}
\quad(0\le r<m),\qquad
|K_m|=\frac{b-1}{b+1}\bigl(b^m+(-1)^{m-1}\bigr).
\]
The probability that a uniform leaf \(y\) has common-prefix length exactly \(r<m\) with \(x\) is \((b-1)b^{-r-1}\), and the diagonal probability is \(b^{-m}\). Thus every absolute kernel-row integral is
\[
\begin{aligned}
\sum_{r=0}^{m-1}\frac{b-1}{b^{r+1}}|K_r|+b^{-m}|K_m|
&=\frac{2(b-1)m}{b+1}
-\frac{(b-1)^2}{b(b+1)}\sum_{r=0}^{m-1}(-1/b)^r\\
&\quad+\frac{b-1}{b+1}\left(1-(-1/b)^m\right).
\end{aligned}
\]
Evaluating the finite geometric series and simplifying gives the boxed formula. Every row has this value, and taking \(f(y)=\operatorname{sgn}K(x,y)\) yields \((T_{b,m}f)(x)=\|T_{b,m}\|_\infty\), proving sharpness. Conversely equality in the triangle inequality at row \(x\) forces every \(f(y)\) to equal the same global sign times \(\operatorname{sgn}K(x,y)\), since each \(K(x,y)\ne0\). Any global norm attainment must occur at some row; this characterizes all real norming inputs. The kernel is symmetric, so self-adjoint duality gives the same \(L^1\) norm.

The martingale differences \(E_k-E_{k-1}\) are pairwise orthogonal projections in \(L^2\). Hence the transform acts by eigenvalues \(\epsilon_k\) on their mutually orthogonal ranges and vanishes on constants: its \(L^2\) norm is \(1\). The displayed depth increment follows by subtracting the exact endpoint formulas; its parenthesis is positive for every allowed parameter.

## Verification
Run `python3 verify.py` with Python 3 and no third-party packages. The program independently constructs tested matrix entries directly from the defining conditional expectations, computes their exact rational absolute row sums, checks exact norm attainment by row signs, checks zero row sums, and verifies the depth-increment identity. It passed 20 configurations and 1,182 exact-rational assertions, including every kernel row on the indicated small configurations and single rows at larger depths. All infinite-parameter conclusions follow from the algebraic proof above; finite checks are not substituted for that proof.

For illustration the binary sequence begins \(1,3/2,9/4,23/8,57/16,135/32\), and the ternary sequence begins \(4/3,20/9,88/27,344/81,1276/243\). If \(N=b^m\) is the number of leaves, the leading term is \(\bigl(2(b-1)/((b+1)\log b)\bigr)\log N\). By contrast, the nonalternating all-positive coefficients yield \(E_m-E_0\), whose endpoint norm is only \(2(1-b^{-m})\). Thus sign alternation produces sharp logarithmic endpoint amplification despite unit \(L^2\) norm.

## Relationship to prior work
Martingale transforms and Haar multipliers are classical; their definitions and weighted operator-norm problems are not claimed as new. Wittwer (2000) obtains a sharp order of dependence on a dyadic \(A_2\) weight for a Hilbert-space transform bound. Kerr (arXiv:0906.4028) analyzes two-matrix-weight \(L^2\) boundedness. Lacey (arXiv:1501.05818) proves sparse domination and \(L^p\)-weighted bounds for martingale transforms. The inspected relevant sections do not provide this uniform \(b\)-ary alternating-level finite-depth \(L^\infty\) formula, the branching-dependent leading coefficient, or its row-sign extremizer classification. These comparisons do not establish historical uniqueness.

## Limitations
The exact expression depends on equal leaf weights, constant branching across all levels, and perfectly alternating depth coefficients. It does not determine endpoint norms for arbitrary nonhomogeneous trees, arbitrary level multipliers, or arbitrary nodewise martingale-transform coefficients. The unbounded linear-in-depth behavior is an endpoint statement, not an \(L^2\) instability. Possible earlier descriptions under finite Haar multiplier, martingale variation, or tree-matrix terminology remain a literature-priority risk. Independent external verification has not been performed.

## References
- J. Wittwer, *A sharp estimate on the norm of the martingale transform*, Mathematical Research Letters 7 (2000), 1–12, DOI: 10.4310/MRL.2000.V7.N1.A1.
- R. Kerr, *Martingale transforms, the dyadic shift and the Hilbert transform: a sufficient condition for boundedness between matrix weighted spaces*, arXiv:0906.4028, first posted 22 June 2009.
- M. T. Lacey, *An elementary proof of the A2 bound*, arXiv:1501.05818, first posted 23 January 2015.
