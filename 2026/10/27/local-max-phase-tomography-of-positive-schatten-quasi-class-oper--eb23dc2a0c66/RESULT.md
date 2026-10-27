# Local max-phase tomography of positive Schatten quasi-class operators

## Finding
Fix \(0<p<1\) and a complex separable Hilbert space \(H\). For a positive injective \(A\in\mathcal S_p(H)\), a unit vector \(v\), and \(t>0\), set \(P_v x=\langle x,v\rangle v\) and
\[
\mathcal F_A(v,t)=\max\{\|A+tP_v\|_p^p,\|A-tP_v\|_p^p\},\qquad \|X\|_p^p=\operatorname{Tr}|X|^p.
\]
For every unit \(v\in\operatorname{Ran}A^{1/2}\), the positive-sided response recovers the inverse fractional quadratic form:
\[
\boxed{\lim_{t\downarrow0}\frac{\mathcal F_A(v,t)-\operatorname{Tr}A^p}{pt}=\langle v,A^{p-1}v\rangle.}
\]
In particular, suppose that positive injective operators \(A,B\in\mathcal S_p(H)\) satisfy \(cA\le B\le CA\) in Loewner order for some constants \(0<c\le C<\infty\). If for one \(t_0>0\), every unit vector \(v\in H\), and all \(0<t<t_0\),
\[
\mathcal F_A(v,t)=\mathcal F_B(v,t),
\]
then \(A=B\). Thus the local max-phase data against **positive rank-one projections alone** determine every operator within its positive order-comparability class, even when the operators have infinite rank and do not commute.

## Assumptions and scope
The Hilbert space may have any finite or countably infinite dimension. Positivity means self-adjoint and nonnegative; injectivity means trivial kernel, not bounded invertibility. For \(0<p<1\), \(\mathcal S_p\) is the Schatten quasi-ideal. The unbounded negative power \(A^{p-1}\) is interpreted as a positive self-adjoint operator with quadratic-form domain \(\operatorname{Dom}(A^{-(1-p)/2})\). The first formula is asserted on the explicitly stated dense set \(\operatorname{Ran}A^{1/2}\). The uniqueness assertion requires comparability of the two positive operators; it is not a theorem about arbitrary noncomparable operators, indefinite operators, or arbitrary max-phase isometries.

## Proof
**1. A positive rank-one fractional-trace derivative.** Write \(R_s=(A+sI)^{-1}\), \(c_p=\sin(\pi p)/\pi\). The scalar fractional-power representation and operator monotonicity give the trace identity, for \(t>0\),
\[
\begin{aligned}
\operatorname{Tr}[(A+tP_v)^p-A^p]
&=c_p\int_0^\infty s^p\operatorname{Tr}\bigl(R_s-(A+tP_v+sI)^{-1}\bigr)\,ds\\
&=c_p t\int_0^\infty\frac{s^p\langle v,R_s^2v\rangle}{1+t\langle v,R_sv\rangle}\,ds.
\end{aligned}
\]
Here the second equality is the rank-one resolvent identity; positivity of the integrand justifies Tonelli and limiting arguments. Divide by \(t\) and let \(t\downarrow0\). Monotone convergence and the spectral theorem yield the possibly infinite extended derivative
\[
\begin{aligned}
\lim_{t\downarrow0}\frac{\operatorname{Tr}[(A+tP_v)^p-A^p]}{t}
&=c_p\int_0^\infty s^p\langle v,(A+sI)^{-2}v\rangle\,ds\\
&=p\langle v,A^{p-1}v\rangle,
\end{aligned}
\]
since \(c_p\int_0^\infty s^p(\lambda+s)^{-2}\,ds=p\lambda^{p-1}\) for \(\lambda>0\). If \(v=A^{1/2}w\), this quantity is \(p\langle w,A^pw\rangle<\infty\).

**2. Resolving the max-phase branch.** For a nonzero \(v\in\operatorname{Ran}A^{1/2}\), write \(v=A^{1/2}w\) using the minimum-norm inverse image. Cauchy--Schwarz gives \(P_v\le\|w\|^2 A\) as quadratic forms. Hence \(A-tP_v\ge0\) whenever \(0<t\le\|w\|^{-2}\). Then \(A+tP_v\ge A-tP_v\ge0\), so operator monotonicity of \(x\mapsto x^p\) implies
\[
\mathcal F_A(v,t)=\operatorname{Tr}(A+tP_v)^p
\]
for all sufficiently small positive \(t\). Step 1 proves the boxed formula. The trace at \(t=0\) is the limit of the displayed max-profile because the \(p\)-power quasi-triangle inequality bounds its variation by \(t^p\).

