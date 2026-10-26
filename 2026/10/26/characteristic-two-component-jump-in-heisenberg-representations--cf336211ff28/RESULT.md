# Characteristic-two component jump in Heisenberg representations into \(\mathfrak n_4\)

## Finding
Let \(H(k)=\operatorname{Hom}_{\mathrm{Lie}}(\mathfrak h_3(k),\mathfrak n_4(k))\). The underlying reduced affine variety of \(H(k)\), after extension to an algebraic closure of \(k\), has precisely **four irreducible components of dimension \(10\)** in characteristic other than \(2\), and precisely **two irreducible components of dimensions \(10\) and \(11\)** in characteristic \(2\). All are geometrically irreducible and rational.

For every finite field \(\mathbb F_q\), the exact number of marked Lie homomorphisms is
\[
\#H(\mathbb F_q)=\begin{cases}
q^6(q^5+2q^4-2q^3-q^2+q),&\operatorname{char}\mathbb F_q=2,\\
q^6(4q^4-2q^3-3q^2+2q),&\operatorname{char}\mathbb F_q\ne2.
\end{cases}
\]
For \(q=2,3,4,5\), these counts are respectively \(2944,181521,5718016,34140625\).

## Assumptions and scope
Over an arbitrary field \(k\), define the three-dimensional Heisenberg Lie algebra with basis \(x,y,z\), brackets \([x,y]=z\), \([x,z]=[y,z]=0\). Let \(\mathfrak n_4(k)\) denote all strictly upper-triangular \(4\times4\) matrices with the commutator bracket, including characteristic two. Every homomorphism is determined by the ordered matrices \(X=\phi(x)\), \(Y=\phi(y)\), and \(\phi(z)=[X,Y]\). Accordingly, the only remaining identities are \([X,[X,Y]]=0=[Y,[X,Y]]\). Matrices are labelled by their four standard basis vectors; no quotient by conjugation is taken.

Write the first superdiagonal of \(X\) as \((a,b,c)\) and of \(Y\) as \((A,B,C)\), and let the other six coefficients of the pair be free. Define column vectors \(u=(a,A)^T\), \(v=(b,B)^T\), \(w=(c,C)^T\) in \(k^2\), and \(p=\det(u,v)\), \(s=\det(v,w)\), \(\Delta=\det(u,w)\). The base affine space has coordinates \((u,v,w)\in(k^2)^3\), with the six other coordinates contributing an affine \(\mathbb A^6\) factor.

## Proof
**Exact matrix equations.** Direct multiplication gives \([X,Y]_{13}=p\), \([X,Y]_{24}=s\); its \((1,4)\)-entry is central in \(\mathfrak n_4\). The two iterated commutators therefore vanish if and only if
\[
 s u-pw=0\qquad\text{in }k^2.
\]
No equation involves the remaining six matrix entries.

**Characteristic other than two.** If \(\Delta\ne0\), the independent columns \(u,w\) force \(p=s=0\), which forces \(v=0\). If \(\Delta=0\), choose a common direction \(t\) of the nonzero columns \(u,w\), writing \(u=\alpha t\), \(w=\beta t\). Then \(p=\alpha\det(t,v)\), \(s=-\beta\det(t,v)\), and
\[
 su-pw=-2\alpha\beta\det(t,v)t.
\]
The equation is thus equivalent to \(u=0\), or \(w=0\), or \(\det(t,v)=0\), with the last condition equivalent to \(\operatorname{rank}[u\ v\ w]\le1\) when both \(u,w\ne0\). Including the case \(\Delta\ne0\), the reduced solution locus is precisely the union
\[
\{v=0\}\ \cup\ \{u=0\}\ \cup\ \{w=0\}\ \cup\ \{\operatorname{rank}[u\ v\ w]\le1\}.
\]
The first three are distinct affine four-spaces; the last is the irreducible \(2\times3\) rank-at-most-one determinantal variety, also of dimension \(4\). None is contained in another. After the free \(\mathbb A^6\) factor, these give exactly four distinct geometrically irreducible components of dimension \(10\).

