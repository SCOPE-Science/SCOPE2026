# Sharp negative-type exponent for incidence metrics of generalized quadrangles

## Finding
Let \(\mathcal Q\) be any finite generalized quadrangle of order \((q,q)\), \(q\ge2\), with point-line incidence graph \(G\) and graph distance \(d\). Put
\[
F_q(p)=q(q+1)2^p+q^3 4^p-(q+1)-q^2(q+1)3^p.
\]
There is exactly one root \(\alpha_q>0\) of \(F_q\), and \(0<\alpha_q<\log_2(1+1/q)\). For real \(p\ge0\), the matrix with diagonal zero and off-diagonal entries \(d(u,v)^p\) is conditionally negative definite if and only if \(p\le\alpha_q\). It is strictly conditionally negative definite for \(0\le p<\alpha_q\). At \(p=\alpha_q\), the centered negative-distance form has rank \(2(q+1)(q^2+1)-2\); this is the minimum squared-Euclidean embedding dimension. Along admissible orders tending to infinity,
\[
\alpha_q=\frac{1}{q^3\log(4/3)}+O(q^{-4}).
\]
By Schoenberg's criterion, \(\exp(-t d(u,v)^p)\) is positive semidefinite for every \(t>0\) exactly in the same exponent interval.

## Assumptions and scope
A generalized quadrangle of order \((q,q)\) has \(v=(q+1)(q^2+1)\) points and the same number of lines; each point lies on \(q+1\) lines, and each line contains \(q+1\) points. Distinct points have graph distance two if collinear and four otherwise. Distinct lines have distance two if concurrent and four otherwise. Point-to-line distance is one for incidence and three for nonincidence. The claim is conditional on existence; it does not posit a generalized quadrangle for every integer \(q\). It includes nonclassical realizations sharing these incidence axioms. At exponent zero, each positive off-diagonal distance is raised to zero and diagonal entries remain zero.

