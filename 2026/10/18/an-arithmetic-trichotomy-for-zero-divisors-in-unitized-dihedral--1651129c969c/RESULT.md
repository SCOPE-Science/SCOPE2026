# An arithmetic trichotomy for zero divisors in unitized dihedral quandle algebras

## Finding

**Theorem.** Let \(K=\mathbb F_q\) be any finite field, and let \(R_3=\{0,1,2\}\) have quandle operation \(i\triangleright j=2j-i\pmod 3\). The unitized quandle algebra \(S=K1\oplus K[R_3]\) is a four-dimensional commutative nonassociative algebra. Write \(u=a1+xe_0+ye_1+ze_2\) and let \(L_u:v\mapsto uv\). Define \(s=x+y+z\) and \(Q=x^2+y^2+z^2-xy-xz-yz\). Then

\[\det L_u=a(a+s)(a^2-Q).\]

For a nonzero element \(u\), the existence of a nonzero \(v\) with \(uv=0\) is therefore equivalent to \(\det L_u=0\). The exact number \(Z(q)\) of such nonzero zero divisors is

\[Z(q)=q^3-1+(q-1)B(q),\qquad B(q)=\begin{cases}2q^2-2q+1,&q\equiv1\pmod3,\\2q^2-1,&q\equiv2\pmod3,\\2q^2,&3\mid q.\end{cases}\]

Consequently, the number of elements with injective (equivalently, bijective) left multiplication is \(q^4-Z(q)-1\). This is a complete vertex-count formula for the undirected zero-divisor graph considered for this algebra.

## Assumptions and scope

The quandle algebra \(K[R_3]\) has basis \(e_0,e_1,e_2\) with products \(e_i^2=e_i\) and \(e_ie_j=e_k\) when \(i,j,k\) are distinct. The element \(1\) is adjoined as a two-sided multiplicative identity and is linearly independent from the three quandle basis elements. No associativity is assumed. The zero-divisor graph counts **nonzero** elements with nonzero annihilators; zero itself is excluded. The phrase 'bijective multiplication' is used rather than the potentially ambiguous nonassociative notion of a unit.

The result applies to every prime power \(q\), including characteristics two and three. Congruences modulo three refer to the integer field order. Although characteristic-three coefficient fields are all divisible by three, the other two cases can occur in arbitrary characteristics other than three.

## Proof

For \(u=a1+xe_0+ye_1+ze_2\), the matrix of \(L_u\) relative to \((1,e_0,e_1,e_2)\) is

\[\begin{pmatrix}a&0&0&0\\x&a+x&z&y\\y&z&a+y&x\\z&y&x&a+z\end{pmatrix}.\]

Expand its lower-right determinant. Direct algebraic simplification over \(\mathbb Z[a,x,y,z]\) gives

\[\det\begin{pmatrix}a+x&z&y\\z&a+y&x\\y&x&a+z\end{pmatrix}=(a+s)(a^2-Q).\]

The identity is polynomial over the integers and remains true in every field characteristic. In a finite-dimensional vector space, \(L_u\) is singular precisely when its kernel contains a nonzero vector. Thus singularity characterizes zero divisors, including the zero element in the singularity count.

There are exactly \(q^3\) singular elements with \(a=0\). If \(a\ne0\), scaling the three coefficients by \(a^{-1}\) converts the remaining condition into \((1+s)(1-Q)=0\). It remains to count the triples satisfying \(s=-1\) or \(Q=1\). There are \(q^2\) triples with \(s=-1\).

