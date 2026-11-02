# Four-pole zero-product census for diamond-poset incidence algebras

## Finding

Let \(P_m\), \(m\geq 0\), be the ordinal sum of a singleton, an antichain of \(m\) points, and a singleton. Thus for \(m\geq 1\) its strict comparisons are \(0<i<\infty\) for each \(i\in\{1,\ldots,m\}\), together with \(0<\infty\). Let \(A_m(k)=I(P_m,k)\) be the associative incidence algebra. For every finite field \(k=\mathbb F_q\), including fields of characteristic two, define the ordered one-sided zero-product count
\[
Z_m(q)=\#\{(a,b)\in A_m(\mathbb F_q)^2:ab=0\}.
\]
Then
\[
\begin{aligned}
Z_m(q)={}&q^3\left(q^{3m}(3q-2)^m+(q-1)q^{3m}(2q-1)^m\right)\\
&+2q^2(q-1)\left[q^2(q^2+q-1)\right]^m
+q(q-1)^2\left[q^2(2q-1)\right]^m.
\end{aligned}
\]

Set \(B_1=q^3(3q-2)\), \(B_2=q^3(2q-1)\), \(B_3=q^2(q^2+q-1)\), and \(B_4=q^2(2q-1)\). The generating function is exactly
\[
\sum_{m\geq0} Z_m(q)t^m=
\frac{q^3}{1-B_1t}+
\frac{q^3(q-1)}{1-B_2t}+
\frac{2q^2(q-1)}{1-B_3t}+
\frac{q(q-1)^2}{1-B_4t}.
\]
For every integer \(q\geq2\), the four bases are positive and pairwise distinct; consequently the count sequence has a **minimal order-four constant-coefficient linear recurrence** with characteristic polynomial
\[
(T-B_1)(T-B_2)(T-B_3)(T-B_4).
\]
In particular \(Z_m(q)\sim q^3 B_1^m\) as \(m\to\infty\), for each fixed finite field order \(q\).

## Assumptions and scope

The poset has \(m+2\) vertices and exactly \(3m+3\) intervals, counting singletons; hence \(\dim_k A_m(k)=3m+3\). For \(m=0\) the middle antichain is empty and the definition means the two-point chain. For \(m=1\) it is the three-point chain, so \(A_1(k)\) is the full upper-triangular \(3\times3\) algebra. For \(m\geq2\), the corresponding matrix algebra is supported on the diagonal, first row, and last column. The formula counts **ordered** pairs with \(ab=0\), not unordered pairs, commuting pairs, or pairs satisfying both \(ab=ba=0\). All scalar coefficients are in an arbitrary finite field; the argument does not require odd characteristic.

## Proof

Order the vertices as \(0,1,\ldots,m,\infty\). Write diagonal entries of the first factor as \(a_0,a_i,a_\infty\) and of the second as \(b_0,b_i,b_\infty\). For the off-diagonal coordinates use \(x_i=a_{0i}\), \(y_i=a_{i\infty}\), \(z=a_{0\infty}\), and \(u_i=b_{0i}\), \(v_i=b_{i\infty}\), \(w=b_{0\infty}\). From the interval-basis convolution multiplication, the equation \(ab=0\) is **equivalent** to
\[
\begin{gathered}
a_0b_0=0,\quad a_ib_i=0\ (1\leq i\leq m),\quad a_\infty b_\infty=0,\\
a_0u_i+x_ib_i=0,\qquad a_iv_i+y_ib_\infty=0\quad (1\leq i\leq m),\\
a_0w+zb_\infty+\sum_{i=1}^m x_iv_i=0.
\end{gathered}
\]
There are no other possible nonzero matrix positions; in particular the final summand is the contribution of each composable length-two path \(0<i<\infty\). This term is the coupling absent from two-level star incidence algebras.

Fix the two endpoint coordinates \(a_0\) and \(b_\infty\). Let \(G_{\epsilon\delta}\) denote the number of choices of a single middle diagonal pair \((a_i,b_i)\) and its four off-diagonal coordinates \((x_i,u_i,y_i,v_i)\) satisfying the two local linear equations, with \(\epsilon=\mathbf1_{a_0\neq0}\), \(\delta=\mathbf1_{b_\infty\neq0}\). The middle diagonal possibilities are exactly \((0,0)\), \((a_i\neq0,b_i=0)\), and \((a_i=0,b_i\neq0)\). Counting solutions in these three cases gives
\[
\begin{aligned}
G_{00}&=q^4+2(q-1)q^3=q^3(3q-2),\\
G_{10}=G_{01}&=q^3+(q-1)q^2+(q-1)q^3=q^2(q^2+q-1),\\
G_{11}&=q^2+2(q-1)q^2=q^2(2q-1).
\end{aligned}
\]
For clarity, the three summands of \(G_{00}\) have respectively \(q^4\), \((q-1)q^3\), and \((q-1)q^3\) solutions; the three summands of \(G_{10}\) have \(q^3\), \((q-1)q^2\), and \((q-1)q^3\) solutions. This supplies a direct check of the local linear-system boundary cases.

