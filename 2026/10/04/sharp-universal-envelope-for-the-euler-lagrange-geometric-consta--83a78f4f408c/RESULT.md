# Sharp universal envelope for the Euler–Lagrange geometric constant
## Finding
Let \(X\) be a real Banach space with \(\dim X\ge2\), and let \(\lambda,\mu>0\). For
\[
L_{YJ}(\lambda,\mu,X)=\sup_{(x,y)\ne(0,0)}
\frac{\|\lambda x+\mu y\|^2+\|\mu x-\lambda y\|^2}
{(\lambda^2+\mu^2)(\|x\|^2+\|y\|^2)},
\]
one has the sharp universal estimate
\[
L_{YJ}(\lambda,\mu,X)\le
1+\frac{2\lambda\mu}{\lambda^2+\mu^2}
=\frac{(\lambda+\mu)^2}{\lambda^2+\mu^2}.
\]
Moreover, equality holds exactly when \(J(X)=2\). Since \(J(X)<2\) is equivalent to uniform non-squareness, this gives the exact threshold
\[
X\text{ uniformly non-square}
\quad\Longleftrightarrow\quad
L_{YJ}(\lambda,\mu,X)<\frac{(\lambda+\mu)^2}{\lambda^2+\mu^2}.
\]
Thus the same parameter-dependent endpoint previously known for the unit-sphere variant \(L'_{YJ}\) is also the sharp endpoint for \(L_{YJ}\), even though \(L_{YJ}\) allows unequal input norms.

## Assumptions and scope
The scalars are real, \(X\) is a real Banach space of dimension at least two, and \(\lambda,\mu\) are strictly positive. The James constant is
\[
J(X)=\sup_{u,v\in S_X}\min\{\|u+v\|,\|u-v\|\}.
\]
No finite-dimensionality, reflexivity, smoothness, strict convexity, or attainment assumption is used. In particular, all equality statements for infinite-dimensional spaces are understood through the defining suprema, not through assumed maximizers.

## Proof
Write \(a=\|x\|\), \(b=\|y\|\), and \(S=\lambda^2+\mu^2\). By the triangle inequality,
\[
\|\lambda x+\mu y\|\le \lambda a+\mu b,
\qquad
\|\mu x-\lambda y\|\le \mu a+\lambda b.
\]
Hence
\[
\begin{aligned}
\|\lambda x+\mu y\|^2+\|\mu x-\lambda y\|^2
&\le (\lambda a+\mu b)^2+(\mu a+\lambda b)^2\\
&=S(a^2+b^2)+4\lambda\mu ab\\
&\le \left(S+2\lambda\mu\right)(a^2+b^2),
\end{aligned}
\]
where the last step is \(2ab\le a^2+b^2\). Dividing by \(S(a^2+b^2)\) proves
\[
L_{YJ}(\lambda,\mu,X)\le 1+\frac{2\lambda\mu}{S}.
\]

It remains to characterize equality. Suppose first that \(J(X)=2\). There are \(u_n,v_n\in S_X\) such that both \(\|u_n+v_n\|\to2\) and \(\|u_n-v_n\|\to2\). Choose norm-one support functionals \(f_n,g_n\in X^*\) satisfying
\[
f_n(u_n+v_n)=\|u_n+v_n\|,
\qquad
g_n(u_n-v_n)=\|u_n-v_n\|.
\]
Because \(f_n(u_n),f_n(v_n)\le1\) and their sum tends to \(2\), both tend to \(1\). Likewise \(g_n(u_n)\to1\) and \(g_n(v_n)\to-1\). Therefore
\[
\|\lambda u_n+\mu v_n\|\ge \lambda f_n(u_n)+\mu f_n(v_n)\to\lambda+\mu,
\]
and
\[
\|\mu u_n-\lambda v_n\|\ge \mu g_n(u_n)-\lambda g_n(v_n)\to\lambda+\mu.
\]
Using \(\|u_n\|=\|v_n\|=1\) in the defining quotient shows that its values tend to
\[
\frac{2(\lambda+\mu)^2}{2S}=rac{(\lambda+\mu)^2}{S},
\]
so the universal upper bound is attained as a supremum.

Conversely, suppose
\[
L_{YJ}(\lambda,\mu,X)=\frac{(\lambda+\mu)^2}{S}.
\]
Choose \((x_n,y_n)\) whose defining quotients tend to this value, and rescale each pair so that
\[
\|x_n\|^2+\|y_n\|^2=2.
\]
Put \(a_n=\|x_n\|\), \(b_n=\|y_n\|\). The scalar part of the upper-bound proof gives
\[
\frac{\|\lambda x_n+\mu y_n\|^2+\|\mu x_n-\lambda y_n\|^2}{2S}
\le 1+\frac{2\lambda\mu}{S}a_nb_n
\le 1+\frac{2\lambda\mu}{S}.
\]
Convergence to the right endpoint forces \(a_nb_n\to1\). Since \(a_n^2+b_n^2=2\), it follows that \(a_n\to1\) and \(b_n\to1\).

Set
\[
A_n=\lambda a_n+\mu b_n,
\qquad
B_n=\mu a_n+\lambda b_n,
\]
and
\[
r_n=\|\lambda x_n+\mu y_n\|,
\qquad
s_n=\|\mu x_n-\lambda y_n\|.
\]
The total triangle-inequality defect
\[
(A_n^2-r_n^2)+(B_n^2-s_n^2)
\]
is nonnegative and tends to zero, because the upper scalar envelope and the actual quotient have the same limit. Each summand therefore tends to zero. Since \(A_n,B_n\to\lambda+\mu>0\), we have \(A_n-r_n\to0\) and \(B_n-s_n\to0\).

For all sufficiently large \(n\), let \(F_n\in S_{X^*}\) norm \(\lambda x_n+\mu y_n\). With \(u_n=x_n/a_n\), \(v_n=y_n/b_n\),
\[
A_n-r_n=
\lambda a_n\bigl(1-F_n(u_n)\bigr)
+\mu b_n\bigl(1-F_n(v_n)\bigr)\to0.
\]
Both summands are nonnegative and their coefficients stay bounded away from zero, hence \(F_n(u_n)\to1\) and \(F_n(v_n)\to1\). Thus
\[
\|u_n+v_n\|\ge F_n(u_n)+F_n(v_n)\to2.
\]
Similarly, norm \(\mu x_n-\lambda y_n\) by \(G_n\in S_{X^*}\). Then
\[
B_n-s_n=
\mu a_n\bigl(1-G_n(u_n)\bigr)
+\lambda b_n\bigl(1+G_n(v_n)\bigr)\to0,
\]
so \(G_n(u_n)\to1\) and \(G_n(v_n)\to-1\). Consequently
\[
\|u_n-v_n\|\ge G_n(u_n)-G_n(v_n)\to2.
\]
Therefore \(J(X)=2\). This proves the equality characterization and, by the standard equivalence \(J(X)<2\) with uniform non-squareness, the asserted strict-threshold criterion.

## Verification
The proof was reconstructed directly from the definitions. The two nontrivial limit steps were checked separately: endpoint convergence forces \(a_nb_n\to1\) under \(a_n^2+b_n^2=2\), and vanishing of a sum of nonnegative triangle-inequality defects forces each defect to vanish. Hahn–Banach support functionals then recover simultaneous near-antipodality of the normalized pair. No finite experiment, numerical approximation, or assumed attainment of a supremum is used.

Boundary checks agree with known cases. If \(\lambda=\mu\), the endpoint is \(2\), reducing to the classical non-square endpoint of the von Neumann–Jordan constant. For unequal parameters the endpoint is strictly below \(2\). If \(X\) is Hilbert, the Euler–Lagrange identity gives \(L_{YJ}=1\), strictly below the endpoint for positive \(\lambda,\mu\).

## Relationship to prior work
Liu and Li introduced \(L_{YJ}\) in 2021 and recorded only the universal estimate \(1\le L_{YJ}\le2\). Their Theorem 5 gives a sufficient condition for uniform non-squareness using a different parameter-dependent threshold, and their examples obtain sharper special conclusions in some parameter regimes. Their later unit-sphere variant \(L'_{YJ}\) has the sharp upper endpoint \(1+2\lambda\mu/(\lambda^2+\mu^2)\) and characterizes uniform non-squareness at that endpoint.

The distinction is substantive: \(L_{YJ}\) optimizes over unequal input norms as well as directions, whereas \(L'_{YJ}\) fixes both inputs on the unit sphere. Thus the known \(L'_{YJ}\) theorem does not by itself imply the present universal bound or rule out an unequal-norm maximizer. The proof above shows that unequal norms can never exceed the unit-sphere endpoint, and that approaching the endpoint actually forces the input norms to become equal and the normalized vectors to witness \(J(X)=2\).

Yang and Yang (2024) still summarize the known bounds as \(L_{YJ}\le2\) and \(L'_{YJ}\le1+2\lambda\mu/(\lambda^2+\mu^2)\), before proving a different comparison with a generalized James constant. Yang, Li, and Yang (2024) likewise state those bounds and compute exact values only for the regular octagon space. These inspected later sources therefore do not subsume the universal envelope and equality characterization above.

## Limitations
The theorem concerns real Banach spaces and strictly positive \(\lambda,\mu\). No claim is made here about complex analogues under alternative definitions of the geometric constants. The literature search cannot exclude an obscure or unindexed independent occurrence of the same elementary inequality or equality characterization. The result is an exact structural theorem, not a quantitative estimate of how far \(L_{YJ}\) lies below the endpoint when \(J(X)<2\).

## References
1. Q. Liu and Y. Li, “On a New Geometric Constant Related to the Euler-Lagrange Type Identity in Banach Spaces,” *Mathematics* 9 (2021), 116. DOI: 10.3390/math9020116. First published 2021-01-07.
2. Q. Liu, C. Zhou, M. Sarfraz, and Y. Li, “On New Moduli Related to the Generalization of the Parallelogram Law,” *Bulletin of the Malaysian Mathematical Sciences Society* 45 (2022), 307–321. DOI: 10.1007/s40840-021-01196-7.
3. X. Yang and C. Yang, “An inequality between \(L_{YJ}(\lambda,\mu,X)\) constant and generalized James constant,” *Mathematical Inequalities & Applications* 27 (2024), 571–581. DOI: 10.7153/mia-2024-27-39.
4. X. Yang, H. Li, and C. Yang, “On the \(L_{YJ}(\lambda,\mu,X)\) constant for the regular octagon space,” *Filomat* 38 (2024), 1583–1593. DOI: 10.2298/FIL2405583Y.
