# Four-gonal genus-four curves over every finite field

## Finding

**Theorem.** For every finite field \(k=\mathbf F_q\), there exists a smooth, geometrically integral, projective curve \(C/k\) of genus \(4\) and **\(k\)-gonality exactly \(4\)**. An explicit canonical complete intersection \(C=V(Q,F)\subset\mathbf P^3_k\) can be chosen in every characteristic, as follows. Use homogeneous coordinates \([X:Y:Z:W]\).

* When \(\operatorname{char}(k)\ge5\), choose any nonsquare \(c\in k^\times\) and take
  \[
  Q=XY+Z^2-cW^2,\qquad F=X^3+Y^3+W^3.
  \]
* When \(\operatorname{char}(k)=3\), choose any nonsquare \(c\in k^\times\) and take
  \[
  Q=XY+Z^2-cW^2,\qquad
  F=X^3+Y^3+Z^2W+XW^2-YW^2+ZW^2.
  \]
* When \(\operatorname{char}(k)=2\), choose \(a\in k\) with \(\operatorname{Tr}_{k/\mathbf F_2}(a)=1\) and take
  \[
  Q=XY+Z^2+ZW+aW^2,\qquad
  F=X^3+Y^3+Z^2W+X^2W.
  \]

In each case the quadric is nonsplit over \(k\), the complete intersection is geometrically smooth, and the curve contains the \(k\)-point \([1:-1:1:0]\) when \(\operatorname{char}(k)\ne2\) and \([1:1:1:0]\) when \(\operatorname{char}(k)=2\). The theorem settles the genus-four existence case of Question 1.3 of Faber--Grantham--Howe (2022 preprint), which asked for a genus-\(g\) curve of gonality \(g\) over each finite field.

## Assumptions and scope

The field is an **arbitrary** finite field, of any prime-power cardinality. Gonality means the minimum degree of a morphism \(C\to\mathbf P^1\) **defined over \(k\)**, rather than geometric gonality over an algebraic closure. The theorem is existential; it does not classify all genus-four curves, their isomorphism classes, or their arithmetic zeta functions. The three formulas are characteristic-specific, but require no search for a cubic.

## Proof

**1. The ambient quadrics are nonsplit.** In odd characteristic, \(Z^2-cW^2\) is an anisotropic binary quadratic form because \(c\) is a nonsquare. In characteristic two, \(Z^2+ZW+aW^2\) is anisotropic because \(T^2+T+a\) has no root in \(k\) exactly when \(\operatorname{Tr}_{k/\mathbf F_2}(a)=1\). In either case \(Q\) is the orthogonal sum of a hyperbolic plane \(XY\) and an anisotropic plane. Hence it is a nonsingular quadric surface of Witt index one, and has no \(k\)-rational lines or \(k\)-rational ruling; over \(\overline{k}\) it is \(\mathbf P^1\times\mathbf P^1\).

**2. Smoothness in odd characteristic at least five.** Suppose \(Q=F=0\) is singular. Since \(Q\) is smooth, its gradient and that of \(F\) would be linearly dependent. The gradient \(\nabla F=(3X^2,3Y^2,0,3W^2)\) cannot vanish on \(Q\), so \(\nabla F=\lambda\nabla Q\) with \(\lambda\ne0\). Its \(Z\)-component gives \(Z=0\). If \(W=0\), the equations \(XY=0\) and \(X^3+Y^3=0\) leave no projective point. Thus normalize \(W=1\). Now \(XY=c\); the \(W\)-component gives \(\lambda=-3/(2c)\), and the \(X\)- and \(Y\)-components yield \(X^3=Y^3=-1/2\). Thus \(c^3=X^3Y^3=1/4\), impossible: \(c^3\) is a nonsquare and \(1/4\) is a square. There is no geometric singularity.

**3. Smoothness in characteristic three.** At \(W=0\), the curve equations become \(XY+Z^2=0\) and \((X+Y)^3=0\). Every projective solution has \(X\ne0\), \(Y=-X\), and \(Z^2=X^2\ne0\). At such a point the \(W\)-component of \(\nabla F\) equals \(Z^2\ne0\), whereas that of \(\nabla Q\) is zero: the gradients cannot be proportional. At \(W\ne0\), put \(W=1\), \(X=x\), \(Y=y\), and \(Z=z\). On this chart the cubic equation is
\[
(x+y)^3+z^2+x-y+z=0.
\]
If the gradients were proportional, the nonzero \(X\)- and \(Y\)-components \((1,-1)\) of \(\nabla F\) imply \(x=-y\) and \(y\ne0\). The \(Z\)-component then implies \(y(1-z)=-z\). The cubic equation reduces to \(y=-z^2-z\). Substitution gives \(z^3=0\), hence \(z=y=0\), contradiction. This proves smoothness for every nonzero \(c\), in particular for nonsquares.

