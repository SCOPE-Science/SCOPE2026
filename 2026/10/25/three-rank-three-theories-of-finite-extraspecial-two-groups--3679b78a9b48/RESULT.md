# Three rank-three theories of finite extraspecial two-groups

## Finding

In the first-order language with equality, a constant \(e\) for the group identity, and a ternary relation \(R(x,y,z)\) meaning \(xy=z\), all finite extraspecial \(2\)-groups have exactly **three** theories at quantifier rank \(3\). The representatives are the dihedral group \(D_8\), the quaternion group \(Q_8\), and either extraspecial group of order \(32\). In particular, for any extraspecial \(2\)-groups \(G,H\) of orders at least \(32\),

\[
G\equiv_3 H.
\]

The largest smallest representative has \(32\) elements, sharply. At order \(32\), the plus and minus types are equivalent at rank \(3\) but distinguishable at rank \(4\). Thus the first rank at which the Arf sign is visible in that pair is exactly \(4\).

## Assumptions and scope

An extraspecial \(2\)-group is a finite nonabelian group with center, commutator subgroup, and Frattini subgroup all the same group of order \(2\). Its order is \(2^{2n+1}\), \(n\ge1\), with exactly two isomorphism types at each such order. The first-order language is *relational multiplication*, not a binary function-language with unrestricted group terms; the identity is named. All formulas and quantifier ranks refer to this language. The result concerns these groups only, not all class-two groups or all prime-power groups.

Write \(Z(G)=\{e,c\}\), \(V=G/Z(G)\), and \(q(\bar x)=0\) or \(1\) according as \(x^2=e\) or \(c\). Then \(V\) is a \(2n\)-dimensional vector space over \(\mathbf F_2\), and its quadratic form has nonsingular polar form \(B(\bar x,\bar y)\) defined by \([x,y]=c^{B(\bar x,\bar y)}\). The two groups of each order correspond to the two Arf signs of \(q\).

## Proof

**1. Reduction to two-point extension profiles.** For a tuple of at most three selected group elements, its atomic diagram consists of equalities, equalities with \(e\), and all instances of \(R\) on selected coordinates (repetitions allowed). For an ordered pair \((x,y)\), let \(P_G(x,y)\) be the set of atomic diagrams of \((x,y,z)\) as \(z\) ranges over \(G\). Let \(T_G(x)=\{P_G(x,y):y\in G\}\). The exact recursive first-order/Ehrenfeucht–Fraïssé characterization gives

\[
G\equiv_3H\quad\Longleftrightarrow\quad
\{T_G(x):x\in G\}=\{T_H(x):x\in H\}.
\]

No cardinalities of repeated diagram types are counted by this set-based recursion.

**2. The finite local table is uniform from order \(32\).** Let \(n\ge2\). For fixed \(x,y\), let \(U=\operatorname{span}(\bar x,\bar y)\), of dimension at most two. Every selected third element \(z\) either lies in the preimage of \(U\) (at most eight elements) or outside it. In the first case its atomic diagram follows completely from the relations \(x^2=c^{q(\bar x)}\), \(y^2=c^{q(\bar y)}\), \([x,y]=c^{B(\bar x,\bar y)}\), and the relations \(y\in\{x,cx\}\) or \(x,y\in\{e,c\}\) when applicable. In the second case no product involving \(z\) and either nonidentity noncentral selected point can equal a selected point; the only remaining new atomic fact is \(z^2=e\) or \(c\), plus the identity laws when \(x=e\) or \(y=e\).

For every regular quadratic form of dimension \(2n\ge4\), each of its two value fibers has cardinality \(2^{2n-1}\pm2^{n-1}\), thus at least \(6\). Since \(|U|\le4\), outside \(U\) there is always a \(z\) of each square type. Therefore **the full** \(P_G(x,y)\) is obtained by enumerating the central extension of \(U\) and appending precisely two generic diagrams, one with square \(e\) and one with square \(c\). This is a finite, exact description valid for arbitrary \(n\ge2\).

It suffices to classify \(x\) as \(e\), \(c\), a noncentral involution \(I\), or an order-four element \(J\). The local enumeration yields the following distinct \(P\)-profiles as \(y\) varies. Here \(B\) is evaluated on the independent quotient vectors when applicable.

| \(x\) type | Profiles realized by \(y\) | Number |
|---|---|---:|
| \(e\) | \(y=e,c,I,J\) | 4 |
| \(c\) | \(y=e,c,I,J\) | 4 |
| \(I\) | \(y=e,c,x,cx\); independent \(I\) with \(B=1\); independent \(J\) with \(B=0,1\) | 7 |
| \(J\) | \(y=e,c,x,cx\); independent \(I\) with \(B=0,1\); independent \(J\) with \(B=0,1\) | 8 |

All \(23\) entries in these four rows are distinct as ordered-pair profiles. There is exactly one important equality of *descriptions*: when \(x\) is a noncentral involution, independent involutions \(y\) with \(B(\bar x,\bar y)=0\) give exactly the same \(P_G(x,y)\) as \(y=cx\). For the latter pair, \(xy=c\); for the former, \(xy\) is a noncentral involution. These alternatives have identical three-element atomic diagrams since distinguishing the centrality of the product needs one further selection. All the other entries follow directly by enumerating at most eight preimage elements and the two generic squares, as prescribed above.

