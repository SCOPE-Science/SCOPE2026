# Ordinary ideals in translation skew group rings are controlled by the action kernel
## Finding
Let \(k\) be a field of characteristic \(0\), let \(G\) be an abelian group, and let \(c:G\to(k,+)\) be a nonzero homomorphism. Consider
\[
A=k[X]\rtimes G,
\qquad
u_gX=(X-c(g))u_g,
\]
where the symbols \(u_g\) form the group basis. Put \(K=\ker c\) and \(C=kK\). Then
\[
Z(A)=C,
\]
and contraction and extension are mutually inverse lattice isomorphisms
\[
\operatorname{Id}(A)\longleftrightarrow\operatorname{Id}(C),
\qquad
I\longmapsto I\cap C,
\qquad
J\longmapsto AJ.
\]
Equivalently, every two-sided ideal \(I\) of \(A\) satisfies
\[
I=A(I\cap C),
\]
and every ideal \(J\) of \(C\) satisfies \(AJ\cap C=J\). Moreover
\[
(AJ_1)(AJ_2)=A(J_1J_2),
\]
so prime and maximal two-sided ideals of \(A\) correspond exactly to prime and maximal ideals of \(C\).

If \(G\cong\mathbb Z^d\) and \(r=\operatorname{rank}_{\mathbb Z}c(G)\), then \(K\cong\mathbb Z^{d-r}\) and hence
\[
C\cong k[z_1^{\pm1},\ldots,z_{d-r}^{\pm1}].
\]
Thus all ordinary two-sided ideal, prime, and maximal-ideal questions in this family reduce to a Laurent polynomial ring.

The characteristic-zero hypothesis is sharp for this correspondence. In characteristic \(p\), with \(G=\mathbb Z\) and \(c(1)=1\), the polynomial \(X^p-X\) is translation-invariant and yields a proper two-sided ideal whose contraction to \(k\ker c\) is zero.

## Assumptions and scope
The ring is the translation case of the group-graded Ore family in Ait Mohamed, after the standard change of variable that identifies that family with a skew group ring. The hypotheses used here are: \(G\) is abelian; \(c\ne0\); and \(\operatorname{char}k=0\). No finite generation of \(G\) is needed for the ideal correspondence. The Laurent-polynomial description is the additional specialization \(G\cong\mathbb Z^d\).

## Proof
Because \(G\) is abelian and every \(k\in K\) acts trivially on \(X\), the subring \(C=kK\) is central in \(A\).

Let \(I\) be a two-sided ideal and take a nonzero finite-support element
\[
a=\sum_g f_g(X)u_g\in I.
\]
The inner derivation \(\operatorname{ad}_X\) acts diagonally on the group components:
\[
[X,f_g(X)u_g]=c(g)f_g(X)u_g.
\]
Only finitely many eigenvalues \(c(g)\) occur in \(a\). For each occurring value \(\lambda\), Lagrange interpolation in the operator \(\operatorname{ad}_X\) isolates the full block
\[
a_\lambda=\sum_{c(g)=\lambda} f_g(X)u_g\in I.
\]
Choose \(h\in G\) with \(c(h)=\lambda\). Right multiplication by \(u_h^{-1}\) moves this block into \(C[X]\), since every \(gh^{-1}\) occurring has \(c(gh^{-1})=0\). Therefore every block of every element of \(I\) is a group unit times an element of \(I\cap C[X]\).

Write \(J=I\cap C\). We show
\[
I\cap C[X]=J[X].
\]
Choose \(q\in G\) with \(a_0=c(q)\ne0\). Conjugation by \(u_q\) translates \(X\) by \(-a_0\). Hence, for every \(F(X)\in I\cap C[X]\), also \(F(X-a_0)\in I\cap C[X]\). If \(F\) has positive degree \(n\) and leading coefficient \(b_n\in C\), the finite difference
\[
F(X-a_0)-F(X)
\]
has degree \(n-1\) and leading coefficient \(-n a_0b_n\). Induction on degree shows this difference lies in \(J[X]\). Since \(\operatorname{char}k=0\), the scalar \(-na_0\) is nonzero and invertible in \(k\), so \(b_n\in J\). Subtracting \(b_nX^n\) and continuing by induction gives \(F\in J[X]\). The reverse inclusion is immediate.

