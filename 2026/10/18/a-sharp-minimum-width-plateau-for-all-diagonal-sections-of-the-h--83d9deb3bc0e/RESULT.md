# A sharp minimum-width plateau for all diagonal sections of the hypercube

## Finding

For every integer \(n\ge4\) and every real \(0<t<n\), consider the intrinsic \((n-1)\)-dimensional Euclidean polytope
\[
K_{n,t}=\{x\in[0,1]^n:\sum_{i=1}^n x_i=t\}.
\]
Put \(q_n=\lfloor n^2/4\rfloor\), \(m(t)=\min\{t,n-t\}\), and \(\tau_n=\sqrt{q_n/(n-1)}\). Its least Euclidean projection width is exactly
\[
\boxed{w(K_{n,t})=\min\left\{\sqrt{\frac n{n-1}},\ m(t)\sqrt{\frac n{q_n}}\right\}.}
\]
In particular, \(1<\tau_n<n/2\), and the width is strictly increasing on \((0,\tau_n)\), constant on \([\tau_n,n-\tau_n]\), and strictly decreasing on \((n-\tau_n,n)\). This is a genuine plateau across continuously varying, generally noncongruent cube sections.

Every least-width unit normal lies in \(H=\{u\in\mathbb R^n:\sum_i u_i=0\}\) and is proportional, up to permutation and sign, to a vector constant on each side of a coordinate partition. In the open outer regimes \(m(t)<\tau_n\), the two block sizes are exactly \(\lfloor n/2\rfloor\) and \(\lceil n/2\rceil\); in the open central regime \(m(t)>\tau_n\), they are exactly \(1\) and \(n-1\). At either transition \(m(t)=\tau_n\), precisely those two families minimize. No other directions minimize.

## Assumptions and scope

All widths use the ordinary induced Euclidean norm in the affine hyperplane \(\sum_i x_i=t\), not ambient normals perpendicular to that hyperplane. Specifically, for unit \(u\in H\), let \(\omega_K(u)=\max_{x\in K}\langle u,x\rangle-\min_{x\in K}\langle u,x\rangle\); then \(w(K)=\min_{\|u\|_2=1,\,u\in H}\omega_K(u)\). We assume \(n\ge4\), \(0<t<n\), so every section has dimension \(n-1\). Normal directions are oriented antipodally equivalently, and their families are described up to coordinate permutations. The discontinuities concern the *minimizing normal orbit*, not the continuous width function.

## Proof

**Step 1: a general sharp reduction for permutahedra.** Let \(a=(a_1,\dots,a_n)\) be any nonconstant vector whose coordinates are ordered \(a_1\ge\cdots\ge a_n\), and let \(Q(a)=\operatorname{conv}\{(a_{\sigma(1)},\ldots,a_{\sigma(n)}):\sigma\in S_n\}\). Rearrangement allows us, after permuting coordinates of a candidate normal, to take \(u_1\le\cdots\le u_n\). Set \(\delta_j=u_{j+1}-u_j\ge0\). Because \(u\in H\), it admits the exact expansion
\[
 u=\sum_{j=1}^{n-1}\delta_j v_j,
 \qquad (v_j)_i=\begin{cases}-(n-j)/n&i\le j,\\j/n&i>j,\end{cases}
 \qquad\|v_j\|_2=\sqrt{j(n-j)/n}.
\]
The rearrangement inequality gives
\[
\omega_{Q(a)}(u)=\sum_{j=1}^{n-1}\delta_j B_j,
\quad B_j=\sum_{i=1}^{j}a_i-\sum_{i=n-j+1}^{n}a_i>0.
\]
(For a nonconstant sorted vector every \(B_j\) is positive.) Therefore, by the triangle inequality,
\[
\frac{\omega_{Q(a)}(u)}{\|u\|_2}\ge
\frac{\sum_j\delta_j B_j}{\sum_j\delta_j\|v_j\|_2}\ge
\min_{1\le j<n}\frac{B_j}{\|v_j\|_2}.
\]
Every single-step normal \(u=v_j/\|v_j\|_2\) realizes its indicated ratio. Conversely, two distinct \(v_j\) are never positive-collinear; the Euclidean triangle inequality is strict whenever at least two \(\delta_j\) are positive. Hence **every** minimizing normal is a two-level vector \(v_j\) with a minimizing cut size \(j\), including all equality cases.

