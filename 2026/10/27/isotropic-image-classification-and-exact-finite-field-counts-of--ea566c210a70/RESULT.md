# Isotropic-image classification and exact finite-field counts of Heisenberg Nijenhuis operators

## Finding
Let \(k\) be any field, let \((V,\omega)\) be a \(2n\)-dimensional symplectic vector space for \(n\geq1\), and let \(\mathfrak h=V\oplus kz\) be its Heisenberg Lie algebra, with \([v,w]=\omega(v,w)z\) and \([z,\mathfrak h]=0\). A \(k\)-linear map \(N:\mathfrak h\to\mathfrak h\) is a Nijenhuis operator if and only if it has the unique form
\[
N(v+tz)=(cI_V+B)v+(\ell(v)+ct)z,
\qquad c\in k,\quad \ell\in V^*,\quad \omega(Bv,Bw)=0\ \text{for all }v,w\in V.
\]
In other words, the image of \(B\) is totally isotropic. In particular \(0\leq r=\operatorname{rank}B\leq n\), and every such rank occurs.

Over \(k=\mathbb F_q\), put
\[
I_{n,r}(q)=\prod_{j=0}^{r-1}\frac{q^{2n-j}-q^j}{q^r-q^j},\qquad
S_{n,r}(q)=\prod_{j=0}^{r-1}(q^{2n}-q^j),
\]
with both empty products equal to one. For \(0\leq r\leq n\), the exact joint census of the rank of \(B\) and the **centered operator rank** \(d=\operatorname{rank}(N-cI_{\mathfrak h})\) is
\[
\#\{N:\operatorname{rank}B=r,\ d=r\}
=q I_{n,r}(q)S_{n,r}(q)q^r,
\]
\[
\#\{N:\operatorname{rank}B=r,\ d=r+1\}
=q I_{n,r}(q)S_{n,r}(q)(q^{2n}-q^r),
\]
with all other pairs impossible. Consequently the total number is
\[
\boxed{\mathcal N_n(q)=q^{2n+1}\sum_{r=0}^{n}I_{n,r}(q)S_{n,r}(q).}
\]
The scalar \(c\) is intrinsic: it is the action of \(N\) on the central line. Moreover, \(c\) is an eigenvalue of \(N\) with algebraic multiplicity at least \(n+1\). Thus no such operator is regular semisimple.

For example, \(\mathcal N_1(q)=q^6+q^5-q^4\), and \(\mathcal N_2(2)=108032\).

## Assumptions and scope
The form \(\omega\) is alternating and nondegenerate, including in characteristic two. The bracket is the ordinary binary Lie bracket, and the Nijenhuis identity is
\[
[Nx,Ny]=N([Nx,y]+[x,Ny]-N[x,y])\qquad\text{for all }x,y\in\mathfrak h.
\]
The structural classification holds over arbitrary fields; the displayed numerical formulas hold for every prime power \(q\). It concerns all linear operators, not merely invertible operators, derivations, automorphisms, or diagonalizable maps. The convention \(n\geq1\) excludes the abelian zero-symplectic-space case.

## Proof
Write an arbitrary linear map, using \(\mathfrak h=V\oplus kz\), in block form
\[
N(v+tz)=Av+tu+(\ell(v)+ct)z,
\quad A\in\operatorname{End}(V),\ u\in V,\ \ell\in V^*,\ c\in k.
\]
Fix \(v\in V\). The vector component of the Nijenhuis equation for \((v,z)\) is \(\omega(v,u)u=0\), since \([Nv,Nz]\) is central and \([v,Nz]=\omega(v,u)z\). If \(u\ne0\), nondegeneracy supplies \(v\) with \(\omega(v,u)\ne0\), a contradiction. Hence \(u=0\). This reasoning uses no division by two.

Now \(N(z)=cz\). On \((v,w)\), the central component of the Nijenhuis torsion equals
\[
\omega(Av,Aw)-c\omega(Av,w)-c\omega(v,Aw)+c^2\omega(v,w)
=\omega((A-cI_V)v,(A-cI_V)w).
\]
All other components vanish, and the remaining basis-pair torsions involving \(z\) already vanish. Thus the identity for every pair holds exactly when \(B=A-cI_V\) has totally isotropic image. Since a totally isotropic subspace of a nondegenerate \(2n\)-dimensional symplectic space has dimension at most \(n\), the rank bound follows. For every \(r\leq n\), choose an isotropic \(r\)-space and a surjection onto it to realize the rank.

