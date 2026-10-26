# Subalgebra–ideal separation in free cube-zero associative algebras

## Finding

Fix a prime power \(q\), an integer \(r\ge 1\), and an \(r\)-dimensional vector space \(V\) over \(\mathbb F_q\). Let \(W=V\otimes_{\mathbb F_q}V\), and give \(A_r=V\oplus W\) the nonunital associative multiplication
\[
(v,a)(w,b)=(0,v\otimes w).
\]
Thus \(A_r^2=W\), \(A_r^3=0\), and \(A_r\) is the positive-degree truncation through degree two of the free associative algebra on \(r\) generators. Throughout, **subalgebra** means an \(\mathbb F_q\)-linear subspace closed under multiplication (no identity is required). Ideals are two-sided \(\mathbb F_q\)-linear ideals.

Write \({n\brack k}_q\) for the Gaussian binomial coefficient (zero unless \(0\le k\le n\)), and \(m=r^2\). Let \(S_{r,q}(z)\) and \(I_{r,q}(z)\) count all subalgebras and two-sided ideals, respectively, by their \(\mathbb F_q\)-dimensions. Then, for every \(r\ge1\) and every prime power \(q\),
\[
\boxed{S_{r,q}(z)=\sum_{u=0}^{r}{r\brack u}_q\sum_{t=u^2}^{m}{m-u^2\brack t-u^2}_q\,q^{u(m-t)}z^{u+t}},
\]
\[
\boxed{I_{r,q}(z)=\sum_{u=0}^{r}{r\brack u}_q\sum_{t=2ru-u^2}^{m}{m-2ru+u^2\brack t-2ru+u^2}_q\,q^{u(m-t)}z^{u+t}}.
\]
These include the zero subalgebra/ideal and the entire algebra. The same formulas refine by \(u=\dim\pi(S)\), where \(\pi:A_r\to V\) is projection onto the degree-one component.

For fixed \(q\) and \(r\to\infty\), a uniformly chosen subalgebra has \(\dim\pi(S)=1\) with probability tending to one, whereas a uniformly chosen two-sided ideal has \(\dim\pi(I)=0\) with probability tending to one. More precisely, with \(\mathcal S_r\) and \(\mathcal I_r\) the sets of all subalgebras and ideals,
\[
\boxed{\frac{|\mathcal I_r|}{|\mathcal S_r|}\sim\frac{1}{{r\brack1}_q}\sim(q-1)q^{-r}.}
\]
The asymptotic is for each **fixed** prime power \(q\); no joint \(q,r\) limit is claimed.

## Assumptions and scope

The free nilpotent associative algebra under study is nonunital and satisfies the identity that every product of three elements is zero. The degree-one space has dimension \(r\), the degree-two space has dimension \(r^2\), and there are no other relations among its degree-two words. In particular, \(U\otimes U\) has dimension \(u^2\) for every \(u\)-dimensional subspace \(U\le V\). The base field can be any finite field, in every characteristic. Dimensions and all counts are taken over that base field.

## Proof

**1. Unique subspace coordinates.** For each subspace \(X\le A_r\), set \(U=\pi(X)\) and \(T=X\cap W\), with dimensions \(u\) and \(t\). The map \(\pi:X\to U\) has kernel \(T\), and \(X\) is uniquely specified, once \(U,T\) are fixed, by a linear graph map \(f:U\to W/T\). Conversely, every such graph map produces a subspace \(X\), of dimension \(u+t\). There are \(q^{u(m-t)}\) choices of \(f\).

**2. Multiplicative closure.** For lifts \(u+\widetilde f(u)\) and \(v+\widetilde f(v)\) in \(X\), their product is exactly \(u\otimes v\in W\). Products involving a vector of \(T\) vanish. Hence \(X\) is a subalgebra if and only if \(U\otimes U\subseteq T\). This tensor subspace has dimension \(u^2\). For each fixed \(U\) there are \({m-u^2\brack t-u^2}_q\) choices of \(T\) of dimension \(t\) containing it. Since the choices of \(U\) number \({r\brack u}_q\), the subalgebra polynomial follows by multiplication of these independent counts.

