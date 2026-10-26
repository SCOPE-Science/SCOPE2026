# Conjugacy-class spectrum and stable commuting probability of mixed cyclic automorphism groups

## Finding
For every prime \(p\) and integer \(b\ge2\), put
\[
 A_{p,b}=C_p\oplus C_{p^b},\qquad G_{p,b}=\operatorname{Aut}(A_{p,b}).
\]
The complete conjugacy-class-size distribution in \(G_{p,b}\) is

| Class size | Number of classes |
| --- | ---: |
| \(1\) | \((p-1)p^{b-1}\) |
| \(p(p-1)\) | \((p^2-1)p^{b-2}\) |
| \(p^2\) | \((p-1)(p-2)p^{b-1}\) |

A row with zero multiplicity is absent; in particular, the final row disappears at \(p=2\). There are no other conjugacy-class sizes. Consequently
\[
 k(G_{p,b})=(p-1)(p^2+1)p^{b-2},\qquad
 \operatorname{cp}(G_{p,b})=\frac{p^2+1}{p^3(p-1)},
\]
where \(k\) is the number of conjugacy classes and \(\operatorname{cp}\) is the proportion of ordered commuting pairs. The commuting probability depends on \(p\) but **not** on \(b\), even as \(|G_{p,b}|\) grows. In particular \(\operatorname{cp}(G_{2,b})=5/8\) for every \(b\ge2\), and \(G_{2,b}/Z(G_{2,b})\cong C_2\oplus C_2\).

## Assumptions and scope
The symbols \(C_m\), \(Z(H)\), \(C_H(g)\), and \(k(H)\) denote, respectively, the cyclic group of order \(m\), the centre, an element centralizer, and the number of conjugacy classes. An automorphism of \(A_{p,b}\) can be represented **uniquely** by the constrained matrix
\[
 T(a,u,v,d)=\begin{pmatrix}a&u\\p^{b-1}v&d\end{pmatrix},
\]
where \(a\in\mathbf F_p^\times\), \(u,v\in\mathbf F_p\), and \(d\in(\mathbf Z/p^b\mathbf Z)^\times\). The first row is interpreted modulo \(p\), the second modulo \(p^b\). All exponents and counts concern **ordinary group conjugacy in the automorphism group**, not conjugation by the underlying abelian group, which is trivial. The bound \(b\ge2\) is essential: when \(b=1\), the automorphism group is \(\operatorname{GL}_2(\mathbf F_p)\), with a different class spectrum.

## Proof
**Automorphism normal form.** The first cyclic generator has order \(p\), so its second-coordinate image is a multiple of \(p^{b-1}\). The second cyclic generator has arbitrary first-coordinate image. This gives the displayed matrix form. Its reduction modulo \(p\) is upper triangular with diagonal entries \(a\) and \(d\bmod p\), because \(b\ge2\). The matrix is invertible exactly when these entries are both nonzero. Thus
\[
 |G_{p,b}|=(p-1)^2p^{b+1}.
\]

**Commutation equations.** Set \(\delta=d\bmod p\), \(x=a-\delta\in\mathbf F_p\). For a second automorphism \(T(a',u',v',d')\), put \(\delta'=d'\bmod p\) and \(x'=a'-\delta'\). Multiplying the two constrained matrices and comparing entries in their respective quotient rings shows that they commute **if and only if**
\[
 xu'=x'u,\qquad xv'=x'v,\qquad vu'=v'u
 \quad\text{in }\mathbf F_p.\tag{1}
\]
The last equality comes from the lower-right entry: its difference is \(p^{b-1}(vu'-v'u)\), which vanishes modulo \(p^b\) precisely under the third condition. Hence no higher digit of \(d\) or \(d'\) appears in (1).

**Centralizer trichotomy.** If \(x\ne0\), choose \(a',\delta'\) in \(\mathbf F_p^\times\) arbitrarily, giving \((p-1)^2\) choices. The first two equations uniquely set \(u'=(x'/x)u\) and \(v'=(x'/x)v\); the third then holds. There are \(p^{b-1}\) lifts of \(\delta'\) to \(d'\). Thus
\[
 |C_G(T)|=(p-1)^2p^{b-1},\qquad |T^G|=p^2.\tag{2}
\]
If \(x=0\) but \((u,v)\ne(0,0)\), the first two equations force \(x'=0\). Thus \(a'=\delta'\) has \(p-1\) choices. The single nonzero linear equation \(vu'-v'u=0\) has exactly \(p\) solutions in \(\mathbf F_p^2\), and \(d'\) has \(p^{b-1}\) lifts. Therefore
\[
 |C_G(T)|=(p-1)p^b,\qquad |T^G|=p(p-1).\tag{3}
\]
Finally, when \(x=u=v=0\), all three equations are automatic for every second automorphism, so \(T\in Z(G)\). These are all central elements, since (2) and (3) give nontrivial class sizes for every prime.

