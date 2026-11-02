# Exact Weil spectra and nonisomorphic isogenous genus-four curves in a reciprocal hyperelliptic family

## Finding

For \(p\in\{11,13\}\), define the smooth projective curve
\[
C_{p,a}:\quad y^2=x^9+a x^5+x,\qquad a\in\mathbf F_p,\quad a^2\ne4.
\]
All these curves have genus four. The Hasse–Weil numerator of every curve in this two-field family has the constrained form
\[
P_{p,a}(T)=\bigl(1+b_p(a)T^2+p^2T^4\bigr)^2.
\]
The following are the **complete** coefficient values, with one row for every admissible parameter:

| \(p\) | \(a\) | \(b_p(a)\) |
| --- | --- | --- |
| 11 | 0, 1, 3, 4, 5, 6, 7, 8, 10 | 0, 6, 10, -2, 16, -16, 2, -10, -6 |
| 13 | 0, 1, 3, 4, 5, 6, 7, 8, 9, 10, 12 | 0, 6, -10, -16, -10, 14, -14, 10, 16, 10, -6 |

In characteristic 11 all nine parameters have pairwise different zeta functions. In characteristic 13, exactly two distinct-parameter pairs have the same zeta function: \(\{3,5\}\), with \(b=-10\), and \(\{8,10\}\), with \(b=10\). The members of **each** pair are geometrically nonisomorphic (over an algebraic closure) but have isogenous Jacobians over \(\mathbf F_{13}\). Every listed curve satisfies \(\#C_{p,a}(\mathbf F_p)=p+1\) and \(\#C_{p,a}(\mathbf F_{p^3})=p^3+1\). The zeta numerator determines all other extension-field point counts. This is a classification of this fixed normalized family, not of all genus-four curves.

## Assumptions and scope

Everything is over a finite field of odd characteristic \(p\in\{11,13\}\). A curve is understood as the smooth projective model of the affine equation. Put \(h_a(x)=x^8+a x^4+1\). Its roots are distinct and nonzero if and only if \(a^2\ne4\): the quadratic \(z^2+az+1\) has distinct nonzero roots and \(x\mapsto x^4\) is separable in these characteristics. Hence \(x h_a(x)\) is squarefree of degree nine, and the smooth model has genus four.

The Hasse–Weil convention is
\[
Z(C,T)=\frac{P_C(T)}{(1-T)(1-pT)},\qquad
P_C(T)=\exp\Bigl(\sum_{n\ge1}\frac{p^n+1-\#C(\mathbf F_{p^n})}{n}(-T^n)\ \text{with the standard Newton-sign convention}\Bigr).
\]
More explicitly, if \(s_n=p^n+1-\#C(\mathbf F_{p^n})\) are Frobenius power sums and \(P=1+c_1T+\cdots\), then \(k c_k=-\sum_{j=1}^k c_{k-j}s_j\) and \(c_0=1\). This recurrence fixes all signs without relying on the displayed exponential mnemonic.

## Proof

**1. Explicit genus-two quotients.** The hyperelliptic involution \(\iota:(x,y)\mapsto(x,-y)\) and the reciprocal involution \(\sigma:(x,y)\mapsto(x^{-1},y/x^5)\) commute. Introduce \(t=x+x^{-1}\). Under \(\sigma\), the invariant \(v_+=y(x+1)/x^3\) satisfies
\[
v_+^2=(t+2)(t^4-4t^2+2+a).
\]
Under \(\iota\sigma\), the invariant \(v_-=y(x-1)/x^3\) satisfies
\[
v_-^2=(t-2)(t^4-4t^2+2+a).
\]
These are smooth genus-two curves \(D_{p,a,+}\) and \(D_{p,a,-}\), since the reciprocal transformations give degree-two quotient maps of a smooth genus-four curve with the corresponding four fixed points. The standard eigenspace or Kani–Rosen decomposition for the Klein-four group gives an \(\mathbf F_p\)-isogeny
\[
\operatorname{Jac}(C_{p,a})\sim_{\mathbf F_p}
\operatorname{Jac}(D_{p,a,+})\times\operatorname{Jac}(D_{p,a,-}).
\]
Here \(C/\langle\iota\rangle\) has genus zero, and the two remaining genus-two quotients account for all genus-four holomorphic differentials. The isogeny has degree a power of two, hence is separable in the stated characteristics.

**2. Relation between the two quotients.** Substituting \(t\mapsto-t\) carries the \(+\) equation into the negative of the \(-\) equation. Thus the two genus-two curves are quadratic twists by \(-1\). In characteristic 13, \(-1\) is a square, so the quotients are isomorphic over the base field. In characteristic 11, \(-1\) is a nonsquare. For every admissible \(a\), exact finite-field enumeration (the second verifier) gives
\[
\#D_{11,a,+}(\mathbf F_{11})=12,
\]
and in fact its Weil numerator has zero odd coefficients. Therefore its quadratic twist has the *same* Weil polynomial. Both cases give
\[
P_{C_{p,a}}(T)=P_{D_{p,a,+}}(T)^2.
\]

**3. Exact finite quotient census.** Count solutions of \(v^2=f(t)\) over \(\mathbf F_p\) and \(\mathbf F_{p^2}\) by the elementary character sum \(1+\sum_{t}\chi(f(t))\). The independent standalone enumerator `verify_quotients.py` loops over the full \(p-2\) admissible parameter sets, both quotient signs, and every field element. It verifies
\[
\#D_{p,a,+}(\mathbf F_p)=p+1,
\qquad
\#D_{p,a,+}(\mathbf F_{p^2})=p^2+1+2b_p(a),
\]
with precisely the tables above, and also verifies identical counts for the minus quotient. For a genus-two curve, the functional equation and Newton identities imply from these two counts the **entire** numerator
\[
P_{D_{p,a,+}}(T)=1+b_p(a)T^2+p^2T^4.
\]
This proves every genus-four numerator and every table value, because the enumerator ranges over the complete finite parameter sets. No unexamined higher extension degree is needed.

**4. Geometric nonisomorphism and finite-field isogeny.** For the normalized reciprocal family, the geometric isomorphism criterion of Ohashi–Kudo, Proposition 3.2.4, implies \(C_{p,a}\cong_{\overline{\mathbf F}_p}C_{p,a'}\) if and only if \(a^2={a'}^2\). Indeed, in their parameters \(\lambda+\lambda^{-1}=a^2-2\), and the criterion is equality up to \(\lambda\leftrightarrow\lambda^{-1}\). In \(\mathbf F_{13}\), the collision pairs obey \(3^2\ne5^2\) and \(8^2\ne10^2\). They are therefore geometrically nonisomorphic. Their equal Weil numerators imply base-field isogeny of their Jacobians by the Tate–Honda isogeny criterion. This proves the asserted arithmetic collisions rather than merely equality of initial point counts.

**5. Other point counts.** Since every numerator is an even polynomial, every odd Frobenius power sum vanishes. In particular the rational point counts over degrees one and three are \(p+1\) and \(p^3+1\), respectively. All degrees follow recursively from the known numerator.

## Verification

Execute `python3 verify_quotients.py` (pure Python standard library), which prints `QUOTIENT_REPLAY_OK`. It independently constructs \(\mathbf F_{p^2}\) from the quadratic nonsquares \(-1\) for \(p=11\) and \(-2\) for \(p=13\), enumerates both quintic genus-two quotients, checks the complete table and collisions, and tests nonsquareness.

Execute `python3 verify_direct.py` (also standard library), which prints `DIRECT_REPLAY_OK`. It uses polynomial-basis finite-field arithmetic, verifies irreducibility of its explicit extension-field moduli, and directly counts \(C_{p,a}(\mathbf F_{p^n})\) for every admissible \(a\) and \(n=1,2,3,4\). It reconstructs the genus-four Weil polynomial with Newton identities and the genus-four functional equation; **all** outputs agree with the independently computed squared genus-two formulas. The `spectrum.csv` file supplies all parameter values and the first four point counts. Direct enumeration is finite and exact; the genus-two decomposition and functional equations justify extrapolation to all extension degrees.

## Relationship to prior work

S. A. Novoselov, *Counting points on hyperelliptic curves of type \(y^2=x^{2g+1}+ax^{g+1}+bx\)*, arXiv:1902.05992 (first public version February 15, 2019), develops algorithms and Dickson-polynomial quotient methods for precisely this broad family. The quotient construction and general point-count strategy are therefore **prior knowledge**, not claimed as new. His inspected paper provides possible characteristic polynomials modulo \(p\) and algorithms, not the complete exact paired \(p=11,13\) spectrum or these two explicit geometrically nonisomorphic, same-zeta pairs.

R. Ohashi and M. Kudo, *Computing superspecial hyperelliptic curves of genus 4 with automorphism group properly containing the Klein 4-group*, arXiv:2312.16858 (first public December 28, 2023), establish the reciprocal family, isomorphism criterion and superspeciality algorithms. Their results, including Proposition 3.2.4, are essential inputs. Their inspected results do not list the above complete Weil spectra at 11 and 13. The **new finite arithmetic classification** is the exact table and its pairwise isogeny/nonisomorphism consequences, not the geometry or existence of the family itself.

## Limitations

The census concerns only \(p=11,13\) and the coefficient-normalized family with \(a^2\ne4\), not arbitrary genus-four curves or all twists of these geometric classes. Isogeny is an isogeny of unpolarized Jacobians over \(\mathbf F_{13}\); it is **not** an isomorphism of principally polarized Jacobians. Two relevant primary papers were compared by their mathematical implications; priority against all unpublished or unindexed numerical tables is not certified. The computations establish exhaustive finite counts only over the explicitly enumerated finite parameter spaces, while the genus-two quotient argument provides the all-degrees implication.

## References

1. S. A. Novoselov, *Counting points on hyperelliptic curves of type \(y^2=x^{2g+1}+ax^{g+1}+bx\)*, arXiv:1902.05992 (2019), https://arxiv.org/abs/1902.05992; published *Finite Fields and Their Applications* 68 (2020), 101757.
2. R. Ohashi and M. Kudo, *Computing superspecial hyperelliptic curves of genus 4 with automorphism group properly containing the Klein 4-group*, arXiv:2312.16858 (2023), https://arxiv.org/abs/2312.16858, Proposition 3.2.4.
3. J. Tate, *Endomorphisms of abelian varieties over finite fields*, *Inventiones Mathematicae* 2 (1966), 134–144 (isogeny classification by Frobenius).
