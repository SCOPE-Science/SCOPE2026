# Exact embedding dimension seven for a genus-three zero-Wahl-defect singularity

## Finding

Let \(C\) be the smooth genus-three hyperelliptic curve \(z^2=x^7-1\), with \(p\) its unique point at infinity, and let \(A=\mathcal O_C(p)\). Set \(k=2\), and let \(\zeta\in H^1(C,A^2)\) be the class represented near \(p\) by \(t^{-5}\), where \(x=t^{-2}\). Let \((V_\zeta,0)\) be the normal complex surface singularity obtained by contracting the zero section of the Park–Shin nonlinear neighborhood associated with \((C,A,k,\zeta)\). Then

\[
\operatorname{edim}(V_\zeta,0)=\dim_{\mathbb C}\mathfrak m/\mathfrak m^2=7.
\]

By the established properties of this construction, \(V_\zeta\) has Wahl defect zero and is neither \(\mathbb Q\)-Gorenstein nor quasi-homogeneous. Its minimal embedding dimension is therefore exactly seven, strengthening the published lower bound six for this concrete first genus-three member.

## Assumptions and scope

All analytic spaces and completed local rings are over \(\mathbb C\). On \(U=C\setminus\{p\}\), set \(u=y_U\). On a disc around \(p\), choose the local parameter \(t\) and put \(v=y_W\). The bundle gluing is \(a_U=t a_W\) and the nonlinear fiber-coordinate gluing is

\[
v=t^{-1}u(1+2t^{-5}u^2)^{-1/2}.
\]

Near \(p\), \(z=t^{-7}\sqrt{1-t^{14}}\), with the holomorphic square root taking the value one at zero. Denote the completed local ring of the contracted germ by \(\widehat R\) and the filtration by vanishing order along \(C\) by \(F^j\). In the associated graded algebra \(J=\operatorname{gr}_F\widehat R\), a symbol \(fT^j\) denotes a section \(f\in H^0(C,A^j)\) in graded degree \(j\); \(T\) is only bookkeeping, not necessarily a ring element.

## Proof

**1. Extendible coefficients.** The canonical bundle is \(K_C\simeq A^4\). The residue functional of \(\zeta=[t^{-5}]\) on \(H^0(C,A^2)=\langle1,x\rangle\) takes the constant coefficient. Park–Shin, Lemma 8.4, therefore gives

\[
J_1=0,\qquad J_2=\mathbb C\cdot xT^2,\qquad
J_j=H^0(C,A^j)T^j\quad(j\ge3).
\]

The pole semigroup at \(p\) is \(\langle2,7\rangle\). Thus the \(j\)-th graded space has basis \(x^aT^j\) for \(2a\le j\) and, when \(j\ge7\), \(x^azT^j\) for \(2a+7\le j\); in degree two only \(xT^2\) remains. In particular \(J_2,J_3,J_4,J_5,J_6,J_7\) have respective dimensions \(1,2,3,3,4,5\).

**2. Seven formal functions generate.** The following seven leading coefficients have formal lifts:

\[
xT^2,\quad T^3,\quad xT^3,\quad T^4,\quad xT^4,\quad T^5,\quad zT^7.
\]

Choose lifts \(f_2,f_3,g_3,f_4,g_4,f_5,h_7\), respectively, invariant under the appropriate parity character for the involution \(u\mapsto-u\). Their expansions on \(U\) can be chosen to begin

\[
\begin{aligned}
f_2&=xu^2-2zu^4+O(u^6),& f_3&=u^3+O(u^7),\\
g_3&=xu^3-3zu^5+O(u^7),& f_4&=u^4+O(u^8),\\
g_4&=xu^4-4zu^6+O(u^8),& f_5&=u^5+O(u^9),\\
h_7&=zu^7+O(u^9).&&
\end{aligned}
\]

Indeed, for an initial coefficient \(f\) in degree \(q\), the coefficient \(a\) at order \(q+2\) is compatible across the overlap precisely when \(t^{q+2}(a+q t^{-5}f)\) is regular at \(p\). For \(f=x\) take \(a=-qz\), since \(t^{-7}-z\) is regular at \(p\); for \(f=1\) take \(a=0\), since \(t^{q-3}\) is regular for \(q\ge3\). Subsequent obstructions vanish because \(H^1(C,A^j)=0\) for \(j>4\). The involution gives parity-pure lifts. The degree-seven lift exists by the same cohomology vanishing.

The two cancellations

\[
f_2f_4-f_3g_3=zu^8+O(u^{10}),\qquad
f_2f_5-f_3g_4=2zu^9+O(u^{11})
\]

