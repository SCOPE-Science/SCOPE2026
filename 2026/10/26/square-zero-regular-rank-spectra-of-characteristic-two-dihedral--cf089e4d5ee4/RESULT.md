# Square-zero regular-rank spectra of characteristic-two dihedral group algebras

## Finding

For an odd positive integer \(m\), an even prime power \(q=2^f\), and the dihedral group
\[G=D_{8m}=\langle r,s\mid r^{4m}=s^2=1,\ srs=r^{-1}\rangle,\]
let \(A=\mathbb F_q[G]\), of dimension \(8m\). For \(x^2=0\), write \(\rho(x)=\dim_{\mathbb F_q} xA=\operatorname{rank}_{\mathbb F_q}(L_x)\). The entire polynomial \(\mathcal R_{q,m}(z)=\sum_{x^2=0}z^{\rho(x)}\) factors into a uniform rank polynomial for the dihedral group of order eight and rank polynomials for two-by-two matrices over length-four chain rings.

To specify the factors, factor \(T^m-1\) into monic irreducibles in \(\mathbb F_q[T]\). Ignore \(T-1\), and group the remaining factors into orbits under monic reciprocal \(f(T)\mapsto f^*(T)=T^{\deg f}f(T^{-1})/f(0)\). Each self-reciprocal factor has even degree \(2d\); attach weight \(d\). Each pair \(\{f,f^*\}\) of distinct factors of common degree \(d\) also has weight \(d\). Denote this multiset of weights by \(\{d_\omega\}_{\omega\in\mathcal O}\). It satisfies \(\sum_\omega d_\omega=(m-1)/2\).

For each prime power \(Q\), write \(a_Q=(Q-1)(Q+1)^2\) and \(b_Q=(Q^2-1)(Q^2-Q)\). Define
\[\begin{aligned}
H_q(z)&=1+(q-1)z+(q^3-q)z^2+(2q^5-q^4-q^3)z^4,\\
P_Q(z)&=1+a_Qz^2+(b_Q+a_QQ^3)z^4\\
&\quad+\bigl[a_Q(Q^4-Q^3)+(Q^2-1)Q^5\bigr]z^6\\
&\quad+\bigl[b_QQ^4+(Q^2-1)(2Q^6-Q^5)\bigr]z^8.
\end{aligned}\]
Then the rank enumerator is
\[\boxed{\mathcal R_{q,m}(z)=H_q(z)\prod_{\omega\in\mathcal O}P_{q^{d_\omega}}(z^{d_\omega}).}\]
The empty product for \(m=1\) is one. Thus
\[\mathcal R_{q,m}(1)=(2q-1)q^4\prod_{\omega}(3q^{8d_\omega}-2q^{6d_\omega}).\]
The largest possible rank is \(4m\). Its coefficient, which counts acyclic regular-module differentials \((A,L_x)\), is
\[\boxed{(2q^5-q^4-q^3)\prod_{\omega}\left[b_{Q_\omega}Q_\omega^4+(Q_\omega^2-1)(2Q_\omega^6-Q_\omega^5)\right]},\qquad Q_\omega=q^{d_\omega}.\]
Acyclic means \(\ker L_x=\operatorname{im}L_x\); since \(L_x^2=0\) on an \(8m\)-dimensional vector space, this is equivalent to \(\rho(x)=4m\). Only zero has rank zero.

## Assumptions and scope

All fields have characteristic two, \(q\) is an arbitrary power of two, and \(m\) is any odd positive integer. The group has **order \(8m\)**, not \(4m\). Elements are counted individually in the full labeled group algebra, not up to conjugacy and not by the number of distinct left ideals. The rank is the ordinary \(\mathbb F_q\)-dimension of \(xA\); a block over an extension field \(\mathbb F_{q^d}\) contributes a factor \(d\) to this rank.

## Proof

**1. Algebra blocks.** Write \(r=uv\) where \(u\) has order \(m\) and \(v\) has order four; the oddness of \(m\) gives \(\langle r\rangle\cong C_m\times C_4\). Conjugation by \(s\) inverts each factor. Hence \(A\) is a crossed product of \(\mathbb F_q[C_m]\otimes\mathbb F_q[C_4]\) with the order-two inversion action. The first factor is a product of finite fields, indexed by the irreducible factors of \(T^m-1\), while the second is \(R_4=\mathbb F_q[t]/(t^4)\), \(t=v+1\). Inversion sends \(t\) to \(t/(1+t)=t+t^2+t^3\).

