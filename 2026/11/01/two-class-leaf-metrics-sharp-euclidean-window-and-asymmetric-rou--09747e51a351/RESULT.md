# Two-class leaf metrics: sharp Euclidean window and asymmetric roundness blow-up

## Finding
Let \(m,n\ge2\) be integers and \(a,b>0\). Consider a weighted star having \(m\) leaves of arm length \(a\) and \(n\) leaves of arm length \(b\), but equip **only its \(m+n\) leaves** with the inherited path metric. Its within-class distances are \(2a\) and \(2b\), and its cross-class distance is \(a+b\). Put
\[
A=1-\frac1m,\quad B=1-\frac1n,\quad q=\frac{a-b}{a+b}\in(-1,1),\qquad
F_q(p)=A(1+q)^p+B(1-q)^p.
\]
If \(a=b\), the metric is equilateral and has strict \(p\)-negative type for every finite \(p\ge0\), hence supremal generalized roundness \(\wp=\infty\). If \(a\ne b\), its exact exponent \(\wp=\wp_{m,n}(a,b)>1\) is the **unique** solution in \((1,\infty)\) of
\[
\boxed{\;A\left(\frac{2a}{a+b}\right)^\wp+B\left(\frac{2b}{a+b}\right)^\wp=2.\;}
\]
It has strict \(p\)-negative type for \(0\le p<\wp\), non-strict \(\wp\)-negative type with a one-dimensional zero-sum equality space, and fails \(p\)-negative type for every \(p>\wp\). Thus for unequal arm lengths the least dimension of an isometric Euclidean embedding of the snowflake metric \(d^{p/2}\) is \(m+n-1\) below \(\wp\), and exactly \(m+n-2\) at the endpoint. At equal lengths it is \(m+n-1\) for every finite \(p>0\).

The exponent is strictly decreasing as \(q\) increases from \(0\) to \(1\), and strictly increasing as \(q\) increases from \(-1\) to \(0\). Its extreme-ratio limits are
\[
\lim_{a/b\to\infty}\wp_{m,n}(a,b)=\log_2\frac{2m}{m-1},\qquad
\lim_{a/b\to0}\wp_{m,n}(a,b)=\log_2\frac{2n}{n-1}.
\]

There is a **sharp Euclidean feasibility window** for the original leaf metric \(d\). Define
\[
S=A+B,\quad D=A-B,\quad K=2-A-B=\frac1m+\frac1n,\qquad
q_{\pm}=\frac{-D\pm\sqrt{D^2+SK}}{S}.
\]
Then \(-1\le q_-<0<q_+\le1\), and \(d\) embeds isometrically in a Euclidean space if and only if \(q_-\le q\le q_+\). Inside this interval the required dimension is \(m+n-1\), except at an attained boundary \(q=q_\pm\in(-1,1)\), where it is \(m+n-2\). The endpoints \(q_+=1\) and \(q_-=-1\) arise exactly when \(m=2\) and \(n=2\), respectively, and cannot be attained with finite positive \(a,b\).

The divergence near the equilateral metric is **directionally asymmetric when \(m\ne n\)**. Define
\[
\kappa_+=\log\frac{1+\sqrt{1-AB}}{A},\qquad
\kappa_-=\log\frac{1+\sqrt{1-AB}}{B}.
\]
As the lengths become equal from the two sides,
\[
\boxed{\quad
\lim_{a/b\downarrow1}\wp_{m,n}(a,b)\log(a/b)=2\kappa_+,\qquad
\lim_{a/b\uparrow1}\wp_{m,n}(a,b)\log(b/a)=2\kappa_-.
\quad}
\]
In particular, the two reciprocal small-anisotropy constants are unequal precisely when \(m\ne n\), although the limiting equilateral metric has infinite generalized roundness.

