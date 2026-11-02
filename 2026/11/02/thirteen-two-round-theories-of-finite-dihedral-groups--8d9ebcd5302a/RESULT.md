# Thirteen two-round theories of finite dihedral groups

## Finding
For \(n\ge3\), write \(D_{2n}=\langle r,s\mid r^n=s^2=1,\ srs=r^{-1}\rangle\), of order \(2n\). In the language with equality, named identity \(e\), and ternary multiplication \(M(x,y,z)\) meaning \(xy=z\), let \(\equiv_2\) denote agreement on all sentences of quantifier rank at most two. With \(E=\{3,4,5,6,8\}\), the complete classification is
\[
D_{2m}\equiv_2 D_{2n}\quad\Longleftrightarrow\quad
(m=n\in E)\ \lor\ \bigl(m,n\notin E\ \land\ \gcd(m,24)=\gcd(n,24)\bigr).
\]
The thirteen least representative rotation widths are \(3,4,5,6,7,8,9,10,12,16,18,20,24\); the largest least representative has \(48\) group elements.

## Assumptions and scope
All groups are finite, \(n\ge3\); \(D_{2n}\) denotes order \(2n\), not order \(n\). Multiplication is a **ternary relation**, not a function symbol, and the identity is named. Quantifier rank is the nesting depth of first-order quantifiers. No extra predicates identify rotations or reflections.

## Proof
**(1) Two-round atomic reduction for cyclic groups.** Use additive notation for \(C_n=\mathbb Z/n\mathbb Z\). Fix the first selected element \(x\). Every atomic equality or addition statement on \(0,x,y\) is determined by the eight Boolean tests
\[
x=0,\quad 2x=0,\quad y=0,\quad 2y=0,\quad y=x,\quad y=-x,\quad y=2x,\quad 2y=x.
\]
Indeed, exhaust the nine possible ordered input pairs in an addition atom and the three possible outputs. For instance \(x+y=x\) means \(y=0\), \(x+x=y\) means \(y=2x\), and \(x+y=0\) means \(y=-x\). These tests also determine all equality atoms. Conversely each displayed test is atomic or a Boolean combination of the atomic diagram. Consequently the one-round extension type of a pointed \(C_n,x\) is precisely the **set** of Boolean vectors realized by varying \(y\). The rank-two theory is precisely the set of these pointed extension types as \(x\) varies.

**(2) Large-order reduction.** For fixed \(x\), all test vectors outside \(\{0,x,-x,2x\}\), the solutions of \(2y=x\), and the nonzero element of order two (if present), are one generic vector. These exceptional sets have at most \(4+2+1=7\) elements; thus, for \(n\ge9\), the generic vector exists. Their collisions are determined by the order of \(x\) when it divides \(2,3,4\); their remaining multiplicity-free pattern is determined by parity of \(n\) and whether \(x\in2C_n\). The fact that the equation \(2y=x\) has zero, one, or two solutions follows directly from \(\gcd(2,n)\). This proves the following complete pointed classification for \(n\ge9\): \(x=0\); possible \(x\) of orders \(2,3,4\), with the information of membership in \(2C_n\); and \(x\) of order at least five, again distinguished only by membership in \(2C_n\). The categories have different extension Boolean-vector sets (inspect the displayed eight tests).

For odd \(n\ge9\), \(2C_n=C_n\); there is always a generic nonzero element of order at least five, and the remaining optional category is order three, present exactly when \(3\mid n\). For even \(n\ge10\), both generic categories exist (\(x=1\) and \(x=2\)); order-two elements occur, with the unique involution divisible by two precisely when \(4\mid n\); order-three elements occur exactly when \(3\mid n\); and order-four elements occur exactly when \(4\mid n\), with the order-four elements divisible by two precisely when \(8\mid n\). Therefore the collection of pointed types, hence the rank-two theory of \(C_n\), is determined by \(\gcd(n,24)\) in this large range. Distinct divisors of \(24\) give distinct collections: divisibility by \(2,3,4,8\) is detected by the presence of the corresponding order/parity/square-root pointed category. For odd \(n=7\), an identical check of the eight Boolean tests yields the same root type as all odd \(n\ge9\) not divisible by three.

**(3) Finite exceptions.** The complete exact atomic-diagram recurrence described in Verification, run on the finite cases \(3\le n\le24\), proves that \(C_3,C_4,C_5,C_6,C_8\) each form a singleton theory not matching any other representative, and that the other eight minimal representative widths are \(7,9,10,12,16,18,20,24\). Combined with the infinite classification in (2), this proves the asserted thirteen cyclic-group classes. This finite computation exhausts the stated bounded cases, rather than extrapolating any infinite claim.

**(4) Transfer to dihedral groups.** Gomaa (2007), Lemma 3.10, proves in this first-order group language that for each quantifier rank \(\ell\), \(D_{2m}\equiv_\ell D_{2n}\) holds if and only if \(C_m\equiv_\ell C_n\). The primary proof was inspected (dissertation pp. 87–88), including its EF-game correspondence between rotations and modular residues and the reference for the converse Duplicator strategy. At \(\ell=2\), steps (1)–(3) give the claimed dihedral classification. A separate full atomic-diagram computation on dihedral multiplication, which does **not** assume the transfer lemma, reproduces all thirteen classes through width 200.

## Verification
The accompanying standalone C++ program `dihedral_rank2.cpp` enumerates every ordered pair of selected group elements for each width \(3\le n\le200\). It encodes all atomic equality and multiplication formulas on the identity and selected elements, then computes exact rank-one pointed sets and rank-two root sets (with set equality, not probabilistic hash equality). Its recorded output contains precisely thirteen classes. Independently, `cyclic_rank2.cpp` carries out the same construction in cyclic groups through width 110, and `rank2_profile_invariants.py` enumerates pointed cyclic types through width 144 using a separate implementation. The small representative table and symbolic case split above jointly certify the infinite result; finite computations alone are not used to assert stabilization.

## Relationship to prior work
Gomaa, *Model Theory and Complexity Theory* (2007), Section 3.8, Lemma 3.10, establishes the dihedral–cyclic equivalence transfer for arbitrary quantifier rank; Theorem 3.14 supplies broad upper and lower logical-depth bounds. These results do not state the exact rank-two, thirteen-class arithmetic classification, which is obtained here by analyzing all pointed two-round atomic extension types. The pre-existing classification for a different ternary quandle-like operation \(Q(a,b,c)\iff2b-a=c\) has superficially similar modulus-\(24\) behaviour but has a different signature and rank; it does not yield the rank-two relational group theorem by quantifier-rank-preserving interpretation.

## Limitations
The classification concerns exactly quantifier rank two and multiplication **as a relation**. It does not apply to functional multiplication terms or higher ranks without additional work. The literature search and inspected full primary material support a distinct claim, but cannot exclude all unindexed historical formulations. No independent mathematical audit has occurred.

## References
1. W. Gomaa, *Model Theory and Complexity Theory*, PhD dissertation, University of Maryland (2007), Section 3.8, Lemma 3.10 and Theorem 3.14. University archive: https://drum.lib.umd.edu/items/b8c06e8c-d2da-4d80-923e-0bd02e2a8440 (first public date 2007-07-06).
2. W. Gomaa, *Descriptive Complexity of Finite Abelian Groups*, International Journal of Algebra and Computation (2010), doi:10.1142/S0218196710006047. Only bibliographical abstract was accessible for this edition; the 2007 dissertation supplied the primary complete mathematical text.
