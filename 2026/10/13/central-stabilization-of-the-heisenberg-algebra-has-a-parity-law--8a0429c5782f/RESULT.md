# Central stabilization of the Heisenberg algebra has a parity law for subalgebra commutativity
## Finding
Let \(q\) be a prime power and let \(r\ge 0\). Define the finite-dimensional Lie algebra
\[
L_r(q)=\mathfrak h_3(\mathbb F_q)\oplus \mathbb F_q^r
\]
with basis \(x,y,z,c_1,\ldots,c_r\), bracket \([x,y]=z\), and all remaining basis brackets zero. For a finite Lie algebra \(L\), write \(\operatorname{sd}(L)\) for the proportion of ordered pairs of Lie subalgebras \((A,B)\) such that \(A+B\) is again a Lie subalgebra.

Write \(\genfrac{[}{]}{0pt}{}{n}{j}_q\) for the Gaussian binomial coefficient and define
\[
G_n(q)=\sum_{j=0}^{n}\genfrac{[}{]}{0pt}{}{n}{j}_q,
\qquad
A_n(q)=\sum_{j=0}^{n}\genfrac{[}{]}{0pt}{}{n}{j}_q q^j,
\]
\[
B_r(q)=\sum_{j=0}^{r}\genfrac{[}{]}{0pt}{}{r}{j}_q q^{2j},
\qquad
N_r(q)=G_{r+1}(q)+(q+1)A_{r+1}(q)+B_r(q),
\]
and
\[
J_r(q)=\sum_{h=0}^{r}q^{-h}\genfrac{[}{]}{0pt}{}{r}{h}_q
\sum_{a=0}^{r-h}\genfrac{[}{]}{0pt}{}{r-h}{a}_q
\sum_{b=0}^{r-h-a}q^{ab}\genfrac{[}{]}{0pt}{}{r-h-a}{b}_q.
\]
Then \(N_r(q)\) is exactly the number of Lie subalgebras of \(L_r(q)\), and
\[
\boxed{
\operatorname{sd}(L_r(q))
=1-\frac{q^{2r+3}(q+1)J_r(q)}{N_r(q)^2}.
}
\]
For fixed \(r\), the large-field limit has a parity law:
\[
\boxed{
\lim_{q\to\infty}\operatorname{sd}(L_r(q))=
\begin{cases}
0,&r\text{ even},\\[2mm]
\frac14,&r\text{ odd}.
\end{cases}}
\]
Thus successive central stabilizations do not approach a single asymptotic regime: the limiting subalgebra commutativity degree alternates forever between \(0\) and \(1/4\).

## Assumptions and scope
The result holds over every finite field \(\mathbb F_q\), including characteristic \(2\), and for every integer \(r\ge0\). The direct summand \(\mathbb F_q^r\) is central and abelian. The result concerns the subalgebra commutativity degree, not the elementwise commuting probability.

The case \(r=0\) is the three-dimensional Heisenberg algebra and specializes to the published formula
\[
\operatorname{sd}(L_0(q))=
\frac{3q^3+12q^2+16q+16}{(q^2+2q+4)^2}.
\]
The case \(r=1\) specializes to the previously recorded one-dimensional central stabilization formula
\[
\operatorname{sd}(L_1(q))=
1-\frac{q^4(q+1)(3q+1)}{(2q^3+4q^2+3q+5)^2}.
\]
The new content is the uniform formula for arbitrary \(r\) together with the parity asymptotic.

## Proof
Put \(Z=Z(L_r(q))=\langle z,c_1,\ldots,c_r\rangle\) and \(V=L_r(q)/Z\). Then \(\dim Z=r+1\), \(V\cong\mathbb F_q^2\), and the bracket on \(V\) is a nonzero alternating form with values in \(\mathbb F_q z\).

Every Lie subalgebra \(A\) is determined by three data: \(P=\pi(A)\le V\), \(C=A\cap Z\), and a linear graph map \(P\to Z/C\). If \(\dim P\le1\), the closure condition is automatic. If \(P=V\), closure is equivalent to \(z\in C\). Hence the number of subalgebras with \(\dim P=0,1,2\), respectively, is
\[
G_{r+1}(q),\qquad (q+1)A_{r+1}(q),\qquad B_r(q),
\]
which proves the formula for \(N_r(q)\).

Now consider two subalgebras \(A,B\). They can fail to permute only when \(\pi(A)\) and \(\pi(B)\) are distinct one-dimensional subspaces of \(V\). Indeed, if one projection is zero then the cross bracket vanishes; if one projection is all of \(V\), that subalgebra contains \(z\); and if the two projections are the same line then the cross bracket again vanishes. For two distinct lines, \([A,B]=\mathbb F_q z\), and their independence in \(V\) gives
\[
(A+B)\cap Z=(A\cap Z)+(B\cap Z).
\]
Therefore \(A+B\) fails to be a subalgebra exactly when
\[
z\notin C+D,
\qquad C=A\cap Z,\quad D=B\cap Z.
\]

