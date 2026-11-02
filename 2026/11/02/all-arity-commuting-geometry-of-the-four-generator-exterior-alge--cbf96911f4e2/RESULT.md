# All-arity commuting geometry of the four-generator exterior algebra

## Finding

Let \(V\) be a four-dimensional vector space over a field \(k\), and let \(E=\bigwedge_k V\), the sixteen-dimensional unital associative exterior algebra. For every integer \(m\ge 2\), define the **reduced commuting-tuple variety**
\[
\mathcal C_m(E)=\{(x_1,\ldots,x_m)\in E^m:\ x_ix_j=x_jx_i\text{ for all }i,j\}_{\mathrm{red}}.
\]
The following assertions hold.

**Geometry in odd characteristic.** If \(\operatorname{char}k\ne2\), then \(\mathcal C_m(E)\) is geometrically irreducible of dimension \(12m+4\). Its smooth locus is exactly the open subset on which at least one tuple entry has nonzero exterior-degree-one component. Its reduced singular locus is the affine linear subspace where *all* degree-one components vanish. Thus the singular locus has dimension \(12m\), hence constant codimension four, for every \(m\ge2\). The irreducibility and singular-locus statements concern the reduced variety; no reducedness claim for the original equation scheme is made.

**Characteristic two.** If \(\operatorname{char}k=2\), the exterior algebra is commutative, and \(\mathcal C_m(E)=\mathbb A_k^{16m}\) is smooth.

**Exact finite-field census.** For every prime power \(q\) and every integer \(m\ge2\), the number of ordered pairwise commuting \(m\)-tuples is
\[
\boxed{\#\mathcal C_m(E)(\mathbb F_q)=
\begin{cases}
q^{8m}\left[q^{4m}+\dfrac{q^4-1}{q-1}(q^m-1)q^{3m+1}\right],&q\text{ odd},\\[3pt]
q^{16m},&q\text{ even}.
\end{cases}}
\]
This counts actual tuple elements, not simultaneous conjugacy orbits. For odd characteristic, the same stratification yields the Grothendieck-class identity
\[
[\mathcal C_m(E)]=\mathbb L^{8m}\left[\mathbb L^{4m}+
(1+\mathbb L+\mathbb L^2+\mathbb L^3)(\mathbb L^m-1)\mathbb L^{3m+1}\right],
\]
where \(\mathbb L=[\mathbb A^1_k]\). In particular the count is a polynomial in \(q\) on odd prime powers.

**Supplementary adjoint-rank spectrum.** For any odd \(q\), the additive rank of \(\operatorname{ad}_x:y\mapsto xy-yx\) for \(x\in E\) belongs to \(\{0,1,4\}\), with respective multiplicities
\[
q^8,\qquad q^8(q^4-1),\qquad q^{12}(q^4-1).
\]
Hence ranks two and three do not occur. This is included as an internal cross-check and structural refinement of the tuple formula, not as the sole novelty claim. For even \(q\), all commutator ranks are zero.

## Assumptions and scope

The multiplication is exterior multiplication, including \(v\wedge v=0\) for each \(v\in V\) in characteristic two. Choose a nonzero volume element \(\omega\in\bigwedge^4V\). There is a perfect bilinear pairing
\[
\langle\ ,\ \rangle:V\times\bigwedge^3V\longrightarrow k,
\quad v\wedge w=\langle v,w\rangle\omega.
\]
The vector space of even elements of \(E\) has dimension eight, as does the odd part. For each tuple entry write
\[
x_i=c_i+v_i+w_i,
\quad c_i\in E_{\mathrm{even}},\quad v_i\in V,\quad w_i\in\bigwedge^3V.
\]
No characteristic restrictions are imposed except where explicitly stated. Geometric statements are valid after extension to any algebraic closure of \(k\); the counting statement holds over all finite extensions of finite prime fields. The case \(m=1\) is simply affine sixteen-space; \(m=0\) is a point.

## Proof

