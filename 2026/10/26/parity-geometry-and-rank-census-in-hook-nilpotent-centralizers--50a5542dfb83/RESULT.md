# Parity geometry and rank census in hook nilpotent centralizers

## Finding

For every field \(k\) and integer \(n\ge3\), let \(N=J_n(0)\oplus J_1(0)\) act on \(k^{n+1}\). Consider the square-zero centralizer locus
\[
\mathcal Z_n(k)=\{X\in\operatorname{End}_k(k^{n+1}):XN=NX,\ X^2=0\}.
\]
The **reduced algebraic variety** underlying this locus has a sharp parity transition. When \(n=2h\),
\[
\mathcal Z_n^{\mathrm{red}}\cong\mathbb A^h\times V(bc),
\]
a union of two affine spaces of dimension \(h+1\), meeting in an affine space of dimension \(h\). When \(n=2h+1\),
\[
\mathcal Z_n^{\mathrm{red}}\cong\mathbb A^h\times V(bc+z^2),
\]
an irreducible quadratic cone times affine space, of dimension \(h+2\). In both cases the singular locus of the reduced variety has dimension \(h\), and the descriptions remain valid in characteristic two.

For every finite field \(\mathbb F_q\), the complete ordinary matrix-rank generating polynomial is
\[
\boxed{\begin{aligned}
R_{n,q}(u)&=\sum_{X\in\mathcal Z_n(\mathbb F_q)}u^{\operatorname{rank}X}\\
&=1+(q-1)(2q+1)u
 +(q-1)(2q-1)\sum_{r=2}^{\lfloor n/2\rfloor}q^{r-1}u^r\\
&\quad+\mathbf1_{n\ \mathrm{odd}}(q-1)^2q^{(n-1)/2}u^{(n+1)/2}.
\end{aligned}}
\]
(The sum is empty when its lower limit exceeds its upper limit.) Thus
\[
\boxed{\#\mathcal Z_n(\mathbb F_q)=
\begin{cases}
(2q-1)q^{n/2},&n\ \mathrm{even},\\
q^{(n+3)/2},&n\ \mathrm{odd}.
\end{cases}}
\]
Multiplication by \(X\) defines a square-zero differential on \(k^{n+1}\) commuting with \(N\). Such a differential is acyclic over \(\mathbb F_q\) exactly for odd \(n\) at rank \((n+1)/2\); its exact count is \((q-1)^2q^{(n-1)/2}\). The acyclicity count is zero for even \(n\).

## Assumptions and scope

Here \(k\) is an arbitrary field, \(J_n(0)\) is one nilpotent Jordan block of size \(n\), and \(J_1(0)\) is a one-dimensional zero block. The geometry is that of the underlying **reduced** algebraic set, not a statement about the possibly nonreduced scheme defined by the raw entries of \(X^2\). The finite-field assertions apply to every prime power \(q\), with no characteristic restriction. Ranks are ordinary \(k\)-linear ranks, not ranks over a truncated polynomial ring. Throughout, \(n\ge3\).

## Proof

**Centralizer coordinates.** Let \(R=k[t]/(t^n)\) and \(M=R\oplus k\), with \(t\) acting as \(N\). An \(R\)-linear endomorphism has unique coordinates \(a\in R\), \(b,c,d\in k\):
\[
X(f,u)=(af+b t^{n-1}u,\;cf(0)+du).
\]
This follows from \(\operatorname{End}_R(R)=R\), \(\operatorname{Hom}_R(k,R)=kt^{n-1}\), and \(\operatorname{Hom}_R(R,k)=k\), using the displayed bases. Squaring gives the four block conditions
\[
a^2+bc\,t^{n-1}=0,\qquad b(a_0+d)=0,\qquad c(a_0+d)=0,\qquad d^2=0,
\]
where \(a_0=a(0)\). The last equation forces \(d=0\); the constant coefficient of the first forces \(a_0=0\). The middle two are then automatic, so
\[
X^2=0\quad\Longleftrightarrow\quad d=a_0=0\ \text{and}\ a(t)^2+bc\,t^{n-1}=0\pmod {t^n}.
\]
This reasoning uses no restriction on characteristic.

**Valuation and geometry.** If \(a\ne0\), write \(v=\operatorname{ord}_t(a)\). The first nonzero term of \(a^2\) has exponent \(2v\) and nonzero coefficient. It cannot be canceled by \(bc\,t^{n-1}\) when \(2v<n-1\). If \(n=2h\), this forces \(a_0=\cdots=a_{h-1}=0\), after which \(a^2=0\) and \(bc=0\). The free coefficients are \(a_h,\ldots,a_{2h-1}\), giving \(\mathbb A^h\times V(bc)\). If \(n=2h+1\), it forces \(a_0=\cdots=a_{h-1}=0\), and the remaining equation is \(a_h^2+bc=0\); the \(h\) coefficients \(a_{h+1},\ldots,a_{2h}\) are free. This gives \(\mathbb A^h\times V(bc+z^2)\). These assertions also hold when \(a=0\).

