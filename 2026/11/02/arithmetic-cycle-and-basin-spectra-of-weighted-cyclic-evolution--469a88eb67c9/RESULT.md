# Arithmetic cycle and basin spectra of weighted cyclic evolution algebras

## Finding

Let \(q\) be any prime power, \(n\geq 1\), and \(a_0,\ldots,a_{n-1}\in\mathbb F_q^\times\). Let \(E\) be the evolution algebra with natural basis \(e_i\), indexed by \(\mathbb Z/n\mathbb Z\), whose nonzero products are \(e_{i-1}^2=a_i e_i\). Its quadratic evolution operator on coordinate vectors is
\[
F_a(x)_i=a_i x_{i-1}^2.
\]
Write \(m=q-1=2^s h\) with \(h\) odd and \(s\geq0\). The exact number of points entering a periodic orbit after **at most** \(j\) iterations is
\[
\boxed{T_j=(1+h2^{\min(j,s)})^n}\qquad(j\geq0).
\]
Thus the number of strictly preperiodic points with exact entrance time \(j\), \(1\leq j\leq s\), is \((1+h2^j)^n-(1+h2^{j-1})^n\); there are no longer tails. In particular, exactly \((1+h)^n\) points are periodic. These statistics do not depend on any of the nonzero weights. If \(s=0\), the operator is a permutation.

At every periodic point with precisely \(r\) nonzero coordinates, the attached inverse-image tree has height \(s\). For \(s\geq1\), its root has \(2^r-1\) off-cycle predecessors; each non-root node at depth less than \(s\) has \(2^r\) predecessors, and every node at depth \(s\) is a leaf. The statement also applies to \(r=0\), when the tree is trivial. In even field cardinality all trees are trivial.

There is also a complete exact cycle-length census, sensitive to the weights. Choose a primitive element \(\gamma\) of \(\mathbb F_q^\times\), and choose integer exponents \(b_i\) with \(a_i=\gamma^{b_i}\). Put
\[
G=\gcd(m,2^n-1),\qquad B\equiv b_0+\sum_{i=1}^{n-1}2^{n-i}b_i\pmod G.
\]
For every \(t\geq1\), put \(g_t=\gcd(n,t)\), \(\ell_t=n/g_t\), \(d_t=\gcd(m,2^{t\ell_t}-1)\), and \(H_t=(2^{t\ell_t}-1)/(2^n-1)\). The latter quotient is an integer. Define \(\epsilon_t=1\) if \(d_t\mid B H_t\), and \(\epsilon_t=0\) otherwise. The divisibility condition is independent of the chosen representative of \(B\) modulo \(G\).

