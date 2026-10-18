# Sharp tame-defect laws and rigidity for radial \(\ell_p\) extensions

## Finding

Let \(1<p<\infty\), let \(F\ne\{0\}\) be a finite-dimensional real Banach space, and let \(X=F\times\ell_p(\mathbb N;\mathbb R)\) carry a Banach norm \(\|(f,v)\|_X=\varphi(f,\|v\|_p)\) whose restriction to \(\{0\}\times\ell_p\) is the standard \(\ell_p\)-norm, so \(\varphi(0,s)=s\). The function \(\varphi(f,s)\) is the norm of \((f,se_1)\); no differentiability, convexity formula, or special formula for its dependence on \(f\) is assumed beyond the existence of the stated Banach norm.

Following the inequality in Shkarin's Definition 3, define its least **multiplicative tame-defect constant** by
\[
\mathfrak T(X)=\sup_{\substack{x\ne0,\,y\in X\\u_n\rightharpoonup0}}
\frac{\displaystyle\limsup_{n\to\infty}\frac{\|y+u_n\|_X}{\|x+u_n\|_X}}{\displaystyle\max\{1,\|y\|_X/\|x\|_X\}}.
\]
Every weakly null sequence is bounded; the quotient is eventually well-defined because \(\liminf\|x+u_n\|_X\ge\|x\|_X>0\). Taking \(x=y\) shows \(\mathfrak T(X)\ge1\), and the space is tame exactly when \(\mathfrak T(X)=1\).

**Theorem (scalar reduction, rigidity, and sharp mixed-sum law).** Define
\[
R_a(f,s)=\varphi\bigl(f,(s^p+a^p)^{1/p}\bigr),\qquad a,s\ge0.
\]
Then the entire infinite-dimensional defect is exactly the following scalar variational expression:
\[
\boxed{\mathfrak T(X)=\sup_{\substack{a,s,t\ge0,\ f,g\in F\\\varphi(f,s)>0}}
\frac{R_a(g,t)}{R_a(f,s)\,\max\{1,\varphi(g,t)/\varphi(f,s)\}}.}
\tag{1}
\]
Moreover, \(X\) is tame if and only if
\[
\boxed{\varphi(f,s)=\bigl(\varphi(f,0)^p+s^p\bigr)^{1/p}
\quad\text{for all }f\in F,\ s\ge0.}
\tag{2}
\]
For the particularly natural mixed-direct-sum family \(X=F\oplus_q\ell_p\), \(1\le q\le\infty\), the exact quantitative law is
\[
\boxed{\mathfrak T(F\oplus_q\ell_p)=2^{|1/p-1/q|},\qquad 1/\infty:=0.}
\tag{3}
\]
The supremum in (3) is attained by explicit unit vectors and a weakly null sequence. Thus (3) is sharp for **every** nonzero finite-dimensional real \(F\), regardless of its norm or dimension.

## Assumptions and scope

The scalar field is real. The tail is the infinite sequence space \(\ell_p\) with \(1<p<\infty\), so its coordinate vectors converge weakly to zero. The finite block \(F\) has positive finite dimension but is otherwise arbitrary. Radiality means exactly that the norm depends on the infinite tail only through its \(\ell_p\)-norm. The mixed sum \(F\oplus_q\ell_p\) uses \((\|f\|_F^q+\|v\|_p^q)^{1/q}\) for finite \(q\), and the maximum for \(q=\infty\). All suprema range over arbitrary bounded weakly null sequences, not merely disjointly supported examples. The formula is NOT claimed for arbitrary, nonradial extensions, for finite-dimensional tails, or for \(p=1\).

## Proof

**1. A weak-null disjointness lemma.** Suppose \(w_n\rightharpoonup0\) in \(\ell_p\), and \(v\in\ell_p\) is fixed. Then
\[
\|v+w_n\|_p^p-\|w_n\|_p^p\longrightarrow\|v\|_p^p.\tag{4}
\]
Indeed \(w_n\) is bounded and every fixed coordinate converges to zero. For finitely supported \(v\), (4) follows by separating its support from the unchanged remaining coordinates. For general \(v\), approximate in \(\ell_p\) by its first \(m\) coordinates and use the locally Lipschitz behavior of the \(p\)-th power of a norm uniformly on bounded balls; then let \(m\to\infty\). This supplies the needed infinite-dimensional limit without assuming disjoint supports.

