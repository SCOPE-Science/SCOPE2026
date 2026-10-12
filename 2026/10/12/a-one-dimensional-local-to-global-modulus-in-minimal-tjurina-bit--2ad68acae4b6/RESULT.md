# A one-dimensional local-to-global modulus in minimal-Tjurina bitangent arrangements
## Finding
Let \(m\ge 3\) and let \(A=\{a_1,\ldots,a_m\}\subset\mathbb C^*\) be a set of distinct parameters. Consider
\[
C_A=V\!\left(\prod_{a\in A}(xz+a y^2)\right),\qquad
D_A=V\!\left(y\prod_{a\in A}(xz+a y^2)\right).
\]
These are respectively the \(\mathcal C_2\) and \(\mathcal{CL}_6\) families in Beorchia--Miró-Roig. Their Theorem 3.6 identifies precisely these two families as the reduced conic-line arrangements of degree \(d\ge 6\) with a linear Jacobian syzygy and minimal global Tjurina number \(\tau=d^2-3d+2\); Example 3.3 also records that they are nearly free.

The additional statement proved here is a local-to-global moduli separation. The singular locus of either arrangement is exactly
\[
\{p,q\}=\{[1:0:0],[0:0:1]\}.
\]
At either point the germ of \(C_A\) is analytically equivalent to
\[
G_A:\ \prod_{a\in A}(z+a y^2)=0,
\]
and the germ of \(D_A\) is analytically equivalent to
\[
H_A:\ y\prod_{a\in A}(z+a y^2)=0.
\]
For either family, the germs attached to \(A\) and \(B\) are analytically equivalent if and only if
\[
B=uA+v
\]
for some \(u\in\mathbb C^*\) and \(v\in\mathbb C\). In contrast, the global projective arrangements are equivalent if and only if
\[
B=cA
\]
for some \(c\in\mathbb C^*\). Hence the unordered local-analytic parameter space has generic dimension \(m-2\), while the projective parameter space has generic dimension \(m-1\). The natural map from projective classes to the pair of embedded local analytic germ types therefore has generic one-dimensional fibers.

For a concrete witness, take
\[
A=\{1,2,4\},\qquad B=\{2,3,5\}=A+1.
\]
The corresponding degree-six \(C_A,C_B\) and degree-seven \(D_A,D_B\) have analytically identical germs at both singular points, but neither pair is projectively equivalent.

## Assumptions and scope
The ground field is \(\mathbb C\). All parameters are nonzero and pairwise distinct, and translations \(A\mapsto A+v\) are considered only when \(0\notin A+v\), so every displayed conic remains smooth. The claim concerns embedded analytic equivalence of the reduced plane-curve germs and projective equivalence of the global reduced arrangements.

For \(C_A\), every component is a smooth conic. For \(D_A\), the additional component is the line \(y=0\). The result does not claim that the abstract topological type of these singularities is new; it identifies the exact analytic parameter quotient and compares it with the global projective quotient for the source's extremal nearly free families.

## Proof
For distinct \(a,b\in A\), simultaneous vanishing of
\[
xz+a y^2=0,\qquad xz+b y^2=0
\]
forces \(y=0\), hence \(xz=0\). Thus any two conics meet only at \(p\) and \(q\). Since each conic is smooth when \(a\ne0\), these are the only singular points of \(C_A\). The line \(y=0\) also meets every conic only at \(p,q\), so the same is true for \(D_A\).

On the affine chart \(x=1\) at \(p\), each conic has equation \(z+a y^2=0\). On the chart \(z=1\) at \(q\), after renaming the affine coordinate \(x\) as \(z\), one obtains the identical germ. This gives \(G_A\), and adding the line \(y=0\) gives \(H_A\).

We classify these germs. Suppose first that an analytic coordinate change sends \(G_A\) to \(G_B\). The unique tangent line, counted with multiplicity \(m\), is \(z=0\), so the linear part has the form
\[
Y=\alpha y+\beta z+O(2),\qquad Z=\delta z+\gamma y^2+O(3),
\]
with \(\alpha\delta\ne0\); only the displayed terms affect the quadratic contact coefficient of a branch. Along the branch \(z=-a y^2\), one has
\[
Y^2=\alpha^2y^2+O(y^3),\qquad
Z=(\gamma-\delta a)y^2+O(y^3).
\]
If its image is the branch \(Z+bY^2=0\), comparison of the quadratic terms gives
\[
b=\frac{\delta a-\gamma}{\alpha^2}=ua+v,
\]
where \(u\ne0\). Since branches may be permuted, necessarily \(B=uA+v\). Conversely, whenever \(B=uA+v\), the analytic automorphism
\[
Y=y,\qquad Z=uz-vy^2
\]
satisfies
\[
Z+(ua+v)Y^2=u(z+a y^2)
\]
for every \(a\in A\), proving sufficiency. For \(H_A\), the line \(y=0\) is the unique branch transverse to the common tangent of the other \(m\) branches, so it is intrinsic; the same argument applies, and the displayed coordinate change also preserves it.

