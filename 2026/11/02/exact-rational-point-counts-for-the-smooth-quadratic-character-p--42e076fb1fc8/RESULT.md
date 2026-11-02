# Exact rational-point counts for the smooth quadratic-character plane curves

## Finding
For every odd prime power \(q=p^r\) with \(p\ge5\), put \(m=(q-1)/2\) and consider the degree-\(m\) plane curve
\[
C_q:\quad (X+Y+Z)^m+X^m+Y^m+Z^m=0\quad\subset\mathbb P^2_{\mathbb F_q}.
\]
Then \(C_q\) is smooth and geometrically integral, and the number of its rational projective points is exactly
\[
\boxed{\#C_q(\mathbb F_q)=
\begin{cases}
3(q-1)^2/8,&q\equiv1\pmod4,\\
3(q^2-4q+11)/8,&q\equiv3\pmod4.
\end{cases}}
\]
Each coordinate axis meets \(C_q(\mathbb F_q)\) in no points when \(q\equiv1\pmod4\), and in exactly one point when \(q\equiv3\pmod4\). In the latter case, these points are \([0:1:-1]\), \([1:0:-1]\), and \([1:-1:0]\), respectively. The formulas hold for extension fields as well as prime fields.

## Assumptions and scope
The characteristic is at least five, \(q\) is any power of that characteristic, and all rational-point counts are over the *defining* field \(\mathbb F_q\) (not an arbitrary extension of it). The smoothness and the nontrivial blocking property in the \(q\equiv3\pmod4\), \(q\ge11\) range are established in the motivating paper; the new mathematical statement is the exact two-class point count, together with the exact coordinate-axis intersection counts. The latter refines the original paper's existence observation. For \(q\equiv1\pmod4\), the original paper already notes that the curve is not blocking.

