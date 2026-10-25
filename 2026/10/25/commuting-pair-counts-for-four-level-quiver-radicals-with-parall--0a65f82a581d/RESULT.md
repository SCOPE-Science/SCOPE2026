# Commuting-pair counts for four-level quiver radicals with parallel outer arrows

## Finding

Fix positive integers \(a,c\) and a prime power \(q\). Consider the four-vertex quiver
\[
1\overset{a}{\longrightarrow}2\longrightarrow3\overset{c}{\longrightarrow}4,
\]
where the outer labels denote numbers of parallel arrows. Let \(P\) be the direct sum of one copy of each of the four indecomposable projective representations, and let \(J=\operatorname{rad}(\operatorname{End}_{\mathbb F_q Q}(P))\). Put
\[
R_{n,m}(r;q)=\prod_{j=0}^{r-1}\frac{(q^n-q^j)(q^m-q^j)}{q^r-q^j},\qquad 0\le r\le\min(n,m),
\]
with the empty product equal to \(1\). Thus \(R_{n,m}(r;q)\) is the exact number of rank-\(r\) matrices of shape \(n\times m\) over \(\mathbb F_q\). Define
\[
Z_{a,c}(q)=\sum_{r=0}^{\min(a,4)}R_{a,4}(r;q)q^{(4-r)c},
\]
and
\[
\begin{aligned}
T_{a,c}(q)={}&q^{2(a+c)}+(q^a-1)q^{2(a+c)-c}\\
&+(q^c-1)q^{2(a+c)-a}+(q^a-1)(q^c-1)q^{a+c+1}.
\end{aligned}
\]
The number of ordered pairs \((X,Y)\in J\times J\) with \(XY=YX\) is exactly
\[
\boxed{C_{a,c}(q)=q^{2ac}\bigl[Z_{a,c}(q)+(q^2-1)T_{a,c}(q)\bigr].}
\]
Since \(\dim_{\mathbb F_q}J=2a+2c+ac+1\), the algebra group \(1+J\) has exactly
\[
\boxed{k(1+J)=q^{-(2a+2c+ac+1)}C_{a,c}(q)}
\]
conjugacy classes. These are **uniform explicit formulas**, for arbitrary positive \(a,c\) and every finite field, not merely an assertion of polynomiality.

## Assumptions and scope

The quiver is finite, acyclic, and has the specified three consecutive arrow classes; there are no additional arrows. Each indecomposable projective occurs with multiplicity one in \(P\). The parameter \(q\) is any prime power, including powers of \(2\). No restriction on \(a,c\) beyond positive integrality is imposed. Radical means the Jacobson radical, and two elements commute if their products agree in the associative endomorphism algebra. Under reversal of multiplication, the radical may equivalently be identified with the positive-length path ideal of \(\mathbb F_q Q\); the condition \(XY=YX\) is unchanged by reversing multiplication.

The six coefficient spaces of \(J\) are the first-to-second paths \(U\) of dimension \(a\), the second-to-third arrows \(\mathbb F_q\), the third-to-fourth paths \(W\) of dimension \(c\), the first-to-third paths \(U\), the second-to-fourth paths \(W\), and the first-to-fourth paths \(U\otimes W\). There are no paths of length greater than \(3\). All statements count **ordered** pairs.

## Proof

We use the path-algebra presentation, reversing the multiplication of the endomorphism algebra if necessary. Let \(U=\mathbb F_q^a\), \(W=\mathbb F_q^c\). A radical element has unique coordinates
\[
X=(u,s,w,p,z,h)\in U\oplus\mathbb F_q\oplus W\oplus U\oplus W\oplus(U\otimes W).
\]
Write \(Y=(v,t,x,r,y,\ell)\) in the same six summands. Path concatenation shows that \([X,Y]=0\) is equivalent to the pair of length-two equations
\[
tu-sv=0,\qquad sx-tw=0,
\]
and one length-three equation
\[
u\otimes y-v\otimes z+p\otimes x-r\otimes w=0.
\]
(The signs reflect the order \(XY-YX\) and are immaterial in characteristic two.) The top-length coordinates \(h,\ell\) never enter any commutator: they contribute the free factor \(q^{2ac}\) to the pair count.

**Case \((s,t)=(0,0)\).** The length-two equations disappear. The length-three equation can be represented by the ordinary matrix product \(MN=0\), where
\[
M=[u\;\;-v\;\;p\;\;-r]\in M_{a,4}(\mathbb F_q),\qquad
N=\begin{bmatrix}y\\z\\x\\w\end{bmatrix}\in M_{4,c}(\mathbb F_q).
\]
For each \(M\) of rank \(r\), the columns of \(N\) must lie in its \((4-r)\)-dimensional nullspace. Hence exactly \(q^{(4-r)c}\) choices of \(N\) are possible. Summing over matrix ranks yields precisely \(Z_{a,c}(q)\). This argument is exhaustive for the zero-middle-arrow case.

