# Square-zero nil-clean fibers and sharp index for branched interval incidence algebras

## Finding

For a finite field \(k=\mathbb F_q\) and an integer \(r\ge2\), let \(P_r\) have a minimum \(\bot\), maximum \(\top\), and exactly \(r\) incomparable middle elements \(m_i\), with \(\bot<m_i<\top\). On its incidence algebra \(A=I(P_r,k)\), define the square-zero nil-clean fiber
\[
h_2(a)=\#\{e\in A:e^2=e,\ (a-e)^2=0\}.
\]
The following pointwise formula classifies this invariant for every element, not only its possible values. Write the diagonal entries of \(a\) as \((\alpha,\beta_1,\ldots,\beta_r,\gamma)\) and its two arms as \(p_i=a(\bot,m_i)\) and \(s_i=a(m_i,\top)\).

If any diagonal entry lies outside \(\{0,1\}\), then \(h_2(a)=0\). Otherwise, if \(\alpha\ne\gamma\), define \(c_i=s_i\) when \(\beta_i=\gamma\) and \(c_i=p_i\) when \(\beta_i=\alpha\). Then
\[
h_2(a)=\begin{cases}q^{r+1},&c_1=\cdots=c_r=0,\\q^r,&\text{otherwise}.\end{cases}
\]
If \(\alpha=\gamma\), put \(T=\{i:\beta_i\ne\alpha\}\), \(t=|T|\), and \(C=\sum_{i\notin T}p_is_i\). For \(t=0\), the value is \(1\) when \(C=0\) and \(0\) otherwise. For \(t\ge1\),
\[
h_2(a)=\begin{cases}q^{2t-1}+q^t-q^{t-1},&C=0,\\q^{2t-1}-q^{t-1},&C\ne0.\end{cases}
\]
All values are independent of \(a(\bot,\top)\). In particular, the sharp square-zero nil-clean index is
\[
\boxed{\max_{a\in A}h_2(a)=q^{2r-1}+q^r-q^{r-1}.}
\]
The unrestricted nil-clean index of this algebra is \(q^{2r}\). Thus bounding the nilpotence degree of the remainder to two causes a strict, explicitly quantified loss, first visible for \(r=2\).

## Assumptions and scope

All algebras are associative with identity. The prime power \(q\ge2\) is arbitrary, including characteristic two. The poset has exactly the comparabilities stated above, so its incidence algebra has dimension \(3r+3\): there are \(r+2\) diagonal coefficients, \(2r\) arm coefficients, and one coefficient on \((\bot,\top)\). The property \((a-e)^2=0\) means square-zero, not merely nilpotent. There is no commutation requirement between \(e\) and \(a-e\). The quantity counts labeled decompositions, not conjugacy orbits.

## Proof

The incidence convolution is \((fg)(x,y)=\sum_{x\le z\le y}f(x,z)g(z,y)\). If \((a-e)^2=0\), its diagonal vanishes. An idempotent has each diagonal coordinate in \(\{0,1\}\), so a nonbinary diagonal gives no decompositions. Assume from now on all diagonal entries are binary and fixed for \(e\).

Use \(x_i=e(\bot,m_i)\), \(y_i=e(m_i,\top)\), and \(z=e(\bot,\top)\). Computing \(e^2=e\) gives, with multiplication in \(k\),
\[
(\alpha+\beta_i-1)x_i=0,\qquad
(\beta_i+\gamma-1)y_i=0,\qquad
(\alpha+\gamma-1)z+\sum_i x_iy_i=0.
\]
These are necessary and sufficient, since the stated coordinates are all incidence intervals. As each diagonal value is binary, \(x_i\) is free precisely when \(\alpha\ne\beta_i\) and \(y_i\) is free precisely when \(\beta_i\ne\gamma\). If \(\alpha\ne\gamma\), exactly one of \(x_i,y_i\) is free for each \(i\), and \(z\) is free. If \(\alpha=\gamma\), the \(2t\) variables \((x_i,y_i)\) for \(i\in T\) are free, all other arm variables vanish, and \(z\) is uniquely determined by the third equation. The argument is valid in characteristic two because each nonzero coefficient above is a unit \(\pm1\).

Put \(n=a-e\). Its diagonal is zero, so the only possibly nonzero coefficient of \(n^2\) is the coefficient on \((\bot,\top)\). Direct convolution gives
\[
(n^2)(\bot,\top)=\sum_{i=1}^r(p_i-x_i)(s_i-y_i).
\]
The value of \(a(\bot,\top)\) and the choice of \(z\) are absent. If \(\alpha\ne\gamma\), the equation is affine linear in exactly \(r\) free arm variables, with coefficients \(c_i\) as defined in the statement. If all coefficients vanish, every term in the constant also vanishes; thus every assignment solves the equation, yielding \(q^r\) assignments times \(q\) choices for \(z\). Otherwise one nonzero linear coefficient fixes one variable and gives \(q^{r-1}\) arm assignments, again times \(q\) for \(z\). This gives the two unequal-endpoint counts.

