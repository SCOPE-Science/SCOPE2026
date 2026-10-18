# Exact affine ReLU variation norm and its bias–slope transition

## Finding

**Theorem (exact affine norm and sparsity transition).** Let \(H\) be any real separable Hilbert space and \(\sigma(t)=\max\{t,0\}\). On functions \(f:H\to\mathbb R\), consider the bias-penalizing ReLU variation norm
\[
\|f\|_{\mathrm V}=\inf\left\{\|\mu\|_{\mathrm{TV}}:\ f(x)=\int_{\beta^2+\|h\|^2\le1}\sigma(\beta+\langle h,x\rangle)\,d\mu(\beta,h)\quad\text{for every }x\in H\right\},
\]
where the infimum is over finite signed Borel measures on the weakly compact unit ball of \(\mathbb R\oplus H\). Set \(f_{a,b}(x)=\langle a,x\rangle+b\), \(s=\|a\|\), and \(B=|b|\). Then
\[
\boxed{\|f_{a,b}\|_{\mathrm V}=\min_{c\in\mathbb R}\left\{|c|+2\sqrt{s^2+(b-c)^2}\right\}
=\begin{cases}
2\sqrt{s^2+B^2},&0\le B\le s/\sqrt3,\\
B+\sqrt3\,s,&B\ge s/\sqrt3.
\end{cases}}
\]
The two expressions agree at the threshold. If \(s>0\), the least number of atoms in a norm-minimizing signed measure is exactly two when \(B\le s/\sqrt3\) and exactly three when \(B>s/\sqrt3\). If \(s=0\) and \(b\ne0\), one atom suffices and is necessary; the zero function requires none. All assertions hold on the entire, generally unbounded input space, not merely on a prescribed compact interval.

## Assumptions and scope

The Hilbert space is real and separable; scalar outputs and the **joint Euclidean** parameter norm \(\beta^2+\|h\|^2\le1\) are essential. The representation is an equality at every input, with neither an unpenalized affine skip connection nor a free bias. Signed-measure total variation is the cost. The infimum is attained by the explicitly constructed finite atomic measures below. The model coincides with the scalar-output specialization of the unit-ball variation space in Yang and Shi's Definition 2.1 [1]. This result does not claim the same formula for other parameter norms, compact-domain equivalence classes, or arbitrary nonlinear functions.

## Proof

**Step 1: Reduction to one variable.** If \(s=0\), evaluation at \(x=0\) gives \(|b|\le\|\mu\|_{\mathrm{TV}}\), since \(0\le\sigma(\beta)\le1\) on the parameter ball. The signed atom \(b\delta_{(1,0)}\) attains that cost. Now suppose \(s>0\) and put \(u=a/s\). Restrict any representation to \(x=tu\), \(t\in\mathbb R\). Push \(\mu\) forward under the continuous contraction \((\beta,h)\mapsto(\beta,\langle h,u\rangle)\). This map sends the Hilbert unit ball into the Euclidean unit disk and cannot increase total variation. On the line the target is \(st+b\). Thus a scalar one-variable lower bound is a valid lower bound in every \(H\).

**Step 2: Necessary measure identities.** Let \(\nu\) be an arbitrary finite signed representing measure on \(\{(\beta,w):\beta^2+w^2\le1\}\) for \(x\mapsto sx+b\). Its part on \(w=0\) contributes the constant
\[
c=\int_{\{w=0\}}\sigma(\beta)\,d\nu(\beta,w),\qquad |c|\le\|\nu\|_{\mathrm{TV},\{w=0\}}.
\]
On \(w>0\), push the signed measure \(w\,d\nu\) under \(t=-\beta/w\) to a signed measure \(\alpha_+\). On \(w<0\), push \((-w)\,d\nu\) under the same map to \(\alpha_-\). Because \(\sigma(\beta+wx)=w\sigma(x-t)\) for \(w>0\), and \(\sigma(\beta+wx)=(-w)\sigma(t-x)\) for \(w<0\),
\[
sx+b=c+\int_{\mathbb R}(x-t)_+\,d\alpha_+(t)+\int_{\mathbb R}(t-x)_+\,d\alpha_-(t).
\]
The first absolute moments exist, and the Euclidean ball constraint gives for each sign
\[
\int_{\mathbb R}\sqrt{1+t^2}\,d|\alpha_\pm|(t)\le\|\nu\|_{\mathrm{TV},\{\pm w>0\}},
\]
since \(|w|\sqrt{1+(\beta/w)^2}=\sqrt{w^2+\beta^2}\le1\). In the sense of distributions, differentiating the displayed integral twice shows \(\alpha_++\alpha_-=0\), because the target is affine. Therefore \(\alpha_-=-\alpha_+\). Using the identity \((x-t)_+-(t-x)_+=x-t\),
\[
s=\int d\alpha_+\quad\text{and}\quad b=c-\int t\,d\alpha_+.
\]
Combining the cost of the two signs and the constant part, then applying the triangle inequality for the Euclidean norm to the finite signed vector measure \((1,t)\,d\alpha_+\), yields
\[
\|\nu\|_{\mathrm{TV}}\ge |c|+2\int\sqrt{1+t^2}\,d|\alpha_+|(t)
\ge |c|+2\sqrt{\left(\int d\alpha_+\right)^2+\left(\int t\,d\alpha_+\right)^2}
=|c|+2\sqrt{s^2+(b-c)^2}.
\]
This argument applies to **arbitrary signed measures**, not just finite networks, and proves the claimed lower bound after taking the infimum over \(c\).

