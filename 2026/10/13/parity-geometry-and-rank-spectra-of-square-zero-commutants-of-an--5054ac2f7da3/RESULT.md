# Parity geometry and rank spectra of square-zero commutants of an almost-regular nilpotent

## Finding
Let \(K\) be any field, let \(n\ge 2\), and let \(B=J_n(0)\oplus J_1(0)\) act on an \((n+1)\)-dimensional \(K\)-space. Define the square-zero commutant
\[
\mathcal Z_n(K)=\{X\in M_{n+1}(K):XB=BX,\ X^2=0\}.
\]
Write \(k=\lfloor n/2\rfloor\). The underlying reduced affine variety of this commutant is, for all characteristics,
\[
\mathcal Z_{2k}^{\mathrm{red}}\cong\mathbb A^k\times\{(b,c):bc=0\},\qquad
\mathcal Z_{2k+1}^{\mathrm{red}}\cong\mathbb A^k\times\{(u,b,c):u^2+bc=0\}.
\]
Consequently, for \(n\) even the locus consists of two irreducible affine \((k+1)\)-spaces meeting along an affine \(k\)-space. For \(n\) odd it is irreducible of dimension \(k+2\), with an affine \(k\)-dimensional singular locus; its transverse variety is an affine quadratic cone. These statements concern reduced varieties, not the possibly nonreduced equation schemes.

For every prime power \(q\) (including powers of two), the complete matrix-rank enumerator for \(K=\mathbb F_q\) is
\[
H_{n,q}(T):=\sum_{X\in\mathcal Z_n(\mathbb F_q)}T^{\operatorname{rank}X}
=1+2(q-1)T+(2q-1)(q-1)\sum_{r=1}^{k}q^{r-1}T^r
+\mathbf 1_{\{n\text{ odd}\}}(q-1)^2q^kT^{k+1}.
\]
In particular,
\[
|\mathcal Z_{2k}(\mathbb F_q)|=(2q-1)q^k,\qquad
|\mathcal Z_{2k+1}(\mathbb F_q)|=q^{k+2}.
\]
Thus the rank support is exactly \(0,1,\ldots,k\) for even \(n\) and \(0,1,\ldots,k+1\) for odd \(n\). In the odd case the singular quadratic cone has the same finite-field point count as an affine plane for every finite extension, despite not being an affine plane.

## Assumptions and scope
The block \(J_n(0)\) is the nilpotent Jordan block with one chain of length \(n\), and \(J_1(0)=0\). The zero matrix is included in the rank enumerator. The rank is ordinary \(K\)-linear rank on the full \((n+1)\)-dimensional module. All formulas hold uniformly for every prime power; no characteristic restriction, algebraic closure, or divisibility assumption is imposed. The geometric isomorphisms hold over any field after passing to the underlying reduced affine varieties.

## Proof
Regard the underlying module as \(M=R\oplus K\) over \(K[t]\), where \(R=K[t]/(t^n)\) and \(t\) acts as \(B\). Write \(\overline v\) for the image of \(v\in R\) in \(R/tR=K\). Every endomorphism commuting with \(B\) has a unique expression
\[
X(v,w)=(a(t)v+bwt^{n-1},\ c\overline v+dw),
\quad a(t)\in R,\ b,c,d\in K.
\]
This follows because \(\operatorname{Hom}_{K[t]}(K,R)=Kt^{n-1}\), \(\operatorname{Hom}_{K[t]}(R,K)=K\), and \(\operatorname{End}_{K[t]}(R)=R\).

Direct composition gives the four equations
\[
a(t)^2+bc\,t^{n-1}=0,\quad b(a(0)+d)=0,\quad c(a(0)+d)=0,\quad d^2=0.
\]
Since \(K\) is a field, the last equation gives \(d=0\); the constant coefficient of the first gives \(a(0)=0\). The middle two are then automatic. Hence the only remaining equation is
\[
a(t)^2+bc\,t^{n-1}=0,\qquad a(t)\in tR.
\]

If \(a(t)\ne0\), let \(s\) be its \(t\)-adic order. Its square has lowest nonzero term in degree \(2s\), with coefficient the square of the nonzero leading coefficient. Hence no solution has \(2s<n-1\). For \(n=2k\), the equation is equivalent to \(a(t)\in t^kR\) and \(bc=0\). The \(k\) coefficients of \(a(t)\) from degrees \(k\) through \(2k-1\) are free. This gives the first affine-variety decomposition.

