# Projective multidegree of the Enriques Cremona transformation
## Finding
Let \(f:\mathbf P^5\dashrightarrow\mathbf P^5\) be the Brooke--Marquand Cremona transformation defined by quintics double along their Fano-model Enriques surface. If \(\widetilde P\) is the common resolution, \(H\) is the pullback of a source hyperplane, and \(L\) is the pullback of a target hyperplane, define
\[
d_k=\int_{\widetilde P}H^{5-k}L^k,\qquad 0\le k\le5.
\]
Then the projective multidegree is
\[
(d_0,d_1,d_2,d_3,d_4,d_5)=(1,5,25,25,5,1).
\]
In particular, the two middle projective degrees are both \(25\).

## Assumptions and scope
Work over \(\mathbf C\), with the smooth Fano-model Enriques surface and the common resolution constructed in Corey Brooke and Lisa Marquand, *Birational cubic fourfolds via an Enriques Cremona transformation*, arXiv:2609.10353. Write \(P^-=\operatorname{Bl}_S\mathbf P^5\), let \(H\) be the pullback of the hyperplane class, let \(E\) be the exceptional divisor over \(S\), and put
\[
D=5H-2E.
\]
The cited construction has twenty disjoint residual base planes \(\Pi_i\subset P^-\). Blowing them up gives \(\mu:\widetilde P\to P^-\) with exceptional divisors \(G_i\), and the target hyperplane class is
\[
L=\mu^*D-\sum_{i=1}^{20}G_i.
\]
No assertion is made here about other Cremona transformations or about degenerations of the Enriques surface.

## Proof
The intersection data used below are exactly those appearing in the source calculation of the top self-intersection:
\[
H^5=1,\quad H^4E=H^3E^2=0,\quad H^2E^3=10,\quad HE^4=60,\quad E^5=222.
\]
Expanding \(D=5H-2E\) before resolving the twenty planes gives
\[
b_k:=\int_{P^-}H^{5-k}D^k=(1,5,25,45,-15,21).
\]

Each \(\Pi_i\) is a projective plane. Its hyperplane restriction is \(H|_{\Pi_i}=l\). The plane meets the Enriques surface in the cubic divisor used in the construction, so \(E|_{\Pi_i}=3l\), hence
\[
D|_{\Pi_i}=-l.
\]
The source proves
\[
N_{\Pi_i/P^-}\simeq\mathcal O_{\mathbf P^2}(-1)^{\oplus3}.
\]
For the blowup of a codimension-three center, with \(G=G_i\),
\[
\mu_*(G^3)=[\Pi_i],\qquad
\mu_*(G^4)=c_1(N_{\Pi_i/P^-}),\qquad
\mu_*(G^5)=c_1(N)^2-c_2(N).
\]
Thus on one plane
\[
\int G^5=6,\qquad
\int DG^4=3,\qquad
\int D^2G^3=1,
\]
and also
\[
\int HG^4=-3,\qquad
\int HDG^3=-1,\qquad
\int H^2G^3=1.
\]
Because the twenty centers are disjoint, mixed products involving exceptional divisors over different planes vanish.

Now expand \(L=\mu^*D-\sum_iG_i\). Terms with fewer than three powers of a fixed \(G_i\) push forward to zero. Therefore the corrections to \(b_k\) are zero for \(k\le2\). For \(k=3\), each plane contributes
\[
-\int H^2G^3=-1.
\]
For \(k=4\), each plane contributes
\[
-4\int HDG^3+\int HG^4=4-3=1.
\]
For \(k=5\), each plane contributes
\[
-10\int D^2G^3+5\int DG^4-\int G^5=-10+15-6=-1.
\]
Multiplying by twenty gives the total correction vector
\[
(0,0,0,-20,20,-20).
\]
Adding it to the preliminary vector yields
\[
(1,5,25,45,-15,21)+(0,0,0,-20,20,-20)
=(1,5,25,25,5,1),
\]
as claimed.

## Verification
The standalone script `artifacts/verify_multidegree.py` performs the binomial expansion from the quoted source intersections, applies the codimension-three blowup corrections for all twenty planes, and asserts
\[
(1,5,25,25,5,1).
\]
It also writes the intermediate values \(b_k\) and the correction vector into `artifacts/multidegree_certificate.json`. The endpoint check \(d_5=1\) reproduces the source's birationality intersection calculation, while \(d_1=d_4=5\) agrees with the fact that both the map and its inverse are defined by quintics.

## Relationship to prior work
Brooke--Marquand prove that quintics double along the Enriques surface define a Cremona transformation, describe a factorization through the blowup of twenty disjoint planes, compute the normal bundle of each plane, and verify the top intersection \(L^5=1\). Their paper does not state the full projective multidegree. Its results already force the four endpoint data
\[
d_0=1,\qquad d_1=5,\qquad d_4=5,\qquad d_5=1,
\]
but they do not by themselves state the two interior values \(d_2\) and \(d_3\). The calculation above extracts those values from the same resolution geometry.

Projective degrees are a standard graph invariant of a rational map, and general algorithms for computing them are available in the literature on computational birational geometry. Searches using the aliases *projective degrees*, *multidegree*, *graph multidegree*, the Enriques Cremona terminology, and the exact numerical sequence did not locate this fixed-map computation. This search evidence is not a proof that no unindexed computation exists.

## Limitations
The proof depends on the resolution data established for the Brooke--Marquand Enriques Cremona transformation, especially the twenty disjoint planes and their normal bundle \(\mathcal O_{\mathbf P^2}(-1)^{\oplus3}\). It does not reprove the construction of that resolution. The literature comparison was targeted rather than exhaustive, so an unindexed or unpublished prior computation of the same multidegree remains a residual originality risk.

## References
1. Corey Brooke and Lisa Marquand, *Birational cubic fourfolds via an Enriques Cremona transformation*, arXiv:2609.10353, first public version 2026-09-09.
2. Giovanni Staglianò, *A Macaulay2 package for computations with rational maps*, describing general computation of projective degrees and related invariants of rational maps.
