# Characteristic-two excess derivations and the nonsingular density of graded filiform Lie algebras

## Finding
For each integer \(m\geq3\), consider the naturally graded filiform Lie algebra \(Q_{2m}(k)\) over a field \(k\), with defining brackets given below. Its derivation space has dimension
\[
\dim_k\operatorname{Der}(Q_{2m})=\begin{cases}3m,&\operatorname{char}k\ne2,\\4m-2,&\operatorname{char}k=2.\end{cases}
\]
Thus characteristic two adds exactly \(m-2\) independent derivation directions. This difference already appears in dimension six and grows without bound.

If \(k=\mathbb F_q\) has characteristic \(p\), put \(d=3m\) for odd \(p\), and \(d=4m-2\) for \(p=2\). The number of invertible derivations is exactly
\[
q^{d-2}(q-1)\bigl(q-\min\{p,2m-1\}\bigr).
\]
In particular, no invertible derivation exists over the prime field \(\mathbb F_p\) once \(2m-1\ge p\), but an invertible derivation exists over every proper finite extension \(\mathbb F_{p^r}\) with \(r\ge2\). The latter assertion concerns \(m\ge3\), for which \(2m-1\ge5\); when \(2m-1<p\), invertible derivations exist already over \(\mathbb F_p\).

## Assumptions and scope
Let \(n=2m\ge6\). The vector space has basis \(e_1,\dots,e_n\), with nonzero defining brackets
\[
[e_1,e_i]=e_{i+1}\quad (2\le i\le n-1),\qquad
[e_i,e_{n+1-i}]=(-1)^{i+1}e_n\quad(2\le i\le m).
\]
All other brackets are obtained by skew-symmetry and bilinearity or vanish. In characteristic two the bracket is interpreted as alternating, with \([v,v]=0\), not merely as a skew-symmetric bilinear map. These constants satisfy Jacobi in every characteristic. A derivation is a \(k\)-linear map \(D\) with \(D([u,v])=[D(u),v]+[u,D(v)]\). An invertible derivation is invertible as a linear map, not necessarily as an algebra automorphism.

## Proof
Write
\[
D(e_1)=\sum_{i=1}^n a_i e_i,\qquad D(e_2)=\sum_{i=1}^n b_i e_i.
\]
The relation \([e_2,e_3]=0\), projected to \(e_4\), forces \(b_1=0\), because \(n\ge6\). Each \(D(e_j)\) for \(j\ge3\) is uniquely determined by the recursion
\[
D(e_j)=[D(e_1),e_{j-1}]+[e_1,D(e_{j-1})].
\]
In particular, \(D(e_j)\) lies in the span of \(e_j,\ldots,e_n\) for \(j\ge3\), and its coefficient on \(e_j\) is \((j-2)a_1+b_2\) for \(3\le j\le n-1\). For \(3\le j\le n-2\), the coefficient of \(e_{n-1}\) in \(D(e_j)\) is \(b_{n+1-j}\) whenever that index is in range.

Put \(t=n+1-j\). The coefficient of \(e_n\) in the derivation identity for \([e_2,e_j]=0\) is
\[
\bigl((-1)^{t+1}-1\bigr)b_t=0\quad(3\le t\le n-2).
\]
Hence exactly the even-index constraints \(2b_4=2b_6=\cdots=2b_{n-2}=0\) are imposed. The derivation identities for the two expressions \([e_1,e_{n-1}]=e_n\) and \([e_2,e_{n-1}]=-e_n\) agree precisely when \(a_2=a_1-b_2\). The remaining zero-bracket identities among \(e_i,e_j\) for \(i,j\ge3\) give only equations already implied by these even-index constraints: when \(i+j<n+1\), their coefficient of \(e_n\) is proportional to \(\bigl(1+(-1)^{n+1-i-j}\bigr)b_{n+3-i-j}\), and otherwise they vanish. When \(i+j=n+1\), the two diagonal weights sum to the already determined weight of \(e_n\). No additional restrictions occur. Conversely, these conditions and the recursion verify the derivation identity for every basis pair, proving sufficiency.

There are \(n-1\) free parameters among \((a_1,\ldots,a_n)\), and initially \(n-1\) among \((b_2,\ldots,b_n)\). If \(2\ne0\), the \(m-2\) entries \(b_4,b_6,\ldots,b_{n-2}\) vanish; if \(2=0\), they are all free. This gives \(2n-2-(m-2)=3m\) and \(2n-2=4m-2\), respectively.

