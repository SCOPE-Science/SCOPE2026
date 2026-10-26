# Sharp coordinatewise stability and a two-parameter phase boundary for extended Lorentz-cone projection

## Finding

For all integers \(p,q\ge1\), consider the closed convex extended Lorentz cone
\[
L_{p,q}=\{(x,u)\in\mathbb R^p\times\mathbb R^q:\ x_i\ge\|u\|_2\text{ for every }1\le i\le p\}.
\]
Let \(\Pi_{p,q}\) be its **Euclidean nearest-point projection**, while input and output distances are measured in the ordinary coordinate maximum norm \(\|\cdot\|_\infty\). Define the global Lipschitz modulus
\[
\Lambda_{p,q}=\sup_{z\ne w}\frac{\|\Pi_{p,q}(z)-\Pi_{p,q}(w)\|_\infty}{\|z-w\|_\infty}.
\]
For \(q\ge2\), let
\[
H_q=\max_{0\le a\le1}\left\{a-a^2+\sqrt{q-1}\,a\sqrt{1-a^2}\right\},\qquad H_1=0.
\]
Then the exact sharp constant in all dimensions is
\[
\boxed{\Lambda_{p,q}=1+\max\left\{\frac{\sqrt q-1}{2},\frac{p}{p+1}H_q\right\}.}
\]
In particular, \(\Pi_{p,q}\) is nonexpansive in coordinate maximum norm **if and only if** \(q=1\). For \(q\ge2\), \(H_q\) has a unique maximizer \(a_q\in(0,1)\), characterized by
\[
1-2a_q+\sqrt{q-1}\,\frac{1-2a_q^2}{\sqrt{1-a_q^2}}=0.
\]
Put \(A_q=(\sqrt q-1)/2\). Since \(H_q>A_q\) for all \(q\ge2\), the two possible most sensitive output groups switch at the unique *real* boundary
\[
\boxed{p_*(q)=\frac{A_q}{H_q-A_q}.}
\]
The maximizing derivative row is a scalar-coordinate row when \(p<p_*(q)\), a vector-coordinate row when \(p>p_*(q)\), and both types when equality holds. This criterion is applied only to integer \(p\ge1\). The boundary has the asymptotic behavior
\[
p_*(q)\sim\sqrt{q/2}\quad(q\to\infty).
\]
Thus, for fixed \(p\), the scalar-output mechanism eventually dominates as \(q\) increases; for fixed \(q\ge2\), the vector-output mechanism eventually dominates as \(p\) increases.

## Assumptions and scope

The coordinates \(x\) and \(u\) are real; \(p,q\) are positive integers. All projections minimize the **squared Euclidean** distance, not the distance induced by \(\ell^\infty\). The sharp Lipschitz ratio is a supremum of ratios over all distinct points. No assertion is made that the supremum is attained by a distinct finite pair. The \(p=1\) Lorentz-cone specialization is background/consistency; the multi-scalar classification \(p\ge2\) is the main new content.

## Proof

**1. A scalar formula for the projection.** Fix input \((x,u)\) and write \(t=\|u\|_2\). For a proposed output Euclidean radius \(r\ge0\), the best scalar coordinates are \(y_i=\max(x_i,r)\), and the best vector coordinate is Euclidean-ball clipping \(v=\min\{1,r/t\}u\) (take \(v=0\) if \(t=0\)). One may restrict to \(0\le r\le t\): above \(t\), increasing \(r\) cannot improve the distance. Hence, if \(t>0\), the optimal radius minimizes
\[
F(r)=\sum_{i=1}^p(r-x_i)_+^2+(t-r)^2,\qquad 0\le r\le t.
\]
Its strictly increasing derivative divided by two is \(G(r)=r-t+\sum_i(r-x_i)_+\). If \(G(0)\ge0\), the optimum is \(r=0\). Otherwise it is the unique root of \(G(r)=0\) in \((0,t]\). The projection is consequently
\[
\Pi_{p,q}(x,u)=\left((\max\{x_i,r\})_{i=1}^p,\frac r t u\right)\quad(t>0),
\]
with the obvious \(t=0\) limit \(((\max\{x_i,0\})_i,0)\). Strict convexity of Euclidean distance proves uniqueness; alternatively the scalar equation supplies the full KKT system.