## Proof
Write \(N\) for the \(v\times v\) point-line incidence matrix, \(A=NN^\top-(q+1)I\), and \(A'=N^\top N-(q+1)I\). The collinearity graph is strongly regular with parameters \((v,q(q+1),q-1,q+1)\). Its eigenvalues are \(q(q+1)\), \(q-1\), and \(-(q+1)\). Thus \(N\) has singular values \(q+1\), \(\sqrt{2q}\), and zero on the corresponding sectors. These conclusions also follow directly by counting a common line through collinear pairs and a unique connecting point-line path for noncollinear pairs.

Put \(a=2^p\), \(b=3^p\), \(c=4^p\) and let \(J\) denote the all-ones matrix of order \(v\). Relative to point and line coordinates, the powered-distance matrix is
\[
D_p=\begin{pmatrix}(a-c)A+c(J-I)&(1-b)N+bJ\\(1-b)N^\top+bJ&(a-c)A'+c(J-I)\end{pmatrix}.
\]
On the total-sum-zero subspace, it has four kinds of spectral values. The point-versus-line constant vector has eigenvalue
\[
L_c=q(q+1)a+q^3c-(q+1)-q^2(q+1)b=F_q(p).
\]
For each \(q-1\) eigenvector of the collinearity graph, the paired singular-vector sector has eigenvalues
\[
L_\pm=(q-1)a-qc\pm\sqrt{2q}(b-1).
\]
On the \(-(q+1)\) eigenvectors, where \(N\) vanishes, the remaining value is
\[
L_0=qc-(q+1)a.
\]
All these spectral values must be nonpositive for conditional negative definiteness. The global constant is removed and is not an additional obstruction.

Set \(x=2^p\) and \(\gamma=\log_2 3\), with \(1<\gamma<8/5\). The constant-sector eigenvalue becomes
\[
F_q=q^3x^2+q(q+1)x-q^2(q+1)x^\gamma-(q+1).
\]
At \(x=1\) it equals \(-1\), whereas
\[
F_q(1+1/q)=q(q+1)[q+2-q(1+1/q)^\gamma]>0.
\]
The strict inequality follows from convexity of \((1+u)^\gamma\) on \([0,1/2]\): its chord satisfies \((1+u)^\gamma<1+2u\), since \((3/2)^\gamma<2\). Moreover for every \(x\ge1\),
\[
F_q''(x)=2q^3-\gamma(\gamma-1)q^2(q+1)x^{\gamma-2}>0,
\]
using \(\gamma(\gamma-1)<24/25\) and \(q\ge2\); also \(F_q'(1)=q^3(2-\gamma)+q^2(1-\gamma)+q>0\). Consequently \(F_q\) is strictly increasing for \(x\ge1\), with exactly one zero \(\alpha_q\) in the announced interval and strictly positive thereafter.

For \(0\le p\le\log_2(1+1/q)\), put \(u=2^p-1\), so \(0\le u\le1/q\). Then
\[
L_0=(1+u)[qu-1]<0
\]
for \(u<1/q\), and
\[
L_+=-1-(q+1)u-qu^2+\sqrt{2q}((1+u)^\gamma-1).
\]
The elementary bound \((1+u)^\gamma-1\le(8/5)u(1+1/q)\) gives
\[
L_+\le-1+u\bigl[(8/5)\sqrt{2q}(1+1/q)-(q+1)\bigr]-qu^2<0.
\]
Indeed the coefficient in brackets is strictly less than \(q\), since \((8/5)\sqrt{2q}(1+1/q)<2q+1\) for all \(q\ge2\) (at \(q=2\) this is \(24/5<5\), and the ratio of the two sides decreases with \(q\)). As \(L_-\le L_+\), all nonconstant paired sectors are strictly negative at the root \(\alpha_q\). Thus the only new zero at the endpoint is the point-versus-line constant vector. For larger \(p\), \(F_q(p)>0\), proving failure of conditional negative definiteness globally, not merely near the root.

Write \(v=(q+1)(q^2+1)\). The Schoenberg Gram matrix \(-\tfrac12 H D_pH\), with \(H=I-J_{2v}/(2v)\), has rank \(2v-1\) below the threshold and \(2v-2\) at the threshold. Finally \(F_q(0)=-1\), \(F_q'(0)=q^3\log(4/3)-q^2\log(3/2)+q\log 2\), and uniformly in the root interval \(F_q''(p)=O(q^3)\). The mean-value and Taylor estimates give \(\alpha_q=1/[q^3\log(4/3)]+O(q^{-4})\).

## Verification
The standalone `gq_check.py` constructs actual symplectic generalized quadrangles over prime fields \(q=2\) and \(q=3\), checks their incidence counts and graph-distance matrices, and tests the centered powered-distance eigenvalue signs below, at, and above the predicted root. It also reports the root asymptotics at additional parameter values. Execute `python gq_check.py` with NumPy and SciPy installed. Direct finite tests corroborate, but do not substitute for, the proof for every admissible \(q\).

## Relationship to prior work
Sánchez gives a general finite-metric supremal negative-type criterion; the present result instead resolves the exact threshold, endpoint rank, and large-order asymptotic for all generalized-quadrangle incidence metrics. Abreu et al. discuss finite generalized quadrangles as regular girth-eight incidence graphs and supply geometric context, not this powered-distance classification. Projective-plane incidence graphs are generalized triangles of girth six and have different distance sectors; their sharp negative-type thresholds do not imply this formula.

## Limitations
Existence is assumed for the specified generalized-quadrangle order. The result does not classify other generalized polygons or nonbalanced order pairs. Source comparison was bounded; an equivalent statement in older distance-regular-graph or association-scheme literature remains possible. This is not independently audited.

## References
1. J. Sánchez, *On supremal p-negative type of a finite metric space*, arXiv:1108.0451v1, first public 2011-08-02, https://arxiv.org/abs/1108.0451 .
2. M. Abreu, G. Araujo-Pardo, C. Balbuena, D. Labbate, G. Salas, *Families of small regular graphs of girth 7*, arXiv:1211.2672v1, first public 2012-11-12, https://arxiv.org/abs/1211.2672 .
