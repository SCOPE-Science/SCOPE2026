# Free algebra modulo compact operators on a countable tree of ℓp spaces

## Statement

Let \(\mathbb F\) be either \(\mathbb R\) or \(\mathbb C\), let
\[
\mathcal T=\{0,1\}^{<\mathbb N},
\qquad
E_s=\ell_{|s|+1}(\mathbb F),
\]
and form the Hilbertian direct sum
\[
X=\left(\bigoplus_{s\in\mathcal T} E_s\right)_2.
\]
Write \(\mathcal{SS}(X)\) and \(\mathcal K(X)\) for the strictly singular and compact operators on \(X\).

There exist two operators \(S_0,S_1\in\mathcal{SS}(X)\setminus\mathcal K(X)\) such that the assignment
\[
z_i\longmapsto S_i+\mathcal K(X)\qquad(i=0,1)
\]
extends to an injective algebra homomorphism
\[
\mathbb F\langle z_0,z_1\rangle_+
\hookrightarrow
\mathcal{SS}(X)/\mathcal K(X),
\]
where \(\mathbb F\langle z_0,z_1\rangle_+\) denotes the free non-unital associative algebra on two generators.

Equivalently, every nonzero noncommutative polynomial in \(S_0,S_1\) with zero constant term is noncompact. In particular, \(\mathcal{SS}(X)/\mathcal K(X)\) is neither nil nor nilpotent.

## Construction

For \(n\ge 0\), let
\[
J_n:\ell_{n+1}\longrightarrow\ell_{n+2}
\]
be the formal coordinate inclusion and put \(a_n=2^{-(n+1)}\). Each \(J_n\) is finitely strictly singular, hence strictly singular, and is noncompact.

For a node \(s\in\mathcal T\), let \(P_s:X\to E_s\) and \(I_s:E_s\to X\) be the canonical coordinate projection and injection. For \(i\in\{0,1\}\), define
\[
S_i x
=
\sum_{s\in\mathcal T}
a_{|s|}\,I_{si}J_{|s|}P_sx.
\]
The summands have pairwise disjoint source and target coordinates, so \(S_i\) is bounded and
\[
\|S_i\|\le \sup_{n\ge0}a_n=\frac12.
\]

## Proof of strict singularity

Let
\[
S_i^{(N)}=
\sum_{|s|\le N}
a_{|s|}\,I_{si}J_{|s|}P_s.
\]
There are only finitely many nodes with \(|s|\le N\). Every summand is strictly singular because \(J_{|s|}\) is strictly singular and the strictly singular operators form an operator ideal. Hence each \(S_i^{(N)}\) is strictly singular.

Moreover,
\[
\|S_i-S_i^{(N)}\|
\le \sup_{n>N}a_n
=2^{-(N+2)}\longrightarrow0.
\]
Since the strictly singular operators form a norm-closed ideal, \(S_i\) is strictly singular.

The restriction of \(S_i\) from the root block \(E_\varnothing=\ell_1\) to the child block \(E_i=\ell_2\) is \(\frac12 J_0\), which is noncompact. Thus \(S_i\notin\mathcal K(X)\).

## No polynomial relation modulo compact operators

For a nonempty binary word \(u=u_1\cdots u_m\), define
\[
S_u=S_{u_m}\cdots S_{u_1},
\qquad
b_m=\prod_{j=0}^{m-1}a_j.
\]
Starting from the root block, \(S_u\) follows the unique branch labelled by \(u\). Consequently,
\[
P_uS_uI_\varnothing=b_m J_{0,m},
\]
where \(J_{0,m}:\ell_1\to\ell_{m+1}\) is the formal inclusion, while
\[
P_vS_uI_\varnothing=0
\]
for every node \(v\ne u\) with \(|v|=m\). Words of different lengths land on different levels.