**2. Jacobian on every smooth chart.** Work at a point where \(t>0\), \(0<r<t\), and no \(x_i\) equals \(r\). Let \(I=\{i:x_i<r\}\), \(k=|I|\ge1\), \(v=u/t\) (thus \(\|v\|_2=1\)), and \(\alpha=r/t\in(0,1)\). Implicit differentiation of \(G(r)=0\) gives
\[
dr=\frac{\sum_{i\in I}dx_i+\langle v,du\rangle}{k+1}.
\]
Every active scalar output row therefore has absolute row sum
\[
R_x(k,v)=\frac{k+\|v\|_1}{k+1};
\]
inactive scalar rows have sum one. For the vector outputs \(r v\), the scalar-input derivative in row \(j\) has \(k\) entries equal in modulus to \(|v_j|/(k+1)\). The vector-input block is
\[
B=\alpha I_q+\left(\frac1{k+1}-\alpha\right)vv^{\mathsf T}.
\]
Thus their exact absolute row sums are
\[
R_{u,j}=\frac{k|v_j|}{k+1}
+\left|\alpha+\left(\frac1{k+1}-\alpha\right)v_j^2\right|
+\left|\frac1{k+1}-\alpha\right||v_j|(\|v\|_1-|v_j|).
\]

**3. A two-endpoint maximization.** For fixed \(k,v,j\), the preceding expression is convex in \(\alpha\in[0,1]\), so its supremum occurs at \(\alpha=0\) or \(\alpha=1\). At \(\alpha=0\), it equals \(|v_j|R_x(k,v)\le R_x(k,v)\). At \(\alpha=1\), the diagonal of \(B\) is positive and the row sum reduces exactly to
\[
R_{u,j}(1)=1+\frac{k}{k+1}|v_j|(1+\|v\|_1-2|v_j|).
\]
At a fixed \(a=|v_j|\), Cauchy--Schwarz bounds the other \(q-1\) absolute coordinates by \(\sqrt{(q-1)(1-a^2)}\); equality holds when those coordinates have equal modulus. Consequently the maximum of the parenthesized contribution is precisely \(H_q\) for \(q\ge2\), and it is zero for \(q=1\). The scalar rows obey \(\|v\|_1\le\sqrt q\), so maximizing over \(1\le k\le p\) yields
\[
\max_{k,v}R_x=\frac{1+\sqrt q}{2},\qquad
\sup_{k,v,j,\alpha}R_{u,j}\le\max\left\{\frac{1+\sqrt q}{2},1+\frac p{p+1}H_q\right\}.
\]
The first extremum comes from exactly one active scalar coordinate. Since \(k/(k+1)\) increases in \(k\), the second takes \(k=p\). In the exterior chart, any \(v\) and \(0<\alpha<1\) can be realized with exactly \(k\) active coordinates: take \(t=1\), \(u=v\), \(r=\alpha\), and \(x_i=r-(1-r)/k\) on \(I\), with \(x_i>r\) outside \(I\). This construction proves lower sharpness of the first branch and, by letting \(\alpha\uparrow1\), lower sharpness of the second branch.

**4. Global passage.** The projection is locally Lipschitz (indeed Euclidean nonexpansive). On the open regions where the projection radius is zero or equals the input vector radius, the projection is coordinatewise clipping or the identity and has induced maximum-norm derivative at most one. On the remaining open active-set charts, the Jacobian row sums obey the displayed constant. The switching sets and the vector-origin locus have measure zero along generic translated lines. Approximate any connecting line segment by generic translated segments and use absolute continuity and integration of derivatives on them. Continuity then gives the same upper bound for the original segment. The lower bounds from Step 3 establish the exact global modulus.

