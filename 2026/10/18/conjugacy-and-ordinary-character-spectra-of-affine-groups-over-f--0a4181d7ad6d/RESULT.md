# Conjugacy and ordinary character spectra of affine groups over finite chain rings

## Finding

Let \(R\) be any finite commutative chain ring with residue field of cardinality \(q\) and maximal-ideal nilpotency length \(n\geq1\). The affine group \(G=R^+\rtimes R^\times\), acting by \(x\mapsto ux+a\), has a complete conjugacy classification and a complete complex irreducible character table described by the valuation of ring elements.

Write \(U=R^\times\), \(N=|U|=(q-1)q^{n-1}\), and let \(v(0)=n\) with \(v(a)=h\) if \(a\in\mathfrak m^h\setminus\mathfrak m^{h+1}\). For each \(u\in U\) put \(k=v(1-u)\). Exactly \(k+1\) conjugacy classes have multiplier \(u\): their representatives are \((0,u)\) and \((\pi^h,u)\) for \(0\leq h<k\). Their sizes respectively are \(q^{n-k}\) and \((q-1)q^{n-1-h}\). The number of units having \(k=0\) is \((q-2)q^{n-1}\); for \(1\leq k<n\) it is \((q-1)q^{n-k-1}\); for \(k=n\) it is one. Hence the **entire class-size multiset depends only on \((q,n)\)**, and

\[
\#\operatorname{Cl}(G)=(q-1)q^{n-1}+\frac{q^n-1}{q-1},
\qquad
\operatorname{cp}(G)=q^{-n}+\frac{q^n-1}{(q-1)^2q^{2n-1}}.
\]

All complex irreducible characters consist of \(N\) linear characters inflated from \(U\) and, for each \(0\leq h<n\), exactly \(q^h\) characters of degree

\[
d_h=(q-1)q^{n-1-h}.
\]

Repeated degrees must be combined when \(q=2\). Thus the complete irreducible degree multiset is also independent of the chain-ring isomorphism type. In addition, the formulas in the Proof section calculate every entry of the ordinary complex character table.