**Counting the classes.** In the central case there are \((p-1)p^{b-1}\) elements and thus as many singleton classes. The case \(x=0\), \((u,v)\ne(0,0)\) contains \((p-1)(p^2-1)p^{b-1}\) elements; dividing by the common orbit size \(p(p-1)\) gives \((p^2-1)p^{b-2}\) classes. The case \(x\ne0\) contains \((p-1)(p-2)p^{b+1}\) elements; dividing by \(p^2\) gives \((p-1)(p-2)p^{b-1}\) classes. This proves the table.

Summing the three class counts yields
\[
 k(G)=p^{b-2}\big[p(p-1)+(p^2-1)+p(p-1)(p-2)\big]
       =(p-1)(p^2+1)p^{b-2}.
\]
The number of ordered commuting pairs in a finite group \(G\) is \(\sum_{g\in G}|C_G(g)|=|G|k(G)\). Dividing by \(|G|^2\) gives the stated commuting probability.

For \(p=2\), the diagonal residues satisfy \(a=\delta=1\). The map \(T\mapsto(u,v)\) is a surjective group homomorphism onto \(\mathbf F_2^2\) (the off-diagonal multiplication formulas reduce to addition), and its kernel is exactly the centre determined above. This proves the indicated quotient description.

## Verification
The standalone, dependency-free file `check_aut_classes.py` constructs all automorphisms as constrained matrices and multiplies them directly in their mixed moduli. It exhaustively computes every element centralizer, the class-size multiplicities, and the class count for the seven pairs
\[
 (p,b)\in\{(2,2),(2,3),(2,4),(2,5),(3,2),(3,3),(5,2)\}.
\]
The checker returns `AUT_CYCLIC_MIXED_CLASS_EQUATION_OK`. For example, the distribution of **elements** by class size at \((p,b)=(3,2)\) is \(6\) in size-one classes, \(48\) in size-six classes, and \(54\) in size-nine classes, giving \(20\) classes in total. These finite computations corroborate the proof but are not its basis.

## Relationship to prior work
Hillar and Rhea (2006, Sections 3–4) establish a general matrix description and order formula for automorphisms of finite abelian groups. The normal form above specializes their framework, but their paper does not state or calculate this internal conjugacy-class distribution or the exponent-independent commuting probability. Mann (2008) studies general restrictions imposed by the set of conjugacy-class sizes in finite groups; its theorems do not count the classes of these particular automorphism groups. Related counts of automorphisms with prescribed fixed points and of square-one automorphisms measure different conditions on individual maps, and do not determine their *mutual commutation* or inner centralizers. The present calculation specifically supplies that missing data.

## Limitations
The theorem applies only to the first cyclic exponent equal to one and a strictly larger second exponent; it does not furnish a class equation for \(\operatorname{Aut}(C_{p^a}\oplus C_{p^b})\) with \(a\ge2\). The class spectrum is determined, not a list of individual normal-form representatives of conjugacy orbits. Publication-priority assessment is necessarily incomplete: an older detailed treatment of automorphism groups or a general class-equation formula not located here could imply the result. No independent review is asserted by the mathematical statement.

## References
1. C. J. Hillar and D. L. Rhea, *Automorphisms of Finite Abelian Groups*, arXiv:math/0605185, first submitted 2006-05-08; later *Amer. Math. Monthly* **114** (2007), 917–923. https://arxiv.org/pdf/math/0605185
2. A. Mann, *Conjugacy Class Sizes in Finite Groups*, *J. Aust. Math. Soc.* **85** (2008), 251–255. https://doi.org/10.1017/S1446788708000906
3. A. Ranum, *The Group of Classes of Congruent Matrices with Application to the Group of Isomorphisms of any Abelian Group*, *Trans. Amer. Math. Soc.* **8** (1907), 71–91. https://doi.org/10.2307/1986235 (bibliographic comparison only; full text not inspected).