The isolated-block argument now gives \(I\subseteq AJ\), while \(AJ\subseteq I\) is automatic; hence
\[
I=A(I\cap C).
\]
Conversely, for \(J\triangleleft C\), centrality of \(C\) makes \(AJ\) a two-sided ideal. Decomposing \(A\) over representatives of \(G/K\) and by polynomial degree shows that the degree-zero, trivial-coset component of \(AJ\) is exactly \(J\); thus \(AJ\cap C=J\). This proves the lattice isomorphism.

For the center, if \(z\in Z(A)\), then \([X,z]=0\) removes every group component outside \(K\), so \(z\in C[X]\). Commuting with \(u_q\) forces \(F(X-a_0)=F(X)\). The same leading-term finite-difference argument shows that \(F\) has degree zero, giving \(Z(A)=C\).

Centrality also gives \((AJ_1)(AJ_2)=A(J_1J_2)\). Therefore the lattice isomorphism preserves maximal ideals, and the product identity shows that it preserves and reflects primality.

Finally, in characteristic \(p\), for the translation \(X\mapsto X-1\),
\[
(X-1)^p-(X-1)=X^p-X.
\]
Thus \(X^p-X\) is invariant. The ideal it generates is proper and has positive \(X\)-degree, while its intersection with \(k\ker c\) is zero. Hence the characteristic-zero conclusion does not extend unchanged to positive characteristic.

## Verification
The proof is symbolic. The critical points checked directly are: diagonalization of \(\operatorname{ad}_X\) on each finite support; validity of Lagrange interpolation because only finitely many distinct eigenvalues occur at once; the degree drop and nonvanishing leading coefficient in the finite-difference step; contraction after extension; and the positive-characteristic invariant-polynomial boundary example. No finite experiment is used as a substitute for the universal argument.

## Relationship to prior work
Ait Mohamed's 2026 preprint identifies the relevant Ore family with an affine skew group ring and classifies its graded ideals; in characteristic zero it also characterizes graded simplicity and simplicity. The ordinary two-sided ideal lattice in the non-simple translation case is not stated there.

Öinert's work on skew group rings of abelian groups proves ideal-intersection and simplicity criteria, including nonzero intersection with the center under appropriate hypotheses. Öinert, Lundström, and others likewise obtain nonzero ideal intersections with commutants determined by central kernels in strongly graded settings. These intersection theorems are strictly weaker than the equality \(I=A(I\cap Z(A))\) proved here.

Mihovski's 2001 paper on invariant ideals of crossed products gives a potentially relevant generation theorem involving a subgroup attached to an invariant subfield. Only the accessible abstract was available for comparison. In the present translation action, the natural fixed scalar field is fixed by all of \(G\), so the displayed abstract statement does not identify the kernel \(K=\ker c\) and does not visibly imply the claimed central ideal-lattice isomorphism. This remains the main literature risk.

## Limitations
The exact contraction-extension proof uses characteristic zero in the finite-difference leading coefficient \(-na_0\). Positive characteristic has explicit additional translation-invariant polynomials. The theorem assumes \(G\) abelian; nonabelian groups need not have central \(k\ker c\), and the conclusion is not asserted there. The literature comparison is limited by lack of full-text access to the Mihovski paper, so a remote possibility of a more general older theorem subsuming the result remains.

## References
1. A. Ait Mohamed, *Group-graded Ore extensions and graded simplicity*, arXiv:2609.38131v1 (2026).
2. J. Öinert, *Simplicity of skew group rings of abelian groups*, arXiv:1111.7214.
3. J. Öinert et al., *Commutativity and Ideals in Strongly Graded Rings*, Annals of Functional Analysis / Applied Categorical Structures literature, DOI: 10.1007/s10440-009-9435-3.
4. D. Mihovski, *A-Invariant Ideals of Crossed Products*, Communications in Algebra 29 (2001), DOI: 10.1081/AGB-100105035.
