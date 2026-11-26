# Sharp \(h^*\)-unimodality criterion on the Gorenstein canonical boundary of \(\mathbb P(1^r,a,b)\)
## Finding
Let \(r\ge2\), and let \(X=\mathbb P(1^r,a,b)\) be Gorenstein, canonical, and non-terminal. Associate to \(X\) the reflexive weighted-projective simplex
\[
\Delta_X=\Delta_{(1,\mathbf q)},\qquad \mathbf q=(1^{r-1},a,b),
\]
and write \(h_X^*(z)\) for its Ehrhart \(h^*\)-polynomial.

For the unimodality criterion, use the following boundary parametrization and product formulas. Every such \(X\) is either
\[
X_{r,t}=\mathbb P\!\left(1^r,\frac{2r}{t},r+\frac{2r}{t}\right),\qquad t\mid 2r,
\]
or the exceptional equal-weight space \(\mathbb P(1^r,r,r)\).

For \(X_{r,t}\), put \(a=2r/t\). If \(t=2c\) is even, then
\[
h_{r,t}^*(z)=
\left(\sum_{j=0}^{a-1}z^{jc}\right)
\left(1+2\sum_{i=1}^{c}z^i+z^{c+1}\right).
\]
If \(t\) is odd, then \(t\mid r\); putting \(p=r/t\) and \(u=(t+1)/2\),
\[
h_{r,t}^*(z)=
\left(\sum_{j=0}^{p-1}z^{jt}\right)
\left(1+2\sum_{i=1}^{t}z^i+z^{t+1}+2z^u\right).
\]
The equal-weight member has
\[
h^*_{\mathbb P(1^r,r,r)}(z)=
(1+z+\cdots+z^{r-1})(1+z+z^2).
\]

These formulas give a sharp unimodality classification. The equal-weight member is always \(h^*\)-unimodal. For the divisor family \(X_{r,t}\), \(h_{r,t}^*\) is non-unimodal exactly in either of the following two cases:
\[
\text{(i) }t\ge3\text{ is odd and }r\ge2t;
\qquad
\text{(ii) }t\ge6\text{ is even and }r\ge\frac{3t}{2}.
\]
Equivalently, \(t=1,2,4\) is always unimodal; for odd \(t\ge3\) unimodality occurs exactly when \(r=t\); and for even \(t\ge6\) it occurs exactly when \(2r/t\le2\).

Thus the canonical/non-terminal Gorenstein boundary contains infinite explicit families of both unimodal and non-unimodal reflexive simplices, separated by elementary divisor arithmetic.

## Assumptions and scope
The base field is \(\mathbb C\). The weighted projective spaces are ordinary well-formed spaces; the repeated weight \(1\) makes well-formedness automatic. The simplex \(\Delta_{(1,\mathbf q)}\) is the standard lattice simplex associated to the fan of the weighted projective space after distinguishing one unit weight. The statement concerns the Ehrhart \(h^*\)-polynomial of that simplex, not the Hilbert numerator of the weighted homogeneous coordinate ring.

The Gorenstein hypothesis means every weight divides the total weight \(Q=r+a+b\). For such a weighted projective space the associated simplex is reflexive. Unimodality means that the coefficient sequence weakly increases up to some index and then weakly decreases.

## Proof
Write \(Q=r+a+b\), and order \(a\le b\). First classify the Gorenstein canonical/non-terminal locus. Set
\[
x=Q/a,\qquad y=Q/b.
\]
These are integers with \(x\ge y\). Put \(d=b-a\). The two heavy affine charts have cyclic quotient types
\[
\frac1a(1^r,b),\qquad \frac1b(1^r,a).
\]
In the \(b\)-chart the age numerator for \(1\le j<b\) is \(rj+[-jd]_b\), and in the \(a\)-chart for \(1\le j<a\) it is \(rj+[jd]_a\); brackets denote least nonnegative residues. The ages are positive integers by the Gorenstein divisibility conditions. Thus every Gorenstein member is canonical, and terminality fails exactly when a nonidentity element has age one. A chart of weight \(1\) has no such elements.

