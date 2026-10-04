# Tetrahedral tangent cone on the balanced block-circulant line
## Finding
Let \(Z_4\) be the complex projective closure of the \(4\times4\) orthostochastic matrices, and let \(P\) be one of the nine five-dimensional block-circulant linear components appearing in the Chen--Dey analysis. On the affine doubly-stochastic chart, use coordinates \(p,A,B,C,D\) so that
\[
M=\frac12\begin{pmatrix}
p+A&p-A&1-p+B&1-p-B\\
p-A&p+A&1-p-B&1-p+B\\
1-p+C&1-p-C&p+D&p-D\\
1-p-C&1-p+C&p-D&p+D
\end{pmatrix}.
\]
The balanced line is \(L=V(A,B,C,D)\). For the reduced section \(P\cap Z_4\), an octic defining equation \(F\) satisfies the exact identity
\[
16F=L_1L_2L_3L_4-4(AB-CD)(AC-BD)\bigl(AD(1-p)^2-BCp^2\bigr),
\]
where
\[
\begin{aligned}
L_1&=-(1-p)A-pB-pC-(1-p)D,\\
L_2&=-(1-p)A-pB+pC+(1-p)D,\\
L_3&=-(1-p)A+pB-pC+(1-p)D,\\
L_4&=-(1-p)A+pB+pC-(1-p)D.
\end{aligned}
\]
Hence for every \(p_0\in\mathbb C\setminus\{0,1\}\), the transverse multiplicity of \(P\cap Z_4\) along \(L\) at \(p=p_0\) is exactly \(4\), and the normal tangent cone is the reduced tetrahedral arrangement \(V(L_1L_2L_3L_4)\). The four normal hyperplanes are independent because their coefficient determinant is
\[
-16p_0^2(1-p_0)^2\neq0.
\]
By row-column permutation symmetry, the same conclusion holds for each of the nine relevant block-circulant components.

## Assumptions and scope
The ground field is \(\mathbb C\), and the local statement is about the reduced affine section of \(Z_4\) by one of the canonical five-dimensional block-circulant linear spaces \(P\). The parameter values \(p=0\) and \(p=1\) are excluded from the generic tangent-cone statement because the four linear factors cease to be independent there. The result concerns the tangent cone and transverse multiplicity; it does not assert that the full analytic germ splits into four branches.

For real \(0<p<1\), points of \(L\) are genuinely orthostochastic. If \(u^2=p\) and \(v^2=1-p\), then
\[
\frac1{\sqrt2}\begin{pmatrix}
u&u&v&v\\
u&-u&v&-v\\
v&v&-u&-u\\
v&-v&-u&u
\end{pmatrix}
\]
is orthogonal, and its entrywise square is the balanced matrix on \(L\).

## Proof
Chen--Dey show that the nine relevant five-dimensional components can be described by partitioning a doubly stochastic \(4\times4\) matrix into four \(2\times2\) circulant blocks. They also prove, on the affine chart, that the intersection of such a component with \(Z_4\) has the same zero set as the restriction of the three classical naive octics.

For the displayed representative \(P\), substituting the matrix \(M\) into those three octics gives one identically zero restriction and two identical restrictions. Denote the common nonzero restriction by \(F\). Exact symbolic expansion gives the displayed identity for \(16F\). Treating \(A,B,C,D\) as normal variables to \(L\), the only normal degrees occurring in \(F\) are \(4\) and \(6\). Its degree-four part is exactly
\[
\operatorname{in}_L(F)=\frac1{16}L_1L_2L_3L_4.
\]
The \(4\times4\) coefficient matrix of \(L_1,L_2,L_3,L_4\) in \(A,B,C,D\) has determinant \(-16p^2(1-p)^2\). Thus at \(p=p_0\notin\{0,1\}\), the initial form is a product of four distinct independent linear forms. Therefore the transverse order is exactly \(4\), and the normal tangent cone is the reduced union of those four hyperplanes.

The polynomial \(F\) is squarefree in characteristic zero: its greatest common divisor with all five first partial derivatives is \(1\). Thus it is a reduced hypersurface equation, compatible with taking the reduced section. Finally, row and column permutations preserve orthostochasticity and permute the nine block-circulant components, so the same local statement transfers to all of them.

## Verification
The standalone verifier `artifacts/verify.py` reconstructs the doubly stochastic parametrization, the three naive octics, the restricted equation, the exact degree-four and degree-six decomposition, and the determinant \(-16p^2(1-p)^2\). It also checks squarefreeness by the derivative gcd and verifies the explicit orthogonal square root on the real balanced line. The package replay returns `VERIFY_OK`.

## Relationship to prior work
Chen and Dey determine set-theoretic equations for \(Z_4\), identify the nine relevant five-dimensional block-circulant components, and prove that on each such component the orthostochastic section is obtained from the restricted naive octics. Their paper records the ambient equations and the computer-algebra restrictions, but it does not state the factorization of the normal initial form along the balanced line, the transverse multiplicity \(4\), or the tetrahedral normal tangent cone established here. The earlier Chterental--Doković work supplies the naive orthostochastic equations used by Chen--Dey, but predates the \(Z_4\) component analysis.

## Limitations
The endpoints \(p=0\) and \(p=1\) have a degenerate normal tangent cone and are not classified here. The result is local to the canonical block-circulant sections and does not determine the singularity type of the full six-dimensional variety \(Z_4\) along the balanced line. A reduced tangent cone with four hyperplanes does not by itself imply that the full analytic germ has four irreducible branches, and no such branch claim is made.

## References
1. Justin Chen and Papri Dey, *The 4 x 4 orthostochastic variety*, arXiv:2001.10691v1 (first public 2020-01-29); Experimental Mathematics, DOI:10.1080/10586458.2021.1982427.
2. Oleg Chterental and Dragomir Ž. Doković, *On orthostochastic, unistochastic and qustochastic matrices*, Linear Algebra and its Applications 428 (2008), 1178--1201, DOI:10.1016/j.laa.2007.09.022.
