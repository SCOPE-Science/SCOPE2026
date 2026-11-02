# Complete group Rota–Baxter classification on the quaternion group of order eight

## Finding

Let \(Q\) be the quaternion group \(Q_8=\{\pm1,\pm i,\pm j,\pm k\}\), with \(i^2=j^2=k^2=ijk=-1\). A (weight-one, group-theoretic) Rota–Baxter operator is any map \(B:Q\to Q\) such that, for all \(g,h\in Q\),
\[
 B(g)B(h)=B\bigl(gB(g)hB(g)^{-1}\bigr). \tag{RB}
\]
Put \(Z=\{1,-1\}\) and \(V=Q/Z\cong C_2\times C_2\). **Every** group Rota–Baxter operator on \(Q\) is uniquely of one of the forms
\[
 B_{\chi}^{\mathrm{cen}}(g)=\chi(g),\qquad
 B_{\chi}^{\mathrm{inv}}(g)=g^{-1}\chi(g),
 \quad \chi\in\operatorname{Hom}(Q,Z).
\]
There are exactly four homomorphisms \(\chi\) and hence **exactly eight operators**, with four from each form. Their image-cardinality distribution is exactly
\[
 \#\{B:|B(Q)|=r\}=
 \begin{cases}
 1,&r=1,\\
 3,&r=2,\\
 4,&r=8,\\
 0,&\text{otherwise}.
 \end{cases}
\]
Under conjugation by \(\operatorname{Aut}(Q)\), the eight operators form exactly four orbits, of sizes \(1,3,1,3\): each displayed family has one orbit of size one (the trivial character) and one orbit of size three (the nontrivial characters).

With the dual convention \(\widetilde B(g)=g^{-1}B(g^{-1})\), dualization interchanges the two displayed forms for the same \(\chi\). In particular **no** group Rota–Baxter operator on \(Q\) has both itself and its dual bijective. The four bijective operators are involutive permutations of \(Q\).

Under the standard exact-factorization definition of a splitting operator, precisely the trivial operator and the inversion operator are splitting; the other six are non-splitting.

## Assumptions and scope

Only the abstract quaternion group of order eight is considered, **not** its real quaternion algebra, its group algebra, or any linear Rota–Baxter operator. The center \(Z=\{1,z\}\), where \(z=-1\), is the unique subgroup of order two; every element of \(Q\setminus Z\) has order four. The quotient \(V=Q/Z\) is an elementary abelian group of order four. Homomorphisms to \(Z\) are understood as ordinary group homomorphisms; they are automatically trivial on \(Z\).

A standard splitting operator arises from an exact factorization \(Q=HL\) by subgroups satisfying \(H\cap L=\{1\}\), by sending \(hl\) to \(l^{-1}\). The word *splitting* below means this precise construction.

## Proof

**1. The identity and the central involution.** Taking \(g=h=1\) in (RB) yields \(B(1)^2=B(1)\), so \(B(1)=1\). Since \(z\) is central, taking \(g=h=z\) yields \(B(z)^2=B(z^2)=1\). The only solutions of \(x^2=1\) in \(Q\) are \(1\) and \(z\), so \(B(z)\in Z\). Taking \(g=z\) and arbitrary \(h\) in (RB), and using centrality of \(B(z)\), then gives
\[
 B(zh)=B(z)B(h). \tag{1}
\]

**2. Two simultaneous homomorphisms.** Define the auxiliary product \(g\circ h=gB(g)hB(g)^{-1}\) and the auxiliary map \(C(g)=gB(g)\). The defining identity gives
\[
 B(g\circ h)=B(g)B(h),\qquad
 C(g\circ h)=C(g)C(h). \tag{2}
\]
The second identity is immediate on substituting the first:
\[
 (g\circ h)B(g\circ h)
 =gB(g)hB(g)^{-1}B(g)B(h)
 =gB(g)hB(h).
\]
Because \(Q/Z\) is abelian, conjugation acts trivially on this quotient, so
\[
 \overline{g\circ h}=\bar g\bar h\quad\text{in }V. \tag{3}
\]
No assumption that \(\circ\) equals the original multiplication on \(Q\) is used.

**3. The case \(B(z)=1\).** Equation (1) now reads \(B(zg)=B(g)\). Thus \(B\) descends to a well-defined set map \(b:V\to Q\). By (2) and (3),
\[
 b(\bar g\bar h)=B(g\circ h)=b(\bar g)b(\bar h),
\]
so \(b\) is a group homomorphism. Every element of the exponent-two group \(V\) maps to an element of order dividing two, and the only such elements in \(Q\) belong to \(Z\). Thus \(b(V)\subseteq Z\), and \(B(g)=\chi(g)\) for a unique \(\chi\in\operatorname{Hom}(Q,Z)\).

**4. The case \(B(z)=z\).** Equation (1) gives \(B(zg)=zB(g)\); hence \(C(zg)=zg\,zB(g)=C(g)\). Thus \(C\) descends to \(c:V\to Q\). From (2) and (3), \(c\) is a group homomorphism. Again every element in its image has order dividing two, so \(c(V)\subseteq Z\). Writing \(C(g)=\chi(g)\) gives \(B(g)=g^{-1}\chi(g)\) for a unique \(\chi\in\operatorname{Hom}(Q,Z)\). The cases are disjoint because their values at \(z\) are different.