**Characteristic two.** When \(\Delta=0\), the same proportional-column calculation gives \(su-pw=0\) automatically because \(2=0\); if one column is zero the identity is immediate as well. When \(\Delta\ne0\), the equation forces \(v=0\). Thus the reduced locus is exactly
\[
 \{\Delta=0\}\ \cup\ \{v=0\}.
\]
The determinantal hypersurface \(\Delta=0\) is irreducible of dimension \(5\); \(v=0\) is an irreducible affine four-space not contained in it. Both varieties remain irreducible after any field extension; they are rational on dense coordinate charts. Multiplying by \(\mathbb A^6\) yields precisely dimensions \(11\) and \(10\).

**Point counts.** The number of \(2\times2\) matrices of rank at most one over \(\mathbb F_q\) equals \(q^3+q^2-q\). In characteristic two the base union therefore has
\[
 q^2(q^3+q^2-q)+q^4-(q^3+q^2-q)=q^5+2q^4-2q^3-q^2+q
\]
points. In odd characteristic the rank-at-most-one \(2\times3\) component has \(q^4+q^3-q\) points; each of the three four-dimensional coordinate components has \(q^4\) points. Every pairwise intersection of the determinantal component with a coordinate component has \(q^3+q^2-q\) points; pairwise intersections of coordinate components each have \(q^2\) points. Triple intersections comprising the determinantal component and two coordinate components each have \(q^2\) points, while the intersection of the three coordinate components and the intersection of all four are singletons. Inclusion–exclusion gives \(4q^4-2q^3-3q^2+2q\). Finally multiply by \(q^6\) for the unconstrained entries.

## Verification
The accompanying standard-library script `verify_heisenberg_n4.py` enumerates every ordered pair of first-superdiagonal triples over \(\mathbb F_2,\mathbb F_3,\mathbb F_4,\mathbb F_5\); it also independently constructs the actual strictly upper-triangular matrices and checks the two nested brackets rather than relying solely on the reduced formulas. Reported base counts are \(46,249,1396,2185\). It verifies the predicted field-size formulas without taking finite checks as a proof of the all-field classification. Reproduce with `python3 verify_heisenberg_n4.py`.

## Relationship to prior work
Crumley (arXiv:1105.4935v1, §§1–2) identifies precisely the three matrix identities \(Z=[X,Y]\), \([X,Z]=[Y,Z]=0\) underlying Heisenberg representations, within a characteristic-restricted theory of representations of unipotent algebraic groups. The present result counts and geometrically decomposes the solutions **specifically inside \(\mathfrak n_4\)**, in particular at characteristic two, outside that work's large-characteristic hypothesis. Ceballos, Núñez and Tenorio (arXiv:1404.3510v1, §§1–3, 5) study minimal faithful triangular representations and provide example representatives rather than a complete rational-point count or reduced-component decomposition of this nonfaithfulness-inclusive homomorphism variety. Relevant finite Lie-algebra enumeration records concern subalgebra commutativity or Nijenhuis maps rather than these nested commutator constraints.

## Limitations
Only the reduced locus and labelled homomorphisms are classified. The defining scheme may have nonreduced structure. The theorem does not count isomorphism classes of representations, conjugation orbits, or arbitrary \(n\times n\) target nilradicals. The component classification is valid over arbitrary fields, but the point formula assumes a finite field. Independent external mathematical validation and absolute historical publication-priority certification have not been performed.

## References
1. M. Crumley, *Generic Representation Theory of the Unipotent Upper Triangular Groups*, arXiv:1105.4935v1 (first public version, 25 May 2011), https://arxiv.org/abs/1105.4935.
2. M. Ceballos, J. Núñez, Á. F. Tenorio, *Minimal Faithful Upper-Triangular Matrix Representations for Solvable Lie Algebras*, arXiv:1404.3510v1 (14 April 2014), https://arxiv.org/abs/1404.3510.
