# Exact real-spectrum boundary and optimal transverse field for a centrally perturbed Ising trimer

## Finding

Consider the open three-spin Ising Hamiltonian with a single non-Hermitian raising term at its middle spin,
\[
H=-\frac J4(\sigma_1^x\sigma_2^x+\sigma_2^x\sigma_3^x)
-\frac h2(\sigma_1^z+\sigma_2^z+\sigma_3^z)
+\gamma\sigma_2^+,
\qquad J>0,\quad h\ge0,\quad\gamma\ge0,
\]
with \(\sigma^+=(\sigma^x+i\sigma^y)/2\). Define \(q=h/J\), \(p=\gamma/J\), \(z=q^2\), \(u=p^2\). For \(z>0\), set
\[
\begin{aligned}
\mathcal D(u,z)={}&16u^3-(8+208z+944z^2)u^2\\
&+(1+20z+224z^2+800z^3-2048z^4)u\\
&+16z^3+208z^4+2048z^5.
\end{aligned}
\]
There are precisely two distinct positive roots of \(\mathcal D(\cdot,z)\). Write the smaller as \(u_-(z)\). **All eight eigenvalues of \(H\) are real exactly for**
\[
0\le p^2\le u_-(q^2).
\]
For every \(q>0\), the sharp boundary obeys
\[
q^2<u_-(q^2)<q^2+\tfrac14.
\]
At \(p^2=u_-(q^2)\), a positive squared-energy root becomes double in the six-dimensional reflection-even sector; the theorem concerns eigenvalue reality, not a classification of Jordan blocks. At \(h=0\) the reality boundary is \(p=1/2\).

**Optimal field.** The function \(p_c(q)=\sqrt{u_-(q^2)}\) has one and only one global minimum on \([0,\infty)\). It occurs at \(q_*=\sqrt{z_*}\), where \(z_*\) is the unique positive solution of
\[
3072z^3+876z^2+52z-3=0.
\]
More precisely,
\[
q_*=0.18654891982879065679\ldots,\qquad
p_c(q_*)=0.37705775971022272113\ldots.
\]
Thus the real-spectrum transition cannot be induced in this trimer by any perturbation below \(0.37705775\,J\), regardless of the nonnegative transverse field. A weak field initially *lowers* the threshold while a strong field raises it:
\[
p_c(q)=\tfrac12-\sqrt2\,q+\tfrac92q^2+O(q^3)\quad(q\downarrow0),
\qquad
p_c(q)=q+\frac1{64q}+O(q^{-3})\quad(q\to\infty).
\]
This is an exact three-spin statement, not a claim of a chain-length-independent gap.

## Assumptions and scope

All parameters are real with \(J>0\), \(h,\gamma\ge0\); the chain is open, has exactly three spin-\(1/2\) sites, and the non-Hermitian term acts only on the central site. The term \(\sigma_2^+\) has the usual matrix \(\begin{psmallmatrix}0&1\\0&0\end{psmallmatrix}\) in the \(\sigma^z\)-eigenbasis. The spectral-reality condition refers to *all* complex eigenvalues, counted with algebraic multiplicity. Isolated real degeneracies inside this parameter domain do not alter this definition. The result makes no statement about positive-metric quasi-Hermiticity at the boundary or about spin chains with four or more sites.

## Proof

**1. Symmetric-sector factorization.** By dividing by \(J\), normalize \(J=1\). Exchange of the outer two spins commutes with \(H\). The outer-spin singlet sector is two-dimensional; because \(\sigma_1^x+\sigma_3^x\) and \(\sigma_1^z+\sigma_3^z\) vanish on its one-dimensional outer factor, its effective matrix is \(-q\sigma^z/2+p\sigma^+\), with eigenvalues \(\pm q/2\). The reflection-even sector is six-dimensional. In the triplet basis \(\lvert\uparrow\uparrow\rangle,(\lvert\uparrow\downarrow\rangle+\lvert\downarrow\uparrow\rangle)/\sqrt2,\lvert\downarrow\downarrow\rangle\), the outer-spin sum \(\sigma_1^x+\sigma_3^x\) is \(\sqrt2\) times the path adjacency on three vertices, and \(\sigma_1^z+\sigma_3^z=\operatorname{diag}(2,0,-2)\). Directly evaluating this six-dimensional determinant gives
\[
\det(\lambda I-H/J)=(\lambda^2-z/4)\,F(\lambda^2;u,z)/64,
\]
where
\[
\begin{aligned}
F(y;u,z)={}&64y^3-(32+176z)y^2\\
&+(4+48z+76z^2-16u)y\\
&-z(1-3z)^2-12uz.
\end{aligned}
\]
The attached independent symbolic checker constructs the original eight-dimensional Pauli matrix and confirms this factorization identically, rather than inferring it from sampled eigenvalues.

**2. Complete all-real criterion.** The discriminant of \(F\) as a cubic in \(y\) is exactly \(65536\mathcal D(u,z)\). For \(z>0\),
\[
\mathcal D(0,z)=16z^3(1+13z+128z^2)>0,\quad
\mathcal D(z,z)=z(1+4z)^3>0,
\]
whereas
\[
\mathcal D(z+\tfrac14,z)=-z(8+83z+224z^2+448z^3)<0.
\]
As \(\mathcal D(u,z)\sim16u^3>0\) for \(u\to\infty\), there are positive roots on both sides of \(z+1/4\). Descartes' rule of signs applied to \(\mathcal D\) as a polynomial in \(u\) gives at most two positive roots, counted with multiplicity (the coefficient signs are either \(+,-,+,+\) or \(+,-,-,+\)). Hence these are precisely two simple positive roots and \(z<u_-(z)<z+1/4<u_+(z)\).

