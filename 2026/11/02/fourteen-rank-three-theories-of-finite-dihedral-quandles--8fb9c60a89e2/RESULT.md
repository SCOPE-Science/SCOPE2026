# Fourteen rank-three theories of finite dihedral quandles

## Finding

For every integer \(n\ge 2\), let \(R_n\) denote the dihedral (Takasaki) quandle on \(\mathbb Z/n\mathbb Z\) with operation \(a*b=2b-a\). Regard \(R_n\) as a relational first-order structure with equality and **only** the ternary operation-graph relation \(Q(a,b,c)\), meaning \(a*b=c\). Write \(R_m\equiv_3 R_n\) when these structures satisfy the same sentences of quantifier rank at most three.

**Theorem.** Put \(E=\{2,3,4,5,6,8\}\). For all \(m,n\ge2\),
\[
R_m\equiv_3 R_n\quad\Longleftrightarrow\quad
\bigl(m=n\in E\bigr)\ \lor\ 
\bigl(m,n\notin E\ \text{and}\ \gcd(m,24)=\gcd(n,24)\bigr).
\]
Thus there are exactly **fourteen** theories at rank three: six exceptional singleton classes and eight classes indexed by divisors of \(24\). The least indices of representatives are
\[
2,3,4,5,6,7,8,9,10,12,16,18,20,24.
\]
Every \(R_n\) is rank-three equivalent to one of size at most \(24\); the bound is sharp within this family. In particular \(R_7\equiv_3 R_{11}\equiv_3 R_{25}\), while \(R_8\not\equiv_3 R_{16}\).

## Assumptions and scope

The universe is nonempty, \(n\) is an integer at least two, and equality is part of first-order logic. The operation is **not a function symbol** in the signature. Therefore nested expressions such as \((a*b)*c\) are not atomic formulas: they require quantified witnesses when expressed in this relational language. The statement concerns exactly three rounds of the Ehrenfeucht–Fraïssé game, or equivalently quantifier rank at most three, without restrictions on the number of variables or Boolean combinations of formulas. No claim is made for functional-signature theories, higher rank, or arbitrary Alexander quandles.

## Proof

**1. Exact logical reduction.** For any ordered triple \((a,b,c)\) of selected elements, its complete atomic diagram consists of three equality atoms and the \(27\) ordered instances of \(Q\) with arguments among \(a,b,c\). The quandle translations \(u\mapsto u+v\) are automorphisms; after the first move we can take \(a=0\). Put \(b=d\) and \(c=t\). The entire atomic diagram is uniquely determined by these nine congruence indicators, in the displayed order (with bits numbered \(0\) through \(8\)):

\[
\begin{array}{lll}
E_{ab}:d=0,&E_{ac}:t=0,&E_{bc}:t=d,\\
H_{ab}:2d=0,&H_{ac}:2t=0,&H_{bc}:2(t-d)=0,\\
M_a:t=-d,&M_b:t=2d,&M_c:2t=d.
\end{array}
\]
All congruences are modulo \(n\). For example, \(H_{ab}\) is the atom \(Q(a,b,a)\), and \(M_c\) is \(Q(a,c,b)\). Every other ternary atom either has a repeated argument, and reduces to an \(E\)- or \(H\)-indicator, or has all three arguments represented and is one of the \(M\)-indicators. In particular the nine-bit encoding is equivalent to the full atomic diagram, not an approximation.

For a fixed pair \((0,d)\), let \(P_n(d)\) be the **set** of all nine-bit atomic types attained as \(t\) ranges over \(\mathbb Z/n\mathbb Z\). Under a two-round continuation of the game, this set is a complete invariant of the pointed pair. After three rounds, the first-move type is the set
\[
\mathcal S_n=\{P_n(d):d\in\mathbb Z/n\mathbb Z\}.
\]
Translation makes the first-move choice immaterial. The standard finite back-and-forth recursion therefore yields
\[
R_m\equiv_3 R_n\quad\Longleftrightarrow\quad \mathcal S_m=\mathcal S_n.
\]
The reverse implication can also be read syntactically: a pair-profile difference is witnessed by a rank-three sentence of the form \(\exists a\exists b\,\psi_P(a,b)\), where \(\psi_P\) is the rank-one conjunction saying that exactly the quantifier-free triple diagrams in \(P\) are possible as third vertices.

