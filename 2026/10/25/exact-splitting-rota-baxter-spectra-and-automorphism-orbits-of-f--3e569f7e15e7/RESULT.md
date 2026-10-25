# Exact splitting Rota–Baxter spectra and automorphism orbits of finite dihedral groups

## Finding

For every integer \(n\geq3\), let
\[
G=D_{2n}=\langle r,s\mid r^n=s^2=1,\ srs=r^{-1}\rangle.
\]
A weight-one group Rota–Baxter operator is a map \(B:G\to G\) satisfying
\[
B(g)B(h)=B\bigl(gB(g)hB(g)^{-1}\bigr)
\quad(g,h\in G).
\]
An operator is *splitting* if it arises from an ordered exact subgroup factorization \(G=HL\), \(H\cap L=1\), through \(B(hl)=l^{-1}\). Write \(\mathscr R_n\) for the set of splitting operators and \(\lvert\operatorname{im}B\rvert\) for an operator's image cardinality. The complete image-cardinality enumerator is
\[
\boxed{\sum_{B\in\mathscr R_n}z^{\lvert\operatorname{im}B\rvert}
=\sum_{a\parallel n}a\bigl(z^a+z^{2n/a}\bigr)
+\mathbf 1_{2\mid n}\,n\sum_{b\parallel n/2}z^{2b}.}
\]
Here \(a\parallel m\) means \(a\mid m\) and \(\gcd(a,m/a)=1\) (a *unitary divisor*). If \(\sigma^*(n)=\sum_{a\parallel n}a\), and \(\omega(n)\) counts distinct prime factors, then
\[
\boxed{\lvert\mathscr R_n\rvert
=2\sigma^*(n)+\mathbf1_{2\mid n}\,n2^{\omega(n/2)}.}
\]
The action of \(\operatorname{Aut}(G)\) on operators by \(B\mapsto\phi^{-1}B\phi\) has exactly
\[
\boxed{\lvert\mathscr R_n/\operatorname{Aut}(G)\rvert
=2^{\omega(n)+1}+\mathbf1_{2\mid n}2^{\omega(n/2)}}
\]
orbits. More precisely: for each \(a\parallel n\), there are two orbits, each of size \(a\), associated respectively with an ordered cyclic/dihedral or dihedral/cyclic factorization; if \(n\) is even, each \(b\parallel n/2\) contributes a further orbit of size \(n\), associated with two dihedral factors. These are all the orbits.

For odd \(n\), a theorem of Galt–Gubarev shows that every weight-one Rota–Baxter operator on \(D_{2n}\) is splitting; the formulas therefore count *all* operators and their ordinary automorphism orbits in that case. For even \(n\), the formulas describe only splitting operators: nonsplitting operators also exist.

There is an asymptotic parity phenomenon. For \(n=2m\) with \(m\) odd, let \(M_n\) count cyclic/dihedral ordered splitting factorizations and \(Q_n\) count dihedral/dihedral ones. Then
\[
\frac{Q_n}{M_n}
=\frac13\prod_{p^e\parallel m}\frac{2p^e}{p^e+1}
\geq\frac13\left(\frac32\right)^{\omega(m)}.
\]
Consequently, whenever \(m\) ranges through odd integers with \(\omega(m)\to\infty\), a uniformly sampled splitting operator on \(D_{4m}\) has two dihedral factors with probability tending to one. This statement does not concern the distribution of all nonsplitting operators.

## Assumptions and scope

All groups are abstract finite groups. \(D_{2n}\) has order \(2n\), and \(n\geq3\) ensures that its rotation subgroup is characteristic. A factorization is *ordered*: \((H,L)\) and \((L,H)\) define different splitting operators in general. Subgroups are counted as embedded subgroups, not merely by their abstract isomorphism types. An exact factorization includes the two trivial possibilities \((G,1)\) and \((1,G)\); hence the zero and inverse Rota–Baxter operators are included. The action is ordinary automorphism conjugation, not the larger equivalence relation that also allows interchanging certain associated Rota–Baxter operators.

## Proof

**Step 1: Exact factorizations parameterize splitting operators injectively.** Given \(G=HL\) and \(H\cap L=1\), every \(g\in G\) has a unique expression \(g=hl\), and \(B(hl)=l^{-1}\) satisfies the group Rota–Baxter identity (the standard factorization construction). Conversely, this map satisfies \(\ker B=H\) and \(\operatorname{im}B=L\); thus different ordered embedded pairs cannot give the same splitting operator. We may enumerate such pairs directly.

**Step 2: List embedded subgroups.** For each \(a\mid n\), there is exactly one rotation subgroup
\[
C_a=\langle r^{n/a}\rangle
\]
of order \(a\). The dihedral subgroups with rotation subgroup \(C_a\) are
\[
D_{2a,i}=\langle r^{n/a},r^i s\rangle,
\qquad i\pmod{n/a},
\]
each of order \(2a\). Every subgroup is one of these, with the understanding that \(D_{2,i}\) is a reflection subgroup of order two. Distinct listed subgroups are distinct; no two rotation groups have a reflection.

**Step 3: Cyclic/dihedral pairs.** If \(H=C_a\), \(L=D_{2b,i}\), then \(\lvert H\rvert\lvert L\rvert=2n\) and \(H\cap L=1\) hold exactly when \(ab=n\) and \(\gcd(a,b)=1\). Equivalently \(a\parallel n\) and \(b=n/a\). In that case there are \(n/b=a\) choices of \(i\), and the image order is \(2b=2n/a\). Reversing the two factors gives \(a\) further operators whose image order is \(a\). These account for the first term of the enumerator.

