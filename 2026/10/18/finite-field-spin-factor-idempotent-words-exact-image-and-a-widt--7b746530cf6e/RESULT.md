# Finite-field spin-factor idempotent words: exact image and a width-six exception

## Finding
Let \(F=\mathbb F_q\) have odd cardinality, let \((V,b)\) be a nondegenerate symmetric bilinear space of dimension \(d\ge3\), let \(Q(v)=b(v,v)\), and form the spin-factor Jordan algebra \(J=F1\oplus V\). Write \(\Delta\) for the determinant square class of \(b\) and \(\chi\) for the quadratic character of \(F\), extended by \(\chi(0)=0\). An *idempotent word* is a finite, nonempty, left-nested Jordan product of idempotents, and \(\ell(x)\) is the minimum number of idempotents representing \(x\) when one exists.

**Complete image.** If \(d\ge4\), or \(d=3\) and \(\chi(-\Delta)=1\), precisely the nonscalar elements and the scalar elements \(0,1\) are idempotent words:
\[
P(J)=\{0,1\}\cup\{\alpha1+v:\alpha\in F,\ 0\ne v\in V\}.
\]
If \(d=3\) and \(\chi(-\Delta)=-1\), the nonrepresentable elements are instead the scalar elements other than \(0,1\), together with all nonzero *pure isotropic* elements:
\[
P(J)=\{0,1\}\cup\{\alpha1+v:0\ne v\in V,\ (\alpha\ne0\ \text{or}\ Q(v)\ne0)\}.
\]
There are exactly \(q^2-1\) additional nonrepresentable pure isotropic elements in this case. Consequently,
\[
|P(J)|=\begin{cases}q^{d+1}-q+2,&d\ge4\text{ or }(d=3,\chi(-\Delta)=1),\\q^4-q^2-q+3,&d=3,\chi(-\Delta)=-1.\end{cases}
\]

**Exact maximal finite length.** The idempotent-word width, defined as \(w(J)=\max_{x\in P(J)}\ell(x)\), satisfies
\[
\boxed{w(J)=\begin{cases}6,&q=3,\ d=3,\chi(-\Delta)=-1,\\5,&\text{otherwise}.\end{cases}}
\]
Thus the unique nonsplit ternary quadratic-form type over \(\mathbb F_3\) supplies a genuine width-six exception, while every other nondegenerate finite-field spin factor of vector dimension at least three has width exactly five.

## Assumptions and scope
The underlying operation is
\[
(\alpha1+u)\circ(\beta1+v)=(\alpha\beta+b(u,v))1+\alpha v+\beta u.
\]
All products and dimensions are over the finite field \(F\), whose characteristic is odd. No assertion is made for degenerate quadratic forms, dimension below three, or arbitrary parenthesizations. The determinant square class does not depend on the chosen basis. The algebra has nontrivial idempotents precisely \(e_t=\tfrac12 1+t\) with \(Q(t)=\tfrac14\), in addition to \(0\) and \(1\). Appending \(1\) leaves a word unchanged and appending \(0\) makes it zero.

## Proof
**1. Linear and quadratic predecessor equations.** Let \(x=\alpha1+v\), with \(v\ne0\). For a putative final nontrivial idempotent \(e_t\), write \(x=(\beta1+s)\circ e_t\). Comparing vector and scalar parts shows that this equation is equivalent to
\[
Q(t)=\tfrac14,\qquad b(v,t)=\tfrac\alpha2,\qquad s=2v-2\beta t.
\tag{1}
\]
Conversely, any \(t\) satisfying the first two equations and any \(\beta\in F\) give a valid predecessor. Taking norms in the third equation yields
\[
Q(s)=\beta^2-4\alpha\beta+4Q(v).
\tag{2}
\]
If \(v\) is anisotropic, \(v^\perp\) is a nondegenerate quadratic space of dimension at least two. Every nondegenerate quadratic form in at least two variables over a finite field represents every field element; thus write \(t=(\alpha/(2Q(v)))v+h\) and select \(h\in v^\perp\) with \(Q(t)=1/4\). If \(v\) is isotropic and \(\alpha\ne0\), choose an isotropic hyperbolic partner \(z\) with \(b(v,z)=1\); then \(t=(1/(4\alpha))v+(\alpha/2)z\) has norm \(1/4\) and satisfies \(b(v,t)=\alpha/2\). If \(Q(v)=0=\alpha\), equation (1) asks for a norm-\(1/4\) vector in \(v^\perp\). The quotient \(v^\perp/Fv\) is nondegenerate of dimension \(d-2\), which represents \(1/4\) whenever \(d\ge4\). For \(d=3\) the quotient has dimension one with norm square class \(-\Delta\). It represents \(1/4\) if and only if \(\chi(-\Delta)=1\). This proves exactly when an eligible final idempotent exists, and proves the asserted permanent obstruction for pure isotropic vectors in the nonsplit ternary case.

