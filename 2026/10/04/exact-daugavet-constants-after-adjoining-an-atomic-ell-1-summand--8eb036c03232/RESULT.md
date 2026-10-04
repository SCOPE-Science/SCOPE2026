# Exact Daugavet constants after adjoining an atomic \(\ell_1\) summand
## Finding
Let \(X\) be a nonzero real Banach space, let \(\Gamma\) be nonempty, and let \(z=(x,a)\in S_{X\oplus_1\ell_1(\Gamma)}\). Put \(b=\|a\|_1\) and \(m=\|a\|_\infty\). Then the pointwise Daugavet constant satisfies \[\operatorname{dc}_{X\oplus_1\ell_1(\Gamma)}(x,a)=\min\{b+\operatorname{dc}_X(x),\,2(1-m)\}.\] In particular, if \(X\) has the Daugavet property, then \(\operatorname{dc}(x,a)=2(1-\|a\|_\infty)\) on the unit sphere.

Here \(\operatorname{dc}_X(x)\) is the pointwise Daugavet constant of Choi and Jung, defined for \(x\in B_X\) by
\[
\operatorname{dc}_X(x)=\inf_{S\text{ a slice of }B_X}\ \sup_{u\in S}\|x-u\|.
\]
The identity separates two sharp obstructions: the Banach-space component contributes \(b+\operatorname{dc}_X(x)\), while the largest atomic coordinate contributes \(2(1-m)\).

## Assumptions and scope
The spaces are real. The index set \(\Gamma\) may be finite or infinite, and the supremum defining \(m=\|a\|_\infty\) need not be attained. No Daugavet property is assumed for \(X\) in the main formula. The point \((x,a)\) lies on the unit sphere, so \(\|x\|+b=1\).

The formula also covers the endpoint cases. If \(a=0\), then \(b=m=0\) and the identity gives \(\operatorname{dc}(x,0)=\operatorname{dc}_X(x)\). If \(m=1\), then \((x,a)\) is a signed scalar basis vector and the constant is \(0\).

## Proof
Write \(Z=X\oplus_1\ell_1(\Gamma)\). Its dual is \(Z^*=X^*\oplus_\infty\ell_\infty(\Gamma)\). Let a slice of \(B_Z\) be determined by \((f,c)\in S_{Z^*}\) and \(\alpha>0\). Since
\[
\max\{\|f\|,\|c\|_\infty}\}=1,
\]
at least one of \(\|f\|\) and \(\|c\|_\infty\) equals \(1\).

Suppose first that \(\|f\|=1\). The slice contains every point \((u,0)\) with \(u\in B_X\) and \(f(u)>1-\alpha\). Hence
\[
\sup_{w\in S}\|z-w\|
\ge b+\sup_{u\in B_X,\ f(u)>1-\alpha}\|x-u\|
\ge b+\operatorname{dc}_X(x).
\]

Suppose instead that \(\|c\|_\infty=1\). For every \(\varepsilon\in(0,\alpha)\), choose \(\gamma\in\Gamma\) with \(|c_\gamma|>1-\varepsilon\), and let \(\theta\in\{-1,1\}\) be the sign of \(c_\gamma\). Then \((0,\theta e_\gamma)\) belongs to the slice. Since \(|a_\gamma|\le m\),
\[
\begin{aligned}
\|z-(0,\theta e_\gamma)\|
&=\|x\|+\|a-\theta e_\gamma\|_1\\
&\ge \|x\|+1+b-2|a_\gamma|\\
&=2-2|a_\gamma|\\
&\ge 2(1-m).
\end{aligned}
\]
Thus every slice has supremal distance at least
\[
\min\{b+\operatorname{dc}_X(x),\,2(1-m)\}.
\]

