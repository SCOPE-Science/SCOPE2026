# Geometry and finite-field census of wedge-divisible trivectors

## Finding
Let \(V\) be an \(n\)-dimensional vector space over an arbitrary field \(k\), with \(n\geq 6\), and let \(\Lambda(V)\) be its exterior algebra. For \(\alpha\in\Lambda^3V\) put
\[
D(\alpha)=\{v\in V:v\wedge\alpha=0\},\qquad
X_n=\{\alpha\in\Lambda^3V:D(\alpha)\ne0\}.
\]
The space \(D(\alpha)\) has dimension \(n\) when \(\alpha=0\), and otherwise exactly \(0\), \(1\), or \(3\). The nonzero elements with three-dimensional divisor space are exactly the decomposable trivectors. The elements with one-dimensional divisor space have a unique linear exterior factor and a nondecomposable bivector quotient.

Give \(X_n\) its reduced variety structure. Then \(X_n\) is a closed, irreducible, rational affine variety of dimension \(\binom n2\), and
\[
\operatorname{codim}_{\Lambda^3 V}(X_n)=\binom n3-\binom n2
=\frac{n(n-1)(n-5)}6.
\]
Its smooth locus consists exactly of the trivectors with one-dimensional divisor space; its singular locus is the affine cone over the Plücker Grassmannian \(\operatorname{Gr}(3,V)\), including the origin. In particular, that singular locus has dimension \(3n-8\).

For \(k=\mathbb F_q\), define Gaussian binomial coefficients \(G(a,b)=\bigl[\begin{smallmatrix}a\\b\end{smallmatrix}\bigr]_q\). The exact numbers \(N_d\) of trivectors having \(\dim D(\alpha)=d\) are
\[
\begin{aligned}
N_n&=1,\\
N_3&=(q-1)G(n,3),\\
N_1&=G(n,1)\bigl(q^{\binom{n-1}{2}}-1-(q-1)G(n-1,2)\bigr),\\
N_0&=q^{\binom n3}-N_n-N_3-N_1.
\end{aligned}
\]
All other values vanish. Equivalently, the rank of \(V\longrightarrow\Lambda^4V\), \(v\longmapsto v\wedge\alpha\), belongs to \(\{0,n-3,n-1,n\}\), with these same respective multiplicities. The formulas are valid for every prime power \(q\), including characteristic two.

There is also a homological consequence when \(n=6\). Exterior multiplication by \(\alpha\) is a square-zero degree-three differential on the 64-dimensional graded exterior algebra. For \(\alpha\ne0\) and \(d=\dim D(\alpha)\), its graded cohomology dimensions in degrees zero through six are
\[
(0,d,9+d,18,9+d,d,0),
\]
so its total cohomology dimension is \(36+4d\), namely \(36\), \(40\), or \(48\). The zero differential has total cohomology dimension \(64\). Thus the displayed \(N_d\) specialize to a complete finite-field distribution of these homology dimensions for six generators.

## Assumptions and scope
No restriction on the characteristic of \(k\) is imposed. An exterior bivector has rank \(2r\) when its canonical alternating normal form consists of \(r\) independent two-vector wedges; this definition works in characteristic two. A trivector is decomposable if it is a single wedge of three vectors. The expressions concerning singularities describe geometric points of reduced varieties (equivalently, after extending to an algebraic closure); they make no assertion about the potentially nonreduced determinantal scheme structure.

For the six-generator cohomology assertion, the differential is multiplication by an odd exterior element, not a claim that multiplication is a derivation. In characteristic two it still squares to zero because every element of odd exterior degree has zero square.

