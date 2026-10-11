# Exact pointwise Daugavet constants in mixed \(\ell_p\)–\(\ell_1\) sums

## Finding
For \(1<p<\infty\), let \(X\) be a nonzero real Banach space with the Daugavet property, and let \(\Gamma\) be any nonempty set. Equip \(Z=X\oplus_p\ell_1(\Gamma)\) with its standard sum norm. For \(z=(x,v)\in B_Z\), put
\[
A=\|x\|_X,\qquad B=\|v\|_1,\qquad M=\|v\|_\infty.
\]
Then the pointwise Daugavet constant is
\[
\boxed{\operatorname{dc}_Z(z)=\min_{0\le s\le1}
\left[(A+(1-s^p)^{1/p})^p+(B-M+|s-M|)^p\right]^{1/p}.}
\tag{1}
\]
The scalar minimization is on a compact interval, so its minimum is attained. Thus the full, possibly infinite-dimensional slice invariant depends on only the three natural parameters \(A,B,M\), not on the other atomic coordinates or the isometric structure of \(X\).

In the Hilbert-sum case \(p=2\), for every \(v\in S_{\ell_1(\Gamma)}\) the formula has the sharp two-regime specialization
\[
\boxed{
\operatorname{dc}_{X\oplus_2\ell_1(\Gamma)}(0,v)^2=
\begin{cases}
2(1-M),&0<M\le\frac12,\\
4(1-M)^2,&\frac12\le M\le1.
\end{cases}}
\tag{2}
\]
The two pieces agree at the genuine optimizer transition \(M=1/2\). For \(v=(1/5,1/5,1/5,1/5,1/5)\), (2) gives \(\operatorname{dc}(0,v)=\sqrt{8/5}\). Here the optimal radial coefficient \(s=1/5\) is strictly better than the endpoints \(s=0\) and \(s=1\); it exhibits a mixed slice, rather than one concentrated in either summand.

## Assumptions and scope
The scalar field is real, \(1<p<\infty\), and \(\Gamma\) need not be countable. Every \(v\in\ell_1(\Gamma)\) has countable support. If \(v\ne0\), its largest coordinate modulus \(M\) is attained; for \(v=0\) put \(M=0\) and choose any coordinate in constructions below. Necessarily \(A^p+B^p\le1\). The Daugavet property is needed for the full mixed-coordinate identity; no smoothness or separability is assumed of \(X\).

A slice of \(B_Z\) means
\[
S(\Phi,\delta)=\{w\in B_Z:\Phi(w)>1-\delta\},
\qquad\Phi\in S_{Z^*},\quad\delta>0.
\]
The Choi–Jung pointwise constant is equivalently
\[
\operatorname{dc}_Z(z)=\inf_{S\text{ a slice of }B_Z}\sup_{w\in S}\|z-w\|_Z.
\tag{3}
\]
The Daugavet property says that, for any \(e\in S_X\), any slice \(T\) of \(B_X\) and every \(\epsilon>0\), there exists \(u\in T\) with \(\|e-u\|>2-\epsilon\).

## Proof
**A scalar discrepancy lemma.** If \(0\le c\le M\le B\) and \(0\le s\le1\), then
\[
B-c+|s-c|\ge B-M+|s-M|.
\tag{4}
\]
Indeed, for fixed \(s\), the function \(c\mapsto B-c+|s-c|\) is nonincreasing, being constant for \(c\ge s\) and affine with slope \(-2\) for \(c\le s\).

Let \(q=p/(p-1)\). Every norm-one functional of \(Z\) has the form \(\Phi=(F,G)\in X^*\oplus_q\ell_\infty(\Gamma)\) with
\[
\alpha=\|F\|,\quad\beta=\|G\|_\infty,\quad
\alpha^q+\beta^q=1.
\]
Set \(r=\alpha^{q-1}\), \(s=\beta^{q-1}\). By the dual exponent identity, \(r^p+s^p=1\) and \(\alpha r+\beta s=1\).

