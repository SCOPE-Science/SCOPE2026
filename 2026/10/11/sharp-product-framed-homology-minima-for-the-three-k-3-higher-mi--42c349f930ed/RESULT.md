# Sharp product-framed homology minima for the three \(k=3\) higher mixed sums
## Finding
Consider the three \(k=3\) model types \((p,q)=(4,4),(3,3),(6,2)\) in the direct cyclic mixed-sum construction of Akhmedov--Akhmedov, and restrict to equatorially product-framed gluings whose Mayer--Vietoris surface matrix has full row rank. The exact minimum possible orders of integral first homology are respectively
\[
64,\qquad 27,\qquad 24.
\]
Moreover these minima are attained with
\[
H_1\cong (\mathbb Z/4)^3,\qquad (\mathbb Z/3)^3,\qquad \mathbb Z/6\oplus(\mathbb Z/2)^2.
\]
Thus the product-framed Smith problem posed for these three model cases has a sharp answer at the level of the minimum order and an explicit minimizing group in every case.

More generally, for any product-framed type \((p,q;g,h)\) for which the surface matrix
\[
A_S=\begin{pmatrix}Q_{p,g}\\-Q_{q,h}S\end{pmatrix}
\]
has full row rank, one has the stronger universal divisibility
\[
pq\,\gcd(p,q)\mid |H_1(Z;\mathbb Z)|.
\]
The three displayed minima show that this stronger divisor is sharp in all three \(k=3\) model cases.

## Assumptions and scope
The statement uses the explicit cyclic multisections and the adapted integral bases of Akhmedov--Akhmedov. The gluing is equatorially product-framed, so the framing term is zero. The symplectic homology action is an integral matrix \(S\in\operatorname{Sp}(2G,\mathbb Z)\), and the full-row-rank condition is exactly the condition giving finite first homology and the required rational cohomology.

The result does not claim the same minima when a nonzero framing term is allowed. In that setting the meridional row couples to the surface rows and the split presentation used here is unavailable.

## Proof
For a product-framed gluing, the cited Mayer--Vietoris presentation is
\[
H_1(Z;\mathbb Z)\cong \operatorname{coker}A_S\oplus\mathbb Z/d,
\qquad d=\gcd(p,q).
\]
The adapted covering maps satisfy
\[
\operatorname{coker}Q_{p,g}\cong\mathbb Z/p,
\qquad
\operatorname{coker}Q_{q,h}\cong\mathbb Z/q.
\]
There is a natural surjection
\[
\operatorname{coker}A_S\longrightarrow
\operatorname{coker}Q_{p,g}\oplus\operatorname{coker}Q_{q,h},
\qquad [(x,y)]\longmapsto([x],[y]).
\]
It is well defined because every vector in the image of \(A_S\) maps to zero in both factor cokernels, and it is surjective because arbitrary representatives \(x\) and \(y\) may be chosen independently. Therefore, whenever \(\operatorname{coker}A_S\) is finite,
\[
pq\mid |\operatorname{coker}A_S|,
\]
and hence
\[
pq\,d\mid |H_1(Z;\mathbb Z)|.
\]
For the three model cases this gives lower bounds \(64\), \(27\), and \(24\).

It remains to attain the lower bounds. In the interleaved standard symplectic coordinates \((e_0,f_0,e_1,f_1,\ldots)\), let
\[
J=\bigoplus_{i=0}^{G-1}\begin{pmatrix}0&1\\-1&0\end{pmatrix},
\qquad
T_v=I+v(v^\top J).
\]
Each \(T_v\) is integral symplectic. The certificate file lists, for each model case, a short ordered product of such transvections. For those three products, exact maximal-minor calculations give
\[
\gcd\{\text{maximal minors of }A_S\}=16,\qquad9,\qquad12,
\]
respectively. These equal \(pq\). Therefore the natural surjection above is an isomorphism in each case, so the surface cokernels are respectively
\[
(\mathbb Z/4)^2,\qquad(\mathbb Z/3)^2,\qquad\mathbb Z/6\oplus\mathbb Z/2.
\]
Adding the split meridional summand \(\mathbb Z/d\) gives the three claimed first-homology groups and proves sharpness.

Finally, every displayed integral symplectic matrix is realized by a surface diffeomorphism because the mapping class group surjects onto the integral symplectic group; the source uses this same realization step for its gluing theorem. Hence the certificates describe genuine product-framed symplectic gluings, not only abstract matrices.

## Verification
`artifacts/verify_minimal_h1.py` reconstructs the covering matrices directly from the adapted-basis formula, reconstructs the three gluing matrices from the listed symplectic transvections, verifies \(S^\top J S=J\), enumerates every maximal minor using exact integer Bareiss determinants, and computes their greatest common divisor. Its replay output is stored in `artifacts/verification_output.txt` and ends with `VERIFY_OK`.

The finite computation proves the sharp upper bounds for the three explicit gluings. The universal lower bound is symbolic and does not depend on finite enumeration.

## Relationship to prior work
Akhmedov--Akhmedov prove the product-framed split Mayer--Vietoris formula, the adapted-basis description with \(\operatorname{coker}Q_{p,g}\cong\mathbb Z/p\), and the existence of full-rank gluings. They state only the weaker universal divisibility by \(\operatorname{lcm}(p,q)\), and explicitly ask for the minimal possible orders in the three \(k=3\) model cases. The present result uses their presentation to obtain the stronger product-framed lower divisor and supplies explicit symplectic matrices whose determinantal divisors attain it.

The earlier \(k=1\) paper treats square Mayer--Vietoris matrices and transvection families for the rational-cohomology \(S^2\times S^2\) cases. It does not contain the rectangular \(k=3\) Smith calculations or the three minima above.

## Limitations
The exact minima are proved only within the equatorially product-framed family. A nonzero framing term changes the integral presentation and could in principle lower the order; no statement about the global minimum over all normal framings is made. The result also does not classify every finite abelian group occurring for the three model types, and it does not address the two remaining \(k=3\) numerical types.

The certificates depend on the adapted covering-basis convention stated in the source and repeated in the verifier. No claim is made about uniqueness of minimizing gluing matrices or diffeomorphism types.

## References
1. A. Akhmedov and A. Akhmedov, *Higher Braided Mixed Sums, Intersection Lattices, and Symplectic Four-Manifolds*, arXiv:2610.03756v1, first public 2026-09-26.
2. A. Akhmedov, *Braided Multisections and Symplectic Four-Manifolds with the Rational Cohomology of \(S^2\times S^2\)*, arXiv:2609.11727v1, first public 2026-09-10.
3. B. Farb and D. Margalit, *A Primer on Mapping Class Groups*, Princeton University Press, 2012, for the standard symplectic representation of the mapping class group.
