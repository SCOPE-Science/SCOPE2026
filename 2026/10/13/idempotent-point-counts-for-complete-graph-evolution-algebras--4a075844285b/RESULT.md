# Idempotent-point counts for complete-graph evolution algebras

## Finding

For every integer \(n\ge3\) and odd prime power \(q=p^f\), consider the evolution algebra \(E(K_n)\) of the complete loopless graph on \(n\) vertices, with natural basis \(e_1,\dots,e_n\) and multiplication
\[
e_ie_j=0\quad(i\ne j),\qquad
 e_i^2=\sum_{j\ne i}e_j.
\]
We count **individual idempotent elements** \(x\) with \(x^2=x\), not evolution algebras satisfying \(E^2=E\). Write \(N_{n,q}\) for their number.

For \(k=1,\ldots,n-1\), put
\[
\delta_k=1-4k(n-k),
\qquad
c_0=\begin{cases}1,&p\mid n-1,\\2,&p\nmid n-1.\end{cases}
\]
Define the nonconstant two-value root count
\[
r_k=\begin{cases}
1+\chi_q(\delta_k)-\mathbf1_{p\mid n+1},&p\nmid n-1,\\
\mathbf1_{p\nmid(2k-1)},&p\mid n-1,
\end{cases}
\]
where the quadratic character \(\chi_q\) takes values \(1,0,-1\) on nonzero squares, zero, and nonsquares, respectively; \(\mathbf1\) denotes the indicator. All arithmetic in these indicator conditions uses ordinary integers reduced modulo \(p\).

Then the exact formula is
\[
\boxed{N_{n,q}=c_0+\frac12\sum_{k=1}^{n-1}\binom nk r_k.}
\]
Every nonconstant idempotent has exactly two distinct coordinate values. Moreover **every geometric idempotent is defined over the quadratic extension \(\mathbf F_{p^2}\) of the prime field**, including when \(p\mid n-1\).

Consequently, for \(m\ge1\), the idempotent variety over \(\mathbf F_{q^m}\) has exactly
\[
\#\operatorname{Idem}(E(K_n))(\mathbf F_{q^m})
=\begin{cases}N_{n,q},&m\text{ odd},\\N_{n,q^2},&m\text{ even},\end{cases}
\]
and the point-counting zeta function is
\[
\boxed{
Z(T)=(1-T)^{-N_{n,q}}
(1-T^2)^{-(N_{n,q^2}-N_{n,q})/2}.
}
\]
The latter exponent is an integer because the extra geometric points occur in pairs interchanged by Frobenius.

## Assumptions and scope

The source's Example 3.1 uses the adjacency matrix of \(K_n\), a matrix with zero diagonal and one in every off-diagonal position. The source primarily studies **automorphisms** of this algebra, and calls an algebra “idempotent” when its square equals itself. We instead study **idempotent elements**; these are fixed points of the quadratic evolution map.

All odd characteristics are admitted. When \(p\mid n-1\), the adjacency matrix is singular and the algebra no longer satisfies \(E^2=E\), but the same defining multiplication and idempotent problem still make sense. The theorem explicitly includes this singular case.

The primary MSC for the finding is \(17A36\), in the algebra category of automorphisms, derivations, and other operators of nonassociative algebras. The first public preprint for the exact example appeared on 2 February 2022. This classification concerns individual elements and is not a classification of all evolution algebras up to isomorphism.

## Proof

Write
\[
x=\sum_{i=1}^n x_i e_i,\qquad S=\sum_{i=1}^n x_i^2.
\]
The multiplication table gives
\[
x^2=\sum_{i=1}^n\left(S-x_i^2\right)e_i.
\]
Thus \(x^2=x\) is equivalent to
\[
\boxed{x_i^2+x_i=S\quad\text{for all }i.}
\]
Every coordinate is a root of the same quadratic polynomial \(X^2+X-S\); hence an idempotent has either one or two distinct coordinate values, over any extension field. A constant coordinate value \(a\) satisfies
\[
a=(n-1)a^2.
\]
It gives \(c_0\) solutions: zero always, plus \(a=1/(n-1)\) exactly when \(p\nmid n-1\).

For a nonconstant solution, choose the subset \(I\) of indices with value \(u\), of cardinality \(k\) with \(1\le k\le n-1\); the remaining \(n-k\) coordinates have value \(v\). The two distinct roots of \(X^2+X-S\) satisfy
\[
u+v=-1,\qquad v=-1-u.
\]
Substituting the \(k\) copies of \(u\) and \(n-k\) copies of \(v\) into \(u^2+u=S\) gives
\[
\boxed{(n-1)u^2+(2(n-k)-1)u+(n-k)=0.}\tag{1}
\]
Conversely any \(u\) satisfying (1), with \(u\ne -1/2\), gives an idempotent with exactly the indicated two values: subtracting the two fixed-point equations reduces to the identity \(u+v=-1\). The excluded value \(u=-1/2\) is precisely the coincident-root case.

If \(p\nmid n-1\), (1) is quadratic with discriminant
\[
(2(n-k)-1)^2-4(n-1)(n-k)
=1-4k(n-k)=\delta_k.
\]
It has \(1+\chi_q(\delta_k)\) roots. Its value at \(u=-1/2\) is \((n+1)/4\), which vanishes for every \(k\) exactly when \(p\mid n+1\). Removing that one constant-coordinate root gives the stated \(r_k\).

