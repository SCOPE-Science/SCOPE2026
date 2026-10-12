# Projective moduli and symmetry jumps of free four-hyperflex quartic arrangements

## Finding
For each \(\lambda\in\mathbb C\setminus\{0,1\}\), put \(H_\lambda=xy(x-y)(x-\lambda y)\) and define the reduced plane curve
\[
\mathcal X_\lambda:\quad H_\lambda(x,y)\bigl(H_\lambda(x,y)-z^4\bigr)=0\subset\mathbb P^2_\mathbb C.
\]
Its irreducible components are one smooth quartic and four distinct lines. All four lines are hyperflex tangents of the quartic and concur away from it. The complete singularity basket is one ordinary fourfold point together with four singularities of type \(A_7\). Every member is free with exponents \((3,4)\).

The exact projective equivalence relation is
\[
\mathcal X_\lambda\cong_{\mathrm{PGL}_3(\mathbb C)}\mathcal X_\mu
\iff \mu\in\left\{\lambda,1-\lambda,\lambda^{-1},(1-\lambda)^{-1},\lambda/(\lambda-1),(\lambda-1)/\lambda\right\}.
\]
Equivalently, the two curves are projectively equivalent exactly when \(j(\lambda)=j(\mu)\), where
\[
j(\lambda)=256\frac{(1-\lambda+\lambda^2)^3}{\lambda^2(1-\lambda)^2}.
\]
The coarse projective classification set of this family is therefore the affine \(j\)-line.

Let \(D_\lambda\) be the unordered set of four roots of \(H_\lambda\) on \(\mathbb P^1\), and let \(K_\lambda\subset\mathrm{PGL}_2(\mathbb C)\) be its full stabilizer. The full projective automorphism group of the **reducible curve**, not merely of its quartic component, is
\[
G_\lambda=\left\{[\operatorname{diag}(A,c)]:A\in\mathrm{GL}_2(\mathbb C),\ c\in\mathbb C^\times,\ H_\lambda(A(x,y))=c^4H_\lambda(x,y)\right\}.
\]
Here brackets mean projective matrix class. There is a central exact sequence
\[
1\longrightarrow\mu_4\longrightarrow G_\lambda\longrightarrow K_\lambda\longrightarrow1,
\]
with \(K_\lambda\cong V_4\), \(D_4\), or \(A_4\), according as \(j(\lambda)\) is neither \(0\) nor \(1728\), equals \(1728\), or equals \(0\). Consequently,
\[
|G_\lambda|=\begin{cases}16&j(\lambda)\notin\{0,1728\},\\32&j(\lambda)=1728,\\48&j(\lambda)=0.\end{cases}
\]
At the harmonic value \(j=1728\), the smooth quartic component is projectively isomorphic to the Fermat quartic with \(96\) projective automorphisms, but its full eight-degree marked union with four tangent lines retains only \(32\) of them.

## Assumptions and scope
Work over the complex numbers, in characteristic zero. The parameter must avoid \(0\) and \(1\), otherwise the four line components cease to be distinct. Projective equivalence means equality after an element of \(\mathrm{PGL}_3(\mathbb C)\); no arbitrary abstract isomorphisms are included. The claimed classification concerns precisely the displayed four-line plus quartic family; it does not classify all free plane curves of degree eight or all configurations of four quartic hyperflex tangents.

## Proof
**1. Smoothness and singularities.** The quartic \(C_\lambda: H_\lambda-z^4=0\) has \(\partial C_\lambda/\partial z=-4z^3\). Any singular point would have \(z=0\) and simultaneously \(H_\lambda=\partial_xH_\lambda=\partial_yH_\lambda=0\). This is impossible because \(H_\lambda\) is a squarefree binary quartic. Thus \(C_\lambda\) is smooth and irreducible. The four lines are \(x=0\), \(y=0\), \(x=y\), and \(x=\lambda y\); they meet only at \(P=[0:0:1]\), which is not on \(C_\lambda\). The intersection of any such line with \(C_\lambda\) is supported at its point at infinity, with total multiplicity four, because restricting its quartic equation to that line gives \(-z^4\). In analytic local coordinates at this point the equation of the union is \(u(u-v^4)=0\), which is \(A_7\). At \(P\) the equation is four distinct linear factors times a unit, yielding an ordinary fourfold point. These are all singularities, since the quartic is smooth and there are no other pairwise intersections.

**2. Freeness and explicit Jacobian certificate.** Write \(H=H_\lambda\) and \(f=H(H-z^4)\). Its partials are
\[
f_x=(2H-z^4)H_x,\qquad f_y=(2H-z^4)H_y,\qquad f_z=-4Hz^3.
\]
There are two polynomial Jacobian syzygies
\[
\rho_3=(H_y,-H_x,0),\qquad \rho_4=(xz^3,yz^3,2H-z^4).
\]
Euler's identity \(xH_x+yH_y=4H\) gives \(\rho_4\cdot\nabla f=0\); the other relation is immediate. Their cross product equals \(-\nabla f\) exactly. The criterion for a reduced plane curve that two homogeneous syzygies whose cross product is a nonzero constant times the gradient form a free basis (Saito's determinant criterion) proves the exponents \((3,4)\). Independently, the above basket gives total Tjurina number \(4\cdot7+(4-1)^2=37=(8-1)^2-3\cdot4\), consistent with freeness. Freeness and the basic construction are already established more generally in Theorem 1.5 of Dimca--Ilardi--Pokora--Sticlaru; they are not claimed as new.