**5. The optimizer and phase boundary.** For \(q\ge2\), the function whose maximum defines \(H_q\) has derivative
\[
f_q'(a)=1-2a+\sqrt{q-1}\frac{1-2a^2}{\sqrt{1-a^2}}
\]
and second derivative
\[
f_q''(a)=-2-\sqrt{q-1}\frac{a(3-2a^2)}{(1-a^2)^{3/2}}<0\quad(0<a<1).
\]
Its derivative is positive at zero and tends to minus infinity as \(a\uparrow1\), so there is a unique maximizer. Testing \(a=1/\sqrt2\) yields
\[
H_q\ge\frac1{\sqrt2}-\frac12+\frac{\sqrt{q-1}}2>
\frac{\sqrt q-1}2=A_q.
\]
Comparison of the two branches gives the stated unique real boundary \(p_*(q)\). For \(q=1\), both increments in the main formula vanish, proving nonexpansivity. For \(q\ge2\), \(A_q>0\), proving strict expansivity.

**6. Large vector dimension.** The unique maximizer \(a_q\) satisfies \(a_q=1/\sqrt2+O(q^{-1/2})\). A Taylor expansion of the strictly concave objective around \(1/\sqrt2\) gives
\[
H_q=\frac{\sqrt{q-1}}2+\frac1{\sqrt2}-\frac12+O(q^{-1/2}).
\]
Consequently \(H_q-A_q=1/\sqrt2+O(q^{-1/2})\) and \(p_*(q)=\sqrt{q/2}+O(1)\). All limits concern positive integer vector dimensions; no uniform error claim beyond these asymptotics is asserted.

## Verification

Run `python3 verify_extended_cone.py` using Python's standard library. Its deterministic bisection, independently constructed finite-difference Jacobians, random-pair tests, row-extremizer approximations, and strict-concavity consistency checks passed 164490 assertions when the files were prepared. The checks cover finitely many integer pairs and cannot replace the proof for arbitrary dimensions. No external solver or infinite formal certificate is claimed.

## Relationship to prior work

Németh and Zhang introduced the extended Lorentz cone and analyzed isotone projections **onto cylinders** in its induced order; that is different from computing the coordinatewise sharp Lipschitz constant of projection **onto the cone itself** [1,2]. Their later paper treats linear cone-positive operators and does not imply the nonlinear projection modulus [3]. The ordinary single-scalar Lorentz case \(p=1\) has an independently known sharp coordinatewise modulus and is included only as a consistency specialization. In contrast, the formula for \(p\ge2\), its exact active-constraint optimization, and the dimension-dependent switch of dominating output types are the claimed contributions. General Euclidean nonexpansivity only bounds the Euclidean norm and does not supply these sharp maximum-coordinate constants.

## Limitations

The theorem is finite dimensional and concerns Euclidean projection measured in the **unweighted** coordinate maximum norm; it does not address projections defined using an \(\ell^p\) metric, nonsymmetric weighted coordinate norms, perturbations of cone geometry, or the dual cone. Bibliographic priority is provisional: exact equivalent results might occur under variational inequality, second-order cone sensitivity, or matrix-clipping terminology. The published projection-algorithm paper appearing later in October 2016 falls after the stated source-date anchor and is not used to establish priority. Independent mathematical and bibliographic validation has not been performed.

## References

[1] S. Z. Németh and G. Zhang, *Extended Lorentz cones and mixed complementarity problems*, arXiv:1405.7835 (first public 2014-05-30), https://arxiv.org/abs/1405.7835.

[2] S. Z. Németh and G. Zhang, *Extended Lorentz cones and variational inequalities on cylinders*, Journal of Optimization Theory and Applications 168 (2016), 756–768, https://doi.org/10.1007/s10957-015-0833-6.

[3] S. Z. Németh and G. Zhang, *Positive operators of extended Lorentz cones*, arXiv:1608.07455 (2016-08-26), https://arxiv.org/abs/1608.07455.
