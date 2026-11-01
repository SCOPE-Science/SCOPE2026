# Sharp Gaussian distance-power thresholds and leaf-balancing on double-star trees

## Finding
Let \(T_{a,b}\) be the unweighted tree with two adjacent hubs, with \(a\ge1\) leaves at the first hub and \(b\ge1\) at the second. For every real \(p\ge0\), put \(t=2^p\), \(u=3^p\), \(h=t(t-2)/2\), and \(z=u-1-t^2/2\). Define the real symmetric matrix
\[
M_{a,b}(p)=\begin{pmatrix}h-t/a&z\\z&h-t/b\end{pmatrix}.
\]
There is a unique \(p_{a,b}\in(1,2]\) for which the maximal eigenvalue of \(M_{a,b}(p)\) is zero. Moreover, \(p_{a,b}=2\) exactly when \(a=b=1\). The distance-power kernel \((d(x,y)^p)_{x,y\in T_{a,b}}\) is conditionally negative semidefinite exactly for \(0\le p\le p_{a,b}\), equivalently the Gaussian kernel \((\exp(-s d(x,y)^p))_{x,y}\) is positive semidefinite for **every** \(s>0\) exactly for these powers. Above this exponent it is indefinite for sufficiently small \(s>0\).

At fixed total leaf number \(L=a+b\), the threshold \(p_{a,b}\) **strictly increases with the product \(ab\)**. Thus the most unbalanced distribution \((1,L-1)\) uniquely minimizes the threshold, and the maximally balanced distribution \((\lfloor L/2\rfloor,\lceil L/2\rceil)\) uniquely maximizes it, up to exchange of hubs.

For equal leaf numbers \(a=b=m\), the threshold is the unique root in \((1,2]\) of
\[
3^p=1+(1+1/m)2^p.
\]
As \(m\to\infty\),
\[
p_{m,m}=1+\frac{2}{m(3\log3-2\log2)}+O(m^{-2}).
\]
At the critical power the zero-sum radical of the distance-power form is one-dimensional for \((a,b)\ne(1,1)\), and two-dimensional for \((a,b)=(1,1)\). The corresponding minimal squared-Euclidean embedding dimensions are \(a+b\) and \(1\), respectively.

## Assumptions and scope
All vertices, including hubs and leaves, belong to the metric space. Distances are unweighted shortest-path distances and take values \(0,1,2,3\). At exponent zero, use \(d(x,x)^0=0\) and \(d(x,y)^0=1\) when \(x\ne y\). Conditional negative semidefiniteness means \(\sum_{x,y}\omega_x\omega_y d(x,y)^p\le0\) for every real weight vector of total mass zero. The simultaneous-all-scales Gaussian statement is essential; no claim is made that a given kernel above the threshold is indefinite at every scale.

## Proof
**1. Exact reduction.** Let \(\alpha,\beta\) be the total weights on the two leaf sets, \(\gamma\) the first hub weight, and \(\delta=-\alpha-\beta-\gamma\) the second hub weight. Write the leaf weights as their group means plus deviations of zero sum, and put \(\gamma_*=(-t\alpha+t\beta)/2-\beta\). Directly summing the pair distances gives the exact identity
\[
\begin{split}
\sum_{x,y}\omega_x\omega_y d(x,y)^p
={}&(\alpha,\beta)M_{a,b}(p)(\alpha,\beta)^{\mathsf T}
-2(\gamma-\gamma_*)^2\\
&-t\sum_{x\text{ first leaf}}(\omega_x-\alpha/a)^2
-t\sum_{y\text{ second leaf}}(\omega_y-\beta/b)^2.
\end{split}
\]
Thus the distance power is conditionally negative semidefinite **if and only if** \(M_{a,b}(p)\preceq0\), and the equality space has the nullity of that two-by-two matrix. In particular, at \(p=1\), \(t=2\), \(u=3\), \(h=z=0\), and \(M_{a,b}(1)=\operatorname{diag}(-2/a,-2/b)\), giving strict negative type. For \(0\le p<1\), negative type follows from the standard decreasing-exponent property; it is strict by the strict-lower-exponent theorem.

