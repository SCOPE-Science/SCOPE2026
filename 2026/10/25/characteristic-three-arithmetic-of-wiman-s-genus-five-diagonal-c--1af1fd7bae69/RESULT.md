# Characteristic-three arithmetic of Wiman's genus-five diagonal complete intersection

## Finding
Let \(X\) be the projective curve over \(\mathbb F_3\) cut out in \(\mathbb P^4\) by
\[
\begin{aligned}
x_0^2+x_3^2+x_4^2&=0,\\
x_1^2+x_3^2-x_4^2&=0,\\
x_2^2+x_3x_4&=0.
\end{aligned}
\]
This integral-equation model appears as the genus-five Wiman entry with complex automorphism-group identifier \((192,181)\) in Swinarski's equation catalogue. Its *literal characteristic-three fiber* is smooth, geometrically connected, nonhyperelliptic and nontrigonal, of genus five. Its exact zeta function is
\[
\boxed{Z(X/\mathbb F_3,T)=\frac{(1+3T^2)^3(1-2T^2+9T^4)}{(1-T)(1-3T)}.}
\]
Equivalently its numerator is
\[
1+7T^2+18T^4+54T^6+189T^8+243T^{10}.
\]
The Jacobian has \(3\)-rank \(2\), \(a\)-number \(3\), and Newton slopes \(0^{[2]},(1/2)^{[6]},1^{[2]}\). It is prime-to-three isogenous over \(\mathbb F_3\) to the product of three supersingular elliptic curves and an ordinary, \(\mathbb F_3\)-simple abelian surface. In particular,
\[
\#X(\mathbb F_3)=4,\quad \#X(\mathbb F_9)=24,\quad
\#X(\mathbb F_{27})=28,\quad \#X(\mathbb F_{81})=56.
\]
The rational-point count over every extension \(\mathbb F_{3^r}\), for every integer \(r\geq1\), is uniquely determined by the displayed zeta function.

## Assumptions and scope
All equations are interpreted over \(\mathbb F_3\), with geometry after base change to an algebraic closure when needed. This is a statement about the literal coefficientwise reduction of the three *displayed* integral quadrics, not about every integral model of the complex Wiman curve, or about its full automorphism group in characteristic three. The Weil polynomial is specific to this \(\mathbb F_3\)-form: geometric isomorphism or the same complex automorphism-group label alone does not identify the arithmetic twist.

The three quadratic equations form the canonical ideal of this smooth projective curve: a smooth complete intersection of type \((2,2,2)\) in \(\mathbb P^4\) has canonical bundle \(\mathcal O_X(1)\) and genus \(5\). In particular, it is nonhyperelliptic and nontrigonal. The term *simple* below means simple over \(\mathbb F_3\); absolute simplicity is not asserted.

## Proof
**1. Smoothness, connectedness, and genus.** The projection
\[
\pi:X\longrightarrow\mathbb P^1,\qquad
[x_0:x_1:x_2:x_3:x_4]\longmapsto[x_3:x_4]
\]
is everywhere defined: setting \(x_3=x_4=0\) in the defining equations forces all five projective coordinates to vanish. Put \(t=x_3/x_4\). The function field is obtained from \(\mathbb F_3(t)\) by adjoining the three square roots
\[
q_1=-(t^2+1),\qquad q_2=1-t^2,\qquad q_3=-t.
\]
The six geometric branch points are the two zeros of \(t^2+1\), the two zeros of \(t^2-1\), and \(0,\infty\). These are pairwise distinct, all simple zeros or poles of the corresponding square classes. Their disjoint odd-valuation supports prove that the three classes are linearly independent in \(\overline{\mathbb F}_3(t)^\times/\overline{\mathbb F}_3(t)^{\times2}\). Thus the cover is geometrically connected of degree \(8\), Galois with group \(G=(\mathbb Z/2\mathbb Z)^3\). Since exactly one quadratic coordinate branches at each branch point, local Kummer coordinates show that its smooth projective model is smooth at the branch fibers; it is étale elsewhere. The complete intersection itself is nonsingular by the same local description and its finite projection, hence agrees with that model. Riemann–Hurwitz gives
\[
2g(X)-2=8(-2)+6\cdot4=8,\qquad g(X)=5.
\]
The canonical complete-intersection adjunction verifies the same genus independently.

