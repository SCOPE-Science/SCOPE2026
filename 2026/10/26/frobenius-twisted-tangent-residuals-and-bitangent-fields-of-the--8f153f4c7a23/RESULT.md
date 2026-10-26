# Frobenius-twisted tangent residuals and bitangent fields of the characteristic-three Klein quartic

## Finding
Let \(C\) over \(\mathbb F_3\) be the plane quartic
\[
C:\quad F(X,Y,Z)=X^3Y+Y^3Z+Z^3X=0.
\]
Write \(\mathrm{Fr}_9([X:Y:Z])=[X^9:Y^9:Z^9]\) and let \(A([X:Y:Z])=[Y:Z:X]\). Define the morphism \(\Phi=A\circ\mathrm{Fr}_9\) on \(C\). For every geometric point \(P\in C\), the scheme-theoretic line intersection divisor satisfies
\[
(T_PC\cdot C)=3P+\Phi(P).
\]
The hyperflexes are exactly the fixed points of \(\Phi\); they are in bijection with the geometric bitangent lines. All \(28\) are explicitly parametrized by the distinct roots \(u\) of
\[
g(u)=u^{28}+u^{21}+1\in\mathbb F_3[u]
\]
via
\[
P(u)=[u:u^{-9}:1],\qquad L_u:\ X+u^3Y+u^{-27}Z=0.
\]
The Frobenius orbit degrees of the points and lines are \(1,3,6,6,6,6\). For every \(n\ge1\), their numbers of \(\mathbb F_{3^n}\)-rational members are
\[
N_n=1+3\mathbf 1_{3\mid n}+24\mathbf1_{6\mid n}.
\]
The zeta function of each *reduced* finite zero-dimensional scheme is
\[
Z(T)=\frac{1}{(1-T)(1-T^3)(1-T^6)^4}.
\]

## Assumptions and scope
The characteristic is \(3\); geometric points are taken over an algebraic closure of \(\mathbb F_3\). The quartic is the exact displayed cyclic model, with its indicated \(\mathbb F_3\)-structure. A hyperflex is a point with tangent intersection divisor \(4P\). A bitangent is a line whose intersection is twice an effective degree-two divisor, including the hyperflex case. Frobenius means the arithmetic operation of raising projective coordinates to the third power; the cycle partition does not distinguish arithmetic from geometric Frobenius since orbit sizes are unchanged. The zeta functions concern the reduced subschemes, not any unspecified infinitesimal scheme structures.

## Proof
The partial derivatives are \(F_X=Z^3\), \(F_Y=X^3\), and \(F_Z=Y^3\), so the curve is smooth. At \(P=[a:b:c]\) its tangent is \(c^3X+a^3Y+b^3Z=0\). In characteristic \(3\), the expansion of \(F(P+tQ)\) along a tangent direction has no quadratic term, so the tangent meets \(C\) at \(P\) with multiplicity at least \(3\).

The cyclic permutation preserves \(F\), and \(F(\Phi(P))=F(P)^9=0\). Also the tangent equation evaluated at \(\Phi(P)=[b^9:c^9:a^9]\) is \(c^3b^9+a^3c^9+b^3a^9=F(P)^3=0\). Thus \(\Phi(P)\in T_PC\cap C\). If \(\Phi(P)\ne P\), degree-four Bézout gives \((T_PC\cdot C)=3P+\Phi(P)\); if they coincide, it gives \(4P\). A line cannot be tangent at two distinct points, because each would contribute multiplicity at least \(3\) to a degree-four intersection. It follows that every bitangent must be a hyperflex tangent and every hyperflex tangent is a bitangent; the assignment \(P\mapsto T_PC\) is injective on hyperflexes.

A fixed point of \(\Phi\) has \(Z\ne0\): if \(Z=0\), the third coordinate of \(\Phi(P)\) forces \(X=0\), but \(\Phi([0:1:0])=[1:0:0]\). Write \(P=[u:v:1]\). Proportionality of \([v^9:1:u^9]\) with \([u:v:1]\) yields \(u\ne0\), \(v=u^{-9}\), and \(u^{91}=1\). Substitution into \(F=0\) gives \(u^{-6}+u^{-27}+u=0\), equivalent to \(g(u)=u^{28}+u^{21}+1=0\). Conversely, the exact identity \(g(u)\mid(u^{91}-1)\) over \(\mathbb F_3\), verified by polynomial division in the attached standalone checker, ensures every root gives a fixed point. The tangent formula yields \(L_u\).