The even locus has two transverse affine components, with intersection (and precisely the reduced singular locus) \(b=c=0\). For odd \(n\), the polynomial \(bc+z^2\) is irreducible over any field: regarded as a polynomial linear in \(b\), its coefficients \(c\) and \(z^2\) are coprime. Its partial derivatives are \(c,b,2z\); on the hypersurface they simultaneously vanish precisely at \(b=c=z=0\), even in characteristic two. Thus the asserted irreducibility, dimensions, and singular loci follow.

**Rank lemma.** For a square-zero \(X\) with \(a\ne0\) and \(v\le n-2\), the images of \(t,t^2,\ldots,t^{n-1}\) span \(t^{v+1}R\) of dimension \(n-v-1\). The vector \(X(1,0)=(a,c)\) adds one independent image direction, whereas \(X(0,1)=(bt^{n-1},0)\) is already in that span. Hence \(\operatorname{rank}X=n-v\). If \(v=n-1\), the relation \(bc=0\) makes all images span a single line, so the rank is one. If \(a=0\), then \(bc=0\), giving rank one if exactly one of \(b,c\) is nonzero and rank zero otherwise.

**Counting fibers.** Rank one receives \((q-1)(2q-1)\) choices with \(v=n-1\), plus \(2(q-1)\) with \(a=0\); their sum is \((q-1)(2q+1)\). For each \(2\le r\le\lfloor n/2\rfloor\), put \(v=n-r\). The leading coefficient of \(a\) has \(q-1\) choices, the \(r-1\) subsequent coefficients have \(q^{r-1}\) choices, and \(bc=0\) has \(2q-1\) solutions. These give \((q-1)(2q-1)q^{r-1}\) matrices. Only for \(n=2h+1\) is there another valuation \(v=h\): its nonzero leading coefficient has \(q-1\) choices, the \(h\) upper coefficients are free, and \(bc=-a_h^2\ne0\) has \(q-1\) solutions. This gives \((q-1)^2q^h\) matrices of rank \(h+1\). The zero matrix is unique. Summation yields \(R_{n,q}(u)\). Alternatively, \(\#V(bc)(\mathbb F_q)=2q-1\), while \(\#V(bc+z^2)(\mathbb F_q)=q^2\); the stated total counts follow. Finally the homology dimension of a square-zero linear map on \(k^{n+1}\) is \(n+1-2\operatorname{rank}X\), establishing the acyclicity assertion.

## Verification

The included standalone `check.py` enumerates **all** \(q^{n+3}\) coordinate tuples for each test case, constructs the corresponding actual \((n+1)\)-square matrix, tests its square directly, and independently computes its rank by elimination. It checks \(q=2\), \(3\), \(4\), and \(5\), including \(\mathbb F_4\), across 14 field-size/dimension combinations with \(3\le n\le8\). The executed program ended with `HOOK_SQUARE_ZERO_RANK_OK 14 exhaustive fields/dimensions`. These finite enumerations verify examples and detect formula errors; the preceding argument, not enumeration, proves the infinite family.

Run from the same directory: `python check.py`.

## Relationship to prior work

Britnell and Wildon study *which* nilpotent similarity classes can contain commuting representatives, including two-part partitions, rather than exact point counts in the square-zero fiber of one fixed hook class. Basili, Iarrobino, and Khatami investigate the full nilpotent centralizer and its generic Jordan type; the irreducibility of that larger nilpotent locus does not imply that the square-zero sublocus is irreducible, and indeed the even hook case here is reducible. Hua develops canonical forms for **indecomposable** pairs of commuting nilpotent matrices with unequal block lengths, including the broader two-block setting. His classification does not directly provide the labeled finite-field rank multiplicities or reduced singular-locus geometry of the whole square-zero fiber. These known classifications and centralizer descriptions are not themselves claimed as new. The asserted contribution is their characteristic-uniform, parity-resolved, exact square-zero fiber geometry and full rank census for the hook family.

## Limitations

No simultaneous-similarity orbit census, scheme-theoretic primary decomposition, or classification for fixed matrices with three or more nontrivial Jordan blocks is proved. All geometric statements concern reduced varieties. The finite-field formulas have an elementary proof, but priority among all published and unpublished formulas is not independently established; more general Hall-polynomial or quiver-module enumerations could contain an indirect implication. The bundled computations are finite checks, not independent formal certification.

## References

1. J. R. Britnell and M. Wildon, *On types and classes of commuting matrices over finite fields*, arXiv:1001.0811v1 (public 2010-01-06), subsequently J. London Math. Soc. 83 (2011), 470–492. DOI:10.1112/jlms/jdq088.
2. R. Basili, A. Iarrobino, and L. Khatami, *Commuting nilpotent matrices and Artinian algebras*, J. Commut. Algebra 2 (2010), 295–325. DOI:10.1216/JCA-2010-2-3-295.
3. J. Hua, *Canonical forms for a class of pairs of commuting nilpotent matrices under simultaneous similarity*, arXiv:2305.00176v1 (2023).
4. D. Bogdanić, A. Đurić, S. Koljančić, P. Oblak, and K. Šivic, *Jordan structures of nilpotent matrices in the centralizer of a nilpotent matrix with two Jordan blocks of the same size*, arXiv:2212.08425v1 (2022); Linear Algebra Appl. (2024). This reference concerns the equal-block boundary, not the hook count.