**2. Uniqueness and Gaussian equivalence.** Normalize \(S(p)=M_{a,b}(p)/2^p\) and set
\[
y(p)=\frac{2^p-2}{2},\qquad w(p)=(3/2)^p-2^{-p}-2^{p-1}.
\]
Then \(S(p)=\bigl(\begin{smallmatrix}y-1/a&w\\w&y-1/b\end{smallmatrix}\bigr)\). The two eigenvalues of its derivative are \(y'\pm w'\), and
\[
y'+w'=(3/2)^p\log(3/2)+2^{-p}\log2>0,
\]
\[
y'-w'=2^p\bigl[\log2-(3/4)^p\log(3/2)-(1/4)^p\log2\bigr]>0
\]
for all \(p\ge1\). The last bracket is at least \((3/4)\log(4/3)>0\). Therefore \(S'(p)\) is positive definite for \(p\ge1\), and its top eigenvalue crosses zero at most once. At \(p=1\) it is negative; at \(p=2\) it has diagonal entries \(1-1/a\) and \(1-1/b\) and zero off diagonal, so it is positive unless \(a=b=1\), when it vanishes. The crossing thus exists and is unique in the stated interval. Beyond it the distance-power form has a positive zero-sum direction.

The classical Schoenberg equivalence identifies conditional negative semidefiniteness of \(d^p\) with positive semidefiniteness of \(\exp(-s d^p)\) at all \(s>0\). In the nonnegative-type regime, the finite distance-power forms yield squared-Euclidean embeddings. If a zero-sum direction has \(\omega^{\mathsf T}D_p\omega>0\), then the Taylor expansion \(\omega^{\mathsf T}K_{s,p}\omega=-s\omega^{\mathsf T}D_p\omega+O(s^2)\) is negative for all sufficiently small positive \(s\).

**3. Strict balancing.** For \(1<p<2\), one has \(0<z<h\). Indeed, strict convexity of \(p\mapsto\log(1+4^p/2)\) and equality with \(p\log3\) at endpoints \(1,2\) imply \(3^p>1+4^p/2\), so \(z>0\). Strict increase of the increments \((x+1)^p-x^p\) gives \(4^p-3^p>2^p-1\), so \(h>z\).

Fix \(L=a+b\), take \(a\le b\), and let \(r=p_{a,b}<2\). At the crossing \(\det M_{a,b}(r)=0\) and both diagonal entries are strictly negative because \(z(r)>0\). Expanding its determinant yields
\[
\det M_{a,b}=h^2-z^2+\frac{t^2\bigl(1-L(t-2)/2\bigr)}{ab}.
\]
Since \(0<z<h\), the vanishing determinant forces the final numerator \(t^2(1-L(t-2)/2)\) to be negative. If \(a'+b'=L\) and \(a'b'>ab\), the new determinant at \(r\) is strictly larger than zero. Furthermore \(\max(a',b')<b\), so both new diagonal entries remain strictly negative. Thus \(M_{a',b'}(r)\) is negative definite and its threshold is strictly larger than \(r\). This proves the entire majorization ordering, not merely the balanced case.

**4. Balanced roots and endpoint dimensions.** If \(a=b=m\), the eigenvalues of \(M_{m,m}\) are \(h-t/m\pm z\), and \(z>0\) on \((1,2)\). The top eigenvalue equals \(3^p-1-(1+1/m)2^p\). Dividing by \(2^p\), the equation becomes \((3/2)^p-2^{-p}=1+1/m\), whose left side is strictly increasing. Taylor expansion at \(p=1\) has derivative \((3\log3-2\log2)/2\), proving the asymptotic formula. At the crossing for \((a,b)\ne(1,1)\), \(z>0\) guarantees that the other matrix eigenvalue is strictly negative; the radical therefore has dimension one. At \((1,1),p=2\), the full two-by-two matrix is zero, so the radical has dimension two. Centering the negative-type matrix and using the standard squared-Euclidean Gram correspondence yields Euclidean ranks \((a+b+2)-1-1=a+b\), or \(4-1-2=1\), respectively.

## Verification
The accompanying `verify.py` implements the two-by-two spectral formula and independently builds the graph distance matrices. It checks 677 assertion groups over small asymmetric and balanced double stars, verifies finite centered-distance spectra on both sides of their critical exponent, confirms the exact hub-elimination identity, compares all leaf partitions for total leaf counts up to 36, and checks the balanced root and asymptotic formula through 299 leaves per side. Numeric checks support but do not replace the analytic proof. Run `python verify.py` with Python 3 and NumPy installed.

## Relationship to prior work
Schoenberg's general kernel criterion and the negative-type interval theorem are classical. Doust and Weston (2007) proved strict \(1\)-negative type for finite metric trees, a positive interval beyond one, and an exact exponent for a **single** star. Li and Weston (2009) established lower-exponent strictness and general quantitative bounds. Sánchez (2011) gave a general finite-metric matrix criterion and a sharp formula for complete bipartite **graphs**, which are not the two-hub tree metrics treated here. The result above adds an explicit *diameter-three tree* classification, a strict balancing extremal principle at fixed order, endpoint ranks, and sharp balanced asymptotics; those statements do not follow directly as asserted corollaries of the inspected sources. General finite-matrix criteria provide an algorithmic route, but do not by themselves supply the leaf-balancing theorem.

## Limitations
The exact comparison covers the cited primary texts and bounded public searches, not every historical source or potentially equivalent graph-metric table. The Gaussian statement concerns positive semidefiniteness **at all positive scales**; at exponents above the threshold only small-scale failure is claimed. Computational checks are finite corroboration, not an exhaustive proof. No independent mathematical validation has been performed.

## References
- I. J. Schoenberg, *Metric spaces and positive definite functions*, Transactions of the American Mathematical Society 44 (1938), 522–536.
- I. Doust and A. Weston, *Enhanced negative type for finite metric trees*, first public arXiv version 2007-05-03, arXiv:0705.0411; Journal of Functional Analysis 254 (2008), 2336–2364.
- H. Li and A. Weston, *Strict \(p\)-negative type of a metric space*, first public arXiv version 2009-01-06, arXiv:0901.0695.
- S. Sánchez, *On the supremal \(p\)-negative type of a finite metric space*, first public arXiv version 2011-08-02, arXiv:1108.0451; Journal of Mathematical Analysis and Applications 389 (2012), 98–107.