The trivial character of \(C_m\) contributes the entire algebra \(\mathbb F_q[D_8]\). For a pair of distinct reciprocal irreducible factors of degree \(d\), inversion swaps the two factors, and the crossed product of the swapped copies is \(M_2(\mathbb F_{q^d}[t]/(t^4))\). For a nontrivial self-reciprocal irreducible factor of degree \(2d\), inversion induces the nontrivial Galois automorphism \(\sigma\) of \(K=\mathbb F_{q^{2d}}\) over \(F=\mathbb F_{q^d}\). The action on \(K[t]/(t^4)\) combines \(\sigma\) with \(t\mapsto t+t^2+t^3\). Choose \(\theta\in K\) with \(\theta+\sigma(\theta)=1\). The element \(w=t+\theta t^2+\theta t^3\) is invariant and generates the fixed ring \(F[w]/(w^4)\), since \(w\equiv t\pmod{t^2}\). Galois descent identifies the associated crossed product with the endomorphism ring of the rank-two free module \(K[t]/(t^4)\) over its fixed ring, hence with \(M_2(F[w]/(w^4))\). Therefore
\[A\cong\mathbb F_q[D_8]\times\prod_{\omega\in\mathcal O} M_2(\mathbb F_{q^{d_\omega}}[w]/(w^4)).\]
The dimensions match: \(8+\sum_\omega16d_\omega=8m\).

**2. The \(D_8\) factor.** Put \(B=\mathbb F_q[t]/(t^4)\), and write any group-algebra element as \(x=a+bs\), where \(a,b\in B\) and \(s a=a^*s\), with \(t^*=t+t^2+t^3\). Then \(x^2=0\) if and only if \(a^2+bb^*=0\) and \(ab+ba^*=0\). Expanding \(a=\sum_{i=0}^3a_it^i\) and \(b=\sum_{i=0}^3b_it^i\), these conditions reduce exactly to \(a_0=b_0\), \(a_1=0\), and \(b_1(b_0+b_1)=0\); all higher coefficients are free.

When \(b_0\ne0\), there are \(2(q-1)q^4\) solutions; the \(s\)-coefficient \(b\) is a unit, so \(xB\) already has \(\mathbb F_q\)-dimension four, and \(x^2=0\) forces \(\rho(x)=4\). When \(b_0=0\), also \(b_1=0\), so \(x=t^2[(a_2+a_3t)+(b_2+b_3t)s]\). Its left-multiplication image is governed by the two-by-two matrix \(\left(\begin{smallmatrix}a_2+a_3t&b_2+b_3t\\b_2+b_3t&a_2+a_3t\end{smallmatrix}\right)\) acting on \((\mathbb F_q[t]/t^2)^2\). If \(a_2+b_2\ne0\), its image has dimension four; there are \((q^2-q)q^2=q^4-q^3\) such elements. If \(a_2=b_2\ne0\), the image has dimension two, giving \((q-1)q^2\) elements. Finally if \(a_2=b_2=0\), the image has dimension two when \(a_3\ne b_3\) (\(q^2-q\) choices), one when \(a_3=b_3\ne0\) (\(q-1\) choices), and zero for the zero element. Adding the cases gives exactly \(H_q\).

**3. A length-four matrix factor.** Fix \(Q=2^e\), \(S=\mathbb F_Q[t]/(t^4)\), and enumerate \(X\in M_2(S)\) with \(X^2=0\) by the dimension of the left-multiplication image on \(M_2(S)\). Right multiplication by \(X\) on either matrix column shows that this rank is twice the \(\mathbb F_Q\)-dimension of \(\operatorname{im}(X:S^2\to S^2)\).

Let \(a_Q\) denote the number of rank-one matrices over \(\mathbb F_Q\) and \(b_Q\) the number of invertible two-by-two matrices; the stated formulas count them. First take \(X=t^2(B+tC)\), with \(B,C\in M_2(\mathbb F_Q)\). All these matrices square to zero. When \(B=0\), the rank contributions \(0,2,4\) have counts \(1,a_Q,b_Q\). For rank-one \(B\) (\(a_Q\) possibilities), its Schur complementary entry in \(C\) vanishes in \(Q^3\) of the \(Q^4\) cases, yielding rank four, and is nonzero in the other \(Q^4-Q^3\), yielding rank six. For invertible \(B\), any \(C\) gives rank eight, accounting for \(b_QQ^4\) elements.

Next take \(X=t(J+tB+t^2C)\), where the reduction \(J\) is nonzero and satisfies \(J^2=0\). There are \(Q^2-1\) choices for \(J\), and conjugating one of them to \(E_{12}\) shows that \(JB+BJ=0\) forces \(B=bI+cJ\), giving \(Q^2\) choices; \(C\) is arbitrary (\(Q^4\) choices). After pivoting at the \(t\)-entry, the complementary Smith entry is \(t^3(C_{21}+b^2)\). It vanishes for \(Q^3\) choices of \(C\) (per \(B\)), giving rank six, and is nonzero for the other \((Q-1)Q^3\), giving rank eight. Hence this case contributes \((Q^2-1)Q^5\) at rank six and \((Q^2-1)(Q-1)Q^5\) at rank eight.

