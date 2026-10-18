# Characteristic-two canonical ribbon in the Jacobian scheme of the chordal cubic

## Finding

Let \(k\) be an algebraically closed field, and consider the *chordal cubic threefold* \(X_k\subset\mathbb P^4_k\) defined by the Hankel determinant
\[
F=\det\begin{pmatrix}a&b&c\\ b&c&d\\ c&d&e\end{pmatrix}
=ace+2bcd-ad^2-b^2e-c^3.
\]
Let \(\Sigma_k\) be the intrinsic hypersurface singular scheme, defined by \((F,F_a,F_b,F_c,F_d,F_e)\).

**The characteristic dichotomy is scheme-theoretic.** If \(\operatorname{char}k\ne2\), then \(\Sigma_k\) is the *reduced* rational normal quartic \(C=\nu_4(\mathbb P^1)\). If \(\operatorname{char}k=2\), then
\[
\Sigma_k=V(ce+d^2,\ ae+c^2,\ ac+b^2)\subset\mathbb P^4_k.
\]
This is a locally complete-intersection, generically double, non-split ribbon supported on the same \(C\), with conormal sheaf \(\mathcal I_{C/\Sigma_k}\simeq\mathcal O_{\mathbb P^1}(-6)\). Its homogeneous ideal is a complete intersection of three quadrics, so
\[
\deg\Sigma_k=8,\qquad p_a(\Sigma_k)=5,\qquad
\omega_{\Sigma_k}\simeq\mathcal O_{\Sigma_k}(1).
\]
Under the standard coordinates, it is precisely the genus-five *balanced canonical ribbon*. In particular, the singular-scheme family over \(\operatorname{Spec}\mathbb Z\) is not flat at the prime \(2\): the Hilbert polynomial jumps from \(4m+1\) away from \(2\) to \(8m-4\) at \(2\).

## Assumptions and scope

All assertions concern geometric fibers over algebraically closed fields; the projective Jacobian scheme includes the original cubic equation, which matters in characteristic \(3\). The identification of the ribbon and its conormal is characteristic-two only. The characteristic-other-than-two statement includes characteristic \(3\), with the original equation retained. Scheme degrees and Hilbert polynomials use \(\mathcal O_{\mathbb P^4}(1)\). The family in the last statement is the closed singular subscheme cut out by \(F\) and its five ordinary derivatives in the integral projective cubic.

## Proof

**1. Exact Jacobian ideal.** Integer differentiation yields
\[
(F_a,F_b,F_c,F_d,F_e)
=(ce-d^2,\ 2(cd-be),\ ae+2bd-3c^2,\ 2(bc-ad),\ ac-b^2).
\]
In characteristic two the second and fourth derivatives vanish, and the remaining three are the displayed quadrics. Moreover, the Euler relation \(3F=\sum x_iF_{x_i}\) becomes \(F=\sum x_iF_{x_i}\), so adjoining \(F\) does not enlarge the ideal.

**2. Two affine charts and reduced support in characteristic two.** On \(D(a)\), set \(a=1\). The equations force \(c=b^2\) and \(e=c^2=b^4\). The remaining equation is \(d^2=b^6\). With \(t=b\) and \(u=d+b^3\), the exact coordinate algebra is
\[
\mathcal O_{\Sigma_k}(D(a))\simeq k[t,u]/(u^2),
\quad [a:b:c:d:e]=[1:t:t^2:t^3+u:t^4].
\]
Similarly, on \(D(e)\), with \(e=1\), one obtains
\[
\mathcal O_{\Sigma_k}(D(e))\simeq k[q,v]/(v^2),
\quad [a:b:c:d:e]=[q^4:q^3+v:q^2:q:1].
\]
If \(a=e=0\) at a geometric point of the singular scheme, the equations give \(b^2=c^2=d^2=0\), contradicting projectivity. Hence these charts cover \(\Sigma_k\). Reduction sets \(u=v=0\), giving the ordinary quartic Veronese curve \(C\), and the nilradical is locally invertible with square zero.

**3. Gluing and conormal.** On the intersection \(D(ae)\), the two presentations satisfy
\[
q=t^{-1}+u t^{-4},\qquad v=u t^{-6},\qquad u^2=v^2=0.
\]
Thus the conormal line is \(\mathcal O_{\mathbb P^1}(-6)\). The correction \(ut^{-4}=v q^{-2}\) determines a nonzero class in \(H^1(\mathbb P^1,T_{\mathbb P^1}\otimes\mathcal O(-6))\simeq H^1(\mathbb P^1,\mathcal O(-4))\): relative to the second chart the class is represented by \(q^{-2}\), which is not a Čech coboundary. This shows the ribbon is non-split. The same gluing, after reversing chart names and noting that signs coincide in characteristic two, is the balanced genus-five ribbon of Deopurkar–Fedorchuk–Swinarski, Definition 4.1.