To count over \(\mathbb F_q\), an ordered isotropic independent \(r\)-frame \((v_1,\ldots,v_r)\) has
\[
\prod_{j=0}^{r-1}(q^{2n-j}-q^j)
\]
choices: after \(j\) isotropic independent vectors, the next vector must lie in their perpendicular space of dimension \(2n-j\), but outside their \(j\)-dimensional span. Dividing by the number \(\prod_{j=0}^{r-1}(q^r-q^j)\) of ordered bases of a fixed \(r\)-space gives \(I_{n,r}(q)\) isotropic image spaces. For each such image \(W\), the number of rank-\(r\) maps \(V\twoheadrightarrow W\) is \(S_{n,r}(q)\), the number of full-row-rank \(r\)-by-\(2n\) matrices.

For fixed \(B\) of rank \(r\), the centered endomorphism sends \(v+tz\mapsto Bv+\ell(v)z\). Its rank is \(r\) precisely when \(\ell\) lies in the \(r\)-dimensional row space of \(B\), giving \(q^r\) choices; otherwise it is \(r+1\), giving \(q^{2n}-q^r\) choices. The independent scalar \(c\) contributes a factor of \(q\). This proves the joint census and its sum.

Finally, since \(\operatorname{rank}B\leq n\), the eigenvalue zero of \(B\), over an algebraic closure, has algebraic multiplicity at least \(2n-r\geq n\). The block-triangular operator \(N\) has the additional eigenvalue \(c\) on \(kz\), hence the asserted multiplicity of \(c\).

## Verification
The standalone pure-Python file `checker.py` checks the full Nijenhuis identity directly on a basis without relying on the derived isotropic criterion. It exhausts all \(2^9\) and \(3^9\) endomorphisms of the three-dimensional Heisenberg algebra, agreeing with both the criterion and the centered-rank counts: respectively \(80\) and \(891\) Nijenhuis operators. It also exhausts all \(2^{16}\) candidate matrices \(B\) for the five-dimensional binary case, obtaining isotropic-image rank counts \((1,225,3150)\), and performs independent randomized direct torsion checks on five-dimensional operators over prime fields of orders two, three and five. The deterministic certificate ends with `HEISENBERG_NIJENHUIS_OK`.

The symbolic proof, not the finite tests, establishes the result uniformly in \(n\) and \(q\).

## Relationship to prior work
Liu, Sheng, Zhou and Bai (2016, arXiv:1601.02356v1, Definition 3.4 and its binary-Lie specialization) give the general Nijenhuis identity and deformation-theoretic context, but not a Heisenberg-specific isotropic-image equivalence or finite-field census. Zhikhareva (2024, arXiv:2410.10536v1, Sections 2–6) classifies three-dimensional Lie algebras admitting *regular semisimple* Nijenhuis operators; in particular her nilpotent obstruction is consistent with the repeated-eigenvalue consequence here. That result does not classify arbitrary nonsemisimple Nijenhuis operators on Heisenberg algebras or count their rank strata over finite fields. The isotropic-subspace and surjection factors separately are classical finite symplectic linear algebra; the Nijenhuis parametrization is what connects them.

## Limitations
The formulas are for labeled linear endomorphisms, not for conjugacy classes under automorphisms of \(\mathfrak h\). No group-scheme or scheme-theoretic singularity assertions are made. Computations directly exhaust only the small fields/dimensions stated above. The literature search and source inspections do not establish absolute publication priority; unindexed classifications or unpublished material could contain equivalent formulas.

## References
1. J. Liu, Y. Sheng, Y. Zhou and C. Bai, *Nijenhuis operators on n-Lie algebras*, arXiv:1601.02356v1, publicly posted 2016-01-11; 2000 MSC 17B99 and 13D10. https://arxiv.org/abs/1601.02356
2. E. S. Zhikhareva, *Three-dimensional Lie algebras admitting regular semisimple algebraic Nijenhuis operators*, arXiv:2410.10536v1, 2024-10-14. https://arxiv.org/abs/2410.10536
