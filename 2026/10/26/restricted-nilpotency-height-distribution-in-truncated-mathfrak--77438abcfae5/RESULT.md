# Restricted nilpotency-height distribution in truncated \(\mathfrak{sl}_2\) currents

## Finding
Let \(q=p^e\) be any odd prime power, and let \(m\geq1\). Equip \(L_m=\mathfrak{sl}_2(\mathbb F_q[t]/(t^m))\) with its restricted Lie algebra structure induced by matrix powers. For integers \(k\geq0\), define
\[
Z_{m,k}=\#\{X\in L_m:X^{[p]^k}=0\},\qquad X^{[p]^0}=X.
\]
Thus \(Z_{m,0}=1\). For \(k\geq1\), put \(P=p^k\), \(c=\lceil m/P\rceil\) and, for each integer \(0\leq v<c\), put
\[
h_v=\left\lceil\frac{2(m-Pv)}{P-1}\right\rceil.
\]
Then the exact, nonrecursive enumeration is
\[
\boxed{Z_{m,k}=q^{3(m-c)}+(q^2-1)\sum_{v=0}^{c-1}q^{3(m-v)-2-h_v}.}
\]
The nilpotent locus has exactly \(q^{3m-1}\) elements. If the restricted nilpotency height of a nonzero nilpotent \(X\) is the least \(k\geq1\) with \(X^{[p]^k}=0\), then the number of elements of height \(k\) is precisely \(Z_{m,k}-Z_{m,k-1}\). The greatest attainable height is
\[
\boxed{\left\lceil\log_p(2m+1)\right\rceil.}
\]
For fixed \(p\) and \(q=p^e\), as \(m\to\infty\), the height \(H_m\) of a uniformly chosen nonzero nilpotent satisfies
\[
\boxed{H_m/\log_p m\ \xrightarrow{\mathbb P}\ 1.}
\]
These statements describe the restricted power map, not the nilpotency class of the Lie algebra and not the ordinary Jordan nilpotency index of an adjoint operator.

## Assumptions and scope
All fields have odd characteristic \(p\); \(q\) may be any power of \(p\). The coefficient ring is the truncated equal-characteristic local ring \(R_m=\mathbb F_q[t]/(t^m)\). Its \(t\)-adic valuation is truncated at \(m\), with \(\operatorname{val}_t(0)=m\) when applied to an element of \(R_m\). No assumption of algebraic closure or primality of \(q\) is made. A matrix in \(L_m\) is uniquely written
\[
X=\begin{pmatrix}c&a\\b&-c\end{pmatrix},\qquad a,b,c\in R_m.
\]
The restricted power \(X^{[p]}\) is the matrix \(X^p\); it again has trace zero in odd characteristic. The count includes the zero element (height zero); the probability limit conditions on nonzero nilpotents.

## Proof
**Power identity.** Put \(Q(a,b,c)=c^2+ab\). The identity \(X^2=Q(a,b,c)I_2\) holds over the commutative ring \(R_m\). Because \(p\) is odd, for every \(k\geq1\),
\[
X^{[p]^k}=X^{p^k}=Q(a,b,c)^{(p^k-1)/2}X.
\]
The exponent is an integer; this identity fixes all characteristic and normalization conventions.

**Primitive valuation and smooth quadratic counting.** Every nonzero \(X\) has a unique integer \(0\leq v<m\) such that its three coordinates are all divisible by \(t^v\), with at least one having valuation exactly \(v\). It is uniquely \(X=t^vY\), where \(Y\) is a primitive triple over \(R_r\), \(r=m-v\). There are \(q^{3r}-q^{3(r-1)}\) such triples. For every integer \(1\leq h\leq r\), the number of primitive \(Y\in R_r^3\) satisfying \(Q(Y)\equiv0\pmod{t^h}\) is
\[
\boxed{(q^2-1)q^{3r-h-2}.}
\]
To prove this, over \(\mathbb F_q\) the equation \(c^2+ab=0\) has \(q^2\) solutions: for \(a\ne0\), there is one \(b\) for each \((a,c)\), and for \(a=0\) one has \(c=0\) and arbitrary \(b\). All but the origin are primitive, giving \(q^2-1\) initial solutions. At a nonzero solution its gradient \((b,a,2c)\) is nonzero, since \(p\ne2\). Each lift of a solution modulo \(t^j\) to a solution modulo \(t^{j+1}\) therefore has exactly \(q^2\) choices for its three new coefficients. All unrestricted coefficients after precision \(h\) contribute \(q^{3(r-h)}\), giving \((q^2-1)q^{2(h-1)+3(r-h)}\), as claimed.

**Exact power-height count.** Fix \(k\geq1\), write \(P=p^k\), and fix the above \(v\). If \(Pv\geq m\), then \(X^P=0\) regardless of \(Y\). These elements, together with zero, are exactly \(t^c L_m\), where \(c=\lceil m/P\rceil\), giving \(q^{3(m-c)}\) elements. If \(Pv<m\), then the power identity and the fact that \(Y\) has a unit coordinate show
\[
X^P=0\quad\Longleftrightarrow\quad Q(Y)^{(P-1)/2}\equiv0\pmod{t^{m-Pv}}
\quad\Longleftrightarrow\quad\operatorname{val}_t Q(Y)\geq h_v.
\]
Here \(1\leq h_v\leq m-v=r\); in the zero case the inequality is interpreted at the precision \(r\). Applying the primitive-lifting count and summing over \(0\leq v<c\) proves the displayed formula for \(Z_{m,k}\).