The exact number of points fixed by \(F_a^t\) with precisely \(r\) nonzero coordinates is
\[
\boxed{P_{r,t}=\begin{cases}
\binom{g_t}{j}(\epsilon_t d_t)^j,&r=j\ell_t,\ 0\le j\le g_t,\\
0,&\text{otherwise},
\end{cases}}
\]
where \(0^0=1\). In particular \(\#\operatorname{Fix}(F_a^t)=(1+\epsilon_t d_t)^{g_t}\). The number of distinct cycles of **least** length \(t\) with support size \(r\) is exactly
\[
\boxed{C_{r,t}=\frac1t\sum_{v\mid t}\mu(t/v)P_{r,v}.}
\]
These formulas and the rooted trees determine the entire directed functional graph of \(F_a\) up to isomorphism.

A further arithmetic rigidity holds: changing the basis by nonzero diagonal scalars changes the vector of weight exponents without changing \(B\pmod G\), and two exponent vectors are diagonally equivalent **if and only if** their \(B\)-classes agree. Applying the same unit power permutation \(x\mapsto x^u\) to every coordinate, \(\gcd(u,q-1)=1\), sends \(B\) to \(uB\). Consequently, whenever two weight vectors satisfy \(\gcd(B,G)=\gcd(B',G)\), their entire finite functional graphs are isomorphic. This last implication does not assert that the converse holds for arbitrary graph isomorphisms.

## Assumptions and scope

The weights are all nonzero; a zero weight changes the support dynamics and is excluded. The finite field may have any characteristic and need not be a prime field. The grading is the specified cyclic natural basis and the operator is the **quadratic evolution operator** \(x\mapsto x^2\) in the evolution algebra, not an algebra homomorphism. All fixed-point counts refer to the finite set \(\mathbb F_q^n\). A point's entrance time is the smallest \(j\geq0\) for which \(F_a^j(x)\) is periodic. Support size counts nonzero natural-basis coordinates.

## Proof

**1. Coefficient normalization.** On a nonzero coordinate write \(x_i=\gamma^{z_i}\), \(z_i\in\mathbb Z/m\mathbb Z\). The exponent map reads \(z'_i=b_i+2z_{i-1}\). A diagonal coordinate change \(x_i=\gamma^{u_i}y_i\) replaces \(b_i\) by \(b_i+2u_{i-1}-u_i\). Successively choose \(u_1,\ldots,u_{n-1}\) so that every new coefficient but that at index zero vanishes. The remaining coefficient is \(B+(2^n-1)u_0\pmod m\). As \(u_0\) varies, its possible values are exactly the residue class \(B\pmod G\). This proves both the normalization and its completeness. It is a coordinate scaling valid also when some original coordinates are zero.

**2. Fixed-point formula.** Use the normalized map, whose only potentially nonunit weight is \(a_0=\gamma^B\). Iterating \(t\) steps permutes supports by a shift of \(t\) along the \(n\)-cycle. That shift has \(g_t\) disjoint coordinate orbits, each of length \(\ell_t\). A point fixed by \(F_a^t\) must have an entire coordinate orbit zero or an entire orbit nonzero. On an active orbit, compose its \(\ell_t\) equations. The resulting one-variable equation has the form
\[
z=\gamma^{2^e B H_t}z^{2^{t\ell_t}}
\]
for a suitable nonnegative integer \(e\) depending on the coordinate orbit. The exponent \(H_t=1+2^n+\cdots+2^{n(t/g_t-1)}\) records the \(t/g_t\) visits to the unique weighted edge. Since \(d_t\) divides the odd number \(2^{t\ell_t}-1\), the factor \(2^e\) is invertible modulo \(d_t\). In the cyclic group \(\mathbb F_q^\times\) the equation therefore has precisely \(d_t\) nonzero solutions when \(d_t\mid B H_t\), and none otherwise. Each solution determines every other coordinate on that orbit uniquely (all nonzero forward multipliers). Choosing \(j\) of the \(g_t\) orbits gives the asserted \(P_{r,t}\). To verify that the criterion is well-defined, observe \(d_t\mid m\) and \(d_t\mid (2^n-1)H_t\), which implies \(d_t\mid GH_t\) by prime-power valuations. Möbius inversion of \(P_{r,t}=\sum_{v\mid t}vC_{r,v}\) yields the exact least-cycle formula.

**3. Periodicity and entrance time.** Decompose the cyclic group \(\mathbb Z/m\mathbb Z\) canonically into its \(2\)-primary factor \(\mathbb Z/2^s\mathbb Z\) and odd factor \(\mathbb Z/h\mathbb Z\). On active coordinates the exponent update is \(z'_i=b_i+2z_{i-1}\), while the set of active positions merely rotates. On the entire \(2\)-primary coordinate space the affine map \(z\mapsto b+2Sz\), where \(S\) is the cyclic shift, has a unique fixed vector \(c\): the matrix \(I-2S\) is invertible modulo \(2^s\) (indeed its determinant is \(1-2^n\), odd). Subtract \(c\) on active coordinates only. The resulting deviations are shifted and multiplied by \(2\) every step, so they vanish after \(j\) steps precisely if each initial deviation is killed by \(2^j\). Each active position offers \(2^{\min(j,s)}\) permitted deviations. On the odd coordinate group the same affine rule is a permutation between successive support patterns because multiplication by \(2\) is invertible modulo \(h\); hence every one of the \(h\) odd values is already on a periodic support orbit. Summing over all \(\binom nr\) support sets of size \(r\) gives
\[
T_j=\sum_{r=0}^n\binom nr\bigl(h2^{\min(j,s)}\bigr)^r=(1+h2^{\min(j,s)})^n.
\]
Once the primary deviations vanish, the remaining support-and-odd-coordinate dynamics is a permutation, and conversely no point with nonzero primary deviation can be periodic because repeated multiplication by two kills its deviation. Thus these are exact entrance times, including the characteristic-two case \(s=0\).

**4. Rooted predecessor trees.** Fix a support pattern of cardinality \(r\). Its unique predecessor support pattern is determined by inverse rotation; on odd exponents the predecessor is unique. For \(s\geq1\), a primary deviation vector at depth less than \(s\) is divisible by two in all active coordinates, so it has exactly \(2^r\) primary predecessors. A deviation at depth \(s\) has at least one odd primary coordinate and hence has none. At a periodic point one of the \(2^r\) predecessors lies on its cycle, leaving \(2^r-1\) attached off-cycle roots. These facts prove the entire tree description. For \(s=0\), all maps on each fixed support pattern are bijections.

**5. An arithmetic sufficiency criterion for graph conjugacy.** For \(\gcd(u,m)=1\), the pointwise power permutation \(R_u(x)_i=x_i^u\) (with \(R_u(0)=0\)) conjugates the weights \(a_i\) to \(a_i^u\), multiplying \(B\) by \(u\pmod G\). The reduction \((\mathbb Z/m\mathbb Z)^\times\to(\mathbb Z/G\mathbb Z)^\times\) is surjective, and units modulo \(G\) act transitively on residues having any fixed \(\gcd(B,G)\). Together with step 1 this gives the claimed explicit graph conjugacy. No classification of general, nonlinear graph conjugacies is needed.

## Verification

The standalone `verify.py` enumerates the entire phase space over small prime fields and extension fields. It traces every orbit to measure entrance time, independently counts fixed points and their support strata for each of the first 32 iterates, and reconstructs every point's actual incoming-edge count to test the uniform rooted-tree degrees. All 928 weighted configurations (354,173 tested starting states) pass. The finite tests are supplementary, not proof of the all-fields assertions; the proof above uses only cyclicity of finite-field units and elementary primary decomposition.

## Relationship to prior work

Elduque and Labra introduced a weighted-graph viewpoint for evolution algebras and proved a finiteness theorem for automorphism groups of perfect evolution algebras. Their proofs treat algebraic automorphisms, not this full coefficient-sensitive functional graph of the quadratic iteration. Sha and Hu derive one-variable powering-map cycle counts and explicitly study how a nontrivial scalar changes the one-variable equations, including failure of the unweighted formulas; the single-variable power-equation lemma used in step 2 is classical and is **not** claimed as new. Delgado-Eckert supplies a general graph-theoretic framework and fixed-point-system tests for monomial maps, rather than the complete parameterized cycle-and-basin census here. Hutz and Patel establish precise periodic-point and tail formulas for **split coordinatewise** powering maps. A cyclic weighted shift is not generally split under the coordinate change permitted in their statements; its iterate at time \(n\) is split, but the claimed full-time cycle lengths and coefficient obstruction require the additional cyclic-orbit and diagonal-gauge arguments above. These comparisons do not exclude an older equivalent treatment of cyclic weighted maps elsewhere.

## Limitations

All weights must be nonzero. The result does not treat general evolution algebras, arbitrary monomial exponent matrices, or quadratic operators on cyclic graphs with branches. The equivalence using \(\gcd(B,G)\) is a sufficient functional-graph isomorphism criterion, not a claimed necessary criterion for unrestricted graph isomorphisms. Historical priority has not been exhaustively determined; independent mathematical validation has not been performed.

## References

1. A. Elduque and A. Labra, *Evolution Algebras and Graphs*, arXiv:1312.4685v1, publicly submitted 2013-12-17, https://arxiv.org/html/1312.4685v1 .
2. M. Sha and S. Hu, *Monomial Dynamical Systems of Dimension One over Finite Fields*, arXiv:0910.5550, publicly submitted 2009-10-29, https://arxiv.org/abs/0910.5550 .
3. E. Delgado-Eckert, *An Algebraic and Graph Theoretic Framework to Study Monomial Dynamical Systems over a Finite Field*, arXiv:0711.1230, publicly submitted 2007-11-08, https://arxiv.org/abs/0711.1230 .
4. B. Hutz and T. Patel, *Periodic Points and Tail Lengths of Split Polynomial Maps Modulo Primes*, arXiv:1710.07821v1, publicly submitted 2017-10-21, https://arxiv.org/html/1710.07821v1 .
