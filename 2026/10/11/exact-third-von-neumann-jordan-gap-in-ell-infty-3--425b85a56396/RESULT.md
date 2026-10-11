# Exact third von Neumann–Jordan gap in \(\ell_\infty^3\)
## Finding
For the real Banach space \(X=\ell_\infty^3\), define
\[
C^{(3)}(x_1,x_2,x_3)=
\frac{\sum_{{\varepsilon_2,\varepsilon_3\in\{{-1,1\}}}}\|x_1+\varepsilon_2x_2+\varepsilon_3x_3\|_\infty^2}
{{4(\|x_1\|_\infty^2+\|x_2\|_\infty^2+\|x_3\|_\infty^2)}}.
\]
Then
\[
\overline C_{{NJ}}^{{(3)}}(X)=\frac{{3+\sqrt3}}{{2}},
\qquad
\overline C_{{mNJ}}^{{(3)}}(X)=\frac73.
\]
In particular, the unit-sphere restriction is genuinely strict in dimension three:
\[
\overline C_{{mNJ}}^{{(3)}}(X)<\overline C_{{NJ}}^{{(3)}}(X).
\]
For the unrestricted constant, equality is attained by
\[
x_1=(\sqrt3-1)(1,1,1),\qquad
x_2=(1,-1,-1),\qquad
x_3=(-1,1,-1).
\]
For the modified constant, replace \(x_1\) by \((1,1,1)\).

## Assumptions and scope
The space is real and exactly three-dimensional with the supremum norm. The upper third von Neumann–Jordan constant is the supremum of \(C^{(3)}\) over nonzero triples, while the upper modified constant restricts all three vectors to the unit sphere. No assertion is made here for complex scalars, for other dimensions beyond the comparison stated below, or for lower constants.

## Proof
Write
\[
a_j=\|x_j\|_\infty\quad (j=1,2,3),\qquad
S=a_1+a_2+a_3,
\qquad
Q=a_1^2+a_2^2+a_3^2.
\]
For fixed \((a_1,a_2,a_3)\), arrange the coordinates of \((x_1,x_2,x_3)\) as a \(3\times3\) matrix. The numerator of \(C^{(3)}\) is a convex function of this matrix on the box whose \(j\)-th column lies in \([-a_j,a_j]^3\): each summand is the maximum of three squares of linear forms. A convex function on a compact polytope is bounded above by its maximum on the vertices. Hence it is enough to consider coordinate rows of the form
\[
(\sigma_1a_1,\sigma_2a_2,\sigma_3a_3),\qquad \sigma_j\in\{-1,1\}.
\]
After identifying a sign row with its negative, there are four projective sign classes,
\[
(1,1,1),\quad (1,1,-1),\quad (1,-1,1),\quad (1,-1,-1).
\]
The three coordinate rows therefore use one, two, or three distinct projective classes.

If only one class occurs, direct expansion gives numerator \(4Q\), so the quotient is \(1\).

If two classes occur, symmetry reduces to the pair \((1,1,1)\), \((1,1,-1)\). Two sign sums have norm \(S\), while the other two have a common norm
\[
M=\max\{|S-2a_1|,|S-2a_2|\}.
\]
For either candidate inside this maximum,
\[
S^2+(S-2a_i)^2
=2\bigl((S-a_i)^2+a_i^2\bigr)
\le 4Q,
\]
because the square of the sum of the other two radii is at most twice the sum of their squares. Thus this case gives at most \(2\).

Suppose finally that three distinct projective classes occur. The three covered sign sums have norm \(S\). If
\[
m=\min\{a_1,a_2,a_3\},
\]
then the remaining sign sum has norm exactly \(S-2m\). Reorder so that \(m=a_1\le a_2,a_3\). For fixed \(a_1\) and \(u=a_2+a_3\), the numerator depends only on \(a_1\) and \(u\), while
\[
a_2^2+a_3^2\ge \frac{u^2}{2}.
\]
Hence the quotient is maximized when \(a_2=a_3=t\). Put \(r=a_1/t\in[0,1]\). The quotient becomes
\[
f(r)=\frac{r^2+2r+4}{r^2+2}.
\]
Let
\[
C=\frac{3+\sqrt3}{2},\qquad r_0=\sqrt3-1.
\]
A direct factorization gives
\[
C-f(r)=
\frac{(1+\sqrt3)(r-r_0)^2}{2(r^2+2)}\ge0.
\]
Thus \(\overline C_{NJ}^{(3)}(\ell_\infty^3)\le C\), with equality at \(r=r_0\). The displayed triple realizes exactly those radii and three distinct projective classes, so the bound is attained.

For the modified constant, \(a_1=a_2=a_3=1\). At a vertex row, exactly one of the four projective sign sums has squared magnitude \(9\) and the other three have squared magnitude \(1\). Three coordinate rows can cover at most three projective classes, so the numerator is at most
\[
3\cdot9+1=28.
\]
Three distinct classes attain this value. Since the denominator is \(12\),
\[
\overline C_{mNJ}^{(3)}(\ell_\infty^3)=\frac{28}{12}=\frac73.
\]
Finally,
\[
\frac{3+\sqrt3}{2}-\frac73=\frac{3\sqrt3-5}{6}>0,
\]
which proves strict separation.

## Verification
The companion script `verify.py` uses only the Python standard library. It enumerates all \(4^3\) projective sign-row configurations for the modified problem, verifies the maximum numerator \(28\), checks the exact \(\mathbb Q(\sqrt3)\) equality witness for the unrestricted problem, and checks the coefficient identities behind the sharp square factorization. The analytic proof above, not the finite enumeration alone, supplies the unrestricted global upper bound.

## Relationship to prior work
Ciesielski and Płuciennik define the upper and upper modified \(n\)-th von Neumann–Jordan constants and prove the general inequalities
\[
\overline C_{mNJ}^{(n)}(X)\le \overline C_{NJ}^{(n)}(X)\le n.
\]
For \(\ell_\infty^m\), their Proposition 4 gives the maximal value \(n\) when \(m\ge2^{{n-1}}\); for \(n=3\), this starts at \(m=4\). Their stated result therefore does not determine the three-dimensional cube. A separate database record gives the modified constants of the square plane \(\ell_\infty^2\) for all orders, but it does not imply either value above for \(\ell_\infty^3\). The present calculation fills the dimension-three case and shows that unequal radii increase the third-order constant from \(7/3\) to \((3+\sqrt3)/2\).

## Limitations
The argument exploits the three-coordinate cube and the four projective sign classes specific to the third-order problem. It does not give a closed formula for arbitrary \(n\) and \(m\), and it does not classify all equality triples. The 2024 \((n,p)\)-generalization was located and its abstract inspected, but its full article was not available through the accessed route; its abstract describes exact calculations for \(\ell^p\), \(L^p\), and the \(\ell_\infty-\ell_1\) space rather than this finite cube.

## References
1. M. Ciesielski and R. Płuciennik, “On some modifications of n-th von Neumann–Jordan constant for Banach spaces,” arXiv:1811.01652, first public 5 November 2018; Banach Journal of Mathematical Analysis 14 (2020), 650–673, doi:10.1007/s43037-019-00033-1.
2. H. Li, X. Yang, and C. Yang, “On \((n,p)\)-th von Neumann–Jordan constants for Banach spaces,” Mathematical Inequalities & Applications 27 (2024), 583–600, doi:10.7153/mia-2024-27-40.
