# An arithmetic phase transition for fixed-point-free automorphisms of standard filiform Lie algebras

## Finding
Let \(n\ge4\) and let \(q\) be any prime power. Define the standard filiform Lie algebra \(L_n(\mathbb F_q)\) on a basis \(e_1,\ldots,e_n\) by \([e_1,e_i]=e_{i+1}\) for \(2\le i\le n-1\) and all other unordered basis brackets zero. An automorphism is *fixed-point-free* when its fixed vector space is zero.

Write \(\varphi_{\mathrm E}(t)\) for Euler's totient function. The exact number of fixed-point-free \(\mathbb F_q\)-linear Lie algebra automorphisms is
\[
F_n(q)=q^{2n-3}\sum_{\substack{t\mid(q-1)\\t>1}}\varphi_{\mathrm E}(t)\bigl(q-1-\min\{t,n-1\}\bigr).
\]
The complete automorphism group has order \(q^{2n-3}(q-1)^2\). In particular, the following criterion is exact:
\[
F_n(q)>0\quad\Longleftrightarrow\quad q>n\ \text{or}\ q-1\text{ is composite}.
\]
Here a *composite* integer has a proper divisor strictly between one and itself; in particular, one is not composite. Thus for every field size with \(q-1\) composite, fixed-point-free automorphisms occur in every dimension \(n\ge4\); when \(q-1\) is prime, they occur precisely for \(4\le n<q\). No restriction on the characteristic is imposed.

## Assumptions and scope
All automorphisms are ordinary \(\mathbb F_q\)-linear Lie algebra automorphisms of the explicitly displayed \(L_n\), not abstract additive-group automorphisms, group automorphisms, conjugacy classes, or automorphisms of arbitrary filiform algebras. The restriction \(n\ge4\) is essential to the characteristic-ideal argument. In dimension three, \(L_3\) is Heisenberg and its automorphism group is larger.

## Proof
**Step 1: recover the characteristic abelian ideal.** Set \(H=\langle e_2,\ldots,e_n\rangle\). It is abelian of codimension one. The derived algebra is \([L_n,L_n]=\langle e_3,\ldots,e_n\rangle\). For \(n\ge4\), \([e_1,e_3]=e_4\ne0\); because every bracket among members of \(H\) is zero, this proves
\[
H=C_{L_n}([L_n,L_n]).
\]
Consequently every automorphism preserves \(H\).

**Step 2: parametrize every automorphism, without field restrictions.** Write
\[
\Phi(e_1)=a e_1+\sum_{i=2}^n b_i e_i,\qquad
\Phi(e_2)=d e_2+\sum_{i=3}^n c_i e_i,
\]
where \(a,d\in\mathbb F_q^\times\), and all \(b_i,c_i\in\mathbb F_q\) are arbitrary. Define recursively
\[
\Phi(e_{i+1})=[\Phi(e_1),\Phi(e_i)]\qquad(2\le i\le n-1).
\]
On the abelian ideal \(H\), the adjoint action of \(\Phi(e_1)\) equals \(a\) times the forward-shift map \(e_i\mapsto e_{i+1}\). The recursion therefore preserves every original bracket, including all zero brackets, in any characteristic. Its matrix is lower triangular with diagonal
\[
a,\quad d,\quad ad,\quad a^2d,\ \ldots,\ a^{n-2}d.
\]
It is invertible because \(ad\ne0\). Conversely, every automorphism must have the displayed first two columns by preservation of \(H\) and the lower central series; recursion then forces all other columns. In particular the parametrization is *unique*, with precisely \(2n-3\) free additive coefficients. Thus \(|\operatorname{Aut}(L_n(\mathbb F_q))|=q^{2n-3}(q-1)^2\).

**Step 3: fixed points reduce to a multiplicative order condition.** Since the matrix is triangular, \(\Phi-I\) is invertible exactly when
\[
a\ne1,\qquad d\ne a^{-j}\quad\text{for every }0\le j\le n-2.
\]
For a fixed \(a\) of multiplicative order \(t>1\), the excluded elements \(a^{-j}\) number exactly \(\min(t,n-1)\). Therefore \(q-1-\min(t,n-1)\) values of \(d\) remain, and every permissible \((a,d)\) has exactly \(q^{2n-3}\) distinct lifts to automorphisms. Because \(\mathbb F_q^\times\) is cyclic, it has exactly \(\varphi_{\mathrm E}(t)\) elements of order \(t\) for each divisor \(t\) of \(q-1\). Summation yields the formula.

