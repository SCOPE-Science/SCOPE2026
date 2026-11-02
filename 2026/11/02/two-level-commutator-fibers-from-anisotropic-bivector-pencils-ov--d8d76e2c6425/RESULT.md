# Two-level commutator fibers from anisotropic bivector pencils over odd finite fields

## Finding
Let \(q\) be any odd prime power, \(V\) a four-dimensional vector space over \(\mathbb F_q\), and \(W\) a four-dimensional vector space over \(\mathbb F_q\). Suppose that a surjective linear map
\[
\beta:\bigwedge^2 V\longrightarrow W
\]
has kernel \(U\) containing **no nonzero decomposable bivector**. (Equivalently, \(\beta(v\wedge w)=0\) exactly when \(v,w\) are linearly dependent over \(\mathbb F_q\).) These maps exist for every odd \(q\).

Write \(F_\beta(t)=|\{(v,w)\in V^2:\beta(v\wedge w)=t\}|\). There is a canonical, up to an overall nonzero scalar, nondegenerate **minus-type quadratic form** \(Q_\beta\) on \(W\) such that
\[
F_\beta(t)=
\begin{cases}
q^5+q^4-q,&t=0,\\
q(q^2-1),&t\ne0,\ Q_\beta(t)=0,\\
q(q^2-1)(q+1),&Q_\beta(t)\ne0.
\end{cases}
\]
The number of nonzero targets in the second case is exactly \(q^3-q^2+q-1\); the number in the third case is exactly \(q^4-q^3+q^2-q\). Consequently, **all** \(q^4\) commutator values occur, but nonzero fibers have precisely two different sizes, rather than one.

