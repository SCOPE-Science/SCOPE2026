# Exact slope-stability chambers and Harder–Narasimhan filtrations for Segre–Veronese syzygy bundles

## Finding
Let \(X=\mathbf P^1_{\mathbf C}\times\mathbf P^1_{\mathbf C}\). For integers \(a,b\ge1\), let \(L=\mathcal O_X(a,b)\) and let \(E=M_L\) be its complete evaluation kernel. Write \(H_1,H_2\) for the pullbacks of the hyperplane divisors of the two factors, and put \(A=\alpha H_1+\beta H_2\), where \(\alpha,\beta>0\) are real. Then the complete slope-stability chamber is
\[
 E\text{ is }\mu_A\text{-stable}\quad\Longleftrightarrow\quad
 \frac1{b+1}<\frac{\alpha}{\beta}<a+1.
\]
At either equality the bundle is **strictly slope-semistable**, and outside the closed interval it is **slope-unstable**. Both outer-chamber Harder–Narasimhan filtrations, and the Jordan–Hölder gradeds at the two walls, have explicit line-bundle terms:
\[
\begin{array}{ll}
\alpha\ge(a+1)\beta:&0\to\mathcal O_X(-1,0)^{\oplus a(b+1)}\to E\to\mathcal O_X(a,-1)^{\oplus b}\to0,\\[2mm]
\beta\ge(b+1)\alpha:&0\to\mathcal O_X(0,-1)^{\oplus b(a+1)}\to E\to\mathcal O_X(-1,b)^{\oplus a}\to0.
\end{array}
\]
In a strict outer chamber the displayed subbundle is exactly the maximal destabilizing Harder–Narasimhan term. At equality the terms give the associated graded of a Jordan–Hölder filtration, after splitting their direct sums into lines. Invariants are
\[
\operatorname{rk}E=ab+a+b,\quad c_1(E)=-aH_1-bH_2,\quad c_2(E)=2ab.
\]
For any fixed \(m,n\ge1\) and ample real \(A\), the least integer \(d\ge1\) for which \(M_{\mathcal O_X(dm,dn)}\) is slope-stable is exactly
\[
 d_{\min}=\max\!\left\{1,\;1+\left\lfloor\max\!\left(
 \frac{\alpha/\beta-1}{m},\,\frac{\beta/\alpha-1}{n}
 \right)\right\rfloor\right\}.
\]
When an integer \(d\) hits one of the two walls, the corresponding bundle is strictly semistable.

## Assumptions and scope
All varieties and bundles are over \(\mathbf C\). Slope is defined by \(\mu_A(F)=c_1(F)\cdot A/\operatorname{rk}F\) for nonzero torsion-free coherent sheaves. The polarization is any positive real class in the ample cone, not merely a tensor-power ray. The complete linear system of \(L\) is used; incomplete evaluation systems are not covered. The surface has intersection numbers \(H_1^2=H_2^2=0\) and \(H_1\cdot H_2=1\). Since \(a,b\ge1\), the evaluation is surjective, and \(E\) is a vector bundle.

## Proof
**1. Exact filtrations from tensor-product evaluations.** On \(\mathbf P^1\), the complete evaluation sequence of \(\mathcal O_{\mathbf P^1}(e)\), for any integer \(e\ge1\), has kernel \(\mathcal O_{\mathbf P^1}(-1)^{\oplus e}\). Indeed the kernel is a subbundle of a trivial bundle with no global sections and degree \(-e\); equivalently this is the familiar evaluation sequence for the complete Veronese linear series. Denote the spaces of global sections of the two factors by \(V_a,V_b\). The surjection
\[
 V_a\otimes V_b\otimes\mathcal O_X\longrightarrow\mathcal O_X(a,b)
\]
factors first through \(V_b\otimes\mathcal O_X(a,0)\), and then through \(\mathcal O_X(a,b)\). Its first kernel is \(\mathcal O_X(-1,0)^{\oplus a(b+1)}\), and the kernel of the second map is \(\mathcal O_X(a,-1)^{\oplus b}\). The snake lemma produces the first displayed extension. Factoring in the opposite order gives the second displayed extension. Both are globally exact sequences of locally free sheaves, not merely fiberwise rank identities.

**2. Slopes and the two wall semistabilities.** From the evaluation sequence,
\[
\mu_A(E)=-\frac{a\beta+b\alpha}{ab+a+b}.
\]
The factors of the first extension have slopes \(-\beta\) and \(a\beta-\alpha\), equal precisely at \(\alpha=(a+1)\beta\). The factors of the second have slopes \(-\alpha\) and \(b\alpha-\beta\), equal precisely at \(\beta=(b+1)\alpha\). Direct sums of line bundles of equal slope are slope-semistable; an extension of two slope-semistable sheaves of the same slope is slope-semistable. Thus \(E\) is semistable on both rays. On either ray it is not stable, since the respective proper nonzero subbundle has exactly the slope of \(E\).