Finally take \(X=J+tB+t^2C+t^3D\) with nonzero reduction \(J^2=0\). The successive equations from \(X^2=0\) force \(B=bI+cJ\), and then impose two independent linear conditions each on \(C\) and \(D\). Thus the count is \((Q^2-1)Q^6\). Each such operator has a unit matrix entry, and since \(X^2=0\) its image on \(S^2\) has the maximum allowed dimension four; therefore each has left-regular rank eight. Summing these disjoint cases produces precisely \(P_Q\). Substituting one gives \(P_Q(1)=Q^8+2(Q^2-1)Q^6=3Q^8-2Q^6\).

**4. Multiplicativity.** A square-zero element in a finite direct product is exactly a tuple of square-zero elements of its factors, and the dimensions of the images of its blockwise left multiplications add. Over \(\mathbb F_q\), an \(\mathbb F_{q^d}\)-rank contribution is multiplied by \(d\). This proves the product identity. Since \(H_q\) has degree four and each \(P_Q\) degree eight, the maximal rank is \(4+8\sum d_\omega=4m\). Its coefficient and the count at \(z=1\) follow. Both leading coefficients are strictly positive for \(q\ge2\), so the maximum occurs.

## Verification

The two standalone C++17 programs included in `checks/` conduct independent brute-force tests of the algebra identities, separate from the block proof:

```
c++ -std=c++17 -O2 checks/verify_dihedral.cpp -o check_d
./check_d 1
./check_d 3
c++ -std=c++17 -O2 checks/verify_local.cpp -o check_l
./check_l
```

The first exhaustively checks all \(2^8\) elements of \(\mathbb F_2[D_8]\) and all \(2^{24}\) elements of \(\mathbb F_2[D_{24}]\), computes squares using the group law, and computes ranks of full left-regular matrices. For \(D_{24}\), the rank counts are \(1,1,15,9,172,78,996,168,4512,384,9024,15360\) at ranks \(0,1,2,3,4,5,6,7,8,9,10,12\), respectively; total \(30720\). This agrees coefficient-by-coefficient with \(H_2(z)P_2(z)\). The second exhaustively checks all \(4^8\) group-algebra elements of \(\mathbb F_4[D_8]\), finding ranks \(0:1\), \(1:3\), \(2:60\), \(4:1728\); it also checks all \(2^{16}\) matrices in \(M_2(\mathbb F_2[t]/t^4)\), finding ranks \(0:1\), \(2:9\), \(4:78\), \(6:168\), \(8:384\). These finite enumerations are checks, not proofs for unbounded \(m\) and \(q\); the general proof is above.

## Relationship to prior work

Brochero Martínez (arXiv:1405.3716, first public 2014-05-14) analyzes reciprocal factors and the semisimple case of dihedral group algebras; his Theorem 3.1 requires that the characteristic not divide the rotation subgroup order. Here the rotation subgroup has order \(4m\) in characteristic two, so its repeated-root length-four blocks require new analysis. Cao, Cao, Fu, and Gao (arXiv:1902.07533, especially Theorems 2.4 and 5.1) decompose and enumerate *self-dual binary left ideals* in these same group algebras. They do not give counts by square-zero generator and exact rank of the associated multiplication differential: multiple generators can have the same image ideal, and the square-zero condition is additional. Previously established rank enumerations of square-zero matrices over length-two chain rings do not automatically determine the length-four blocks or this characteristic-two dihedral product. Existing enumeration of traceless matrices over discrete valuation rings likewise does not count the square-zero subset of all matrices.

## Limitations

The result assumes \(m\) odd and characteristic two; it does not treat the larger two-primary cyclic factor when \(m\) is even. It counts elements of the algebra rather than isomorphism classes of differential modules, and it does not enumerate distinct left ideals or weight distributions of associated codes. The factorization is explicit once \(T^m-1\) is factored, but no complexity bound for factoring is asserted. Absolute publication priority and independent mathematical validation have not been established.

## References

1. F. E. Brochero Martínez, *Structure of Finite dihedral group algebra*, arXiv:1405.3716, first public 2014-05-14, https://arxiv.org/abs/1405.3716. Theorem 3.1 and reciprocal-factor setup.
2. Y. Cao, Y. Cao, F.-W. Fu, and J. Gao, *Self-dual binary [8m,4m]-codes constructed by left ideals of the dihedral group algebra*, arXiv:1902.07533, 2019, https://arxiv.org/abs/1902.07533. Theorems 2.4 and 5.1 and explicit examples.
3. A. Carnevale, S. Shechter, and C. Voll, *Enumerating traceless matrices over compact discrete valuation rings*, arXiv:1709.02717, 2017, https://arxiv.org/abs/1709.02717. Related but different traceless-image enumeration.
