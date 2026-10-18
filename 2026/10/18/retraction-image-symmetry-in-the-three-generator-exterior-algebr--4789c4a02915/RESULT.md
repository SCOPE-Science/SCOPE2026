# Retraction-image symmetry in the three-generator exterior algebra over odd finite fields

## Finding

Let \(q\) be an odd prime power, \(V=\mathbb F_q^3\), and \(E=\bigwedge_{\mathbb F_q}V\), an eight-dimensional unital algebra. A **retraction** is a unital \(\mathbb F_q\)-algebra endomorphism \(e:E\to E\) with \(e^2=e\). Put \(J=\bigoplus_{j=1}^3\bigwedge^jV\), and define the **tangent rank** \(r(e)=\operatorname{rank}(\overline e:J/J^2\to J/J^2)\). The rank is in \(\{0,1,2,3\}\), and the vector-space dimension of \(e(E)\) is exactly \(2^{r(e)}\).

Write \(S_q=q^2+q+1\), let \(I_r(q)\) be the number of *distinct image subalgebras* of tangent rank \(r\), let \(F_r(q)\) be the number of retractions onto any one such image, and let \(T_r(q)\) be the number of retractions of tangent rank \(r\). Then all images of a given rank have the same fiber multiplicity, and

\[
\begin{array}{c|c|c|c}
r&I_r(q)&F_r(q)&T_r(q)\\\hline
0&1&1&1\\
1&S_q\,q^3&q^2&S_q\,q^5\\
2&S_q\,q^3&q^3&S_q\,q^6\\
3&1&1&1.
\end{array}
\]

Thus ranks one and two have **equally many distinct images**, although rank-two images admit \(q\) times as many retractions apiece. In particular, the total number of retractions and images are, respectively,

\[
2+S_q(q^5+q^6),\qquad 2+2S_q\,q^3.
\]

## Assumptions and scope

The field may be any finite extension of an odd prime field, without a restriction on \(q\bmod 4\) or \(q\bmod 3\). Endomorphisms are unital algebra homomorphisms, not necessarily parity-preserving. The image is counted as an *actual embedded subalgebra*, not merely an isomorphism type. Tangent rank uses the unique nilpotent maximal ideal \(J\), so is intrinsic. The characteristic-two case is not included.

## Proof

**Step 1 (tangent linearization).** Fix a basis \(x,y,z\) of \(V\), with \(w=xyz\). Every unital endomorphism preserves \(J\), and its tangent matrix \(U\) satisfies \(U^2=U\) when the endomorphism is idempotent. Conjugation by an invertible linear change of the three generators is an algebra automorphism and sends any rank-\(r\) idempotent \(U\) to the standard projection \(P_r\). The number of rank-\(r\) linear projections is \({3\brack r}_q q^{r(3-r)}\), because one chooses an \(r\)-plane and an ordered complementary \((3-r)\)-plane.

**Step 2 (normal forms).** For \(U=P_r\), write each generator image as its prescribed linear component plus a degree-two term and a scalar multiple of \(w\). In odd characteristic, the equations \(e(x_i)^2=0\) and \(e(x_i)e(x_j)+e(x_j)e(x_i)=0\) are equivalent to vanishing of the degree-three coefficients \(u_i\wedge v_j+u_j\wedge v_i\), where \(u_i\) and \(v_i\) are its degree-one and degree-two components. The equations \(e^2(x_i)=e(x_i)\) then give the following **complete** normal forms (all displayed parameters independently range over \(\mathbb F_q\)):

For \(r=0\), the generator images are zero. For \(r=3\), the endomorphism is the identity (an idempotent automorphism is the identity). For \(r=1\),

\[
e(x)=x+a\,xy+b\,xz+s\,w,\qquad e(y)=e(z)=0.
\]

For \(r=2\),

\[
e(x)=x+b\,xz+s\,w,\qquad
 e(y)=y+b\,yz+t\,w,\qquad
 e(z)=d\,xy.
\]

For clarity, in the rank-two case the exterior relations first force the degree-two parts to be \(a\,xy+b\,xz\), \(c\,xy+b\,yz\), and \(d\,xy\). Comparing degree-two components of \(e^2=e\) gives \(a=c=0\). Then \(e(xy)=xy\), \(e(xz)=e(yz)=e(w)=0\), and comparison of degree-three parts forces the \(w\)-coefficient of \(e(z)\) to vanish; there are no restrictions on \(b,s,t,d\). For rank one the analogous relations force the second and third generator images to vanish, leaving \(a,b,s\). All reverse substitutions satisfy the defining relations and idempotence. Thus the numbers of lifts above a fixed tangent projection are exactly \(1,q^3,q^4,1\) for ranks \(0,1,2,3\).

Since \({3\brack1}_q={3\brack2}_q=S_q\), Step 1 yields

\[
(T_0,T_1,T_2,T_3)=(1,S_q\,q^5,S_q\,q^6,1).
\]

The normal forms show that the image dimensions are \(1,2,4,8\), respectively.

**Step 3 (rank-one images).** Fix the tangent image line \(\langle x\rangle\). Each possible rank-one image is \(\mathbb F_q1+\mathbb F_q a\), where the unique generator with linear component \(x\) has the form

\[
a=x+\alpha\,xy+\beta\,xz+s\,w.
\]