In the ordered basis, the derivation matrix is lower triangular. Its diagonal entries are
\[
a_1,\ b_2,\ a_1+b_2,\ 2a_1+b_2,\ldots,\ (n-3)a_1+b_2,\ (n-3)a_1+2b_2.
\]
Therefore
\[
\det D=a_1 b_2\prod_{j=1}^{n-3}(ja_1+b_2)\bigl((n-3)a_1+2b_2\bigr).
\]
The two distinguished parameters \(a_1,b_2\) are independent, and every assignment to them admits exactly \(q^{d-2}\) derivations. Invertibility requires \(a_1\ne0\). With \(z=b_2/a_1\), the forbidden elements of \(\mathbb F_q\) are \(0,-1,\ldots,-(n-3)\), and, for odd \(p\), the additional element \(-(n-3)/2\). For \(p=2\), the final factor is \(a_1\ne0\), so the forbidden set has two elements. For odd \(p\le n-3\), the integer residues \(0,\ldots,n-3\) already exhaust \(\mathbb F_p\). For odd \(p>n-3\), the additional half-integer residue is distinct from them, since \(n-3\) is odd, and gives a total of \(n-1\) distinct forbidden elements. In all cases the number of forbidden slopes is \(\min\{p,n-1\}\). Thus the number of invertible derivations is \(q^{d-2}(q-1)(q-\min\{p,n-1\})\), as claimed.

## Verification
The standalone `check.py` implements the stated bracket constants independently of the parameter recursion, builds the full derivation-condition matrix, and calculates its rank over \(\mathbb F_p\). It checks Jacobi, all derivation identities, and the determinant factorization for the dimensions \(n=6,8,10,12\) and primes \(p=2,3,5,7\). It also enumerates all \(2^{10}=1024\) derivations of \(Q_6(\mathbb F_2)\) and confirms that none is invertible. Run with `python3 check.py`; the final line is `Q_FILIFORM_DERIVATIONS_OK`. Tests of small fields corroborate, but do not prove, the all-dimensional statement; the proof above is symbolic.

## Relationship to prior work
Adimi and Makhlouf's 2012 preprint (Section 4, and its 2013 version) fixes the naturally graded families and studies their coadjoint indices, rather than derivation spaces over arbitrary characteristics. The 2005 work of Cabezas and Pastor places this family in the classification of naturally graded filiform algebras over complex fields. Cagliero and Tirao (2014) study cohomology under a two-dimensional derivation torus; their published abstract does not determine the extra characteristic-two derivation directions. Tsartsaflis (2015) studies characteristic-two Betti numbers for related Vergne-type filiform algebras, not this derivation enumeration. The characteristic-two dimension jump, full finite-field count and comparison across prime-field extensions are the claims being assessed, not the known definition of \(Q_n\) or the mere existence of a derivation torus.

## Limitations
The conclusion concerns the precisely presented natural graded family \(Q_{2m}\), not all filiform deformations. A primary publication on the complex derivation algebra of \(Q_n\) (Wu, 2013) and a closely related full cohomology article (Cagliero–Tirao, 2014) could not both be inspected in full; their available descriptions do not establish characteristic-two coverage, but publication priority cannot be certified from this comparison. There is no independent mathematical audit. The checker verifies the stated finite list of small prime fields, not all extensions or dimensions.

## References
1. H. Adimi and A. Makhlouf, *Index of Graded Filiform and Quasi Filiform Lie Algebras*, arXiv:1212.1650v1 (first posted 2012-12-07), Section 4; Filomat 27 (2013), 467–483. https://arxiv.org/abs/1212.1650
2. J. M. Cabezas and J. R. Pastor, *Naturally graded p-filiform Lie algebras in arbitrary finite dimension*, Journal of Lie Theory (2005). https://jolt.centre-mersenne.org/item/10.5802/jolt.381.pdf
3. L. Cagliero and P. Tirao, *The cohomology of filiform Lie algebras of maximal rank*, Linear Algebra Appl. 455 (2014), 143–167. https://doi.org/10.1016/j.laa.2014.04.031
4. I. Tsartsaflis, *On the Betti numbers of filiform Lie algebras over fields of characteristic two*, arXiv:1511.03132v1 (2015). https://arxiv.org/abs/1511.03132
5. M. Wu, *The derivation algebra of a \(Q_n\) filiform Lie algebra*, 2013 (abstract available). https://www.researchgate.net/publication/268168101_The_derivation_algebra_of_a_Q_n_filiform_Lie_algebra
