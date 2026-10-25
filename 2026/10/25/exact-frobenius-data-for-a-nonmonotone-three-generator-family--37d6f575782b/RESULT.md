# Exact Frobenius data for a nonmonotone three-generator family

## Finding

For integers \(h\geq3\), \(d\geq1\), and \(a\geq(h-1)(h^2-h+1)\) with \(\gcd(a,d)=1\), consider the numerical semigroup
\[
S=\langle a,\ ha+d,\ h^2a+(h^2-h+1)d\rangle.
\]
Put \(B=h^2-h+1\), \(T=(h-1)^2\), and write \(a=qB+s\) with \(q\geq h-1\) and \(0\leq s<B\). Define
\[
R=a\bigl(h^2(q-1)+h(B-1)\bigr)+d(qB-1)-a,
\]
and, if \(s>0\), define
\[
U=a\bigl(h^2q+h(s-1)\bigr)+d(a-1)-a.
\]
The complete pseudo-Frobenius set and type are
\[
\operatorname{PF}(S)=
\begin{cases}
\{R\},&s=0,\\
\{R,U\},&1\leq s<B,
\end{cases}
\qquad
\operatorname{type}(S)=
\begin{cases}1,&s=0,\\2,&s>0.\end{cases}
\]
The two listed pseudo-Frobenius numbers are distinct when \(s>0\). In particular, \(S\) is symmetric exactly when \(B\mid a\), and its Frobenius number is
\[
F(S)=\begin{cases}R,&s=0,\\\max\{R,U\},&s>0.\end{cases}
\]
For \(s>0\), the phase transition is explicit:
\[
U-R=ds-ah(T-s).
\]
Thus \(U>R\) precisely when \(ds>ah(T-s)\), and otherwise \(R>U\). Equality cannot occur under the coprimality hypothesis. The genus is
\[
\boxed{\displaystyle
g(S)=\frac{Bh^2q(q-1)}2+\frac{qhB(B-1)}2
+sh^2q+\frac{hs(s-1)}2+\frac{(d-1)(a-1)}2.}
\]
Finally, the entire Apéry set of \(S\) with respect to its multiplicity \(a\) is explicit: for every integer \(0\leq r<a\), the unique Apéry element in residue class \(dr\pmod a\) is
\[
A_r=a\left(h^2\left\lfloor\frac rB\right\rfloor+h(r\bmod B)\right)+dr.
\]

## Assumptions and scope

The generators are positive, and \(\gcd(a,ha+d)=\gcd(a,d)=1\), so \(S\) is a numerical semigroup with multiplicity \(a\). The lower bound on \(a\) is a sufficient large-multiplicity condition used to control all representatives of each residue class; the theorem makes no claim for smaller \(a\). The offsets \(d\) are positive and need not be small relative to \(a\). All formulas quantify over the complete infinite range specified above, not over a finite computational cutoff.

## Proof

**1. Weighted change-making.** Every semigroup element has the form
\[
az+(ha+d)v+(h^2a+Bd)u
=a(z+hv+h^2u)+d(v+Bu),\qquad z,u,v\geq0.
\]
Fix \(M=v+Bu\geq0\). Among all decompositions into \(1\)-coins and \(B\)-coins, the least coefficient of \(a\) is obtained by maximizing \(u\):
\[
hv+h^2u=hM-h(B-h)u=hM-hTu.
\]
Since \(T>0\), the maximum \(u=\lfloor M/B\rfloor\) is optimal. Hence the minimum weighted cost is exactly
\[
W(M)=h^2\left\lfloor\frac MB\right\rfloor+h(M\bmod B).
\]
The nonnegative extra multiple \(az\) cannot improve this minimum.

**2. No residue wrap lowers the cost.** Coprimality implies that all nonnegative values of \(M\) producing the residue \(dr\pmod a\), for a fixed \(0\leq r<a\), are exactly \(M=r+\ell a\), \(\ell\geq0\). For any \(M\geq0\), let \(K=\lfloor(M+a)/B\rfloor-\lfloor M/B\rfloor\). If \(s=0\), then \(K=q\), and
\[
W(M+a)-W(M)=h(a-Tq)=h^2q>0.
\]
If \(s>0\), then \(K\leq q+1\), so
\[
W(M+a)-W(M)=h(a-TK)
\geq h(qh+s-T)\geq h(h-1)>0,
\]
where \(B-T=h\) and \(q\geq h-1\). Therefore
\[
aW(M+a)+d(M+a)>aW(M)+dM,
\]
and the smallest value in each residue class uses \(M=r\). This proves the displayed Apéry-set formula.

**3. Frobenius number and genus.** Write \(r=jB+v\) with \(0\leq v<B\). Within each complete block, \(A_r\) increases by \(ha+d\) as \(v\) increases by one. Its terminal value increases by \(ah^2+dB>0\) from one complete block to the next. Consequently, the largest Apéry element is either at \(r=qB-1\), or, if \(s>0\), at \(r=a-1\). These give \(R+a\) and \(U+a\), respectively. Their difference is \(ds-ah(T-s)\). The classical Apéry identity \(F(S)=\max_r A_r-a\) proves the Frobenius statements.