**Step 2: vertices of the cube section.** At a vertex of \(K_{n,t}\), at most one coordinate can lie strictly between zero and one, since two fractional coordinates admit opposite infinitesimal changes while staying in the section. With \(k=\lfloor t\rfloor\), \(r=t-k\), the vertices are exactly the distinct permutations of \((1,\ldots,1,r,0,\ldots,0)\) with \(k\) ones and \(r\) included only if nonzero. Thus Step 1 applies.

**Step 3: exact cut widths.** For a subset of \(j\) coordinates, maximizing their sum subject to the box and total constraints yields \(\min\{j,t\}\); minimizing it yields \(\max\{0,t-(n-j)\}\). Consequently,
\[
 B_j=\min\{j,t\}-\max\{0,t-(n-j)\}
 =\min\{j,n-j,t,n-t\}.
\]
Since \(B_j=B_{n-j}\), write \(b=\lfloor n/2\rfloor\), \(m=\min(t,n-t)\); the exact candidate widths for \(1\le j\le b\) are
\[
\sqrt n\frac{\min\{j,m\}}{\sqrt{j(n-j)}}
=\sqrt n\min\left\{\sqrt{\frac j{n-j}},\frac m{\sqrt{j(n-j)}}\right\}.
\]
For integer \(1\le j\le b\), the first expression is *strictly increasing*, so its minimum occurs only at \(j=1\). The second is *strictly decreasing*, so its minimum occurs only at \(j=b\), where \(b(n-b)=q_n\). Taking the minimum of these two minima yields
\[
 w(K_{n,t})=\sqrt n\min\left\{\frac1{\sqrt{n-1}},\frac{m}{\sqrt{q_n}}\right\}.
\]
When \(m<\tau_n\), the winning \(j=b\) branch is realized with \(B_b=m\). When \(m>\tau_n\), the winning \(j=1\) branch is realized with \(B_1=1\) because \(\tau_n>1\). At equality both are realized. The strict monotonicities and the strict triangle-equality classification of Step 1 exclude any other minimizing cut sizes or normal types. Finally \(q_n>n-1\) and \(q_n<(n-1)n^2/4\) for \(n\ge4\), giving \(1<\tau_n<n/2\). This proves every assertion.

## Verification

The attached executable \(\texttt{checker.py}\) performs independent exhaustive exact-rational cut-support comparisons against explicit vertex permutations for dimensions \(4\) through \(8\), checks candidate minimizing widths, and tests independently generated random unit directions. It also tests the strict phase comparisons in dimensions \(4\) through \(89\). These are finite checks supporting the formulas; all-dimensional validity follows only from the proof above.

## Relationship to prior work

Har-Peled and Robson [1] prove the minimum width of a regular simplex and describe balanced two-level extremal directions. Here this appears only at the endpoint section \(t=1\) (or \(t=n-1\)); that discrete result does not determine how widths and minimizing directions vary at nonintegral \(t\). The integer-rank hypersimplex formula covers only \(t\in\mathbb Z\). The present statement treats all real levels with exact irrational thresholds and complete equality cases. Ang et al. [2] work with the identical fixed-sum cube section in a Euclidean projection-optimization problem but do not address its minimum projection width. The elementary rearrangement principle used in Step 1 is classical; no priority is claimed for that principle.

## Limitations

This is an intrinsic Euclidean-width theorem, not a formula for arbitrary norms, anisotropic boxes, projections onto nonlinear manifolds, or the entire directional-width distribution. No full global literature-exhaustiveness or independent review is asserted. An equivalent earlier derivation under the terminology of permutahedra or generalized hypersimplices may exist. The finite checker does not replace the analytic quantifier argument.

## References

[1] Sariel Har-Peled and Eliot W. Robson, *On the Width of the Regular n-Simplex*, arXiv:2301.02616v1 (publicly submitted 2023-01-06). https://arxiv.org/abs/2301.02616

[2] Andersen Ang, Jianzhu Ma, Nianjun Liu, Kun Huang, and Yijie Wang, *Fast Projection onto the Capped Simplex with Applications to Sparse Regression in Bioinformatics*, NeurIPS 2021. https://papers.neurips.cc/paper/2021/file/52aaa62e71f829d41d74892a18a11d59-Paper.pdf