If \(p\mid n-1\), equation (1) becomes
\[
(1-2k)u+(1-k)=0.
\]
When \(2k-1\not\equiv0\pmod p\), there is one root. If \(2k-1\equiv0\pmod p\), then \(1-k\equiv1/2\not\equiv0\pmod p\), so there are no roots. Moreover \(u=-1/2\) never solves (1) in this case, since \(p\) is odd and \(p\mid n-1\) implies \(p\nmid n+1\). This proves the second formula for \(r_k\).

There are \(\binom nk\) labeled subsets \(I\), each admitting \(r_k\) choices of \(u\). Each nonconstant idempotent is represented **twice** in this construction: once with its \(u\)-positions marked and once with its distinct \(v\)-positions marked. Together with the constant solutions, this proves
\[
N_{n,q}=c_0+\frac12\sum_{k=1}^{n-1}\binom nk r_k.
\]

Each \(u\) satisfies a polynomial of degree at most two whose coefficients lie in the prime field \(\mathbf F_p\). Therefore every coordinate of every geometric idempotent belongs to \(\mathbf F_{p^2}\), including the linear case. For \(q=p^f\), Frobenius on the geometric idempotent set consequently has order dividing two. Its fixed points over \(\mathbf F_{q^m}\) depend only on the parity of \(m\). If \(N_1=N_{n,q}\), \(N_2=N_{n,q^2}\), the exponential definition yields
\[
\begin{aligned}
Z(T)&=\exp\left(\sum_{m\ge1}\frac{\#\operatorname{Idem}(E(K_n))(\mathbf F_{q^m})}{m}T^m\right)\\
&=(1-T)^{-N_1}(1-T^2)^{-(N_2-N_1)/2}.
\end{aligned}
\]
This proves the zeta formula.

## Verification

The included `artifacts/verify.py` implements equation (1) and the closed count formula. Independently, it exhaustively checks all coordinate vectors directly against the defining multiplication over prime fields for
\[
q\in\{3,5,7,11\},
\]
with dimensions through nine for \(q=3\), through six for \(q=5\), and through five for \(q=7,11\).

It also uses an explicit quadratic field \(\mathbf F_9=\mathbf F_3[t]/(t^2+1)\) to test the nontrivial square-class transition. For \(n=3\), the exact counts are
\[
N_{3,3}=2,\qquad N_{3,9}=8,
\]
so the associated zeta function is
\[
Z(T)=(1-T)^{-2}(1-T^2)^{-3}.
\]
The checker returns `VERIFY_OK`; its output is included as `artifacts/verify_output.txt`. Finite computations are replay evidence only; the all-dimensions proof is the quadratic reduction above.

## Relationship to prior work

Sriwongsa–Zou, arXiv:2202.01333, Example 3.1, defines \(E(K_n)\) exactly as above and determines its automorphism group under nonsingularity hypotheses. Their meaning of “idempotent evolution algebra” is \(E^2=E\), not an element \(x^2=x\). The formulas here concern individual idempotents, include the singular characteristic boundary, and give finite-field and extension-field point counts, so the automorphism theorem does not imply them.

Elduque–Labra, arXiv:1902.02191, treats graph evolution algebras, automorphism schemes, and derivations. Its general graph-to-algebra construction underlies the example but does not give the idempotent-point enumeration or its quadratic-extension splitting property.

García-Martínez–Pérez-Rodríguez, *A note on complete evolution algebras*, discusses the general polynomial system for idempotents and establishes existence results for complex regular evolution algebras. Its “complete” concerns extendibility of subalgebra bases, not complete graphs. The general idempotent equations there do not specialize to or enumerate the fixed points on \(E(K_n)\).

Searches for complete-graph fixed points, idempotent counts, the discriminant fingerprints, and extension-field zeta functions did not yield the present exact classification.

## Limitations

The formulas are for odd characteristic and \(n\ge3\); characteristic two is not classified. Counts are for labeled idempotent **elements**, not orbits under algebra automorphisms or isomorphism classes of algebras.

The zeta function counts geometric solutions as rational points of the **reduced underlying point set**. It makes no claim that the original idempotent scheme is reduced or smooth in exceptional characteristics.

Equivalent finite-field counts might exist under quadratic dynamical systems or genetics terminology not recovered in these searches. Search absence is not a proof of global historical novelty.

## References

1. S. Sriwongsa and Y. M. Zou, “On Automorphism Groups of Idempotent Evolution Algebras,” arXiv:2202.01333v1 (2 February 2022), *Linear Algebra and its Applications* 641 (2022), DOI `10.1016/j.laa.2022.02.010`.
2. A. Elduque and A. Labra, “Evolution algebras, automorphisms, and graphs,” arXiv:1902.02191v1 (6 February 2019), *Linear and Multilinear Algebra* 69 (2021), 331–342, DOI `10.1080/03081087.2019.1598931`.
3. X. García-Martínez and A. Pérez-Rodríguez, “A note on complete evolution algebras,” *Archiv der Mathematik* 126 (2026), 597–604, DOI `10.1007/s00013-026-02251-0`.