**4. Smoothness in characteristic two.** At \(W\ne0\), set \(W=1\). The \(Z\)-partial derivative of \(Q\) is \(1\), whereas the \(Z\)-partial derivative of \(F\) is zero. Linear dependence of the gradients therefore forces \(\nabla F=0\), i.e. \(X=Y=Z=0\). The equation \(Q=0\) would give \(a=0\), contrary to the trace-one hypothesis. At \(W=0\), the two equations are \(XY+Z^2=0\), \(X^3+Y^3=0\). Thus \(X,Y,Z\) are nonzero. After scaling \(Y=1\), write \(X=t\), so \(t^3=1\) and \(Z=t^2\). The two gradients there are
\[
\nabla Q=(1,t,0,t^2),\qquad
\nabla F=(t^2,1,0,t+t^2).
\]
Proportionality would force the scalar \(t^2\) from the first coordinate and then \(t+t^2=t^2t^2=t\) from the fourth coordinate, implying \(t^2=0\). Contradiction. Thus the intersection is geometrically smooth.

**5. Genus and irreducibility.** In every characteristic \(Q\) is a smooth quadric and \(F\) does not contain \(Q\). On \(Q_{\overline{k}}\cong\mathbf P^1\times\mathbf P^1\), the intersection is a smooth divisor of class \((3,3)\). Such a divisor is connected (any decomposition into nonempty effective components has positive intersection), and smoothness therefore makes it geometrically integral. By adjunction,
\[
\omega_C\cong\mathcal O_C(1),\qquad \deg\omega_C=6,\qquad g(C)=4.
\]
The embedding in \(\mathbf P^3\) is the complete canonical embedding, and \(Q\) is the unique quadric containing it.

**6. Gonality.** The classification of canonical quadrics for genus-four curves (Faber--Grantham, Lemma 5.1) shows that a \(k\)-rational degree-three pencil would give a \(k\)-rational ruling of the unique canonical quadric, or a quadric cone; both are excluded by the nonsplit smooth \(Q\). The canonical embedding also excludes degree-one and degree-two maps. Hence \(\operatorname{gon}_k(C)\ge4\). The explicitly displayed \(k\)-rational point \(P\) gives \(h^0(C,\omega_C(-2P))\ge h^0(C,\omega_C)-2=2\), so a pencil of degree at most \(\deg\omega_C-2=4\) exists by Riemann--Roch. Consequently \(\operatorname{gon}_k(C)=4\).

## Verification

The accompanying `verify.py` uses exact Gröbner-basis calculations over prime fields on all four affine projective charts. It checks that the ideal generated by \(Q\), \(F\), and all \(2\times2\) Jacobian minors is the unit ideal in the cases \((p,c)=(2,1),(3,2),(5,2),(7,3),(11,2)\), and checks the displayed rational point in each case. All checks passed. These finite sample calculations corroborate the **all-field algebraic proof above**, and are not substituted for that proof. For general extension fields, the trace-one and nonsquare hypotheses ensure the required anisotropic binary form.

## Relationship to prior work

Faber, Grantham and Howe, *On the Maximum Gonality of a Curve over a Finite Field* (arXiv:2207.14307, first released July 28, 2022), Question 1.3, ask whether for each genus and each finite field there is a curve whose gonality equals its genus. They observe that this is known for genus four over fields of cardinality at most four, and suggest looking for smooth cubic sections of nonsplit quadrics over odd fields, without providing a uniform existence proof. Their theorem about the upper bound and exceptional higher gonality does not imply existence of degree-four gonality curves. The present theorem supplies an explicit smooth cubic section **for every field**, including characteristic two and characteristic three extensions.

Faber and Grantham, *Binary Curves of Small Fixed Genus and Gonality with Many Rational Points* (arXiv:2005.07054), Lemma 5.1, give the canonical quadric / trigonal-pencil classification used here. Their Theorem 5.3 gives a particular binary genus-four curve of gonality four, which is not asserted to be newly discovered here. The contribution is a single constructive existence theorem uniform across all finite fields. No claim of priority is made beyond the inspected sources; an unindexed equivalent construction remains possible.

## Limitations

The theorem is about \(k\)-gonality, not geometric gonality (over \(\overline{k}\), these curves are trigonal). The result neither counts curves nor proves any novelty beyond the explicit universal existence theorem. Published-literature coverage remains a bibliographic risk and no independent mathematical audit has been performed. The verification script checks selected prime fields and the proof covers every prime power.

## References

1. X. Faber, J. Grantham and E. W. Howe, *On the Maximum Gonality of a Curve over a Finite Field*, arXiv:2207.14307, initial release 2022-07-28, Question 1.3 and Theorem 1.1, https://arxiv.org/abs/2207.14307 .
2. X. Faber and J. Grantham, *Binary Curves of Small Fixed Genus and Gonality with Many Rational Points*, arXiv:2005.07054, initial release 2020-05-14, Lemma 5.1 and Theorem 5.3, https://arxiv.org/abs/2005.07054 .
