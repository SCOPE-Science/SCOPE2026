# The marked \(\mu_6\)-action on bielliptic Picard bitangents has orbit type \(1+3+4\cdot6\)
## Finding
Let \(k\) be an algebraically closed field of characteristic different from \(2\) and \(3\). For the smooth bielliptic Picard quartic
\[
C_{a,b}:\quad Y^3Z=X^4+aX^2Z^2+bZ^4,
\qquad b(a^2-4b)\ne0,
\]
use the marked action
\[
\zeta\cdot(x,y)=(\zeta^3x,\zeta^4y)
\]
of \(\mu_6\). Its action on the 28 bitangents has orbit decomposition
\[
28=1+3+4\cdot6.
\]
The unique fixed bitangent is \(Z=0\). The unique size-three orbit is
\[
Y=cZ,\qquad c^3=b-\frac{a^2}{4},
\]
and every remaining bitangent has trivial stabilizer in \(\mu_6\).

Equivalently, the 28 odd theta characteristics have the same orbit decomposition. Under the bitangent-to-two-torsion correspondence of Laga--Shnidman, the 12 pairs under the bielliptic involution \(\tau\) identify with \(A[2]\setminus A[\widehat\lambda]\); these 12 points split into four free \(\mu_3\)-orbits of size three.

## Assumptions and scope
The statement concerns the distinguished marked \(\mu_6\)-action, not necessarily the full automorphism group of the curve. This distinction matters on the special locus \(a=0\), where the geometric automorphism group is larger. The smoothness hypothesis \(b(a^2-4b)\ne0\) is essential. All assertions are geometric, after base change to an algebraic closure, and characteristic \(2\) and \(3\) are excluded.

## Proof
Write \(\sigma\) for the order-three element \((x,y)\mapsto(x,\omega y)\) and \(\tau\) for the involution \((x,y)\mapsto(-x,y)\). Laga--Shnidman prove that \(\tau\) fixes exactly four bitangents: the line at infinity and the three horizontal lines \(Y=cZ\) with \(c^3=b-a^2/4\). They also prove that the other 24 bitangents form 12 \(\tau\)-orbits of size two.

It remains to determine the fixed bitangents of \(\sigma\). A line with coefficient vector \([A:B:C]\) is fixed setwise by \([X:Y:Z]\mapsto[X:\omega Y:Z]\) exactly when either \(B=0\) or \(A=C=0\). Thus a \(\sigma\)-invariant line is either \(Y=0\) or belongs to the pencil \(AX+CZ=0\).

The line \(Z=0\) is a bitangent: its intersection with \(C_{a,b}\) is the divisor \(4\infty\). The line \(Y=0\) is not a bitangent, because its intersection polynomial is
\[
X^4+aX^2Z^2+bZ^4,
\]
which has four distinct roots under \(b(a^2-4b)\ne0\). For a finite line \(X=uZ\), the restriction of the quartic equation is
\[
Z\bigl(Y^3-(u^4+au^2+b)Z^3\bigr)=0.
\]
If \(u^4+au^2+b\ne0\), the intersection consists of four simple points; if it vanishes, the multiplicity profile is \(1+3\). Neither is an even divisor. Hence \(Z=0\) is the only \(\sigma\)-fixed bitangent.

Let \(n_d\) be the number of \(\mu_6\)-orbits of size \(d\). Since the order-three subgroup fixes exactly one bitangent,
\[
n_1+2n_2=1.
\]
Since the order-two subgroup fixes exactly four,
\[
n_1+3n_3=4.
\]
The unique line fixed by all of \(\mu_6\) is \(Z=0\), so \(n_1=1\). Finally
\[
n_1+2n_2+3n_3+6n_6=28.
\]
These equations give
\[
(n_1,n_2,n_3,n_6)=(1,0,1,4).
\]
Because \(b-a^2/4\ne0\), the three horizontal bitangents are distinct, and \(\sigma\) cycles them, so they are precisely the size-three orbit.

For the final assertion, Laga--Shnidman's map from a non-\(\tau\)-fixed bitangent \(\ell\) to the associated point of \(A[2]\setminus A[\widehat\lambda]\) factors through the \(\tau\)-pair \(\{\ell,\tau\ell}\). The construction is \(\mu_3\)-equivariant because \(\mu_3\) commutes with \(\tau\), fixes \(\infty\), and acts compatibly on the Jacobian and the projection to \(A\). Each free \(\mu_6\)-orbit therefore descends to a free three-cycle on \(\tau\)-pairs, giving four such three-cycles.

## Verification
The proof uses the source's exact count of \(\tau\)-fixed bitangents and then an independent classification of the \(\sigma\)-invariant projective lines. The accompanying checker verifies the horizontal square identity, the discriminant of the \(Y=0\) section, the vertical-line restriction, and the orbit-count equations. Re-execution of the embedded checker returns

`VERIFY_OK orbit=1+3+4x6 mu3_fixed=1 tau_fixed=4 prym_pairs=4x3`.

## Relationship to prior work
Laga--Shnidman introduce the marked \(\mu_6\)-action and prove that the bielliptic involution \(\tau\) has four fixed bitangents and 12 two-element bitangent orbits. Their Proposition 7.19 identifies those 12 pairs with \(A[2]\setminus A[\widehat\lambda]\). The inspected bitangent section does not give the orbit decomposition for the full marked \(\mu_6\)-action. Searches for equivalent formulations using bitangents, odd theta characteristics, the marked cyclic order-six action, and the induced action on the 12 Prym two-torsion points did not locate a statement covering the decomposition proved here.

## Limitations
This result does not classify the action of the full automorphism group on the special curve \(a=0\); it only concerns the marked \(\mu_6\)-subgroup that exists throughout the family. The originality comparison is limited by the possibility that an older classical bitangent table or an unindexed computation records the same cycle structure in different terminology. No claim is made about arithmetic Galois orbits over a nonclosed ground field.

## References
J. Laga and A. Shnidman, *The geometry and arithmetic of bielliptic Picard curves*, arXiv:2308.15297, first posted 29 August 2023; Journal of the London Mathematical Society 112 (2025), e70347, DOI:10.1112/jlms.70347. Relevant material: Section 2.1, Lemma 7.18, and Proposition 7.19.