**Every slice contains a distant witness.** Fix any slice \(S(\Phi,\delta)\). If \(\beta>0\), choose \(\gamma\in\Gamma\) with \(|G_\gamma|>\beta-\epsilon\), and let \(\sigma\in\{-1,1\}\) be the sign of \(G_\gamma\). If \(\beta=0\), choose any \(\gamma\) and \(\sigma\); then \(s=0\).

We can choose \(u\in B_X\) with \(F(u)>\alpha-\epsilon\) and
\[
\|x-r u\|>A+r-\epsilon.
\tag{5}
\]
Here and below the tolerance may be made arbitrarily small. To prove (5), when \(A>0\) and \(\alpha>0\) use the Daugavet property at \(x/A\) in a sufficiently thin slice determined by \(F/\alpha\). If \(\|x/A-u\|>2-\eta\), the elementary scaling inequality
\[
\|A(x/A)-ru\|\ge A+r-\max\{A,r\}\eta
\tag{6}
\]
follows by applying the triangle inequality to the difference after separating the unequal nonnegative coefficients. If \(A=0\), a norming slice for \(F\) gives \(\|u\|\to1\); if \(\alpha=0\), then \(r=0\) and (5) holds without an \(X\)-witness.

Take \(W=(ru,s\sigma e_\gamma)\in B_Z\). By \(\alpha r+\beta s=1\), both choices can be made sufficiently norming to guarantee \(\Phi(W)>1-\delta\), so \(W\in S\). Let \(c=|v_\gamma|\le M\). The triangle inequality on one coordinate and (4) give
\[
\|v-s\sigma e_\gamma\|_1
=B-c+|v_\gamma-s\sigma|
\ge B-c+|s-c|\ge B-M+|s-M|.
\tag{7}
\]
Letting \(\epsilon\downarrow0\) in (5) and (7) shows
\[
\sup_{W\in S}\|z-W\|_Z^p
\ge (A+r)^p+(B-M+|s-M|)^p.
\tag{8}
\]
This is at least the minimum of the expression on the right of (1), raised to \(p\). Since the slice was arbitrary, (3) gives the lower bound in (1).

**Sharp near-atomic slices.** Conversely, fix any \(s\in[0,1]\) and put \(r=(1-s^p)^{1/p}\). Choose \(\gamma_0\) with \(|v_{\gamma_0}|=M\) (arbitrary when \(M=0\)), and let \(\sigma\) be its sign when \(M>0\) (otherwise arbitrary). Choose a unit functional \(h\in X^*\). Define
\[
\Psi=(r^{p-1}h,\ s^{p-1}\sigma e_{\gamma_0}^*)\in S_{Z^*}.
\tag{9}
\]
Consider the slices \(S_\delta=S(\Psi,\delta)\) as \(\delta\downarrow0\). For \((u,w)\in S_\delta\), write \(R=\|u\|\) and \(T=\|w\|_1\). Then \(R^p+T^p\le1\), and
\[
1-\delta<r^{p-1}h(u)+s^{p-1}\sigma w_{\gamma_0}
\le r^{p-1}R+s^{p-1}T\le1.
\tag{10}
\]
Equality in Hölder's inequality for nonnegative vectors in \(\ell_p^2\) is unique. Compactness of its unit ball therefore implies **uniformly for every point of \(S_\delta\)** that \((R,T)\to(r,s)\). If \(s>0\), the nonnegative deficit \(s^{p-1}(T-\sigma w_{\gamma_0})\) tends uniformly to zero. Hence \(w\to s\sigma e_{\gamma_0}\) in \(\ell_1\); when \(s=0\), simply \(T\to0\). Also \(R\to r\) in either case. Consequently
\[
\limsup_{\delta\downarrow0}\sup_{(u,w)\in S_\delta}
\|z-(u,w)\|_Z^p
\le(A+r)^p+\|v-s\sigma e_{\gamma_0}\|_1^p
=(A+r)^p+(B-M+|s-M|)^p.
\tag{11}
\]
The slice-infimum (3) is thus no larger than this expression for **every** \(s\in[0,1]\). Taking the minimum proves the reverse bound and (1). None of the reasoning requires \(\Gamma\) to be finite.

