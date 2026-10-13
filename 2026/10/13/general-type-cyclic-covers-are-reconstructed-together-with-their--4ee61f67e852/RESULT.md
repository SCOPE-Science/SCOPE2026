# General-type cyclic covers are reconstructed together with their branch divisors
## Finding
Fix integers \(n\ge 1\), \(r\ge 2\), and \(m\ge 2\) with
\[
(r-1)m>n+1,
\qquad
\gcd(rm,n+1+m)=1.
\]
Let \(F,G\in\mathbf C[x_0,\ldots,x_n]\) be homogeneous of degree \(rm\), with smooth projective zero loci, and define
\[
X_F=\{z^r-F(x)=0\},\qquad X_G=\{z^r-G(x)=0\}
\]
inside \(\mathbf P(1^{n+1},m)\). If there is a dg Morita equivalence
\[
\operatorname{MF}^{\mathrm{gr},\mathrm{dg}}(z^r-F)
\simeq_{\mathrm{Mor}}
\operatorname{MF}^{\mathrm{gr},\mathrm{dg}}(z^r-G),
\]
then there are \(L\in\operatorname{GL}_{n+1}(\mathbf C)\) and \(a\in\mathbf C^*\) such that
\[
G(Lx)=a^rF(x).
\]
Thus the full graded matrix-factorization category determines not only the weighted hypersurface but also its cyclic-cover presentation: the branch divisors are projectively linearly equivalent, and the covers are isomorphic over the corresponding projective automorphism of \(\mathbf P^n\).

## Assumptions and scope
The ground field is \(\mathbf C\). The weight of each \(x_i\) is \(1\), the weight of \(z\) is \(m\), and the weighted degree is \(d=rm\). The sum of the ambient weights is
\[
W=n+1+m.
\]
The inequality \((r-1)m>n+1\) is exactly \(d>W\), so these weighted hypersurfaces are of general type. The coprimality assumption is exactly the numerical hypothesis \(\gcd(d,W)=1\) in the weighted general-type reconstruction theorem of Lin--Zeng--Zhang.

Smoothness of \(V(F)\subset\mathbf P^n\) implies quasismoothness of \(z^r-F\): a nonzero critical point of its affine cone would satisfy \(z=0\), \(F=0\), and all first derivatives of \(F\) equal to zero, contradicting smoothness of the branch hypersurface. The same holds for \(G\). Since \(r,m\ge2\), neither equation is a linear cone.

## Proof
Theorem 1.7 of Lin--Zeng--Zhang applies to the two quasismooth weighted hypersurfaces because \(d>W\), \(\gcd(d,W)=1\), and neither equation is a linear cone. The assumed Morita equivalence therefore yields a weight-preserving polynomial automorphism \(\phi\) and a scalar \(c\in\mathbf C^*\) such that, after choosing the orientation of the equivalence,
\[
\phi\bigl(z^r-G(x)\bigr)=c\bigl(z^r-F(x)\bigr).
\]

Because \(m\ge2\), degree-one variables cannot involve \(z\). Hence every weight-preserving polynomial automorphism has the form
\[
x\longmapsto Lx,
\qquad
z\longmapsto az+h_m(x),
\]
where \(L\in\operatorname{GL}_{n+1}(\mathbf C)\), \(a\in\mathbf C^*\), and \(h_m\) is homogeneous of ordinary degree \(m\). Substitution gives
\[
(az+h_m(x))^r-G(Lx)=c\bigl(z^r-F(x)\bigr).
\]
The coefficient of \(z^r\) gives \(c=a^r\). The coefficient of \(z^{r-1}\) is
\[
r a^{r-1}h_m(x).
\]
The right-hand side has no \(z^{r-1}\)-term. Since the characteristic is zero and \(a\ne0\), one gets \(h_m=0\). The constant term in \(z\) is therefore
\[
-G(Lx)=-a^rF(x),
\]
which proves \(G(Lx)=a^rF(x)\).

Consequently \([L]\in\operatorname{PGL}_{n+1}(\mathbf C)\) carries \(V(F)\) to \(V(G)\). The weighted-projective map \([x:z]\mapsto[Lx:az]\) identifies the two cyclic covers and commutes with their projections to \(\mathbf P^n\) after applying \([L]\) on the base.

## Verification
The critical hypothesis check is exact: \(d=rm\), \(W=n+1+m\), and \(d-W=(r-1)m-(n+1)>0\). The only additional algebra beyond Theorem 1.7 is the classification of graded automorphisms in weights \((1^{n+1},m)\) and the binomial coefficient comparison above.

The source itself performs the analogous coefficient comparison for its Fano double-cover Corollary 1.5. In the general-type portion of the paper, Theorem 1.7 supplies the weighted reconstruction statement, but no cyclic-cover corollary is stated. The argument here checks that the reconstructed weighted hypersurface automatically retains the cyclic-cover structure for every \(r\ge2\) under the stated arithmetic hypotheses.

No finite experiment is used as evidence for the universal statement.

## Relationship to prior work
Lin--Zeng--Zhang prove the weighted general-type reconstruction theorem for full graded matrix-factorization categories. Their paper separately gives a branch-divisor reconstruction corollary only for Fano double covers of \(\mathbf P^n\), where the same kind of coefficient comparison is carried out for \(r=2\).

Dell--Jacovskis--Rota study cyclic covers categorically through equivariant Kuznetsov components and prove Torelli statements for specific prime Fano threefolds. Their full text explicitly places those Torelli applications in the Fano setting and does not give the general-type full-matrix-factorization statement above. Lin's earlier 2026 Hochschild--Serre reconstruction result treats the weighted Fano Kuznetsov-component case; Lin--Zeng--Zhang explicitly identify the general-type theorem as new.

Targeted searches for general-type cyclic covers, graded matrix factorizations, branch-divisor reconstruction, and the equation \(z^r-F\) found no prior statement implying this all-\(r\) general-type branch-recovery result. Published-finding searches likewise found no equivalent claim.

## Limitations
The result requires the explicit coprimality condition \(\gcd(rm,n+1+m)=1\), the general-type inequality \((r-1)m>n+1\), and \(m\ge2\). It uses the full graded dg matrix-factorization category, not merely the ordinary derived category of the cover. No claim is made that these numerical hypotheses are necessary for categorical reconstruction. Because the initiating theorem is very recent, an equivalent specialization could exist in material not yet indexed by the searches used here.

## References
1. Xun Lin, Jieheng Zeng, Shizhuo Zhang, *Categorical Torelli theorem for (weighted) hypersurfaces via singularity category*, arXiv:2610.00130v1, 9 September 2026.
2. Hannah Dell, Augustinas Jacovskis, Franco Rota, *Cyclic covers: Hodge theory and categorical Torelli theorems*, arXiv:2310.13651v2; International Mathematics Research Notices 2025, rnaf120.
3. Xun Lin, *Group action of Hochschild-Serre algebra and categorical reconstruction*, arXiv:2609.07562v1, 7 September 2026.