**3. Interior stability from a known central stable polarization.** The independent input is the established theorem that \(M_L\) is \(\mu_L\)-stable when \(L\) is an ample globally generated line bundle on a Hirzebruch surface: Torres-López and Zamora, Corollary 3.5 in arXiv:2008.11255. It applies to the zeroth Hirzebruch surface \(X\). One can check the numerical hypothesis in the cited Proposition 3.3 directly: a general divisor in \(|L|\) is smooth and irreducible by Bertini, \(-K_X=2H_1+2H_2\), and \((-K_X)\cdot L=2(a+b)\ge4\), which exceeds the required bound 2. In particular \(E\) is stable for \(A=L=aH_1+bH_2\), whose ratio \(a/b\) is strictly between the two wall ratios since \(ab+b>1\) and \(ab+a>1\).

For a nonzero proper torsion-free subsheaf \(F\subset E\) of smaller rank, define \(\Delta_F(A)=\mu_A(F)-\mu_A(E)\). It is a linear functional in the numerical polarization \(A\). By step 2, it is nonpositive on each of the two boundary rays. Every ample polarization strictly between the rays is a positive linear combination of their generators. If \(\Delta_F\) vanished at an interior polarization, it would have to vanish on both rays; hence it would vanish at \(L\), contradicting \(\mu_L\)-stability. Therefore \(\Delta_F(A)<0\) for every proper positive-rank subsheaf and every interior \(A\): the whole open chamber is stable, with no hidden wall.

**4. Exterior Harder–Narasimhan filtrations.** If \(\alpha>(a+1)\beta\), the two slopes of the first extension satisfy
\[
 -\beta>\mu_A(E)>a\beta-\alpha.
\]
Its subbundle and quotient are both direct sums of line bundles and hence semistable; their strict descending slopes make the exact sequence the Harder–Narasimhan filtration. The second extension similarly gives the Harder–Narasimhan filtration when \(\beta>(b+1)\alpha\). The two exterior regions cannot overlap. This proves the claimed complete classification, including the semistable boundary and associated graded descriptions.

**5. Numerical invariants and sharp powers.** From the evaluation exact sequence, \(c(E)=1/(1+aH_1+bH_2)\). Using \(H_1^2=H_2^2=0\) gives the stated rank, first Chern class, and \(c_2(E)=2ab\). Substituting \(a=dm\) and \(b=dn\) into the strict inequalities of the chamber yields \(d>(\alpha/\beta-1)/m\) and \(d>(\beta/\alpha-1)/n\). Taking the least positive integer satisfying both gives the displayed exact ceiling-with-strict-inequality formula. The same boundary arguments handle equality.

## Verification
The standalone standard-library-only program `verify.py` checks \(84{,}100\) exact rational slope comparisons for \(1\le a,b\le10\) and positive integer polarization coefficients \(1\le\alpha,\beta\le29\), and \(16\) direct evaluations of both tensor-product factorization maps for \(1\le a,b\le4\). On execution it prints `VERIFY_OK 84100 slope comparisons; 16 exact evaluation factorizations`. This checks numerical identities and the evaluation-factorization architecture at sample fibers. It does not prove semistability or the all-integers theorem; those follow from the two globally exact sequences, the cited stability input, and the polarization-linear argument above.

## Relationship to prior work
Misra, arXiv:2602.06629 (first public February 6, 2026), studies instability under changing polarization and proves a general criterion requiring Picard number at least three; the present surface has Picard number two. Devey–Hering–Jochemko–Süß, arXiv:2409.04666, explicitly exclude \(\mathbf P^1\times\mathbf P^1\) from their toric instability theorem, and handle nonzero Hirzebruch parameters separately. Torres-López and Zamora, arXiv:2008.11255, establish stability for the *single natural polarization* \(A=L\); their result is used here as an input, not claimed as new. The claim here is the entire two-dimensional ample-chamber classification, precise exterior Harder–Narasimhan terms, and sharp first stable tensor power. No complete equivalent statement was identified by targeted searches, though absence from searches does not establish historical priority.

## Limitations
The theorem is for the split quadric surface over \(\mathbf C\), complete linear series, and positive bidegrees. It does not classify Gieseker stability, singular or nonample polarizations, the behavior of sublinear systems, or syzygy bundles on more general toric surfaces. The proof relies on a published central-polarization stability theorem, cited explicitly, and priority over all differently formulated work cannot be guaranteed without an independent literature audit.

## References
- S. Misra, *On instability of Syzygy Bundles*, arXiv:2602.06629, first posted February 6, 2026. https://arxiv.org/abs/2602.06629
- L. Devey, M. Hering, K. Jochemko, H. Süß, *On the instability of syzygy bundles on toric surfaces*, arXiv:2409.04666, first posted September 7, 2024; Annali di Matematica Pura ed Applicata, published 2025. https://arxiv.org/abs/2409.04666
- H. Torres-López and A. G. Zamora, *Some Remarks on H-stability of Syzygy Bundles on Algebraic Surfaces*, arXiv:2008.11255, especially Proposition 3.3 and Corollary 3.5. https://arxiv.org/abs/2008.11255
