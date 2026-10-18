# Finite-field idempotents of connected Alexander quandle algebras via orbit lattices

## Finding
Let \(G\) be a finite abelian group, let \(\varphi\) and \(1-\varphi\) be automorphisms of \(G\), and let \(k=\mathbb F_q\) have characteristic prime to \(|G|\). Define \(Q=\operatorname{Alex}(G,\varphi)\), with \(x*y=\varphi(x)+(1-\varphi)(y)\), and let \(k[Q]\) have basis \(e_x\) and product \(e_xe_y=e_{x*y}\). The following finite abelian-group construction classifies **every** idempotent of \(k[Q]\) and gives its exact cardinality, for splitting and nonsplitting coefficient fields alike.

Let \(m\) be the exponent of \(G\). Choose the least positive \(L\) for which \(m\mid q^L-1\) (put \(L=1\) for the trivial group), and put \(N=q^L-1\). In \(\widehat G=\operatorname{Hom}(G,\mathbb F_{q^L}^{\times})\), define commuting permutations
\[
A\chi=\chi\circ\varphi,\qquad B\chi=\chi\circ(1-\varphi),\qquad F\chi=\chi^q.
\]
For each orbit \(\Omega\) of \(\langle A,B,F\rangle\), define an integer matrix \(M_\Omega\) with columns labeled by \(\chi\in\Omega\), and, for every \(\chi\in\Omega\), two rows
\[
\mathbf e_\chi-\mathbf e_{A\chi}-\mathbf e_{B\chi},
\qquad \mathbf e_{F\chi}-q\mathbf e_\chi.
\]
Write its nonzero Smith diagonal entries as \(d_{\Omega,1},\ldots,d_{\Omega,r_\Omega}\), and set
\[
s_\Omega=N^{|\Omega|-r_\Omega}\prod_{j=1}^{r_\Omega}\gcd(N,d_{\Omega,j}).
\]
Then the exact number of idempotents, **including zero**, is
\[
\boxed{\#\operatorname{Idem}(k[Q])=\prod_{\Omega}(1+s_\Omega).}
\]
Moreover, for each orbit the Fourier coordinates of an idempotent are either all zero or all nonzero; in the latter case they are precisely the elements of \(\ker(M_\Omega:(\mathbb Z/N\mathbb Z)^\Omega\to(\mathbb Z/N\mathbb Z)^{2|\Omega|})\), read as exponents of a generator of \(\mathbb F_{q^L}^{\times}\). Choices on distinct orbits are independent. Exactly half of all idempotents have augmentation zero and half augmentation one.

**Closed midpoint specialization.** If \(|G|\) is odd and \(\varphi=\frac12\operatorname{id}_G\), let \(T\chi=\chi^2\) on \(\widehat G\). For each \(F\)-orbit \(\mathcal C\) on the set of \(T\)-orbits, choose a character \(\chi\) in one of its \(T\)-orbits. Let \(r\) be its \(T\)-orbit length, \(s\) the length of \(\mathcal C\), and \(0\le h<r\) be determined by \(F^s\chi=T^h\chi\). Then
\[
\boxed{\#\operatorname{Idem}(k[G_{\mathrm{mid}}])=\prod_{\mathcal C}\left(1+\gcd(2^r-1,q^s-2^h)\right).}
\]
In particular, **for every power of two \(q\)** this count is exactly \(2^{|G|}\), since the idempotents are precisely the vectors whose natural-basis coefficients belong to \(\mathbb F_2\).

## Assumptions and scope
The base field is finite; its characteristic does not divide the order of \(G\). The group \(G\) need not be cyclic or of odd order for the main theorem. The map \(1-\varphi\) must be an automorphism (the Latin/connected Alexander condition). The midpoint specialization requires odd order so division by two is defined in \(G\). The groups and permutation actions, and all Smith invariants, are finite and explicitly computable from an invariant-factor presentation of \(G\). This does **not** claim a formula in modular characteristic dividing \(|G|\), nor for non-Latin Alexander quandles.

## Proof
**1. Fourier isomorphism and multiplication.** Identify the underlying vector space of \(k[Q]\) with \(k[G]\), writing \(e_g\leftrightarrow X^g\). The quandle product is \(u\star v=\varphi_*(u)(1-\varphi)_*(v)\), the right-hand product being ordinary group-ring multiplication. The exponent condition on \(L\) and \(\operatorname{char}k\nmid |G|\) give the invertible Fourier isomorphism
\[
k[G]\otimes_k\mathbb F_{q^L}\longrightarrow\mathbb F_{q^L}^{\widehat G},\qquad z_\chi=\sum_{g\in G}a_g\chi(g).
\]
By direct substitution, \(z_\chi(u\star v)=z_{A\chi}(u)z_{B\chi}(v)\). Thus \(u\star u=u\) is equivalent, in every character coordinate, to \(z_\chi=z_{A\chi}z_{B\chi}\).

**2. Descent to the ground field.** A vector of Fourier coordinates comes from \(k[G]\), rather than only the splitting extension, if and only if
\[
z_{F\chi}=z_\chi^q\qquad(\chi\in\widehat G).
\]
Necessity follows from raising its defining character sum to the \(q\)-th power. For sufficiency, apply the inverse Fourier formula
\[
a_g=\frac1{|G|}\sum_{\chi\in\widehat G}z_\chi\chi(g)^{-1}.
\]
The stated relation and the permutation \(F\) show \(a_g^q=a_g\). Hence every coefficient belongs to \(\mathbb F_q\). This proves that no extraneous splitting-field solutions are counted.

**3. Zero support is a union of full orbits.** If \(z_\chi\ne0\), then the idempotent equation forces both \(z_{A\chi}\ne0\) and \(z_{B\chi}\ne0\). Because \(A,B\) are finite permutations, iterating yields invariance under both and their inverses. The Frobenius equation makes zero/nonzero status invariant under \(F\). Thus the nonzero support is a union of entire \(\langle A,B,F\rangle\)-orbits. Setting all coordinates on an orbit to zero satisfies both equations, independently of other orbits.

**4. Linearizing each nonzero orbit and counting.** Fix a generator \(\zeta\) of the cyclic group \(\mathbb F_{q^L}^{\times}\). On a selected orbit \(\Omega\), write \(z_\chi=\zeta^{v_\chi}\), with \(v_\chi\in\mathbb Z/N\mathbb Z\). Both sets of equations become exactly \(M_\Omega v=0\pmod N\). Integer unimodular row and column operations put \(M_\Omega\) into Smith diagonal form without changing the kernel cardinality over \(\mathbb Z/N\mathbb Z\). A diagonal entry \(d\ne0\) admits \(\gcd(N,d)\) solutions, and a zero column admits \(N\) solutions. This yields \(s_\Omega\) and the product formula. The trivial character is a singleton orbit and has \(z_{\mathbf1}\in\{0,1\}\); it is independent of all others and equals augmentation, proving the equal split.

**5. Midpoint simplification.** With \(\varphi=1-\varphi=\frac12\), the Fourier equation becomes \(z_{T\chi}=z_\chi^2\) for \(T\chi=\chi^2\). On a \(T\)-cycle of length \(r\), choose \(t=z_\chi\). Its other entries are \(t^{2^j}\); consistency forces either \(t=0\) or \(t^{2^r-1}=1\). Frobenius permutes these cycles. If its return after \(s\) steps is \(T^h\chi\), descent is exactly \(t^{q^s}=t^{2^h}\). Since \(q^s-2^h\) is prime to the field characteristic, the common multiplicative roots number \(\gcd(2^r-1,q^s-2^h)\). Include the zero choice and multiply. In characteristic two, commutativity of midpoint multiplication cancels off-diagonal square terms, so directly \((\sum_ga_ge_g)^2=\sum_ga_g^2e_g\); fixed coefficients are exactly \(\mathbb F_2\). The count follows. \(\square\)

## Verification
The accompanying `verify.py` reconstructs the cyclic-character orbits and integer Smith matrices; it compares calculated exact counts with exhaustive direct multiplication checks for 14 small cyclic prime-field instances and one non-scalar, two-generator instance. It also directly verifies midpoint counts over extension fields of orders four and eight using polynomial finite-field arithmetic. Execute `python verify.py` after installing the declared `sympy` requirement. These finite checks are independent regression tests, not proofs of the universal result. Illustrative outputs: for \(G=\mathbb Z/5\mathbb Z\), \(\varphi(g)=2g\), and \(k=\mathbb F_2\), the count is \(12\); for the midpoint \(\varphi(g)=3g\), it is \(32\). For \(G=(\mathbb Z/3\mathbb Z)^2\), with \(\varphi\) represented by \(\begin{psmallmatrix}0&2\\1&1\end{psmallmatrix}\) over \(\mathbb Z/3\mathbb Z\), the count over \(\mathbb F_2\) is \(80\), rather than the midpoint count of \(512\).

## Relationship to prior work
Zhang's 2026 group-ring transport and Fourier identity provide the starting multiplication formula, and his Theorem 5.2 classifies **integral** idempotents of midpoint quandles, not finite-field idempotents. The present result uses Frobenius descent, full-support orbit decomposition and Smith normal forms to give **complete finite-field counts for all connected Alexander quandles**, including noncommutative and nonsplitting-field cases. Work of Elhamdadi, Ta and Virgin establishes a Fourier approach to **integral** quandle-ring idempotents, while Ta's 2026 midpoint characterization extends the closed specialization to all finite medial commutative quandles.

## Limitations
Novelty is assessed against accessible sources rather than certified universally: an equivalent description under monomial dynamical equations or quandle-algebra character lattices may exist; full text for Elhamdadi–Ta–Virgin (arXiv:2609.03799) was unavailable for section-by-section comparison, although its public abstract emphasizes integral idempotents. A 2024 Fernando–Wu conference abstract reports finite-field idempotent work without an accessible theorem statement; general coverage is unresolved. This is an explicit enumerative algorithm, not a complexity bound or a closed elementary expression for every action.

## References
1. Zhi-Lin Zhang, *Group-ring methods for Alexander quandle rings*, arXiv:2610.08204v1, first submitted 2026-10-06, Sections 2 and 5: https://arxiv.org/html/2610.08204v1.
2. Mohamed Elhamdadi, Lực Ta, Bryce Virgin, *Fourier Analysis and Idempotents in Quandle Algebras*, arXiv:2609.03799v1 (2026-09-03): https://arxiv.org/abs/2609.03799.
3. Lực Ta, *On medial Latin quandles and affine modules*, *Canadian Mathematical Bulletin* (2026), Corollary 4.2: https://www.cambridge.org/core/journals/canadian-mathematical-bulletin/article/on-medial-latin-quandles-and-affine-modules/25AB10790DD974EA3D7B327E9830818E.
4. Gregory Churchill, Indu Rasika Churchill, Neranga Fernando and Bhitali Kousik, *A further study of quandles and quandle rings*, arXiv:2608.09149 (2026-08-10): https://arxiv.org/abs/2608.09149.
5. Neranga Fernando and Zhaoqi Wu, *Idempotents and Tripotents in Quandle Rings*, Canadian Mathematical Society Winter Meeting abstract (2024): https://www2.cms.math.ca/Events/winter24/abs/ffa.
