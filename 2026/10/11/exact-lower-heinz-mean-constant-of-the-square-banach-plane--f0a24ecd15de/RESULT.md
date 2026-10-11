# Exact lower Heinz-mean constant of the square Banach plane
## Finding
Let \(X=(\mathbb R^2,\lVert\cdot\rVert_\infty)\). For \(0\le \nu\le1\), write
\[
M_\nu(a,b)=\frac{a^\nu b^{1-\nu}+a^{1-\nu}b^\nu}2,
\]
with the continuous endpoint convention on \([0,\infty)^2\), and define
\[
h_\nu(X)=\inf_{x\in S_X}\sup_{y\in S_X}M_\nu(\lVert x+y\rVert_\infty,\lVert x-y\rVert_\infty).
\]
Then
\[
h_\nu(X)=\frac{2^\nu+2^{1-\nu}}2
\qquad(0\le \nu\le1).
\]
The infimum is attained at each coordinate-axis unit vector.

## Assumptions and scope
The scalar field is real and the norm is \(\lVert(s,t)\rVert_\infty=\max\{|s|,|t|\}\). The claim concerns Dinarvand's lower Heinz-mean constant \(h_\nu\), not the upper constant \(H_\nu\). No assertion is made for other Banach spaces.

## Proof
The Heinz mean is symmetric in its two arguments and is nondecreasing in each argument on \([0,\infty)\).

First fix the axis point \(x_0=(1,0)\). If \(y=(u,v)\in S_X\), set
\[
A=\lVert x_0+y\rVert_\infty=\max\{|1+u|,|v|\},\qquad
B=\lVert x_0-y\rVert_\infty=\max\{|1-u|,|v|\}.
\]
Because \(|u|,|v|\le1\), one has \(\max\{A,B\}\le2\). Also \(\min\{A,B\}\le1\): if \(u\ge0\), then \(B\le1\), while if \(u\le0\), then \(A\le1\). Hence, after possibly interchanging \(A\) and \(B\), monotonicity gives
\[
M_\nu(A,B)\le M_\nu(2,1)=\frac{2^\nu+2^{1-\nu}}2.
\]
Equality is obtained with \(y=(1,1)\), for which \((A,B)=(2,1)\). Therefore
\[
\sup_{y\in S_X}M_\nu(\lVert x_0+y\rVert_\infty,\lVert x_0-y\rVert_\infty)
=\frac{2^\nu+2^{1-\nu}}2.
\]
This proves the required upper bound for \(h_\nu(X)\).

For the reverse inequality, the signed-coordinate permutations are linear isometries of \(X\). Thus every \(x\in S_X\) is isometric to a point \((1,a)\) with \(0\le a\le1\). For such a point choose \(y=(1,-1)\). Then
\[
\lVert x+y\rVert_\infty=2,\qquad
\lVert x-y\rVert_\infty=1+a\ge1.
\]
Consequently
\[
\sup_{y\in S_X}M_\nu(\lVert x+y\rVert_\infty,\lVert x-y\rVert_\infty)
\ge M_\nu(2,1+a)\ge M_\nu(2,1).
\]
Taking the infimum over \(x\in S_X\) yields the reverse bound and proves the formula.

Finally, \(\nu\mapsto(2^\nu+2^{1-\nu})/2\) is symmetric about \(1/2\), strictly decreasing on \([0,1/2]\), and strictly increasing on \([1/2,1]\). Hence its minimum is \(\sqrt2\) at \(\nu=1/2\), and its endpoint values are \(3/2\).

## Verification
The proof is exact and requires no numerical approximation. The included `verify.py` independently checks the axis upper-bound inequalities on a dense rational grid, the explicit lower-bound witness for every tested boundary point, and the endpoint values. These finite checks are supplementary and are not used as a substitute for the analytic proof.

## Relationship to prior work
Dinarvand introduced \(H_\nu\) and \(h_\nu\) and, for the square plane, stated \(H_\nu=2\) together with only the bounds \(\sqrt2\le h_\nu\le3/2\). The formula above fills that exact square-plane gap and interpolates the two known endpoint quantities continuously in \(\nu\). A later paper on absolute normalized norms develops exact formulas for the upper constant \(H_\nu\), not the lower infimum-supremum constant treated here.

## Limitations
The argument exploits the full signed-permutation symmetry and flat faces of the two-dimensional square. It does not by itself determine \(h_\nu\) for higher-dimensional cubes or for general absolute normalized planes. The literature searches reported in the review found no exact square-plane formula, but no search can establish absolute uniqueness of a mathematical statement.

## References
1. M. Dinarvand, “Heinz means and triangles inscribed in a semicircle in Banach spaces,” *Mathematical Inequalities & Applications* 22 (2019), 275–290. DOI: 10.7153/MIA-2019-22-21.
2. Z.-F. Zuo and Y.-M. Huang, “Absolute normalized norms in \(\mathbb R^2\) and Heinz means constant,” *Topological Methods in Nonlinear Analysis* 60 (2022), 475–490. DOI: 10.12775/TMNA.2022.003.