**5. Both families satisfy (RB).** For the central family, \(B(g)=\chi(g)\) has central image, and the equation reduces to \(\chi(g)\chi(h)=\chi(gh)\). For the inverse-twisted family, with \(\chi\) central,
\[
 gB(g)hB(g)^{-1}=hg,
\]
so its right-hand side is \((hg)^{-1}\chi(hg)=g^{-1}h^{-1}\chi(g)\chi(h)\), precisely \(B(g)B(h)\). This proves necessity and sufficiency.

**6. Enumeration, orbits, duals.** Since \(V\cong C_2^2\), exactly four homomorphisms \(V\to Z\) exist, one trivial and three nontrivial. The central maps have images of sizes \(1\) or \(2\). For the inverse-twisted map \(F(g)=g^{-1}\chi(g)\), one has \(\chi(F(g))=\chi(g)\), because \(\chi\) kills \(Z\), and consequently \(F(F(g))=g\). Thus all four inverse-twisted maps are bijections. Automorphisms of \(Q\) induce the full group \(\operatorname{GL}_2(\mathbb F_2)\) on \(V\), which permutes the three nontrivial characters transitively. Because an automorphism preserves the two displayed families, the orbit-size list is \(1,3,1,3\).

For \(\chi(g)\in Z\), \(\chi(g^{-1})=\chi(g)\). Substituting into \(\widetilde B(g)=g^{-1}B(g^{-1})\) shows that \(\widetilde{B_\chi^{\mathrm{cen}}}=B_\chi^{\mathrm{inv}}\) and \(\widetilde{B_\chi^{\mathrm{inv}}}=B_\chi^{\mathrm{cen}}\). One member of each pair has image of size at most two, so no pair is mutually bijective.

**7. Splitting.** Every nontrivial subgroup of \(Q\) contains its unique involution \(z\). Consequently two nontrivial subgroups cannot intersect trivially. Hence any exact factorization \(Q=HL\) has \(H=\{1\}\) or \(L=\{1\}\), yielding only inversion or the trivial operator. The other six are therefore non-splitting in the stated sense.

## Verification

Two independently implemented finite checks accompany the symbolic proof. `verify.cpp` constructs the eight-element multiplication table, checks associativity and inverses, exhausts all \(8^7=2{,}097{,}152\) maps with \(B(1)=1\), and compares the exact solution set with the two formula families. It additionally computes all automorphism orbits and duals. `verify.py` uses a separate signed-quaternion multiplication implementation to check all formula instances and dual distributions.

Reproduce in a POSIX environment with C++17 and Python 3:

```sh
g++ -std=c++17 -O2 -Wall -Wextra verify.cpp -o verify
./verify
python3 verify.py
```

Observed outputs:

```text
VERIFY_OK candidates=2097152 operators=8 images=1:1,2:3,8:4 aut=24 orbit_sizes=1:2,3:2 dual=checked
FORMULA_CHECK_OK operators=8 image_cardinalities=1,2,2,2,8,8,8,8
```

The exhaustive program is a finite crosscheck; the proof in sections 1–7 independently establishes the entire classification without relying on enumeration.

## Relationship to prior work

Savelyev's 2026 classification of group Rota–Baxter operators on the finite Heisenberg and exponent-\(p^2\) extraspecial groups of order \(p^3\) explicitly assumes odd prime \(p\ge3\). The quaternion group is the order-eight extraspecial group of minus type; it is not in those odd-prime classifications. The present theorem determines the exact previously excluded small-prime case, including the counts, automorphism orbits, dual bijectivity and splitting distinction. This is **not** a claim that the general group Rota–Baxter identity, the trivial and inversion operators, or central-character constructions are new.

Galt and Gubarev's classification of dihedral-group and alternating-group Rota–Baxter operators does not directly cover the quaternion group, which is non-dihedral. Their results and the general group Rota–Baxter framework are relevant background, but the exhaustiveness argument for \(Q\) is established here directly.

## Limitations

The proof classifies only the group of order eight \(Q\); it neither counts operators on higher-order extraspecial \(2\)-groups nor gives a classification of arbitrary Hamiltonian groups. Historical priority for this exact small-group classification remains subject to independently inspecting all older and unindexed classifications of finite-group Rota–Baxter operators. The present derivation gives no such broad uniqueness claim.

## References

1. A. Savelyev, *Rota–Baxter operators on extraspecial groups*, arXiv:2608.28291v1, first posted 2026-08-28, https://arxiv.org/abs/2608.28291 .
2. V. Bardakov and V. Gubarev, *Rota–Baxter groups, skew left braces, and the Yang–Baxter equation*, Journal of Algebra (2022), https://doi.org/10.1016/j.jalgebra.2021.12.036 .
3. A. Galt and V. Gubarev, *Rota–Baxter Operators on Dihedral and Alternating Groups*, Advances in Group Theory and Applications **23** (2026), 27–62, https://doi.org/10.32037/agta-2026-003 .