Give \(G_\beta=V\times W\) the group multiplication
\[
(v,z)(w,t)=\bigl(v+w,z+t+\tfrac12\beta(v\wedge w)\bigr).
\]
Then \(G_\beta\) is a class-two group of order \(q^8\), exponent equal to the odd characteristic of \(\mathbb F_q\), and \(Z(G_\beta)=G_\beta'=\{0\}\times W\). Its commutator word map on ordered group-element pairs has fibers \(q^8F_\beta(t)\) above \((0,t)\). The theorem therefore gives the **complete commutator-word fiber distribution** for every group in this anisotropic-kernel family, without selecting a particular representative of its isomorphism type.

## Assumptions and scope
The field is finite of odd cardinality \(q\), not necessarily prime cardinality. The vector space dimension is exactly \(\dim V=\dim W=4\), and \(\beta\) is required to be surjective with a two-dimensional kernel having no nonzero decomposable vectors. Group multiplication is understood on the underlying additive groups; \(\tfrac12\) is the multiplicative inverse of \(2\) in \(\mathbb F_q\). The fibers are over **specified commutator targets**, not averaged over the target space.

These algebras and groups arise from the extremal situation of compressing the six-dimensional exterior-square commutator space while retaining the implication that commuting quotient vectors are proportional. The existence and maximal dimension of decomposable-free subspaces are established subjects in earlier literature; the statement assessed here is the *individual commutator-fiber spectrum and its exact multiplicities*, not the established extremal kernel dimension itself.

## Proof
**1. The Plücker quadratic form and its quotient.** Choose a basis \(e_1,\ldots,e_4\) of \(V\). With coordinates \((a,b,c,d,e,f)\) on \(\bigwedge^2V\) corresponding to \((e_{12},e_{13},e_{14},e_{23},e_{24},e_{34})\), put
\[
Q(a,b,c,d,e,f)=af-be+cd.
\]
This is a nondegenerate split quadratic form of dimension six (the orthogonal sum of three hyperbolic planes). A bivector is nonzero decomposable **if and only if** \(Q=0\): its alternating \(4\times4\) matrix has determinant \(Q^2\), and nonzero alternating matrices in dimension four have rank either two or four.

Our two-dimensional kernel \(U\) contains no nonzero \(Q\)-isotropic vector, so \(Q|_U\) is anisotropic and nondegenerate. Since \(q\) is odd, there is the orthogonal direct sum
\[
\bigwedge^2V=U\mathbin{\perp}U^\perp.
\]
The projection \(\pi_\perp\) identifies \(W=(\bigwedge^2V)/U\) with \(U^\perp\). Define \(Q_\beta(t)=Q(\pi_\perp(x))\), where \(\beta(x)=t\). Changing the volume basis scales \(Q\) by a nonzero scalar; this does not change its null cone or the fiber formulas.

Because \(Q\) has plus type in dimension six while \(Q|_U\) is an anisotropic binary form, its four-dimensional orthogonal complement has **minus type**. This follows from the classification of nondegenerate quadratic forms over finite fields of odd order, or from the multiplicative discriminant and Witt cancellation. Thus \(U^\perp\) is equivalent to the orthogonal sum of one hyperbolic plane and an anisotropic norm plane.

**2. Counting decomposable representatives of each target.** For a given \(t\in W\), let \(x_\perp\in U^\perp\) be its unique orthogonal representative. Every lift is \(x_\perp+u\), \(u\in U\). Orthogonality gives
\[
Q(x_\perp+u)=Q_\beta(t)+Q(u).
\]
An anisotropic binary quadratic form over \(\mathbb F_q\) is a nonzero scalar multiple of the norm form of \(\mathbb F_{q^2}/\mathbb F_q\). Every prescribed **nonzero** norm value has exactly \(q+1\) representations, whereas zero has exactly one representation. Therefore the number of decomposable lifts is one when \(Q_\beta(t)=0\), and \(q+1\) when \(Q_\beta(t)\ne0\). For \(t=0\), the unique decomposable lift is the zero bivector; for \(t\ne0\), all the counted lifts are nonzero.

**3. Counting pairs for each bivector.** For a fixed nonzero decomposable \(z\in\bigwedge^2V\), the set of ordered \((v,w)\in V^2\) with \(v\wedge w=z\) is a single \(\mathrm{SL}_2(\mathbb F_q)\)-torsor, of cardinality
\[
|\mathrm{SL}_2(\mathbb F_q)|=q(q^2-1).
\]
For zero wedge, the vectors must be dependent. There are \(q^4\) pairs with \(v=0\), and \((q^4-1)q\) additional pairs with \(v\ne0\) and \(w\in\mathbb F_qv\). Thus the zero-wedge fiber has size \(q^5+q^4-q\). Combining this with step 2 gives all three asserted values of \(F_\beta\).

**4. Multiplicities of the two nonzero values.** The minus-type quadratic space \(U^\perp\) has an orthogonal decomposition \(H\perp A\), where \(H\) is a hyperbolic plane and \(A\) an anisotropic plane. After suitable coordinates its equation is \(xy+N(a,b)\), with \(N\) anisotropic. For \((a,b)=0\), precisely \(2q-1\) pairs \((x,y)\) satisfy \(xy=0\). For each of the other \(q^2-1\) choices of \((a,b)\), the scalar \(-N(a,b)\) is nonzero and the equation \(xy=-N(a,b)\) has exactly \(q-1\) solutions. Hence the quadratic cone has
\[
(2q-1)+(q^2-1)(q-1)=q^3-q^2+q
\]
vectors, including the origin. Subtraction gives the two stated target multiplicities. The consistency identity
\[
(q^5+q^4-q)+(q^3-q^2+q-1)q(q^2-1)
 +(q^4-q^3+q^2-q)q(q^2-1)(q+1)=q^8
\]
confirms that these disjoint fibers partition \(V^2\).

**5. Explicit existence and group interpretation.** Choose any nonsquare \(\delta\in\mathbb F_q^\times\) and the anisotropic plane
\[
U=\langle e_{12}+e_{34},\ e_{13}+\delta e_{24}\rangle.
\]
Indeed, \(Q(s(e_{12}+e_{34})+t(e_{13}+\delta e_{24}))=s^2-\delta t^2\), which vanishes only for \(s=t=0\). An explicit surjection with kernel \(U\) is
\[
\beta(a,b,c,d,e,f)=(f-a,\ e-\delta b,\ c,\ d).
\]
For this example the induced quadratic form on the target is
\[
Q_\beta(t_1,t_2,t_3,t_4)=t_3t_4-\tfrac14t_1^2+\tfrac1{4\delta}t_2^2.
\]
The multiplication on \(G_\beta\) is associative because \(\beta\) is bilinear, and the displayed commutator is \([(v,z),(w,t)]=(0,\beta(v\wedge w))\) with the usual commutator convention. The center is precisely \(W\) since a vector commuting with all quotient vectors would have wedge zero against every vector, forcing it to be zero. Surjectivity implies \(G_\beta'=W\). The central coordinates of an ordered pair can be chosen independently in \(q^8\) ways, yielding the last fiber statement.

## Verification
Run `python3 verify.py` with the Python standard library. It checks that the displayed anisotropic plane has no decomposable nonzero element, that \(\beta\) has rank four, and that every nonzero contraction has rank three for prime fields of sizes \(3,5,7,11\). For \(q=3\) and \(q=5\), it **exhaustively enumerates all \(q^8\) ordered pairs** \((v,w)\) and every commutator target and checks all three fiber formulas and both target multiplicities. The command returns `VERIFY_OK`. These finite checks do not establish the universal claim for all prime powers; steps 1–5 do.

## Relationship to prior work
Levit and Shwartz, arXiv:2605.17171 (first posted May 16, 2026), §7.3, prove the general reduction of higher commuting probabilities to isotropic tensors (Propositions 7.9–7.11), and §7.5 examines full-contraction-rank and semi-extraspecial groups. Their formulas address tuple **totals** or other families and do not supply this **target-by-target two-level commutator distribution** in the four-by-four quotient with anisotropic kernel.

Gow and Quinlan, *On the vanishing of subspaces of alternating bilinear forms* (2006), specifically develop decomposable-free bivector subspaces and their relation to nilpotent group commutators (Theorems 2 and 3). Those existence and maximality results are not new here. Their theorems do not determine the two distinct **nonzero word-map fiber sizes** and the minus-type null-cone multiplicities of the quotient map. Vaughan-Lee (2015) classifies groups of order \(p^8\) and exponent \(p\), including four-generator class-two cases, but that is an isomorphism-class census, not a fiber census for specified central commutator targets. Berkovich, Kazarin, and Zhmud', *Groups of Prime Power Order*, Vol. 6, §311, treat a stronger normal-closure hypothesis on centralizers and likewise do not tabulate these fibers.

In a different setting, exact commutator-fiber counts for Kronecker path algebras have been studied. Those are associative algebra commutator maps, not the group family or quadratic target stratification here.

## Limitations
The quadratic-form proof uses odd characteristic. The statement does not claim uniqueness of the group up to isomorphism, does not characterize all class-two groups of order \(q^8\), and does not address arbitrary homomorphisms with larger kernels or kernels containing decomposable vectors. Existing literature already establishes the decomposable-free kernel construction and the maximal permissible kernel dimension: that is background, not a new contribution. Although targeted comparisons found no exact prior fiber table for this family, the possibility of equivalent results in older word-map or constant-rank literature remains. No independent mathematical audit has been performed.

## References
- V. E. Levit and R. Shwartz, *Higher Commutativity in Finite Groups, Rigidity, Extremal Bounds, and Heisenberg-Type Families*, arXiv:2605.17171 (v1 May 16, 2026), https://arxiv.org/abs/2605.17171, especially §§7.3–7.5.
- R. Gow and R. Quinlan, *On the vanishing of subspaces of alternating bilinear forms*, Linear Multilinear Algebra 54 (2006), 415–428, https://doi.org/10.1080/03081080500361264; author's lawful full text: https://maths.ucd.ie/~rodgow/alternatingnew.pdf.
- M. Vaughan-Lee, *Groups of order \(p^8\) and exponent \(p\)*, International Journal of Group Theory 4 (2015), 25–42, freely accessible full text https://www.researchgate.net/publication/283548910_Groups_of_order_p8_and_exponent_p.
- Y. Berkovich, L. Kazarin and E. Zhmud', *Groups of Prime Power Order*, Vol. 6 (2018), §311, https://doi.org/10.1515/9783110533149-055.