**1. Exact equations and rank-one projection.** Even elements commute with everything. If \(\operatorname{char}k\ne2\), two odd elements commute precisely when their exterior product is zero. The odd products have homogeneous degrees two and four, so the commuting equations are exactly
\[
 v_i\wedge v_j=0,\qquad
 \langle v_i,w_j\rangle-\langle v_j,w_i\rangle=0
 \quad(1\le i<j\le m).
\tag{1}
\]
The first conditions are the vanishing of every two-by-two minor of the four-by-\(m\) matrix with columns \(v_i\). Over every field, they force matrix rank at most one. Notice that degree-three products with each other vanish because they would have exterior degree six.

**2. Dense stratum, dimension, and point count.** The locus of nonzero rank-one four-by-\(m\) matrices is smooth and geometrically irreducible of dimension \(4+m-1=m+3\). Each such matrix has a presentation \(v_i=t_i v\), with \(v\ne0\), \((t_i)\ne0\), unique up to common rescaling. The second set of equations in (1) becomes
\[
 t_i\langle v,w_j\rangle-t_j\langle v,w_i\rangle=0.
\]
Since \(w\mapsto\langle v,w\rangle\) is surjective, the \(m\) scalars \(\langle v,w_i\rangle\) must lie in the one-dimensional space spanned by \((t_i)\); the remaining three coordinates of each \(w_i\) are free. Consequently the \(w\)-fiber is affine of dimension \(3m+1\), Zariski-locally trivially over the rank-one locus. Including the free even coordinates, the nonzero-rank stratum is smooth, geometrically irreducible, and has dimension
\[
(m+3)+(3m+1)+8m=12m+4.
\]

Every point with all \(v_i=0\) lies in its closure. Indeed, fix arbitrary \(w_1,\ldots,w_m\). If some \(w_i\ne0\), choose \(v\ne0\) for which \(t_i=\langle v,w_i\rangle\) is not identically zero. Then \(v_i(\epsilon)=\epsilon t_i v\), with all \(w_i\) and even components fixed, defines a one-parameter family satisfying (1), of rank one for \(\epsilon\ne0\), specializing to the given zero-rank point. When all \(w_i=0\), choose any nonzero \(v\) and nonzero vector \((t_i)\). Thus the entire reduced commuting variety is irreducible of the asserted dimension.

For \(k=\mathbb F_q\), the zero-rank portion has \(q^{4m}\) possibilities for all \(w_i\). The nonzero rank-one matrix portion has
\[
\#\mathbb P^3(\mathbb F_q)\,(q^m-1)=\frac{q^4-1}{q-1}(q^m-1)
\]
choices, with \(q^{3m+1}\) possible \(w\)-tuples above each. Each admits \(q^{8m}\) even-coordinate choices. This gives the claimed count. Zariski-local triviality gives the stated Grothendieck class by the identical partition into the two strata.

**3. Complete singular locus.** The rank-one stratum is smooth by Step 2. We show that every zero-rank point is singular in the *reduced* variety; this uses actual curves rather than differentiating equations and assuming their ideal is radical. Fix its degree-three coordinates and represent them by an \(m\)-by-four matrix \(S\) via the pairing; put \(r=\operatorname{rank}(S)\). A rank-one deformation with \(v_i(\epsilon)=\epsilon t_i v\) and \(w_i\) fixed gives a genuine curve whenever \((t_i)\) is proportional to \(S v\), or when \(S v=0\) and \((t_i)\) is arbitrary. All such tangent directions therefore belong to the tangent space of the reduced variety.

The linear span of these directions is the full kernel of the linear equations
\[
\langle v_i',w_j\rangle-\langle v_j',w_i\rangle=0.
\tag{2}
\]
To see this, change bases so \(S\) has an \(r\)-by-\(r\) identity block and zeros elsewhere. Vectors \(v\in\ker S\) with arbitrary \((t_i)\) span the \(m(4-r)\) free columns of the direction matrix. The directions \((Sv)\otimes v\), as \(v\) varies, span the \(r\)-by-\(r\) symmetric block by polarization (valid in odd characteristic). The two contributions show that this span has dimension
\[
\tau(r,m)=\frac{r(r+1)}2+m(4-r).
\]
For \(m\ge2\) and \(0\le r\le\min(m,4)\), one always has \(\tau(r,m)>4\): the cases \(r=0,1,2,3,4\) give respectively \(4m,1+3m,3+2m,6+m,10\), where only the admissible cases are used. The \(4m\) variations of the \(w_i\) themselves are independent actual tangent vectors, as all zero-\(v\) points commute. Hence the odd-part tangent space has dimension at least \(4m+\tau(r,m)>4m+4\), the local dimension of the irreducible odd-part variety. The even coordinates add \(8m\) freely. Thus all zero-\(v\) points are singular and there are no other singular points. The zero-\(v\) locus has dimension \(4m+8m=12m\), giving codimension four.