**Step 4: Dihedral/dihedral pairs.** Both factors are dihedral only when \(2ab=n\), so \(n\) must be even. Their rotation subgroups intersect trivially exactly when \(\gcd(a,b)=1\). In this case, put \(n=2ab\). The reflection indices for \(D_{2a,i}\), \(D_{2b,j}\) range respectively modulo \(2b\) and \(2a\). A shared reflection would require solving \(i\equiv j\pmod{\gcd(2a,2b)}\); because \(\gcd(a,b)=1\), the intersection is trivial exactly when \(i\) and \(j\) have opposite parity. There are \((2b)(2a)/2=n\) such ordered pairs per ordered unitary decomposition \(ab=n/2\). Their image order is \(2b\). This gives the second term and the total number of maps.

**Step 5: Automorphism orbits.** Each automorphism of \(G\) has the form
\[
\phi_{u,v}(r)=r^u,\qquad\phi_{u,v}(s)=r^v s,
\]
where \(\gcd(u,n)=1\) and \(v\pmod n\). It fixes each \(C_a\), and sends the index \(i\) of \(D_{2a,i}\) to \(ui+v\) modulo \(n/a\). The translation \(v\) is transitive on all choices in Step 3, producing one orbit of size \(a\) for each order of factors. In Step 4 the congruences for sending one opposite-parity index pair to another have moduli \(2a\), \(2b\) with greatest common divisor two. Taking \(u=1\) suffices: both pairs have odd index difference, so the Chinese remainder compatibility condition holds, and a common translation \(v\) exists. Hence each ordered unitary decomposition in Step 4 forms one orbit of size \(n\). Counting these orbits proves the orbit formula.

**Step 6: Parity asymptotic.** If \(n=2m\) with odd \(m\), the first two subgroup types contribute \(M_n=2\sigma^*(2m)=6\prod_{p^e\parallel m}(1+p^e)\), while the third contributes \(Q_n=2m\,2^{\omega(m)}\). Their ratio is as displayed. Each odd prime power satisfies \(2p^e/(p^e+1)\geq3/2\), establishing divergence and the probability limit.

## Verification

The accompanying standalone `VERIFY.py` constructs dihedral groups as pairs of exponents, enumerates every embedded subgroup and ordered exact pair, and compares the direct enumeration with the divisor formulas for \(1\leq n\leq24\). For \(1\leq n\leq10\) it constructs every corresponding operator and directly checks the Rota–Baxter identity for every ordered pair of group elements. For \(3\leq n\leq24\) it independently enumerates automorphism orbits of ordered factorization pairs and matches the predicted numbers. Small \(n=1,2\) checks probe numerical boundaries only; the orbit theorem is claimed for \(n\geq3\). Run with `python VERIFY.py`; the successful terminal markers are `VERIFY_OK` and `ORBIT_VERIFY_OK`. The finite checks are not a proof of the general formulas.

## Relationship to prior work

Galt and Gubarev, *Rota-Baxter operators on dihedral and alternating groups* (first public version April 22, 2024), provide the standard splitting construction and prove that there are no nonsplitting group Rota–Baxter operators on odd dihedral groups (Theorem 3(a)). The new claim does not reprove the global classification of possible operators; it refines the splitting sector by exact embedded-map multiplicities, a full image-size polynomial, and ordinary automorphism orbit sizes.

Ochoa Arango and Umbarila Martín, *On the number of exact factorization of finite Groups* (first public version September 16, 2024), classify dihedral subgroup-factorization *types* and count their coarse equivalence classes, where factors may be exchanged and only factor-group isomorphism types matter (Definition 1.2, Lemma 1.8, Theorem 1.9). Those established structural facts are acknowledged. The present counts distinguish ordered embedded complements and retain their image sizes and automorphism orbits; none of those finer numerical invariants are the quantity \(f_2\) computed in that paper.

The classification of splitting operators of \(D_8\) is separately known from work by Liu and Wang; in particular, the value 18 at \(n=4\) is not claimed as new.

## Limitations

This statement excludes \(n=1,2\) in the orbit classification, and it does not enumerate nonsplitting operators on even-order rotation dihedral groups. The fine enumeration is a consequence of known structural descriptions of group factorizations together with new explicit embedding and automorphism counts; it is not independent of that foundational work. A complete priority comparison with every specialized publication on factorization counts or dihedral group Rota–Baxter operators is not established. The public mathematical claims are proof-supported but have not received independent external audit.

## References

1. A. Galt and V. Gubarev, *Rota-Baxter operators on dihedral and alternating groups*, arXiv:2404.14078, first public version 2024-04-22, Theorem 3 and §2. https://arxiv.org/abs/2404.14078
2. J. A. Ochoa Arango and M. A. Umbarila Martín, *On the number of exact factorization of finite Groups*, arXiv:2409.10428, first public version 2024-09-16, Definition 1.2, Lemma 1.8, Theorem 1.9. https://arxiv.org/abs/2409.10428
3. V. G. Bardakov and V. Gubarev, *Rota–Baxter groups, skew left braces, and the Yang–Baxter equation*, Journal of Algebra 596 (2022), 328–351, §2. https://doi.org/10.1016/j.jalgebra.2021.12.036
4. Q. Liu and S. Wang, *Classification of Rota-Baxter operators on \(D_8\)* (2024), small-order comparison; published abstract consulted, full text not exhaustively inspected.