The polynomial factors in \(\mathbb F_3[u]\) as
\[
\begin{aligned}
g(u)={}&(u-1)(u^3-u-1)(u^6+u^4+u^3+1)\\
&\cdot(u^6+u^5-u^3+u^2+u+1)\\
&\cdot(u^6+u^5+u^4+u^3+u^2+u+1)\\
&\cdot(u^6-u^5+u^4-u^2+u+1).
\end{aligned}
\]
All factors are irreducible over \(\mathbb F_3\). This can be checked by polynomial multiplication and the standard finite-field irreducibility criterion: for each monic factor \(h\) of degree \(d\), verify \(u^{3^d}\equiv u\pmod h\) and \(\gcd(h,u^{3^{d/r}}-u)=1\) for each prime \(r\mid d\). The attached checker evaluates every identity using modular polynomial arithmetic. Additionally, \(g'(u)=u^{27}\), relatively prime to \(g\), so the \(28\) roots are simple and the reduced fixed-point scheme is finite étale. Since \(P\mapsto T_PC\) is Frobenius-equivariant and bijective on these \(28\) points, both configurations have the stated Frobenius cycles. The rational counts and zeta functions follow from the orbit degrees.

## Verification
Run the self-contained Python standard-library artifact `verification.py` with Python 3.8 or later. It implements polynomial addition, multiplication, exact division, GCD, modular exponentiation, and Rabin irreducibility checks over \(\mathbb F_3\). It reproduces the six irreducible factors, their product, separability, the identity \(g\mid(u^{91}-1)\), and the formula for \(\mathbb F_{3^n}\) for sample extension degrees. Expected final output begins `VERIFY_OK`. The universal claim is proved by the divisor and polynomial arguments above, not by checking a finite collection of extension degrees.

## Relationship to prior work
Oyono–Ritzenthaler (2010, Section 2, pp. 3–4) explicitly identify the exceptional characteristic-three Klein/Fermat geometric isomorphism class and its \(28\) hyperflexes and bitangents. Those *geometric totals* are not new. Meagher–Top (2010, Section 4) note that the characteristic-three cyclic Klein model is a twist of the Fermat quartic. Their Section 8 study of the Klein curve expressly assumes characteristic different from \(2,3,7\) and therefore does not imply the particular characteristic-three bitangent orbit type calculated here. Elkies treats the classical Klein quartic and a distinct Fermat-related reduction over \(\mathbb F_3\); geometric equivalence does not imply equal fields of definition for the fixed cyclic model. The contribution here is the explicit twisted-Frobenius residual-tangent formula together with the exact arithmetic descent and zeta function for its reduced bitangent configuration.

## Limitations
This result concerns this one model over \(\mathbb F_3\), not all twists, and the *reduced* hyperflex and bitangent configurations; it does not assert any structure for potential nonreduced parameter schemes. The critical polynomial factorizations are fully replayable, but an independent audit of the scientific result and exhaustive historical novelty certification have not been performed. Specialized historical arithmetic tables could contain the same orbit data in a different representation.

## References
1. R. Oyono and C. Ritzenthaler, *On rationality of the intersection points of a line with a plane quartic* (2010), arXiv:1006.0873, https://arxiv.org/pdf/1006.0873.
2. S. Meagher and J. Top, *Twists of genus three curves over finite fields*, Finite Fields Appl. **16** (2010), 347–368, https://doi.org/10.1016/j.ffa.2010.06.001; open text https://home.mathematik.uni-freiburg.de/arithgeom/TwistsGenThreeCurve.pdf.
3. N. D. Elkies, *The Klein quartic in number theory*, in *The Eightfold Way: The Beauty of Klein's Quartic Curve* (1999), https://people.math.harvard.edu/~elkies/papers/klein.pdf.
