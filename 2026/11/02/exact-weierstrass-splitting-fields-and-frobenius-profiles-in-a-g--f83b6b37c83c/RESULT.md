# Exact Weierstrass splitting fields and Frobenius profiles in a genus-two Jacobian-isomorphism family

## Finding
Let \(K\) be any field of characteristic different from \(2\). Write
\[
 U(T)=T(T^2+1)(2T^2+1)(T^2+2)(T^2-1)(T^4+T^2+1).
\]
For every \(t\in K\) with \(U(t)\ne0\), consider the smooth projective genus-two curves \(C_t\) and \(C_{-t}\) defined by the affine models
\[
 (t^2+1)(t^2-t+1)(t-1)y^2
 =(4x^2+t)\bigl(16t^4x^4+8(2t^4-4t^3+5t^2-4t+2)x^2+1\bigr),
\]
and the same model with parameter \(-t\). Their unpolarized Jacobians are isomorphic over \(K\) by Abdellatif's Theorem 2 [1]. The additional factor \(t\ne0\) in the parameter assumptions is explicitly required in its proof.

**Theorem (Weierstrass Galois structure).** Put \(i^2=-1\), \(s^2=t^2+1\), \(A=t^2-t+1\), and \(B=t-1\), in a separable closure of \(K\). The six Weierstrass points of \(C_t\), identified with their \(x\)-coordinates, are exactly
\[
 \left\{\frac{\sqrt{-t}}2,-\frac{\sqrt{-t}}2\right\}
 \ \sqcup\ 
 \left\{\frac{i(\epsilon A+\delta Bs)}{2t^2}:\epsilon,\delta\in\{\pm1\}\right\}.
\]
All six are distinct. The exact splitting field of these six points is
\[
 K\bigl(i,\sqrt{t^2+1},\sqrt t\bigr).
\]
The six points of \(C_{-t}\) have **the same exact splitting field**, despite generally different Galois permutation representations. Thus the common splitting field is multiquadratic of degree at most eight.

The complete permutation representations over \(K\) are explicit. For any \(g\in\operatorname{Gal}(K^{\mathrm{sep}}/K)\), define signs \(\alpha_g,\beta_g,\gamma_g\in\{\pm1\}\) by \(g(i)=\alpha_g i\), \(g(s)=\beta_gs\), \(g(\sqrt t)=\gamma_g\sqrt t\). On the four-root block, \(g\) acts as \((\epsilon,\delta)\mapsto(\alpha_g\epsilon,\alpha_g\beta_g\delta)\) on **both** curves (with the corresponding \(A,B\) for each). On the two-root block of \(C_t\) it swaps the points exactly when \(\alpha_g\gamma_g=-1\), whereas on \(C_{-t}\) it swaps them exactly when \(\gamma_g=-1\).

For a finite field \(K=\mathbb F_q\) of odd cardinality, let \(\chi\) be its quadratic character, extended by \(\chi(0)=0\), and let \(w_q(C)\) be the number of \(\mathbb F_q\)-rational Weierstrass points. Then
\[
 \begin{aligned}
 w_q(C_t)&=2\mathbf1_{\chi(-t)=1}
      +4\mathbf1_{\chi(-1)=\chi(t^2+1)=1},\\
 w_q(C_{-t})&=2\mathbf1_{\chi(t)=1}
      +4\mathbf1_{\chi(-1)=\chi(t^2+1)=1}.
 \end{aligned}
\]
The quartic group of four Weierstrass points has Frobenius cycle type either \(1^4\) or \(2^2\); a four-cycle never occurs. **If \(q\equiv3\pmod4\), the two curves have exactly \(0\) and \(2\) rational Weierstrass points, in some order**, while their zeta functions are identical. Their six-point Frobenius cycle types are consequently \(2^3\) and \(1^2 2^2\), respectively. If \(q\equiv1\pmod4\), they have equal Weierstrass counts, given by the formulas. Over \(\mathbb F_{q^2}\), all six Weierstrass points of both curves are rational.

For example, over \(\mathbb F_{11}\) the admissible parameter \(t=2\) gives \(w_{11}(C_2)=2\) and \(w_{11}(C_{-2})=0\), although both curves have \(20\) rational points. The latter point-count agreement holds over every extension field by the isomorphism of their Jacobians [1].