supply the missing graded initials \(zT^8\) and \(zT^9\) as polynomials in the seven lifts. The resulting nine initial elements generate all of \(J\): for \(x^aT^j\), repeatedly use \(xT^2\), handling remainders \(0,1,2\) with \(xT^2,xT^3,xT^4\), and all remainders \(\ge3\) with \(T^3,T^4,T^5\); for \(x^azT^j\), first use \((xT^2)^a\), then use \(zT^7,zT^8,zT^9\) for residual degrees \(0,1,2\), or \(zT^7\) times \(T^3,T^4,T^5\) for larger residual degrees. Here \(3,4,5\) generate every integer at least three under addition.

The complete-filtered-algebra lifting lemma (Park–Shin, Lemma 8.3) applied to these nine polynomial expressions therefore gives a surjection from the formal power series ring in the original **seven** lifts onto \(\widehat R\). Thus \(\operatorname{edim}\le7\).

**3. Seven cotangent classes are independent.** Since every nonconstant function has filtration degree at least two, the cotangent classes in degrees two and three contribute \(1+2=3\). In degree four, the initial products span just \(\langle x^2T^4\rangle\), so \(T^4,xT^4\) give two additional independent classes. In degree five the products of \(J_2\) and \(J_3\) span \(\langle xT^5,x^2T^5\rangle\); hence \(T^5\) gives a sixth class. These dimensions are genuine cotangent dimensions through degree six by Park–Shin Lemma 8.2, because \(\operatorname{Sym}^2J_2\longrightarrow J_4\) is injective.

In degree seven, \(zT^7\) gives a seventh independent cotangent class. To check the subtle cancellation issue, choose parity-pure lifts as above. A product in \(\mathfrak m^2\) has lowest possible degree four, and its terms beyond the lowest degree occur only two degrees later. The only products whose corrections can contribute in degree seven have initial degree five, necessarily in \(J_2J_3\). But the multiplication map \(J_2\otimes J_3\to J_5\) is injective, taking \(x\otimes1,x\otimes x\) to the independent coefficients \(x,x^2\). Thus no cancellation at degree five can uncover a new degree-seven leading term. Direct products of initial degree seven lie in the \(x\)-polynomial span \(\langle T^7,xT^7,x^2T^7,x^3T^7\rangle\), not the \(z\)-direction. Hence \(zT^7\notin\operatorname{gr}_F^7\mathfrak m^2\), and the cotangent space has dimension at least seven. Combined with the upper bound, this proves the theorem.

## Verification

The companion `verify.py` checks the pole-order bases through degree ninety, the nine-generator semigroup spanning property, the injective low-degree products and the exact coefficients in both cancellations. Run `python3 verify.py`; the expected output is `VERIFY_OK: sections/graded generators/leading cancellations/lower bound`. The script checks finite algebraic consequences; the proof for all degrees is the semigroup induction above, and existence of formal lifts uses cohomology rather than experimentation.

## Relationship to prior work

Park–Shin (arXiv:2610.21093v1), Proposition 8.6, compute a lower bound of six for their genus-three, zero-defect member but do not evaluate its embedding dimension exactly. Their Lemmas 8.2–8.4 provide essential published filtration and extension results. The present statement supplies the missing sharp upper bound and a seventh independent cotangent class. The related genus-two zero-defect example is a different contracted singularity and its embedding-dimension computation does not imply the genus-three value. Grauert and Fujiki provide general historical background to nonlinear contractions, not a verified computation of this explicit germ.

## Limitations

The theorem concerns this specified genus-three germ, not all hyperelliptic neighborhoods, all analytic structures with the same exceptional curve, or a classification of normal singularities of embedding dimension seven. Formal power series generators are not asserted to be convergent explicit polynomial equations. The small computational check cannot certify the analytic lifting lemmas, which are used as published results. An unlocated equivalent calculation in older literature remains possible. No independent mathematical audit has been performed.

## References

1. H. Park and D. Shin, *Nonlinear neighborhoods of smooth curves and arbitrarily negative Wahl defects*, arXiv:2610.21093v1, first public version 15 October 2026; §§2, 6, 8, especially Lemmas 6.1, 6.2, 8.2–8.4 and Proposition 8.6.
2. H. Grauert, *Über Modifikationen und exzeptionelle analytische Mengen*, Math. Ann. 146 (1962), cited for the contraction context by Park–Shin.
3. Bourbaki, *Commutative Algebra*, Chapter III, §2, no. 9, Proposition 11, as cited in Park–Shin Lemma 8.3 for filtered-generator lifting.
