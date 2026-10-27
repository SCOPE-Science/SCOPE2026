# Exact monotone catenary degree of three consecutive triangular numbers

## Finding

Put \(T_j=j(j+1)/2\) and, for every integer \(n\ge 3\), let
\[
S_n=\langle T_n,T_{n+1},T_{n+2}\rangle.
\]
The **monotone catenary degree** of this numerical semigroup is exactly
\[
\boxed{\mathsf c_{\mathrm{mon}}(S_n)=2n+3.}
\]
The value is attained by a pair of distinct *equal-length* factorizations. The upper bound is constructive: all factorizations of the same semigroup element can be joined by a chain of nondecreasing factorization lengths, with every link of factorization distance at most \(2n+3\).

## Assumptions and scope

A factorization of \(m\in S_n\) is a vector \(z=(z_1,z_2,z_3)\in\mathbb N_0^3\) satisfying \(z_1T_n+z_2T_{n+1}+z_3T_{n+2}=m\). Its length is \(|z|=z_1+z_2+z_3\). For two factorizations define their coordinatewise minimum \(h_i=\min(z_i,z'_i)\) and the usual factorization distance
\[
d(z,z')=\max\{|z-h|,|z'-h|\}.
\]
A monotone \(N\)-chain between \(z,z'\) is a chain within their common fiber with every distance at most \(N\) and with lengths monotone from the initial to final length (nondecreasing when \(|z|\le|z'|\), nonincreasing otherwise). The invariant \(\mathsf c_{\mathrm{mon}}(S_n)\) is the least uniform \(N\) working for every fiber and every pair. The generators above form a minimal generating set for \(n\ge3\), as also established in the cited 2017 source. The definition does not identify ordinary and monotone catenary degrees.

## Proof

**1. A primitive equal-length obstruction.** Write \(A=T_n\), \(B=T_{n+1}\), \(C=T_{n+2}\). Then \(B-A=n+1\), \(C-B=n+2\), and \(C-A=2n+3\). If the difference \(d\) of two factorizations has total length zero, its two linear constraints give
\[
(n+1)d_2+(2n+3)d_3=0,\qquad d_1+d_2+d_3=0.
\]
Because \(\gcd(n+1,2n+3)=1\), all such differences are integer multiples of the primitive vector
\[
w=(n+2,-(2n+3),n+1).
\]
Its positive and negative parts,
\[
w_+=(n+2,0,n+1),\qquad w_-=(0,2n+3,0),
\]
are factorizations of the same semigroup element, and each has length \(L=2n+3\). The only nonnegative integer points in this fiber **at that length** are these two: every other candidate differs from \(w_+\) by an integer multiple of \(w\), while any multiple outside the two endpoints produces a negative coordinate. Therefore any monotone chain between these equal-length endpoints must stay at length \(L\) and pass directly between them. The distance of the endpoints is \(L\), yielding \(\mathsf c_{\mathrm{mon}}(S_n)\ge L\).

**2. The even-index relation lattice.** Suppose \(n=2t\) with \(t\ge2\), and put \(g=2t+1\). The generators are
\[
(A,B,C)=(tg,(t+1)g,(t+1)(2t+3)).
\]
The vectors
\[
r=(t+1,-t,0),\qquad s=(0,2t+3,-g)
\]
preserve weighted value, and change length by \(1\) and \(2\), respectively. They span the **entire integer relation lattice**: given any weighted-zero difference \(d\), reduction modulo \(g\) forces \(g\mid d_3\) because \(\gcd(g,C)=1\); subtracting the corresponding multiple of \(s\) leaves a relation of \(t\) and \(t+1\), which is an integer multiple of \(r\).

Let \(x,y\) be factorizations with \(|x|\le|y|\), and write \(y-x=pr+qs\). Necessarily \(p+2q\ge0\). We express this difference in one of the following forms, all with nonnegative coefficients:

- If \(p,q\ge0\), use \(q s\) followed by \(p r\).
- If \(p\ge0>q\), write \(k=-q\) and use \((p-2k)r+k(2r-s)\); the length condition ensures \(p\ge2k\).
- If \(p<0\le q\), write \(a=-p\le2q\). When \(a\le q\), use \(a(s-r)+(q-a)s\); otherwise use \((2q-a)(s-r)+(a-q)(s-2r)\).

Every elementary vector in these expressions changes length by \(0\), \(1\), or \(2\). Except in the first case they all have coordinate signs conformal to the net displacement \(y-x\), so all intermediate triples remain nonnegative, in any order. In the first case, applying \(s\) first consumes only third coordinates and adds second coordinates; the final nonnegativity of \(y\) guarantees both the \(s\)-stage and the following \(r\)-stage are possible. The distances of the moves \(r,s,s-r,s-2r\), and their negatives, are bounded by
\[
\max\{t+1,2t+3,3t+3,4t+3\}=4t+3=2n+3.
\]
Thus the claimed monotone chain exists for even \(n\).

**3. The odd-index relation lattice.** Suppose \(n=2t+1\) with \(t\ge1\), and put \(g=2t+3\). Then
\[
(A,B,C)=((t+1)(2t+1),(t+1)g,(t+2)g).
\]
Define the value-preserving relation vectors
\[
r=(g,-(2t+1),0),\qquad s=(0,t+2,-(t+1)).
\]
They change factorization length by \(2\) and \(1\). Since \(\gcd(g,A)=1\) and \(\gcd(t+1,t+2)=1\), the same modular argument shows they span the entire integer relation lattice. For factorizations \(|x|\le|y|\) write \(y-x=pr+qs\) with \(2p+q\ge0\). Again the following nonnegative decompositions apply:

- If \(p,q\ge0\), use \(q s\) followed by \(p r\).
- If \(p\ge0>q\), put \(k=-q\le2p\). For \(k\le p\) use \((p-k)r+k(r-s)\); for \(p<k\le2p\) use \((2p-k)(r-s)+(k-p)(r-2s)\).
- If \(p<0\le q\), put \(k=-p\) and use \((q-2k)s+k(2s-r)\).

The nonnegative-intermediate-point argument is identical: in the first case apply \(s\) before \(r\), and in the remaining cases every elementary vector has signs conformal to \(y-x\). Every move has nonnegative length change and distance bounded by
\[
\max\{2t+3,t+2,3t+3,4t+5\}=4t+5=2n+3.
\]
The chain exists also for odd \(n\). Reversing an increasing chain handles the reversed order of endpoints. Together with Step 1 this proves the formula for every \(n\ge3\).

## Verification

Run `python3 verify.py` with Python 3 and no third-party libraries. The checker reconstructs the two parity-dependent relation bases, confirms their weighted and length identities, verifies the two-point equal-length obstruction, and independently enumerates short fibers to check that every pair is connected by the constructive monotone chain. The packaged finite run tested all parameters \(3\le n\le15\), 185 fibers with multiple factorizations, and 2,923 factorization pairs. The infinite conclusion depends on the algebraic argument above, not on this finite enumeration.

## Relationship to prior work

Robles-Pérez and Rosales (2017), Propositions 24–25, prove freeness and give two **undirected** defining relations for precisely these triangular-number semigroups. Those relations are used here and are not claimed new. The present theorem concerns a different invariant: chains must obey *monotone factorization length*, so an undirected presentation alone does not prove the upper bound. The new upper-bound argument adds directed composite moves, explicitly including a length-preserving move with the sharp distance \(2n+3\). García-Sánchez, Ojeda and Sánchez-R.-Navarro (2012/2013) give general computational frameworks for equal/homogeneous catenary invariants, but do not state this parameter-uniform monotone classification. Süer and Sezgin (2020/2021) study catenary degrees of particular low-multiplicity telescopic families, not this monotone classification. Chomicz (2026) computes ordinary catenary degrees for **four** consecutive triangular generators, a different family and invariant.

## Limitations

The theorem is restricted to the additive monoids generated by **three** consecutive triangular numbers beginning with \(n\ge3\). It does not provide corresponding monotone catenary degrees for four or more consecutive generators or general polynomial sequences. The proof explicitly uses both the triangular consecutive-gap coprimality and the two-relation presentation; extending either structural property requires new work. Publication priority beyond the inspected literature and indexed records has not been independently established.

## References

1. A. M. Robles-Pérez and J. C. Rosales, *The Frobenius number for sequences of triangular and tetrahedral numbers*, arXiv:1706.04378 (first posted 2017-06-14), especially Propositions 24–25.
2. P. A. García-Sánchez, I. Ojeda and A. Sánchez-R.-Navarro, *Factorization invariants in half-factorial affine semigroups*, arXiv:1207.5838 (2012), Int. J. Algebra Comput. 23 (2013), 111–122.
3. M. Süer and M. Ş. Sezgin, *Betti elements and catenary degree of telescopic numerical semigroup families*, arXiv:2011.09548 (2020), Algebra Lett. (2021), article 3.
4. K. Chomicz, *On numerical semigroups with embedding dimension four*, arXiv:2604.25653 (2026), Section 5.
