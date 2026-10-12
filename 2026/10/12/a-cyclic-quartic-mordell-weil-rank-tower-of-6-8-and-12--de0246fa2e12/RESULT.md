# A cyclic quartic Mordell–Weil rank tower of \(6\), \(8\), and \(12\)

## Finding

Let \(w,t\) be algebraically independent over \(\mathbb C\), and put
\[
A(w)=w^2+14w+1,\qquad D(w)=w(w-1)^4,\qquad
C(w)=w^3-33w^2-33w+1.
\]
Consider the elliptic curve
\[
\mathcal E:\quad y^2=x^3-27\cdot481 A(w)t^4x
 +2916\bigl(30^4t^{10}+D(w)t^2\bigr)-54\cdot4879 C(w)t^6
\]
over \(\mathbb C(w,t)\). Let \(s,v\) satisfy \(s^2=w\) and \(v^2=s\). Then the exact Mordell–Weil ranks are
\[
\boxed{\begin{aligned}
\operatorname{rank}\mathcal E(\mathbb C(w,t))&=6,\\
\operatorname{rank}\mathcal E(\mathbb C(s,t))&=8,\\
\operatorname{rank}\mathcal E(\mathbb C(v,t))&=12.
\end{aligned}}
\]
More precisely, the order-four Galois automorphism \(\sigma:v\mapsto iv\), fixing \(t\), acts on the rational Mordell–Weil space \(V=\mathcal E(\mathbb C(v,t))\otimes_\mathbb Z\mathbb Q\) as
\[
\boxed{V\simeq \mathbb Q_{\mathrm{triv}}^{\oplus6}\oplus
 \mathbb Q_{\mathrm{sign}}^{\oplus2}\oplus
 \mathbb Q(i)^{\oplus2}},
\]
where the generator acts on the sign summand by \(-1\) and on each \(\mathbb Q(i)\) summand by multiplication by \(i\). These are statements about rational rank and rational representation, not a description of integral Mordell–Weil generators or their saturation.

## Assumptions and scope

The constant field is \(\mathbb C\) and has characteristic zero. All indicated parameters are transcendental with exactly the displayed algebraic relations. The curve is the generic Weierstrass curve of Burek's level-four Kummer-derived elliptic Calabi–Yau family, written over its coarse cyclic quartic parameter. The rank means the rank of rational points of this elliptic curve over the indicated two-variable function field. It does not assert the existence of a smooth Calabi–Yau compactification after quotienting the parameter base.

## Proof

**1. Cyclic descent and the full rank.** In the notation of Burek, set
\(A(z)=z^8+14z^4+1\), \(B(z)=z(z^4-1)\), and \(C(z)=z^{12}-33z^8-33z^4+1\). His equation (1.5), with \(u=2\), is precisely the displayed elliptic curve after substituting \(w=v^4\), since \(B(v)^4=w(w-1)^4\). In particular, it is fixed coefficientwise by \(\sigma(v)=iv\). Burek's Proposition 5.6 proves that \(\mathcal E(\mathbb C(v,t))\) is torsion-free of rank twelve. His Appendix A supplies twelve explicit independent sections, here ordered as
\[
P_1,\ldots,P_6,P'_1,\ldots,P'_6,
\]
with the primed family obtained by replacing his constant \(u=2\) by \(u=2i\). They span \(V\) over \(\mathbb Q\).

**2. Specialization determines the full Galois action.** The twelve polynomial sections specialize at \(v=5\) to points on a smooth elliptic K3 surface over \(\mathbb C(t)\). Burek's Appendix A.3 computes their exact height matrix \(H\) and shows \(\det H=4096/9\). Thus their specializations are linearly independent. Consequently, specialization at \(v=5\) is injective on the twelve-dimensional rational span of the generic sections. This is sufficient even if the specialized surface contains other sections. Because the generic rational Mordell–Weil space has rank exactly twelve, \(\sigma(P_j)\) is a rational linear combination of the twelve sections. Its specialization is obtained by substituting \(v=5i\) into the same polynomial formula. The latter point is on the *same* specialized Weierstrass curve, since the coefficients are invariant under \(v\mapsto iv\).

Let
\[
H_{jk}=\langle P_j(5),P_k(5)\rangle,
\quad G_{jk}=\langle P_j(5),P_k(5i)\rangle,
\]
where the twelve indices include both primed and unprimed points. It follows rigorously from the injective specialization that the matrix \(T\) of \(\sigma\) in the ordered generic basis is \(T=H^{-1}G\). No inference from finite experimental specialization to a universal identity is being made: specialization is used to identify an action on a **known twelve-dimensional** rational vector space.

**3. Exact mixed-height computation.** At \(v=5\), the minimal elliptic surface has \(\chi(\mathcal O)=2\), two split Kodaira-IV fibers at \(t=0,\infty\), and sixteen \(\mathrm I_1\) fibers. All relevant sections avoid the zero section. Hence Shioda's formula gives
\[
\langle P,Q\rangle=2-P\cdot Q-
 \operatorname{contr}_{0}(P,Q)-\operatorname{contr}_{\infty}(P,Q).
\]
At either type-IV fiber, two sections on the *same* nonidentity component contribute \(2/3\); on *different* nonidentity components they contribute \(1/3\). As Burek's local formulas (A.8) and (A.9) show, all original twelve sections have the same nonidentity component at zero, while their primed/unprimed distinction specifies one of two nonidentity components at infinity. Under \(v\mapsto iv\), the leading \(y/t\) at zero changes sign because \(B(iv)^2=-B(v)^2\), so the transformed section lies on the *other* nonidentity component there. The infinity component is unchanged.