Now let
\[
Q=\sum_{u\in F}c_uS_u
\]
be a nonzero finite linear combination of distinct nonempty words. For the standard unit vectors \((e_j)\) of the root copy of \(\ell_1\),
\[
QI_\varnothing e_j
=
\big(c_u b_{|u|}e_j\big)_{u\in F}
\]
inside the finite direct sum of the descendant blocks indexed by \(F\). Hence for \(j\ne k\),
\[
\|QI_\varnothing(e_j-e_k)\|_X^2
=
\sum_{u\in F}
|c_u|^2 b_{|u|}^2
\,2^{\,2/(|u|+1)}>0,
\]
and the right-hand side is independent of \(j,k\). Therefore \((QI_\varnothing e_j)\) has no Cauchy subsequence, so \(QI_\varnothing\), and hence \(Q\), is noncompact.

Every such \(Q\) is strictly singular because it is a finite sum of products containing strictly singular factors. Thus its coset in \(\mathcal{SS}(X)/\mathcal K(X)\) is nonzero. Distinct noncommutative polynomials therefore remain distinct modulo \(\mathcal K(X)\), proving the claimed free-algebra embedding.

## Context

Kato introduced strictly singular operators as a compact-like perturbation class. A classical source of noncompact strictly singular maps is the formal inclusion \(\ell_p\to\ell_q\) for \(p<q\); Milman's 1970 result proves these inclusions are in fact finitely strictly singular, and a later exposition gives a direct finite-dimensional proof.

Recent work of Laustsen and Wirzenius proves that when \(X\) is a **finite** direct sum of spaces from the Baernstein, Schreier and classical \(\ell_p\) families, the quotient \(\mathcal{SS}(X)/\mathcal K(X)\) is nilpotent with an explicitly determined index. The construction above shows a sharp failure of that finite-sum phenomenon for a concrete countable direct sum of classical sequence spaces: not only can nilpotency fail, but the quotient can already contain a free noncommutative algebra on two generators.

## Limitations

The originality claim is to the best of our knowledge. Targeted searches for countable direct sums, strictly singular operators modulo compact operators, weighted/tree shifts, free semigroups and free subalgebras did not locate this construction or an equivalent theorem. The tree-shift mechanism is elementary once the formal inclusions are available, so an equivalent observation may exist under different operator-ideal or free-semigroup terminology.

Milman's 1970 Russian-language primary paper was identified through later sources but was not fully inspected here. Pietsch's classical monograph on operator ideals was also not exhaustively checked. These sources support the background theory and are not known to state the countable-tree free-algebra conclusion, but they remain residual originality risks.

No computational verification is needed: the proof reduces to operator-ideal closure, the standard strict singularity/noncompactness of \(\ell_p\hookrightarrow\ell_q\) for \(p<q\), and an explicit separation estimate on the images of the unit-vector sequence.

## References

1. T. Kato, *Perturbation theory for nullity, deficiency and other quantities of linear operators*, Journal d'Analyse Mathématique **6** (1958), 261–322. https://doi.org/10.1007/BF02790090
2. S. Goldberg and E. O. Thorp, *On some open questions concerning strictly singular operators*, Proc. Amer. Math. Soc. **14** (1963). https://doi.org/10.1090/S0002-9939-1963-0145361-3
3. V. D. Milman, *Operators of class \(C_0\) and \(C_0^*\)* (Russian), Teor. Funkcii Funkcional. Anal. i Prilozen. **10** (1970), 15–26.
4. Th. Schlumprecht, *On the closed subideals of \(L(\ell_p\oplus\ell_q)\)*, Operators and Matrices **6** (2012), 311–326. https://doi.org/10.7153/oam-06-22
5. N. J. Laustsen and H. Wirzenius, *Compactness of compositions of strictly singular operators on direct sums of Baernstein, Schreier and \(\ell_p\)-spaces*, Proc. Amer. Math. Soc. **154** (2026), 2345–2356. https://doi.org/10.1090/proc/17594
6. K. R. Davidson and D. R. Pitts, *Invariant Subspaces and Hyper-Reflexivity for Free Semigroup Algebras*, Proc. London Math. Soc. **78** (1999), 401–430. https://doi.org/10.1112/S002461159900180X