**2. Exact reduction.** A weakly null sequence \(u_n=(h_n,w_n)\) in \(X\) has \(h_n\to0\) in \(F\) (finite dimensionality). Any subsequence along which the ratio in the definition of \(\mathfrak T(X)\) approaches its limsup admits a further subsequence on which \(\|w_n\|_p\to a\ge0\). For each fixed \((f,v)\), (4) and continuity of the norm give
\[
\|(f,v)+u_n\|_X\longrightarrow
\varphi\bigl(f,(\|v\|_p^p+a^p)^{1/p}\bigr).
\]
Applying this simultaneously to \(x,y\) proves the **upper bound** in (1). Conversely, choose arbitrary \(f,g\in F\), radii \(s,t,a\ge0\), vectors \(v=se_1\), \(z=te_1\), and the weakly null sequence \(u_n=(0,ae_{n+1})\). For every \(n\), disjoint supports give **exactly** \(\|(f,v)+u_n\|=R_a(f,s)\) and \(\|(g,z)+u_n\|=R_a(g,t)\). This gives the reverse bound. No compactness or attainment of the scalar supremum is required.

**3. Rigidity at the tame threshold.** Fix any nonzero \(f\in F\) and write \(b=\varphi(f,0)>0\). Consider the equal-norm vectors \(x=(f,0)\) and \(y=(0,be_1)\). With \(u_n=(0,ae_{n+1})\), the two respective perturbation norms are \(\varphi(f,a)\) and \((b^p+a^p)^{1/p}\). If \(\mathfrak T(X)=1\), applying the tame inequality with \(x,y\) in both orders forces equality for every \(a\ge0\). When \(f=0\) equality holds by tail normalization. Hence (2) follows for all \(f,a\). Conversely (2) identifies \(X\) as the isometric \(p\)-sum \(F\oplus_p\ell_p\). The weak-null identity (4) together with \(h_n\to0\) shows that for any fixed \(z\) and weakly null \(u_n\),
\[
\|z+u_n\|_X^p-\|z\|_X^p-\|u_n\|_X^p\longrightarrow0.
\]
This implies the tame inequality (for example along any subsequence realizing the required limsup), so \(\mathfrak T(X)=1\). No use of a putative converse from a norm-attainment theorem is made.

**4. Mixed sums: universal upper bound.** Fix \(1\le q\le\infty\), write \(r=\min\{p,q\}\), \(s=\max\{p,q\}\), and interpret the \(s=\infty\) expression as a maximum. For \(z=(f,v)\), let \(B=\|z\|_X\). The scalar weak-null profile for \(F\oplus_q\ell_p\) is
\[
M_a(z)=\begin{cases}
\bigl(\|f\|_F^q+(\|v\|_p^p+a^p)^{q/p}\bigr)^{1/q},&q<\infty,\\
\max\{\|f\|_F,(\|v\|_p^p+a^p)^{1/p}\},&q=\infty.
\end{cases}
\]
The following **two-sided mixed-norm comparison** is sharp:
\[
\boxed{(B^s+a^s)^{1/s}\le M_a(z)\le(B^r+a^r)^{1/r}.}\tag{5}
\]
For \(q\ge p\), the left inequality follows from \((b^p+a^p)^{q/p}\ge b^q+a^q\); the right inequality is the triangle inequality in \(\ell_{q/p}^2\) applied to \((\|f\|_F^p,\|v\|_p^p)\) and \((0,a^p)\). For \(q\le p\), the right inequality follows from \((b^p+a^p)^{q/p}\le b^q+a^q\); the left inequality is the triangle inequality in \(\ell_{p/q}^2\) applied to \((\|f\|_F^q,0)\) and \((\|v\|_p^q,a^q)\). The \(q=\infty\) case follows immediately from maxima and \(p\)-powers. In these comparisons \(b=\|v\|_p\).