## Assumptions and scope
The field \(K\) need not be perfect; its characteristic must only differ from \(2\). The parameter restriction excludes all vanishing factors of \(U\). In particular \(t\ne0\), \(B\ne0\), \(A\ne0\), \(t^2+1\ne0\), and also \(t^2+t+1\ne0\), since \(t^4+t^2+1=(t^2-t+1)(t^2+t+1)\). All square roots are chosen in a separable closure; the asserted fields are independent of these choices. The six-point Weierstrass divisor is the ramification divisor of the unique degree-two map from a genus-two curve to \(\mathbb P^1\); its field of definition and permutation representation are intrinsic to the curve. The coordinates refer to the displayed hyperelliptic model.

The finite-field statements require only \(q\) odd and an admissible \(t\in\mathbb F_q\). There is no assertion that every small finite field contains an admissible parameter. An isomorphism of Jacobians here always means **unpolarized**; the canonical principal polarizations are not asserted to agree.

## Proof
**1. A separable sextic.** Set
\[
 Q_t(x)=16t^4x^4+8(2t^4-4t^3+5t^2-4t+2)x^2+1.
\]
Exact polynomial identities over \(\mathbb Z[t,x]\) give
\[
 Q_t(x)=(4t^2x^2+1)^2+16(t^2+1)(t-1)^2x^2
\]
and
\[
 (t^2-t+1)^2=t^2+(t^2+1)(t-1)^2.
\]
Therefore, after adjoining \(i\) and \(s\), factoring the quartic into two quadratics yields the four explicitly claimed roots \(i(\epsilon A+\delta Bs)/(2t^2)\). The roots are distinct: \(A\ne0\), \(Bs\ne0\), and \(A^2-B^2s^2=t^2\ne0\). The other two roots are the distinct zeros of \(4x^2+t\). There is no collision between either pair because
\[
 \operatorname{Res}_x(4x^2+t,Q_t(x))
 =256(t-1)^4(t^2-t+1)^4\ne0.
\]
The coefficient of \(x^6\) in the sextic is \(64t^4\ne0\); hence its smooth projective double cover of \(\mathbb P^1\) has exactly six simple branch points, is geometrically connected, and has genus two by Riemann--Hurwitz.

**2. Exact splitting field.** Denote the four quartic roots by \(r_{\epsilon,\delta}\). All six roots belong to \(L=K(i,s,\sqrt t)\) (the first two since \(\sqrt{-t}=i\sqrt t\)). Conversely the full root field contains
\[
 r_{+,+}-r_{-,+}=\frac{iA}{t^2},\qquad
 r_{+,+}-r_{+,-}=\frac{iBs}{t^2}.
\]
Since \(A,B,t\) are nonzero in \(K\), these expressions recover \(i\) and \(s\) from the quartic roots. Either of the remaining quadratic roots then recovers \(\sqrt{-t}\), and multiplying by \(i\) recovers \(\sqrt t\). Thus the root field equals \(L\), not merely a subfield. For \(C_{-t}\), replace \(A,B\) by \(t^2+t+1,-t-1\). Both remain nonzero, so the same calculation recovers \(i,s\); its linear pair gives \(\sqrt t\). Both exact splitting fields are therefore \(L\). The extension is generated by three square roots and is separable multiquadratic, possibly of degree less than eight because of square-class relations.

**3. Full Frobenius action.** In \(\mathbb F_q\), the four-root parameters transform under Frobenius as
\[
 (\epsilon,\delta)\longmapsto
 \bigl(\chi(-1)\epsilon,\,\chi(-1)\chi(t^2+1)\delta\bigr).
\]
Both signs have order dividing two. Frobenius thus fixes all four if and only if \(\chi(-1)=\chi(t^2+1)=1\); otherwise it has exactly two transpositions. The other pair consists of two rational points if and only if \(\chi(-t)=1\), while the corresponding pair on \(C_{-t}\) is rational if and only if \(\chi(t)=1\). This proves the displayed formulas and complete cycle-type alternatives.

If \(q\equiv3\pmod4\), then \(\chi(-1)=-1\), making the quartic subset two transpositions in both curves. Moreover \(\chi(-t)=-\chi(t)\), so exactly one quadratic subset consists of two rational points and the other is a transposition. Thus \(\{w_q(C_t),w_q(C_{-t})\}=\{0,2\}\) and the entire cycle types are \(1^2 2^2\) and \(2^3\). If \(q\equiv1\pmod4\), \(\chi(-t)=\chi(t)\), and their complete cycle-type profiles agree. Every nontrivial Frobenius cycle has length two, proving universal splitting over \(\mathbb F_{q^2}\).