If \((a_0,b_\infty)\neq(0,0)\), the last displayed equation is a nontrivial linear equation in \((z,w)\), with exactly \(q\) solutions for every middle configuration. The outer equations admit \(q\) possibilities for \(b_0\) when \(a_0=0\) and one otherwise; likewise, there are \(q\) possibilities for \(a_\infty\) when \(b_\infty=0\) and one otherwise. There are \(q-1\) nonzero choices for either nonzero endpoint. Thus these three endpoint regimes contribute
\[
2q^2(q-1)G_{10}^m+q(q-1)^2G_{11}^m.
\]

For \(a_0=b_\infty=0\), the final equation is instead the dot-product condition \(\sum_i x_iv_i=0\). It leaves both \(z\) and \(w\) free, and leaves \(b_0\), \(a_\infty\) free as well. Fix any nontrivial additive character \(\psi:\mathbb F_q\to\mathbb C^\times\). By finite-field orthogonality, the number of admissible middle configurations with zero dot product is
\[
\frac1q\left(G_{00}^m+(q-1)H^m\right),
\]
where \(H\) is the local sum of \(\psi(x_iv_i)\) over the configurations satisfying the two local linear equations. The \((0,0)\) middle-diagonal case contributes
\[
q^2\sum_{x,v\in\mathbb F_q}\psi(xv)=q^3
\]
(the sum over \(x,v\) equals \(q\)). Each of the other two middle-diagonal types forces \(x_iv_i=0\) and contributes \((q-1)q^3\). Thus
\[
H=q^3+2(q-1)q^3=q^3(2q-1).
\]
Every nonzero Fourier frequency produces the same local sum \(H\), since scaling \(x\) by any nonzero scalar is bijective. Multiplication by the \(q^4\) free choices of \((b_0,a_\infty,z,w)\) yields the \((0,0)\) contribution
\[
q^3\left(G_{00}^m+(q-1)H^m\right).
\]
Combining the four disjoint endpoint regimes proves the claimed closed formula, including \(m=0\), where all empty products are one.

For the recurrence, note for \(q\geq2\) that
\[
B_1-B_2=q^3(q-1)>0,\quad B_2-B_3=q^2(q-1)^2>0,\quad B_3-B_4=q^3(q-1)>0.
\]
All four scalar coefficients in the exponential formula are nonzero. The four sequences \(B_j^m\) are linearly independent over \(\mathbb Q\) by the Vandermonde determinant. Every linear recurrence annihilating \(Z_m(q)\) must therefore vanish at all four distinct \(B_j\); the displayed product polynomial annihilates it and has minimal degree four. The strict inequality of bases also gives the asymptotic expression.

## Verification

The companion standalone file `verify.py` implements the incidence multiplication table directly. For each element \(a\) it independently forms its left-multiplication matrix and computes the kernel size \(q^{\dim A_m-\operatorname{rank}L_a}\); summing these kernels gives the exact number of ordered pairs with \(ab=0\). This procedure is independent of the character-sum decomposition above. Its exhaustive tests over \(\mathbb F_2,\mathbb F_3,\mathbb F_5,\mathbb F_7\), and the genuine extension field \(\mathbb F_4\) pass fourteen parameter configurations, reaching \(m=4\) for \(q=2\) and \(m=2\) for \(q=3\). Example values include \(Z_2(2)=16288\), \(Z_2(3)=2325753\), and \(Z_1(4)=160192\). The infinite-family proof is the field character-sum argument, not numerical extrapolation.

## Relationship to prior work

Quinn's *The incidence algebras of posets and acyclic categories* supplies an explicit interval-basis multiplication description and studies Groebner bases and shellability, not cardinalities of ordered zero-product pairs. Ekhad and Zeilberger enumerate upper-triangular matrices satisfying \(X^2=0\); this is a different, diagonal restriction of a one-variable condition, not \(ab=0\) for two independently chosen elements of the diamond incidence algebra. Jia and Xiao study identities of maps under two-sided zero products on incidence algebras, not one-sided finite-field pair counts.

A known count for **outward-star** incidence algebras (one minimal vertex and incomparable maxima) has no composable length-two paths, and its multiplication constraints decouple; it does not imply the present four-pole formula. Earlier results on commuting idempotents and square-zero radical elements in incidence algebras likewise impose distinct polynomial equations. This work does not claim a new definition of incidence algebras, a general all-posets enumeration, or historical priority beyond the comparisons explicitly made.

## Limitations

The result is an exact finite-field point count and minimal recurrence, not a classification of irreducible components or of nonreduced zero-product schemes. It concerns only one-sided ordered zero products in the specified ordinal-sum posets, not arbitrary incidence algebras. A literature search and relevant primary-text comparisons have not established a prior equivalent closed form; the possibility of an unnoticed formulation under a general triangular-matrix enumeration remains a publication-priority risk. There has been no independent mathematical audit.

## References

- D. Quinn, *The incidence algebras of posets and acyclic categories*, Kyushu J. Math. 67 (2013), 117–127, doi:10.2206/kyushujm.67.117; arXiv:1501.02481 (preprint). J-STAGE online-release date: 2013-07-25.
- S. B. Ekhad and D. Zeilberger, *The number of solutions of X squared equals zero in triangular matrices over GF(q)*, Electronic J. Combin. 3 (1996), R2, arXiv:math/9512224.
- H. Jia and Z. Xiao, *Functional identities of degree 2 at two-sided zero products on incidence algebras*, arXiv:2608.26853 (2026).