**Total nilpotent count and maximal height.** Reduction modulo \(t\) is a map \(L_m\to\mathfrak{sl}_2(\mathbb F_q)\) with fibers of size \(q^{3(m-1)}\). By the power identity, an element is eventually killed by a \(p\)-power exactly when its reduced quadratic value is zero. The latter is a quadric with \(q^2\) points, so the nilpotent count is \(q^{3m-1}\). For \(P\geq2m+1\), any nilpotent primitive triple has \(Q(Y)\in tR_r\) and is killed; nonprimitive triples are killed since \(Pv\geq m\). Conversely, for \(m\geq2\), take \(c=0,a=1,b=t\); then \(Q=t\) has valuation one and \(X^{P}\ne0\) whenever \((P-1)/2<m\). For \(m=1\), nonzero nilpotents are already killed by the first \(p\)-power, agreeing with the asserted formula.

**Asymptotic law.** The maximal-height bound gives \(H_m\leq\lceil\log_p(2m+1)\rceil\), hence the upper tail. Fix \(0<\epsilon<1\) and let \(k=\lfloor(1-\epsilon)\log_p m\rfloor\), \(P=p^k\) and \(c=\lceil m/P\rceil\). Then \(c\to\infty\). Dividing the exact enumeration by \(q^{3m-1}\) yields
\[
\frac{Z_{m,k}}{q^{3m-1}}=q^{1-3c}+(q^2-1)\sum_{v=0}^{c-1}q^{-3v-1-h_v}.
\]
For \(v<c/2\), \(h_v\geq c-2\); the partial sum is at most a constant (depending on \(q\)) times \(q^{-c}\). For \(v\geq c/2\), ignore \(h_v\geq1\) and bound the remaining geometric tail by a constant times \(q^{-3c/2}\). Consequently the displayed fraction tends to zero. Replacing the denominator by the nonzero nilpotent count \(q^{3m-1}-1\) does not change this conclusion. Thus \(\Pr(H_m\leq(1-\epsilon)\log_p m)\to0\), completing convergence in probability.

## Verification
A standalone `verify.py` enumerates all trace-zero matrices directly over the indicated small prime-field truncations and computes repeated matrix powers by polynomial-matrix multiplication, without using the displayed quadratic-power identity. Its exhaustive test cases are \((p,m)=(3,1),(3,2),(3,3),(5,1),(5,2),(7,1)\). In each, the exact counts for \(k=0,1,2,3,4,5\) agree with the formula. For example, in characteristic three at truncation length three, the height histogram is: height zero \(1\), height one \(1376\), height two \(5184\), and nonnilpotent \(13122\); the sum is \(3^9=19683\). The executable terminates with `VERIFY_OK`.

## Relationship to prior work
Chaffe and Topley, *Modular representations of truncated current Lie algebras* (arXiv:2311.08208, first posted 2023-11-14), Proposition 3.4 identifies the eventual restricted-nilpotent locus by the degree-zero coefficient, and §3.3 studies index and regular elements. The present statement is a quantitative refinement: it counts every successive kernel of the iterated restricted power map and derives its maximal and typical height. Those numerical distributions do not follow from an identification of the final nilpotent set alone. The smooth-lifting argument for the quadratic cone is standard and is not asserted to be new.

Zordan, *Adjoint orbits of matrix groups over finite quotients of compact discrete valuation rings and representation zeta functions* (arXiv:1608.05725), concerns adjoint orbit lifting and shadows over mixed-characteristic number-field rings, with applications to representation zeta functions. Its general orbit methodology is relevant background but its theorems do not explicitly give these equal-characteristic restricted-power-height counts. Distinct notions of nilpotency (iterated restricted powers, ordinary associative powers, and adjoint nilpotence) are not conflated.

## Limitations
The theorem is restricted to odd characteristic and split \(\mathfrak{sl}_2\) over equal-characteristic truncated polynomial rings; characteristic two and higher rank are not addressed. The finite computations are corroboration, not a substitute for the proof. Existing more general orbit or nilpotent-jet techniques may permit a rederivation of the counts; a comprehensive priority claim is not made.

## References
1. Matthew Chaffe and Lewis Topley, *Modular representations of truncated current Lie algebras*, arXiv:2311.08208v1 (2023-11-14), https://arxiv.org/html/2311.08208v2. Relevant original text: §2 and Propositions 3.3–3.5.
2. Michele Zordan, *Adjoint orbits of matrix groups over finite quotients of compact discrete valuation rings and representation zeta functions*, arXiv:1608.05725 (2016-08-19), https://arxiv.org/html/1608.05725v3. Relevant original text: Introduction, Theorems A–C, and §3.
