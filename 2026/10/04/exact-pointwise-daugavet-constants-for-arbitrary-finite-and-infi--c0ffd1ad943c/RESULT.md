# Exact pointwise Daugavet constants for arbitrary finite and infinite \(\ell_p\)-sums
## Finding
Let \(1<p<\infty\), let \(\Gamma\) be a nonempty index set, and let \((X_\gamma)_{\gamma\in\Gamma}\) be a family of nonzero real Banach spaces, each with the Daugavet property. Set
\[
Z=\left(\bigoplus_{\gamma\in\Gamma}X_\gamma\right)_p.
\]
For \(z=(z_\gamma)_{\gamma\in\Gamma}\in B_Z\), define
\[
a_\gamma=\|z_\gamma\|,\qquad \rho=\|z\|,\qquad m=\inf_{\gamma\in\Gamma}a_\gamma.
\]
Then the Daugavet constant of \(z\) is exactly
\[
\operatorname{dc}_Z(z)=\left(\rho^p+(1+m)^p-m^p\right)^{1/p}.
\]
Equivalently,
\[
\operatorname{dc}_Z(z)=\inf_{\gamma\in\Gamma}
\left(\rho^p-a_\gamma^p+(1+a_\gamma)^p\right)^{1/p}.
\]

If \(\Gamma\) is infinite, then every \((a_\gamma)\in\ell_p(\Gamma)\) has \(\inf_\gamma a_\gamma=0\). Hence
\[
\operatorname{dc}_Z(z)=\left(1+\|z\|^p\right)^{1/p}
\quad (z\in B_Z),
\]
and, in particular,
\[
\operatorname{dc}_Z(z)=2^{1/p}\quad(z\in S_Z).
\]
Thus an infinite \(\ell_p\)-sum of Daugavet spaces has a completely flat pointwise Daugavet-constant profile on its unit sphere, although for \(p>1\) this value is strictly smaller than \(2\).

## Assumptions and scope
All spaces and functionals are real. The exponent satisfies \(1<p<\infty\), with conjugate exponent \(q=p/(p-1)\). The index set may have any nonzero cardinality. No separability assumption is made. The only geometric assumption on a summand is the Daugavet property.

For a Banach space \(X\) and \(x\in B_X\), the Daugavet constant is used in the equivalent slice form
\[
\operatorname{dc}_X(x)=\inf_S\sup_{y\in S}\|x-y\|,
\]
where the infimum ranges over slices of \(B_X\). This is the formulation established from Definition 2.1 in Choi--Jung.

## Proof
Fix \(z\in B_Z\), write \(a=(a_\gamma)\in\ell_p(\Gamma)_+\), and let \(S=S(B_Z,x^*,\delta)\) be an arbitrary slice, where \(x^*=(x_\gamma^*)\in S_{Z^*}\). Put \(b_\gamma=\|x_\gamma^*\|\). Then \(b=(b_\gamma)\in S_{\ell_q(\Gamma)}\). Define
\[
c_\gamma=b_\gamma^{q-1}.
\]
Because \((q-1)p=q\), one has \(c\in S_{\ell_p(\Gamma)}\) and
\[
\sum_\gamma b_\gamma c_\gamma=\sum_\gamma b_\gamma^q=1.
\]

Choose \(0<\eta<\delta\). If \(b_\gamma>0\) and \(a_\gamma>0\), set \(e_\gamma=z_\gamma/a_\gamma\). Since \(X_\gamma\) has the Daugavet property, \(e_\gamma\) is a Daugavet point, so there is \(u_\gamma\in B_{X_\gamma}\) such that
\[
\frac{x_\gamma^*}{b_\gamma}(u_\gamma)>1-\eta,
\qquad
\|e_\gamma-u_\gamma\|>2-\eta.
\]
If \(b_\gamma>0\) and \(a_\gamma=0\), choose \(u_\gamma\in B_{X_\gamma}\) with
\[
\frac{x_\gamma^*}{b_\gamma}(u_\gamma)>1-\eta;
\]
then \(\|u_\gamma\|>1-\eta\). For \(b_\gamma=0\), take \(u_\gamma=0\). Let \(w_\gamma=c_\gamma u_\gamma\). Then \(w=(w_\gamma)\in B_Z\) and
\[
x^*(w)> (1-\eta)\sum_\gamma b_\gamma c_\gamma=1-\eta>1-\delta,
\]
so \(w\in S\).

We use the elementary scaling lemma: if \(e_1,e_2\in B_X\) and \(\|e_1+e_2\|>1+\alpha\), then for all \(\lambda,\mu\ge0\),
\[
\|\lambda e_1+\mu e_2\|>\alpha(\lambda+\mu).
\]
Indeed,
\[
(\lambda+\mu)(1+\alpha)<(\lambda+\mu)\|e_1+e_2\|
\le \|\lambda e_1+\mu e_2\|+\lambda+\mu.
\]
Applying this with \(e_1=e_\gamma\), \(e_2=-u_\gamma\), and \(\alpha=1-\eta\) gives, when \(a_\gamma>0\),
\[
\|z_\gamma-w_\gamma\|>(1-\eta)(a_\gamma+c_\gamma).
\]
For \(a_\gamma=0\) the same lower bound follows from \(\|u_\gamma\|>1-\eta\), and for \(b_\gamma=0\) it is immediate because \(c_\gamma=0\). Therefore
\[
\sup_{y\in S}\|z-y\|\ge(1-\eta)\|a+c\|_p.
\]
Letting \(\eta\downarrow0\) and then using that \(S\) was arbitrary yields
\[
\operatorname{dc}_Z(z)\ge
\inf_{c\in S_{\ell_p(\Gamma)}\cap\ell_p(\Gamma)_+}\|a+c\|_p.
\]