**4. Complete intersection and invariants.** The reduced support has projective dimension one, so the three quadrics have homogeneous height three. In the Cohen–Macaulay polynomial ring in five variables they form a regular sequence. Adjunction for a \((2,2,2)\) complete intersection gives \(\omega_{\Sigma_k}=\mathcal O_{\Sigma_k}(6-5)=\mathcal O_{\Sigma_k}(1)\); its degree is \(2\cdot2\cdot2=8\). The Hilbert series
\[
\frac{(1-T^2)^3}{(1-T)^5}
=\frac{(1+T)^3}{(1-T)^2}
\]
has eventual Hilbert polynomial \(8m-4\), so \(p_a=5\). This independently follows from \(0\to\mathcal O_{\mathbb P^1}(-6)\to\mathcal O_{\Sigma_k}\to\mathcal O_{\mathbb P^1}\to0\). There are exactly five independent linear sections, and \(\omega=\mathcal O(1)\), hence the displayed embedding is canonical.

**5. Other characteristics.** When \(2\) is invertible, on \(D(a)\) the three derivative equations \(F_e=0\), \(F_d=0\), \(F_c=0\) successively yield \(c=b^2\), \(d=b^3\), and \(e=b^4\). They generate the whole local singular ideal there, so that chart is the reduced affine Veronese parameter line. The symmetric argument applies on \(D(e)\). If a geometric singular point satisfied \(a=e=0\), the derivatives \(F_a,F_e\) would force \(b=d=0\); the defining equation then gives \(c^3=0\), impossible in projective space. Therefore the two reduced charts cover all of \(\Sigma_k\), including in characteristic \(3\). The reduced quartic has Hilbert polynomial \(4m+1\), so the integral singular scheme has distinct fiber Hilbert polynomials and is not flat at \(2\).

## Verification

Running `python verify.py` with SymPy executes exact integer and characteristic-two polynomial identities for the determinant, five derivatives, chart maps, overlap transition, and genus-five ribbon generators. It verifies the Hilbert polynomial in degrees \(2\) through \(10\), and exhaustively checks the *set of prime-field rational singular points* for \(p\in\{2,3,5,7\}\). A successful run prints `VERIFY_OK`. The finite-point census is only an independent consistency check of geometric support, not a proof of the scheme structure or the infinite-characteristic dichotomy. The full proof is the chart/ideal computation above.

## Relationship to prior work

Allcock–Carlson–Toledo write the standard chordal cubic as this Hankel determinant and identify its rational normal quartic chordal locus (chapter 2, equations (2.3)–(2.4)), in their complex setting. Bayer–Eisenbud establish the geometry and classification framework for canonical ribbons. Deopurkar–Fedorchuk–Swinarski **already explicitly give the three genus-five balanced-ribbon quadrics**, which specialize in characteristic two to the three displayed Jacobian generators (their Theorem 4.4 and Corollary 4.8). Thus the *equations and abstract ribbon are not new*. The contribution asserted here is the characteristic-sensitive identification of the cubic's *intrinsic Jacobian singular scheme* with that ribbon, including the complete odd/characteristic-two Hilbert-polynomial dichotomy. This is a close algebraic consequence of combining two published constructions, and possible explicit antecedents remain a significant novelty risk.

## Limitations

The nonreduced ribbon is a special-fiber phenomenon and is not asserted in odd characteristic. The paper does not analyze the relative embedded structure of the entire arithmetic singular scheme beyond the fiber Hilbert-polynomial obstruction to flatness, nor distinguish non-geometric field forms. It does not give new equations for the abstract balanced ribbon: those are known. No independent audit has been performed, and an unlocated source may already make the Jacobian/ribbon connection.

## References

1. D. Allcock, J. A. Carlson, D. Toledo, *The Moduli Space of Cubic Threefolds as a Ball Quotient*, arXiv:math/0608287 (first submitted 2006-08-11), chapter 2, equations (2.3)–(2.4). https://arxiv.org/abs/math/0608287
2. D. Bayer and D. Eisenbud, *Ribbons and Their Canonical Embeddings*, Transactions of the American Mathematical Society 347 (1995), 719–756. https://www.math.columbia.edu/~bayer/papers/Ribbons_BE95.pdf
3. A. Deopurkar, M. Fedorchuk, D. Swinarski, *Gröbner Techniques and Ribbons*, especially Definition 4.1, Theorem 4.4, Corollary 4.8. https://ananddeopurkar.org/papers/groebner.pdf
