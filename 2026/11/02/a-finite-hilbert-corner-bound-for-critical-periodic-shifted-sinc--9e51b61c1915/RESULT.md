# A finite Hilbert-corner bound for critical periodic shifted-sinc stability

## Finding

Let \(p\ge 4\) be an integer and put \(L=\lfloor p/2\rfloor\). For a sign vector \(s\in\{-1,+1\}^{p}\), set
\[
(H_{p,s})_{jr}=p^{-1/2}\exp\!\left(-\frac{2\pi i j}{p}\left(r+\frac{s_r}{4}\right)\right),\qquad 0\le j,r<p.
\]
Define the optimal critical periodic lower squared synthesis bound
\[
A_p=\min_{s\in\{-1,+1\}^{p}}\lambda_{\min}(H_{p,s}^{*}H_{p,s}).
\]
For \(s^{\mathrm{blk}}\) with consecutive \(+1\) on residues \(0,\ldots,\lceil p/2\rceil-1\) and \(-1\) on the remaining residues, write \(A_p^{\mathrm{blk}}=\lambda_{\min}(H_{p,s^{\mathrm{blk}}}^{*}H_{p,s^{\mathrm{blk}}})\). Let \(\mathcal H_L=((j+k+1)^{-1})_{0\le j,k<L}\) be the classical finite Hilbert matrix, and let \(\Lambda_L=\lambda_{\max}(\mathcal H_L)\).

**Theorem (critical upper half of the periodic logarithmic-degeneration problem).** For every integer \(p\ge4\),
\[
0<A_p\le A_p^{\mathrm{blk}}\le 1-\frac{\Lambda_{\lfloor p/2\rfloor}}{\pi}.
\]
Consequently,
\[
\boxed{\displaystyle\limsup_{p\to\infty}(\log p)^2 A_p\le\frac{\pi^4}{2}.}
\]
The same asymptotic upper bound holds with \(A_p\) replaced by \(A_p^{\mathrm{blk}}\). In particular, the upper-bound direction \(A_p=O((\log p)^{-2})\) of the critical logarithmic-degeneration conjecture follows **without** assuming that balanced two-block patterns are extremal. This is a one-sided result: no matching lower bound or exact limit is claimed.

## Assumptions and scope

All vector spaces are complex, all norms of finite matrices are Euclidean operator norms, and \(\log\) is the natural logarithm. The parameter is fixed at the binary perturbation threshold \(\delta=1/4\); the underlying finite matrix is precisely the constant periodic Fourier/Vandermonde matrix used for the *auxiliary binary local-shift model*. It is not a result about arbitrary perturbations of the genuine Gram form, and does not claim uniform estimates over that different model. The finite Hilbert matrix is indexed from zero, so its denominator is \(j+k+1\). The critical coefficient uses the exact finite-Hilbert-matrix asymptotic established by de Bruijn and Wilf.

## Proof

**1. Gram block decomposition.** Fix \(p\ge4\), put \(m=\lceil p/2\rceil\), and choose the balanced two-block sign pattern. Columns of \(H_{p,s^{\mathrm{blk}}}\) within the same sign group are mutually orthonormal: their frequency differences are nonzero integers with magnitude less than \(p\), and the corresponding geometric sums vanish. Reorder columns by their sign. Then
\[
H_{p,s^{\mathrm{blk}}}^{*}H_{p,s^{\mathrm{blk}}}=
\begin{pmatrix}I_m&C^*\\ C&I_{p-m}\end{pmatrix},
\]
where \(C\) is the cross-sign Gram block. Its extreme eigenvalues are \(1\pm\|C\|\), because the off-diagonal self-adjoint block has norm \(\|C\|\) and symmetric spectrum. Thus
\[
A_p\le A_p^{\mathrm{blk}}=1-\|C\|.
\]

**2. An exact positive Hilbert corner.** Let \(L=p-m=\lfloor p/2\rfloor\). Inside \(C\) select all \(L\) negative-sign rows indexed by \(r_-=m+j\), \(0\le j<L\), and the \(L\) positive-sign columns indexed in reverse order by \(r_+=m-1-k\), \(0\le k<L\). Their frequency separation is
\[
a_{jk}=(r_--1/4)-(r_++1/4)=j+k+\tfrac12.
\]
The elementary geometric-sum identity gives the corresponding cross-Gram entries (or their complex conjugates, depending on the orientation of the Gram block):
\[
C_{jk}=\frac1p\sum_{h=0}^{p-1}\exp\!\left(\frac{2\pi i h a_{jk}}p\right)
=\exp\!\left(\frac{\pi i(p-1)a_{jk}}p\right)
\frac{(-1)^{j+k}}{p\sin(\pi a_{jk}/p)}.
\]
Here \(0<a_{jk}<p\), so each displayed sine denominator is positive. The numerator phase is a product of a factor depending only on \(j\) and a factor depending only on \(k\). Therefore two diagonal unitary multipliers transform this \(L\)-by-\(L\) corner into the real symmetric positive-entry matrix
\[
K_{p,L}=\left(\frac1{p\sin\bigl(\pi(j+k+1/2)/p\bigr)}\right)_{0\le j,k<L}.
\]
Compression and unitary invariance imply \(\|C\|\ge\|K_{p,L}\|\).