**2. Character quotients.** Each nonzero character of \(G\) corresponds to the double cover with square root of the product of its selected \(q_i\). Three singleton characters have two geometric branch points and hence genus zero. The other four characters yield the following smooth quotient curves over \(\mathbb F_3\):
\[
\begin{array}{rlcl}
E_{12}:&y^2=t^4-1,&&g=1,\\
E_{13}:&y^2=t^3+t,&&g=1,\\
E_{23}:&y^2=t^3-t,&&g=1,\\
H:&y^2=t-t^5,&&g=2.
\end{array}
\]
For the affine odd-degree models, infinity is the additional branch point. All four right-hand sides are squarefree in characteristic three. The three genus-one quotients have rational points and thus carry the indicated elliptic-curve structures.

**3. Jacobian splitting with controlled degree.** The character idempotents
\[
e_\chi=\frac1{8}\sum_{g\in G}\chi(g)g
\]
lie in \(\mathbb Z_{(3)}[G]\). Their mutually orthogonal decomposition on the Jacobian's prime-to-two isogeny category gives, using the seven nontrivial quotient characters and the vanishing singleton-genus pieces,
\[
\operatorname{Jac}(X)\sim_{\mathbb F_3}^{(2)}
E_{12}\times E_{13}\times E_{23}\times\operatorname{Jac}(H).
\]
Here the superscript indicates an isogeny whose kernel is annihilated by a power of two. One may realize it with sums of pullbacks and norms from the quotient maps, with denominators only powers of \(2\). Consequently it induces an isomorphism on \(3\)-divisible groups after the appropriate identifications. In particular the Frobenius numerator and the Newton polygon split as those of the factors, and their \(3\)-ranks and \(a\)-numbers add.

**4. Exact finite base-field arithmetic.** Write \(Q_i(T,U)\) for the homogenizations of the three quadratic square-root forms, and for a subset \(S\subseteq\{1,2,3\}\) write \(Q_S=\prod_{i\in S}Q_i\). For any odd \(q=3^r\), each double cover associated to \(S\) has exactly
\[
\#C_S(\mathbb F_q)=\sum_{[T:U]\in\mathbb P^1(\mathbb F_q)}
\bigl(1+\chi_q(Q_S(T,U))\bigr),
\]
where \(\chi_q(0)=0\) and \(\chi_q\) is the quadratic character on \(\mathbb F_q^\times\). The forms \(Q_S\) have even degrees, so the expression is independent of projective representatives. Exhausting the \(q+1\) representatives gives the following exact arithmetic certificate, independently reproduced by the embedded standard-library verifier:

| Quotient | \(\#(\mathbb F_3)\) | \(\#(\mathbb F_9)\) |
|---|---:|---:|
| \(E_{12}\) | 4 | 16 |
| \(E_{13}\) | 4 | 16 |
| \(E_{23}\) | 4 | 16 |
| \(H\) | 4 | 6 |

For each elliptic curve, the trace of \(3\)-Frobenius is \(3+1-4=0\), giving its numerator \(1+3T^2\). For the genus-two quotient, writing \(s_r\) for the sum of the \(r\)-th powers of its four Frobenius eigenvalues gives \(s_1=4-4=0\) and \(s_2=10-6=4\). Newton's identities therefore give the first two coefficients \(0\) and \(-2\); the genus-two functional equation supplies the remaining coefficients, yielding \(1-2T^2+9T^4\). Multiplying these factors via Step 3 proves the announced genus-five zeta numerator, and hence all extension-field point counts. The four displayed counts also agree with the formula; the \(\mathbb F_3\) and \(\mathbb F_9\) counts were separately obtained by exhaustive direct projective enumeration of all five-coordinate points satisfying the three quadrics.

**5. Newton polygon, \(a\)-number and simple factor.** The three trace-zero elliptic curves are supersingular in characteristic three. For \(H:y^2=f(t)\) with \(f(t)=t-t^5\), the Cartier–Manin matrix with respect to the standard genus-two basis \(dt/y,t\,dt/y\) is, up to transpose and Frobenius conventions,
\[
\begin{pmatrix}0&-1\\1&0\end{pmatrix}.
\]
Indeed, in characteristic three the required coefficients are those of \(f(t)^{(3-1)/2}=t-t^5\) in degrees \(1,2,4,5\). The determinant is nonzero, so \(\operatorname{Jac}(H)\) is ordinary: \(3\)-rank two and \(a\)-number zero. Each supersingular elliptic factor has \(3\)-rank zero and \(a\)-number one. The prime-to-three isogeny proves the claimed \(3\)-rank two, \(a\)-number three, and the Newton slopes.

Finally, \(\operatorname{Jac}(H)\) has Frobenius characteristic polynomial \(u^4-2u^2+9\). To factor this monic even polynomial as two rational quadratics, either both factors are even, requiring rational roots of \(z^2+2z+9\), whose discriminant is \(-32\), or they have opposite linear coefficients and equal constants \(b=\pm3\), forcing their linear coefficient's square to be \(2b+2\), namely \(8\) or \(-4\). Neither can happen over \(\mathbb Q\). Thus the quartic is irreducible over \(\mathbb Q\), and the corresponding ordinary abelian surface is simple over \(\mathbb F_3\).

## Verification
The included file `verify.py` is self-contained, uses only the Python standard library, and uses the irreducible polynomials \(z^2+1\), \(z^3+2z+1\), and \(z^4+z+2\) for the relevant extensions of \(\mathbb F_3\). It exhaustively counts the projective base fibers of the original degree-eight cover and the four positive-genus character quotients over \(\mathbb F_3\), \(\mathbb F_9\), \(\mathbb F_{27}\), and \(\mathbb F_{81}\). It additionally enumerates the original canonical complete intersection directly in \(\mathbb P^4(\mathbb F_3)\) and \(\mathbb P^4(\mathbb F_9)\), providing a genuinely distinct check of the first two totals. Running `python3 verify.py` prints `VERIFY_OK` only after all assertions hold. The all-extension conclusion depends on the proved Jacobian decomposition and the genus-one and genus-two Weil polynomials, not on extrapolating four finite tests.

## Relationship to prior work
Swinarski's 2016 preprint, *Equations of Riemann surfaces with automorphisms*, §4.3, prints these exact canonical quadrics as the complex Wiman genus-five entry; that model is prior work and is not claimed as new. Kudo and Harashita's 2021 preprint on parametrizing genus-five nonhyperelliptic, nontrigonal curves is the motivating modern arithmetic study: its characteristic-three calculations select curves with at least 32 points over \(\mathbb F_9\), and their displayed list of four Weil polynomials concerns that 32-point threshold, not this 24-point Wiman-form curve. Their 2022 paper treats the complementary hyperelliptic and trigonal genus-five categories, also without the present exact zeta or mixed Newton-polygon claim. Work on bielliptic genus-five curves and modular realizations establishes related geometric involution structures, but no exact characteristic-three Frobenius polynomial for this fixed model was located in the accessible material. General idempotent or Prym decomposition theorems are acknowledged as tools; the new point is their explicit arithmetic evaluation for the stated reduction, not the general decomposition.

## Limitations
This theorem concerns one specified \(\mathbb F_3\)-model; it neither classifies twists nor computes its full geometric automorphism group in characteristic three. The abelian surface is proved simple over \(\mathbb F_3\), not absolutely simple. The computational checks independently verify finite small-field assertions; the infinite extension-field formula instead follows from the proof. Searches and relevant accessible primary texts did not establish equivalent prior arithmetic coverage, but inaccessible older bielliptic literature and unindexed tables may still contain an equivalent calculation. No independent external mathematical audit has been performed.

## References
1. David Swinarski, *Equations of Riemann surfaces with automorphisms*, arXiv:1607.04778, initially public 2016-07-16, §4.3 and linked genus-five equation catalogue: https://arxiv.org/abs/1607.04778 ; https://faculty.fordham.edu/dswinarski/RiemannSurfaceAutomorphisms/genus-5.htm .
2. Momonari Kudo and Shushi Harashita, *Representation of non-special curves of genus 5 as plane sextic curves and its application to finding curves with many rational points*, arXiv:2102.07270, initially public 2021-02-14, especially §§1, 4.2, 5: https://arxiv.org/abs/2102.07270 .
3. Momonari Kudo and Shushi Harashita, *Genus-five hyperelliptic or trigonal curves with many rational points in characteristic three*, arXiv:2204.06805, initially public 2022-04-14, especially §§1 and 4: https://arxiv.org/abs/2204.06805 .
4. T. Kato, K. Magaard and H. Völklein, *Bi-elliptic Weierstrass points on curves of genus 5*, Indagationes Mathematicae 22 (2011), 116–130, DOI:10.1016/j.indag.2011.08.006 (related geometry; full text not accessible in this research pass).
