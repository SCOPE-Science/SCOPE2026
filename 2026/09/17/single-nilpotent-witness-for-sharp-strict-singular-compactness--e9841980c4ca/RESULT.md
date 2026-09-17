# A single nilpotent strictly singular operator witnesses the sharp compactness exponent

## Summary

Laustsen and Wirzenius determined the exact nilpotency index of the quotient algebra of strictly singular operators modulo compact operators on finite direct sums of Baernstein spaces, p-convexified Schreier spaces, and classical \(\ell_p\)-spaces. Their sharpness statement is formulated using a product of several *different* strictly singular operators.

The same index is in fact witnessed by powers of one operator. More precisely, except for the degenerate case in which the quotient is zero, there is a strictly singular operator \(T\) whose nilpotency index as an actual bounded operator equals the nilpotency index of the quotient algebra, and whose last nonzero power is non-compact. Thus the sharp uniform power-compactness exponent is attained by one operator, in the strongest possible form \(T^{k+1}=0\) and \(T^k\notin\mathcal K(X)\).

The mechanism is a finite weighted-shift construction along the ordered chain of formal inclusions used by Laustsen--Wirzenius, together with the absorption isomorphisms \(B_p\oplus\ell_p\cong B_p\) and \(S_p\oplus c_0\cong S_p\). This upgrade is not a formal consequence of the nilpotency index of an arbitrary noncommutative algebra.

## Setting

Let \(L\subset(1,\infty)\) and \(M,N\subset[1,\infty)\) be finite and not all empty, and set
\[
X=\Big(\bigoplus_{p\in L}B_p\Big)\oplus
  \Big(\bigoplus_{q\in M}\ell_q\Big)\oplus
  \Big(\bigoplus_{r\in N}S_r\Big).
\]
Following Laustsen--Wirzenius, define
\[
k=\begin{cases}
|L|+|L\cup M|-1,&N=\varnothing,\\
|L|+|L\cup M|+|N|,&N\ne\varnothing.
\end{cases}
\]
Write \(\mathcal S(X)\) and \(\mathcal K(X)\) for the strictly singular and compact operators on \(X\), respectively.

Their Theorem 1.1 states that every product of \(k+1\) members of \(\mathcal S(X)\) is compact, while some product of \(k\) members is non-compact. Hence \(\mathcal S(X)/\mathcal K(X)\) has nilpotency index \(k+1\).

## Theorem: one-operator attainment of the index

Assume \(k\ge1\). Then there exists \(T\in\mathcal S(X)\) such that
\[
T^{k+1}=0
\qquad\text{and}\qquad
T^k\notin\mathcal K(X).
\]
Consequently, \(k+1\) is the least integer \(m\) such that \(A^m\) is compact for every \(A\in\mathcal S(X)\), and this least uniform power-compactness exponent is attained by a single algebraically nilpotent strictly singular operator.

### Proof

Laustsen--Wirzenius introduce the finite family
\[
\Sigma=\begin{cases}
\{B_p:p\in L\}\cup\{\ell_q:q\in L\cup M\},&N=\varnothing,\\
\{B_p:p\in L\}\cup\{\ell_q:q\in L\cup M\}\cup\{S_r:r\in N\}\cup\{c_0\},&N\ne\varnothing.
\end{cases}
\]
It has cardinality \(k+1\). Their linear order on these model spaces allows an enumeration
\[
Y_1\prec Y_2\prec\cdots\prec Y_{k+1}
\]
such that each formal inclusion
\[
R_j=R_{Y_j,Y_{j+1}}:Y_j\to Y_{j+1},\qquad 1\le j\le k,
\]
is strictly singular. Moreover,
\[
R_kR_{k-1}\cdots R_1=R_{Y_1,Y_{k+1}}
\]
is non-compact: it sends the normalized unit-vector basis of \(Y_1\) to the normalized unit-vector basis of \(Y_{k+1}\).

Set
\[
Z=Y_1\oplus\cdots\oplus Y_{k+1}.
\]
We claim that \(Z\cong X\). If \(N=\varnothing\), then \(Z\) differs from \(X\) only by the extra copies of \(\ell_p\) with \(p\in L\setminus M\). For every \(p\in L\), Laustsen--Wirzenius record
\[
B_p\oplus\ell_p\cong B_p,
\]
so these extra summands are absorbed. If \(N\ne\varnothing\), the same \(\ell_p\)-absorption applies, and the additional \(c_0\) summand is absorbed by any Schreier summand because
\[
S_r\oplus c_0\cong S_r.
\]
Thus \(Z\cong X\) in both cases.

Define an operator \(S\in\mathcal B(Z)\) by the finite shift
\[
S(y_1,\ldots,y_{k+1})
=(0,R_1y_1,R_2y_2,\ldots,R_ky_k).
\]
Every matrix entry of \(S\) is either zero or one of the strictly singular maps \(R_j\). For a finite direct sum, membership in an operator ideal is equivalent to membership of every matrix entry in that ideal. Hence \(S\in\mathcal S(Z)\).

The shift has length \(k+1\), so
\[
S^{k+1}=0.
\]
On the other hand, if \(J_1:Y_1\to Z\) is the first-coordinate embedding and \(Q_{k+1}:Z\to Y_{k+1}\) the last-coordinate projection, then
\[
Q_{k+1}S^kJ_1=R_k\cdots R_1,
\]
which is non-compact. Therefore \(S^k\) is non-compact.

