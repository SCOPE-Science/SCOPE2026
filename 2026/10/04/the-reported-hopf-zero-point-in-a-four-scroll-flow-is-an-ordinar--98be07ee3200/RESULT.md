# The reported Hopf-zero point in a four-scroll flow is an ordinary supercritical Hopf point

## Finding
Consider the four-dimensional polynomial flow introduced by Vaidyanathan, Moroz, Sambas, Mohamed, Johansyah, Mamat and Ahmad,
\[
\dot x_1=a(x_1-x_2)-x_2x_3+x_4,\qquad
\dot x_2=x_1x_3-bx_2+x_4,
\]
\[
\dot x_3=x_1x_2-dx_2^2-cx_3,\qquad
\dot x_4=-x_1,
\]
with \(b,c,d>0\). The source varies \(a\), identifies \(a=0\) as a Hopf point for \(b=27\), \(c=8\), \(d=1/10\), but reports the spectrum there as \(\pm i,0,-27\) and calls the event a degenerate codimension-two Hopf-zero bifurcation.

For the printed vector field, the exact spectrum at that point is instead
\[
\{-8,-27,i,-i\}.
\]
Thus there is no zero eigenvalue. Moreover the critical pair crosses transversally as \(a\) increases,
\[
\left.\frac{d}{da}\operatorname{Re}\lambda(a)\right|_{a=0}
=\frac{b^2}{2(1+b^2)}
=\frac{729}{1460}>0.
\]
Using the explicit normalization in the proof, the first Lyapunov coefficient at \(a=0\) is
\[
l_1=-\frac{c^2(b^2+3)+8-d(2bc+3c^2+8)}{2c(b^2+1)^2(c^2+4)}.
\]
At the source parameters this gives
\[
l_1=-\frac{58491}{724744000}<0.
\]
Hence, in the smooth extension in which \(a\) is allowed to pass through zero, \(a=0\) is an ordinary nondegenerate supercritical Hopf point. The bifurcating periodic orbit lies on the original positive-parameter side: an asymptotically orbitally stable small periodic orbit exists for all sufficiently small \(a>0\).

The characteristic polynomial also shows where zero-Hopf spectra actually occur. For \(a=b\in(0,1)\), the equilibrium spectrum is
\[
\{-c,0,\pm i\sqrt{1-a^2}\}.
\]
So the source's zero-eigenvalue condition and its \(a=0\) Hopf condition were combined at a parameter point where they do not simultaneously hold.

## Assumptions and scope
The claim concerns the vector field exactly as printed above. Parameters \(b,c,d\) are positive, and the local Hopf classification treats \(a\) as a real unfolding parameter near zero. The source's physical parameter convention takes \(a>0\); this causes no conflict with the conclusion because the stable periodic branch lies at sufficiently small positive \(a\). The theorem is local near the origin and near \(a=0\). It does not classify the remote four-scroll attractors, periodic windows at larger \(a\), or the global multistability reported by the source.

## Proof
The Jacobian at the origin is
\[
A(a)=\begin{pmatrix}
a&-a&0&1\\
0&-b&0&1\\
0&0&-c&0\\
-1&0&0&0
\end{pmatrix}.
\]
Its characteristic polynomial factors exactly as
\[
\det(\lambda I-A(a))=(\lambda+c)
\left[\lambda^3+(b-a)\lambda^2+(1-ab)\lambda+(b-a)\right].
\]
At \(a=0\), the cubic factor is
\[
\lambda^3+b\lambda^2+\lambda+b=(\lambda+b)(\lambda^2+1),
\]
which proves the spectrum \(\{-c,-b,i,-i\}\). In particular, for \((b,c)=(27,8)\) there is no zero eigenvalue.

Let \(p(\lambda,a)\) denote the cubic factor. Implicit differentiation at \((\lambda,a)=(i,0)\) gives
\[
\frac{d\lambda}{da}=-\frac{p_a}{p_\lambda}
=\frac{bi}{2(-1+bi)},
\qquad
\operatorname{Re}\frac{d\lambda}{da}
=\frac{b^2}{2(1+b^2)}>0.
\]
Thus the imaginary pair crosses the imaginary axis transversally.