**3. Two-sided ideals.** The products of an arbitrary element of \(A_r\) with a lift from \(U\), on both sides, span \(V\otimes U+U\otimes V\). Its dimension is \(ru+ru-u^2=2ru-u^2\), since \((V\otimes U)\cap(U\otimes V)=U\otimes U\). Thus \(X\) is a two-sided ideal if and only if \(T\) contains this sum. Replacing the compulsory subspace dimension by \(2ru-u^2\) in Step 2 proves the ideal polynomial. No hypothesis about whether \(X\) is graded has entered either count.

**4. A uniform Gaussian bound.** Define \(G_n(q)=\sum_{k=0}^n{n\brack k}_q\), the number of all subspaces of \(\mathbb F_q^n\). Put \(C_q=\prod_{j=1}^{\infty}(1-q^{-j})^{-1}<\infty\). The product formula for Gaussian coefficients gives, uniformly in \(n,k\),
\[
q^{k(n-k)}\le {n\brack k}_q\le C_q q^{k(n-k)}.
\]
Summing the Gaussian tails about \(k=n/2\) shows that for some fixed \(B_q<\infty\),
\[
q^{\lfloor n^2/4\rfloor}\le G_n(q)\le B_q q^{\lfloor n^2/4\rfloor}.
\]
Indeed, in the even case the normalized tail exponents are negative squares, while in the odd case they are consecutive-integer products. Consequently \(G_{n-1}(q)/G_n(q)=O_q(q^{-\lfloor n/2\rfloor})\).

**5. Subalgebras predominantly have one degree-one direction.** Let \(S_u\) count subalgebras whose projected dimension is \(u\). For \(u=0\) every subspace of \(W\) works, so \(S_0=G_m(q)\). For \(u=1\), the Gaussian Pascal identity yields the exact expression
\[
S_1={r\brack1}_q\sum_{t=1}^{m}{m-1\brack t-1}_q q^{m-t}
={r\brack1}_q\bigl(G_m(q)-G_{m-1}(q)\bigr).
\]
For \(2\le u\le r\), put \(D=u(u-1)\). Bounding the Gaussian coefficients and completing the square in the summation variable gives
\[
S_u\le C_q^2(m+1)q^{\,u(r-u)+(m-D)^2/4}.
\]
Here the exponent is at most \(m^2/4-m/4\), because \(u(r-u)\le m/4\) and \(2\le D<m\) imply
\[
 u(r-u)-mD/2+D^2/4\le m/4-mD/4\le-m/4.
\]
It follows that \(\sum_{u=2}^{r}S_u=o(G_m(q))\). Together with Step 4 this implies
\[
|\mathcal S_r|={r\brack1}_qG_m(q)\bigl(1+o(1)\bigr),
\qquad
\Pr(\dim\pi(S)=1)\longrightarrow 1.
\]

**6. Ideals predominantly lie in the square.** Let \(I_u\) count two-sided ideals with projected dimension \(u\). Again \(I_0=G_m(q)\). In the \(u\ge1\) terms of the ideal formula the free tensor dimension is \(N=(r-u)^2\). A completion-of-the-square bound now gives
\[
I_u\le C_q^2(m+1)q^{\,u(r-u)+(N+u)^2/4}.
\]
For \(1\le u\le r\) we have \(N+u=(r-u)^2+u\le(r-1)^2+1=m-2r+2\). Thus
\[
\sum_{u=1}^{r}I_u\le rC_q^2(m+1)q^{m/4+(m-2r+2)^2/4}=o(G_m(q)),
\]
since the difference between the exponent displayed and \(m^2/4\) equals \(-r^3+9r^2/4-2r+1\), tending to negative infinity. Hence \(|\mathcal I_r|=G_m(q)(1+o(1))\) and \(\Pr(\dim\pi(I)=0)\to1\).