Choose a complement \(Z=\mathbb F_q z\oplus W\) with \(W\cong\mathbb F_q^r\). If \(z\notin C\), then \(C\) is the graph of a linear functional on a subspace \(U\le W\); similarly \(D\) is the graph of a functional on \(T\le W\). The condition \(z\notin C+D\) is exactly that the two functionals agree on \(U\cap T\). If \(h=\dim(U\cap T)\), the number of agreeing pairs of functionals is \(q^{\dim U+\dim T-h}\). Multiplying by the graph-map weights attached to the two one-dimensional quotient projections leaves the uniform factor \(q^{2r+2-h}\). Thus the weighted number of central pairs is
\[
q^{2r+2}\sum_{U,T\le W}q^{-\dim(U\cap T)}=q^{2r+2}J_r(q).
\]
There are \(q(q+1)\) ordered pairs of distinct lines in \(V\), so the number of nonpermuting ordered subalgebra pairs is
\[
q^{2r+3}(q+1)J_r(q).
\]
Dividing by \(N_r(q)^2\) proves the exact formula.

It remains to justify the displayed finite sum for \(J_r(q)\). For fixed \(H=U\cap T\) of dimension \(h\), put \(a=\dim(U/H)\) and \(b=\dim(T/H)\). After choosing \(H\), choose \(U/H\), then choose a \(b\)-space disjoint from it. The latter choice contributes the standard factor
\[
q^{ab}\genfrac{[}{]}{0pt}{}{r-h-a}{b}_q.
\]
Summing over \(h,a,b\) yields the stated expression.

For the limit, the dominant term of \(N_r(q)\) comes from \((q+1)A_{r+1}(q)\). If \(r=2m\), its unique top-degree summand occurs at \(j=m+1\) and has leading coefficient \(1\). If \(r=2m+1\), the two top-degree summands occur at \(j=m+1,m+2\) and give leading coefficient \(2\). For \(J_r(q)\), when \(r=2m\) the unique leading dimension pair is \((m,m)\), with generic intersection zero and leading coefficient \(1\). When \(r=2m+1\), the leading pairs \((m,m)\), \((m,m+1)\), and \((m+1,m)\) have generic intersection zero and contribute leading coefficient \(3\); the pair \((m+1,m+1)\) has unavoidable positive intersection and is lowered by the factor \(q^{-\dim(U\cap T)}\). Comparing the leading terms of the numerator and denominator gives nonpermuting proportions \(1\) and \(3/4\), respectively, proving the parity limit.

## Verification
The standalone checker `artifacts/check_formula.py` independently enumerates all vector subspaces in reduced row-echelon form for small prime fields, tests Lie-subalgebra closure directly from the bracket, and tests whether each ordered pair has subalgebra sum. It then compares the brute-force counts against the closed formula.

The recorded checks are
\[
(q,r)=(2,0),(3,0),(2,1),(3,1),(2,2),
\]
with exact agreement in every case. The largest listed case has \(198\) subalgebras and \(31{,}620\) permuting ordered pairs. The checker also verifies the known \(r=0\) and \(r=1\) specializations symbolically and terminates with `CHECK_OK`.

These finite computations are regression checks only. The theorem for arbitrary prime powers and arbitrary \(r\) is established by the symbolic counting proof above.

## Relationship to prior work
Muhie, Otera, and Russo introduced and computed the subalgebra commutativity degree for the three-dimensional Heisenberg algebra over finite fields; their formula is exactly the \(r=0\) specialization above. Their full preprint was inspected, including the definition, the Heisenberg theorem, and its proof, and searches for central direct sums did not reveal the arbitrary-\(r\) stabilization considered here.

A subsequently published comparison record gives the exact \(r=1\) central-stabilization formula. The present formula recovers that result but is not inferred from it: the proof counts arbitrary central dimension and exposes the new parity law. Published formulas for higher-rank Heisenberg algebras \(H_m(\mathbb F_q)\) concern a different family: those algebras have one-dimensional center and a nondegenerate symplectic quotient of dimension \(2m\), whereas \(L_r(q)\) has center dimension \(r+1\) and a fixed two-dimensional quotient.

## Limitations
No claim is made that the displayed Gaussian sum is the shortest possible closed form. The result is specific to a central abelian stabilization of \(\mathfrak h_3\); it does not classify subalgebra commutativity degrees of general two-step nilpotent Lie algebras.

There is a residual originality risk from the group-theoretic side: for odd prime characteristic, Lazard correspondence relates this Lie family to a Heisenberg \(p\)-group times an elementary abelian central factor, so an older subgroup-commutativity calculation for that direct-product group could imply a prime-field specialization. Targeted searches for that alias did not locate a formula covering the arbitrary-\(r\) statement, and such a group result would in any case need comparison with the all-prime-power Lie formulation.

## References
1. S. K. Muhie, D. E. Otera, and F. G. Russo, *On the number of modular pairs in finite dimensional Lie algebras on finite fields*, arXiv:2609.19086v1, first public 2026-09-16. Primary MSC includes 17B05.
2. *Exact subalgebra commutativity degree after a one-dimensional central stabilization of the Heisenberg algebra*, published comparison record dated 2026-10-04.
3. *Exact subalgebra commutativity degree of finite Heisenberg Lie algebras*, published comparison record dated 2026-09-18.