**4. Why the zeta functions agree.** Abdellatif's Theorem 2 [1], with the nonzero parameter assumption made explicit in its proof, constructs an isomorphism \(\operatorname{Jac}(C_t)\simeq\operatorname{Jac}(C_{-t})\) over \(K\) as unpolarized abelian varieties. Over a finite field, isomorphic Jacobians have identical characteristic polynomials of Frobenius on first \(\ell\)-adic cohomology, hence identical zeta functions and curve point counts over every finite extension. This external theorem is a cited input, not re-proved here. The new Weierstrass-branch calculation shows that this agreement need not preserve the number or permutation type of rational Weierstrass points.

## Verification
The standalone `verify_weierstrass.py` is executable with Python 3 and SymPy: `python verify_weierstrass.py`. It verifies the quartic factorization, its four individual root identities in the algebraic square-root ring, the sextic quadratic--quartic resultant, and the Weierstrass character formulas by direct polynomial root enumeration in sixteen prime fields and four quadratic extensions. There are \(488\) admissible parameter instances in the tested fields. It separately verifies \(488\) matching paired genus-two point counts using quadratic-character sums and the two points at infinity, and explicitly checks complete splitting into six roots over four selected quadratic extensions. Its final marker is `WEIERSTRASS_AND_JACOBIAN_COMPATIBILITY_PASS`. This is finite corroboration; the universal claims follow from the symbolic identities and field-theoretic argument above.

For \(q=11\) and \(t=2\), direct field enumeration gives two rational roots for \(C_2\) (\(x=4,7\)), none for \(C_{-2}\), and \(20\) curve points for each. These examples do not assert a classification of all genus-two curves with isomorphic Jacobians.

## Relationship to prior work
Abdellatif [1], first publicly available October 4, 2024, supplies precisely the two sextic equations, their parameter exclusions, and the isomorphism of **unpolarized Jacobians**, as part of a degree-four elliptic-isogeny construction. Its Section 6 gives quadratic factor data, but it does not state this family-specific six-point Weierstrass splitting field, Galois label action, exact finite-field rational-Weierstrass counts, or the uniform \(q\equiv3\pmod4\) contrast. Those are obtained here from a separate explicit quartic factorization and Frobenius analysis. The additional restriction \(t\ne0\) is present in the source's proof and is adopted rather than silently extending it.

Howe [2] previously constructed other genus-two pairs with isomorphic unpolarized Jacobians and showed that broad arithmetic properties such as having rational or real points need not be determined by the unpolarized Jacobian. The **general phenomenon** of arithmetic disparity is not new. The present scope is narrower and more precise: the complete Weierstrass permutation representations and exact common splitting field in Abdellatif's specific degree-four family, including formulas over every admissible odd finite field. General six-point branch/Galois theory supplies the language but does not by itself compute this parameter-dependent representation.

## Limitations
The claim concerns the six Weierstrass points, not all rational points or an isomorphism of principally polarized Jacobians. It does not classify the locus of geometrically isomorphic specialized curves, establish a new Jacobian isomorphism, prove absolute simplicity, or count admissible parameters for every finite field. Existence of admissible parameters in a given small field is not claimed. Field extensions of degree \(1,2,4,8\) can occur as subcases of the displayed multiquadratic compositum; their occurrence is not classified individually. Earlier results, including the source's theorem and Howe's broader arithmetic examples, are credited explicitly. A prior equivalent branch-field computation in unindexed or later literature cannot be excluded without independent verification.

## References
[1] Raghda Abdellatif, *Families of Pairs of Genus 2 Curves with Isomorphic Unpolarized Jacobians*, arXiv:2410.03664v1 (submitted 2024-10-04), Theorem 2 and Section 6. https://arxiv.org/html/2410.03664v1

[2] Everett W. Howe, *Infinite families of pairs of curves over \(\mathbb Q\) with isomorphic Jacobians*, arXiv:math/0304471 (2003), Theorem 1 and Introduction; *Journal of the London Mathematical Society* 72 (2005), 327–350. https://arxiv.org/abs/math/0304471

[3] MSC2020, classification 14H25 (arithmetic ground fields for curves). https://mathscinet.ams.org/msc/msc2020.html?t=14H20