**Exact transition for \(p=2\) and pure atomic unit vectors.** Put \(A=0\), \(B=1\), and \(0<M\le1\). The scalar objective in (1), squared, becomes
\[
F_M(s)=1-s^2+(1-M+|s-M|)^2.
\]
On \(0\le s\le M\), this is \(2-2s\), decreasing. On \(M\le s\le1\), it is
\[
1+(1-2M)^2+2(1-2M)s,
\]
which is nondecreasing if \(M\le1/2\) and nonincreasing if \(M\ge1/2\). Hence the minimizing \(s\) is \(M\) in the first regime and \(1\) in the second; their respective squared values are \(2(1-M)\) and \(4(1-M)^2\). This proves (2).

## Verification
The standalone `verify.py` uses Python 3's exact rational arithmetic to check the monotonic one-coordinate discrepancy (4) for 3,146 admissible tuples, 2,736 Euclidean radial profiles for \(p=2\), and 10,100 exact rational tests of the two phase branches in (2). It also verifies that five equal atomic masses have objective \(8/5\) at \(s=1/5\), strictly below the values at both radial endpoints. Reproduce with `python verify.py` from the directory containing this document and the checker. These tests support arithmetic; the proof for all real \(p>1\), arbitrary Banach spaces and infinite index sets is analytic in (4)–(11).

## Relationship to prior work
Choi and Jung (arXiv:2307.10647, Sections 2 and 4) introduce the Daugavet constant, provide general lower estimates for absolute sums (Proposition 4.1) and coordinate-axis upper estimates for \(\ell_p\) sums (Proposition 4.8). Neither proposition computes a mixed Daugavet–atomic pointwise profile as in (1), nor the phase boundary (2). Haller, Pirk and Veeorg (arXiv:2001.06197) study qualitative extremal points under absolute sums, not these quantitative constants. Haller and collaborators (arXiv:2005.02045) compute global slice-thickness indices for sums of Daugavet spaces rather than mixed atomistic pointwise constants.

A separately published exact result for \(X\oplus_1\ell_1(\Gamma)\) identifies a largest-atom penalty at the **\(p=1\) endpoint**; it does not imply the nonlinear radial optimization at \(1<p<\infty\). Separate published results for \(\mathbb R\oplus_pY\) with a Daugavet point in \(Y\) cover just the **one-atom instance** of (1), where no nontrivial atomic spreading can occur. Other published \(\ell_p\) formulas assume **all** summands have the Daugavet property, whereas an atomic \(\ell_1\) summand does not. The strict mixed optimizer for five atoms shows why neither endpoint comparison determines (1).

## Limitations
The full formula assumes the Daugavet property for the non-atomic Banach summand, real scalars, and \(1<p<\infty\). It does not assert a corresponding formula for a general Banach summand lacking Daugavet points, for arbitrary second summands, for \(p=1\) or \(p=\infty\), or for the pointwise Delta constant. The scalar minimum for general \(p\) is an **explicit one-dimensional variational formula**, not a uniform elementary closed form; a closed form is proved only for the specialization (2). Numerical or finite exact tests do not prove the infinite-dimensional theorem. The originality comparison is limited to named inspected literature and focused searches; equivalent unindexed formulations remain possible.

## References
1. G. Choi and M. Jung, *The Daugavet and Delta-constants of points in Banach spaces*, arXiv:2307.10647, first publicly posted 2023-07-20 (primary MSC 46B04); especially Definition 2.1 and Propositions 4.1, 4.8.
2. R. Haller, K. Pirk and T. Veeorg, *Daugavet- and Delta-points in absolute sums of Banach spaces*, arXiv:2001.06197 (2020).
3. R. Haller, J. Langemets, V. Lima, R. Nadel and A. Rueda Zoca, *On Daugavet indices of thickness*, arXiv:2005.02045 (2020).