If \(\alpha=\gamma\), all inactive arms contribute the constant \(C\), while translation of the active variables \((x_i,y_i)\) changes the remaining equation into the ordinary dot-product equation \(X_1Y_1+\cdots+X_tY_t=-C\) over \(k\). If \(t=0\), this has a solution exactly when \(C=0\). If \(t\ge1\), when \(C=0\) the zero vector \(X\) contributes \(q^t\) possibilities for \(Y\), and each of the \(q^t-1\) nonzero \(X\) contributes \(q^{t-1}\). When \(C\ne0\), the zero vector contributes none and each nonzero vector contributes \(q^{t-1}\). This proves the pointwise formula.

For \(r\ge2\), the largest equal-endpoint count is \(Z_r=q^{2r-1}+q^r-q^{r-1}\), attained by choosing \(\beta_i\ne\alpha=\gamma\) for every middle vertex, so \(t=r\) and the inactive sum is empty. The other equal-endpoint counts are bounded by \(Z_r\) because the zero-dot-product counts increase with dimension; unequal-endpoint counts are at most \(q^{r+1}\). For \(r=2\), \(Z_r-q^{r+1}=q^2-q>0\); for \(r\ge3\), \(q^{2r-1}\ge q^{r+2}>q^{r+1}\). Hence \(Z_r\) is the sharp overall maximum.

For comparison, dropping the square-zero condition on \(n\) while retaining nilpotence permits every idempotent with the prescribed diagonal: the strictly off-diagonal incidence ideal is nilpotent. For the displayed diagonal with all middle entries opposite to the endpoints, the idempotent fiber has \(q^{2r}\) elements. Every other diagonal fiber has size at most \(q^{2r}\): with unequal endpoints it has \(q^{r+1}\), while with equal endpoints and \(t\) opposites it has \(q^{2t}\). Therefore the ordinary nil-clean index is exactly \(q^{2r}\), and the refined index is strictly smaller.

## Verification

The accompanying standalone Python file `verify.py` enumerates all idempotents using literal incidence convolution rather than using the classification equations. It compares the number leaving a square-zero difference with the stated pointwise formula for all arm coefficients and binary diagonals in six small field/poset cases: \((r,q)=(1,2),(1,3),(2,2),(2,3),(2,4),(3,2)\). The main theorem begins at \(r=2\); \(r=1\) tests boundary algebra. The \(q=4\) arithmetic uses the irreducible polynomial \(X^2+X+1\). The checker also independently maximizes every tested fiber and agrees with the claimed index for \(r\ge2\). It reports `DIAMOND_SQZERO_NILCLEAN_OK 6 families 7800 fibers`. The infinite family is established algebraically above, not inferred from the finite check.

## Relationship to prior work

Basnet and Bhattacharyya introduced the nil-clean index for unrestricted nilpotent summands [1]. Breaz and collaborators study nil-clean matrix rings [2]. Khripchenko's 2010 description of idempotents in finitary incidence algebras [3] supplies foundational conjugacy theory; the present proof uses direct incidence equations and additionally imposes \((a-e)^2=0\). Hou describes upper-triangular idempotents, including their total enumeration [4]; the available abstract does not itself address the square-zero remainder or these branched interval posets. General idempotent counting for split basic algebras also determines the unrestricted diagonal fibers, but cannot by itself count the isotropic quadratic section imposed here. In particular, the unrestricted fiber for the maximal-cut diagonal is \(q^{2r}\), while its square-zero section has \(q^{2r-1}+q^r-q^{r-1}\) points. This is a claim about a restriction to nilpotence order two, not a new count of unrestricted idempotents.

## Limitations

The theorem covers finite fields and the height-three posets with one minimum and one maximum and no comparabilities between middle elements. It does not classify longer posets, nonreduced geometric schemes, or conjugacy classes of decompositions. Literature search and inspection support the stated scientific difference, but exhaustive priority verification is not claimed; in particular, the full text of Hou's triangular-idempotent paper was not available for direct comparison. Independent mathematical validation is not included.

## References

1. D. K. Basnet and J. Bhattacharyya, *Nil clean index of rings*, International Electronic Journal of Algebra 15 (2014), 145–156. https://www.ieja.net/files/papers/volume-15/12-V15-2014.pdf
2. S. Breaz et al., *Nil-clean matrix rings*, arXiv:1310.0416, version 1 (1 October 2013). https://arxiv.org/abs/1310.0416
3. N. S. Khripchenko, *Finitary incidence algebras of quasiorders*, Matematychni Studii 34 (2010), 30–37. https://matstud.org.ua/texts/2010/34_1/30-37.pdf
4. X. Hou, *Idempotents in triangular matrix rings*, Linear and Multilinear Algebra, published online 22 March 2019, doi:10.1080/03081087.2019.1596223. https://doi.org/10.1080/03081087.2019.1596223