Because
\[
\frac rQ=1-\frac1x-\frac1y,
\]
one obtains
\[
r-d=Q\frac{y-2}{y},\qquad r+d-a=Q\frac{x-3}{x}.
\]
Since \(x\ge y\ge2\) and \(Q>a+b\), we have \(x\ge3\). When \(y=2\), we have \(d=r\), and \(j=1\) in the \(b\)-chart gives numerator \(r+(b-d)=b\). If \(y>2\) and \(x=3\), then \(x=y=3\), so \(a=b=r\), and \(j=1\) gives age one. In the remaining case \(y>2\), \(x>3\), we have \(d<r\) and \(a<r+d\). If \(d=0\), these imply \(r>a=b\), so both charts are terminal. If \(d>0\), in the \(b\)-chart only \(rj\le b\) needs checking; then \(0<jd<b\), and the numerator is \(b+j(r-d)>b\). In the \(a\)-chart only \(rj\le a\) needs checking; then \(jd<a\), and the numerator is \(j(r+d)>a\). This proves terminality in all remaining cases.

When \(y=2\), we have \(b=r+a\) and
\[
t:=x-2=\frac{2r}{a}
\]
is a positive divisor of \(2r\), giving \(X_{r,t}\). Conversely, for every positive divisor \(t\mid 2r\), these weights give \(Q/b=2\) and \(Q/a=t+2\); the equal-weight case gives \(Q/a=Q/b=3\). This proves the boundary parametrization in both directions.

Now apply the standard floor formula for a weighted-projective simplex. With \(\mathbf q=(1^{r-1},a,b)\),
\[
h_X^*(z)=\sum_{m=0}^{Q-1}z^{w(m)},\qquad
w(m)=m-\left\lfloor\frac{am}{Q}\right\rfloor-\left\lfloor\frac{bm}{Q}\right\rfloor,
\]
since the \(r-1\) unit-weight floor terms vanish for \(0\le m<Q\).

For \(X_{r,t}\), one has
\[
a=\frac{2r}{t},\qquad b=r+a,\qquad Q=a(t+2)=2b.
\]
Therefore
\[
w(m)=m-\left\lfloor\frac{m}{t+2}\right\rfloor-\left\lfloor\frac m2\right\rfloor
=\left\lceil\frac m2\right\rceil-\left\lfloor\frac{m}{t+2}\right\rfloor.
\]

Suppose first that \(t=2c\). With \(L=t+2=2(c+1)\),
\[
w(m+L)=w(m)+c.
\]
There are exactly \(a\) blocks of length \(L\). On the initial block \(0\le m<L\), the exponents are \(\lceil m/2\rceil\), whose multiplicities are
\[
1,2,2,\ldots,2,1
\]
in degrees \(0,1,\ldots,c,c+1\). This gives the even-\(t\) factorization.

If \(t\) is odd, then \(t\mid r\). Put \(p=r/t\) and \(L=t+2\). Since \(L\) is odd,
\[
w(m+2L)=w(m)+t,
\]
and \(Q=p(2L)\), so there are \(p\) blocks. On \(0\le m<2L\), the exponent multiplicities are \(1\) at degrees \(0\) and \(t+1\), \(2\) at every interior degree except \(u=(t+1)/2\), and \(4\) at degree \(u\). This is exactly the odd-\(t\) factorization.

For \((a,b)=(r,r)\), \(Q=3r\) and
\[
w(m)=m-2\left\lfloor\frac m3\right\rfloor.
\]
Writing \(m=3j+s\) with \(0\le j<r\) and \(s\in\{0,1,2\}\) gives \(w(m)=j+s\), proving the equal-weight product formula.

It remains to read off unimodality. For the equal-weight member the coefficients count overlaps of two integer intervals, so they rise to a plateau and then fall. For \(t=1\), the odd base block is \(1+4z+z^2\), shifted by consecutive powers of \(z\); the coefficient sequence is unimodal. For \(t=2\), the even base block is \(1+2z+z^2\), again shifted consecutively; for \(t=4\), the base block is \(1+2z+2z^2+z^3\) and the shifts are by two degrees. Both yield a single plateau and are unimodal.

