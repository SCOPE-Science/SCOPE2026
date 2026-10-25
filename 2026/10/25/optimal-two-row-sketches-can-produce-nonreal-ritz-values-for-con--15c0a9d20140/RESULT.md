# Optimal two-row sketches can produce nonreal Ritz values for condition-two SPD systems

## Finding

There is an exact three-regime spectral transition in the two-step deterministically sketched Rayleigh–Ritz method, even when its coordinate sketch is the **unique global maximizer** of the smallest singular value of the sampled orthonormal Krylov basis. Within an explicit three-dimensional real symmetric positive-definite (SPD) family, let \(p\in(0,1)\), \(h,t>0\), and \(d>\sqrt{h^2+t^2}\). For the uniquely optimal two-row coordinate sketch, the computed reduced matrix is
\[
M=\begin{pmatrix}d&h-pt\\h&d\end{pmatrix}.
\]
Its eigenvalues are two distinct real values for \(h>pt\), a defective double eigenvalue for \(h=pt\), and the **nonreal conjugate pair** \(d\pm i\sqrt{h(pt-h)}\) for \(0<h<pt\). Both standard DEIM and Q-DEIM choose this very sketch.

The squared-norm embedding defect on the two-dimensional Krylov space is exactly \(\delta=p^2/(1+p^2)\), which can be arbitrarily small. The full SPD matrix can simultaneously have spectral condition number **exactly \(2\)**, independently of \(p\). At fixed full-matrix spectral half-width \(w=\sqrt{h^2+t^2}\), the largest possible imaginary part among this family is exactly
\[
\max_{h,t>0,\ h^2+t^2=w^2}\frac{|\operatorname{Im}\lambda(M)|}{w}
=\sqrt{\frac{\sqrt{1+p^2}-1}{2}},
\]
achieved uniquely at \(h/t=p/(1+\sqrt{1+p^2})\). Consequently the maximal imaginary part, normalized by \(w\), is asymptotic to \(\sqrt\delta/2\) as \(\delta\downarrow0\). Thus optimal basis embedding does not guarantee even real Ritz extraction, and the worst spectral pollution in this family has a sharp square-root rather than linear scale in its squared-norm defect.

## Assumptions and scope

All matrices and computations are real and in exact arithmetic before computing eigenvalues. Put \(c=(1+p^2)^{-1/2}\) and define the orthogonal matrix and symmetric Jacobi matrix
\[
Q=\begin{pmatrix}c&0&-pc\\0&1&0\\pc&0&c\end{pmatrix},\qquad
H=\begin{pmatrix}d&h&0\\h&d&t\\0&t&d\end{pmatrix},\qquad A=QHQ^\top.
\]
Let \(b=Qe_1\) and \(V=[Qe_1,Qe_2]\), so \(V\) is an orthonormal basis of the genuine two-step Krylov space \(\mathcal K_2(A,b)=\operatorname{span}\{b,Ab\}\). A two-row coordinate selector chooses two distinct standard coordinate rows. Define the sketched Rayleigh–Ritz matrix as \(M_S=(SV)^{-1}SAV\) when \(SV\) is nonsingular. The optimization criterion is the maximum of \(\sigma_{\min}(SV)\) among the three possible unordered two-row coordinate selectors, as in deterministic row-subset sketching. A permutation of the selected rows leaves \(M_S\) invariant.

## Proof

**SPD and the Krylov basis.** Orthogonality of \(Q\) is immediate. The characteristic polynomial of \(H\) is \((d-\lambda)[(d-\lambda)^2-(h^2+t^2)]\); its eigenvalues are \(d\), \(d\pm w\), where \(w=\sqrt{h^2+t^2}\). Because \(d>w\), \(A\) is SPD and \(\kappa_2(A)=(d+w)/(d-w)\). Moreover \(Ab=dQe_1+hQe_2\), and \(h>0\), so the claimed two-dimensional Krylov space has exactly the displayed orthonormal basis.

**Selection is globally optimal, including DEIM and Q-DEIM.** In ambient coordinate order the rows of \(V\) are \((c,0)\), \((0,1)\), and \((pc,0)\). Their two-row choices have respective minimum singular values \(c\) for rows \(\{1,2\}\), \(pc\) for \(\{2,3\}\), and \(0\) for \(\{1,3\}\). Since \(0<p<1\), rows \(\{1,2\}\) are uniquely optimal. DEIM applied to the ordered columns first picks row \(1\) because \(c>pc\), and then picks row \(2\) because the second column has value \(1\) only there. Q-DEIM first pivots to row \(2\) of norm \(1\) in \(V^\top\), and then chooses row \(1\) over row \(3\) because \(c>pc\). Both methods therefore select the globally optimal unordered pair. For its selector \(S\), \(SV=\operatorname{diag}(c,1)\), giving exact squared-norm bounds \(c^2\|z\|_2^2\le\|SVz\|_2^2\le\|z\|_2^2\) for every \(z\in\mathbb R^2\), with \(1-c^2=\delta\).

**Exact transition.** Set \(q_3=Qe_3\). The Krylov decomposition is \(AV=V\begin{psmallmatrix}d&h\\h&d\end{psmallmatrix}+q_3\begin{psmallmatrix}0&t\end{psmallmatrix}\). The sampled third direction obeys \((SV)^{-1}Sq_3=(-p,0)^\top\). Therefore
\[
M=(SV)^{-1}SAV=\begin{pmatrix}d&h-pt\\h&d\end{pmatrix},\qquad
\det(\lambda I-M)=(\lambda-d)^2-h(h-pt).
\]
The claimed real/defective/nonreal trichotomy follows from the sign of \(h-pt\). At \(h=pt>0\), \(M-dI\) is nonzero and has square zero, so the double root is defective. By contrast, the ordinary symmetric Rayleigh–Ritz matrix \(V^\top AV=\begin{psmallmatrix}d&h\\h&d\end{psmallmatrix}\) has the real eigenvalues \(d\pm h\).