**Step 4: prove the existence dichotomy.** If \(q>n\), choose a generator \(a\) of \(\mathbb F_q^\times\), of order \(q-1>n-1\); then there is at least one admissible \(d\). If \(q\le n\), every possible order \(t\) satisfies \(t\le q-1\le n-1\), so a positive summand occurs precisely when a divisor \(t\) obeys \(1<t<q-1\). This is equivalent to \(q-1\) being composite. These implications also cover \(q=2\) and all positive characteristics.

## Verification
The accompanying standalone `verify.py` reconstructs Lie brackets from basis vectors, recursively builds automorphism matrices, tests *all* defining and zero bracket relations, and computes ranks of both the automorphism matrix and the matrix minus the identity over finite fields. It exhaustively tests five configurations: \((n,q)=(4,2),(5,2),(4,3),(4,4),(4,5)\), including full enumeration of all additive shear coefficients. Eight further configurations independently test all multiplicative parameter pairs with sampled shears. The code uses explicit polynomial-basis arithmetic for \(\mathbb F_4\) and \(\mathbb F_8\). It also compares the order-divisor formula with an independent direct enumeration of nonzero field parameters. The executable produces `verify_output.txt`, ending in `FILIFORM_FIXED_POINT_FREE_COUNTS_OK 13_CONFIGURATIONS`.

For example, over \(\mathbb F_5\) the four-dimensional Lie algebra has exactly \(12{,}500\) fixed-point-free automorphisms out of \(50{,}000\) total. Over \(\mathbb F_8\), dimension five has \(37{,}748{,}736\) such automorphisms, whereas dimension eight has none. These finite tests support the proof but are not a proof for arbitrary \(n\) and \(q\).

## Relationship to prior work
The classical standard filiform bracket and the broader problem of filiform degeneration occur in Herrera-Granada and Tirao's 2013 work, which establishes its primary Lie-algebra context but neither an automorphism census nor this finite-field obstruction. Burde and Dekimpe's 2026 paper gives a structurally closer fixed-point-free existence theorem for **complex** filiform Lie algebras (Theorem 6.5); that theorem does not determine a finite-field count or the present dependence on the factorization of \(q-1\). Falcón et al. (2016) classify filiform Lie algebras of dimensions at most seven over small finite fields, a different invariant from the full automorphism fixed-space distribution in unbounded dimension; its complete text was not available for direct comparison here.

Related exact finite-field counts for the three-dimensional Heisenberg Lie algebra concern an algebra with a larger automorphism group and do not imply this formula for \(n\ge4\). A separate finite-field adjoint-rank spectrum for two filiform families counts Lie algebra elements, not fixed-point-free automorphisms. Searches for equivalent formulations, general almost-abelian automorphism formulas and finite-field counting coverage found no direct match; this lack of a match is not a proof of historical novelty.

## Limitations
This is a theorem about ordinary linear automorphisms of the standard graded filiform Lie algebra, not about all filiform isomorphism classes, class-preserving or higher-order automorphisms, or all fixed-space dimensions. It does not determine automorphism conjugacy classes or the order distribution of fixed-point-free automorphisms. The intrinsic characteristic-ideal proof does not apply in dimension three. Independent mathematical review and exhaustive historical priority checking have not been performed; another general formula for automorphisms of almost-abelian nilpotent Lie algebras could subsume part or all of the count.

## References
1. J. F. Herrera-Granada and P. Tirao, *Filiform Lie algebras of dimension 8 as degenerations*, arXiv:1308.4580v1, publicly posted 21 August 2013. https://arxiv.org/html/1308.4580v1
2. D. Burde and K. Dekimpe, *Fixed-point-free automorphisms of solvable Lie algebras*, arXiv:2604.27916v1, publicly posted 30 April 2026; see Section 6, especially Definition 6.1 and Theorem 6.5. https://arxiv.org/html/2604.27916v1
3. Ó. J. Falcón, R. M. Falcón, J. Núñez, A. M. Pacheco and M. T. Villar, *Classification of Filiform Lie Algebras up to dimension 7 Over Finite Fields*, An. Şt. Univ. Ovidius Constanţa **24** (2016), 185–204, doi:10.1515/auom-2016-0036. The complete text was not inspected.