First suppose \(3\nmid q\), and take a primitive cube root \(\omega\) in a splitting field. Put \(v=x+\omega y+\omega^2z\) and \(v'=x+\omega^2 y+\omega z\). The determinant of the Fourier coordinate transformation from \((x,y,z)\) to \((s,v,v')\) is nonzero (it is a nonzero multiple of three), and a direct product expansion gives \(Q=vv'\).

If \(q\equiv1\pmod3\), the two nontrivial Fourier coordinates range independently over \(K\). Hence \(Q=1\) has \(q(q-1)\) solutions, and intersecting \(s=-1\) leaves \(q-1\) solutions. Inclusion-exclusion yields \(B(q)=q^2+q(q-1)-(q-1)=2q^2-2q+1\).

If \(q\equiv2\pmod3\), the two nontrivial coordinates satisfy \(v'=v^q\) over \(K_2=\mathbb F_{q^2}\); the transformation \((x,y,z)\longleftrightarrow(s,v)\in K\times K_2\) is a \(K\)-linear isomorphism. Thus \(Q=N_{K_2/K}(v)\). The norm-one group has \(q+1\) elements. Therefore \(Q=1\) has \(q(q+1)\) solutions and its intersection with \(s=-1\) has \(q+1\); hence \(B(q)=q^2+q(q+1)-(q+1)=2q^2-1\).

In characteristic three, the polynomial identity \(Q=(x+y+z)^2=s^2\) holds. The two equations \(s=-1\) and \(Q=1\) together select exactly the **two distinct** planes \(s=-1\) and \(s=1\). Consequently \(B(q)=2q^2\). These arguments give the piecewise count \(q^3+(q-1)B(q)\) of all singular left multiplications; subtract one for the zero element. This proves the theorem. \(\square\)

## Verification

Run `python3 verify.py` with the provided standalone script. It constructs the finite fields directly from polynomial quotient representations, computes multiplication tables for the four-dimensional unitized quandle algebra and determines singularity by Gaussian elimination rather than by the displayed factorization. Every element was exhaustively checked for \(q\in\{2,3,4,5,7,8,9\}\). The numbers of nonzero zero divisors were respectively \(14,62,138,320,852,1400,2024\). All agreed with the predicted formulas. The script prints `VERIFY_OK` when all exhaustive comparisons pass. These finite checks support, but do not replace, the symbolic and finite-field counting proof.

## Relationship to prior work

Churchill, Churchill, Fernando and Kousik (arXiv:2608.09149, first public 2026-08-10) introduce zero-divisor graphs of quandle rings. Their Section 6.3 explicitly draws the extended dihedral-quandle graph only over \(\mathbb F_2\) and observes that the nonzero elements other than unity are zero divisors. Our formula recovers its \(14\) vertices but separately evaluates the complete finite-field family and identifies the arithmetic dependence on the splitting of cubic roots and on characteristic three. Bardakov, Passi and Singh (arXiv:2001.06843; Osaka J. Math. 2022) establish basic zero-divisor phenomena in quandle rings; the inspected material does not give this complete finite-field census.

Earlier finite-field results on derivations, idempotents, the algebra of left multiplication operators and Fourier decompositions of Alexander-quandle algebras are conceptually related. The invariant counted here is different: which individual left multiplication operators are singular within this specific four-dimensional *unitized*, nonassociative family. The exact arithmetic count and its three regimes are not statements of those earlier results. No claim is made that those tools are unrelated, nor that indexing searches prove global uniqueness.

## Limitations

Only the number of graph vertices is determined, not the full graph degree distribution, adjacency spectrum or automorphism group. No extension to larger dihedral quandles is asserted. An equivalent implicit consequence of matrix representation theory or unindexed quandle literature remains possible. The proof has undergone self-review and independent audit has not been performed.

## References

1. G. Churchill, I. R. Churchill, N. Fernando and B. Kousik, *A further study of quandles and quandle rings*, arXiv:2608.09149 (2026), especially Definition 1.9 and Section 6.3. https://arxiv.org/abs/2608.09149
2. V. G. Bardakov, I. B. S. Passi and M. Singh, *Zero-divisors and idempotents in quandle rings*, Osaka J. Math. 59 (2022), 611–637; arXiv:2001.06843. https://arxiv.org/abs/2001.06843