For \(n=2k+1\), the equation is equivalent to \(a(t)\in t^kR\) and \(a_k^2+bc=0\), where \(a_k\) is the coefficient of \(t^k\). The remaining \(k\) coefficients, in degrees \(k+1\) through \(2k\), are free, giving the second decomposition. The polynomial \(u^2+bc\) is irreducible over every field: treated as a polynomial of degree one in \(b\), its two coefficients \(c\) and \(u^2\) are relatively prime in \(K[u,c]\). The cone is singular precisely at \((u,b,c)=(0,0,0)\). For even \(n\), the equation \(bc=0\) is a union of two coordinate hyperplanes. These facts prove the assertions about reduced geometry, including in characteristic two.

For the rank count, if \(a(t)\ne0\) has order \(s\) and \(bc=0\), then \(\operatorname{rank}X=n-s\): if \(c=0\) the image lies in \(aR\oplus0\), and the extra \(b\)-column already lies in \(aR\); if \(c\ne0\), then \(b=0\), the image of \((1,0)\) contributes one dimension outside \(R\oplus0\), and \(a(t)tR\) contributes \(n-s-1\) more. In the exceptional odd-dimensional branch \(a_k\ne0\) and \(bc=-a_k^2\), both \(b,c\) are nonzero, but the additional \(b\)-column lies in \(a(t)tR\), so the same rank formula holds. If \(a=0\), the equation gives \(bc=0\); the rank is zero for \(b=c=0\) and one in the remaining \(2(q-1)\) cases.

For each \(r=1,\ldots,k\), a nonzero \(a\) of order \(s=n-r\) has exactly \((q-1)q^{r-1}\) choices, and \(bc=0\) has \(2q-1\) choices. When \(n=2k+1\), the additional order-\(k\) branch has \((q-1)q^k\) choices for \(a\), \(q-1\) choices for \(b\ne0\), and then one forced value \(c=-a_k^2/b\); its rank is \(k+1\). This proves the stated enumerator. Its sum at \(T=1\) is \((2q-1)q^k\) in even dimension and \(q^{k+2}\) in odd dimension; alternatively, the odd quadratic cone has exactly \((2q-1)+(q-1)^2=q^2\) rational points.

## Verification
The accompanying standalone `verify.py` performs matrix multiplication, Gaussian elimination, and direct enumeration without using the stated valuation argument. It exhausts the endomorphisms commuting with \(B\) through their explicit parameter basis over \(\mathbb F_2,\mathbb F_3,\mathbb F_4,\mathbb F_5\) for the dimensions listed in `VERIFICATION.md`. In three small cases it additionally exhausts all ambient square matrices and checks the centralizer dimension independently. The computations check examples and finite instances; the proof above establishes the infinite families.

For example, over \(\mathbb F_2\),
\[
H_{3,2}(T)=1+5T+2T^2,\qquad H_{4,2}(T)=1+5T+6T^2,
\]
while over \(\mathbb F_3\),
\[
H_{3,3}(T)=1+14T+12T^2,\qquad H_{4,3}(T)=1+14T+30T^2.
\]

## Relationship to prior work
Britnell and Wildon [1, Proposition 4.4] give a Jordan-partition feasibility classification for nilpotent matrices commuting with a fixed matrix of Jordan type \((n-1,1)\). Their proof explicitly describes the centralizer algebra. Oblak [2, Section 3] studies the nilpotent centralizer of matrices with two Jordan blocks and identifies permitted Jordan shapes and maximal-orbit behavior. These already establish important support and feasibility information; no claim is made to rediscover the centralizer parametrization or mere feasibility of individual ranks. The present calculation imposes the square-zero equation, determines the reduced geometric type of that cut, and computes all finite-field multiplicities of its matrix-rank strata. Its difference from general nilpotent-centralizer irreducibility is significant: the square-zero subvariety is reducible for even \(n\).

## Limitations
This is a statement about one fixed Jordan partition \((n,1)\), not arbitrary nilpotent centralizers, and it counts matrices rather than simultaneous similarity orbits. The geometric claim concerns the reduced variety; no assertion is made about the scheme structure of its original quadratic equations. The literature comparison does not constitute a proof that no equivalent formula occurs in uncatalogued or uninspected work. Independent external validation has not been performed.

## References
[1] J. R. Britnell and M. Wildon, *On types and classes of commuting matrices over finite fields*, arXiv:1001.0811v1 (first public 2010-01-06), Section 4, especially Proposition 4.4. https://arxiv.org/abs/1001.0811

[2] P. Oblak, *On the nilpotent commutator of a nilpotent matrix*, arXiv:1106.1545v1 (first public 2011-06-08), Section 3. https://arxiv.org/abs/1106.1545
