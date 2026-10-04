# Exact Daugavet constants of arbitrary \(c_0\)-sums
## Finding
Let \(\Gamma\) be a nonempty index set and let \((X_\gamma)_{\gamma\in\Gamma}\) be a family of nonzero real Banach spaces. Put
\[
Z=\left(\bigoplus_{\gamma\in\Gamma}X_\gamma\right)_{c_0},
\]
where an element \(x=(x_\gamma)\) satisfies: for every \(\varepsilon>0\), only finitely many \(\gamma\) have \(\|x_\gamma\|\ge\varepsilon\). For finite \(\Gamma\), this is the usual finite \(\ell_\infty\)-sum.

For every \(x=(x_\gamma)\in B_Z\),
\[
\boxed{\operatorname{dc}_Z(x)=\sup_{\gamma\in\Gamma}\operatorname{dc}_{X_\gamma}(x_\gamma).}
\]
Thus finite \(\ell_\infty\)-sums satisfy the corresponding maximum formula. For scalar summands, the formula recovers both the known finite-dimensional identity on \(\ell_\infty^N\) and the known identity \(\operatorname{dc}_{c_0}(x)=1\).

## Assumptions and scope
All Banach spaces are real and nonzero. For a Banach space \(X\), \(x\in B_X\), \(x^*\in S_{X^*}\), and \(\alpha>0\), write
\[
S(B_X,x^*,\alpha)=\{u\in B_X:x^*(u)>1-\alpha\}.
\]
The Daugavet constant introduced by Choi and Jung is equivalently
\[
\operatorname{dc}_X(x)=\inf_{S}\ \sup_{u\in S}\|x-u\|,
\]
where the infimum runs over all slices \(S\) of \(B_X\). This is the slice-radius form of their Definition 2.1.

The dual of the \(c_0\)-sum is the \(\ell_1\)-sum
\[
Z^*=\left(\bigoplus_{\gamma\in\Gamma}X_\gamma^*\right)_{\ell_1}.
\]
Hence every \(f=(f_\gamma)\in S_{Z^*}\) satisfies \(\sum_\gamma\|f_\gamma\|=1\), and its mass can be approximated arbitrarily well on a finite subset of \(\Gamma\).

## Proof
Set
\[
M=\sup_{\gamma\in\Gamma}\operatorname{dc}_{X_\gamma}(x_\gamma).
\]
We prove both inequalities.

First fix \(\gamma_0\in\Gamma\) and an arbitrary slice
\[
S=S(B_Z,f,\alpha),\qquad f=(f_\gamma)\in S_{Z^*},\quad \alpha>0.
\]
Let \(a_\gamma=\|f_\gamma\|\). Choose a finite set \(F\subset\Gamma\) containing \(\gamma_0\) such that
\[
\tau:=\sum_{\gamma\notin F}a_\gamma<\alpha/3,
\]
and choose \(\eta>0\) with \(\eta<\min\{1,\alpha/3\}\).

Suppose first that \(a_{\gamma_0}>0\). By the slice-radius characterization in \(X_{\gamma_0}\), for every \(\varepsilon>0\) there is \(u_{\gamma_0}\in B_{X_{\gamma_0}}\) such that
\[
\frac{f_{\gamma_0}(u_{\gamma_0})}{a_{\gamma_0}}>1-\eta
\quad\text{and}\quad
\|x_{\gamma_0}-u_{\gamma_0}\|>
\operatorname{dc}_{X_{\gamma_0}}(x_{\gamma_0})-\varepsilon.
\]
For each \(\gamma\in F\setminus\{\gamma_0\}\) with \(a_\gamma>0\), choose \(u_\gamma\in B_{X_\gamma}\) with
\[
f_\gamma(u_\gamma)>(1-\eta)a_\gamma.
\]
If \(a_\gamma=0\), take \(u_\gamma=0\), and set \(u_\gamma=0\) for \(\gamma\notin F\). Then \(u=(u_\gamma)\in B_Z\), it has finite support, and
\[
f(u)>(1-\eta)\sum_{\gamma\in F}a_\gamma=(1-\eta)(1-\tau)>1-\alpha.
\]
Hence \(u\in S\), and
\[
\sup_{v\in S}\|x-v\|\ge
\operatorname{dc}_{X_{\gamma_0}}(x_{\gamma_0})-\varepsilon.
\]
Letting \(\varepsilon\downarrow0\) gives the desired component lower bound.

If \(a_{\gamma_0}=0\), use the same finite norming construction on \(F\setminus\{\gamma_0\}\), but choose
\[
u_{\gamma_0}=-\frac{x_{\gamma_0}}{\|x_{\gamma_0}\|}
\]
when \(x_{\gamma_0}\ne0\), and choose any unit vector of \(X_{\gamma_0}\) when \(x_{\gamma_0}=0\). This does not change \(f(u)\), and
\[
\|x_{\gamma_0}-u_{\gamma_0}\|=1+\|x_{\gamma_0}\|.
\]
Since every two points of \(B_{X_{\gamma_0}}\) are at distance at most \(1+\|x_{\gamma_0}\|\) from \(x_{\gamma_0}\),
\[
\operatorname{dc}_{X_{\gamma_0}}(x_{\gamma_0})\le1+\|x_{\gamma_0}\|.
\]
Thus the same lower bound follows. Because the global slice and \(\gamma_0\) were arbitrary,
\[
\operatorname{dc}_Z(x)\ge M.
\]