It remains to compute this scalar infimum. Let
\[
F(t)=(1+t)^p-t^p,
\]
which is increasing on \([0,\infty)\). For any nonnegative \(c\in S_{\ell_p(\Gamma)}\), each coordinate with \(c_\gamma>0\) satisfies \(c_\gamma\le1\) and hence \(a_\gamma/c_\gamma\ge m\). Thus
\[
(a_\gamma+c_\gamma)^p-a_\gamma^p
=c_\gamma^p F(a_\gamma/c_\gamma)
\ge c_\gamma^p F(m).
\]
Summing gives
\[
\|a+c\|_p^p\ge\rho^p+F(m).
\]
Conversely, choosing \(c\) to be a coordinate unit vector at indices with \(a_\gamma\downarrow m\) gives the reverse inequality in the infimum. Hence
\[
\inf_{c\in S_{\ell_p}^+}\|a+c\|_p
=\left(\rho^p+(1+m)^p-m^p\right)^{1/p}.
\]

For the matching upper bound, fix \(\gamma_0\in\Gamma\) and choose \(x_0^*\in S_{X_{\gamma_0}^*}\). Consider the coordinate slice
\[
S_\delta=\{w\in B_Z:x_0^*(w_{\gamma_0})>1-\delta\}.
\]
For \(w\in S_\delta\), put \(r_\gamma=\|w_\gamma\|\). Then \(r\in B_{\ell_p}\), \(r_{\gamma_0}>1-\delta\), and coordinatewise triangle inequalities followed by Minkowski give
\[
\|z-w\|\le\|a+r\|_p
\le\|a+e_{\gamma_0}\|_p+\|r-e_{\gamma_0}\|_p.
\]
Moreover,
\[
\|r-e_{\gamma_0}\|_p^p
\le\delta^p+1-(1-\delta)^p\longrightarrow0.
\]
Therefore
\[
\operatorname{dc}_Z(z)\le\|a+e_{\gamma_0}\|_p
=\left(\rho^p-a_{\gamma_0}^p+(1+a_{\gamma_0})^p\right)^{1/p}.
\]
Taking the infimum over \(\gamma_0\) gives the reverse bound and completes the proof.

## Verification
The proof was reconstructed from the slice definition, with all quantifiers retained. The dual exponent identity \((q-1)p=q\), the scaling lemma, the scalar minimization, and the coordinate-slice upper bound were checked directly. No finite experiment is used to justify the infinite-dimensional statement.

Boundary checks agree with known cases. For a one-summand family the formula becomes \(\operatorname{dc}(z)=1+\|z\|\), as expected in a Daugavet space. If \(z=0\), it gives \(\operatorname{dc}(0)=1\). For an infinite family it gives the constant sphere value \(2^{1/p}\), whose infimum agrees with the established Daugavet slice-thickness value.

## Relationship to prior work
Choi and Jung introduced the Daugavet constant and proved its slice characterization. Their stability section treats absolute sums by general lower estimates and, for \(1<p<\infty\), an upper estimate \(2^{1/p}\) on coordinate-axis points. In the inspected full text, Proposition 4.1 is a lower bound for two-summand absolute sums and Proposition 4.8 supplies the axis upper bound; no formula there determines the Daugavet constant at an arbitrary point of an \(\ell_p\)-sum from its entire coordinate-norm profile.

Haller, Langemets, Lima, Nadel, and Rueda Zoca proved that if two summands have the Daugavet property, then the global slice Daugavet index of thickness of their \(\ell_p\)-sum is \(2^{1/p}\). That global infimum does not determine the pointwise constants. The present formula recovers that value by taking the infimum over the sphere, while additionally showing the finite-sum dependence on the smallest coordinate and the flat sphere profile for every infinite index set.

Focused semantic-database and web searches for the exact pointwise formula, coordinate-norm aliases, and stronger direct-sum coverage did not locate a statement implying the formula. This is evidence of non-coverage, not a proof of exhaustive novelty.

## Limitations
Only real Banach spaces and \(1<p<\infty\) are covered. The theorem assumes every summand has the Daugavet property and makes no claim for general absolute sums, for \(p=1\) or \(p=\infty\), or for the \(\Delta\)-constant. The originality comparison is limited to the inspected primary full texts and focused searches; terminology or results outside those sources may still overlap.

## References
1. G. Choi and M. Jung, *The Daugavet and Delta-constants of points in Banach spaces*, arXiv:2307.10647. First public version: 2023-07-20. In particular, Definition 2.1 and Section 4.
2. R. Haller, J. Langemets, V. Lima, R. Nadel, and A. Rueda Zoca, *On Daugavet indices of thickness*, arXiv:2005.02045. First public version: 2020-05-05. In particular, Theorem 2.6.
