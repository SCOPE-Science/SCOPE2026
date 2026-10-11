# Exact Lipschitz stability and contractivity threshold for weighted cross-polytope projections

## Finding
Let \(1<p<\infty\), let \(q=p/(p-1)\), fix \(n\ge1\), positive weights \(w=(w_1,\ldots,w_n)\), and a radius \(r>0\). On the real Banach space \((\mathbb R^n,\|\cdot\|_p)\) consider the weighted cross-polytope
\[
B_{w,r}=\left\{z\in\mathbb R^n:\sum_{i=1}^nw_i|z_i|\le r\right\}
\]
and its unique nearest-point projection \(P_{p,w,r}(x)=\arg\min_{z\in B_{w,r}}\|x-z\|_p\).

**Exact metric projection.** For \(x\in B_{w,r}\), the minimizer is \(x\). Otherwise, there exists a unique \(\tau>0\) satisfying
\[
\sum_{i=1}^nw_i\bigl(|x_i|-\tau w_i^{q-1}\bigr)_+=r,
\qquad
(P_{p,w,r}(x))_i=\operatorname{sgn}(x_i)\bigl(|x_i|-\tau w_i^{q-1}\bigr)_+.
\]
Here \((t)_+=\max(t,0)\) and \(\operatorname{sgn}(0)=0\).

**Exact global stability.** For every nonempty subset \(S\subseteq\{1,\ldots,n\}\), write \(w_S=(w_i)_{i\in S}\), \(a_S=(w_i^{q-1})_{i\in S}\), \(W_S=\sum_{i\in S}w_i^q\), and define the rank-one-corrected identity
\[
J_S=I_S-\frac{a_Sw_S^T}{W_S}:\ell_p^{S}\to\ell_p^{S}.
\]
Then
\[
\boxed{\operatorname{Lip}_{\ell_p}(P_{p,w,r})
=\max\!\left\{1,\max_{\emptyset\ne S\subseteq[n]}
\|J_S\|_{\ell_p^{S}\to\ell_p^{S}}\right\}.}
\]
Here \(\operatorname{Lip}\) is the smallest \(L\) such that \(\|P(x)-P(y)\|_p\le L\|x-y\|_p\) for every \(x,y\in\mathbb R^n\). The finite-subset expression is exact even when the individual linear operator norms have no elementary closed form.

**Sharp nonexpansivity classification.**
\[
\boxed{\operatorname{Lip}_{\ell_p}(P_{p,w,r})=1
\quad\Longleftrightarrow\quad
p=2\ \text{or}\ n=1\ \text{or}\ (n=2\ \text{and}\ w_1=w_2).}
\]
In dimension two the entire global constant, including anisotropic weights, is
\[
\boxed{\operatorname{Lip}_{\ell_p}(P_{p,w,r})=
\frac{(w_1^p+w_2^p)^{1/p}
(w_1^{q(q-1)}+w_2^{q(q-1)})^{1/q}}
{w_1^q+w_2^q}.}
\]
All conclusions hold for every \(r>0\).

## Assumptions and scope
All scalars, vectors, and norms are real. The dimension is finite and positive. The weights and radius are strictly positive, and the exponent is strictly between one and infinity. If \(n=1\), the map is scalar clipping and the Lipschitz constant is one. An optimal Lipschitz constant need only be a supremum of ratios: no assertion of a maximizing *distinct* input pair is required.

## Proof
**1. Existence, uniqueness, and coordinate signs.** Strict convexity of \(\ell_p^n\) gives uniqueness; compact convex feasibility gives existence. A coordinate of a feasible point with sign opposite to the corresponding coordinate of \(x\) can be changed to zero, improving the distance without increasing the weighted constraint. For each coordinate the minimizing sign is therefore the sign of the input. Outside the ball the constraint is active; otherwise strict convexity and the unconstrained minimizer force \(P(x)=x\). The KKT condition for minimizing \(\sum_i|x_i-z_i|^p/p\) with active weighted constraint gives
\[
|x_i-z_i|^{p-1}=\mu w_i
\quad\text{whenever }z_i\ne0,
\]
and complementary slackness gives zero when the unconstrained coordinate shrinkage exceeds its magnitude. Setting \(\tau=\mu^{1/(p-1)}\), and noting \(1/(p-1)=q-1\), yields the formula. The mass function is continuous and strictly decreasing from a value above \(r\) to zero up to its last positive coordinate, hence its positive root is unique.

