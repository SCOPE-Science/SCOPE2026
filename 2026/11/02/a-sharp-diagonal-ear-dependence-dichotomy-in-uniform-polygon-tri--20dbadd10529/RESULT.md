# A sharp diagonal–ear dependence dichotomy in uniform polygon triangulations

## Finding

Let \(n\ge 2\), and choose uniformly one of the \(C_n\) triangulations of a fixed, labeled convex polygon with \(n+2\) vertices, where \(C_n=\binom{2n}{n}/(n+1)\). Let \(E\) be the number of *ears*: triangles of the triangulation meeting two sides of the original polygon. Fix an internal diagonal \(d\), and let \(I_d\) indicate its inclusion. This diagonal separates polygons with \(a+2\) and \(b+2\) vertices, with integers \(a,b\ge1\) and \(a+b=n\).

**Exact conditional law.** Define, for each integer \(r\ge1\),
\[
H_r(z)=\sum_{j=0}^{\lfloor(r+1)/2\rfloor}
 \binom{r-j+1}{j}\frac{C_{r-j}}{C_r}(z-1)^j.
\]
Then
\[
\mathbb E[z^E\mid I_d=1]=H_a(z)H_b(z),\qquad
\Pr(I_d=1)=\frac{C_aC_b}{C_n}.
\]
Here the two independent factors count ear tips internal to the two boundary arcs separated by \(d\); neither endpoint of \(d\) can be an ear tip of the original polygon.

**Complete finite-size covariance classification.** The conditional-mean shift is
\[
\begin{aligned}
\Delta_{n;a,b}
&=\mathbb E[E\mid I_d=1]-\mathbb E[E]\\
&=\frac{2n^2+n-1-(n+7)ab}{(2a-1)(2b-1)(2n-1)}.
\end{aligned}
\]
Consequently
\[
\operatorname{Cov}(E,I_d)=\frac{C_aC_b}{C_n}\,\Delta_{n;a,b}.
\]
For \(n=2,3\) all such covariances vanish. For **every** \(n\ge4\), the covariance is strictly positive when \(\min(a,b)=1\) (the diagonal cuts off an ear triangle), and strictly negative when \(a,b\ge2\) (neither side is a triangle).

**A sharp obstruction to upgrading means to stochastic ordering.** For a convex octagon, take a diagonal with \(a=b=3\). Writing probabilities in increasing order of ear counts \(2,3,4\), respectively,
\[
\Pr(E=2,3,4)=\left(\frac{16}{33},\frac{16}{33},\frac1{33}\right),
\quad
\Pr(E=2,3,4\mid I_d=1)=\left(\frac{16}{25},\frac8{25},\frac1{25}\right).
\]
Thus conditioning on this long diagonal decreases the probability of at least three ears, from \(17/33\) to \(9/25\), but **increases** the probability of four ears, from \(1/33\) to \(1/25\). Negative covariance here is not negative stochastic dependence of the full ear-count distribution.

## Assumptions and scope

The polygon is strictly convex, with distinct cyclically labeled vertices. The sampling measure is uniform on its noncrossing diagonal triangulations. Only genuine internal diagonals \(d\) are considered. A triangle is an ear exactly when it uses two *original* polygon boundary sides; using the conditioned diagonal as a boundary side of a subpolygon does not make it an ear of the original polygon. The parameter \(n\) counts the Catalan index, not the polygon's vertex count. The results are exact for all integers \(n\ge2\) and \(a,b\ge1\) satisfying \(a+b=n\). No claim of stochastic ordering beyond the explicitly stated octagon counterexample is made.

## Proof

1. **Catalan decomposition at a diagonal.** There are \(C_n\) triangulations of the \((n+2)\)-gon. Those containing \(d\) are obtained by independently triangulating its two resulting polygons, giving \(C_aC_b\) possibilities. Conditioned on \(I_d=1\), the two subtriangulations are independent and uniform. Since a diagonal endpoint touches a triangle on each side of \(d\), it cannot be an original ear tip. Every other vertex lies strictly inside exactly one of the two boundary arcs, and is an original ear tip if and only if it is an ear tip in that subpolygon.

2. **Marked ear tips along a boundary arc.** Fix one subpolygon with \(r+2\) vertices and distinguish its diagonal side, whose two endpoints are forbidden as original ear tips. The remaining \(r\) vertices form an ordered path. A specified set of \(j\) such vertices can simultaneously be ear tips exactly when no two are adjacent in that path. There are \(\binom{r-j+1}{j}\) such sets. After deleting their \(j\) ear triangles, the remaining polygon has \(r+2-j\) vertices and admits \(C_{r-j}\) triangulations. Thus, if \(U_r\) counts permitted ear tips,
\[
\mathbb E\binom{U_r}{j}=\binom{r-j+1}{j}\frac{C_{r-j}}{C_r}.
\]
Expanding \(z^{U_r}=(1+(z-1))^{U_r}\) gives \(H_r\), and the two independent subpolygons yield the conditional product formula.