**3. Projective rigidity.** Suppose a projective map \(T\) carries \(\mathcal X_\lambda\) to \(\mathcal X_\mu\). The quartic component is uniquely characterized as the only component of degree greater than one. The four line components have the unique common intersection point \(P=[0:0:1]\); hence \(T(P)=P\). Consequently a linear representative has block form
\[
T=\begin{pmatrix}A&0\\ \ell&c\end{pmatrix},
\]
where \(A\in\mathrm{GL}_2(\mathbb C)\), \(\ell\) is a linear form in \(x,y\), and \(c\ne0\). Preservation of the unique quartic component gives the polynomial identity
\[
H_\mu(A(x,y))-(\ell(x,y)+cz)^4=\alpha\bigl(H_\lambda(x,y)-z^4\bigr)
\]
for some \(\alpha\ne0\). Comparing coefficients of \(z^3\) forces \(\ell=0\); comparing \(z^4\) gives \(\alpha=c^4\); thus \(H_\mu\circ A=c^4H_\lambda\). Conversely, every projective change of \([x:y]\) taking one unordered root set to the other can be represented by \(A\) with \(H_\mu\circ A=\alpha H_\lambda\); choosing any fourth root \(c\) of \(\alpha\) lifts it to a projective equivalence. No other projective equivalences or automorphisms exist.

**4. Four-point moduli.** Four distinct unordered points of \(\mathbb P^1\) are equivalent precisely under the six anharmonic changes of cross-ratio displayed in the finding. Their classical invariant \(j\) separates these orbits: the equation \(j(t)=j(\lambda)\), after clearing denominators, has exactly the anharmonic orbit as its set of roots (with multiplicities at special values). Every finite \(j\in\mathbb C\) has a preimage distinct from \(0,1\), because the only poles of this rational invariant are \(0,1,\infty\). The moduli classification follows.

**5. Stabilizers.** Specialize Step 3 to \(\mu=\lambda\). The projection \(G_\lambda\to K_\lambda\) is surjective by the fourth-root lifting argument. Its kernel is the four deck transformations \([x:y:z]\mapsto[x:y:\zeta z]\), with \(\zeta^4=1\), which commute with every block-diagonal automorphism. The cross-ratio orbit has six values generically, three when \(\lambda\in\{-1,2,\frac12\}\), and two when \(\lambda^2-\lambda+1=0\). The stabilizer in \(S_4\) therefore has size \(24/6=4\), \(24/3=8\), and \(24/2=12\), respectively. These are the well-known Klein-four, dihedral, and tetrahedral permutation subgroups. The exceptional conditions are precisely \(j=1728\) and \(j=0\). Multiplication by the four deck lifts yields orders \(16,32,48\).

**6. The harmonic Fermat symmetry gap.** When \(\lambda=-1\), the binary quartic \(xy(x^2-y^2)\) has harmonic root cross-ratio, as does \(x^4+y^4\). A binary linear transformation therefore identifies them up to a scalar. After rescaling \(z\), \(C_{-1}\) becomes the Fermat quartic, classically known to have \(96\) projective automorphisms. Step 5 gives precisely \(32\) projective automorphisms of its prescribed quartic-plus-four-tangent-line union, of index three in the quartic automorphism group.

## Verification
The accompanying symbolic verifier computes both syzygies, their cross product with the complete Jacobian gradient, Euler's formula, invariance of \(j\) under all six anharmonic transformations, and exact generic, harmonic, and equianharmonic sample stabilizer sizes. It also checks \(\tau=37\). These finite and symbolic checks reproduce key polynomial identities; the exhaustive classification and all complex parameters are established by Steps 3--5, not inferred from sampled values. Run \(\texttt{python verify.py}\) with the versions in \(\texttt{requirements.txt}\).

## Relationship to prior work
Dimca, Ilardi, Pokora, and Sticlaru's Theorem 1.5 (arXiv:2301.01117; 2023-01-03) already establishes freeness for arbitrary collections of distinct binary linear factors. Their Section 5 also discusses smooth plane quartics with many hyperflexes, including Fermat's \(96\) quartic automorphisms. Classical cross-ratio and anharmonic stabilizer theory already classifies unordered four-point sets on a line. Van Bommel and collaborators summarize the classical large automorphism groups of smooth quartics, including \(G_{48}\) and Fermat's \(G_{96}\), in Section 7.2.1 of their paper on quartics and Cayley octads. The separate assertion proved here is the complete *projective moduli and full stabilizers of the marked reducible free curves*, using their intrinsic component structure and the block-diagonal rigidity argument. In particular, the harmonic marked union has only a subgroup of index three of the smooth quartic's symmetries.

## Limitations
The quartic freeness statement and cross-ratio facts are established prior mathematics, not new discoveries. The result makes no assertion of abstract isomorphism classification or exhaustive classification of every degree-eight free plane curve. The group exact sequence specifies the marked arrangement's full projective stabilizer but does not give a separate abstract group presentation for every member. Although the cited literature was inspected for directly matching statements, an equivalent special-case projective stabilizer calculation in unindexed historical literature cannot be excluded. Independent external validation has not been performed.

## References
1. A. Dimca, G. Ilardi, P. Pokora, and G. Sticlaru, *Construction of free curves by adding lines to a given curve*, arXiv:2301.01117 (first public version, 2023-01-03), Theorem 1.5 and Section 5; DOI: 10.1007/s00025-023-02036-9. Primary MSC 14H50.
2. R. van Bommel, J. Docking, V. Dokchitser, R. Lercier, and E. Lorenzo García, *Reduction of Plane Quartics and Cayley Octads*, Section 7.2.1, DOI: 10.1007/s10208-025-09704-y; open-access text published 2025-06-02.
3. Classical anharmonic six-valued cross-ratio invariant and the stabilizers of four distinct points of the projective line (standard projective geometry).
