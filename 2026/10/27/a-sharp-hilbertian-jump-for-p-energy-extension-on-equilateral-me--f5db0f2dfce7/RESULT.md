# A sharp Hilbertian jump for \(p\)-energy extension on equilateral metric stars

## Finding

Let \(T_m\) be a unit-arm metric star with center \(o\) and \(m\ge 2\) leaves. For \(1<p<\infty\), the canonical scalar \(p\)-energy extension \(E_p\) of leaf values \(v=(v_1,\ldots,v_m)\) is affine on every arm and has center value \(c_p(v)\), the unique minimizer of
\[
J_p(c;v)=\sum_{i=1}^m |v_i-c|^p.
\]
For functions on these metric spaces write \(\operatorname{Lip}(f;X)=\sup_{x\ne y}|f(x)-f(y)|/d_X(x,y)\). The **exact global two-data stability constant** is
\[
K_{m,p}:=\sup_{\operatorname{Lip}(v-w;\partial T_m)>0}
 \frac{\operatorname{Lip}(E_p(v)-E_p(w);T_m)}{\operatorname{Lip}(v-w;\partial T_m)}
=
\begin{cases}
1,&m=2,\\
2(m-1)/m,&m\ge3,\ p=2,\\
2,&m\ge3,\ 1<p<\infty,\ p\ne2.
\end{cases}
\]
The constants in the first two cases are attained. For \(m\ge3\) and \(p\ne2\), the value \(2\) is a nonattained supremum over distinct data with nonconstant difference. Thus the sharp constant is discontinuous as a function of the energy exponent at the Hilbert value \(p=2\), although every fixed-data center \(c_p(v)\) depends continuously on \(p\).

The approach to the sharp constant has explicit and different exponents on the two sides. Fix \(m\ge3\), take \(v=(-1,0,1,0,\ldots,0)\) and, for \(t>0\), define \(v^{(t)}\) by raising its second coordinate by \(t\) for \(p>2\), or its first coordinate by \(t\) for \(1<p<2\). In either construction the two-data quotient \(Q_p(t)\) satisfies \(Q_p(t)\to2\). More precisely,
\[
2-Q_p(t)\sim
\begin{cases}
\displaystyle 2\left(\frac{p-1}{m-2}\right)^{1/(p-1)}t^{(2-p)/(p-1)},&1<p<2,\\[6pt]
\displaystyle\frac{t^{p-2}}{p-1},&p>2.
\end{cases}
\]

## Assumptions and scope