Given \(x\ne0,y\in X\) and \(a\ge0\), write \(b=\|x\|_X>0\) and \(c=\|y\|_X\). If \(c\le b\), (5) gives
\[
\frac{M_a(y)}{M_a(x)\max\{1,c/b\}}
\le\frac{(b^r+a^r)^{1/r}}{(b^s+a^s)^{1/s}}.
\]
If \(c\ge b\), (5) and monotonicity of the function \(u\mapsto(1+u^r)^{1/r}\) give the same bound after dividing by \(c/b\). Consequently
\[
\mathfrak T(X)\le\sup_{t\ge0}
\frac{(1+t^r)^{1/r}}{(1+t^s)^{1/s}}.
\]
For finite \(s\), the logarithmic derivative has the sign of \(t^{r-1}-t^{s-1}\), hence the maximum is at \(t=1\), where it is \(2^{1/r-1/s}\). For \(s=\infty\) the denominator is \(\max\{1,t\}\), which gives the same maximum at \(t=1\).

**5. Equality construction.** Choose \(f_0\in F\) with \(\|f_0\|_F=1\), let \(A=(f_0,0)\), \(B=(0,e_1)\), and \(u_n=(0,e_{n+1})\). Both \(A,B\) are unit vectors, and \(u_n\rightharpoonup0\). For each \(n\),
\[
\|A+u_n\|_X=2^{1/q},\qquad \|B+u_n\|_X=2^{1/p}.
\]
Use \((x,y)=(A,B)\) when \(p\le q\), and interchange them when \(q<p\). The ratio is exactly \(2^{|1/p-1/q|}\). This proves (3) including both endpoint exponents and the dimension-independent sharpness.

## Verification

The proof of (1) uses only finite-head approximation, weak compactness of bounded scalar sequences, and disjoint standard basis vectors. The upper bound in (3) was separately checked against a deterministic array of mixed-sum parameters and random positive coordinates using the standalone `CHECK.py`; that finite experiment corroborates, but does not replace, the analytic inequalities. For \(p=2,q=1\), both the upper bound and explicit construction give \(\sqrt2\). For \(p=2,q=\infty\), both give \(\sqrt2\); for \(p=q\), all formulas give exactly one. The checker and its deterministic settings are included in the package.

## Relationship to prior work

Kalton and Werner (1993), Section 1 and Definition 2.1, introduce property \((M)\), comparing \(\limsup\|z+u_n\|\) for equal-norm \(z\) under weak-null perturbations, and Section 4 studies property \((m_p)\) and almost-isometric embeddings. Their general equal-norm principle is closely related to the rigidity part (2); it is **not** claimed new that property \((M)\) exists. Shkarin (2012), Definition 3, introduces the ratio-based tame condition, proves \(p\)-spaces tame, and raises the characterization question. His Section 5 already uses asymptotic radial splitting for proper Hilbert extensions, and his Section 4 computes an operator norm involving the same exponent \(2^{1/p-1/q}\) in a different norm-attainment problem. His Section 4 also derives an operator norm involving \(2^{1/p-1/q}\) in the case \(p<q\); the coincidence of this numerical exponent is not claimed new. His Theorem 1.8 already shows that scalar \(\ell_q\)-extensions of \(\ell_p\) with \(q\ne p\) can fail compact-perturbation norm attainment; the mere qualitative failure of tameness in these examples is therefore **not** presented as new. The present claim is the exact full radial variational reduction (1), its isometric rigidity consequence (2), and the sharp quantitative all-parameter constant (3), none of which is stated in the inspected passages of these sources. The corresponding earlier results must not be inferred to be absent from uninspected works.

## Limitations

This is a statement about real, finite-dimensional, normalized **radial** extensions of infinite \(\ell_p\) for \(1<p<\infty\); it neither classifies general tame Banach spaces nor settles the open characterization problem in full. The multiplicative defect is defined directly from Shkarin's condition, not asserted to be an established standard invariant. The scalar supremum (1) need not be achieved for arbitrary \(\varphi\). The supporting finite numerical examples do not establish any infinite-dimensional result. Independent mathematical and bibliographic verification has not been performed. A bibliographic possibility remains that an earlier paper derives an equivalent radial characterization or mixed-norm sharp defect using different terminology.

## References

1. Nigel J. Kalton and Dirk Werner, *Property (M), M-ideals, and almost isometric structure of Banach spaces*, arXiv:math/9310216v1 (first posted 11 October 1993); https://arxiv.org/abs/math/9310216 ; Sections 1–4 and Definition 2.1.
2. Stanislav Shkarin, *Norm attaining operators and pseudospectrum*, arXiv:1209.1218v1 (first posted 6 September 2012); https://arxiv.org/abs/1209.1218 ; Definition 2, Theorem 1.8, Definition 3 and Proposition 7.1.
