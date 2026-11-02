# Elliptic Frobenius traces from rank-one Rota–Baxter operators on nilpotent algebras

## Finding

**Theorem.** Let \(k=\mathbb F_q\), where \(q\) is odd. Let \(V=k^4\), \(W=k^2\), and let \(Q_1,Q_2\) be linearly independent quadratic forms on \(V\) whose common projective zero locus
\[
C=\{[v]\in\mathbb P(V):Q_1(v)=Q_2(v)=0\}
\]
is a smooth complete-intersection curve. Put \(B_i(u,v)=\tfrac12(Q_i(u+v)-Q_i(u)-Q_i(v))\), and make \(J=V\oplus W\) a nonunital algebra by
\[
(u,w)\cdot(v,z)=(0,B_1(u,v)e_1+B_2(u,v)e_2).
\]
Then \(J\) is a six-dimensional, commutative, associative algebra with \(J^3=0\), \(J^2=\operatorname{Ann}(J)=W\). Write \(\mathcal R_1(J)\) for the set of **nonzero linear-rank-one**, weight-zero Rota–Baxter endomorphisms \(R:J\to J\), satisfying
\[
R(x)R(y)=R(R(x)y+xR(y))\qquad(x,y\in J).
\]
The exact number is
\[
\boxed{|\mathcal R_1(J)|=(q+1)(q^6-1)+q^2(q^4-1)|C(\mathbb F_q)|.}
\]
There are exactly \((q+1)(q^6-1)\) operators with image contained in \(W\), and \(q^2(q^4-1)|C(\mathbb F_q)|\) with image not contained in \(W\). All these formulas remain valid over each extension \(\mathbb F_{q^s}\) after replacing \(q\) by \(q^s\) and counting points of \(C\) over that extension.

Furthermore, **every elliptic curve over an odd-order finite field is realized by such an algebra**. Thus the single count \(|\mathcal R_1(J)|\) recovers \(|C(\mathbb F_q)|\), its Frobenius trace, the zeta function of \(C\), and the rank-one Rota–Baxter counts over all finite extensions.

## Assumptions and scope

All algebras are nonunital and all operator ranks are ranks as \(k\)-linear maps. Smooth complete intersection means that over an algebraic closure the two equations cut out a smooth codimension-two subscheme of \(\mathbb P^3\); in particular their gradients are independent at every point of \(C\). The characteristic is assumed odd so that quadratic polarization and the step dividing by \(2\) are valid. The vector spaces \(V\) and \(W\) have dimensions exactly four and two. The theorem counts operators as distinct linear maps, *not* classes modulo algebra automorphisms. The zero operator is excluded.

The curve \(C\) has genus one: the adjunction formula gives \(\omega_C\simeq\mathcal O_C(2+2-4)\simeq\mathcal O_C\). A smooth genus-one curve over a finite field has a rational point (e.g. by the genus-one Hasse bound), so it can be regarded as an elliptic curve after choosing a point. The count does not depend on that choice.

## Proof

**1. Algebra and intrinsic square.** The product is symmetric bilinear and lands in \(W\); all products with \(W\) vanish. Hence all triple products vanish and the algebra is commutative and associative. Linear independence of \(Q_1,Q_2\) implies that the image of the bilinear map \((B_1,B_2):V\times V\to W\) spans \(W\) (otherwise a nontrivial linear combination of the \(B_i\) would be zero). Thus \(J^2=W\). If \(u\in V\) annihilates \(J\), the gradients \(2B_i(u,-)\) both vanish; then \(Q_i(u)=B_i(u,u)=0\). A nonzero such \(u\) would be a singular point of \(C\). Therefore \(\operatorname{Ann}(J)=W\).

**2. Rank-one parameterization.** Every nonzero rank-one linear map has a presentation
\[
R(x)=f(x)a,\qquad 0\ne a\in J,\quad0\ne f\in J^*.
\]
Two presentations define the same map precisely when \((a,f)\) is replaced by \((ca,c^{-1}f)\), with \(c\in k^\times\). For such a map the weight-zero Rota–Baxter identity becomes
\[
f(x)f(y)a^2=(f(x)f(ay)+f(y)f(ax))a\quad\text{for all }x,y\in J.
\]
If \(a\in W\), then \(aJ=0=a^2\) and the identity holds for **every** nonzero \(f\).