## Proof
**1. Possible divisor dimensions.** If \(0\ne v\in D(\alpha)\), choose a complement \(V=kv\oplus W\). Writing \(\alpha=v\wedge\beta+\gamma\) with \(\beta\in\Lambda^2W\) and \(\gamma\in\Lambda^3W\), the equation \(v\wedge\alpha=0\) forces \(\gamma=0\). Thus \(\alpha=v\wedge\beta\). For a nonzero bivector, its exterior divisors form a two-dimensional space exactly when its alternating rank is two (the bivector is simple); if its rank is at least four, it has no nonzero exterior divisors. Indeed, if \(w\wedge\beta=0\) with \(w\ne0\), the same splitting shows \(\beta=w\wedge z\) and hence has rank at most two. Applying this to the quotient \(W\simeq V/kv\), if \(\beta\) is simple then \(\alpha\) is decomposable and \(D(\alpha)\) is its three-plane of factors. If \(\beta\) has rank at least four then \(D(\alpha)=kv\): otherwise a second independent divisor would give a second divisor of \(\beta\) after quotienting by \(kv\). Conversely, every decomposable nonzero \(\alpha\) has precisely its three-plane as divisor space. The case \(\alpha=0\) gives \(D(0)=V\).

**2. Irreducibility, dimension and rationality.** Let \(\mathbf P(V)\) be the projective space of lines in \(V\), with tautological line bundle \(\mathcal L\) and quotient bundle \(\mathcal Q\). Consider the incidence variety
\[
Z=\{(L,\alpha):L\subset D(\alpha)\}\cong
\operatorname{Tot}\!\left(\mathcal L\otimes\Lambda^2\mathcal Q\right).
\]
It is a smooth irreducible vector bundle of rank \(\binom{n-1}{2}\) over \(\mathbf P(V)\), hence has dimension \((n-1)+\binom{n-1}{2}=\binom n2\). Its map to \(\Lambda^3V\) has image \(X_n\). Because the incidence is closed in \(\mathbf P(V)\times\Lambda^3V\) and \(\mathbf P(V)\) is proper, the image is closed. The locus where the quotient bivector has rank at least four is a nonempty open subset, since \(n-1\ge5\). On that locus the divisor line is unique by step 1, and is reconstructed as the kernel of the linear map \(v\mapsto v\wedge\alpha\). Thus the incidence map restricts to an isomorphism over the rank-one-divisor locus. The latter is smooth, dense and rational, because it is an open subset of a vector bundle over a rational projective space. The asserted dimensions and codimension follow.

**3. Exact singular locus.** The kernel line depends regularly on \(\alpha\) on the constant-rank locus \(\dim D(\alpha)=1\), by solving a nonzero maximal minor. Hence the incidence is an actual local inverse there, proving smoothness of every such point. For a nonzero decomposable point \(\alpha=a\wedge b\wedge c\), let \(U=\langle a,b,c\rangle\). For each line \(L\subset U\), the *linear* subspace \(L\wedge\Lambda^2V\) belongs to \(X_n\) and passes through \(\alpha\). Therefore the Zariski tangent space at \(\alpha\) contains the sum of those linear subspaces, namely \(U\wedge\Lambda^2V\). Its dimension is
\[
\binom n3-\binom{n-3}{3}=
\binom n2+(n-5)(n-2)>\binom n2\qquad(n\ge6),
\]
so the point is singular. At the origin, the tangent space contains every decomposable coordinate trivector, spanning the whole \(\Lambda^3V\), whose dimension exceeds \(\binom n2\) for \(n\ge6\). Thus zero is singular as well, and there are no others. The cone of nonzero simple trivectors has dimension \(\dim\operatorname{Gr}(3,V)+1=3(n-3)+1=3n-8\).

**4. Finite-field census.** Every three-plane of \(\mathbb F_q^n\) supports exactly \(q-1\) nonzero decomposable trivectors up to its unique Plücker line. Hence \(N_3=(q-1)G(n,3)\). For a fixed line \(L\), the vector space \(L\wedge\Lambda^2(V/L)\) has \(q^{\binom{n-1}{2}}\) elements. Of these, one is zero and \((q-1)G(n-1,2)\) have simple bivector quotients. Every remaining element has exactly this one divisor line, so multiplying by the number \(G(n,1)\) of lines counts each \(d=1\) element once. Subtracting from \(|\Lambda^3V|=q^{\binom n3}\) gives \(N_0\). This argument uses only finite-dimensional exterior algebra and Grassmannian counting, and applies over any finite characteristic.