**2. Exact local affine pieces.** Fix an outside point at which the signs are fixed and the active set \(S=\{i:(P(x))_i\ne0\}\) remains unchanged under sufficiently small perturbations. On this open region,
\[
\tau=\frac{\sum_{i\in S}w_i|x_i|-r}{W_S},
\quad (P(x))_i=\operatorname{sgn}(x_i)(|x_i|-\tau a_i)
\quad(i\in S),
\]
with zero output outside \(S\). The derivative is the sign-conjugate of the matrix \(J_S\), followed by zero extension; changing signs is an isometry of \(\ell_p^n\). Its operator norm therefore equals \(\|J_S\|\).

Every nonempty \(S\) is realized by an open region: choose \(x_i=r/(|S|w_i)+t a_i\) for \(i\in S\), \(x_i=0\) outside, with \(t>0\). Small changes preserve positive active coordinates and strict inactivity elsewhere, and the local threshold equals \(t\). Thus the norm of every \(J_S\) gives a genuine lower bound on the global Lipschitz constant. The map is identity on the interior of \(B_{w,r}\), giving the lower bound one. Conversely the map is continuous and piecewise affine, with finitely many active sets and sign patterns; subdivide any segment into its finitely many affine pieces (or approximate boundary-contained segments by generic ones). Integrating the affine increments gives the maximum of the local operator norms as a global bound. This proves the exact formula.

**3. Nonexpansivity obstruction.** If \(J_S\) has norm one, then for every \(v\in\ker w_S^T\) and every real \(t\),
\[
\|v\|_p=\|J_S(v+t a_S)\|_p\le\|v+t a_S\|_p.
\]
Differentiating the strictly convex function \(\sum_i|v_i+t a_i|^p\) at zero forces
\[
\sum_{i\in S}|v_i|^{p-2}v_i a_i=0
\qquad\text{for every }v\in\ker w_S^T,
\]
where the scalar \(|0|^{p-2}0\) means zero. For distinct \(i,j\in S\), take \(v_i=w_j\), \(v_j=-w_i\), all other coordinates zero. It follows that
\[
w_j^{p-1}w_i^{q-1}=w_i^{p-1}w_j^{q-1}.
\]
When \(p\ne2\), the exponents \(p-1\) and \(q-1\) differ, forcing \(w_i=w_j\). If \(|S|\ge3\), all weights are therefore equal. Taking \(v=(1,1,-2,0,\ldots)\), a zero-sum vector, the derivative condition then requires \(2-2^{p-1}=0\), again forcing \(p=2\). Consequently for \(p\ne2\), every full-support \(J_S\) with \(|S|\ge3\) has norm strictly greater than one, and every unequal-weight two-support \(J_S\) does as well.

In the Hilbert case \(p=2\), nearest-point projection onto any closed convex set is nonexpansive. If \(n=2\) and the weights are equal, the only nonzero active-subset derivative is the signed conjugate of \(\frac12\begin{pmatrix}1&-1\-1&1\end{pmatrix}\), an \(\ell_p^2\) contraction by Hölder's inequality; singleton active derivatives vanish. The exact local-norm formula therefore gives one. The one-dimensional clipping case completes the classification.