**Case \((s,t)\ne(0,0)\).** There are exactly \(q^2-1\) such scalar pairs. The length-two equations uniquely force
\[
(u,v)=(su_0,tu_0),\qquad (w,x)=(sw_0,tw_0)
\]
for \(u_0\in U\), \(w_0\in W\). Put \(P_0=tp-sr\in U\) and \(Q_0=sy-tz\in W\). The remaining condition becomes
\[
P_0\otimes w_0+u_0\otimes Q_0=0.
\]
As \((p,r,z,y)\) varies, the linear map to \((P_0,Q_0)\in U\oplus W\) is surjective and its kernel has dimension \(a+c\). For fixed \((u_0,w_0)\), the map
\[
\Phi_{u_0,w_0}:U\oplus W\to U\otimes W,\qquad (P_0,Q_0)\mapsto P_0\otimes w_0+u_0\otimes Q_0
\]
has rank \(0\) if both vectors vanish, rank \(a\) if \(u_0=0,w_0\ne0\), rank \(c\) if \(u_0\ne0,w_0=0\), and rank \(a+c-1\) if both are nonzero. The last equality follows because \(U\otimes w_0\) and \(u_0\otimes W\) intersect in exactly the line spanned by \(u_0\otimes w_0\). Consequently the numbers of \((p,r,z,y)\) satisfying the equation are respectively
\[
q^{2(a+c)},\quad q^{2(a+c)-a},\quad q^{2(a+c)-c},\quad q^{a+c+1}.
\]
There are respectively \(1\), \(q^c-1\), \(q^a-1\), and \((q^a-1)(q^c-1)\) corresponding pairs \((u_0,w_0)\). Summation gives \(T_{a,c}(q)\) for every fixed nonzero \((s,t)\), and then \((q^2-1)T_{a,c}(q)\) over all nonzero middle-arrow pairs. Combining the two disjoint cases and the free top-length factor proves the stated formula for \(C_{a,c}(q)\).

Finally \(1+J\) is a finite group under multiplication since \(J\) is nilpotent. The elements \(1+X\) and \(1+Y\) commute if and only if \(XY=YX\). Burnside's class equation for commuting pairs therefore gives
\[
k(1+J)=\frac{|\{(X,Y)\in J\times J:XY=YX\}|}{|J|}=\frac{C_{a,c}(q)}{q^{2a+2c+ac+1}}.
\]
Every count is computed over vector spaces and linear maps, so all characteristics are covered.

## Verification

The accompanying `verify.py` is standalone Python using only the standard library. It computes the formula with integer arithmetic and independently enumerates every first radical element \(X\) for small prime fields; for each \(X\) it constructs the commutator map \(\operatorname{ad}_X:Y\mapsto XY-YX\) from path concatenation, takes its rank over the prime field, and adds \(q^{\dim J-\operatorname{rank}(\operatorname{ad}_X)}\). This direct centralizer computation does not implement either case of the proof.

The observed exact values \(C_{a,c}(q)\), checked by running the script, are \(1024\) at \((a,c,q)=(1,1,2)\), \(41553\) at \((1,1,3)\), \(30208\) at \((2,1,2)\) and \((1,2,2)\), and \(2375680\) at \((2,2,2)\). Dividing by \(|J|\) gives corresponding class counts \(16,57,59,59,290\). These finite checks are sanity checks only; the proof above establishes all parameters, including arbitrary prime-power fields.

## Relationship to prior work

Hennecart and Perry's quiver analogue of Higman's conjecture (2022), Conjecture 3.1, asks for polynomiality of the number of commuting pairs in the radical of the endomorphism algebra of a projective quiver representation. Their explicit formulas solve the subclass where no path has length exceeding two. The present family has a genuine length-three path whenever \(a,c\ge1\), and supplies a **uniform closed finite-rank formula** for this longer-path subclass.

Goodwin and Röhrle (first publicly posted in 2009) already establish polynomiality of the number of conjugacy classes of any unipotent radical of a general-linear parabolic subgroup with at most five flag steps. The group \(1+J\) here is the four-block unipotent radical of block sizes \((a,1,1,c)\); **its polynomiality is therefore already known** and is not asserted to be new. The result claimed here is the explicit arithmetic formula valid uniformly for all outer block sizes, obtained from only matrix ranks up to four. Pak and Soffer (2015) provide a general recursion for pattern groups and finite-dimensional computations; fixed-size evaluations are in principle available through that broader method, but the present parameter-uniform closed expression and its elementary compression are not the recursion itself.

An earlier study of square-zero elements in radicals of four-layer incidence algebras counts \(X\) satisfying \(X^2=0\); such a one-element rank-profile does not imply the two-element commuting-pair count \(XY=YX\) established here. Likewise, published Kronecker-quiver commuting-probability formulas concern different radicals with no length-three path. These implications were compared, not merely the terminology of the papers.

## Limitations

This proves an exact count only for the specified four-vertex, three-arrow-class family with multiplicity-one projective summands. It does not solve the arbitrary-quiver polynomiality problem or give an orbit-by-orbit classification of the group. The existing five-step parabolic theorem already guarantees polynomiality here, so the increment is **an explicit uniform count**, not a new polynomiality theorem. Prior work includes general pattern-group recurrence algorithms, and no claim is made that these cannot specialize to the present count. No independent audit or independent validation has been performed.

## References

1. L. Hennecart and N. Perry, *A Quiver Analogue of Higman's Conjecture*, arXiv:2208.07738v1, first posted 16 August 2022; §§3–5. https://arxiv.org/abs/2208.07738
2. S. M. Goodwin and G. Röhrle, *Counting conjugacy classes in the unipotent radical of parabolic subgroups of \(\mathrm{GL}_n(q)\)*, arXiv:0901.0667 (first posted 6 January 2009), Theorem 1.2 and §3. https://arxiv.org/abs/0901.0667
3. I. Pak and A. Soffer, *On Higman's \(k(U_n(q))\) conjecture*, arXiv:1507.00411 (first posted July 2015), §§3–6. https://arxiv.org/abs/1507.00411
