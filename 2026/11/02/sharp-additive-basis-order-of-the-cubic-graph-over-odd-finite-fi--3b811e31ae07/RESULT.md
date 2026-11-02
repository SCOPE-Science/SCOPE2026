# Sharp additive basis order of the cubic graph over odd finite fields

## Finding

For a finite field \(F\) of odd cardinality \(q\), write
\[
C(F)=\{(t,t^3):t\in F\}\subseteq F^2,
\qquad hC(F)=\underbrace{C(F)+\cdots+C(F)}_{h\text{ summands}}.
\]
All sums are in the additive group of \(F^2\), repetition is permitted, and \(0\in C(F)\). The complete odd-characteristic classification is:

1. If \(\operatorname{char}F=3\), then \(hC(F)=C(F)\ne F^2\) for every positive integer \(h\).
2. If \(q=5\), then
   \[
   3C(F)=F^2\setminus\{(s,3s^3):s\in F^\times\},
   \qquad 4C(F)=F^2.
   \]
3. If \(q=7\), then
   \[
   3C(F)=F^2\setminus\{(0,2),(0,-2)\},
   \qquad 4C(F)=F^2.
   \]
4. For every other odd finite field (equivalently, \(q\ge11\) and \(\operatorname{char}F\ge5\)),
   \[
   3C(F)=F^2.
   \]

Moreover \(2C(F)\ne F^2\) for all such fields. Thus the least additive basis order is exactly \(4\) for \(q=5,7\), exactly \(3\) for \(q\ge11\) in characteristic at least \(5\), and does not exist in characteristic \(3\). No statement is made here about characteristic \(2\).

## Assumptions and scope

A finite field \(F\) is arbitrary except that its characteristic is odd. The proof includes nonprime finite fields. We count ordered sums only when checking membership; the theorem concerns the support of those sums, not their multiplicities. The curves in the proof are projective plane cubics over \(F\), and the classical Hasse bound for genus-one curves is used as an established theorem.

## Proof

**Reduction to a cubic.** For a prescribed target \((s,w)\in F^2\), choose \(x,y,z\in F\) with \(x+y+z=s\), hence \(z=s-x-y\). The identity
\[
x^3+y^3+(s-x-y)^3
=s^3-3(x+y)(x-s)(y-s)
\]
shows, in characteristic different from \(3\), that the target has a three-term representation precisely when the affine cubic
\[
(x+y)(x-s)(y-s)=c,\qquad c=(s^3-w)/3
\]
has an \(F\)-point.

If \(c=0\), the triple \((s,0,0)\) represents the target. If \(c=8s^3/27\), the triple \((s/3,s/3,s/3)\) represents the target.

**Smoothness in all other cases.** Assume now that the characteristic is at least \(5\), \(c\ne0\), and \(c\ne8s^3/27\). Let \(E\subset\mathbf P^2\) be
\[
(X+Y)(X-sZ)(Y-sZ)-cZ^3=0.
\]
It has exactly three rational points at infinity, namely
\[
[1:0:0],\quad[0:1:0],\quad[1:-1:0],
\]
and each is nonsingular: the three distinct linear factors of the leading homogeneous term meet the line at infinity transversely.

For a possible affine singularity, put \(U=x-s\), \(V=y-s\). Since \(c\ne0\), both \(U,V\) are nonzero, and vanishing of the two partial derivatives forces
\[
2U+V+2s=0,\qquad U+2V+2s=0.
\]
Subtracting gives \(U=V\), so \(U=V=-2s/3\). Substitution into the original equation gives \(c=8s^3/27\), contrary to assumption. Hence \(E\) is a smooth plane cubic of genus \(1\).

**Uniform covering.** By Hasse's bound,
\[
\#E(F)\ge q+1-2\sqrt q.
\]
For every integer \(q\ge11\) this lower bound exceeds \(3\), so \(E(F)\) has an affine point distinct from its three points at infinity. That point gives the required triple. Together with the two explicitly solved singular parameters, this proves \(3C(F)=F^2\) for every \(q\ge11\) with characteristic at least \(5\).