**5. Six-generator cohomology.** For a nonzero \(\alpha\in\Lambda^3V\), the maps \(\Lambda^jV\to\Lambda^{j+3}V\) have ranks \(1,6-d,6-d,1\) for \(j=0,1,2,3\). The two central ranks agree by the perfect exterior pairing \(\Lambda^aV\times\Lambda^{6-a}V\to\Lambda^6V\), under which wedge multiplication is transpose up to a sign. The outer ranks are one because \(\alpha\ne0\). Wedge multiplication by \(\alpha\) squares to zero, so the homology in degree \(j\) has dimension \(\dim\Lambda^jV-\operatorname{rank}d_j-\operatorname{rank}d_{j-3}\), with out-of-range ranks zero. Substitution gives the displayed seven-tuple and total \(36+4d\).

## Verification
The standalone file `VERIFY.cpp` enumerates *all* \(2^{20}\) cubic trivectors in six variables over \(\mathbb F_2\), constructs each degree-one wedge matrix, and independently row-reduces it. It finds, respectively, \(1\), \(1395\), \(54684\), and \(992496\) trivectors with wedge-map ranks \(0\), \(3\), \(5\), and \(6\), agreeing with the formulas. It separately constructs the four nonzero degree maps of the cubic exterior differential for representative divisor types over \(\mathbb F_2\), \(\mathbb F_3\), and \(\mathbb F_5\), verifying all graded ranks and total homology dimensions. Run with `c++ -O2 -std=c++17 VERIFY.cpp -o verify && ./verify`. These checks are finite corroboration; the all-fields and all-dimensions statements rest on the argument above.

## Relationship to prior work
The linear-divisor space and the decomposability criterion are classical exterior-algebra facts, including the language used in Ghorpade–Patil–Pillai's 2007 work on decomposable subspaces and Grassmann codes. They are not claimed as new. Draisma–Shaw investigate singular lines defined by contraction of trilinear forms, a different geometric incidence condition. Kaipa–Pillai's finite-field orbit calculations for small-dimensional trilinear forms may already imply individual low-dimensional ranks and counts; no originality claim rests solely on the \(n=6\) numerical corollary. The new combined claim assessed here is the *uniform, all-\(n\ge6\) description* of the divisor-rank locus, its precise reduced singular locus, and the complete all-prime-power point census tied to exterior multiplication ranks. Earlier equivalent descriptions under different terminology, or implications of general subspace-variety theory, remain a publication-priority risk.

## Limitations
These are the reduced affine algebraic sets, not scheme-theoretic determinantal multiplicity assertions. The statement does not classify all \(\mathrm{GL}(V)\) orbits of trivectors, their stabilizers, or the cohomology of multiplication by a trivector in dimensions greater than six. No exhaustive historical-priority claim or independent mathematical audit is made.

## References
- S. R. Ghorpade, A. R. Patil and H. K. Pillai, *Decomposable Subspaces, Linear Sections of Grassmann Varieties, and Higher Weights of Grassmann Codes*, arXiv:0710.5161 (first posted 2007-10-26).
- J. Draisma and R. Shaw, *Singular lines of trilinear forms*, arXiv:0909.5676 (first posted 2009-09-30).
- K. V. Kaipa and H. K. Pillai, *Weight spectrum of codes associated with the Grassmannian G(3,7)*, arXiv:1203.0290 (first posted 2012-03-01).
- D. Bulavka and collaborators, *A Hilton–Milner theorem for exterior algebras*, DOI:10.1112/tlm3.70022 (later related literature; included solely for comparison).