The tree has exactly \(m\ge2\) leaves, every arm has length one, and the values are real. The boundary metric is the restriction of the tree metric, so distinct leaves are distance two apart. Along each arm the extension is the affine interpolation between the prescribed leaf value and its center. These interpolants uniquely minimize \(\sum_i\int_{e_i}|u'|^p\) among continuous functions with the given leaf data, by Jensen's inequality followed by strict convexity of \(J_p\).

Writing \(\operatorname{osc}(z)=\max_i z_i-\min_i z_i\), one has
\[
\operatorname{Lip}(z;\partial T_m)=\tfrac12\operatorname{osc}(z),\qquad
\operatorname{Lip}(E_p(v)-E_p(w);T_m)
=\max_i\left|(v_i-w_i)-(c_p(v)-c_p(w))\right|.
\]
Both seminorms vanish on constants, and the two-data supremum excludes zero boundary seminorm. The problem is invariant under common translation and simultaneous scaling of leaf data.

## Proof

**Center uniqueness and strict order.** The function \(J_p(\cdot;v)\) is strictly convex for \(p>1\). Its minimizer is the unique zero of
\[
F_p(c;v)=\sum_{i=1}^m \psi_p(c-v_i),\qquad
\psi_p(s)=\operatorname{sgn}(s)|s|^{p-1},\quad \psi_p(0)=0.
\]
The function \(F_p\) is strictly increasing in \(c\) and strictly decreasing in each leaf coordinate. Consequently \(c_p(v)\) is strictly increasing in every coordinate and translation-equivariant: \(c_p(v+a\mathbf1)=c_p(v)+a\). If \(z=v-w\) is nonconstant and \(a=\min_i z_i\), \(b=\max_i z_i\), comparison with \(w+a\mathbf1\) and \(w+b\mathbf1\) gives the strict bound
\[
a<c_p(v)-c_p(w)<b.
\]
It follows that the star Lipschitz seminorm of the difference is strictly smaller than \(b-a\), whereas the boundary seminorm is \((b-a)/2\). Hence \(K_{m,p}\le2\) for all cases and the value \(2\) is never attained by a nonconstant perturbation.

**Two leaves and the quadratic exponent.** For \(m=2\), symmetry of the strictly convex energy about the midpoint gives \(c_p(v)=(v_1+v_2)/2\), for all \(p>1\). Thus every nonconstant perturbation has quotient exactly one. For \(p=2\) and general \(m\), \(c_2(v)=m^{-1}\sum_i v_i\). A perturbation with values within \([a,b]\) satisfies
\[
\max_i\left|z_i-\frac1m\sum_j z_j\right|
\le\frac{m-1}{m}(b-a).
\]
The bound is achieved with \(z=(1,0,\ldots,0)\), proving \(K_{m,2}=2(m-1)/m\).

**Superquadratic sharpness and rate.** For \(m\ge3\) and \(p>2\), fix \(v=(-1,0,1,0,\ldots,0)\) with \(c_p(v)=0\) and raise its second coordinate to \(t>0\). Let \(s_t=c_p(v^{(t)})\). Strict order gives \(0<s_t<t\). The defining center equation has the asymptotic form
\[
0=2(p-1)s_t-t^{p-1}+o(s_t)+o(t^{p-1})
\]
provided \(s_t=o(t)\). To justify this prior assertion, divide the equation by \(t^{p-1}\), note \(s_t\le t\), and use \(p>2\): the two nonzero base coordinates contribute \(2(p-1)s_t+o(s_t)\) and the zero coordinates contribute at most order \(t^{p-1}\). This forces \(s_t=O(t^{p-1})=o(t)\). Therefore
\[
s_t\sim\frac{t^{p-1}}{2(p-1)}.
\]
The boundary perturbation is \(t\) at exactly one leaf, so its Lipschitz seminorm is \(t/2\). The extended perturbation has central value \(s_t\), and its largest arm slope is \(t-s_t\) for sufficiently small \(t\), because \(s_t=o(t)\). Hence \(Q_p(t)=2(1-s_t/t)\) and \(2-Q_p(t)\sim t^{p-2}/(p-1)\).

**Subquadratic sharpness and rate.** For \(m\ge3\) and \(1<p<2\), raise instead the first base coordinate from \(-1\) to \(-1+t\). Write again \(s_t=c_p(v^{(t)})\), so \(0<s_t<t\). At small \(t\), expanding the contributions from the two extreme leaves gives
\[
0=-(p-1)t+2(p-1)s_t+(m-2)s_t^{p-1}+o(t).
\]
Because \(0<s_t<t\) and \(p-1<1\), this equation yields \(s_t=O(t^{1/(p-1)})=o(t)\) (the extreme-coordinate expansion is uniform for \(s_t\in[0,t]\)). Consequently
\[
s_t\sim\left(\frac{p-1}{m-2}\right)^{1/(p-1)}t^{1/(p-1)}.
\]
Again the boundary perturbation is supported on one leaf and the maximal arm slope of its extension is \(t-s_t\) for small \(t\). Therefore \(Q_p(t)=2(1-s_t/t)\), with the stated subquadratic deficiency. These constructions prove \(K_{m,p}\ge2\) for every \(p\ne2\), completing the formula together with the strict upper bound.

**Continuity for fixed data.** If \(p_k\to p>1\), the strictly convex energies \(J_{p_k}\) converge uniformly on the compact interval \([\min_i v_i,\max_i v_i]\) for fixed \(v\). Their unique minimizers therefore converge to \(c_p(v)\). The jump occurs only after the supremum over data pairs.

## Verification

A standalone standard-library Python script `checker.py` reproduces bisection for the unique root of \(F_p\) and independent evaluations of the two relevant Lipschitz seminorms. It tests sampled two-data inequalities in multiple dimensions and exponents, the exact quadratic equality cases, and the predicted asymptotic center-response coefficients. Run `python checker.py`. The checks are finite numerical stress tests, not an infinite proof; the full scope is established by the preceding symbolic arguments.

## Relationship to prior work

Finite-graph extensions and \(p\)-harmonic functions were developed in earlier graph Dirichlet theories. Sheffield and Smart (arXiv:1006.1741, first public 2010-06-09) study tight and \(p\)-related Lipschitz extensions of finite-graph data, with different energy and lexicographic objectives. Manfredi, Oberman, and Svirodov (arXiv:1212.0834, first public 2012-12-04) develop nonlinear \(p\)-harmonic graph schemes and comparison principles; their graph operator and questions do not contain the present sharp boundary-to-whole-star two-data Lipschitz profile.

A published sharp \(\ell_p\)-metric-projection result for the constant-vector line (identifier `c5b935fc4ff6`) studies the same scalar \(p\)-mean but uses ambient \(\ell_p\) distances on vectors. Its norms and sharp constants do not provide the quotient of the boundary metric Lipschitz seminorm and the full-star Lipschitz seminorm computed here. Related finite-chain isotonic \(\ell_p\)-projection results likewise have different input/output geometries. Classical absolutely minimizing Lipschitz extensions on metric stars, which use the midpoint of the extreme leaf constraints, are not the finite-exponent \(p\)-energy minimizer except in special data configurations. No claim is made that the scalar \(p\)-mean or monotonicity comparison is new.

## Limitations

Only equal-arm real metric stars and strictly convex finite exponents \(1<p<\infty\) are covered. The result makes no assertion for unequal arm lengths, arbitrary trees, complex/vector targets, or graph \(p\)-harmonious discretizations based on mixed maximal/average slopes. There is no independent verification; exact all-dimensional validity rests on the written proof. It remains possible that the same cross-seminorm formula or its reduction exists in older unindexed literature; relevant published sharp \(\ell_p\)-projection records have not been inspected beyond their accessible abstracts/summaries.

## References

1. S. Sheffield and C. K. Smart, *Vector-valued optimal Lipschitz extensions*, arXiv:1006.1741 (initial public version 2010-06-09), https://arxiv.org/abs/1006.1741.
2. J. J. Manfredi, A. M. Oberman and A. P. Svirodov, *Nonlinear elliptic partial differential equations and \(p\)-harmonic functions on graphs*, arXiv:1212.0834 (initial public version 2012-12-04), https://arxiv.org/abs/1212.0834.
3. *Exact Lipschitz phase diagram of metric projection onto the constant-vector line in real \(\ell_p^n\)*, published mathematical record `c5b935fc4ff6`, https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-exact-lipschitz-phase-diagram-of-metric-projection-onto-the-cons--c5b935fc4ff6.
4. *Sharp \(\ell_p\) stability of finite-chain isotonic metric projections*, published mathematical record `f78c125227d5`, https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-sharp-ell-p-stability-of-finite-chain-isotonic-metric-projection--f78c125227d5.
