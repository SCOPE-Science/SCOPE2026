# Fourteen ambiguity planes for six-sample cubic Fourier phase retrieval

## Finding

Let \(\zeta=\exp(\pi i/3)\). For any coefficient vector \(c\in\mathbb C^4\), put \(P_c(z)=c_0+c_1z+c_2z^2+c_3z^3\), and record
\[
\mathcal M(c)=\bigl(|P_c(\zeta^j)|^2,\ |P'_c(\zeta^j)|^2\bigr)_{j=0}^{5}.
\]
Call \(c,d\) equivalent when \(d=\lambda c\) for some \(|\lambda|=1\). There exist **exactly fourteen distinct complex two-dimensional linear subspaces** \(L_1,\ldots,L_{14}\subset\mathbb C^4\) such that:

1. If \(\mathcal M(c)=\mathcal M(d)\) but \(c,d\) are not equivalent, then \(c\in\bigcup_{j=1}^{14}L_j\). Thus \(\mathcal M\) is injective modulo phase for Lebesgue-almost-every \(c\in\mathbb C^4\).
2. In each \(L_j\), a relatively open dense subset of nonzero vectors admits a phase-inequivalent partner with identical measurements. More precisely, if \(u_j,v_j\) are orthonormal positive and negative eigenvectors of the corresponding Hermitian matrix below, then all \(c=\alpha u_j+\beta v_j\) with \(|\alpha|\ne|\beta|\) admit such a partner. The excluded equal-modulus locus is a real hypersurface of \(L_j\).
3. Universal uniqueness fails at six samples, although published work proves universal uniqueness at seven samples for this degree: \(P(z)=1+iz^3\) and \(Q(z)=1-iz^3\) have identical measurements at all six sites and are not equivalent.

The fourteen planes have the **explicit exact algebraic description** \(L_j=\operatorname{ran}H_j\). Put
\[
H(a,b,t,y)=\begin{pmatrix}
3a+8b&2\overline t&0&-iy\\
2t&-4a-9b&-3\overline t&0\\
0&-3t&a&\overline t\\
iy&0&t&b
\end{pmatrix},\qquad a,b,y\in\mathbb R,\quad t\in\mathbb C.
\]
Let \(p=(\sqrt3+i)/2\), \(q=(-\sqrt3+i)/2\), and
\[
\kappa=\frac{-21-\sqrt{57}}{48},\quad
\rho=\sqrt{\frac{\kappa(4+9\kappa)}4},\quad
\eta=\sqrt{-\frac{27\kappa^2+72\kappa^3}{4}}.
\]
All fourteen matrices \(H_j\), one from each family below, are:

* \(H(0,0,0,1)\): one matrix.
* \(H(0,1,0,\pm2\sqrt2)\): two matrices.
* \(H(1,-4/9,0,\pm2\sqrt5/9)\): two matrices.
* \(H(0,0,t,-(2/3)\operatorname{Im}(t^3))\) for \(t\in\{p,i,q\}\): three matrices.
* \(H(1,\kappa,\rho t,-\eta)\) for \(t\in\{p,q,-i\}\), and \(H(1,\kappa,\rho t,+\eta)\) for \(t\in\{\overline p,i,\overline q\}\): six matrices.

## Assumptions and scope

The coefficient field is \(\mathbb C\), the polynomial degree is at most three, the sampling grid consists of exactly the sixth roots of unity, and both value and first-derivative *magnitudes* are used. Zero polynomials are trivially unique up to phase. Distinctness of the fourteen planes means literal distinct subspaces, not merely distinct matrices or different parameterizations. No assertion is made for other grid sizes or higher degrees.

## Proof

**1. Linearization and exact measurement kernel.** For a Hermitian \(4\times4\) matrix \(X\), let \(\mathcal A(X)\) be its twelve real measurements obtained by replacing \(c_j\overline{c_k}\) by \(X_{jk}\) in the definitions of \(\mathcal M\). Fourier orthogonality on six roots gives a real-linear map of rank eleven on the sixteen-dimensional space of Hermitian matrices. Solving its twelve linear equations gives the **complete** five-real-dimensional kernel
\[
\ker\mathcal A=\{H(a,b,t,y):a,b,y\in\mathbb R,\ t\in\mathbb C\}.
\]
This identity is also checked independently by forming the full rational-algebraic measurement matrix and proving its rank is eleven.

If two signals have equal measurements, their difference of rank-one Gram matrices \(X=cc^*-dd^*\) lies in \(\ker\mathcal A\). If they are inequivalent, \(X\ne0\); because every matrix in the kernel has trace zero, \(X\) has rank exactly two with one strictly positive and one strictly negative eigenvalue. In particular \(c,d\in\operatorname{ran}X\).

**2. Exhaustion of rank-two kernel matrices.** Write \(t=u+iv\), \(r=|t|^2\), \(s=y^2\). Vanishing of the four principal three-by-three minors is necessary for rank at most two. In order of deletion of the row and column indexed \(0,1,2,3\), these minors are exactly
\[
\begin{aligned}
F_0&=a(-4ab-9b^2+4r),\\
F_1&=3a^2b+8ab^2-3ar-as-8br,\\
F_2&=-12a^2b-59ab^2+4as-72b^3-4br+9bs,\\
F_3&=-12a^3-59a^2b-72ab^2-31ar-72br.
\end{aligned}
\]

When \(a=0\), the equations give either \(b\ne0,r=0,s=8b^2\), or \(b=0\). In the latter case, \(t=0,y\ne0\) gives one real ray. For \(t\ne0\), the determinant equation is
\[
4r^2+9sr+12y\operatorname{Im}(t^3)=0.
\]
Since \(|\operatorname{Im}(t^3)|\le r^{3/2}\), this is possible only with \(y=\mp(2/3)\sqrt r\) and \(\operatorname{Im}(t^3)=\pm r^{3/2}\). Modulo nonzero *real* scaling, it gives exactly three further rays. Together this yields the first, second and fourth displayed families.

For \(a\ne0\), the equation \(F_0=0\) yields \(r=b(4a+9b)/4\). Substituting into \(F_3=0\) gives
\[
(4a+9b)(4a^2+21ab+24b^2)=0.
\]
If \(4a+9b=0\), then \(t=0\); \(F_1=0\) gives \(s=20a^2/81\), yielding the third family. Otherwise \(b/a\) is one of \((-21\pm\sqrt{57})/48\). The positive-sign root makes \(r<0\) and is impossible. The remaining root \(b/a=\kappa\) gives \(r=\rho^2a^2\), \(s=\eta^2a^2\); both are strictly positive. Normalizing \(a=1\), the determinant equals
\[
D_0+12y\operatorname{Im}(t^3),\qquad D_0=12\eta\rho^3.
\]
Thus \(\operatorname{Im}(t^3)=-\operatorname{sgn}(y)\rho^3\). For each of the two signs of \(y\), there are exactly three unit phases of \(t/\rho\). This yields the six matrices of the final family. Direct substitution verifies every listed matrix has all principal three-minors and determinant zero. Since it is nonzero, Hermitian, and trace zero, its rank is exactly two. Hence all nonzero rank-two kernel matrices lie on precisely these fourteen real rays.

**3. The fourteen planes are distinct.** For every listed \(H_j\), the orthogonal projector onto its range is exactly
\[
\Pi_j=\frac{2H_j^2}{\operatorname{tr}(H_j^2)}.
\]
The exact symbolic verifier compares all \(\binom{14}{2}=91\) projector pairs in the algebraic field generated by the displayed radicals and confirms \(\Pi_i\ne\Pi_j\) for each \(i\ne j\). These exact matrix equalities and inequalities establish the distinctness asserted in the theorem; floating-point comparisons are not used.

**4. Generic failure inside, and uniqueness outside, these planes.** If \(H_j\) has unit eigenvectors \(u_j,v_j\) with eigenvalues \(\pm\lambda\), every \(c=\alpha u_j+\beta v_j\) with \(|\alpha|\ne|\beta|\) has the partner
\[
 d=\begin{cases}
 (|\beta|/|\alpha|)\alpha u_j+(|\alpha|/|\beta|)\beta v_j,&\alpha\beta\ne0,\\
 |\alpha|v_j,&\beta=0,\\
 |\beta|u_j,&\alpha=0.
 \end{cases}
\]
For the last two cases a harmless unit phase is immaterial. Direct multiplication gives \(cc^*-dd^*\) a nonzero real multiple of \(H_j\); hence their measurements agree and they are inequivalent. Conversely any inequivalent pair determines such a rank-two kernel matrix, so both signal vectors belong to one of the fourteen planes. Finite unions of proper complex planes have real Lebesgue measure zero in \(\mathbb C^4\). The explicit pair \(1\pm iz^3\) gives non-universality.

## Verification

The standalone `verify.py` uses exact SymPy arithmetic to verify all fourteen matrices, all 91 range-projector inequalities, the principal-minor and determinant identities, and the explicit ambiguous pair. Separately, the full measurement map was independently reconstructed in exact cyclotomic arithmetic: its real matrix rank is eleven, and all five displayed parameter basis matrices lie in the kernel. These exact finite-dimensional calculations are sufficient because the elimination above proves exhaustion for arbitrary complex coefficients; sampling finitely many candidate signals alone would not suffice.

To reproduce, run `python verify.py` in an environment with Python 3 and SymPy. See `verification-output.txt` for the exact pass record. No numerical tolerance enters the certificate.

## Relationship to prior work

Jaming and Rathmair, *Uniqueness of phase retrieval from three measurements* (arXiv:2205.08753v1, 18 May 2022), study these polynomial-and-derivative phase measurements; in their section 3, Proposition 3.2 establishes **universal** uniqueness at \(2N-1\) grid sites for length-\(N\) polynomials, hence seven sites for cubics. Their Proposition 3.4 gives separate undersampling obstructions, and Question 3.5 explicitly asks about **almost-all** uniqueness below the universal sampling bound. The six-site cubic result and complete fourteen-plane ambiguity geometry proved here are not asserted by either proposition and answer that low-degree almost-all question at six samples. The familiar complex phase retrieval rank-two kernel criterion is the mechanism, not itself a claim of novelty.

A semantic comparison against published research records using the terms “cubic polynomial”, “six roots”, “two-mask Fourier intensity”, “first derivative”, “rank-two Hermitian kernel”, and “exceptional ambiguity planes” found no statement covering this exact classification. Negative search results alone do not prove priority.

## Limitations

This is a finite-dimensional exact theorem and does not provide quantitative stability near the exceptional planes, a reconstruction algorithm robust to noise, or the smallest sample number for generic uniqueness. Other less-obvious earlier formulations in coded diffraction, Hermitian-matrix phase retrieval, or derivative-magnitude interpolation could still overlap; independent literature review is warranted.

## References

1. P. Jaming and M. Rathmair, *Uniqueness of phase retrieval from three measurements*, arXiv:2205.08753v1 (first publicly posted 18 May 2022), especially section 3, Propositions 3.2 and 3.4 and Question 3.5.
2. The exact symbolic arithmetic certificate supplied as `verify.py` and `verification-output.txt`.