For the reverse inequality, first note the elementary estimate
\[
\operatorname{dc}_X(y)\ge1-\|y\|\qquad(y\in B_X).
\]
Indeed, every slice of \(B_X\) contains points whose norms are arbitrarily close to \(1\), so its supremal distance from \(y\) is at least \(1-\|y\|\). Consequently, if \(\Gamma\) is infinite, the \(c_0\) condition implies \(M\ge1\).

Fix \(\varepsilon>0\). If \(\Gamma\) is infinite, choose a nonempty finite set \(F\subset\Gamma\) such that
\[
\|x_\gamma\|<\varepsilon/3\qquad(\gamma\notin F).
\]
If \(\Gamma\) is finite, take \(F=\Gamma\). For each \(\gamma\in F\), choose a slice
\[
S_\gamma=S(B_{X_\gamma},\varphi_\gamma,\alpha_\gamma)
\]
with
\[
\sup_{u\in S_\gamma}\|x_\gamma-u\|<
\operatorname{dc}_{X_\gamma}(x_\gamma)+\varepsilon/3
\le M+\varepsilon/3.
\]
Choose positive numbers \((\lambda_\gamma)_{\gamma\in F}\) with \(\sum_{\gamma\in F}\lambda_\gamma=1\), and define the finite-support functional
\[
\Phi=(\lambda_\gamma\varphi_\gamma)_{\gamma\in F}\in S_{Z^*}.
\]
Take
\[
0<\delta<\min_{\gamma\in F}\lambda_\gamma\alpha_\gamma.
\]
If \(z=(z_\gamma)\in S(B_Z,\Phi,\delta)\), then necessarily \(z_\gamma\in S_\gamma\) for every \(\gamma\in F\). Otherwise, for some \(\gamma\in F\),
\[
\Phi(z)\le1-\lambda_\gamma\alpha_\gamma\le1-\delta,
\]
contradicting membership in the slice. Therefore, for \(\gamma\in F\),
\[
\|x_\gamma-z_\gamma\|<M+\varepsilon/3.
\]
If \(\Gamma\) is infinite and \(\gamma\notin F\), then
\[
\|x_\gamma-z_\gamma\|\le\|x_\gamma\|+\|z_\gamma\|
<1+\varepsilon/3\le M+\varepsilon/3.
\]
There is no tail in the finite case. Hence
\[
\sup_{z\in S(B_Z,\Phi,\delta)}\|x-z\|<M+\varepsilon.
\]
Taking the infimum over slices and then letting \(\varepsilon\downarrow0\) gives
\[
\operatorname{dc}_Z(x)\le M.
\]
Combining the two inequalities proves the formula.

## Verification
The proof was replayed from the slice definition with the quantifiers and both exceptional branches made explicit. In the lower bound, the potentially infinite dual functional is never normed by an infinite unit sequence: only a finite set carrying all but an arbitrarily small \(\ell_1\)-tail is used, so the witness genuinely belongs to the \(c_0\)-sum. The case in which the selected dual coordinate vanishes is handled separately by an opposite unit vector.

In the upper bound, the finite convex combination of component functionals has dual norm exactly \(1\), and the choice \(\delta<\lambda_\gamma\alpha_\gamma\) forces every selected coordinate into its prescribed component slice. For an infinite index set the estimate \(M\ge1\) is proved before the tail estimate is used. No finite experiment, optimization routine, or unproved computational certificate is part of the proof.

## Relationship to prior work
Choi and Jung introduced the Daugavet constant and \(\Delta\)-constant of a point. Their scalar computations include the exact finite-dimensional formula on \(\ell_\infty^N\) and the identity \(\operatorname{dc}_{c_0}(x)=1\). Their stability section proves general lower estimates for absolute sums, including the \(\ell_\infty\) setting, rather than the componentwise equality above for arbitrary Banach summands and arbitrary \(c_0\)-families.

The displayed theorem simultaneously recovers those scalar \(\ell_\infty\) and \(c_0\) results and upgrades the one-sided direct-sum stability information to an exact compositional law for the Daugavet constant. Targeted searches for pointwise Daugavet constants of \(c_0\)-sums, \(\ell_\infty\)-sums, componentwise maxima, and equivalent slice-radius formulations found no statement with the same objects and quantifiers. This supports noncoverage but cannot exclude an equivalent result under different terminology in unindexed literature.

## Limitations
The result is for real Banach spaces and the Daugavet constant. It does not assert an analogous formula for the \(\Delta\)-constant, for complex spaces, or for infinite \(\ell_\infty\)-products without the \(c_0\) tail condition. The originality comparison is limited to the inspected primary paper and targeted database/web searches; bibliographic noncoverage is therefore a residual risk rather than a uniqueness theorem.

## References
1. G. Choi and M. Jung, *The Daugavet and Delta-constants of points in Banach spaces*, arXiv:2307.10647v1, first submitted 2023-07-20; later published in *Proceedings of the Royal Society of Edinburgh Section A: Mathematics*, DOI 10.1017/prm.2024.83.