**2. Uniform symbolic description for \(n\ge9\).** Fix \(d\) and put \(m=\operatorname{ord}(d)=n/\gcd(n,d)\) (\(m=1\) for \(d=0\)). Any third vertex satisfying a nontrivial indicator involving \(t\) belongs to
\[
T=\{0,d,-d,2d\}\ \cup\ \{t:2t=0\}
\ \cup\ \{t:2t=2d\}\ \cup\ \{t:2t=d\}.
\]
The first two doubling equations each include one of the displayed base points, and each doubling equation has at most two solutions. Hence \(|T|\le4+1+1+2=8\). For \(n\ge9\) at least one point outside \(T\) exists, and all such points have one and the same nine-bit atomic diagram (apart from the constant indicators involving \(d\)); the outside type must therefore be included exactly once.

The remaining types are obtained from the finitely many points in \(T\). Coincidences among \(0,d,-d,2d\) depend only on whether \(d,2d,3d\) vanish. If \(n\) is even, writing \(h=n/2\), the extra points from \(2t=0\) and \(2t=2d\) are \(h\) and \(d+h\). Their coincidences with the base points depend only on whether \(2d=0\) or \(4d=0\). Finally, the solutions of \(2t=d\), if present, are one point for odd \(n\) and a pair separated by \(h\) for even \(n\); their intersections with the preceding exceptional points can occur only when \(d=0\) or \(3d=0\). These statements follow immediately by subtracting the displayed congruences. Thus **no other arithmetic property of \(d\) or \(n\)** affects \(P_n(d)\).

It follows that \(P_n(d)\), for \(n\ge9\), depends only on the triple
\[
(\eta,\mu,s),\qquad
\eta=\mathbf1_{2\mid n},\quad
\mu=\min(5,\operatorname{ord}(d)),\quad
s=\mathbf1_{\exists t\, (2t=d)}.
\]
For odd \(n\) the final indicator always equals one; for even \(n\) it is one precisely when \(d\) is even. Substitution into the exceptional-point list gives all **eleven possible pair profiles**. The rightmost column lists their exact nine-bit integers with the least significant bit corresponding to \(E_{ab}\):

| \((\eta,\mu,s)\) | Realizing \((n,d)\) | Set of nine-bit types \(P_n(d)\) |
|---|---|---|
| \((0,1,1)\) | \((9,0)\) | 9, 511 |
| \((0,3,1)\) | \((9,3)\) | 0, 18, 36, 448 |
| \((0,5,1)\) | \((11,1)\) | 0, 18, 36, 64, 128, 256 |
| \((1,1,1)\) | \((10,0)\) | 9, 313, 511 |
| \((1,2,0)\) | \((10,5)\) | 8, 124, 186 |
| \((1,2,1)\) | \((12,6)\) | 8, 124, 186, 264 |
| \((1,3,1)\) | \((12,4)\) | 0, 16, 18, 32, 36, 256, 448 |
| \((1,4,0)\) | \((12,3)\) | 0, 18, 36, 96, 144 |
| \((1,4,1)\) | \((16,4)\) | 0, 18, 36, 96, 144, 256 |
| \((1,5,0)\) | \((10,1)\) | 0, 16, 18, 32, 36, 64, 128 |
| \((1,5,1)\) | \((10,2)\) | 0, 16, 18, 32, 36, 64, 128, 256 |

Each row can be checked by evaluating the at most eight exceptional third vertices and one outside vertex. All eleven profiles in the table are distinct as sets, a fact visible directly from their listed integers.

**3. Exactly eight stable classes.** For odd \(n\ge9\), the realized \(\mu\)-values are \(1\), \(5\), and also \(3\) exactly if \(3\mid n\). No value \(2\) or \(4\) can occur. For even \(n\ge10\), both \((\mu,s)=(5,0)\) and \((5,1)\) occur: take \(d=1\) and \(d=2\), respectively. The value \(\mu=2\) always occurs, with \(s=1\) exactly if \(4\mid n\). The value \(\mu=3\) occurs exactly if \(3\mid n\), always with \(s=1\). The value \(\mu=4\) occurs exactly if \(4\mid n\), with \(s=1\) exactly if \(8\mid n\). The \(\mu=1\) profile always occurs. Therefore the sets \(\mathcal S_n\) for all \(n\ge9\) depend precisely on the four bits encoding divisibility by \(2,3,4,8\), equivalently on \(\gcd(n,24)\). Since the eleven pair profiles are distinct, the eight possible divisibility patterns give **eight distinct** rank-three theories. In the odd coprime-to-\(24\) case, the first representative is \(n=7\), which happens to have exactly the same profile set as the stable odd coprime class.