3. **Unconditional marked ears.** For \(N=n+2\) vertices on a cycle, the number of size-\(j\) sets with no cyclically adjacent vertices is \(\frac{N}{N-j}\binom{N-j}{j}\). Selecting and deleting these ears leaves a polygon with \(N-j\) vertices, so
\[
\mathbb E\binom{E}{j}
=\frac{N}{N-j}\binom{N-j}{j}\frac{C_{n-j}}{C_n},
\qquad 0\le j\le\lfloor N/2\rfloor.
\]
The borderline \(N=4,j=2\) uses the harmless convention \(C_0=1\); direct enumeration gives the same result. In particular, with \(p_r=C_{r-1}/C_r=(r+1)/(2(2r-1))\),
\[
\mathbb E[E]=(n+2)p_n,
\qquad
\mathbb E[E\mid I_d=1]=ap_a+bp_b.
\]

4. **Sign classification.** Substituting the Catalan ratio and \(a+b=n\) gives the displayed rational formula for \(\Delta_{n;a,b}\). Its denominator is positive. If \(a=1\) or \(b=1\), the numerator equals \((n-2)(n-3)\). For \(a,b\ge2\), the elementary bound \(ab\ge2(n-2)\) gives the upper bound \(9(3-n)<0\) on the numerator for \(n\ge4\). The cases \(n=2,3\) yield numerator zero. Finally \(\operatorname{Cov}(E,I_d)=\Pr(I_d=1)(\mathbb E[E\mid I_d=1]-\mathbb E[E])\).

5. **Octagon limit of monotonicity.** With \(r=3\), the marked-ear polynomial is \(H_3(z)=(4z+z^2)/5\), so the diagonal-conditioned octagon polynomial is \(H_3(z)^2\). The unconditional marked-ear formula gives \((16z^2+16z^3+z^4)/33\). Comparison of their coefficients and tails yields the stated strict opposite signs at thresholds three and four.

## Verification

Run `python verify.py` using Python 3's standard library. It expands the exact marked-ear factorial moments to probabilities, checks normalization, conditional means and covariance signs for \(2\le n\le80\), and independently enumerates all noncrossing triangulations of polygons with four through eleven vertices. For every admissible fixed diagonal in those polygons, it compares the enumerated conditional distribution against \(H_aH_b\), and it checks the octagon tails exactly. This run returned `PASS 13138 exact assertions; 6916 triangulations explicitly enumerated`. These finite calculations check the algebra and definitions; the proof of the all-size statement is the marked-ear bijection and sign argument above.

## Relationship to prior work

Hurtado and Noy established the number of triangulations with a prescribed *total* number of ears, and Asinowski and Regev studied triangulations with few ears and the count of triangulations sharing or avoiding prescribed diagonals. Their enumerations provide context and ingredients but do not state the diagonal-conditioned ear law or the all-sizes positive/negative covariance dichotomy. Mansour and Rastegar subsequently gave a systematic treatment of marginal triangle-weight sums, including the ear-count probability-generating function and mean; neither its displayed ear formulas nor its invariant-weight expectation theorem specifies the joint law with a fixed labeled diagonal. The present result keeps those previously known marginal and Catalan facts separate from the conditional law, strict sign classification, and octagon stochastic-order obstruction. Related general recurrences could encode the finite joint counts after further work, so historical novelty requires independent evaluation.

## Limitations

Historical priority has not been independently established. The 1996 Hurtado–Noy paper's accessible abstract and later detailed citations were compared, but its full text could not be inspected. A more general unlocated multivariate enumeration may imply part of the stated conditional law. The octagon example refutes a uniform stochastic-order extension but does not classify all conditional tail signs for every polygon and diagonal. No asymptotic normality or geometric claims about nonconvex polygons are asserted.

## References

- A. Asinowski and A. Regev, *Triangulations with few ears: symmetry classes and disjointness*, original public arXiv submission September 3, 2013, [arXiv:1309.0743](https://arxiv.org/abs/1309.0743), especially the introduction and Sections 2–3.
- F. Hurtado and M. Noy, *Ears of triangulations and Catalan numbers*, Discrete Mathematics **149** (1996), 319–324, [doi:10.1016/0012-365X(94)00331-C](https://doi.org/10.1016/0012-365X(94)00331-C). The original first-public date was not independently established.
- T. Mansour and R. Rastegar, *On typical triangulations of a convex \(n\)-gon*, original public arXiv submission November 11, 2019, [arXiv:1911.04025](https://arxiv.org/abs/1911.04025), especially Theorem 1.1 and Lemma 1.4.
