# Sharp collision-free threefold covering threshold for the finite-field cubic graph

## Finding
For a finite field \(F=\mathbb F_q\) of characteristic at least five, put \(C=\{(x,x^3):x\in F\}\) and let \(R_q^{\mathrm{dist}}(s,w)\) count **ordered** triples of pairwise distinct elements \(x,y,z\in F\) satisfying
\[
x+y+z=s,\qquad x^3+y^3+z^3=w.
\]
Then the restricted threefold sumset is the entire affine plane exactly when \(q\ge23\):
\[
\bigl\{(x+y+z,x^3+y^3+z^3):x,y,z\in F\ \text{pairwise distinct}\bigr\}=F^2
\quad\Longleftrightarrow\quad q\ge23.
\]
For \(q<23\) in the specified characteristics, the possible orders are \(q=5,7,11,13,17,19\). The following table specifies **every** missing target. For \(s=0\), the missing values \(w\) are in column \(Z_q\); for each \(s\ne0\), they are exactly \(w=s^3\lambda\) for \(\lambda\in T_q\).

| \(q\) | \(Z_q\) | \(T_q\) | Total missing targets |
|---|---|---|---:|
| 5 | 1, 2, 3, 4 | 0, 3, 4 | 16 |
| 7 | 1, 2, 5, 6 | 2, 3, 4 | 22 |
| 11 | empty | 3, 10 | 20 |
| 13 | 4, 6, 7, 9 | 2 | 16 |
| 17 | empty | 14 | 16 |
| 19 | 4, 6, 9, 10, 13, 15 | empty | 6 |

There is also an exact representation formula in every characteristic at least five. Let \(\chi:F\to\{-1,0,1\}\) be the quadratic character, with \(\chi(0)=0\), and put
\[
P_{s,w}(u)=u^2(u-2s)^2+\frac43(w-s^3)u,\qquad
h(s,w)=\#\{t\in F:s^3-6t(t-s)^2=w\}.
\]
Then
\[
\boxed{R_q^{\mathrm{dist}}(s,w)=q\mathbf1_{w=s^3}+q-1+
\sum_{u\in F}\chi(P_{s,w}(u))-3h(s,w)+2\mathbf1_{w=s^3/9}.}
\]
Every quantity on the right is explicitly finite. Away from a specified singular cubic, the character sum is the Frobenius trace of a genus-one curve, giving an all-field lower bound.

## Assumptions and scope
The field has \(q=p^f\) elements with \(p\ge5\) prime and \(f\ge1\); division by \(2,3,6,9\) is valid. The three summands are ordered and **pairwise distinct**. A target means any \((s,w)\in F^2\). The tabulated missing sets are subsets of prime fields, since these are all possible field orders below 23 in the permitted characteristics. No statement is made about characteristics two or three or about general coefficient polynomials.

## Proof
**1. Character-sum formula.** Fix \((s,w)\). Write \(u=x+y\) and \(z=s-u\). If \(u\ne0\), then
\[
3u(xy)=u^3+(s-u)^3-w.
\]
For each such \(u\), the ordered solutions \((x,y)\) are the roots of \(X^2-uX+xy\), hence there are \(1+\chi(u^2-4xy)\). Multiplication by the nonzero square \(u^2\) changes the discriminant into \(P_{s,w}(u)\). For \(u=0\), one has \(x=-y\) and \(z=s\); there are \(q\) solutions exactly when \(w=s^3\). Since \(P_{s,w}(0)=0\), summation gives
\[
R_q(s,w)=q\mathbf1_{w=s^3}+q-1+\sum_{u\in F}\chi(P_{s,w}(u))
\]
for the unrestricted ordered count.

**2. Removing collisions.** A triple with \(x=y=t\) has \(z=s-2t\), and the cube moment is \(2t^3+(s-2t)^3=s^3-6t(t-s)^2\). Thus exactly \(h(s,w)\) triples have any one chosen equality among \(x=y\), \(y=z\), \(z=x\). The only intersection of two of these equality events has \(x=y=z=s/3\), which occurs exactly when \(w=s^3/9\). Inclusion-exclusion yields \(R_q^{\mathrm{dist}}=R_q-3h+2\mathbf1_{w=s^3/9}\). Because \(h\le3\), one has \(R_q^{\mathrm{dist}}\ge R_q-9\).

**3. A uniform positive bound for \(q\ge23\).** If \(w=s^3\), then \(P_{s,w}(u)=u^2(u-2s)^2\). The preceding formula gives \(R_q(s,w)=3q-2\) when \(s=0\), and \(3q-3\) otherwise.