**4. Rank spectrum and the characteristic-two boundary.** The map \(\operatorname{ad}_x\) vanishes on even elements and is twice exterior multiplication by the odd part on odd elements. If \(v\ne0\), the degree-two block \(v\wedge V\) has rank three and an independent degree-four output from \(v\wedge\bigwedge^3 V\) adds one, giving rank four. If \(v=0\) but \(w\ne0\), only \(w\wedge V\) remains and has rank one; if both vanish, the rank is zero. Multiplying the counts of these odd strata by the \(q^8\) free even coordinates yields the three rank multiplicities. Finally, in characteristic two, every exterior monomial commutes with every other, so the complete commuting variety is affine space.

## Verification

A standalone pure-Python checker is supplied as `artifacts/check_exterior4.py`, with its actual output in `artifacts/verification_output.txt`. It constructs the complete sixteen-basis exterior multiplication and tests original commutators, not only the simplified count formula. Over \(\mathbb F_3\), it exhaustively computes the adjoint ranks for all \(3^8=6561\) odd elements and recovers the rank profile \((1,80,6480)\); the induced commuting-pair count agrees with the formula. It independently enumerates all rank-one degree-one matrices and computes the linear equation ranks of their degree-three fibers for \((q,m)=(3,2),(3,3),(3,4),(5,2)\). It separately tests tangent-direction spans in every possible rank class at tuple lengths two, three and four over \(\mathbb F_3\), as well as thousands of direct product samples in characteristics two, three, five and seven and genuine extension-field samples over \(\mathbb F_4\).

The program prints `EXTERIOR4_COMMUTING_GEOMETRY_OK` when these checks pass. Every numerical test is finite; the infinite family of statements relies on the algebraic proof above rather than on exhaustive searches across fields or tuple lengths.

## Relationship to prior work

Domokos and Zubor, *Commutative subalgebras of the Grassmann algebra* (2014), study maximal-dimensional commutative subalgebras and square-zero subspaces of the odd part, with a symplectic interpretation for even generator count. Their foundational exterior-algebra and square-zero facts are used here, not presented as new. Márki, Meyer, Szigeti and van Wyk (2013) study matrix embeddings and polynomial identities of finitely generated Grassmann algebras, rather than finite-field commuting-tuple censuses.

Irreducibility for commuting **pairs** with at most five exterior generators has also been obtained in previous calculations and is **not** claimed as a new isolated result. The distinct claims here are a uniform formula and geometric description for arbitrarily long commuting tuples in the four-generator case, and the exact reduced singular locus of codimension four for all tuple lengths at least two. The same-class literature searched did not supply this combined statement. These comparisons do not establish exhaustive publication priority; an equivalent formulation in other literature may exist.

## Limitations

The result is for the exterior algebra on **exactly four** generators and the **reduced** commuting variety. It does not establish the original commuting equation ideal to be radical, classify all higher-generator exterior commuting varieties, or address automorphism-orbit enumeration. Its characteristic-two conclusion uses the standard alternating definition of exterior algebra. The standalone computations are finite consistency tests, not independent proof of all characteristic and tuple-length cases. No independent mathematical audit has been performed, and historical novelty remains subject to further external scrutiny.

## References

1. M. Domokos and M. Zubor, *Commutative subalgebras of the Grassmann algebra*, arXiv:1403.2916, first submitted March 12, 2014, especially Sections 2, 7 and 8. https://arxiv.org/abs/1403.2916
2. L. Márki, J. Meyer, J. Szigeti and L. van Wyk, *Matrix representations of finitely generated Grassmann algebras and some consequences*, arXiv:1307.0292, first submitted July 1, 2013. https://arxiv.org/abs/1307.0292