**3. Entrywise comparison and the finite bound.** For every positive real \(x\), \(\sin x\le x\). Hence for all \(0\le j,k<L\),
\[
(K_{p,L})_{jk}\ge\frac1{\pi(j+k+1/2)}\ge\frac1{\pi(j+k+1)}
=\frac1\pi(\mathcal H_L)_{jk}.
\]
The strictly positive-entry matrix \(\mathcal H_L\) is symmetric. Its top unit eigenvector \(v\) may be chosen componentwise positive by Perron–Frobenius. Thus
\[
\|C\|\ge\|K_{p,L}\|\ge\langle K_{p,L}v,v\rangle\ge
\frac1\pi\langle\mathcal H_Lv,v\rangle=\frac{\Lambda_L}{\pi}.
\]
Substituting this inequality into the Gram formula proves the displayed finite inequality. The strict positivity \(A_p>0\) is the previously established Vandermonde noncollision fact for every fixed period at \(\delta=1/4<1/2\); it is not new here.

**4. Logarithmic asymptotic.** For the classical \(L\)-by-\(L\) Hilbert matrix, de Bruijn and Wilf proved
\[
\pi-\Lambda_L=\frac{\pi^5}{2(\log L)^2}(1+o(1))\qquad(L\to\infty).
\]
The finite inequality therefore yields
\[
0\le(\log p)^2A_p^{\mathrm{blk}}
\le\frac{(\log p)^2}{\pi}(\pi-\Lambda_L)
\longrightarrow\frac{\pi^4}{2},
\]
where the final arrow denotes convergence of the *upper comparison expression*, since \(L=\lfloor p/2\rfloor\) and \(\log L/\log p\to1\). Taking upper limits establishes the theorem for both \(A_p^{\mathrm{blk}}\) and \(A_p\). This completes the proof.

## Verification

The companion standalone `checker.py` independently constructs the critical finite Vandermonde matrices for all periods from \(4\) through \(48\) and the additional periods \(64,72,96,128\). It checks the geometric-sum corner, its positive phase removal, entrywise Hilbert domination, cross-block norm, exact Gram minimum-eigenvalue identity, and the final finite inequality, with documented floating-point tolerances. It passed \(343\) finite assertions over \(49\) periods. The infinite-period rate is proved by the analytical comparison and the cited classical finite Hilbert asymptotic, not by finite tests.

## Relationship to prior work

Vellucci and Samad (2026, arXiv:2610.31956v1), Theorems 5.1 and 6.1, establish the exact cross-block norm characterization and finite-matrix reduction used as the starting definitions. Their Lemma 7.2 establishes the zero lower bound for a nonperiodic step and their Corollary 7.3 proves only \(\inf_p A_p=0\). Their Conjecture 7.5 asks for two-sided inverse-log-squared bounds; its upper-bound direction is not established in the inspected manuscript. Their Conjecture 7.4 additionally proposes two-block extremality, which is **not** used here. The present observation is an exact **finite positive corner comparison**: a periodic two-block cross-Gram block contains a diagonally phase-equivalent nonnegative Hankel corner whose entries dominate the classical finite Hilbert matrix. This is sufficient for a one-sided quantitative theorem without controlling the remaining wrap-around interactions.

The de Bruijn–Wilf 1962 largest-Hilbert-eigenvalue asymptotic is an essential, previously known input, not an independently established result of this note. Preissmann and Lévêque (2013, §2.1, page 201) also state that asymptotic explicitly.

## Limitations

Only the upper logarithmic bound (with a nonasserted-sharp limsup constant) is proved. Neither the conjectured lower estimate \(A_p\ge c/(\log p)^2\), the exact leading coefficient, nor balanced-block extremality is proved. The benchmark finite Hilbert matrix has a known asymptotic, but no assertion is made that the periodic Gram matrix shares its exact spectral asymptotic. The result concerns the auxiliary binary periodic family at the critical quarter shift; it is not extrapolated to general real perturbations or higher-dimensional sampling.

The formula and its proof are subject to ordinary scholarly verification. Literature searches cannot exclude all older implicit variants, particularly in work on finite Cauchy–Vandermonde matrices and Hilbert-like corners.

## References

1. P. Vellucci and G. S. Samad, *Perturbed Exponential Systems, Pattern-Dependent Shifted-Sinc Operators, and Matrix Symbols on Finite Unions of Intervals*, arXiv:2610.31956v1, submitted 2026-10-22. https://arxiv.org/abs/2610.31956
2. N. G. de Bruijn and H. S. Wilf, *On Hilbert's inequality in n dimensions*, Bull. Amer. Math. Soc. 68 (1962), 70–73. DOI: 10.1090/S0002-9904-1962-10726-5.
3. E. Preissmann and O. Lévêque, *On generalized weighted Hilbert matrices*, Pacific J. Math. 265 (2013), 199–222, especially §2.1, p. 201. DOI: 10.2140/pjm.2013.265.199. https://msp.org/pjm/2013/265-1/pjm-v265-n1-p09-s.pdf