Suppose \(a\notin W\). The left side of this equation lies in \(W\), while the right side lies in the line \(ka\), and \(W\cap ka=0\). Choosing \(x\) with \(f(x)=1\), then \(x=y\), shows \(a^2=0\) and \(f(ax)=0\), because the characteristic is not two. For every \(y\in\ker f\), the same identity using this \(x\) gives \(f(ay)=0\). Together these imply \(f(aJ)=0\). Conversely, \(a^2=0\) and \(f(aJ)=0\) make the identity hold. Hence these conditions are necessary and sufficient for a noncentral image generator.

**3. Smoothness makes the noncentral functional fiber constant.** Write \(a=(v,w)\), with \(v\in V\setminus\{0\}\). The square-zero condition is exactly \(Q_1(v)=Q_2(v)=0\), i.e. \([v]\in C(k)\). At such a point the Jacobian criterion gives linear independence of \(B_1(v,-)\) and \(B_2(v,-)\). Therefore \(aJ=W\), so \(f(aJ)=0\) is equivalent to \(f(W)=0\). There are exactly \(q^4-1\) nonzero such functionals in \(\operatorname{Ann}(W)\subset J^*\).

**4. Counting distinct operators.** A central image line can be any of the \(q+1\) points of \(\mathbb P(W)(k)\). Once a representative image generator is chosen, any nonzero functional gives a different operator, contributing \((q+1)(q^6-1)\). For each point \([v]\in C(k)\), choose one representative \(v\ne0\). Every image line outside \(W\) projecting to this point has a *unique* representative \((v,w)\) with \(w\in W\); thus it has \(q^2\) choices. For each, there are \(q^4-1\) admissible nonzero functionals, giving \(q^2(q^4-1)|C(k)|\) operators. The two image types are disjoint and exhaust all nonzero rank-one maps satisfying the identity. This proves the exact formula. The proof is unchanged over finite extensions because smoothness is geometric.

**5. Every elliptic curve occurs.** In odd characteristic, any elliptic curve has a Weierstrass equation
\[
E:\quad y^2=x^3+c_2x^2+c_4x+c_6,
\]
with separable cubic on the right. In homogeneous coordinates \([X_0:X_1:X_2:X_3]\), set
\[
Q_1=X_1^2-X_0X_3,\qquad
Q_2=X_2^2-X_1X_3-c_2X_0X_3-c_4X_0X_1-c_6X_0^2.
\]
On \(X_0\ne0\), the first equation sets \(X_3/X_0=(X_1/X_0)^2\), and the second is exactly the Weierstrass equation with \(x=X_1/X_0\), \(y=X_2/X_0\). At infinity the intersection has one point \([0:0:0:1]\), where the two differentials have independent \(dX_0,dX_1\) terms. In the affine chart, smoothness is the nonsingularity of the Weierstrass equation. Hence the quadrics cut out a smooth projective model of \(E\), so the algebra construction realizes every elliptic curve. Its polar forms are defined because \(2\) is invertible.

**6. Arithmetic recovery.** Put \(M=|\mathcal R_1(J)|\) and
\[
N_C=\frac{M-(q+1)(q^6-1)}{q^2(q^4-1)},\qquad t=q+1-N_C.
\]
The counting theorem gives \(N_C=|C(k)|\). By the classical genus-one Frobenius formula, the Hasse–Weil zeta function is
\[
Z(C,T)=\frac{1-tT+qT^2}{(1-T)(1-qT)}.
\]
Writing \(\alpha,\beta\) for the two roots of \(X^2-tX+q\), the extension point counts are \(q^s+1-\alpha^s-\beta^s\). Inserting these into step 4 with \(q\) replaced by \(q^s\) determines the rank-one operator count over every extension. All assertions follow.

## Verification

