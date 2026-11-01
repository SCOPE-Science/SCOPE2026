# A four-phase parity law for heterogeneous self-feedback in all-to-all XOR networks

## Finding

Fix a finite field \(\mathbb F_q\) of characteristic two, where \(q=2^k\) and \(k\ge1\). Partition the vertices of the complete graph into a set \(U\) of \(a\ge2\) vertices with no self-feedback and a set \(L\) of \(b\ge2\) vertices with self-feedback. A vertex in \(U\) replaces its value by the sum of all *other* vertex values, whereas a vertex in \(L\) sums the values of *all* vertices, including itself. All updates are simultaneous and addition is in \(\mathbb F_q\). Put \(n=a+b\) and let \(F\) be the resulting linear update. A loop means that the vertex's own state is included exactly once.

Write \(J_m(\lambda)\) for a Jordan block of size \(m\) with eigenvalue \(\lambda\), and \(C(g)\) for the companion matrix of \(g(X)=X^2+X+1\). The rational/Jordan block decomposition over \(\mathbb F_q\) is exactly

\[
\begin{array}{c|l}
(a\bmod2,b\bmod2)& \text{block decomposition}\hline
(1,1)&J_1(0)^{\oplus(b-1)}\oplus J_1(1)^{\oplus(a-1)}\oplus C(g)\\
(1,0)&J_3(0)\oplus J_1(0)^{\oplus(b-2)}\oplus J_1(1)^{\oplus(a-1)}\\
(0,1)&J_1(0)^{\oplus(b-1)}\oplus J_3(1)\oplus J_1(1)^{\oplus(a-2)}\\
(0,0)&J_2(0)\oplus J_1(0)^{\oplus(b-2)}\oplus J_2(1)\oplus J_1(1)^{\oplus(a-2)}.
\end{array}
\]

The companion notation describes the same two-dimensional order-three operator even when \(g\) splits over \(\mathbb F_q\). Consequently, the *only* primitive orbit lengths and the maximal first-periodic-entry time \(T_{\max}\) are

\[
\begin{array}{c|c|c}
(a\bmod2,b\bmod2)&\text{primitive periods that occur}&T_{\max}\\\hline
(1,1)&1,3&1\\
(1,0)&1&3\\
(0,1)&1,2,4&1\\
(0,0)&1,2&2.
\end{array}
\]

Let \(C_d\) denote the number of *distinct primitive orbits* of length \(d\). Every unlisted \(C_d\) is zero, and all entries in the next table are exact:

\[
\begin{array}{c|c|c|c|c}
(a\bmod2,b\bmod2)&C_1&C_2&C_3&C_4\\\hline
(1,1)&q^{a-1}&0&(q^{a+1}-q^{a-1})/3&0\\
(1,0)&q^{a-1}&0&0&0\\
(0,1)&q^{a-1}&(q^a-q^{a-1})/2&0&(q^{a+1}-q^a)/4\\
(0,0)&q^{a-1}&(q^a-q^{a-1})/2&0&0.
\end{array}
\]