For a scalar \(c1\), if \((\beta1+s)\circ e_t=c1\) with nontrivial \(e_t\), its vector equation gives \(s=-2\beta t\), after which the scalar part equals zero. Thus no nonzero scalar other than the original idempotent \(1\) is representable. These facts prove all exclusions, irrespective of the word length.

**2. A three-factor discriminant lemma.** Let \(y=\beta1+s\) have \(Q(s)\ne0\). If
\[
D(y)=(8\beta+1)^2-64Q(s)
\]
is a square in \(F\), then \(y\) is a word of length at most three. Indeed, choose \(\gamma\in F\) solving
\[
2\gamma^2-(8\beta+1)\gamma+8Q(s)=0.
\]
Such a root exists by the discriminant condition and is nonzero because \(Q(s)\ne0\). Choose \(u\in V\) with \(Q(u)=1/4\) and \(b(s,u)=\beta/2\), which is possible because \(s\) is anisotropic and \(\dim s^\perp\ge2\). Put \(z=2s-2\gamma u\). Direct expansion gives
\[
Q(z)=4Q(s)-4\gamma\beta+\gamma^2=\gamma/2\ne0.
\]
The nondegenerate space \(z^\perp\) has dimension at least two, so choose \(h\in z^\perp\) with \(Q(h)=1/4-Q(z)\). The two vectors \(z+h\) and \(z-h\) each have norm \(1/4\), and
\[
e_{z+h}\circ e_{z-h}=\gamma1+z,\qquad
(\gamma1+z)\circ e_u=\beta1+s.
\]
Thus the word of length three is explicit.

The discriminant condition is also *necessary* for a word of length at most three with nonzero vector component: a two-idempotent product \(\gamma1+z\) satisfies \(\gamma=2Q(z)\); eliminating its norm after the final multiplication gives precisely the displayed quadratic equation for \(\gamma\), hence its discriminant must be a square. Shorter words can be padded with \(1\) as needed.

**3. Upper bound five when \(q\ge5\).** For any element \(x=\alpha1+v\) admitted by part 1, choose one \(t\) satisfying (1), and define \(y_\beta=\beta1+s_\beta\), where \(s_\beta=2v-2\beta t\). From (2),
\[
D(y_\beta)=1-256Q(v)+16(16\alpha+1)\beta.
\tag{3}
\]
If \(16\alpha+1\ne0\), expression (3) ranges bijectively over \(F\). Exactly \((q+1)/2\ge3\) values of \(\beta\) give square discriminant. The polynomial \(Q(s_\beta)\) is monic quadratic and has at most two zeros. Hence for some \(\beta\) both \(D(y_\beta)\) is a square and \(Q(s_\beta)\ne0\); part 2 makes \(y_\beta\) a three-idempotent word, so \(x=y_\beta\circ e_t\) has length at most four. If \(16\alpha+1=0\), instead select \(\beta\ne-1/16\) with \(Q(s_\beta)\ne0\), possible because at most three values are excluded and \(q\ge5\). The already proved case gives \(\ell(y_\beta)\le4\), hence \(\ell(x)\le5\). Thus the image is exactly that claimed and width is at most five for all \(q\ge5\).

**4. Upper bound five over \(\mathbb F_3\), apart from the exceptional ternary form.** In dimension three, \(\chi(-\Delta)=1\) means the quadratic space is isometric to \(Q(a,b,c)=a^2+bc\), the determinant form on traceless \(2\times2\) matrices. Consequently \(J\cong M_2(\mathbb F_3)^+\), and Gogić--Tomašević, Proposition 4.1, proves that every nonscalar element has idempotent-word length at most five. For \(d\ge4\), every nonzero \(v\in V\) lies in a nondegenerate ternary subspace with \(\chi(-\det)=1\). If \(Q(v)\ne0\), select anisotropic \(u\in v^\perp\) and then \(w\in v^\perp\cap u^\perp\) with \(Q(w)=-Q(v)/Q(u)\); the latter perpendicular space has dimension at least two and represents this value. The ternary span has determinant \(-Q(v)^2\). If \(Q(v)=0\), choose a hyperbolic partner \(z\) and an orthogonal \(w\) of norm one; the span has determinant \(-1\). These subspaces are nondegenerate of the split ternary type, so the matrix result applies to \(\alpha1+v\) inside its spin-factor subalgebra. Hence all nonscalars have length at most five.

**5. The exceptional three-dimensional form over \(\mathbb F_3\).** In the remaining ternary case every form is isometric to \(Q(v)=v_1^2+v_2^2+v_3^2\). The six nontrivial idempotents are \(e_{i,s}=2\cdot1+s e_i\) for \(i=1,2,3\) and \(s\in\{1,2\}\). Signed coordinate permutations preserve the multiplication and act transitively on vectors with a specified number \(r\in\{0,1,2,3\}\) of nonzero coordinates. Accordingly the \(81\) elements have exactly twelve orbit types \((a,r)\), where \(a\in\mathbb F_3\) is the scalar coordinate. For the representative with its first \(r\) vector coordinates equal to \(1\), right multiplication by the six idempotents follows from the exact transition
\[
(a,v)\circ(2,se_i)=\bigl(2a+s v_i,\;2v+a s e_i\bigr)
\quad\text{over }\mathbb F_3.
\]
All successor types, with duplicate types suppressed, are as follows:

| Type | Successor types |
| --- | --- |
| \((0,0)\) | \((0,0)\) |
| \((0,1)\) | \((0,1),(1,1),(2,1)\) |
| \((0,2)\) | \((0,2),(1,2),(2,2)\) |
| \((0,3)\) | \((1,3),(2,3)\) |
| \((1,0)\) | \((2,1)\) |
| \((1,1)\) | \((0,0),(1,1),(2,2)\) |
| \((1,2)\) | \((0,1),(1,2),(2,3)\) |
| \((1,3)\) | \((0,2),(1,3)\) |
| \((2,0)\) | \((1,1)\) |
| \((2,1)\) | \((0,0),(1,2),(2,1)\) |
| \((2,2)\) | \((0,1),(1,3),(2,2)\) |
| \((2,3)\) | \((0,2),(2,3)\) |

Starting from the length-one types \((0,0),(1,0),(2,1)\), iterative application of this exact twelve-row table gives the newly attainable types at successive lengths:
\[
\begin{array}{c|l}
2&(1,2)\\3&(0,1),(2,3)\\4&(0,2),(1,1)\\5&(2,2)\\6&(1,3).
\end{array}
\]
The only missing types are \((2,0)\) and \((0,3)\), respectively the forbidden non-idempotent scalar and the eight nonzero pure isotropic vectors. Since the type \((1,3)\) first appears at length six, \(w(J)=6\). This is a finite twelve-state *proof* by explicitly enumerated exact transitions, not a numerical extrapolation.

**6. Sharp lower bound five uniformly.** For any odd \(q\), choose a nonsquare \(\theta\in F^\times\), and choose a vector \(v\) satisfying \(Q(v)=(1-\theta)/256\). The right-hand side is nonzero, and a nondegenerate form in dimension at least two represents every field element; hence such a vector exists. Set \(x=-(1/16)1+v\), which is nonscalar and eligible for representation. If \(x=y\circ e_t\) with \(y=\beta1+s\), equation (3) gives \(D(y)=\theta\), a nonsquare. But every three-idempotent word with nonzero vector component has square \(D\) by part 2; a scalar predecessor cannot yield this \(x\) unless it is an idempotent and leads to an even shorter word, also impossible by the same necessary discriminant condition. Thus \(\ell(x)\ge5\). Combined with parts 3--5, this proves all exact width assertions.

Finally, in the ternary nonsplit case the number of nonzero isotropic vectors is \(q^2-1\): a nondegenerate conic has \(q+1\) projective rational points, each with \(q-1\) nonzero representatives. Subtracting forbidden scalars and these pure isotropic points gives the stated cardinalities.

## Verification
The supplementary script `verify.py` performs exact finite-field breadth-first enumeration of idempotent words, retaining shortest lengths, across eight representative forms: the two ternary form types over \(\mathbb F_3\), \(\mathbb F_5\), and \(\mathbb F_7\), and two quaternary examples. It compares the *entire unreachable set* with the theorem, checks idempotency, and checks the exact maximal length. It separately reconstructs the twelve-state signed-permutation quotient in the exceptional \(81\)-element algebra, verifies the transition-derived length profile, and counts all \(72\) reachable points. Replay: `python3 verify.py`. The infinite-family conclusions rest on the algebraic proof; finite tests are supplemental.

## Relationship to prior work
I. Gogić and M. Tomašević, *Idempotent words in finite-dimensional simple Jordan algebras*, arXiv:2609.23581 (first publicly posted September 20, 2026), formulate the left-nested-word problem; their Section 3 treats spin factors under quadratic-closure assumptions, and Proposition 4.1 proves the two-by-two matrix case over arbitrary odd-characteristic fields. Those results are invoked in the \(q=3\) split reduction; the finite-field all-form classification, the permanently excluded nonsplit ternary isotropic vectors, the universal sharp five bound, and the nonsplit \(\mathbb F_3\) width-six type are not statements of the motivating paper.

Earlier two-idempotent-fiber calculations for finite-field spin factors concern **length two**. It is not the assertion about *arbitrarily long* left-nested words or their minimal uniform width here; the implication from length-two obstructions to permanent obstructions requires the predecessor argument in part 1, and the width-six phenomenon requires part 5.

## Limitations
The claim concerns only left-nested words, nondegenerate symmetric forms, odd finite fields, and \(\dim V\ge3\). The proof cites an established \(M_2(F)^+\) five-factor theorem for the three-dimensional split case. The twelve-state computation is fully reproducible and small, but does not replace the infinite-family proof. Equivalently formulated classifications in unindexed literature remain a bibliographic risk.

## References
- I. Gogić and M. Tomašević, *Idempotent words in finite-dimensional simple Jordan algebras*, arXiv:2609.23581, first version posted September 20, 2026; particularly Section 3, Lemmas 3.1--3.4, and Proposition 4.1. https://arxiv.org/abs/2609.23581
