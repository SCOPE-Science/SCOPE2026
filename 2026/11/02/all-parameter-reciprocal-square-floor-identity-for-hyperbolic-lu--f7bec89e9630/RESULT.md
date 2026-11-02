# All-parameter reciprocal-square floor identity for hyperbolic Lucas sequences

## Finding
For all integers \(s\ge3\) and all positive integers \(r,n\), the generalized Fibonacci sequence
\[
U_0=0,\qquad U_1=1,\qquad U_{j+2}=sU_{j+1}-U_j\quad(j\ge0)
\]
satisfies
\[
\boxed{\left\lfloor\left(\sum_{k=n}^{\infty}\frac1{U_{rk}^{2}}\right)^{-1}\right\rfloor
=U_{rn}^{2}-U_{r(n-1)}^{2}-1.}
\]
More precisely, if \(S=\sum_{k=n}^{\infty}U_{rk}^{-2}\) and \(A=U_{rn}^{2}-U_{r(n-1)}^{2}\), then
\[
A-1<S^{-1}<A.
\]
This settles the hyperbolic integer-parameter range of the reciprocal-square clause in Conjecture 4.6 of Amdeberhan--Chen--Moll--Sagan, previously established by Park only when \(s\) was sufficiently large.

## Assumptions and scope
Here \(s\) ranges over every integer at least \(3\), and \(r,n\) independently range over all positive integers. There is no upper bound or parity condition. The recurrence uniquely defines integers \(U_j\) and \(U_j>0\) for \(j\ge1\). It grows exponentially, so the displayed series converges absolutely. \(A\) is a positive integer, including the boundary \(n=r=1\) where \(A=1\).

## Proof
Set
\[
C=s^2-4\ge5,\qquad \alpha=\frac{s+\sqrt C}{2}>2,\qquad z=\alpha^{-2r}\in(0,\tfrac14).
\]
Because the characteristic roots of the recurrence are \(\alpha,\alpha^{-1}\), Binet's formula is
\[
U_j=\frac{\alpha^j-\alpha^{-j}}{\sqrt C}.
\]
Consequently
\[
S=C\sum_{k=n}^{\infty}\frac{z^k}{(1-z^k)^2}
=Cz^n\sum_{j=0}^{\infty}\frac{z^j}{(1-z^{n+j})^2},
\]
and
\[
A=\frac{(1-z)z^{-n}(1-z^{2n-1})}{C}.
\]
Thus the exact product formula is
\[
AS=(1-z)(1-z^{2n-1})\sum_{j=0}^{\infty}
\frac{z^j}{(1-z^{n+j})^2}.
\]
**First strict bound.** For \(0<w<1\), the elementary series expansion gives \((1-w)^{-2}>1+2w\). Apply it to \(w=z^{n+j}\) in every term, then sum two geometric series:
\[
AS>(1-z^{2n-1})\left(1+\frac{2z^n}{1+z}\right).
\]
The expression on the right exceeds \(1\) precisely when
\[
2(1-z^{2n-1})>z^{n-1}(1+z).
\]
For \(n\ge1\) and \(0<z<1/4\), its left side is at least \(2(1-z)>3/2\), while its right side is at most \(1+z<5/4\). Therefore \(AS>1\), equivalently \(S^{-1}<A\).

**Second strict bound.** Since \(z^{n+j}\le z^n\), the geometric sum gives
\[
AS<\frac{1-z^{2n-1}}{(1-z^n)^2}<\frac1{(1-z^n)^2}.
\]
It follows, using \(0<z<1/4\), that
\[
0<AS-1<\frac{z^n(2-z^n)}{(1-z^n)^2}
<\frac{2z^n}{(1-z)^2}<\frac{32}{9}z^n.
\]
On the other hand, the first summand in \(S\) already gives \(S>Cz^n\ge5z^n\). Hence \(AS-1<S\), so \((A-1)S<1\), or equivalently \(A-1<S^{-1}\). Combining both strict inequalities and using the integrality of \(A\) proves the floor formula.

## Verification
A standalone exact-integer/rational certificate checker is supplied as `verify.py`. It checks \(256\) triples \((s,r,n)\) with \(3\le s\le10\), \(1\le r\le4\), \(1\le n\le8\). Each check encloses the infinite sum between two rational values using a rigorously bounded geometric tail, then verifies the strict floor inequalities by exact arithmetic. Re-run with `python3 verify.py`; expected output is `VERIFY_OK certified_cases=256 integer_parameters=3..10,1..4,1..8`. These checks are independent finite corroboration; the universal argument is the proof above.

## Relationship to prior work
Amdeberhan, Chen, Moll and Sagan explicitly proposed the reciprocal-square identity for their \(\{n\}_{s,-1}\) in Conjecture 4.6 (arXiv:1306.6511, first posted 27 June 2013). Park's Theorem 18 (arXiv:1407.8086) obtains this exact formula when \(s\) is sufficiently large, but does not eliminate that hypothesis. This theorem supplies an explicit parameter-free bound for every \(s\ge3\), every \(r\), and every \(n\). Yuan, He and Zhou (2014, DOI 10.1155/2014/402540) investigate reciprocals of the same minus-sign recurrence with exponent \(3\); their stated principal problem is distinct from the present reciprocal-square identity. published-finding corpus comparisons to cubic, fourth-power and fifth-power reciprocal sequence tails did not establish this claim; the actual claim-level comparisons are documented in the associated review. The possibility of an unlocated stronger theorem remains a literature risk, not a proof of originality.

## Limitations
The parameter range is \(s\ge3\), not all formal integer specializations in the original conjecture. At \(s=2\), \(U_j=j\), and for \(r=1,n=2\) the proposed right-hand side is \(2\) while the actual floor is \(1\). The result concerns reciprocal **squares** and the unit-determinant recurrence \(U_{j+2}=sU_{j+1}-U_j\), not general companion determinant \(t\) or other reciprocal powers. The finite checker does not prove the infinite-parameter statement. No independent mathematical audit is claimed.

## References
1. T. Amdeberhan, X. Chen, V. H. Moll and B. E. Sagan, *Generalized Fibonacci polynomials and Fibonomial coefficients*, arXiv:1306.6511v1 (27 June 2013), Conjecture 4.6; https://arxiv.org/html/1306.6511v2 .
2. S. Park, *Arithmetic properties of generalized Fibonacci sequences*, arXiv:1407.8086v1 (30 July 2014), Theorem 18 and its proof; https://ar5iv.labs.arxiv.org/html/1407.8086 .
3. P. Yuan, Z. He and J. Zhou, *On the Sum of Reciprocal Generalized Fibonacci Numbers*, Abstract and Applied Analysis (2014), DOI 10.1155/2014/402540, Theorem 1 (reciprocal cubes); https://onlinelibrary.wiley.com/doi/10.1155/2014/402540 .
