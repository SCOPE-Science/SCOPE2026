# Full projective symmetry dichotomy for five-nodal even sextics

## Finding
Let \(k\) be an algebraically closed field of characteristic different from \(2\). Let \(C\subset\mathbb P^2_k\) be an **integral** plane sextic with equation
\[
F=A Y^6+B Y^4Z^2+C_4 X^2Y^4+D Y^2Z^4+E X^2Y^2Z^2+U X^4Y^2+G Z^6+H X^2Z^4-U X^4Z^2,
\]
where \(U\ne0\), and suppose its entire geometric singular locus consists of five ordinary nodes
\[
P_0=[1:0:0],\qquad P_{\epsilon,\eta}=[1:\epsilon a:\eta b]\quad(\epsilon,\eta\in\{1,-1\}),\qquad ab\ne0.
\]
Then its **full embedded projective automorphism group** is precisely one of the following:
\[
\operatorname{Aut}_{\mathbb P^2}(C)\cong
\begin{cases}
(\mathbb Z/2\mathbb Z)^2,&(G,D,H)\ne(-A,-B,C_4),\\
D_8\ \text{(dihedral of order eight)},&(G,D,H)=(-A,-B,C_4).
\end{cases}
\]
In the order-four case the group consists of the independent changes of signs of \(Y\) and \(Z\). In the order-eight case an additional generator is
\[T:[X:Y:Z]\longmapsto[X:iZ:-iY],\qquad i^2=-1.\]
The coefficient condition is intrinsic to the displayed even-sextic coordinates; it is a sharp criterion for their projective symmetry enhancement, not a criterion for abstract automorphisms of the normalization.

The two explicit complex sextics
\[
F_\epsilon=X^4(Y^2-Z^2)+4X^2Y^2Z^2+Y^6-Z^6+\epsilon Y^2(Y^2+Z^2)^2,\qquad \epsilon\in\{0,1\},
\]
are both integral and have exactly the same five ordinary nodes \([1:0:0]\) and \([1:\pm1:\pm i]\), but their full projective groups have orders \(8\) and \(4\), respectively. Their normalizations have genus five and are nonhyperelliptic generalized Howe curves of type \((g_1,g_2,r)=(2,2,4)\).

## Assumptions and scope
The statement is about embedded projective automorphisms over an algebraically closed field of odd characteristic. The hypotheses require exactly the five **geometric ordinary nodes**, no additional singularities, irreducibility, and nonzero quadratic coefficient \(U\). Neither the claim nor the proof assumes that every even sextic of this shape arises from a specific published parameterization. It applies, in particular, to every five-nodal sextic of the even normal form studied by Moriya and Kudo, after permuting coordinates so that the homogenizing coordinate is \(X\). The explicit realization and Howe interpretation are over \(\mathbb C\), not an assertion about arbitrary positive characteristic.

## Proof
**1. The intrinsic five-point configuration.** The two lines joining opposite peripheral nodes, \(P_{++}P_{--}\) and \(P_{+-}P_{-+}\), both contain \(P_0\). They are the only lines through three of the five nodes. Hence \(P_0\) is characterized intrinsically as the only node lying on two three-node lines and is fixed by every projective automorphism. The remaining four nodes form a projective frame: no three of them are collinear (use \(ab\ne0\) and \(\operatorname{char} k\ne2\)). Their permutations must preserve the partition into the two opposite pairs. This is an eight-element permutation group \((C_2\times C_2)\rtimes C_2\). The four sign changes on \((Y,Z)\), together with
\[
T_{a,b}:[X:Y:Z]\mapsto[X:(a/b)Z:(b/a)Y],
\]
realize all eight permutations as projective transformations. Four points in general position form a projective frame, so there can be no additional projective transformations inducing the same node permutation. Therefore the full stabilizer of the node configuration has order eight and every automorphism of \(C\) lies in it.

**2. Excluding an extra symmetry of the wrong tangent type.** The four sign changes preserve \(F\) and form the Klein four group. If the full group is larger, an antidiagonal transformation, differing from \(T_{a,b}\) by signs, must preserve \(C\). Write \(\lambda=a/b\); the extra transformation can be chosen as
\[T_\lambda:[X:Y:Z]\mapsto[X:\lambda Z:\lambda^{-1}Y].\]
Since \(F\) is irreducible, preservation of its zero locus implies \(F\circ T_\lambda=\mu F\) for some \(\mu\in k^\times\). At \(P_0\) the quadratic term is \(U(Y^2-Z^2)\). Comparing the coefficients of this term gives
\[
\lambda^4=1,\qquad \mu=-\lambda^{-2}.
\]
If \(\lambda^2=1\), then \(\mu=-1\). The transformation \(T_\lambda\) fixes pointwise the projective line defined by \(Y=\lambda Z\); hence \(F\) would vanish identically along that line, contradicting irreducibility. Consequently \(\lambda^2=-1\) and \(\mu=1\).

**3. Exact coefficient test and converse.** Set \(s=Y^2\), \(t=Z^2\) on \(X=1\). When \(\lambda^2=-1\), the transformation acts as \((s,t)\mapsto(-t,-s)\). Expanding the equation and comparing the cubic and quadratic coefficients shows that invariance is equivalent to
\[
G=-A,\qquad D=-B,\qquad H=C_4.
\]
The linear coefficients already have the required opposite signs, and \(E\) is unconstrained. Conversely, if these three identities hold, the displayed transformation \(T\) with \(i^2=-1\) preserves \(F\) exactly. It is not a sign change, so it doubles the sign subgroup. Step 1 rules out a larger group. The generated order-eight group is dihedral: the product of \(T\) with one coordinate sign involution has order four and the coordinate sign involution conjugates it to its inverse.