**4. Exact two-dimensional quantitative constant.** For \(n=2\), the full-support derivative is rank one:
\[
J_{\{1,2\}}=\frac1{w_1^q+w_2^q}
\begin{pmatrix}w_2\-w_1\end{pmatrix}
\begin{pmatrix}w_2^{q-1}&-w_1^{q-1}\end{pmatrix}.
\]
The norm of an outer product from \(\ell_p\) to itself equals the \(\ell_p\)-norm of its column times the dual \(\ell_q\)-norm of its row. This yields the displayed closed form. Every singleton derivative is zero, while the interior identity has norm one. Since \(J_{\{1,2\}}\) acts identically on the nonzero kernel of \(w^T\), its norm is at least one; hence the formula already includes the interior contribution. Strictness away from the classified cases follows from Step 3. Finally, rescaling input and output by \(r\) proves independence from the radius.

## Verification
Execute the standalone \(\texttt{verify.py}\) with Python 3.10 or later, requiring no third-party packages. Its deterministic checks cover all five sample dimensions, six exponents, random weighted KKT residuals, exact two-coordinate operator-norm witnesses, finite-difference realization of the sharp constant, and strict expansion in the three-coordinate equal-weight cases. The expected terminal line is \(\texttt{VERIFY\_OK checks=1240 random\_seeds=240441 all\_scenarios\_passed}\). This is a finite, numerical consistency check and not an infinite proof or a validated interval certificate. Analytic arguments above prove the all-parameter statements.

## Relationship to prior work
Duchi, Shalev-Shwartz, Singer, and Chandra (2008) give exact Euclidean projections onto the ordinary \(\ell_1\) ball, including thresholding. The present metric projection varies the ambient exponent and introduces weights; its stability theorem and full subset-derivative modulus do not follow from Euclidean nonexpansivity. Kobos (2015) discusses norm-one linear hyperplane projections and their supporting-functional necessary conditions, overlapping the *linear* obstruction in Step 3 but not giving the nonlinear cross-polytope projection modulus. Denkowska (2013), building on Jamison--Kamińska--Lewicki and Kamińska--Lewicki, characterizes one-complemented kernels and classes of contractive convex sets. Those structural theorems are a substantive antecedent for the qualitative rigidity mechanism. This result is specifically about the **nearest-point projection**, with its exact global Lipschitz constant for arbitrary positive weights, including the sharp planar formula. See references for the precise prior objects; the cited papers are not represented as establishing novelty by their absence of a matching title.

## Limitations
The general formula for \(n\ge3\) is a finite maximum of explicit **linear operator norms**, not a closed elementary expression for every weight pattern. It is not a theorem on arbitrary strictly convex norms, infinite-dimensional spaces, or the nonsmooth endpoints \(p=1,\infty\). Related older results on contractive sets and hyperplane projections may yield the qualitative classification through additional reductions; no assertion of an independent mathematical audit or exhaustive literature completeness is made.

## References
1. J. Duchi, S. Shalev-Shwartz, Y. Singer, T. Chandra, *Efficient Projections onto the \(\ell_1\)-Ball for Learning in High Dimensions*, ICML 2008, 272–279. DOI: 10.1145/1390156.1390191. Author manuscript: https://ai.stanford.edu/~jduchi/projects/jd_ss_ys_l1.pdf .
2. T. Kobos, *A uniform estimate of the relative projection constant*, arXiv:1508.03518, August 2015, https://arxiv.org/pdf/1508.03518 .
3. A. Denkowska, *Contractive and optimal sets in Musielak--Orlicz spaces with a smoothness condition*, Opuscula Math. 33 (2013), 667–684, https://www.opuscula.agh.edu.pl/vol33/4/art/opuscula_math_3337.pdf .
4. J. E. Jamison, A. Kamińska, G. Lewicki, *One-complemented subspaces of Musielak--Orlicz sequence spaces*, J. Approx. Theory 130 (2004), 1–37, DOI: 10.1016/j.jat.2004.07.001.
5. A. Kamińska, G. Lewicki, *Contractive and optimal sets in modular spaces*, Math. Nachr. 268 (2004), 74–95, DOI: 10.1002/mana.200310160.