Suppose \(w\ne s^3\). Write \(A=4(w-s^3)/3\), so
\[
P_{s,w}(u)=u\bigl(u(u-2s)^2+A\bigr),\qquad A\ne0.
\]
The cubic factor has a repeated root only if \(s\ne0\) and its critical point \(2s/3\) vanishes; equivalently \(A=-32s^3/27\), or \(w=s^3/9\). In this singular case
\[
P_{s,w}(u)=u\left(u-\frac{2s}{3}\right)^2\left(u-\frac{8s}{3}\right).
\]
The quadratic character identity \(\sum_u\chi(u(u-v))=-1\) for \(v\ne0\), together with removal of the value at the double root, gives
\[
R_q(s,w)=q-2-\chi(-3).
\]
Here \(\chi(-3)\) follows because the removed quadratic character is \(\chi((2s/3)(-2s))=\chi(-3)\).

In all other cases with \(w\ne s^3\), the quartic \(P_{s,w}\) is squarefree, so \(v^2=P_{s,w}(u)\) has a smooth genus-one projective model with exactly two rational points at infinity (its leading coefficient is a square). If \(t_E=q+1-\#E(F)\), Hasse's bound \(|t_E|\le2\sqrt q\) and the affine point count imply \(R_q(s,w)=q-2-t_E\ge q-2-2\sqrt q\). For \(q\ge23\), the last lower bound exceeds 9. The singular-case bound is at least \(q-3>9\), and the \(w=s^3\) count is larger still. Thus \(R_q^{\mathrm{dist}}(s,w)>0\) for every target.

**4. Sharpness and the small-field classification.** The six eligible field orders below 23 are prime. For each of these, exhaust the \(q^3\) ordered triples, tally by their sum and cube sum, and discard tuples containing a collision. The self-contained checker `verify_restricted_cubic.py` performs precisely this finite exhaustion and asserts equality of each missing-target set to the displayed scaled list. It separately checks the character-sum and collision formulas against independent triple enumeration. Every field below 23 has a missing target, while the preceding argument covers every larger allowed finite field. This proves the iff statement.

## Verification
Execute `python3 verify_restricted_cubic.py` with the Python standard library. It independently enumerates all ordered triples and compares both unrestricted and pairwise-distinct counts with the exact character/collision formulas on \(\mathbb F_q\) for \(q=5,7,11,13,17,19,23,29,31\), and also the quadratic extension fields \(\mathbb F_{25}\), \(\mathbb F_{49}\). It verifies 6,371 complete target fibers and all missing-target sets for the six small fields. The universal \(q\ge23\) statement follows from the proof and Hasse's bound, not from extrapolating the finite tests.

## Relationship to prior work
Moreland and Zieve (2013, arXiv:1304.1442) study the same paired sum-and-cube equations over rational numbers through positive-rank elliptic curves; their Section 6 develops an elliptic reduction, rather than the present finite-field pairwise-distinct covering threshold and complete exceptional-fiber calculation. Choudhry (2010) studies rational/integer equal-sum equal-cube Diophantine families. Existing general cubic-graph additive and Fourier results include unrestricted or twofold counts, which do not determine the collision-free threefold support: for example, \(q=19\) has six missing collision-free targets despite unrestricted threefold coverage. The novel assertion is the sharp restricted threshold and all-field multiplicity characterization, not the general link between cubic equations and genus-one curves.

## Limitations
This does not apply to characteristics two and three. The small-field list is a finite exact enumeration with the embedded verifier, not an independent conceptual classification of every exceptional fiber. The use of Hasse's bound gives positivity rather than an exact closed form for the elliptic Frobenius trace. Moreland--Zieve's elliptic setup is established prior work; an unlocated specialized restricted-sum theorem could alter historical priority. No independent mathematical audit has been performed.

## References
- Gwyneth Moreland and Michael E. Zieve, *Some Diophantine equations related to positive-rank elliptic curves*, arXiv:1304.1442 (first posted 2013-04-04), especially Section 6. https://arxiv.org/abs/1304.1442
- Ajai Choudhry, *Some Diophantine problems concerning equal sums of integers and their cubes*, Hardy--Ramanujan Journal **33** (2010), 59--70. https://doi.org/10.46298/hrj.2010.171
- H. Hasse, classical bound for the number of rational points on an elliptic curve over a finite field (\(|q+1-\#E(F)|\le2\sqrt q\)).