At points other than \(0,\infty\), the intersection multiplicity is the minimum of the orders of vanishing of the two coordinate differences; their sum is obtained by the polynomial greatest common divisor over \(\mathbb Q(i)[t]\). At a common nonidentity branch of either exceptional fiber, the correction is \(\max(0,\operatorname{ord}(x_P-x_Q)-1)\) in the appropriate local coordinate; differing components contribute zero intersection. This is precisely the local intersection rule in Burek's Appendix A.3. For example, the exact intersections and correction terms yield \(G_{11}=2-0-1=1\), \(G_{12}=2-2-1=-1\), and \(G_{1,9}=2-4-2/3=-8/3\).

The attached exact-rational checker reconstructs all twelve section polynomials from equations (A.2)–(A.6), verifies all twelve Weierstrass identities symbolically, reconstructs the published matrix \(H\), and computes all \(144\) entries of \(G\) from polynomial gcds and these local corrections. It gives the following explicit integral matrix \(T=H^{-1}G\):
\[
\small
T=\begin{pmatrix}
0&0&-1&-1&0&0&-1&0&-1&-1&-1&-1\\
-1&1&0&-1&0&0&-1&0&0&-1&-1&-1\\
1&-1&1&0&0&0&1&-1&0&0&0&0\\
0&0&0&1&-1&0&0&0&0&1&0&0\\
0&0&0&1&1&0&0&0&0&0&1&0\\
0&0&0&0&0&0&0&0&0&0&0&1\\
-1&0&0&0&-1&-1&0&0&0&0&0&0\\
0&-1&0&0&-1&-1&0&0&0&0&0&0\\
0&0&-1&0&0&0&0&0&0&0&0&0\\
0&0&0&0&1&0&0&0&0&0&0&0\\
0&0&0&-1&0&0&0&0&0&0&0&0\\
0&0&0&0&0&1&0&0&0&0&0&0
\end{pmatrix}.
\]
Exact matrix multiplication verifies \(T^4=I\), \(T^{\mathsf T}HT=H\), and
\[
(\operatorname{tr}I,\operatorname{tr}T,\operatorname{tr}T^2,
\operatorname{tr}T^3)=(12,4,4,4).
\]
As an independent consistency check, redoing the mixed-height calculation with \(v=-5\) gives \(T^2\) exactly, rather than only its trace.

**4. Descent and character multiplicities.** For a finite Galois extension of fields, rational points over the fixed field are exactly the invariant rational points upstairs. Tensoring with \(\mathbb Q\) commutes with taking invariants of the finite group. Therefore
\[
\begin{aligned}
\dim_{\mathbb Q}V^{\langle\sigma\rangle}&=
\tfrac14(12+4+4+4)=6,\\
\dim_{\mathbb Q}V^{\langle\sigma^2\rangle}&=
\tfrac12(12+4)=8.
\end{aligned}
\]
The trivial, sign and faithful two-dimensional irreducible rational representations of the cyclic group of order four have the above multiplicities \(6,2,2\). Together with Burek's rank-twelve theorem, this proves all claims.

## Verification

Run `python verification/check_descent.py` with Python 3 and SymPy. It uses exact Gaussian-rational coefficients in \(\mathbb Q(i)\), exact polynomial gcds and rational matrix operations. It prints `CHECK_OK`, action traces `[12, 4, 4, 4]` and rank profile `[6, 8, 12]`, and checks equality of the independently calculated order-two action to the square of the order-four action. The formulas used for sections are included, so the program does not depend on an external paper's auxiliary code. An additional exact specialization at \(v=7\) reproduces the full matrix, as a nonessential cross-check. The infinite-function-field statement follows from the specialization-injectivity argument and published rank-twelve theorem; a finite sample is not presented as proof of a generic rank bound.

## Relationship to prior work

Burek establishes the rank-twelve threefold, identifies its explicit Weierstrass equation and twelve independent sections, and computes the reference height matrix; those facts are prerequisites and are not claimed here. Kumar and Kuwata establish the underlying \(F^{(4)}\) family, geometric Mordell–Weil bases, fields of definition and modular symmetries. Their results explain why a level-four parameter is natural. The claim here isolates the exact rank drops in the *specific coefficient-invariant cyclic quartic tower* and computes its complete rational cyclic-group character, neither of which was identified as a stated result in the inspected primary texts. The result is not a claim that such a cyclic action or height-pairing method is new.

## Limitations

The determination is over \(\mathbb C\) and concerns rational ranks and rational representation; it does not identify the saturated integral invariant sublattices, heights of their primitive bases, arithmetic ranks over number fields, or smooth models of the field-of-definition quotients. An earlier implicit invariant-lattice calculation in modular Mordell–Weil literature remains a bibliographic possibility. The proof uses Burek's established rank-twelve theorem, his specialized height matrix, and his local type-IV intersection computations as published premises; the attached program independently reconstructs the numerical certificates employed here.

## References

1. D. Burek, *An elliptic Calabi–Yau threefold of Mordell–Weil rank twelve*, arXiv:2610.01276v1 (first public 2026-10-01 UTC), especially Theorem 1.1, Proposition 5.6 and Appendix A, [arXiv](https://arxiv.org/abs/2610.01276).
2. A. Kumar and M. Kuwata, *Elliptic K3 surfaces associated with the product of two elliptic curves: Mordell–Weil lattices and their fields of definition*, arXiv:1409.2931, especially Sections 2 and 5, [arXiv](https://arxiv.org/abs/1409.2931).
3. T. Shioda, *On the Mordell–Weil lattices*, Commentarii Mathematici Universitatis Sancti Pauli 39 (1990), 211–240 (canonical heights and fiber corrections, cited via the two references above).