For the genus, the classical Apéry identity gives
\[
g(S)=\frac1a\sum_{r=0}^{a-1}A_r-\frac{a-1}{2}
=\sum_{r=0}^{a-1}W(r)+\frac{(d-1)(a-1)}2.
\]
There are \(q\) complete blocks of length \(B\) and one terminal block of length \(s\). Summing \(h^2j+hv\) over these blocks yields exactly the stated genus formula.

**4. All pseudo-Frobenius numbers.** Order the Apéry set by \(x\preceq_S y\) when \(y-x\in S\). For an index \(r=jB+v<a\) with \(v<B-1\) and \(r+1<a\), one has
\[
A_{r+1}-A_r=ha+d\in S.
\]
For an index with \(v=B-1\) and \(r+B<a\), one has
\[
A_{r+B}-A_r=h^2a+Bd\in S.
\]
Thus every Apéry element is below one of the two terminal candidates \(A_{qB-1}\) and \(A_{a-1}\); when \(s=0\) these coincide.

Suppose \(s>0\), and set \(D=U-R=ds-ah(T-s)\). Because the two indices have distinct residues modulo \(a\), \(D\ne0\). If \(D>0\), then \(D\equiv ds\pmod a\), but
\[
D=A_s-ahT<A_s,
\]
so \(D\notin S\). If \(D<0\), then \(-D\equiv d(a-s)\pmod a\), where \(a-s=qB\), and
\[
A_{qB}-(-D)=a\bigl(h^2q-h(T-s)+d\bigr)>0.
\]
The last inequality uses \(q\geq h-1\) and \(s\geq1\). Hence \(-D\notin S\). The two terminal elements are therefore incomparable, and both are maximal. By the standard Apéry characterization \(\operatorname{PF}(S)=\{w-a:w\text{ is maximal in }\operatorname{Ap}(S,a)\}\), the pseudo-Frobenius set has precisely the stated elements. A numerical semigroup is symmetric exactly when it has type one, completing the proof.

## Verification

Run `python3 verify.py` with Python's standard library. The verifier independently computes minimum semigroup representatives in all residue classes by Dijkstra's algorithm, without using the greedy construction to compute those minima. It then checks the complete claimed Apéry set, Frobenius number, genus, and pseudo-Frobenius set. It passed 2,407 parameter triples over \(3\leq h\leq12\), covering both residue regimes, coprime offsets of several sizes, and all formula branches. For selected smaller examples it also enumerates the gaps directly and reconstructs the pseudo-Frobenius set.

For instance, \((h,a,d)=(3,14,1)\) gives \(S=\langle14,43,133\rangle\), \(F(S)=377\), \(g(S)=189\), and \(\operatorname{PF}(S)=\{377\}\). The nearby case \((3,15,1)\) gives \(S=\langle15,46,142\rangle\), \(F(S)=403\), \(g(S)=207\), and \(\operatorname{PF}(S)=\{269,403\}\). These computations are consistency checks; the unrestricted theorem follows from the proof above.

## Relationship to prior work

Liu, Xin, Ye, and Yin first presented a combinatorial framework for Frobenius problems in June 2023. Their revised account discusses precisely the longer family with offsets \(h^i-h+1\) and observes that nonmonotonic greedy weights prevent their main monotonicity theorem from resolving its Frobenius problem. The present result treats the first genuinely nonbinary three-generator instance (two nonmultiplicity generators), retaining all positive coprime offsets and all sufficiently large multiplicities; it also determines the genus, complete pseudo-Frobenius set, and symmetry criterion.

The revised paper's general closed-form theorem for Collection GCNS requires weights \(H_i=ub_i+1\) with a single fixed \(u\). Matching its first nonmultiplicity generator forces \(u=h-1\), but the second would then differ from our coefficient \(h^2\) by \(h(h-1)(h-2)>0\) for \(h\geq3\). Hence that theorem does not contain the present triple family. Standard Apéry and three-generator methods supply background machinery but do not themselves state these closed formulas and their offset-dependent Frobenius phase transition. General symbolic algorithms may recover individual cases; this claim is about the complete uniform closed classification above.

## Limitations

Only three generators are treated, and the large-multiplicity bound is sufficient rather than asserted optimal. The results do not solve the corresponding higher-generator family or cases with negative offsets. Publication priority has not been established against every possible unindexed derivation or broader algorithmic specialization. Finite verification does not replace the unrestricted mathematical proof.

## References

1. F. Liu, G. Xin, S. Ye, J. Yin, *A Generalization of Mersenne and Thabit Numerical Semigroups*, arXiv:2306.03459v1 (first publicly posted 2023-06-06), https://arxiv.org/abs/2306.03459v1 .
2. F. Liu, G. Xin, S. Ye, J. Yin, *On the Frobenius Number and Genus of a Collection of Semigroups Generalizing Repunit Numerical Semigroups*, arXiv:2306.03459v4 (2025 revision), concluding remarks and Theorems 2.10–2.13, https://arxiv.org/html/2306.03459v4 .
3. A. Pascadi, *A Graphical Approach to Finding the Frobenius Number, Genus and Hilbert Series of a Numerical Semigroup*, arXiv:1712.02522 (2017), https://arxiv.org/abs/1712.02522 .