For every integer \(t\ge0\), write \(H_t=\#\{x:T(x)\le t\}\), with \(T(x)\) the first time that the trajectory enters any periodic orbit. The complete entry-time distribution is determined by

\[
\begin{array}{c|c|c|c|c}
(a\bmod2,b\bmod2)&H_0&H_1&H_2&H_3\\\hline
(1,1)&q^{a+1}&q^n&q^n&q^n\\
(1,0)&q^{a-1}&q^{n-2}&q^{n-1}&q^n\\
(0,1)&q^{a+1}&q^n&q^n&q^n\\
(0,0)&q^a&q^{n-1}&q^n&q^n.
\end{array}
\]

Thus \(\#\{T=0\}=H_0\) and \(\#\{T=t\}=H_t-H_{t-1}\) for \(t\ge1\). In particular, when both group sizes are odd, a nontrivial period-three population appears even though neither homogeneous endpoint (every vertex including itself or no vertex including itself) can have period three. The four parity regimes are distinct already at the level of allowed primitive periods or maximal transients.

## Assumptions and scope

All configurations are labelled vectors in \(\mathbb F_q^n\), and their orbits are temporal orbits, not quotients by vertex permutations. The two groups are fixed, and the local rule uses each nonself neighbor exactly once. Only \(a,b\ge2\) are asserted; the homogeneous endpoints are mentioned solely as contrast and are not part of the displayed classification. For \(q>2\), the model is a characteristic-two additive finite-state network rather than a Boolean-valued network. No probabilistic assumptions are needed; the uniform fractions follow by dividing configuration counts by \(q^n\).

## Proof

**1. Global matrix and characteristic polynomial.** For \(x=(x_U,x_L)\), set \(s=\sum_{i=1}^n x_i\). Directly from the rule,
\[
F(x)=(x_U+s\mathbf1_a,\ s\mathbf1_b).
\]
Equivalently, with \(D=\operatorname{diag}(I_a,0_b)\) and \(J=\mathbf1_n\mathbf1_n^{\mathsf T}\), \(F=D+J\). In the rational function field of characteristic two, the matrix determinant lemma gives
\[
\begin{split}
\chi_F(X)&=\det(XI-F)\\
&=X^b(X+1)^a\left(1+\frac{a\bmod2}{X+1}+\frac{b\bmod2}{X}\right)\\
&=X^{b-1}(X+1)^{a-1}\left[X^2+(1+\bar a+\bar b)X+\bar b\right],
\end{split}
\]
where \(\bar a=a\bmod2\) and \(\bar b=b\bmod2\) are interpreted in the field. The displayed identity is a polynomial identity after clearing denominators; no inverses at \(X=0,1\) are being assumed.

**2. Critical kernel calculations.** If \(Fx=0\), its \(L\)-coordinates force \(s=0\), its \(U\)-coordinates then force \(x_U=0\), and its remaining constraint is \(\sum_Lx_i=0\). Hence \(\dim\ker F=b-1\). Let \(u=\sum_Ux_i\). The total sum after one update is \(s'=u+(\bar a+\bar b)s\), and
\[
F^2x=(x_U+(s+s')\mathbf1_a,\ s'\mathbf1_b).
\]
Thus \(F^2x=0\) exactly when \(s'=0\) and \(x_U=s\mathbf1_a\); those conditions imply \(\bar b s=0\) and \(\sum_L x_i=(1+\bar a)s\). It follows, without any division by group sizes, that
\[
\dim\ker F^2=\begin{cases}b-1,&b\text{ odd},\\ b,&b\text{ even}.\end{cases}
\]
The operator \(F+I\) is of the same form after exchanging the roles and sizes of \(U\) and \(L\): its diagonal part is one on \(L\) and zero on \(U\), while its rank-one part is still \(J\). Therefore
\[
\dim\ker(F+I)=a-1,\qquad
\dim\ker(F+I)^2=\begin{cases}a-1,&a\text{ odd},\\a,&a\text{ even}.\end{cases}
\]

**3. Exhaustion of blocks.** The characteristic polynomial gives the algebraic multiplicities at zero and one and, precisely when both sizes are odd, an additional quadratic \(g(X)=X^2+X+1\). The two displayed pairs of nullities give the number of Jordan blocks and the number of blocks of length at least two at each linear eigenvalue. When a group size is even, the algebraic multiplicity exceeds the number of blocks by one (giving one size-two block) or by two (giving one size-three block, since the second nullity grows by only one). These conditions uniquely force all four rows of the block table. For both sizes odd, \(g\) gives a two-dimensional cyclic summand of order three, since \(g(X)\) divides \(X^3-1\) but not \(X-1\). This calculation is valid over every field of characteristic two; extension of scalars does not change the polynomial identities or kernel dimensions.

**4. Primitive cycles.** The nonsingular blocks are either identity blocks, one size-two or size-three unipotent block, or the order-three companion block. In characteristic two, \(J_2(1)\) has order two and \(J_3(1)\) has order four. The fixed subspaces of powers have dimensions \(a-1\) at time one in all four cases; the dimensions at times two, three and four are, respectively, \((a-1,a+1,a-1)\) for odd/odd, \((a-1,a-1,a-1)\) for odd/even, \((a,a-1,a+1)\) for even/odd, and \((a,a-1,a)\) for even/even. A nilpotent coordinate cannot lie in a nonzero periodic orbit. Consequently the numbers of periodic configurations fixed by each indicated power are \(q\) raised to those dimensions. Inclusion-exclusion over divisors, \(\#\operatorname{Fix}(F^d)=\sum_{e\mid d}e C_e\), yields the entire primitive-orbit table. Positive counts verify that every listed length actually occurs.

**5. Exact transient shells.** Fitting decomposition splits the vector space into an invertible summand of dimension \(r\) and nilpotent blocks of lengths \(\ell_1,\ldots,\ell_m\). The condition \(T(x)\le t\) is equivalent to the nilpotent coordinate lying in \(\ker N^t\), so the number of such configurations is \(q^{r+\sum_j\min(t,\ell_j)}\). Substituting the four previously proved block lists gives every entry in the table of \(H_t\). The displayed maximum times are sharp because every specified largest nilpotent Jordan block exists for the entire stated parameter range.

**6. Homogeneous contrast.** With no self-feedback the matrix is \(I+J\); with self-feedback everywhere it is \(J\). Since \(J^2=(n\bmod2)J\), each homogeneous update has eventual period dividing two. In the mixed odd/odd case, by contrast, the \(g\)-summand creates period-three orbits. Thus the new odd period is caused by heterogeneous self-inclusion, not by an overlooked homogeneous cycle.

## Verification

Run `python verify.py` using Python 3 and its standard library. The program constructs every update directly as an XOR of permitted neighbor contributions, independent of the characteristic-polynomial derivation. It compares predicted ranks of five powers of both \(F\) and \(F+I\) for all 169 ordered pairs \(2\le a,b\le14\); checks stabilized-period power identities; exhaustively classifies 11,280 labelled binary configurations for 24 ordered pairs with \(2\le a,b\le6\) and \(a+b\le11\); and exhaustively classifies 47,360 labelled configurations over \(\mathbb F_4\) for eight small parameter pairs. Since the updates use only field addition and coefficients zero or one, the \(\mathbb F_4\) checks may encode field addition as bitwise XOR. All 2,235 assertions passed. The recorded output is in `verification_output.txt`. Finite checks corroborate rather than replace the all-parameter proof above.

## Relationship to prior work

Hernández Toledo's *Linear finite dynamical systems* (2005) supplies the classical general Fitting and cycle-decomposition framework but no inspected group-parity formula for a heterogeneous complete graph. Aledo, Martínez and Valverde's 2015 survey treats general parallel Boolean graph dynamics and explicitly discusses XOR, while their paper on general Boolean states treats maxterm/minterm and independently chosen OR/AND/NOR/NAND updates; neither inspected full text gives this mixed-XOR classification. The published *Sharp period-four census for complete multipartite parity automata* (2026) covers uniform self-exclusive and uniform self-inclusive XOR on complete multipartite graphs, with only periods one, two and four; its complete theorem does not cover a vertex-dependent mixture of those two rules and does not imply the appearance of period three here. Kozerenko and Valverde's *Periods in XOR parallel dynamical systems over directed dependency graphs* (published 2019/2020) investigates complete digraphs and other families; the available abstract is relevant, but a full-text comparison of arbitrary partial self-loop sets was not possible. The claimed contribution is specifically the all-parameter heterogeneous four-regime Jordan, period and transient census, not the general finite-field decomposition method.

## Limitations

The theorem requires characteristic two, complete off-diagonal interaction, synchronous updates and both feedback classes of cardinality at least two. It does not cover arbitrary heterogeneous graph edge sets, nonlinear local functions, or fields of odd characteristic. Full-text equivalence with the relevant 2019/2020 XOR-digraph paper remains an explicitly unresolved historical risk; the existence of a proof here and unsuccessful exact-keyword searches do not establish universal novelty. Independent verification by other researchers has not been performed.

## References

1. J. A. Aledo, S. Martínez and J. C. Valverde, *Parallel Dynamical Systems over Graphs and Related Topics: A Survey*, Journal of Applied Mathematics 2015, article 594294, first online 24 March 2015, DOI: 10.1155/2015/594294.
2. J. A. Aledo, S. Martínez and J. C. Valverde, *Graph dynamical systems with general Boolean states*, Applied Mathematics & Information Sciences 9 (2015), 1803--1808, DOI: 10.12785/amis/090417.
3. R. A. Hernández Toledo, *Linear finite dynamical systems*, Communications in Algebra 33 (2005), 2977--2989, DOI: 10.1081/AGB-200066211.
4. S. Kozerenko and J. C. Valverde, *Periods in XOR parallel dynamical systems over directed dependency graphs*, Journal of Computational and Applied Mathematics 364 (2020), 112313, DOI: 10.1016/j.cam.2019.06.029.
5. *Sharp period-four census for complete multipartite parity automata*, publicly available mathematical research record (2026), complete theorem and proof inspected.
