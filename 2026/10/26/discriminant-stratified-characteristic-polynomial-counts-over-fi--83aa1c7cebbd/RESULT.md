# Discriminant-stratified characteristic-polynomial counts over finite chain rings

## Finding

Let \(R\) be a finite commutative chain ring of length \(m\geq 1\), with maximal ideal \(\pi R\) and residue field \(\kappa=R/\pi R\) of odd order \(q\). For \(t,\delta\in R\), let

\[
N_R(t,\delta)=\#\{A\in M_2(R):\operatorname{tr}(A)=t,\ \det(A)=\delta\}.
\]

Write \(\Delta=t^2-4\delta\), and let \(\nu(a)=s\) when \(a\in\pi^sR\setminus\pi^{s+1}R\), with \(\nu(0)=m\). Define

\[
H(s)=\begin{cases}
(s+1)(q-1)q^{m-1},&0\leq s<m,\
q^{m-1}\bigl(m(q-1)+q\bigr),&s=m.
\end{cases}
\]

Then the exact count is

\[
\boxed{N_R(t,\delta)=\sum_{x\in R}H\bigl(\nu(\Delta-x^2)\bigr).}
\]

Consequently the characteristic-polynomial fiber depends on \((t,\delta)\) only through the discriminant \(\Delta\). More explicitly, if \(v=\nu(\Delta)\), then the following valuation-shell formulas evaluate the count without enumerating the ring elements.

* If \(v=m\), then
\[
N_R(t,\delta)=H(m)+\sum_{r=0}^{m-1}(q-1)q^{m-r-1}H\bigl(\min(2r,m)\bigr).
\]
* If \(v=2h+1<m\), then
\[
N_R(t,\delta)=\sum_{r=0}^{h}(q-1)q^{m-r-1}H(2r)+q^{m-h-1}H(v).
\]
* If \(v=2h<m\), write \(\Delta=\pi^{2h}d\) with \(d\) a unit and put \(\ell=m-2h\). If the residue \(\bar d\in\kappa^\times\) is a nonsquare, then
\[
N_R(t,\delta)=\sum_{r=0}^{h-1}(q-1)q^{m-r-1}H(2r)+q^{m-h}H(v).
\]
If \(\bar d\) is a square, then
\[
\begin{aligned}
N_R(t,\delta)={}&\sum_{r=0}^{h-1}(q-1)q^{m-r-1}H(2r)\
&+(q-2)q^{m-h-1}H(v)\
&+\sum_{j=1}^{\ell-1}2(q-1)q^{m-h-j-1}H(v+j)+2q^hH(m).
\end{aligned}
\]
Empty sums are zero. The square/nonsquare alternative is needed only when \(v<m\) is even.

## Assumptions and scope

The coefficient ring is any finite commutative chain ring with odd residue-field cardinality. Its length is the nilpotency index of a generator \(\pi\) of its maximal ideal. The odd-residue assumption makes \(2\) and \(4\) units, so completing the square is valid. The result counts all matrices, not similarity classes, and fixes both coefficients of the characteristic polynomial \(T^2-tT+\delta\). No assertion is made in residue characteristic two, for arbitrary finite rings that are not chain rings, or for matrices of size greater than two.

## Proof

For each \(u\in R\), the number of ordered pairs \((b,c)\in R^2\) with \(bc=u\) depends only on \(s=\nu(u)\). If \(s<m\), then for each \(i=0,\ldots,s\), there are \((q-1)q^{m-i-1}\) choices of \(b\) of valuation \(i\); each such multiplication map has a kernel of size \(q^i\), and hence exactly \(q^i\) solutions \(c\) to \(bc=u\). Each valuation shell contributes \((q-1)q^{m-1}\), giving \(H(s)=(s+1)(q-1)q^{m-1}\). For \(u=0\), each nonzero valuation shell contributes the same amount and \(b=0\) contributes \(q^m\), giving \(H(m)=q^{m-1}(m(q-1)+q)\).