**Sharp normalized imaginary envelope.** Write \(k=h/t>0\) and \(w=t\sqrt{1+k^2}\). In the nonreal region \(k<p\), the squared normalized imaginary part is \(g(k)=k(p-k)/(1+k^2)\); outside this region it is \(0\). Its derivative has sign of \(p-2k-pk^2\), whose only positive root is \(k_*=p/(1+\sqrt{1+p^2})\). More precisely, with \(g_*=(\sqrt{1+p^2}-1)/2\), the identity
\[
g_*-g(k)=\frac{(1+g_*)(k-k_*)^2}{1+k^2}\ge0
\]
holds for every \(k>0\), and equality holds exactly at \(k=k_*\). Every \(k\) in this optimization is compatible with \(\kappa_2(A)=2\) by choosing \(d=3w\). Finally \(p^2=\delta/(1-\delta)\), so
\[
\frac{|\operatorname{Im}\lambda|_{\max}}{w}
=\sqrt{\frac{(1-\delta)^{-1/2}-1}{2}}
\sim\frac{\sqrt\delta}{2} \quad(\delta\downarrow0).
\]
All inequalities are attained within the stated family, establishing sharpness.

**Exact small-matrix witness.** Take \(p=3/4\), \(h=5/13\), \(t=12/13\), and \(d=3\). Here \(w=1\) and
\[
A=\begin{pmatrix}
3&-16/65&0\\-16/65&3&63/65\\0&63/65&3
\end{pmatrix},\quad
\operatorname{spec}(A)=\{2,3,4\},\quad
M=\begin{pmatrix}3&-4/13\\5/13&3\end{pmatrix}.
\]
Thus \(\kappa_2(A)=2\), the optimal sampler has \(\sigma_{\min}(SV)=4/5\), and its nonreal estimates are exactly \(3\pm2\sqrt5\,i/13\).

## Verification

The accompanying standalone `verify.py` uses symbolic and exact-rational matrix arithmetic to check the orthogonality, Krylov decomposition, formula for \(M\), characteristic polynomial, row-selector comparison, DEIM/Q-DEIM pivot inequalities, exact rational condition-two witness, and the sharp envelope identity. It also checks a reproducible finite rational parameter sample in each discriminant regime. Execute `python verify.py` with SymPy available. These finite tests supplement, but do not replace, the proofs above.

## Relationship to prior work

Bergermann (arXiv:2604.07158, §§2.4, 3, 4.1, 5.3) defines deterministic sketched Rayleigh–Ritz, the minimum-singular-value row-selection objective, DEIM and Q-DEIM, and the resulting eigenvalue method. Those definitions and algorithms are **prior work**. Nakatsukasa and Tropp (arXiv:2111.00113, §6.8) expressly establish the general possibility of nonreal sketched eigenvalues for symmetric input; this qualitative possibility is **not** claimed as new. Liu and Liu (arXiv:2610.22261, §3.1) likewise use real Schur extraction because ordinary sRR may have nonreal projected eigenvalues. Grigori, Kressner, Shao, and Simunec (arXiv:2601.10248, §§2–3) modify the Arnoldi relation to restore similarity to standard Ritz extraction; that is a different algorithm, not a guarantee for the unmodified dsRR projection.

The assessed contribution is confined to the **simultaneous** presence of unique global E-optimality, DEIM/Q-DEIM algorithmic selection, a genuine two-step Krylov basis, exact condition-two SPD input, the complete real/defective/nonreal parameter frontier, and the attained sharp imaginary-part envelope at fixed spectral spread. General recognition that an arbitrary nonsymmetric sketch can give complex Ritz values does not establish those joint conditions or the sharp envelope. The literature search is not a uniqueness proof, and earlier specialized constructions may exist.

## Limitations

The classification and envelope concern the explicitly parameterized real \(3\times3\) SPD family, two Krylov vectors, two selected coordinate rows and the **unmodified** sketched Rayleigh–Ritz reduced matrix. They are not universal upper bounds for all SPD matrices or all sketches. They do not assess oversampled sketches, finite precision, eigenvector convergence, or the similarity-restored and real-Schur alternatives. The nonreal-eigenvalue possibility itself is already established in earlier work. Independent validation has not been performed.

## References

- K. Bergermann, *Deterministic sketching for Krylov subspace methods*, arXiv:2604.07158v1 (first posted 2026-04-08), §§2.4, 3, 4.1, 5.3. https://arxiv.org/abs/2604.07158
- Y. Nakatsukasa and J. A. Tropp, *Fast & Accurate Randomized Algorithms for Linear Systems and Eigenvalue Problems*, arXiv:2111.00113 (first posted 2021-10-29), §§6.7–6.8. https://arxiv.org/abs/2111.00113
- J. Liu and Y. Liu, *Real-Arithmetic Sketched Eigensolvers for Symmetric Matrices*, arXiv:2610.22261v1 (first posted 2026-10-15), §3.1. https://arxiv.org/abs/2610.22261
- L. Grigori, D. Kressner, N. Shao, and I. Simunec, *Restoring similarity in randomized Krylov methods with applications to eigenvalue problems and matrix functions*, arXiv:2601.10248 (first posted 2026-01-15), §§2–3. https://arxiv.org/abs/2601.10248
