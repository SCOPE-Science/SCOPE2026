# Adjoint-rank distribution in finite affine-transformation Lie algebras

## Finding

**Theorem.** Fix any prime power \(q\) and integer \(n\ge 3\). On \(V=\mathbb F_q^n\), put
\[
\mathfrak a_n=\mathfrak{gl}(V)\ltimes V,
\qquad [(A,u),(B,v)]=([A,B],Av-Bu).
\]
For a matrix \(A\), let \(c(A)=\dim_{\mathbb F_q}\{B:AB=BA\}\), let \(\lambda_f(A)\) be its rational-canonical partition for each monic irreducible \(f\), and write \(b_s=m_s(\lambda_t(A))\) for the number of size-\(s\) Jordan blocks at eigenvalue zero. Define \(k=\sum_s b_s\), \(t_s=\sum_{j\le s}b_j\), and \(h_s=\sum_{j<s}b_j\). For \(u\in V\), let \(L=0\) if \(u\in\operatorname{im}A\); otherwise \(L\) is the least integer for which \(u\in\operatorname{im}A+\ker A^L\). Then
\[
\operatorname{rank}(\operatorname{ad}_{(A,u)})=
 n^2+n-c(A)-k+\begin{cases}0,&L=0,\\t_L,&L>0.\end{cases}
\tag{1}
\]
For every similarity class \([A]\), let \(N_A=|\operatorname{GL}_n(q)|/|C_{\operatorname{GL}_n(q)}(A)|\) and \(r_A=n^2+n-c(A)-k\). The **complete adjoint-rank enumerator** is
\[
\mathcal R_{n,q}(z)=
 \sum_{[A]}N_Aq^{n-k}
 \left[z^{r_A}+\sum_{s:b_s>0}q^{h_s}(q^{b_s}-1)z^{r_A+t_s}\right].
\tag{2}
\]
The sum ranges over all similarity classes of all \(n\times n\) matrices, including singular matrices, and has coefficient at \(z^r\) equal to the exact number of affine Lie algebra elements having adjoint rank \(r\). Every quantity in (2) is explicit from finite-field rational canonical data:
\[
 c(A)=\sum_f\deg(f)\sum_{j\ge1}(\lambda'_{f,j})^2,
 \qquad |C_{\operatorname{GL}_n(q)}(A)|=
 q^{c(A)}\prod_f\prod_{s\ge1}\prod_{i=1}^{m_s(\lambda_f)}(1-q^{-i\deg f}).
\tag{3}
\]
In particular, the number of ordered commuting pairs in \(\mathfrak a_n\) is
\[
 \sum_{A\in M_n(\mathbb F_q)}q^{n+c(A)}
 \left(1+\sum_{s:b_s>0}(1-q^{-b_s})\right).
\tag{4}
\]
The probability is (4) divided by \(q^{2(n^2+n)}\).

For the first nontrivial dimension \(n=3\), the only possible adjoint ranks are \(0,3,5,6,7,8,9\). Their exact counts are
\[
\begin{aligned}
 a_0&=1,\\
 a_3&=(q-1)(q+1)(q^2+1),\\
 a_5&=q(q-1)(q^2+q+1)^2,\\
 a_6&=q(q-1)(q^2+q+1)(q^3+q^2-1),\\
 a_7&=q^2(q-1)(q^2+q+1)(q^4+q^3-2q-1),\\
 a_8&=q^3(q-1)(q^2+q+1)(q^4+q^3-2q-1),\\
 a_9&=q^3(q-1)(q+1)(q^7-2q^4-q^3+2q+1).
\end{aligned}
\tag{5}
\]
Consequently, the exact number of commuting pairs in the twelve-dimensional Lie algebra \(\mathfrak a_3\) is
\[
 q^6(q^9+2q^8+4q^7+q^6-6q^5-5q^4+4q^2+q-1).
\tag{6}
\]
For \(q=2\), the rank counts in the order displayed are \(1,15,98,154,532,1064,2232\), totalling \(4096\); the number of commuting ordered pairs is \(86080\).

## Assumptions and scope

All Lie brackets are additive matrix commutators and the natural action on column vectors. The field is any finite field, of any characteristic; no invertibility is imposed on \(A\). The adjoint map is linear on the \((n^2+n)\)-dimensional Lie algebra. The zero-primary partition \(\lambda_t(A)\) is empty if \(A\) is invertible. The zero power convention is excluded by setting \(L=0\) explicitly when \(u\in\operatorname{im}A\). The parameter \(L\) exists because the generalized zero-eigenspace eventually lies in \(\ker A^n\).

## Proof

For \(x=(A,u)\), the centralizer equation for a generic \((B,v)\) is \(AB=BA\) and \(Av=Bu\). Set \(C(A)=\{B:AB=BA\}\) and define \(\Phi_u:C(A)\to V/\operatorname{im}A\) by \(B\mapsto Bu+\operatorname{im}A\). Because \(C(A)\) preserves \(\operatorname{im}A\), this is well defined. Each \(B\in\ker\Phi_u\) admits precisely \(q^k\) compatible vectors \(v\), where \(k=\dim\ker A\). Thus
\[
\dim C_{\mathfrak a_n}(x)=c(A)+k-\operatorname{rank}\Phi_u.
\tag{7}
\]
The invertible-primary summand of \(V\) lies in \(\operatorname{im}A\), so only the zero-primary summand matters. Regard it as a \(\mathbb F_q[t]\)-module \(\bigoplus_{s\ge1}(\mathbb F_q[t]/t^s)^{b_s}\), with \(t\) acting as \(A\). Its quotient by \(tV\) consists of one top coordinate per Jordan block. If \(u\in\operatorname{im}A\), then \(\Phi_u=0\). Otherwise, the largest block size carrying a nonzero top coordinate of \(u\) is precisely \(L\). A commuting module endomorphism cannot send a size-\(L\) block generator to a nonzero top coordinate of a block of size \(s>L\), since its image is killed by \(t^L\). Therefore \(\operatorname{im}\Phi_u\) is contained in the span of the tops of blocks of sizes \(s\le L\).

Conversely, select a size-\(L\) source block with nonzero top coefficient in \(u\). For every target block of size \(s\le L\), the module homomorphism sending that source generator to the target generator and vanishing on all other source blocks commutes with \(A\). Modulo \(\operatorname{im}A\), it maps \(u\) to a nonzero scalar multiple of the chosen target top. These homomorphisms span all \(t_L\) target tops. Hence \(\operatorname{rank}\Phi_u=t_L\), proving (1) from (7), including all zero-characteristic and degeneracy boundaries.

There are \(q^{n-k}\) vectors with \(L=0\). To have \(L=s>0\), all top coordinates of blocks longer than \(s\) must vanish, top coordinates in the \(b_s\) blocks of size \(s\) must not all vanish, and the \(h_s\) shorter-block top coordinates are arbitrary. The remaining \(n-k\) coordinates are arbitrary. This gives exactly \(q^{n-k+h_s}(q^{b_s}-1)\) vectors, which, together with similarity-class multiplicities, proves (2). Formula (3) follows by counting module homomorphisms between the cyclic primary summands and invertible automorphisms of each semisimple quotient; the dimension contribution of a pair of blocks of sizes \(i,j\) for an irreducible polynomial \(f\) is \(\deg(f)\min(i,j)\). For (4), multiply each vector count at level \(s\) by its Lie-centralizer size \(q^{c(A)+k-t_s}\). This gives \(q^{n+c(A)}(1-q^{-b_s})\); the level-zero contribution is \(q^{n+c(A)}\).

For \(n=3\), enumerate rational canonical types with the following exhaustive characteristic-polynomial patterns: irreducible cubic; irreducible quadratic times one linear factor; three distinct linear factors; a repeated eigenvalue with Jordan type \((2)\) or \((1,1)\) plus a different eigenvalue; and a single linear eigenvalue with Jordan type \((3)\), \((2,1)\), or \((1,1,1)\). Split each class by whether zero occurs as an eigenvalue. The total is seventeen symbolic strata, explicitly enumerated by `derive_n3.py`. Substitution of their exact matrix-class sizes and vector weights into (2), followed by polynomial simplification, yields (5); summing \(a_rq^{12-r}\) yields (6). The identity \(\sum_ra_r=q^{12}\) follows both by the vector partition and by direct polynomial simplification.

## Verification

`verify.py` builds an independent matrix of the adjoint operator and computes its rank over each tested finite field. It separately computes \(c(A)\), \(k\), and \(L\) by linear algebra, without invoking rational canonical forms. Exhaustive tests checked all \(64\) elements for \(n=2,q=2\), all \(729\) elements for \(n=2,q=3\), and all \(4096\) elements for \(n=3,q=2\), followed by reproducible samples for \(n=3,q=3\) and \(q=4\). The independent rank counts at \(n=3,q=2\) match (5) exactly and give \(86080\) ordered commuting pairs. `derive_n3.py`, requiring SymPy, independently performs the rational-canonical seventeen-stratum symbolic sum and asserts every coefficient identity in (5), their total, and (6). These tests are finite checks, not infinite proofs.

## Relationship to prior work

Britnell and Wildon (2010 preprint) establish commuting-class-type and matrix-centralizer facts for ordinary matrices. Bellamy and Boos (2016 preprint) classify \(\operatorname{GL}(V)\)-orbits in the enhanced *nilpotent* cone over the complex numbers. Fulman and Guralnick (2016 preprint; 2018 publication) enumerate commuting pairs in classical matrix Lie algebras, notably \(\mathfrak{gl}_n\), but not this affine semidirect Lie algebra. Fulman and Guralnick (2021 preprint) classify conjugacy classes of the *invertible affine group*, via group actions on \(V/(I-g)V\). Their Lemma 3.1 identifies the largest occupied Jordan-block size, a closely related orbit mechanism. In contrast, (1)–(6) count Lie-algebra adjoint ranks and commuting pairs with arbitrary, including singular, linear parts. The previous results motivate the proof and provide matrix similarity ingredients, but the inspected statements do not give (5) or (6).

## Limitations

The rank generating formula for arbitrary \(n\) is an exact finite similarity-class sum, not a single closed polynomial in \(q\) for unrestricted \(n\). The explicit factorization (5) is specialized to \(n=3\). Prior related orbit classifications may enable alternative derivations; no claim of exhaustive bibliographic priority is made. Group conjugacy, enhanced-nilpotent orbit size, and Lie centralizer dimension are distinct invariants. Independent mathematical verification is not claimed.

## References

1. J. R. Britnell and M. Wildon, *On types and classes of commuting matrices over finite fields*, arXiv:1001.0811v1 (public 2010-01-06); doi:10.1112/jlms/jdq088.
2. G. Bellamy and M. Boos, *The (cyclic) enhanced nilpotent cone via quiver representations*, arXiv:1609.04525v1 (public 2016-09-15).
3. J. Fulman and R. Guralnick, *Enumeration of Commuting Pairs in Lie Algebras over Finite Fields*, arXiv:1611.05499v1 (public 2016-11-16); doi:10.1007/s00026-018-0390-4.
4. J. Fulman and R. Guralnick, *Enumeration of conjugacy classes in affine groups*, arXiv:2112.15219v1 (public 2021-12-30); doi:10.2140/ant.2024.18.1189.