**Two small fields.** Over \(F_5\), direct evaluation of
\[
\{x^3+y^3+(s-x-y)^3:x,y\in F_5\}
\]
for \(s=0\) gives all five elements; for \(s=1\) it gives exactly \(\{0,1,2,4\}\). The substitutions \((x,y,z)\mapsto(tx,ty,tz)\) show that nonzero \(s\) is equivalent to \(s=1\) under \((s,w)\mapsto(ts,t^3w)\). The omitted targets are therefore exactly \((s,3s^3)\) for \(s\ne0\). Over \(F_7\), the corresponding value set at \(s=0\) is \(\{0,1,3,4,6\}\), while at \(s=1\) it is all of \(F_7\). Hence the only omitted targets are \((0,2)\) and \((0,-2)\).

For these two fields the complement of \(3C(F)\) has respectively \(4\) and \(2\) points, strictly fewer than \(\#C(F)=q\). For any \(v\in F^2\), the \(q\) distinct points of \(v-C(F)\) therefore cannot all lie in that complement; thus \(v\in 4C(F)\). This proves both fourfold covering assertions.

**Characteristic three and minimality.** If \(\operatorname{char}F=3\), Frobenius is additive: \((x+y)^3=x^3+y^3\). Therefore \(C(F)\) itself is a proper additive subgroup of \(F^2\), and \(hC(F)=C(F)\) for all \(h\ge1\). Finally, in any odd characteristic a sum of two graph points with first coordinate zero has second coordinate zero, since \(x+y=0\) implies \(x^3+y^3=0\). Therefore \((0,w)\notin2C(F)\) when \(w\ne0\), proving the claimed least orders. \(\square\)

## Verification

Run `python3 verify_cubic_graph.py` from the directory containing this document and the verifier. The verifier uses exact finite-field arithmetic, constructs the twofold and threefold sumsets independently, checks the missing targets over \(F_5\) and \(F_7\), checks fourfold covering there, and tests several larger prime and quadratic-extension fields. Its finite checks corroborate but do not establish the unrestricted claim. The infinite-field-order step is proved by the Hasse bound and the smoothness calculation above.

## Relationship to prior work

Cilleruelo's 2010 paper develops finite-field additive techniques and dense Sidon sets (including quadratic graph constructions), but its inspected statements do not give this exact threefold cubic-graph covering classification. Later work of Forey, Fresán and Kowalski develops symmetric Sidon sets from algebraic curves and generalized Jacobians; constraints on additive quadruples alone do not imply universal three-sum coverage. Carlet's 2022 maximal-Sidon-graph framework addresses **characteristic two**, which is deliberately excluded from this statement. A publicly archived calculation of the sharp fourth Fourier-extension moment for the same cubic graph concerns two-plus-two additive collisions and does not imply that every target is a sum of three graph points. The assertion of historical originality remains qualified by possible unlocated equivalent results.

## Limitations

This theorem does not count the number of representations of a target, identify sharp Fourier extension norms, or classify characteristic-two fields. Hasse's bound is cited as a standard theorem, not independently reproved. Finite computations cannot substitute for the genus-one argument. Historical priority has not been independently established, and no independent audit has been performed.

## References

- Javier Cilleruelo, *Combinatorial problems in finite fields and Sidon sets*, arXiv:1003.3576, first public 18 March 2010; primary MSC 11B30.
- Arthur Forey, Javier Fresán, Emmanuel Kowalski, *Sidon sets in algebraic geometry*, arXiv:2301.12878 (2023), Sections 1 and 3.
- Claude Carlet, *On APN Functions Whose Graphs are Maximal Sidon Sets*, LATIN 2022, DOI 10.1007/978-3-031-20624-5_15 (characteristic-two comparison).
- *Exact sharp finite-field cubic-graph L²-to-L⁴ extension norm and extremizers*, public research record (2026), https://github.com/Resultary/2026/tree/main/2026/10/4/SCOPE-exact-sharp-finite-field-cubic-graph-l-2-to-l-4-extension-norm-a--2db777d1e47b.
- Hasse's genus-one point-count bound, \(|\#E(F_q)-(q+1)|\le2\sqrt q\), standard theorem.