For the first upper bound, fix \(\eta>0\). By the definition of \(\operatorname{dc}_X(x)\), choose a slice of \(B_X\), determined by some \(f\in S_{X^*}\), whose supremal distance from \(x\) is less than \(\operatorname{dc}_X(x)+\eta\). Shrinking its slice parameter if necessary, assume the parameter is also less than \(\eta\). The corresponding slice of \(B_Z\) determined by \((f,0)\) forces \(\|v\|_1<\eta\) for every \((u,v)\) in that slice. Therefore
\[
\|z-(u,v)\|
\le \|x-u\|+b+\|v\|_1
<\operatorname{dc}_X(x)+b+2\eta.
\]
Letting \(\eta\downarrow0\) gives
\[
\operatorname{dc}_Z(z)\le b+\operatorname{dc}_X(x).
\]

For the second upper bound, the case \(m=0\) is immediate from the universal estimate \(\operatorname{dc}_Z(z)\le2\). Assume \(m>0\). Choose \(\gamma\in\Gamma\) with \(|a_\gamma|\) arbitrarily close to \(m\), and put \(q=|a_\gamma|\). If \(q<1\), let \(\theta\) be the sign of \(a_\gamma\) and take a slice determined by \((0,\theta e_\gamma^*)\) with parameter smaller than \(1-q\). For \((u,v)\) in this slice, set \(s=\theta v_\gamma\). Then \(s>q\) and
\[
\|u\|+\sum_{\delta\ne\gamma}|v_\delta|\le1-s.
\]
Consequently,
\[
\begin{aligned}
\|z-(u,v)\|
&\le \|x\|+(b-q)+(s-q)+(1-s)\\
&=2(1-q).
\end{aligned}
\]
Letting \(q\uparrow m\) yields \(\operatorname{dc}_Z(z)\le2(1-m)\). If \(q=1\), the same coordinate slices have diameter from \(z\) tending to \(0\), so \(\operatorname{dc}_Z(z)=0\). Combining the two upper bounds with the lower bound proves the formula.

If \(X\) has the Daugavet property, every slice of \(B_X\) contains points arbitrarily close to distance \(1+\|x\|\) from \(x\), so \(\operatorname{dc}_X(x)=1+\|x\|\). Since \(b+\|x\|=1\), the first term in the minimum becomes \(2\), giving the stated corollary.

## Verification
An exact-rational finite consistency check specializes \(X\) to finite-dimensional \(\ell_1\) spaces. In this case the published formula is
\[
\operatorname{dc}_X(x)=1+\|x\|_1-2\|x\|_\infty.
\]
Substitution into the new identity reduces it exactly to the published \(\ell_1\) formula
\[
\operatorname{dc}(z)=2\bigl(1-\|z\|_\infty\bigr).
\]
The included checker exhaustively verifies this identity for \(92{,}760\) normalized signed integer test vectors using exact rational arithmetic.

## Relationship to prior work
Choi and Jung introduced the pointwise Daugavet constant and proved exact formulas on \(L_1\) and \(\ell_1\), together with stability lower bounds for absolute sums. Their \(\ell_1\)-sum result supplies lower estimates but does not state the exact identity above for an arbitrary Banach-space component adjoining an atomic \(\ell_1(\Gamma)\) summand. Haller, Pirk, and Veeorg studied Daugavet and \(\Delta\)-points in absolute sums at the qualitative level. The present formula gives a quantitative exact decomposition in this mixed setting and recovers the known pure \(\ell_1\) formula as a special case.

## Limitations
The proof uses the exact dual decomposition of an \(\ell_1\)-sum and the coordinate slices of \(\ell_1(\Gamma)\); it does not claim an analogous formula for other absolute norms. The finite checker is a consistency test, not a proof of the infinite-dimensional statement. Literature comparison found no exact prior statement with the same hypotheses and conclusion, but an unindexed or differently phrased result remains a residual novelty risk.

## References
1. G. Choi and M. Jung, “The Daugavet and Delta-constants of points in Banach spaces,” arXiv:2307.10647, first public version 20 July 2023; Proc. Royal Soc. Edinburgh Sect. A, DOI 10.1017/prm.2024.83.
2. R. Haller, K. Pirk, and T. Veeorg, “Daugavet- and Delta-points in absolute sums of Banach spaces,” arXiv:2001.06197, first public version 17 January 2020.
