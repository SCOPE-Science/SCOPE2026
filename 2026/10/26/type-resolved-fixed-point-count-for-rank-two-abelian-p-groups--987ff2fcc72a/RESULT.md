# Type-resolved fixed-point count for rank-two abelian p-groups

## Finding

Let \(p\) be any prime and let \(b\ge2\). Put \(A=C_p\oplus C_{p^b}\), and write
\[
A[p]=\{a\in A:pa=0\}\cong C_p^2.
\]
The number of automorphisms \(\varphi\in\operatorname{Aut}(A)\) whose fixed subgroup is exactly \(A[p]\) is
\[
E(p,b)=\begin{cases}
p^2-1,&b=2,\\
(p-1)p^{b-1},&b\ge3.
\end{cases}
\]
Equivalently, \(E(p,b)=(p-1)p^{b-1}+(p-1)\mathbf 1_{b=2}\). This is a count for a specified subgroup, not merely for the cardinality of the fixed-point set.

## Assumptions and scope

The group is the finite abelian group \(A=C_p\oplus C_{p^b}\), with \(p\) prime and \(b\ge2\). Choose generators \(x,y\) of orders \(p,p^b\), respectively. For an automorphism \(\varphi\), define \(\operatorname{Fix}(\varphi)=\{g\in A:\varphi(g)=g\}\). The claim counts exactly those automorphisms for which this subgroup equals the characteristic subgroup \(A[p]\). No assumption on the parity of \(p\) is needed.

## Proof

Every endomorphism of \(A\) has a unique parameterization
\[
\varphi(x)=a x+p^{b-1}c y,\qquad \varphi(y)=\beta x+d y,
\]
where \(a,c,\beta\in\mathbb F_p\) and \(d\in\mathbb Z/p^b\mathbb Z\). It is an automorphism precisely when \(a\ne0\) and \(d\not\equiv0\pmod p\): on \(A/pA\), its matrix is triangular with diagonal entries \(a\) and \(d\bmod p\).

If \(\operatorname{Fix}(\varphi)=A[p]\), then \(\varphi\) fixes both \(x\) and \(p^{b-1}y\). These equations force \(a=1\), \(c=0\), and \(d\equiv1\pmod p\), while \(\beta\in\mathbb F_p\) is unrestricted. Conversely, these conditions make every element of \(A[p]\) fixed. Put \(\delta=d-1\), so \(\delta\in p(\mathbb Z/p^b\mathbb Z)\).

For \(u\in\mathbb F_p\) and \(v\in\mathbb Z/p^b\mathbb Z\), the element \(ux+vy\) is fixed exactly when
\[
\beta(v\bmod p)=0,\qquad \delta v=0\text{ in }\mathbb Z/p^b\mathbb Z.
\]
There are always \(p\) choices of \(u\). Since \(A[p]\) is already contained in the fixed subgroup, equality with \(A[p]\) is equivalent to having exactly \(p\) admissible values of \(v\).

First suppose \(\delta\ne0\), and let \(r\in\{1,\ldots,b-1\}\) be its \(p\)-adic valuation. The kernel of multiplication by \(\delta\) on \(\mathbb Z/p^b\mathbb Z\) has \(p^r\) elements, all divisible by \(p^{b-r}\), hence by \(p\). Thus the condition involving \(\beta\) is automatic, and there are exactly \(p^r\) admissible values of \(v\). Exactly \(p\) occur if and only if \(r=1\). There are \(p^{b-1}-p^{b-2}=(p-1)p^{b-2}\) choices of \(\delta\) of valuation one and \(p\) choices of \(\beta\), giving \((p-1)p^{b-1}\) automorphisms.

Now suppose \(\delta=0\). If \(\beta=0\), all \(p^b\) values of \(v\) are fixed, so the fixed subgroup is too large. If \(\beta\ne0\), the first equation requires \(v\in p(\mathbb Z/p^b\mathbb Z)\), which has \(p^{b-1}\) elements. This number equals \(p\) exactly when \(b=2\), contributing \(p-1\) additional automorphisms in that case and none for \(b\ge3\). Adding the two disjoint cases proves the formula.

## Verification

The standalone checker `verify.py` enumerates all automorphisms in the parameterization and directly compares the fixed-point set with \(A[p]\). Exhaustive checks gave the following matches between enumeration and formula: \((p,b)=(2,2),(2,3),(2,4),(3,2),(3,3),(3,4),(5,2),(5,3)\), with counts \(3,4,8,8,18,54,24,100\), respectively. These finite checks are corroborative only; the proof above establishes the formula for every prime and every \(b\ge2\).

## Relationship to prior work

Camina and Collins studied finite groups admitting automorphisms with prescribed fixed points (1974). Senden's study of the Reidemeister spectrum of finite abelian groups determines which fixed-point cardinalities occur. The type-resolved count here asks a finer question: among automorphisms whose fixed subgroup has order \(p^2\), how many have that subgroup equal to the canonical elementary subgroup \(A[p]\cong C_p^2\)? The inspected statements in Senden's paper address attainable cardinalities rather than multiplicities by fixed-subgroup isomorphism type. The full text of the 1974 paper was not available in the inspected record, so its title alone is not used as evidence of noncoverage.

## Limitations

The result is restricted to \(C_p\oplus C_{p^b}\) with \(b\ge2\) and counts only automorphisms whose fixed subgroup is exactly \(A[p]\). It does not classify all automorphisms with \(p^2\) fixed points, nor fixed subgroups of other types or groups with more invariant factors.

## References

1. A. R. Camina and M. J. Collins, “Finite Groups Admitting Automorphisms with Prescribed Fixed Points,” *Proceedings of the London Mathematical Society* (3) 28 (1974), 45–66. DOI: 10.1112/plms/s3-28.1.45.
2. P. Senden, “The Reidemeister spectrum of finite abelian groups,” arXiv:2205.15740 (first posted 2022-05-31); *Proceedings of the Edinburgh Mathematical Society* 66 (2023), 940–959. DOI: 10.1017/S0013091523000500.