Write a matrix with trace \(t\) as \(\begin{pmatrix}a&b\c&t-a\end{pmatrix}\). Its determinant condition is \(bc=a(t-a)-\delta\). Since \(2\) is a unit, the substitution \(x=2a-t\) is a bijection of \(R\), and

\[
4\bigl(a(t-a)-\delta\bigr)=\Delta-x^2.
\]

Multiplication by the unit \(4\) preserves valuation. Summing the pair count \(H\) over \(a\), equivalently over \(x\), proves the boxed formula.

For the explicit cases, count \(x\) by valuation. When \(v=m\), one has \(\nu(\Delta-x^2)=\min(2\nu(x),m)\). When \(v=2h+1<m\), no valuation of \(x^2\) equals \(v\), so the difference has valuation \(2r\) for \(\nu(x)=r\leq h\), and valuation \(v\) for all \(x\in\pi^{h+1}R\). When \(v=2h<m\), only the shell \(\nu(x)=h\) can have cancellation. Write \(x=\pi^h u\); then the extra valuation is that of \(d-u^2\) up to \(\ell=m-2h\). Because \(2u\) is a unit at a unit root, each simple square root modulo \(\pi\) lifts uniquely through every higher quotient. If \(\bar d\) is nonsquare, there are no such roots. If it is square, there are two roots; the numbers of unit \(u\) with extra valuation \(0\), \(j\in\{1,\ldots,\ell-1\}\), and at least \(\ell\) are respectively \((q-3)q^{m-h-1}\), \(2(q-1)q^{m-h-j-1}\), and \(2q^h\). Adding the shell \(x\in\pi^{h+1}R\), of size \(q^{m-h-1}\), yields the displayed square case. This exhausts every valuation of \(\Delta\).

## Verification

The accompanying `verify.py` enumerates every \(2\times2\) matrix over \(\mathbb Z/p^m\mathbb Z\) for \((p,m)=(3,2),(5,2),(3,3)\), tallies all trace/determinant fibers, and compares them with both the sum formula and the explicit valuation cases. All \(81\), \(625\), and \(729\) fibers pass; the total matrix counts are respectively \(6561\), \(390625\), and \(531441\). These finite tests corroborate the formula in three prime-power rings only; the proof above supplies the general chain-ring argument.

## Relationship to prior work

Reiner's classical paper counts matrices with a prescribed characteristic polynomial over finite fields. Prasad, Singla, and Spallone classify similarity classes and centralizers over local principal ideal rings of length two, which supplies a detailed length-two comparison but not the all-length valuation formula stated here. Choosuwan, Jitman, and Udomkavanich count matrices with a fixed determinant over finite chain rings; that is a one-coefficient marginal count rather than the joint trace-and-determinant fiber. Stasinski proves existence of commutator representations for trace-zero matrices over principal ideal rings, an existence statement rather than a characteristic-polynomial count. The present result gives an explicit discriminant-stratified count for every chain length with odd residue field, in both equal and mixed characteristic.

## Limitations

The formula deliberately excludes residue characteristic two, where completing the square and the simple-root argument need different treatment. The computational checks cover only \(\mathbb Z/p^m\mathbb Z\); equal and mixed characteristic chain rings are handled by the proof, not by enumeration. No generalization to \(n\times n\) matrices is claimed.

## References

1. A. Stasinski, “Similarity and commutators of matrices over principal ideal rings,” arXiv:1211.6872v1 (submitted 2012-11-29); DOI 10.1090/TRAN/6402.
2. A. Prasad, P. Singla, and S. Spallone, “Similarity of matrices over local rings of length two,” arXiv:1212.6157v1 (submitted 2012-12-26); Indiana University Mathematics Journal 64 (2015), 471–514.
3. P. Choosuwan, S. Jitman, and P. Udomkavanich, “Determinants of Matrices over Commutative Finite Principal Ideal Rings,” arXiv:1605.06826v1 (submitted 2016-05-22).
4. I. Reiner, “On the number of matrices with given characteristic polynomial,” Illinois Journal of Mathematics 5 (1961), 324–329; DOI 10.1215/ijm/1255629830.