It remains to compare global projective equivalence. Two distinct conic components span the pencil
\[
\langle xz,y^2\rangle.
\]
The symmetric matrix of \(\lambda xz+\mu y^2\) has determinant proportional to \(-\mu\lambda^2\). Hence the pencil contains a unique rank-one member \(y^2\) and a unique rank-two member \(xz\). Any projectivity carrying one arrangement in the family to another must normalize this pencil and preserve these two rank strata, so it fixes both distinguished pencil parameters. Its induced action on the pencil parameter is therefore a scaling. Equivalently, after allowing the harmless interchange \(x\leftrightarrow z\), one obtains exactly
\[
a\longmapsto ca.
\]
Thus \(C_A\cong_{\mathbb P^2}C_B\), and likewise \(D_A\cong_{\mathbb P^2}D_B\), exactly when \(B=cA\). This agrees with the scaling description of the bitangent-pencil stabilizer in Aluffi--Faber, Lemma 3.1.

The configuration space of \(m\) unordered distinct points of \(\mathbb A^1\) has dimension \(m\). Quotienting the local coefficients by the two-dimensional affine group gives generic dimension \(m-2\); quotienting the global parameters by scaling gives generic dimension \(m-1\). The difference is one. Translation \(A\mapsto A+v\) keeps the local analytic class fixed but, generically, changes the global projective class.

For \(A=\{1,2,4\}\) and \(B=A+1=\{2,3,5\}\), the local equivalence is the explicit map \(Y=y, Z=z-y^2\). Global scaling cannot identify the sets: because \(1\in A\), any scaling factor would have to be one of \(2,3,5\), and none sends \(\{1,2,4\}\) to \(\{2,3,5\}\). This proves the concrete counterexample.

## Verification
The accompanying verifier checks symbolically that the singular pencil has determinant proportional to \(-\mu\lambda^2\), verifies the exact affine transformation identity
\[
Z+(ua+v)Y^2=u(z+a y^2),
\]
checks the second-order coefficient transformation, and confirms that \(\{1,2,4\}\) and \(\{2,3,5\}\) are translation-equivalent but not scaling-equivalent. It also verifies the expected local Milnor numbers from pairwise contacts: \((m-1)(2m-1)\) for \(G_A\) and \(m(2m-1)\) for \(H_A\), which for \(m=3\) sum over the two singular points to the source's global Tjurina numbers \(20\) and \(30\), respectively.

## Relationship to prior work
Beorchia--Miró-Roig supply the exact families, their nearly free property, and the classification by minimal global Tjurina number. Their paper does not identify the embedded local analytic equivalence relation on the finite parameter set, nor compare it with projective equivalence.

Aluffi--Faber study small \(\operatorname{PGL}_3\)-orbits of plane curves built from such pencils. Their Lemma 3.1 describes finite stabilizer components through scaling symmetries of the pencil parameters and the extra coordinate switch in the bitangent case. That global symmetry calculation is treated here as prior coverage. The new point is the mismatch between that multiplicative global quotient and the affine local analytic quotient, together with the resulting one-dimensional fibers and explicit locally identical but projectively inequivalent nearly free arrangements.

## Limitations
The theorem is specific to the two minimal-Tjurina bitangent families \(\mathcal C_2\) and \(\mathcal{CL}_6\), with \(m\ge3\). It does not classify analytic moduli for arbitrary conic pencils or arbitrary nearly free curves. The originality assessment is literature-search based; older singularity literature could encode the affine classification in more general language, although no source located states the family-specific local-to-global comparison proved here.

## References
1. V. Beorchia and R. M. Miró-Roig, *Jacobian Schemes of Conic-Line Arrangements and Eigenschemes*, arXiv:2303.04665, first public version 8 March 2023; Mediterranean Journal of Mathematics 21 (2024), article 16, DOI 10.1007/s00009-023-02553-5.
2. P. Aluffi and C. Faber, *Plane curves with small linear orbits, I*, Annales de l'Institut Fourier 50 (2000), 151--196, DOI 10.5802/aif.1750; especially Lemma 3.1.
