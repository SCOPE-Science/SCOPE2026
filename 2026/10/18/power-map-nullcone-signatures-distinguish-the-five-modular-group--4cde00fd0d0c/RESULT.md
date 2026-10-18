# Power-map nullcone signatures distinguish the five modular group algebras of order eight

## Finding
Let \(k=\mathbb F_q\), with \(q=2^f\), \(f\ge1\), and let \(G\) be a group of order eight. Write \(A_G=kG\), \(J_G=\ker(\varepsilon:A_G\to k)\) for the augmentation ideal, and \(N_i(G)=\#\{a\in J_G:a^i=0\}\). The following exact table holds:

| \(G\) | \(N_2(G)\) | \(N_3(G)\) | \(N_4(G)\) |
|---|---:|---:|---:|
| \(C_8\) | \(q^4\) | \(q^5\) | \(q^6\) |
| \(C_4\times C_2\) | \(q^6\) | \(q^6\) | \(q^7\) |
| \(C_2^3\) | \(q^7\) | \(q^7\) | \(q^7\) |
| \(D_8\) | \((2q-1)q^4\) | \((2q-1)q^5\) | \(q^7\) |
| \(Q_8\) | \(q^4\) | \(q^5\) | \(q^7\) |

All five ordered signatures are distinct for every \(q\ge2\). Thus the three lowest nontrivial power-map fiber cardinalities distinguish the modular group algebras of all groups of order eight. In the two nonabelian cases the reduced zero loci have the following explicit geometry: for \(Q_8\), the square-zero and cube-zero loci are linear spaces of dimensions four and five; for \(D_8\), the square-zero locus is two five-spaces meeting in a four-space, while the cube-zero locus is two six-spaces meeting in a five-space. These are assertions about reduced geometric loci, not scheme-theoretic radicality.

## Assumptions and scope
All fields have characteristic two, and point counts are for finite fields \(k\) of size \(q\). The geometric equations hold over arbitrary characteristic-two fields. Products and powers are taken in the associative group algebra, not in the group itself. The ideal \(J_G\) has \(k\)-dimension seven. The integer \(i\) ranges only over \(2,3,4\); counts for other powers are not asserted.

## Proof
For \(C_8\), use \(kC_8\cong k[t]/(t^8)\) with \(t=g+1\). An element of \(J\) vanishing to order \(v\) has \(i\)-th power zero precisely when \(iv\ge8\). Thus \(N_i=q^{8-\lceil8/i\rceil}\), giving the three entries. For \(C_4\times C_2\), write \(A=k[s,t]/(s^4,t^2)\). An augmentation element has the unique form \(a(s)+tb(s)\), with \(a(s)\in s k[s]/(s^4)\) and \(b(s)\in k[s]/(s^4)\). Its square equals \(a(s)^2\), so it squares to zero precisely when the coefficient of \(s\) in \(a\) vanishes: \(q^6\) choices. If this coefficient is nonzero, its cube has a nonzero coefficient of \(s^3\); hence \(N_3=q^6\). Every fourth power vanishes, giving \(N_4=q^7\). For \(C_2^3\), the group algebra is a commutative algebra on three square-zero augmentation generators; every element of \(J\) squares to zero, yielding \(N_2=N_3=N_4=q^7\).

For either nonabelian group, choose generators \(u,v\) and central \(z\) of order two with \(uvu^{-1}v^{-1}=z\), and put \(c=1+z\). Then \(c^2=0\), \(R=k[c]/(c^2)\), and \(A\) is free over \(R\) with basis \(1,u,v,uv\). For \(Q_8\) choose \(u^2=v^2=z\); for \(D_8\) choose \(u^2=z\), \(v^2=1\). Also \((uv)^2=z\) for \(Q_8\), whereas \((uv)^2=1\) for \(D_8\). The three pairwise commutators of \(u,v,uv\) are \(cuv\), \(cv\), and \(cu\), respectively, in either algebra. Write an element of \(J\) as
\[
a=a_0+b_0u+d_0v+e_0uv+c(a_1+b_1u+d_1v+e_1uv),
\qquad a_0=b_0+d_0+e_0.
\]
For notational convenience put \(B=b_0\), \(C=d_0\), \(D=e_0\). Direct multiplication gives
\[
a^2=c\big(s+CDu+BDv+BCuv\big),
\quad s=\begin{cases}B^2+C^2+D^2 & (Q_8),\\ B^2 &(D_8).\end{cases}
\]
Multiplication by \(c\) identifies the four-dimensional quotient \(A/cA\) with \(cA\) as vector spaces. The displayed square vanishes if and only if all four coefficients of its parenthesis vanish. For \(Q_8\), this forces \(B=C=D=0\), and conversely; hence \(N_2(Q_8)=q^4\) and its square-zero locus is the central linear subspace \(cA\). For \(D_8\), it forces \(B=0\), \(CD=0\), with \(q^4\) unrestricted lifted coefficients; hence \(N_2(D_8)=(2q-1)q^4\), and the reduced locus is the union of the two five-dimensional linear spaces \(B=C=0\) and \(B=D=0\), meeting in \(cA\).

To handle cubes, reduce modulo \(cA\), where \(\bar u^2=\bar v^2=1\) and \(\bar u\bar v=\bar v\bar u\). With \(\alpha=\bar u+1\), \(\beta=\bar v+1\), this quotient is \(k[\alpha,\beta]/(\alpha^2,\beta^2)\). Set \(P=B+D\), \(Q=C+D\), and \(K=s+BC+BD+CD\). Modulo \(c\), the element \(a\) becomes \(P\alpha+Q\beta+D\alpha\beta\); the parenthesis in its square becomes \(K+CP\alpha+BQ\beta+BC\alpha\beta\). Consequently \(a^3=0\) is equivalent to
\[
PK=0,\qquad QK=0,\qquad DK+PQ(B+C)=0.
\]
For \(D_8\), \(K=(B+C)(B+D)\). The system is exactly \(K=0\): the reverse implication follows by substitution, while if \(K\ne0\) the first two equations force \(P=Q=0\), contradicting \(K\ne0\). Therefore \(a^3=0\) is equivalent to \((B+C)(B+D)=0\), the union of two six-dimensional linear spaces whose intersection has dimension five. Its number of points is \((2q^2-q)q^4=(2q-1)q^5\).

For \(Q_8\), \(K=B^2+C^2+D^2+BC+BD+CD\). The same first two equations exclude \(K\ne0\). Under \(K=0\), the third reduces to \((B+D)(C+D)(B+C)=0\). At least two of \(B,C,D\) must therefore coincide. Substitution into \(K=0\) forces the third to coincide as well, since a square vanishes over a field only when its base does. Thus \(a^3=0\) if and only if \(B=C=D\). This is a five-dimensional linear locus, giving \(N_3(Q_8)=q^5\).

For both nonabelian groups, every augmentation element has square in the central square-zero ideal \(cA\); hence every fourth power vanishes and \(N_4=q^7\). However this does not imply \(J^4=0\): in the quaternion case \(w=(1+u)(1+v)\in J^2\) satisfies \(w^2=cw\ne0\), so \(J^4\ne0\). These formulas complete the proof.

## Verification
The included `verify.py` constructs all five eight-element groups by independent multiplication tables, computes every group-algebra element over \(\mathbb F_2\) and \(\mathbb F_4\), multiplies them directly, and counts zero squares, cubes, and fourth powers within the augmentation kernel. Across ten exhaustive cases, all twenty-nine independent equality checks (including the fifth group for each field) matched the symbolic table, and the program returned `ALL_ORDER_EIGHT_OK`. The displayed arbitrary-field proof is essential: finite checks alone do not establish the formulas for all \(q\).

## Relationship to prior work
The structure of modular group rings and normalized unit groups has been investigated extensively. Creedon and Gildea (arXiv:0905.4644, 28 May 2009) study the unitary unit group of \(\mathbb F_{2^f}Q_8\); their explicit center and exponent-two subgroup results can explain portions of the square-zero arithmetic, and those facts are not presented as independently new here. Creedon and Gildea's dihedral unit-group work (DOI 10.4153/CMB-2010-098-5) likewise concerns a related algebraic structure. Ivanov, Ivanov, Volkov and Zhou (arXiv:1407.4341) determine Hochschild and Batalin–Vilkovisky operations for the quaternion group ring but do not state the three-power index signature of all five order-eight group algebras. The specific comparison here is the simultaneous \(N_2,N_3,N_4\) signature with explicit geometric cube-zero loci; group-unit orders by themselves do not determine the cube-zero loci. An unlocated group-ring enumeration may nonetheless subsume part or all of this statement.

## Limitations
This is a same-model mathematical proof and finite-field corroboration, not an independent audit. There is no claim to have established an exhaustive literature-priority result. The full dihedral normalized-unit literature has not been exhaustively inspected. Geometry concerns reduced zero sets only. No scheme-theoretic radicality, higher-order group classification, or general formula for arbitrary finite \(2\)-groups is asserted.

## References
1. L. Creedon and J. Gildea, *Unitary Units of the Group Algebra \(\mathbb F_{2^k}Q_8\)*, arXiv:0905.4644 (first public version 2009-05-28).
2. L. Creedon and J. Gildea, *The Structure of the Unit Group of the Group Algebra \(\mathbb F_{2^k}D_8\)*, Canadian Mathematical Bulletin 54 (2011), 237–243, DOI:10.4153/CMB-2010-098-5.
3. A. Ivanov, S. O. Ivanov, Y. Volkov and G. Zhou, *On the Hochschild cohomology ring of the quaternion group of order eight in characteristic two*, arXiv:1407.4341 (first public version 2014-07-16).
