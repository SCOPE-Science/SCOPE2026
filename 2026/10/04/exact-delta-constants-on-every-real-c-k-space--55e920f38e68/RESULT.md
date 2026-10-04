# Exact \(\Delta\)-constants on every real \(C(K)\) space

## Finding
Let \(K\) be an infinite compact Hausdorff space. Write \(I\) for its isolated points and \(K'=K\setminus I\) for its non-isolated core. For real \(f\in B_{C(K)}\), define
\[
\beta(f)=\max_{t\in K'}|f(t)|
\]
and, for \(1\le r\le2\),
\[
\Phi_f(r)=\sum_{\{t\in I:\ |f(t)|>r-1\}}
\frac{1-|f(t)|}{r+1-|f(t)|},
\]
where the sum is the supremum of its finite subsums and may equal \(+\infty\). Then
\[
\boxed{\displaystyle
\delta c_{C(K)}(f)=
\inf\bigl\{r\in[1,2]:\ r\ge1+\beta(f)\text{ and }\Phi_f(r)\le1\bigr\}.}
\]
The feasible set is nonempty: \(r=1+\|f\|_\infty\) makes the active set empty.

For the convergent-sequence space \(c=C(\mathbb N\cup\{\infty\})\), with \(L=\lim_n x_n\), this becomes
\[
\delta c_c(x)=\inf\left\{r\in[1,2]:r\ge1+|L|,\ 
\sum_{\{|x_n|>r-1\}}\frac{1-|x_n|}{r+1-|x_n|}\le1\right\}.
\]
Thus the non-isolated core supplies a hard floor, while finitely many sufficiently large isolated peaks can raise the constant above that floor. For example, if the first ten coordinates equal \(4/5\) and the remaining coordinates equal \(1/10\), then \(\delta c=9/5\).

## Assumptions and scope
The scalar field is real. The pointwise \(\Delta\)-constant is
\[
\delta c(f)=\inf_{S\ni f}\sup_{g\in S}\|f-g\|_\infty,
\]
where the infimum runs over slices of \(B_{C(K)}\). Since an infinite compact Hausdorff space cannot be discrete, \(K'\ne\varnothing\), so \(\beta(f)\) is well-defined. Every isolated singleton is clopen, hence its coordinate can be changed independently while preserving continuity.

## Proof
Fix a slice
\[
S(\mu,\alpha)=\{g\in B_{C(K)}:\mu(g)>1-\alpha\},\qquad \mu\in S_{M(K)},
\]
containing \(f\), and set
\[
R=\sup_{g\in S(\mu,\alpha)}\|f-g\|_\infty.
\]
We first prove that every such radius \(R\) is feasible.

Take \(t_0\in K'\) and \(s\in\{-1,1\}\) with \(s f(t_0)=|f(t_0)|\). Given \(\varepsilon>0\), continuity gives a neighborhood on which \(s f>|f(t_0)|-\varepsilon\). Because \(t_0\) is non-isolated and \(|\mu|\) has only finitely many atoms above any prescribed mass, this neighborhood contains a point \(u\) around which one can choose a smaller open set of arbitrarily small \(|\mu|\)-mass. A Urysohn perturbation supported there, equal to \(-s\) at \(u\), changes \(\mu(g)\) by less than the positive slice slack while keeping \(g\in B_{C(K)}\). Hence the slice contains points at distance arbitrarily close to \(1+|f(t_0)|\). Taking the supremum over \(t_0\in K'\) yields
\[
R\ge1+\beta(f).
\]

Now let
\[
J=\{t\in I:|f(t)|>R-1\},\qquad d_t=1-|f(t)|.
\]
For \(t\in J\), write \(s_t=\operatorname{sign}f(t)\) and \(a_t=|\mu(\{t\})|\). The atom \(\mu(\{t\})\) must have sign \(s_t\). Otherwise, using that \(\{t\}\) is clopen, one can set the \(t\)-coordinate to \(-s_t\) and choose a continuous unit-ball function on the complement that almost norms the restricted measure; this stays in the slice and has distance \(1+|f(t)|>R\), a contradiction.

Put \(q=1-\mu(f)\). Then \(0\le q<\alpha\), and the polar decomposition of \(\mu\) gives, for every finite \(F\subset J\),
\[
q=\int_K(1-fh)\,d|\mu|\ge\sum_{t\in F}a_t d_t,
\]
where \(h=d\mu/d|\mu|\) and the aligned atoms satisfy \(h(t)=s_t\). Moreover,
\[
a_t(R+d_t)\ge\alpha\qquad(t\in J).
\]
Indeed, if this failed, choose a small \(\eta>0\), set the isolated coordinate to \(s_t(|f(t)|-R-\eta)\), and almost norm the restriction of \(\mu\) on \(K\setminus\{t\}\). The resulting point belongs to the slice but lies at distance \(R+\eta\) from \(f\), again a contradiction.

If \(q>0\), then for every finite \(F\subset J\),
\[
q\ge\sum_{t\in F}a_t d_t
>q\sum_{t\in F}\frac{d_t}{R+d_t},
\]
because \(a_t(R+d_t)\ge\alpha>q\). Taking the supremum over finite \(F\) gives \(\Phi_f(R)\le1\). If \(q=0\), the same integral identity forces \(d_t=0\) at every active atom, so \(\Phi_f(R)=0\). Thus every slice radius satisfies both \(R\ge1+\beta(f)\) and \(\Phi_f(R)\le1\), proving the lower bound in the displayed formula.

For the reverse inequality, fix a feasible \(r\). It is enough to treat \(r'>r\). Then \(r'>1+\beta(f)\), and the active set
\[
J_{r'}=\{t\in I:|f(t)|>r'-1\}
\]
is finite: otherwise an accumulation point would lie in \(K'\) and continuity would force \(\beta(f)\ge r'-1\). Also \(\Phi_f(r')<1\) after increasing \(r'\) slightly if necessary.

If \(J_{r'}\) is empty, every point of the unit ball is already within distance \(r'\) of \(f\). Otherwise write \(a_t=|f(t)|\), \(d_t=1-a_t\), and
\[
b_t=\frac1{r'+d_t},\qquad
\lambda_t=\frac{b_t}{\sum_{u\in J_{r'}}b_u}.
\]
Let \(s_t=\operatorname{sign}f(t)\) and define the norm-one functional
\[
\varphi=\sum_{t\in J_{r'}}\lambda_t s_t\delta_t.
\]
If \(c=(\sum b_t)^{-1}\), then
\[
\varphi(f)=1-c\Phi_f(r')>1-c.
\]
Choose a slice threshold strictly between \(1-c\) and \(\varphi(f)\). This slice contains \(f\). If \(g\) in the slice had \(\|f-g\|_\infty>r'\), the offending point would have to belong to \(J_{r'}\); at such a point \(t\),
\[
s_tg(t)<a_t-r'.
\]
Consequently
\[
\varphi(g)\le1-\lambda_t(r'+d_t)=1-c,
\]
contradicting the slice inequality. Hence the slice radius is at most \(r'\). Letting \(r'\downarrow r\), and then taking the infimum over feasible \(r\), proves the claimed equality.

## Verification
The proof is analytic. The accompanying standard-library checker verifies the finite-dimensional separation identity underlying the upper and isolated-coordinate lower arguments: for an active vector \((a_i)\) and radius \(r\), a slice half-space containing \((a_i)\) can avoid every coordinate-bad face exactly when
\[
\sum_i\frac{1-a_i}{r+1-a_i}<1.
\]
It exhaustively checks rational active vectors of dimensions up to four and rational radii, comparing the closed-form criterion with the exact support function of the union of bad cube faces. This computation does not verify the topological Urysohn step and is not used as a substitute for the proof.

## Relationship to prior work
Abrahamsen, Haller, Lima, and Pirk proved the qualitative \(C(K)\) characterization: a norm-one function is a Daugavet point, equivalently a \(\Delta\)-point, exactly when its modulus attains one at a non-isolated point. Choi and Jung introduced the quantitative Daugavet and \(\Delta\)-constants. Their classical-space section gives lower bounds and special exact families for \(c_0\), and their uniform-algebra section gives a \(\Delta\)-constant upper estimate under a finite near-norming-boundary hypothesis. The inspected statements do not provide the exact all-point \(C(K)\) formula above.

The formula also clarifies how two previously separate mechanisms combine: the non-isolated core forces the floor \(1+\beta(f)\), while isolated points contribute the same finite-face obstruction that appears in coordinate spaces. Neither mechanism alone determines the general value.

## Limitations
The theorem is for real scalar \(C(K)\) spaces. It does not claim a complex analogue or an exact formula for general uniform algebras. The originality search covered the defining quantitative paper, the earlier qualitative \(C(K)\) paper, targeted web searches, and multiple semantic published-finding corpus queries; differently phrased or unindexed equivalent literature remains a residual risk.

## References
1. T. A. Abrahamsen, R. Haller, V. Lima, K. Pirk, “Delta- and Daugavet-points in Banach spaces,” arXiv:1812.02450v1, first posted 2018-12-06; later Proc. Edinburgh Math. Soc. 63 (2020), 475–496, DOI 10.1017/S0013091519000567.
2. G. Choi, M. Jung, “The Daugavet and Delta-constants of points in Banach spaces,” arXiv:2307.10647v1, first posted 2023-07-20; revised 2024-06-24; DOI 10.1017/prm.2024.83.