This common-spectrum phenomenon does **not** imply the affine groups are isomorphic: \(R=\mathbb Z/8\mathbb Z\) and \(R'=\mathbb F_2[t]/(t^3)\) both yield affine groups of order \(32\), with class-size distribution \(1^2,2^3,4^6\) and character-degree distribution \(1^8,2^2,4^1\), but their abelianizations are respectively \(C_2^3\) and \(C_4\times C_2\).

## Assumptions and scope

A *finite commutative chain ring* is a finite commutative ring with identity whose ideals are linearly ordered. Its unique maximal ideal is \(\mathfrak m=(\pi)\), with \(\mathfrak m^n=0\) and \(\mathfrak m^{n-1}\neq0\). Every ideal equals \(\mathfrak m^j\); \(|\mathfrak m^j|=q^{n-j}\) for \(0\leq j\leq n\). No equicharacteristic or odd-characteristic hypothesis is imposed. In particular, Galois chain rings and truncated-polynomial chain rings are allowed, and \(q\) is any prime power.

The group law is \((a,u)(b,w)=(a+ub,uw)\); complex characters are ordinary characteristic-zero characters. A generating additive character of \(R\) means an additive homomorphism \(\psi:R\to\mathbb C^\times\) whose kernel contains no nonzero ideal.

## Proof

**Conjugacy.** Since \(U\) is abelian, direct multiplication gives
\[
(b,w)(a,u)(b,w)^{-1}=(wa+(1-u)b,u).
\]
Set \(k=v(1-u)\). The translation term ranges over \(\mathfrak m^k\). If \(v(a)\geq k\), it can be eliminated, producing the single class \((0,u)\) with \(q^{n-k}\) elements. If \(h=v(a)<k\), unit multiplication preserves \(h\) and is transitive on all ring elements of valuation \(h\); thus this one class has \((q-1)q^{n-1-h}\) elements. Distinct valuations or multipliers cannot be conjugate. These classes partition \(G\), proving both completeness and the asserted sizes.

The unit counts follow by subtracting successive cardinalities of \(1+\mathfrak m^j\). Summing the numbers \(k+1\) over all \(u\in U\) gives \(N+\sum_{j=1}^n|1+\mathfrak m^j|=N+(q^n-1)/(q-1)\), since \(\sum_{j=1}^{n}q^{n-j}=(q^n-1)/(q-1)\). The commuting probability equals the conjugacy-class count divided by \(|G|=q^nN\). Equivalently, for \((a,u)\) with \(h=v(a)\), the centralizer has size \(Nq^k\) if \(h\geq k\), and \(q^{n+h}\) otherwise.

**Dual action and degrees.** The socle \(\mathfrak m^{n-1}\) lies in every nonzero ideal. Choose a nontrivial additive character on this socle and extend it to the additive group of \(R\); the extension \(\psi\) is generating. Multiplication identifies \(R\) with its full additive dual via \(z\mapsto\psi_z\), where \(\psi_z(a)=\psi(za)\). The group \(U\) acts by multiplication on these characters. Its orbits are \(\{0\}\) and the valuation shells \(\mathfrak m^h\setminus\mathfrak m^{h+1}\) for \(0\leq h<n\). A representative \(z_h=\pi^h\) has stabilizer
\[
H_h=\{u\in U:(u-1)\pi^h=0\}=1+\mathfrak m^{n-h},
\qquad |H_h|=q^h.
\]
The orbit has size \(d_h=(q-1)q^{n-1-h}\). The little-group/Clifford correspondence for a finite abelian normal subgroup parametrizes irreducibles above this orbit by \(\widehat H_h\), giving exactly \(q^h\) irreducibles of degree \(d_h\). The zero orbit contributes one inflated linear character for each \(\theta\in\widehat U\). Completeness may also be checked by the sum-of-squares identity
\[
N+\sum_{h=0}^{n-1}q^h (q-1)^2q^{2n-2-2h}=q^nN.
\]

**Every character value.** For each \(0\leq h<n\) and \(\theta\in\widehat H_h\), let \(\chi_{h,\theta}\) be the character induced from \((a,u)\mapsto\psi(\pi^h a)\theta(u)\) on \(R^+\rtimes H_h\). Put \(m=n-h\). Then for every \((a,u)\in G\),
\[
\chi_{h,\theta}(a,u)=
\begin{cases}
0,&u\notin H_h,\\
\theta(u)\,S_m(a),&u\in H_h,
\end{cases}
\quad
S_m(a)=\begin{cases}
(q-1)q^{m-1},&v(a)\geq m,\\
-q^{m-1},&v(a)=m-1,\\
0,&v(a)<m-1.
\end{cases}
\]
Indeed, when \(u\in H_h\), induction evaluates the orbit sum \(\theta(u)\sum_{z\in\pi^h U}\psi(za)\). It is the difference between sums over \(\mathfrak m^h\) and \(\mathfrak m^{h+1}\), each of which is the ideal's cardinality precisely if its annihilator contains \(a\), and zero otherwise. When \(u\notin H_h\), the induced character vanishes because no conjugate is in \(R^+\rtimes H_h\). The characters from the zero orbit are simply \(\chi_{0,\theta}^{\mathrm{lin}}(a,u)=\theta(u)\) for \(\theta\in\widehat U\). These explicit rows, together with the class representatives above, constitute the entire ordinary character table.

**Nonisomorphism with equal spectra.** For any such ring, the derived subgroup of \(G\) is the additive translation subgroup corresponding to the ideal \(J=\sum_{u\in U}(1-u)R\), because \(U\) and \(R^+\) are abelian. Thus \(G_{\mathrm{ab}}\cong(R/J)^+\times U\). For both \(\mathbb Z/8\mathbb Z\) and \(\mathbb F_2[t]/(t^3)\), the ideal \(J\) equals the maximal ideal. The former has \(U\cong C_2\times C_2\); the latter has \(U\cong C_4\). Their abelianizations are consequently \(C_2^3\) and \(C_4\times C_2\), although both have \((q,n)=(2,3)\). Applying the preceding formulas yields the same asserted multisets for their conjugacy-class sizes and ordinary irreducible degrees.

## Verification

The dependency-free companion program `verify.py` directly enumerates ring elements, units, group conjugation, conjugacy-class orbits, centralizers, and the additive-dual orbit degrees. It independently compares the resulting character orbit sums with the asserted three-case formula. The tested rings comprise \(\mathbb F_p[t]/(t^n)\) and \(\mathbb Z/p^n\mathbb Z\) at \((p,n)=(2,1),(2,2),(2,3),(3,1),(3,2),(5,1)\), together with \(\mathbb F_4[t]/(t^n)\) for \(n=1,2\). All 14 finite configurations pass. To reproduce: `python3 verify.py`. The general theorem is proved above and is not inferred from finite tests.

## Relationship to prior work

Wan and Zhou (2025, arXiv:2506.05652v1) study conjugacy types and class-algebra stability for general affine groups over finite **fields**. The present result concerns affine groups of finite commutative chain **rings**, including nonreduced and mixed-characteristic rings; it does not claim their field case as new. General semidirect-product character theory and additive-character duality are standard ingredients.

Character tables for affine groups of \(\mathbb Z/p^n\mathbb Z\) were explicitly discussed before this work, including the MathOverflow discussion that points to V. Dokchitser's thesis. This cyclic-residue-ring special case is not claimed as new. Tanaka (2004) computes related character tables for *affine association schemes* over \(\mathbb Z/p^n\mathbb Z\), which are different objects. The claim of interest here is the all-finite-commutative-chain-ring conjugacy and character formulas together with the complete ring-independent class/degree spectra and nonisomorphic equal-spectrum example.

## Limitations

The ring must be commutative and a chain ring; formulas need not extend to nonprincipal local rings or noncommutative rings. Independence from the ring's isomorphism type holds for the class-size and character-degree **multisets**, not for its complete character table or group isomorphism type. The direct enumeration verifies selected small rings only. Equivalent all-chain-ring results in specialized or unpublished literature, including generalizations of older \(\mathbb Z/p^n\mathbb Z\) work, cannot be excluded without further independent bibliographic review.

## References

- J. Wan and L. Zhou, *Stability of the centers of group algebras of general affine groups \(GA_n(q)\)*, arXiv:2506.05652v1, publicly submitted 6 June 2025; https://arxiv.org/html/2506.05652v1 .
- *Character table for the affine group of \(\mathbb Z/p^n\mathbb Z\)*, MathOverflow question and responses; https://mathoverflow.net/questions/44203/character-table-for-the-affine-group-of-z-pnz .
- H. Tanaka, *Association schemes of affine type over finite rings*, Advances in Geometry (2004), doi:10.1515/advg.2004.015 .
- Y. Alabiad and Y. Alkhamees, work on finite commutative chain rings, doi:10.3934/math.2022100 .