Its square vanishes, and distinct triples \((\alpha,\beta,s)\) give distinct embedded image algebras. These algebras are retraction images: send \(x\) to \(a\) and \(y,z\) to zero. Hence there are \(q^3\) images for each of the \(S_q\) tangent lines. To count retractions onto the specified canonical image \(\mathbb F_q1+\mathbb F_q x\), one must send each generator to a scalar multiple of \(x\), with the coefficient on \(x\) equal to one; the two other scalars are arbitrary. This gives \(q^2\) retractions. Every rank-one image is conjugate to the canonical one under an algebra automorphism. Indeed, for \(a=x+\alpha xy+\beta xz+s w\), the other generator images \(y+\beta yz\) and \(z-\alpha yz\) anticommute with \(a\) and with one another and all have square zero. Together they have identity tangent matrix, and therefore define an automorphism. Thus the same fiber count holds for all such images.

**Step 4 (rank-two images).** Fix tangent image plane \(\langle x,y\rangle\). Any pair of algebra generators with linear parts exactly \(x,y\) for an embedded rank-two image must have the form

\[
A=x+\alpha\,xy+\beta\,xz+s\,w,\qquad
B=y+\gamma\,xy+\beta\,yz+t\,w.
\]

Conversely every such pair has \(A^2=B^2=AB+BA=0\) and \(AB=xy\). There are \(q^5\) allowed ordered pairs. Two pairs determine the same image algebra exactly when one changes \(A\) and \(B\) independently by scalar multiples of \(AB=xy\); this is a free \(q^2\)-element ambiguity. Hence there are \(q^3\) distinct images per tangent plane. Such pairs are extendable to an algebra automorphism, for example by sending the third original generator to

\[
C=z+\gamma\,xz-\alpha\,yz.
\]

The three images \(A,B,C\) satisfy the exterior relations and have invertible linear part, so this map is an automorphism of \(E\). Consequently every rank-two image is conjugate to the canonical subalgebra \(\bigwedge\langle x,y\rangle\). A retraction onto the canonical subalgebra fixes \(x,y\) and sends \(z\) to an arbitrary \(u x+v y+d\,xy\), giving precisely \(q^3\) maps. The exterior relations and idempotence hold for all three parameters. There are \(S_q\) tangent planes, establishing the rank-two row and its uniform fiber count.

Ranks zero and three have uniquely the augmentation map and identity map, respectively. This completes the classification and all counts.

## Verification

A standalone standard-library Python checker uses the eight monomial masks of the exterior algebra, exact signed multiplication modulo odd primes, independent substitution of generator images, and direct tests of the exterior relations and idempotence. Over \(\mathbb F_3\), it exhausts **all** degree-two coefficients and cubic coefficients for each standard tangent projection: the numbers are \((1,27,81,1)\). It separately enumerates generating sets for rank-one and rank-two images with a fixed tangent subspace, recovering \(27\) images in each rank (respectively \(27\) and \(243\) admissible normalized generating tuples), and checks the canonical fixed-image fibers \(9\) and \(27\). It also tests all \(p^4\) rank-two normal-form parameter choices for each of \(p=5,7\), confirming validity without pretending to exhaust all endomorphisms in those characteristics.

For \(q=3\), the global theorem yields \(3159\) rank-one and \(9477\) rank-two retractions, plus the augmentation and identity: \(12638\) total. It gives \(351\) distinct images of each of the two intermediate ranks, hence \(704\) images overall. The checker validates the canonical fibers and image counts, while the general count relies on the proof rather than extrapolating from finite tests. Reproduce with `python3 artifacts/check_exterior_retractions.py` from the extracted package root; no third-party dependencies are needed.

## Relationship to prior work

Bavula's *The Jacobian map, the Jacobian group and the group of automorphisms of the Grassmann algebra* (arXiv:math/0703352, Sections 1–2, especially Theorem 2.14 and Lemma 2.2) develops the full automorphism-group structure and canonical coordinate projections of exterior algebras. Those results provide background for changes of coordinates but do not state the present finite-field retraction-image multiplicities. Guimarães and Koshlukov, *Automorphisms and superalgebra structures on the Grassmann algebra* (arXiv:2009.00175, first public September 1, 2020), study automorphisms of order two and induced superalgebra gradings of the infinite-dimensional Grassmann algebra in characteristic zero, a different endomorphism condition. Fonseca's 2018 work concerns graded polynomial identities over finite fields rather than the prescribed-image idempotent endomorphism census. No priority or universal uniqueness assertion is made beyond the explicitly inspected evidence.

## Limitations

The result covers the three-generator exterior algebra, unital algebra maps, and odd finite fields only. It is not a formula for all generator numbers, nor for characteristic two or arbitrary nonunital linear retractions. The original-literature survey is bounded; an equivalent finite-dimensional endomorphism-monoid calculation may exist under different terminology. No independent mathematical audit has been performed.

## References

1. A. de Araújo Guimarães and P. Koshlukov, *Automorphisms and superalgebra structures on the Grassmann algebra*, arXiv:2009.00175 (initial version, 2020-09-01), https://arxiv.org/abs/2009.00175.
2. V. V. Bavula, *The Jacobian map, the Jacobian group and the group of automorphisms of the Grassmann algebra*, arXiv:math/0703352 (2007), https://arxiv.org/abs/math/0703352.
3. L. F. G. Fonseca, *\(\mathbb Z_2\)-graded identities of the Grassmann algebra over a finite field*, International Journal of Algebra and Computation 28 (2018), 291–307, https://doi.org/10.1142/S0218196718500133 (abstract available; full article not materially inspected).