**7. The sharp quotient asymptotic.** Combining the last two steps,
\[
\frac{|\mathcal I_r|}{|\mathcal S_r|}\sim\frac{1}{{r\brack1}_q}
=\frac{q-1}{q^r-1}\sim(q-1)q^{-r}.
\]
This completes the proof.

## Verification

The companion script `verify_free2.py` independently enumerates all reduced-row-echelon subspaces of the underlying vector space and checks closure under the actual multiplication, and separately checks both-sided ideal closure against the ambient standard basis. It compares the complete dimension and projection distributions against the formulas. Exhaustive checks pass for \((r,q)=(1,2),(1,3),(2,2),(2,3)\), covering respectively \(5,6,2825,56632\) ambient subspaces. For \((r,q)=(2,2)\) there are \(221\) subalgebras and \(77\) ideals; for \((2,3)\) the counts are \(949\) and \(229\). Formula-only checks at larger parameters illustrate, but do not prove, the limits. The universal statements are proved algebraically above.

## Relationship to prior work

Bauer and Schein, *Ideal growth in amalgamated powers of nilpotent rings of class two and zeta functions of quiver representations* (first preprint February 22, 2022, arXiv:2202.10865), study ideal zeta functions of class-two nilpotent algebras over compact discrete valuation rings. This motivates comparing ideal and subalgebra growth, but their Theorems 1.1–1.2 concern p-adic ideal enumerators and amalgamations, not the finite-field free associative cube-zero algebra's rank-refined subalgebra census or its fixed-field, large-generator limit.

Siconolfi, Vantomme, and Voll, *Subgroup growth in free class-2-nilpotent groups* (first arXiv preprint May 31, 2023, arXiv:2305.19665), compute local subalgebra zeta functions of free class-two **Lie** rings, in which the degree-two part is an alternating exterior square. Their Section 4 and Proposition 4.4 treat lattice-index enumeration over discrete valuation rings. The present associative multiplication has the full ordered-word tensor square, whose one-dimensional projection contribution and two-sided ideal constraint lead to the displayed different formulas. Neither set of formulas is being asserted as a specialization of the other.

Mainellis, *Characterizing Nilpotent Associative Algebras by Their Multiplier* (arXiv:2302.01422, February 2, 2023), addresses Schur-multiplier defects and classification, not the subalgebra and ideal distributions considered here.

The subspace-extension argument is elementary, but the complete graded-dimension formulas and the opposite typical projection dimensions supply a specific quantitative distinction between subalgebra and ideal growth for the free associative family. No exhaustive claim about all possible prior formulations is made.

## Limitations

The asymptotic results fix \(q\) while \(r\) grows; there is no asserted uniform joint-field limit. The algebra is the free **nonunital** cube-zero associative algebra, not a free class-two Lie algebra, a general algebra with square-zero radical, or the untruncated free associative algebra. The statements count \(\mathbb F_q\)-linear subalgebras, not arbitrary multiplicatively closed additive subsets or all abstract isomorphism classes. Computer checks cover only the stated small prime fields and are not used as infinite proofs. Unindexed or terminology-shifted earlier finite-field enumerations remain a publication-priority risk.

## References

1. T. Bauer and M. M. Schein, *Ideal growth in amalgamated powers of nilpotent rings of class two and zeta functions of quiver representations*, arXiv:2202.10865v1 (2022-02-22), https://arxiv.org/abs/2202.10865.
2. V. Siconolfi, M. Vantomme and C. Voll, *Subgroup growth in free class-2-nilpotent groups*, arXiv:2305.19665v1 (2023-05-31), https://arxiv.org/abs/2305.19665.
3. E. Mainellis, *Characterizing Nilpotent Associative Algebras by Their Multiplier*, arXiv:2302.01422v1 (2023-02-02), https://arxiv.org/abs/2302.01422.