## Assumptions and scope
The underlying leaf set consists of exactly \(m\) points at tree distance \(a\) from an **excluded** hub and exactly \(n\) points at distance \(b\), with \(m,n\ge2\) and \(a,b>0\). The distances are those of the entire weighted star restricted to this leaf set, not graph distances after deleting the hub. The powered distance matrix \(D_p\) has entries \(d(x,y)^p\) for distinct points and zero diagonal; the \(p=0\) convention gives off-diagonal entries one. Negative type means \(\alpha^{\mathsf T}D_p\alpha\le0\) for every real coefficient vector with coordinate sum zero. Generalized roundness agrees with this invariant; minimal Euclidean dimensions refer to exact isometric embeddings of \(d^{p/2}\), not arbitrary distortion embeddings. All parameter statements have the indicated quantifiers.

## Proof
Write the coefficient vector as \((x_1,\ldots,x_m,y_1,\ldots,y_n)\) with total sum zero, and let \(s=\sum_i x_i=-\sum_j y_j\). Set \(u_i=x_i-s/m\) and \(v_j=y_j+s/n\), so that \(\sum_i u_i=\sum_jv_j=0\). Because each within-class distance is constant and every cross-class distance is \(a+b\), direct expansion gives the exact identity
\[
\begin{aligned}
\alpha^{\mathsf T}D_p\alpha
={}&-(2a)^p\sum_{i=1}^m u_i^2-(2b)^p\sum_{j=1}^n v_j^2\\
&+(a+b)^p\bigl[F_q(p)-2\bigr]s^2.
\end{aligned}
\tag{1}
\]
Both fluctuation coefficients are strictly negative for every finite exponent. Therefore \(p\)-negative type is equivalent to \(F_q(p)\le2\), and strict negative type is equivalent to \(F_q(p)<2\). At equality the entire nonzero kernel on the zero-sum subspace consists of \(x_i=s/m\), \(y_j=-s/n\): it has dimension one.

If \(q=0\), then \(F_0(p)=A+B<2\) for all \(p\), which proves the equilateral assertion. Suppose \(q>0\). The function \(p\mapsto F_q(p)\) is strictly convex, has \(F_q(1)=A(1+q)+B(1-q)<2\), and tends to infinity because \(A>0\) and \(1+q>1\). Its sublevel set at height two therefore ends at exactly one finite \(\wp>1\), after which the function is strictly above two. For \(q<0\) the same proof interchanges the two classes. Identity (1) gives the exact negative-type interval and kernel. The centered Euclidean Gram matrix \(-\frac12 HD_pH\), where \(H=I-\frac{1}{m+n}\mathbf1\mathbf1^{\mathsf T}\), is positive semidefinite exactly in this interval and has rank \(m+n-1\) in its strict interior, dropping by one at its finite endpoint. The standard finite-metric Gram criterion supplies the stated embedding dimensions.

For fixed \(p>1\), \(q\mapsto F_q(p)\) is strictly convex, and \(F_0(p)=A+B<2\). At any positive \(q\) satisfying \(F_q(p)=2\), the \(q\)-derivative is strictly positive (its secant slope from zero is positive). At a negative crossing it is strictly negative. At the critical exponent the \(p\)-derivative is strictly positive by convexity in \(p\) and the strict inequality at \(p=1\). Implicit differentiation now proves both strict monotonicity statements. Taking \(q\to1\) or \(q\to-1\) in the defining equation, using boundedness of the roots obtained from monotonicity and their positive lower bound, yields the two extreme-ratio limits.

For the Euclidean window, put \(p=2\):
\[
F_q(2)-2=S q^2+2Dq-K.
\]
Since \(S,K>0\), this convex quadratic is nonpositive precisely between its two real roots \(q_-\) and \(q_+\). Moreover \(F_{+1}(2)=4A\ge2\) and \(F_{-1}(2)=4B\ge2\), with equality at the corresponding endpoint precisely for a two-leaf class. Hence the two roots lie in \([-1,1]\) as claimed. Identity (1) and its kernel give exact Euclidean embedding ranks also at equality.