**4. Small cases and minimality.** For \(2\le n\le8\), direct examination of all possible pairs and third vertices yields the exceptional singleton theories \(2,3,4,5,6,8\), in addition to the stable class already represented by \(7\). The finite check is fully explicit: `type_certificate.json` gives all nineteen atomic-pair profiles that occur among the fourteen representative structures (as sorted lists of nine-bit integers) and the full list of constituent profiles for each representative. Those fourteen profile-sets are pairwise unequal; `verify.py` computes the actual \(27\) ternary atoms and three equality atoms independently and checks the certificate by a literal three-round type recursion. This exact finite check is part of the proof, not a probabilistic experiment.

For each of the eight stable patterns the first admissible index is respectively \(7,9,10,12,16,18,20,24\) when sorted by index; together with the six singleton exceptions this gives the stated fourteen representatives. The class with \(\gcd(n,24)=24\) has no representative below \(24\), proving the sharp bound.

## Verification

From the directory containing this file, run `python3 verify.py`. The program requires only Python's standard library. It checks independently implemented literal atomic diagrams and nine-flag compressed diagrams for all fourteen representatives, verifies the eleven symbolic pair-profile keys, compares the full rank-three partitions through modulus \(500\) as a regression check, and prints `VERIFY_OK`. The exact expected output is in `verification_output.txt`. The machine-readable finite certificate is `type_certificate.json`; its nine-bit integers can be reconstructed directly from the congruence definitions above.

The universal assertion for all \(n\) rests on the algebraic candidate/overlap proof in Sections 2–3, **not** on the finite regression range. The finite certificate is exhaustive only for the specified small representative structures and canonical pair keys.

## Relationship to prior work

The dihedral/Takasaki operation is a standard algebraic example; the classifying subject is **bounded-rank first-order theory in the ternary relational language**, rather than quandle isomorphism or automorphism. Ho and Nelson classify quandle operation tables up to isomorphism for sizes at most five, and Elhamdadi, Macquarrie, and Restrepo prove the affine automorphism-group formula for every dihedral quandle. The present collapse of infinitely many pairwise nonisomorphic quandles into fourteen rank-three theories is not implied by either statement: isomorphism classification and automorphism-group size retain cardinality information that rank-three formulas need not retain.

Other work on Takasaki quotients concerns homomorphic images or subquandles rather than bounded logical equivalence. No claim of an exhaustive absence of related literature is made.

## Limitations

The result is specific to the operation **graph** relation, not a function symbol or a language with named group operations, constants, orders, or counting quantifiers. The classification does not imply equality of full first-order theories (distinct finite structures are distinguishable at sufficient quantifier rank). The independent external validation of the proof and any claim of exhaustive historical novelty are outside the present evidence.

## References

1. B. Ho and S. Nelson, *Matrices and Finite Quandles*, arXiv:math/0412417 (first publicly posted 2004-12-20), *Homology, Homotopy and Applications* 7 (2005), 197–208. https://arxiv.org/abs/math/0412417
2. M. Elhamdadi, J. Macquarrie, R. Restrepo, *Automorphism Groups of Quandles*, arXiv:1012.5291 (first publicly posted 2010-12-23), *Journal of Algebra and Its Applications* 11 (2012), 1250008. https://arxiv.org/abs/1012.5291
3. Y. Bae and S. Kim, *On Quotient Structure of Takasaki Quandles*, *Journal of Knot Theory and Its Ramifications* 22 (2013), 1341001, DOI:10.1142/S0218216513410010. Abstract and bibliographic record reviewed; full text not inspected.
4. M. Takasaki, *Abstraction of Symmetric Transformations*, *Tohoku Mathematical Journal* 49 (1943), 145–207. Historical foundational reference; its exact day of first public appearance has not been established. https://www.jstage.jst.go.jp/article/tmj1911/49/0/49_0_145/_article/-char/en