**4. Two sharp complex realizations.** Write \(s=Y^2\), \(t=Z^2\) in the affine chart \(X=1\). For \(\epsilon=0,1\), the corresponding cubic is
\[
f_\epsilon(s,t)=s^3-t^3+4st+s-t+\epsilon s(s+t)^2.
\]
An exact Gröbner-basis computation over \(\mathbb Q\) gives
\[
\big\langle f_\epsilon,\partial_s f_\epsilon,\partial_t f_\epsilon\big\rangle=(s-1,t+1)
\]
for both values. Because squaring is étale away from the coordinate axes, the only off-axis singularities are the four points \([1:\pm1:\pm i]\). The Hessian determinants of \(f_\epsilon\) at \((1,-1)\) are respectively \(20\) and \(28\), so all four are ordinary nodes. At \(P_0\) the tangent cone is \(Y^2-Z^2\), giving a fifth ordinary node.

On \(Y=0\) the equation restricts to \(-Z^2(X^4+Z^4)\); on \(Z=0\) it restricts to \(Y^2(X^4+(1+\epsilon)Y^4)\). Their noncentral zeros are smooth, so there are no other affine singularities. On \(X=0\) the binary sextic is \(Y^6-Z^6+\epsilon Y^2(Y^2+Z^2)^2\). Setting \(Y=1\) and \(u=Z^2\) gives \(1-u^3\) for \(\epsilon=0\) and \(2+2u+u^2-u^3\) for \(\epsilon=1\), both squarefree with nonzero top and constant coefficients. Thus infinity is smooth.

There are exactly five nodes and no positive-dimensional singular locus, so the sextics are reduced. If one were reducible, Bézout and the fact that all intersections must be transverse nodes would force a line component (the minimum product of degrees is \(1\cdot5=5\); any other degree split contributes at least eight). Since the equation has no term linear in \(X\), every smooth point at infinity has tangent line through \(P_0\). Thus a line component would pass through \(P_0\) and equal one of its two tangent lines \(Y=Z\) or \(Y=-Z\). But substitution yields \(4X^2Y^4+4\epsilon Y^6\ne0\) on either candidate line. Hence both sextics are integral. Their normalization has genus \(\binom52-5=5\).

The sign involutions on the normalization have respectively \(4\), \(4\), and \(8\) fixed points: the first two fix the four smooth intersections with their respective coordinate lines, exchanging the branches at \(P_0\); the product fixes six smooth points at infinity and both normalization branches over \(P_0\). Riemann–Hurwitz gives quotient genera \(2,2,1\), and the full Klein-four quotient has genus zero. The two genus-two double covers of that rational quotient have four common branch points (equivalently, the genus-five Howe formula \(g=2(g_1+g_2)+1-r\) yields \(r=4\)). Thus their fiber product normalization is of Howe type \((2,2,4)\) and is nonhyperelliptic. Finally, \(F_0\) satisfies the three symmetry equations, whereas \(F_1\) does not; Step 3 gives the stated groups.

## Verification
Run the accompanying standalone Python script with SymPy installed: `python verify.py`. It reconstructs the two homogeneous polynomials, checks the critical Gröbner ideals and Hessian determinants exactly, checks both axis restrictions and squarefreeness at infinity, verifies sign invariance and the additional symmetry only in the first example, and checks the general coefficient identities symbolically. The script's exact rational polynomial computations verify the specialized identities; the parameter-uniform stabilizer classification follows from Steps 1–3, not from finite testing.

## Relationship to prior work
Moriya and Kudo, *Explicit construction of a plane sextic model for genus-five Howe curves, I*, arXiv:2310.15993v1 (first submitted 2023-10-24), give the even sextic normal form and classify the possibilities of three or five double points (Theorems 1–2 and Proposition 4.2.6). Their Lemma 3.2.1 establishes the opposite quadratic coefficients. This is the geometric input, not a new claim. Their article does not state the complete projective stabilizer dichotomy or the displayed sharp coefficient test. Kudo's companion paper, arXiv:2401.00760v1, concerns another sextic model and its singularities and identifies an abstract Klein-four subgroup; it does not establish full projective stabilizers of the five-nodal even normal form. Related results about abstract Howe-curve automorphisms do not automatically classify projective symmetries of a fixed sextic embedding.

## Limitations
Only the five-ordinary-node stratum and embedded automorphisms are classified. The three-singularity degenerations may have other stabilizers. The explicit sharpness examples and Howe identification are over \(\mathbb C\), not asserted as realizations in every odd characteristic. The statement does not determine the full abstract automorphism groups of their genus-five normalizations, nor does it imply a new birational classification. An unindexed prior equivalent result or a stronger theorem in literature not fully inspected remains a priority risk.

## References
1. T. Moriya and M. Kudo, *Explicit construction of a plane sextic model for genus-five Howe curves, I*, arXiv:2310.15993v1 (2023-10-24), especially Theorems 1–2, Lemma 3.2.1, and Proposition 4.2.6, https://arxiv.org/pdf/2310.15993.
2. M. Kudo, *Explicit construction of a plane sextic model for genus-five Howe curves, II*, arXiv:2401.00760v1 (2024-01-01), especially Theorem 1, Corollary 1, and §2.1, https://arxiv.org/pdf/2401.00760.
3. T. Katsura and K. Takashima, *Decomposed Richelot isogenies of Jacobian varieties of hyperelliptic curves and generalized Howe curves*, arXiv:2108.06936v1 (2021), for the generalized Howe genus/quotient framework.