The standalone `checker.py` constructs the original multiplication from the polar forms; it does not assume the rank-one Rota–Baxter identity's reduction. For the elliptic quartics corresponding to \(y^2=x^3+\alpha x\), it compares projective intersections of two quadrics against direct Weierstrass point counts for eight prime-field/parameter cases: \(q=3,5,7,11\) with the parameters logged in `CHECK_OUTPUT.txt`. It checks Jacobian rank at every rational projective point. For all eight configurations, it compares the original Rota–Baxter identity on the \(36\) ordered pairs of basis vectors against the theorem's criterion for \(400\) sampled nonzero rank-one presentations.

It separately implements genuine \(\mathbb F_9=\mathbb F_3[t]/(t^2+1)\) arithmetic and finds \(16\) points on the base-changed elliptic curve, agreeing with the genus-one recurrence. For \(q=3\), \(\alpha=1\), it additionally **exhausts all** \((3^6-1)^2=529984\) pairs of nonzero image generators and nonzero functionals, testing the original operator identity on every ordered basis pair. Dividing representation counts by \(q-1=2\) yields exactly \(5792\) distinct rank-one operators: \(2912\) central-image and \(2880\) noncentral-image. This agrees with the theorem because \(|C(\mathbb F_3)|=4\). Over \(\mathbb F_5\), the three smooth curves with \(\alpha=1,2,4\) have respectively \(4,2,8\) rational points, producing the distinct predicted operator counts \(156144,124944,218544\). These finite checks corroborate, but do not replace, the proof for all fields and smooth pencils.

Run with `python checker.py` using Python 3 and NumPy. The expected complete output is embedded separately in `CHECK_OUTPUT.txt`; the last line is `ELLIPTIC_ROTA_BAXTER_RANK_ONE_OK`.

## Relationship to prior work

The central-extension viewpoint for nilpotent Jordan algebras, including constructions from symmetric cocycles, is established in Hegazi–Abdelwahab (arXiv:1301.6349; first public posting 2013-01-27), which classifies algebras up to dimension four. The present construction concerns a six-dimensional commutative associative central extension and its rank-one Rota–Baxter *operator counts*, not a reclassification of those lower-dimensional algebras. The general rank-one tensor reduction for certain other algebras and finite-field Rota–Baxter enumerations are already known. In particular, Zheng–Guo–Rosenkranz classify Rota–Baxter maps on semigroup algebras of orders two and three, not the present smooth-quadric family. Anghel (2018) relates elliptic curves to spectral-parameter Rota–Baxter/Yang–Baxter operators on complex matrix algebras; that is a different construction and does not give the present finite-field arithmetic enumeration. Neither the quadratic-curve geometry nor the elementary tensor reduction is claimed as new individually; the result is their exact combination, the universal elliptic realization and Frobenius-trace recovery.

## Limitations

The theorem requires odd characteristic, a smooth projective intersection of two quadrics, and rank exactly one. It counts neither zero nor higher-rank Rota–Baxter operators, and does not classify the six-dimensional algebras up to isomorphism. If the quadratic pencil is singular, its Jacobian rank can drop at square-zero image generators, so the constant fiber \(q^4-1\) need not apply. The zeta-function conclusion invokes the standard genus-one Frobenius theorem. The finite computations check only specified small fields, not all finite fields. Publication priority beyond the inspected indexed literature is not independently certified.

## References

1. A. S. Hegazi and H. Abdelwahab, *Construction of Nilpotent Jordan Algebras Over any Arbitrary Fields*, arXiv:1301.6349, first submitted 2013-01-27, https://arxiv.org/abs/1301.6349.
2. S. Zheng, L. Guo and M. Rosenkranz, *Classification of Rota-Baxter operators on semigroup algebras of order two and three*, Communications in Algebra 47 (2019), 3094–3116, https://doi.org/10.1080/00927872.2018.1552278.
3. C. Anghel, *Rota-Baxter operators and elliptic curves*, presentation, 2018-09-20 to 2018-09-23, https://www.imar.ro/~canghel/anghel_caim2018chisinau.pdf.
4. Classical genus-one adjunction, Hasse bound and Frobenius zeta-function formula; used here in their standard forms.
