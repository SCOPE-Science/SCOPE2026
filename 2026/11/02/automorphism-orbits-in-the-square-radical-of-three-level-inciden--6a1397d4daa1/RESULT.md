# Automorphism orbits in the square radical of three-level incidence algebras

## Finding
Let \(q\) be a prime power, \(s,t\geq1\), and let \(P_{2,s,t}\) be the ordinal sum of three antichains of sizes \(2,s,t\). Write \(A=I(P_{2,s,t};\mathbb F_q)\) for its incidence algebra and \(J\) for its Jacobson radical. The full group of \(\mathbb F_q\)-algebra automorphisms of \(A\) acts on \(J^2\), which is naturally \(M_{2\times t}(\mathbb F_q)\), as **all** left and right monomial transformations. This orbit relation, notably, is independent of the middle-layer size \(s\).

Set \(N=q-1\). If \(O_t(q)\) denotes the number of automorphism orbits in \(J^2\), define \(F_q(z)=\sum_{t\geq0}O_t(q)z^t\), with the formal constant term specifying the natural empty-column extension. Then
\[
F_q(z)=\frac1{2N}\left(\frac1{(1-z)^3}\sum_{d\mid N}\frac{\varphi(d)}{(1-z^d)^{N/d}}+R_N(z)\right),
\]
where \(\varphi\) is Euler's totient function, and
\[
R_N(z)=\begin{cases}
\displaystyle\frac{N}{(1-z)^2(1-z^2)^{(N+1)/2}},&N\text{ odd},\\[5pt]
\displaystyle\frac N2\left(\frac1{(1-z)^3(1-z^2)^{N/2}}+\frac1{(1-z)(1-z^2)^{N/2+1}}\right),&N\text{ even}.
\end{cases}
\]
In particular \(O_1(q)=3\) and \(O_2(q)=7+\lfloor(q-1)/2\rfloor\). For every \(t\geq1\), the rank-zero, rank-one, and rank-two orbit counts are exactly \(1\), \(2t\), and \(O_t(q)-2t-1\), respectively. For each fixed \(q\), the orbit sequence is quasipolynomial in \(t\) and satisfies
\[
O_t(q)=\frac{t^{q+1}}{2(q-1)(q+1)!}+O_q(t^q).
\]

## Assumptions and scope
An incidence algebra over a finite poset has a basis \(E_{uv}\) for comparable pairs \(u\leq v\), multiplied by \(E_{uv}E_{xy}=\delta_{v,x}E_{uy}\). The radical \(J\) consists of off-diagonal incidence functions. For \(P_{2,s,t}\), the top-to-bottom interval entries, indexed by two bottom and \(t\) top points, span \(J^2\). Since there are only three ranks, \(J^3=0\). The middle antichain is nonempty, ensuring each bottom-to-top pair factors through it.

The automorphisms are \(\mathbb F_q\)-linear unital algebra automorphisms, not arbitrary semilinear automorphisms. The orbit action is on **individual elements of \(J^2\)**, not on the full radical or on the set of subalgebras. The coefficient-extraction identity for \(F_q\) is interpreted as a formal-power-series identity.

## Proof
### 1. Identify the exact automorphism action
The radical is characteristic, hence so is its square. The quotient \(A/J\) is a product of \(2+s+t\) copies of \(\mathbb F_q\). An algebra automorphism permutes its primitive central idempotents. The bimodule \(e_u(J/J^2)e_v\) is nonzero exactly when \(u<v\) is a covering relation; together with \(e_uJ^2e_v\) this reconstructs the original poset order. Thus the induced permutation is a poset automorphism, necessarily preserving the three ranks and permuting the two bottom points and \(t\) top points separately.

After composing with the inverse poset automorphism, the induced action on \(A/J\) fixes each coordinate. Standard lifting and simultaneous conjugacy of complete primitive orthogonal idempotent systems over a nilpotent ideal allow conjugation by a unit so that every standard diagonal idempotent \(E_{uu}\) is fixed. This is also the elementary special case of the classical incidence-algebra automorphism decomposition. Since each corner \(E_{uu}AE_{vv}\), for \(u\leq v\), has dimension one, the remaining automorphism sends \(E_{uv}\) to \(c_{uv}E_{uv}\) for some nonzero scalar. Multiplication along \(u<w<v\) imposes \(c_{uv}=c_{uw}c_{wv}\). Fixing any middle point \(w_0\) shows that for bottom \(i\) and top \(j\), \(c_{ij}=c_{i w_0}c_{w_0 j}\). Thus the induced action on \(J^2\) is a product of independent row and column diagonal scalings, followed by row/column permutations.

Conjugation by an arbitrary unit \(d+n\), where \(d\) is an invertible diagonal element and \(n\in J\), acts on \(J^2\) in exactly the same way as conjugation by \(d\): both additional commutator contributions contain \(JJ^2\) or \(J^2J\), which vanish. Every independent row and column scaling on \(J^2\) arises from conjugation by a diagonal unit (choose its two bottom and \(t\) top diagonal entries independently), and every row/column permutation arises from a poset automorphism. Hence the group action is exactly double monomial equivalence, not merely contained in it.

### 2. Reduce matrices to projective multisets
Right diagonal scalings identify each nonzero matrix column with its projective point in \(\mathbb P^1(\mathbb F_q)\); the zero column remains a separate symbol. Permuting the columns identifies a matrix with a multiset of size \(t\) drawn from the \(q+2\)-symbol alphabet \(X=\{\mathtt0\}\sqcup\mathbb P^1(\mathbb F_q)\). Independent row scalings induce \(z\mapsto a z\) on the \(N=q-1\) nonaxis projective ratios \(z\in\mathbb F_q^\times\), and the row swap induces \(z\mapsto a/z\). The two axial projective points are fixed by these rotations and interchanged by reflections; the zero-column symbol is fixed throughout. Therefore the remaining effective group is the dihedral-type normalizer \(H=\mathbb F_q^\times\rtimes C_2\), of order \(2N\), acting on multisets of \(X\). This description remains valid for \(N=1\).