Every displayed row is realized in **every** regular quadratic space of dimension at least four. Indeed, every nonzero vector lies in a nonsingular four-dimensional subspace. On that subspace the form is isometric to one of

\[
q_+(a,b,s,t)=ab+st,\qquad
q_-(a,b,s,t)=a+b+ab+st.
\]

Enumerating their sixteen quotient vectors verifies, for each possible nonzero \(x\)-type, every listed independent \(B\)/square combination. The only absence occurs for \(x\) singular in the minus form and \(y\) independent singular with \(B=0\); precisely this omitted case duplicates \(y=cx\) and therefore changes no \(P\)-profile. This finite vector check is reproducible in the attached verifier; it does not assume the ambient dimension is four.

Consequently, for **every** extraspecial \(2\)-group of order at least \(32\), the four classes \(e,c,I,J\) have exactly the same respective \(T_G(x)\). Their sets of pointed types are therefore identical, proving the claimed common rank-three theory.

**3. Three classes, not fewer.** At degree \(n=1\), the two extraspecial groups are \(D_8\) and \(Q_8\), while no extraspecial order lies strictly between \(8\) and \(32\). The rank-two sentence

\[
\exists x\bigl[x\ne e\land R(x,x,e)\land\neg\exists y\,R(y,y,x)\bigr]
\]

is true in \(D_8\) and every extraspecial group of order at least \(32\), because they have noncentral involutions, none of which is a square. It is false in \(Q_8\), whose unique nonidentity involution is the square of each order-four element.

The rank-three sentence

\[
\exists x\exists y\exists z\bigl[\neg R(x,x,e)\land\neg R(y,y,e)\land R(x,y,z)\land\neg R(y,x,z)\bigr]
\]

is false in \(D_8\), whose order-four elements commute, and true in \(Q_8\) and all extraspecial groups of order at least \(32\), which contain noncommuting order-four elements. This proves that the three displayed theories are pairwise distinct, and that their sharp largest minimum order is \(32\).

**4. The Arf sign becomes visible at rank four in order \(32\).** Define \(\Theta\) as the following rank-four sentence, where the last conjunction ranges over exactly \(x,y,z\):

\[
\exists x\exists y\exists z\forall w\left[
\bigwedge_{u\in\{x,y,z\}}\bigl(u\ne e\land R(u,u,e)\land\neg R(w,w,u)\bigr)
\land R(x,y,z)\right].
\]

The quantified variable \(w\) is universal, so each of \(x,y,z\) is a noncentral involution (the central involution has square roots). The product relation forces their three nonzero quotient vectors to form a totally singular two-dimensional subspace. The form \(q_+\) has such a plane, whereas the four-dimensional minus form \(q_-\) has Witt index one and none. Thus \(\Theta\) separates the two order-\(32\) groups; step 2 shows that rank three cannot. This is an exact first-visibility assertion for that pair, not for all higher degrees.

## Verification

`verify.cpp` constructs both central-product types explicitly from bilinear cocycles in degrees \(n=1,2,3\), computes the complete ordered triple atomic diagrams, and recursively computes rank-three Hintikka signatures. `verify_symbolic.py` independently implements the group operations and diagram recursion at degrees one and two; it checks the four row sizes, agreement of the two order-\(32\) theories, distinctness of the three groups' signatures, and the rank-four Arf witness. Compile using `g++ -O2 -std=c++17 verify.cpp -o verify` and run `./verify`; separately run `python3 verify_symbolic.py`. The recorded outputs are in `verification.log`. The infinite-dimensional component of the theorem is justified by step 2, rather than numerical extrapolation.

## Relationship to prior work

Gomaa's 2007 dissertation, *Model Theory and Complexity Theory*, Chapter 3, develops EF games in exactly the relational-multiplication language used here, but its principal classifications concern abelian groups and cyclic/dihedral comparisons, not arbitrary extraspecial two-groups. Kaur and Kulshrestha's preprint *Strongly real special 2-groups* (first posted 2012-10-14, arXiv:1210.3790), §§2–3, supplies the quadratic-form description, classification into two central-product types, and results about strong reality; it does not provide the three-round logical classification or the rank-four separation stated here. The latter result detects totally singular planes, not strong reality. Searches of nearby finite-model-theoretic literature and published research records have not identified a statement implying this theorem; this is a qualified originality assessment, not a proof of uniqueness.

## Limitations

The theorem concerns plain first-order quantifier rank, not counting logic, group terms as function symbols, or bijective-pebble games. It does not classify rank-four theories for all extraspecial degrees; the rank-four witness is asserted only for the two groups of order \(32\). Independent scientific review has not been performed. Historical literature outside the inspected materials may contain equivalent formulations.

## References

1. Walid Gomaa, *Model Theory and Complexity Theory*, University of Maryland dissertation, public repository date 2007-07-06, Chapter 3, especially §§3.1–3.2 and 3.7–3.8. https://drum.lib.umd.edu/items/b8c06e8c-d2da-4d80-923e-0bd02e2a8440
2. Dilpreet Kaur and Amit Kulshrestha, *Strongly real special 2-groups*, arXiv:1210.3790, first posted 2012-10-14, especially §§1–3, Theorem 3.6 and Proposition 3.8. https://arxiv.org/abs/1210.3790