**Step 3: Exact scalar minimization.** By reflection of signs, assume \(b\ge0\). The convex function \(F(c)=|c|+2\sqrt{s^2+(b-c)^2}\) decreases for \(c<0\) and increases for \(c>b\); its minimizer lies in \([0,b]\). In the interior,
\[
F'(c)=1-\frac{2(b-c)}{\sqrt{s^2+(b-c)^2}}.
\]
The unique stationary point is \(c=b-s/\sqrt3\), which is feasible exactly when \(b>s/\sqrt3\). Otherwise \(c=0\) is optimal. Substitution gives the two exact branches. At equality the minimizing constant contribution is still zero.

**Step 4: Matching finite atomic measure.** Define
\[
c_*=\operatorname{sgn}(b)\max\{B-s/\sqrt3,0\},\qquad t_*=-\frac{b-c_*}{s},\qquad q=\sqrt{1+t_*^2},\qquad u=\frac as.
\]
The two parameters \(p_+=(-t_*/q,u/q)\) and \(p_-=(t_*/q,-u/q)\) lie on the unit sphere of \(\mathbb R\oplus H\). The signed atomic measure
\[
\mu_*=s q\,\delta_{p_+}-s q\,\delta_{p_-}+c_*\,\delta_{(1,0)}
\]
represents \(f_{a,b}\) at every \(x\) because \(\sigma(z)-\sigma(-z)=z\). Its total variation is \(2sq+|c_*|\), equal to the lower bound; the three support locations are distinct for \(s>0\). For \(s=0\), use \(b\delta_{(1,0)}\). This also proves attainment.

**Step 5: Minimum atom count.** For \(s>0\), one ReLU atom cannot equal a nonconstant affine function on all \(H\), since any nonconstant ReLU has a nonempty kink hyperplane. For a two-atom representation of a nonconstant affine function, the one-variable distributional second-derivative argument forces a nontrivial positive- and negative-slope pair with the same kink; no flat (constant) atom can be present. Hence such a representation necessarily has \(c=0\), so the optimal possible cost with two atoms is \(2\sqrt{s^2+B^2}\). When \(B>s/\sqrt3\), this strictly exceeds the three-atom optimum, while the displayed construction has exactly three atoms. When \(B\le s/\sqrt3\), it has exactly two atoms, which is minimal. The constant and zero cases were handled at the start.

## Verification

The proof is exact and uses no numerical inference. A standalone Python checker, `affine_variation_check.py`, independently calculates the two-branch value and the minimizing scalar cost on a finite grid, compares each with numerical scalar minimization, and evaluates the explicit atomic representation on an input grid. It currently tests 99 parameter pairs and 792 representation points. These finite tests are diagnostics, not proofs of the measure-theoretic lower bound or the universal claim. Run with `python affine_variation_check.py`; Python 3 and SciPy are required.

## Relationship to prior work

Yang–Shi [1, Definition 2.1] introduce the augmented Hilbert-unit-ball variation norm and [1, Proposition 2.4 and Appendix D] prove its **homogeneous linear** Schatten–one formula, which in scalar output reads \(\|x\mapsto\langle a,x\rangle\|_{\mathrm V}=2\|a\|\). This existing result is not claimed as new. The present theorem determines the genuinely biased affine case, including a strict two-branch transition and minimal atomic support count. Inspection of the relevant original introduction, variation-space section, Proposition 2.4 and Appendix D did not locate an affine formula.

E–Wojtowytsch [2, §§2 and 4.1, especially Remark 4.2] give the parameter-measure and signed-kink descriptions of classical Barron functions and describe the one-dimensional space through an **equivalent** weighted bounded-variation norm. Their equivalence does not imply the sharp two-branch unit-ball variation **equality** here, although their measure decomposition is closely related to Step 2. Shenouda–Parhi–Lee–Nowak [3] develop vector-valued variation spaces and representer theorems; the identified material does not provide this full-line scalar affine calculation. Older treatments with unpenalized biases, free affine skips, compact input domains or \(\ell_1\)-type parameter costs are not identical claims.

## Limitations

No extension to nonlinear targets, general vector output, different parameter norms, or equality only on a compact domain is asserted. The exact result follows from the signed measure model and all-input quantification; relaxing either can change the optimum. The conclusion is a mathematical priority assessment under inspected available sources, not an independent publication-priority certification. Earlier equivalent statements using a different neural-network norm convention remain a residual bibliographic risk.

## References

[1] Jia-Qi Yang and Lei Shi, *Variation Spaces for Encoder–Decoder Neural Operators: Approximation and Generalization*, arXiv:2606.01244v2 (first public version May 31, 2026), https://arxiv.org/abs/2606.01244.

[2] Weinan E and Stephan Wojtowytsch, *Representation formulas and pointwise properties for Barron functions*, arXiv:2006.05982v2, https://arxiv.org/html/2006.05982v2.

[3] Joseph Shenouda, Rahul Parhi, Kangwook Lee, and Robert D. Nowak, *Variation Spaces for Multi-Output Neural Networks: Insights on Multi-Task Learning and Network Compression*, JMLR 25 (2024), https://www.jmlr.org/beta/papers/v25/23-0677.html.

[4] Pedro Savarese, Itay Evron, Daniel Soudry, and Nathan Srebro, *How do infinite width bounded norm networks look in function space?*, COLT/PMLR 99 (2019), https://proceedings.mlr.press/v99/savarese19a.html.