### 3. Apply Burnside's lemma with cycle structure
For a permutation \(h\) with cycles of lengths \(\ell_1,\ldots,\ell_r\) on \(X\), the generating function for \(h\)-fixed multisets is \(\prod_{i=1}^r(1-z^{\ell_i})^{-1}\), since each multiplicity must be constant on a cycle. An element of the cyclic rotation subgroup of order \(d\mid N\) fixes the zero symbol and both axes and has \(N/d\) additional \(d\)-cycles. There are \(\varphi(d)\) such rotations, yielding the first summand.

A reflection maps a nonaxis ratio to \(a/z\). Its fixed ratios satisfy \(z^2=a\). If \(N\) is odd, there is one such ratio for each \(a\), hence each of the \(N\) reflections has two fixed symbols overall (that ratio and the zero column) and \((N+1)/2\) two-cycles (including the interchanged axes). If \(N\) is even, exactly half the \(a\)'s are squares: those reflections have three fixed symbols and \(N/2\) two-cycles; the others have one fixed symbol and \(N/2+1\) two-cycles. These are precisely the stated formulas for \(R_N(z)\). Division by \(2N\) proves the series formula.

### 4. Ranks and asymptotics
An element of rank zero is only the all-zero multiset. Rank one means precisely that every nonzero column occupies the same projective point. The support count \(r\in\{1,\ldots,t\}\) is invariant, while the projective group has exactly two point orbits: the two axes comprise one, and the \(N\) nonaxis ratios comprise the other. Hence there are \(2t\) rank-one orbits. Every remaining multiset has rank two, proving its count.

In the multiset Burnside sum, the identity element has \(q+2\) singleton cycles, so its contribution is \(\binom{t+q+1}{q+1}\); every nonidentity element moves at least two symbols, thus its fixed-multiset coefficient grows at most like \(O_q(t^q)\). Dividing by \(2N\) yields the leading asymptotic term. The displayed rational generating function has only roots of unity as poles, establishing quasipolynomiality by partial fractions.

## Verification
The standalone standard-library program `verify.py` evaluates the closed Burnside coefficients, independently enumerates projective multiset orbits under the finite normalizer action, and separately exhausts orbits of actual matrices under monomial generators for \(q\in\{2,3,4,5\}\), including the extension field \(\mathbb F_4\). It checks the exact rank-stratified formula, and reports `INCIDENCE_LOEWY_ORBITS_OK 23 independent parameter checks`. These finite checks support but do not replace the proof for all prime powers and all \(s,t\).

## Relationship to prior work
Classical structural descriptions of incidence-algebra automorphisms, including Baclawski (1972), Khripchenko (2010), and Brusamarello--Lewis (2011), account for the group-action reduction. The poset reconstruction and factorization of interval scalings should not be regarded as a new general automorphism classification. Gary Mullen (1981), Section 5, already counts matrix equivalence classes under **row and column permutations**, including the known seven-orbit example for \(2\times2\) binary matrices; this numerical special case is not new. Mullen's Section 6 also discusses larger permutation actions on the column-vector alphabet. Neither treatment determines the orbit relation under arbitrary independent **nonzero column scalings and row scalings** over all finite fields, nor the corresponding incidence-algebra \(J^2\) orbit profile and rank strata. The present contribution is this exact family-wide orbit classification and generating series, not the classical Burnside or Pólya method itself.

Can's 2021 work treats incidence monoids and torus double orbits of the whole monoid; its acting group and algebraic-geometric setting differ from the present finite-field automorphism action on \(J^2\). Exact equivalence with an unindexed specialized monomial-matrix enumeration cannot be conclusively excluded.

## Limitations
The theorem is for ordinal sums of antichains with exactly two bottom elements, at least one middle element and at least one top element. It does not enumerate the full radical \(J\), all incidence algebras, or orbits of full general linear row operations. The generating function is for the parameter \(t\) varying, not a Hilbert series of the algebra. A 2011 source was available only by abstract, and complete publication priority has not been independently established. No independent mathematical audit has been performed.

## References
1. K. Baclawski, *Automorphisms and derivations of incidence algebras*, Proc. Amer. Math. Soc. 36 (1972), 351--356. Full-text PDF: https://scispace.com/pdf/automorphisms-and-derivations-of-incidence-algebras-v963bb1zcf.pdf .
2. G. L. Mullen, *Permutation matrices and matrix equivalence over a finite field*, Internat. J. Math. Math. Sci. 4 (1981), 503--512. DOI: 10.1155/S0161171281000367 (Sections 5--6).
3. N. S. Khripchenko, *Automorphisms of finitary incidence rings*, Algebra Discrete Math. 9 (2010), no. 2, 78--97. Open full text: https://admjournal.luguniv.edu.ua/index.php/adm/article/download/632/166 .
4. R. Brusamarello and D. W. Lewis, *Automorphisms and involutions on incidence algebras*, Linear Multilinear Algebra (published online April 15, 2011). DOI: 10.1080/03081087.2010.496113 (abstract consulted).
5. M. B. Can, *Incidence monoids: automorphisms and complexity*, arXiv:2105.09826 (2021), https://arxiv.org/pdf/2105.09826 (full text consulted).