For odd \(t\ge3\), a single block (equivalently \(r=t\)) is unimodal with unique central coefficient \(4\). If there are at least two blocks, the coefficients at \(u\) and \(t+u\) are both \(4\), because these degrees lie outside the overlaps of adjacent blocks. At \(u+1\) the coefficient is \(2\) if \(t\ge5\), and \(3\) if \(t=3\): in the latter case \(u+1=t\), where the second block adds its constant term. In both cases there is a strict descent followed by a rise. This is exactly \(r\ge2t\).

For even \(t=2c\ge6\), so \(c\ge3\), one or two shifted blocks are unimodal. With at least three blocks, the coefficients at degrees \(c,c+1,c+2,2c\) are respectively \(3,3,2,3\): there is a strict descent followed by a rise. Since the number of blocks is \(a=2r/t\), non-unimodality is exactly \(a\ge3\), or \(r\ge3t/2\). The classification follows.

## Verification
The bundled script `verify_hstar_boundary.py` independently reconstructs \(h^*\) from the floor formula, checks the two closed factorizations coefficient-by-coefficient, checks the equal-weight product, and compares the stated unimodality criterion with direct coefficient testing for every \(2\le r\le400\) and every divisor \(t\mid2r\). It also independently scans the Gorenstein canonical/non-terminal pairs for \(2\le r\le60\) using divisibility and all Reid--Tai group elements, confirming the boundary parametrization. It returns `VERIFY_OK`.

## Relationship to prior work
Kasprzyk explains the correspondence between Gorenstein weighted projective spaces and reflexive simplices and develops canonical/terminal criteria for weighted projective spaces. Braun--Davis--Solus give the floor formula used above and study \(h^*\)-unimodality for reflexive simplices, including families generalizing Payne's counterexamples. Braun--Liu later show that every reflexive \(\Delta_{(1,\mathbf q)}\) has a general geometric-series factor and study Kronecker factorizations, with their main classifications focused on different support patterns. Braun--Davis--Hanely--Lane--Solus classify the integer decomposition property for weighted-projective simplices with few distinct non-unit weights and study non-unimodality under reflexive stabilization.

The published Resultary finding *Divisor cores for Gorenstein two-heavy weighted projective spaces* (5519b06e1341) gives the same boundary parametrization; *A triangular classification of canonical and terminal two-heavy weighted projective spaces* (7f218dfae0e7) gives the underlying chart inequalities. *A divisor criterion for Kronecker \(h^*\)-polynomials on a Gorenstein canonical boundary* (ecdefed7e8e0) uses these same factorizations for a different polynomial invariant, whether all roots lie on the unit circle. Its proof gives the same even and odd products, as well as the equal-weight product. These overlapping formulas are inputs to the unimodality analysis and are not asserted as separate novel findings. The contribution assessed here is the sharp necessary-and-sufficient unimodality criterion on the entire boundary. The dates of the two \(h^*\)-records alone do not establish priority.

## Limitations
The theorem is restricted to the family \(\mathbb P(1^r,a,b)\) with at most two non-unit weight entries, and only to its Gorenstein canonical/non-terminal boundary. It does not classify \(h^*\)-unimodality on the interior terminal locus, on non-Gorenstein canonical spaces, or for weighted projective spaces with more non-unit weight entries. The originality search cannot exclude an equivalent specialization buried under different notation in the broad Ehrhart literature.

## References
- A. M. Kasprzyk, *Classifying terminal weighted projective space*, arXiv:1304.3029 (2013).
- B. Braun, R. Davis, and L. Solus, *Detecting the Integer Decomposition Property and Ehrhart Unimodality in Reflexive Simplices*, arXiv:1608.01614 (2016).
- B. Braun and F. Liu, *\(h^*\)-Polynomials With Roots on the Unit Circle*, arXiv:1807.00105 (2018).
- B. Braun, R. Davis, D. Hanely, M. Lane, and L. Solus, *The Integer Decomposition Property and Weighted Projective Space Simplices*, arXiv:2103.17156 (2021).