**3. Common form cores under relative-order bounds.** Set \(\alpha=1-p\in(0,1)\). From \(cA\le B\le CA\), the variational characterization of inverse square-root forms yields
\[
\operatorname{Ran}A^{1/2}=\operatorname{Ran}B^{1/2}=:\mathcal C.
\]
Applying operator monotonicity to positive powers and then inverting in the quadratic-form sense yields
\[
C^{-\alpha}A^{-\alpha}\le B^{-\alpha}\le c^{-\alpha}A^{-\alpha}.
\]
Thus \(A^{-\alpha}\) and \(B^{-\alpha}\) have the same closed quadratic-form domain and equivalent form norms. Because \(A\) is compact and injective, spectral truncations \(\mathbf1_{[1/m,\infty)}(A)v\) of any vector in \(\operatorname{Dom}A^{-\alpha/2}\) lie in \(\mathcal C\) and converge in the form norm of \(A^{-\alpha}\). Hence \(\mathcal C\) is a form core for both negative powers.

**4. Uniqueness.** Taking \(t\downarrow0\) in the assumed profile equality first gives \(\operatorname{Tr}A^p=\operatorname{Tr}B^p\). For every nonzero \(v\in\mathcal C\), apply Step 2 to the normalized vector \(v/\|v\|\) for both operators. Their common local profiles and Step 1 show
\[
\langle v,A^{-\alpha}v\rangle=\langle v,B^{-\alpha}v\rangle.
\]
By polarization and the common-core result from Step 3, the associated closed quadratic forms coincide everywhere on their common domain. Uniqueness of the positive self-adjoint operator represented by a closed form gives \(A^{-\alpha}=B^{-\alpha}\); functional calculus and injectivity yield \(A=B\).

## Verification
The finite-dimensional checker `check_profile.py` evaluates the rank-one profile independently of the quadratic-form formula, checks the positive-branch threshold on noncommuting positive examples, compares numerical one-sided response quotients against spectral inverse-power quadratic forms, and confirms that the two compared operators have distinguishable measured responses. Run with `python check_profile.py`; NumPy is required. These finite checks are diagnostic only. The proof above handles all dimensions; no computation is used as evidence of infinite-dimensional completeness.

A concrete infinite-rank noncommuting class in the theorem is obtained on \(\ell^2(\mathbb N)\) by \(Ae_n=2^{-n/p}e_n\), and \(B=A^{1/2}(I+\varepsilon K)A^{1/2}\), where \(K\) is any bounded self-adjoint contraction and \(0<\varepsilon<1\). Then \((1-\varepsilon)A\le B\le(1+\varepsilon)A\), and both operators belong to \(\mathcal S_p\). Choosing \(K\) to couple neighboring coordinates makes \(A\) and \(B\) noncommuting.

## Relationship to prior work
Zhang and Liu (arXiv:2610.13271v1, 9 October 2026) establish max-phase uniqueness for finite matrices and the finite-rank ideal, and identify the infinite-rank unbounded negative-power domain as an unresolved obstacle. Their finite-dimensional Theorem 2.11 uses rank-one partial isometries in full; it does not state this local positive-projection recovery on infinite-rank order-comparable pairs. The present result uses a positive rank-one resolvent formula and a common unbounded-form core, rather than finite-support inversion.

Huang and Zhu (arXiv:2607.11244v1, 13 July 2026) study the stronger full-distance sphere-isometry problem, which does not itself identify operators from the weaker max-phase responses considered here. Dobosevych and Hryniv (2021) study reconstruction from full spectral data of rank-one perturbations with a known unperturbed operator; they do not supply the present inverse-power-form recovery from scalar max-phase traces of *two unknown operators*. This comparison distinguishes hypotheses and conclusions, not merely titles. No claim of priority beyond inspected evidence is made.

## Limitations
The result does not settle the unrestricted infinite-dimensional max-phase isometry conjecture. Comparability is a substantive hypothesis; the proof would need a separate argument for arbitrary positive pairs whose negative fractional form domains have no common core. The derivative formula is only used on \(\operatorname{Ran}A^{1/2}\); its extended behavior at other vectors does not establish which branch of the max is active. Independent priority review of older operator tomography literature remains appropriate.

## References
1. W. Zhang and Q. Liu, *On Surjective Max-Phase Isometries of Schatten \(p\)-Classes (\(0<p<1\))*, arXiv:2610.13271v1 (first public: 2026-10-09), https://arxiv.org/abs/2610.13271.
2. J. Huang and Y. Zhu, *Tingley's Problem for Schatten \(p\)-Classes*, arXiv:2607.11244 (first public: 2026-07-13), https://arxiv.org/abs/2607.11244.
3. O. Dobosevych and R. Hryniv, *Direct and Inverse Spectral Problems for Rank-One Perturbations of Self-adjoint Operators*, Integral Equations and Operator Theory 93 (2021), article 18, https://doi.org/10.1007/s00020-021-02630-y.