At \(u=0\), the Hamiltonian is Hermitian, so all three roots of \(F\) are nonnegative; its positive discriminant makes them distinct. For \(u>0\), \(F(0;u,z)=-z[(1-3z)^2+12u]<0\), so no squared-energy root can pass through zero. Therefore all three \(y\)-roots stay strictly positive while \(0<u<u_-(z)\), and remain real and nonnegative at the endpoint. Between \(u_-\) and \(u_+\), the discriminant is negative, producing a nonreal conjugate pair of squared energies and hence nonreal energies. For \(u>u_+\), the squared energies are again real, but two are negative: for sufficiently large \(u\), the pairwise root sum \((4+48z+76z^2-16u)/64\) is negative, ruling out three positive roots; the positive root product and positive root sum force precisely two negatives. Their signs cannot change for \(u>u_+\) because \(F(0)<0\). Thus nonreal energies persist. The case \(u=0\), including a possible zero eigenvalue, follows by Hermiticity. At \(z=0\), one has \(F(y;u,0)=4y[(4y-1)^2-4u]\), giving the stated \(p_c(0)=1/2\).

**3. Unique globally optimal field.** The root \(u_-(z)\) is smooth for \(z>0\) because it is a simple root of \(\mathcal D\). Its derivative can vanish only when both \(\mathcal D=0\) and \(\partial_z\mathcal D=0\). Eliminating \(u\) exactly yields
\[
\operatorname{Res}_u(\mathcal D,\partial_z\mathcal D)
=-32768z^2(4z+1)^3(176z^2+25z+2)^3
(3072z^3+876z^2+52z-3).
\]
The last factor has precisely one positive root, since it starts negative and has positive derivative for \(z\ge0\). This gives at most one stationary point of \(u_-\). For \(q\downarrow0\), expansion of the smaller positive discriminant root gives
\[
u_-(q^2)=\tfrac14-\sqrt2\,q+\tfrac{13}{2}q^2+O(q^3),
\]
so the derivative is initially negative. For large \(z\), writing \(u=z+t\) in the discriminant, with \(0<t<1/4\), the leading power of \(z\) is \((64-2048t)z^4\). Its vanishing yields \(u_-(z)=z+1/32+O(z^{-1})\), whose derivative is eventually positive. Thus the stationary point exists, is unique, and is a strict global minimum. Substitution into \(p_c=\sqrt u\) proves both expansions above. The numerical brackets follow from root isolation of the displayed polynomial and the smaller discriminant root; they are not used to establish uniqueness.

## Verification

Run \(\texttt{python check_threshold.py}\) with SymPy and mpmath installed. The script independently constructs the full Pauli Hamiltonian, checks the characteristic factorization, cubic discriminant, sign certificates at both bracketing values, exact elimination resultant, the low- and high-field asymptotic coefficients, and rigorous algebraic identities for the zero-field limit; it also calculates high-precision approximations for the unique minimum. These symbolic identities can be inspected directly from the provided formulas without relying on the executable. Numerical evaluations are only illustrative, not substitutes for the all-parameter sign and resultant arguments.

## Relationship to prior work

Muldoon and Joglekar (arXiv:2304.10064, Sections II–III) defined the centrally and edge-perturbed Ising-chain Hamiltonian, established its zero-field single-site thresholds, and investigated transverse-field effects using diagonalization in larger spin chains. The present result addresses exactly three sites, retains the full transverse-field dependence, and proves the whole all-real spectral boundary and unique positive minimum algebraically; the source's zero-field result is recovered, not claimed as new. Starkov, Fistul, and Eremin (arXiv:2302.14672) studied exceptional points in a different Ising model with a spatially staggered imaginary longitudinal field. Barnett and Joglekar (arXiv:2302.13204) studied exceptional-point curves for tridiagonal single-particle chains with balanced gain and loss; that does not imply this interacting three-spin central-raising threshold. Generic cubic discriminant theory is standard mathematics; the asserted contribution is its complete evaluation and global classification for this specific physically motivated model.

## Limitations

This is a finite, exactly three-spin spectral statement, not a thermodynamic phase transition. It does not establish a comparable positive global threshold for longer chains. The result does not analyze dynamics, amplification rates, condition numbers, nonorthogonal modes, exceptional-point response, or robustness against extra couplings. An equivalent closed-form calculation may exist in less-indexed literature; no independent scientific audit has been performed.

## References

1. J. Muldoon and Y. N. Joglekar, “\(\mathcal{PT}\)-Symmetry breaking in quantum spin chains with exceptional non-Hermiticities,” arXiv:2304.10064 (first submitted 2023-04-20), *Physical Review A* **108**, 062205 (2023). https://arxiv.org/abs/2304.10064
2. G. A. Starkov, M. V. Fistul, and I. M. Eremin, “Formation of Exceptional Points in pseudo-Hermitian Systems,” arXiv:2302.14672 (2023), *Physical Review A* **108**, 022206. https://arxiv.org/abs/2302.14672
3. J. L. Barnett and Y. N. Joglekar, “Effects of detuning on \(\mathcal{PT}\)-symmetric, tridiagonal, tight-binding models,” arXiv:2302.13204 (2023). https://arxiv.org/abs/2302.13204