It remains to determine Hopf criticality. At \(a=0\), write the vector field as \(\dot x=Ax+\tfrac12 B(x,x)\). The symmetric bilinear quadratic part is
\[
B(u,v)=\begin{pmatrix}
-(u_2v_3+u_3v_2)\\
u_1v_3+u_3v_1\\
u_1v_2+u_2v_1-2d\,u_2v_2\\
0
\end{pmatrix}.
\]
Choose
\[
q=\begin{pmatrix}-i\\(b+i)^{-1}\\0\\1\end{pmatrix},
\qquad
p=\begin{pmatrix}-i/2\\0\\0\\1/2\end{pmatrix},
\]
so that \(Aq=iq\), \(A^Tp=-ip\), and \(\langle p,q\rangle=1\) for the Hermitian pairing. Because the vector field is quadratic, the cubic multilinear term vanishes. The standard Hopf coefficient is therefore
\[
l_1=\frac12\operatorname{Re}\left\langle p,
B\!\left(\overline q,(2iI-A)^{-1}B(q,q)\right)
-2B\!\left(q,A^{-1}B(q,\overline q)\right)
\right\rangle.
\]
Exact substitution and rational simplification give
\[
l_1=-\frac{c^2(b^2+3)+8-d(2bc+3c^2+8)}{2c(b^2+1)^2(c^2+4)}.
\]
For \(b=27\), \(c=8\), \(d=1/10\), this is \(-58491/724744000\). The standard Hopf theorem then gives a stable small-amplitude periodic branch on the side \(a>0\), because the crossing derivative is positive and \(l_1<0\).

Finally, a nonzero imaginary root \(\lambda=i\omega\) of the cubic must satisfy
\[
(b-a)(1-\omega^2)=0,
\qquad
\omega(1-ab-\omega^2)=0.
\]
When \(a=b\in(0,1)\), the cubic is
\[
\lambda\left(\lambda^2+1-a^2\right),
\]
which gives the zero-Hopf spectral locus \(\{-c,0,\pm i\sqrt{1-a^2}\}\). At \(a=0\), \(b>0\), the zero-eigenvalue condition is absent.

## Verification
The bundled dependency-free `verify.py` reconstructs the source-parameter Jacobian calculation using exact rational complex arithmetic. It verifies the factorization at \(a=0\), the true zero-Hopf spectral factorization at \(a=b\), the exact crossing derivative \(729/1460\), and the Hopf coefficient \(-58491/724744000\) from the bilinear-form formula using exact Gaussian elimination. Its recorded output is `VERIFY_OK`.

The source's own general characteristic polynomial agrees with the Jacobian reconstructed from its printed equations. The discrepancy appears only in the subsequent substitution at \(a=0\): the source replaces the stable eigenvalue \(-c=-8\) by a zero that belongs to the separate condition \(a=b\).

## Relationship to prior work
The introducing article explicitly gives the printed vector field, the Jacobian, the characteristic polynomial, the condition \(a=b\) for a zero eigenvalue, and then states that \(a=0\) with \(b=27\) has eigenvalues \(\pm i,0,-27\) and is a Hopf-zero point. The correction above follows from the same printed polynomial but adds the exact transversality and first-Lyapunov calculation needed to classify the event.

Exact-title searches, searches for the displayed characteristic polynomial and Hopf-zero claim, searches for the source-parameter coefficient, and searches for a first Lyapunov coefficient or normal-form treatment did not locate a publication stating this correction. A later Vaidyanathan-led two-scroll paper studies a different vector field, and a later four-scroll conference chapter likewise uses a different system; neither implies the present source-specific spectrum or Hopf coefficient. Published published-finding corpus records returned general Hopf and hyperchaotic-system analyses for other equations, not this claim.

## Limitations
The result is a local theorem at the origin. It does not validate or refute the source's large-amplitude hyperchaotic four-scroll attractors, its multistability at \(a=9\), or its periodic windows at larger \(a\). The first Lyapunov coefficient is stated for the explicit eigenvector normalization used above; its sign, and therefore the supercritical/stability conclusion, is invariant under admissible rescaling. The exact public-date field uses the earliest exact date found for a publicly accessible author-uploaded full text, 2021-12-21; the journal issue itself is labeled only “December 2021” in the inspected material.

## References
1. S. Vaidyanathan, I. M. Moroz, A. Sambas, M. A. Mohamed, M. D. Johansyah, M. Mamat and M. Z. Ahmad, “A New Multistable 4-D Hyperchaotic Four-Scroll System, its Dynamic Analysis and Circuit Design,” Engineering Letters 29(4), 1311–1318 (2021). Official article PDF: https://www.engineeringletters.com/issues_v29/issue_4/EL_29_4_03.pdf . Public author-uploaded full text: ResearchGate publication 357200969.
2. MSC2020 37G10, “Bifurcations of singular points in dynamical systems,” Mathematical Reviews / zbMATH MSC2020 database.