Choose an isomorphism \(U:Z\to X\) and put
\[
T=USU^{-1}.
\]
Strict singularity and compactness are invariant under composition with isomorphisms, so \(T\in\mathcal S(X)\), \(T^{k+1}=0\), and \(T^k\) is non-compact. This proves the theorem. \(\square\)

## Why the strengthening is not formal from quotient nilpotency

For a noncommutative algebra, knowing that some product of \(k\) elements is nonzero does not in general imply that some \(k\)-th power is nonzero. Already over \(\mathbb R\) or \(\mathbb C\), let \(A\) have basis \(a,b,c\) and multiplication
\[
ab=c,\qquad ba=-c,
\]
with every other product of basis elements equal to zero. Then \(A^2\ne0\) and \(A^3=0\), so the algebra has nilpotency index three, but \(x^2=0\) for every \(x\in A\). Thus the one-operator witness above uses the ordered formal-inclusion chain and absorption structure of these Banach spaces; it is not an automatic algebraic restatement of Laustsen--Wirzenius's theorem.

## Immediate special cases

1. For every \(1<p<\infty\), the Baernstein space \(B_p\) admits a non-compact strictly singular operator \(T\) with \(T^2=0\).

2. For every \(1\le p<\infty\), the p-convexified Schreier space \(S_p\) admits a non-compact strictly singular operator \(T\) with \(T^2=0\).

3. If \(X=\bigoplus_{j=1}^m B_{p_j}\) with distinct \(1<p_1<\cdots<p_m<\infty\), there is \(T\in\mathcal S(X)\) with
\[
T^{2m}=0,\qquad T^{2m-1}\notin\mathcal K(X).
\]

4. If \(X=\bigoplus_{j=1}^m S_{p_j}\) with distinct \(1\le p_1<\cdots<p_m<\infty\), there is \(T\in\mathcal S(X)\) with
\[
T^{m+1}=0,\qquad T^m\notin\mathcal K(X).
\]

The only case of the displayed general theorem with \(k=0\) is \(X=\ell_p\) for a single \(p\), where every strictly singular operator is already compact and the quotient algebra is zero.

## Variant including \(c_0\)

The same construction also sharpens the \(c_0\)-variant in Remark 1.2(iv) of Laustsen--Wirzenius. If \(N=\varnothing\) and
\[
Y=X\oplus c_0,
\qquad h=|L|+|L\cup M|,
\]
then there exists \(T\in\mathcal S(Y)\) with
\[
T^{h+1}=0,\qquad T^h\notin\mathcal K(Y).
\]
Indeed, use the ordered family
\[
\{B_p:p\in L\}\cup\{\ell_q:q\in L\cup M\}\cup\{c_0\}
\]
and the same shift construction. If \(N\ne\varnothing\), then \(X\oplus c_0\cong X\), so the main theorem already applies without changing the exponent.

## Relation to previous work

The 2026 paper of Laustsen--Wirzenius provides all space-specific ingredients used above: the exact product nilpotency index, the linear order of model spaces, the strictly singular formal inclusions, non-compactness of their full composite, the finite-matrix ideal criterion, and the absorption isomorphisms. It does not state a single-operator power witness, and text searches of the accessible manuscript found no discussion of “power-compact” operators or an equivalent single-operator formulation.

Laustsen--Smith proved that every product of two strictly singular operators on each individual \(B_p\) or \(S_p\) is compact, and earlier established many non-compact strictly singular operators on these spaces. Their available statements do not give the square-zero non-compact witnesses above.

Flores--Hernández--Semenov--Tradacete studied compactness of powers of strictly singular operators on Banach lattices and used shift-like constructions in other spaces to produce strictly singular operators with non-compact powers. Thus the finite-shift idea itself is established prior art. The contribution here is the sharp realization of the Laustsen--Wirzenius index by one algebraically nilpotent operator, enabled by their particular formal-inclusion chain and absorption identities.

## References

1. N. J. Laustsen and H. Wirzenius, “Compactness of compositions of strictly singular operators on direct sums of Baernstein, Schreier and \(\ell_p\)-spaces,” *Proceedings of the American Mathematical Society* 154 (2026), 2345–2356. DOI: 10.1090/proc/17594. arXiv:2509.02405.
2. N. J. Laustsen and J. Smith, “Strictly singular operators on the Baernstein and Schreier spaces,” *Quarterly Journal of Mathematics* 77 (2026), 511–527. DOI: 10.1093/qmath/haag014. arXiv:2509.08796.
3. N. J. Laustsen and J. Smith, “Closed ideals of operators on the Baernstein and Schreier spaces,” *Journal of Mathematical Analysis and Applications* 546 (2025), 129235. DOI: 10.1016/j.jmaa.2025.129235. arXiv:2410.12666.
4. J. Flores, F. L. Hernández, E. M. Semenov and P. Tradacete, “Strictly singular and power-compact operators on Banach lattices,” *Israel Journal of Mathematics* 188 (2012), 323–352. DOI: 10.1007/s11856-011-0152-z.

## Reproducibility notes

The proof is symbolic and requires no numerical computation. To reproduce it, verify the following items in Reference 1: Theorem 1.1; Remark 1.2(iii)–(iv); the matrix ideal criterion (equation (3.2)); Lemma 3.7; and the proof of Theorem 1.1(ii), especially the family \(\Sigma\) in equation (3.6) and the non-compact composite of its formal inclusions. Then form the one-superdiagonal operator matrix displayed above and compute its powers.