Finally, write \(q>0\) and \(c(q)=q\wp(q)\). The root equation is
\[
A\exp\!\left[c(q)\frac{\log(1+q)}q\right]
+B\exp\!\left[c(q)\frac{\log(1-q)}q\right]=2.
\]
As \(q\downarrow0\), any sequence of solutions has \(c(q)\) bounded above and bounded away from zero: otherwise the first term diverges or the left side approaches \(A+B<2\). Every subsequential limit \(c>0\) must satisfy \(Ae^c+Be^{-c}=2\). This equation has exactly one positive solution, \(c=\log[(1+\sqrt{1-AB})/A]=\kappa_+\), by solving a quadratic in \(e^c\). Thus \(q\wp(q)\to\kappa_+\). For \(q<0\), the same argument with the classes swapped gives \(|q|\wp(q)\to\kappa_-\). Since \(\log(a/b)=2\operatorname{artanh}q\sim2q\) as \(q\to0\), the displayed one-sided laws follow. This argument also proves the constants are unequal exactly when \(A\ne B\), equivalently \(m\ne n\).

## Verification
The accompanying `verify_two_class_leaf_roundness.py` checks (1) with exact rational arithmetic for 480 zero-sum samples across multiple class sizes, positive rational lengths and integer exponents (including zero). It also independently constructs centered Gram matrices and checks 20 endpoint inertia configurations and their strict/failing adjacent exponents. Separate calculations test two-sided monotonicity, the directional singular constants and the exact \(p=2\) feasibility polynomial. Run with `python verify_two_class_leaf_roundness.py` in an environment containing NumPy and SciPy. These finite checks are corroboration only; the universal claims are proved above.

## Relationship to prior work
Faver, Kochalski, Murugan, Verheggen, Wesson and Weston [2], Proposition 4.4, determine generalized roundness for a star **leaf metric with one exceptional arm** and \(k\) equal arms. Their calculation is recovered formally by allowing one of our class sizes to equal one, but the present theorem concerns two **non-singleton** arm-length classes, determines their full critical kernel and Euclidean feasibility region, and proves a directionally asymmetric singular limit absent from [2]. In particular, neither their one-exceptional formula nor the generalized-roundness classification of an entire weighted star **including its hub** provides the exact exponent here: including the hub changes the metric space, and at \(a=b\) the leaf-only roundness is infinite while the full star's is finite. Sánchez [1] gives general finite-metric spectral criteria, not this evaluated two-population formula. Robertson [3] gives determinant-based simplifications of that general method, again without the present anisotropy and one-sided singular classification.

## Limitations
This theorem applies to the leaf restriction of a single weighted star with exactly two arm-length classes each of multiplicity at least two. It makes no assertion about three or more different arm lengths, arbitrary tree topology, the metric with its hub included, or non-isometric embeddings. The source comparisons do not establish worldwide priority; an unindexed equivalent derivation remains possible. Numerical eigenvalue tests at extremely small length contrast can be ill-conditioned, so asymptotic conclusions are proved analytically rather than inferred from such tests. Independent review has not been performed.

## References
[1] S. Sánchez, “On the supremal \(p\)-negative type of a finite metric space,” arXiv:1108.0451, first publicly submitted 2011-08-02, https://arxiv.org/abs/1108.0451.

[2] T. Faver, K. Kochalski, M. K. Murugan, H. Verheggen, E. Wesson and A. Weston, “Roundness properties of ultrametric spaces,” arXiv:1201.6669, first publicly submitted 2012-01-31; Glasgow Math. J. 56 (2014), 519–535, Proposition 4.4, https://arxiv.org/abs/1201.6669.

[3] G. Robertson, “The maximal generalised roundness of finite metric spaces,” arXiv:2004.10923, first publicly submitted 2020-04-23, https://arxiv.org/abs/2004.10923.