## Proof
Let \(\chi:\mathbb F_q\to\{0,\pm1\}\) be the quadratic multiplicative character, extended by \(\chi(0)=0\), and let \(\epsilon=\chi(-1)\). For \(a\in\mathbb F_q\), the equality \(a^m=\chi(a)\) holds in \(\mathbb F_q\). The integer \(\chi(x+y+z)+\chi(x)+\chi(y)+\chi(z)\) lies between \(-4\) and \(4\), and since \(p\ge5\), it vanishes in \(\mathbb F_q\) precisely when it vanishes as an integer. Consequently, introducing an indeterminate \(T\), the number \(A_q\) of affine triples including the zero triple that satisfy the homogeneous equation is the constant Laurent coefficient
\[
A_q=[T^0]\sum_{x,y,z\in\mathbb F_q}
 T^{\chi(x)+\chi(y)+\chi(z)+\chi(x+y+z)}.
\]
Each nonzero affine solution corresponds to one of the \(q-1\) nonzero scalar representatives of a rational projective point; therefore \(A_q=1+(q-1)\#C_q(\mathbb F_q)\).

For a nontrivial complex additive character \(\psi\) define \(f_T(a)=T^{\chi(a)}\) and \(\widehat f_t(T)=\sum_{a\in\mathbb F_q}\psi(ta)f_T(a)\). Introducing the fourth variable \(e=-x-y-z\), character orthogonality gives
\[
A_q=[T^0]\frac1q\sum_{t\in\mathbb F_q}
\widehat f_t(T)^3\widehat f_t(T^\epsilon).
\]
Here \(\epsilon=1\) or \(-1\) is used as an ordinary integer exponent, so \(f_T(-a)=f_{T^\epsilon}(a)\). Set
\[
\alpha=(T+T^{-1})/2,\quad\beta=(T-T^{-1})/2,
\quad u=1-\alpha,\quad f_0=1+(q-1)\alpha.
\]
For \(t\ne0\), one has \(\widehat f_t(T)=u+\chi(t)\beta G\), where \(G=\sum_a\chi(a)\psi(a)\) is the quadratic Gauss sum and \(G^2=\epsilon q\). The nonzero \(t\)'s split equally between the two character signs. When \(\epsilon=1\), averaging their fourth powers gives
\[
qA_q=[T^0]\left(f_0^4+(q-1)(u^4+6qu^2\beta^2+q^2\beta^4)\right).
\]
When \(\epsilon=-1\), the last Fourier factor has the opposite quadratic-character term, and averaging \((u+\chi(t)\beta G)^3(u-\chi(t)\beta G)\) gives
\[
qA_q=[T^0]\left(f_0^4+(q-1)(u^4-q^2\beta^4)\right).
\]
The four needed constant coefficients are
\[
[T^0]f_0^4=1+3(q-1)^2+3(q-1)^4/8,\quad
[T^0]u^4=35/8,
\]
\[
[T^0]u^2\beta^2=-5/8,\qquad[T^0]\beta^4=3/8.
\]
Substitution, followed by \(A_q=1+(q-1)\#C_q(\mathbb F_q)\), yields exactly the claimed piecewise formula. These are identities in \(q\), so the argument includes all extension-field cases.

On the coordinate axis \(X=0\), the point equation is \(\chi(y)+\chi(z)+\chi(y+z)=0\). If exactly one of \(y,z\) is zero, the sum is \(\pm2\), impossible in characteristic at least five. For \(yz\ne0\), a sum of three elements from \(\{0,\pm1\}\) can vanish only when \(\chi(y)=-\chi(z)\) and \(y+z=0\); this is possible exactly when \(\epsilon=-1\), giving the unique projective point \([0:1:-1]\). Symmetry proves the other two axis claims.

For completeness, the published smoothness argument can be reconstructed as follows. At a geometric singular point all three derivatives vanish, giving \(x^{m-1}=y^{m-1}=z^{m-1}=-(x+y+z)^{m-1}\); none of the four arguments can be zero. Put \(x=\alpha z\), \(y=\beta z\). Then \(\alpha^{q-3}=\beta^{q-3}=1\) and \((1+\alpha+\beta)^{q-3}=1\), whence \(\alpha^q=\alpha^3\), \(\beta^q=\beta^3\), and \((1+\alpha+\beta)^q=(1+\alpha+\beta)^3\). The Frobenius identity implies \(3(\alpha+\beta)(\alpha+1)(\beta+1)=0\). Every factor is impossible: \(\alpha=-1\), \(\beta=-1\), or \(\alpha+\beta=0\) would force a nonzero \((m-1)\)-st power to be its own negative. Thus the curve is smooth. A smooth positive-degree plane curve is geometrically integral here: two distinct geometric components would intersect by Bézout and cause a singularity.

## Verification
The standalone Python program `verify_point_count.py` (Python standard library only) reproduces the two Laurent-polynomial identities over \(\mathbb Q[q,T,T^{-1}]\) by exact rational arithmetic, so it checks the full symbolic \(q\)-dependent computation rather than only a finite list. It independently enumerates all projective rational solutions and the three axis intersections over fifteen prime fields and four extension fields, including \(q=25,49,121,343\). Execute `python3 verify_point_count.py` from the folder containing the program. Its success marker is `BLOCKING_CURVE_POINT_COUNT_FORMAL_AND_EXTENSION_FIELD_PASS`. The enumeration provides corroboration; the Fourier–Gauss calculation and smoothness argument prove the universal statement.

## Relationship to prior work
Asgarli, Ghioca, and Yip introduced this exact polynomial in Section 7.2 of arXiv:2208.13299. Their Claim 7.2 proves smoothness over all characteristics above three; their Claim 7.3 establishes nontrivial blocking for \(q\equiv3\pmod4\), \(q\ge11\). The paper supplies a point on a coordinate axis in that regime and notes that \(q\equiv1\pmod4\) is not blocking, but does not state the rational-point cardinality of this family. Those original geometric statements are not claimed as new.

The subsequent *Most plane curves over finite fields are not blocking* (arXiv:2211.08523) studies statistical behavior across larger families, rather than the exact count on this specific symmetric half-power curve. Generic curve-count estimates, the blocking property, and the degree bound by themselves do not imply either explicit rational-point formula. Searches of relevant mathematical findings and accessible historical claims did not reveal the same formulas; this is not an exhaustive priority guarantee.

## Limitations
This calculation counts points only over the defining field \(\mathbb F_q\), where the exponent itself depends on \(q\). It does not provide the zeta function of any fixed \(C_q\) over all extensions \(\mathbb F_{q^n}\), because the defining exponent remains \((q-1)/2\) when extending scalars. It does not improve the published blocking theorem or classify arbitrary lines' intersection numbers. An unindexed equivalent computation remains a possible historical priority risk. Independent external validation has not been performed.

## References
1. Asgarli, Ghioca and Yip, *Plane curves giving rise to blocking sets over finite fields*, arXiv:2208.13299v1 (28 August 2022), revised v2 (31 May 2023), Section 7.2, Claims 7.2–7.3, Theorem 1.9. https://arxiv.org/html/2208.13299v2
2. S. Asgarli, D. Ghioca and C. H. Yip, *Most plane curves over finite fields are not blocking*, arXiv:2211.08523v1 (15 November 2022). https://arxiv.org/abs/2211.08523
3. Standard quadratic Gauss-sum identity: for \(\chi\) the quadratic character and \(\psi\) nontrivial additive, \(G(\chi,\psi)^2=\chi(-1)q\).
