# Exact asymptotic moduli and an attained–unattained extremal split in Nakano sequence spaces

## Finding

Let \(1<p_n\le P<\infty\) for every \(n\ge1\), where \(p_n\to1\), and equip the real Nakano sequence space \(X=\ell_{(p_n)}\) with its Luxemburg norm. Set \(P=\max_n p_n\), which is attained because the exponents converge to \(1\) but remain strictly greater than \(1\).

For each \(x\in S_X\) and \(0<t\le1\), let \(L_x(t)>1\) be the unique solution of
\[
\sum_{n=1}^{\infty}\frac{|x_n|^{p_n}}{L_x(t)^{p_n}}+\frac{t}{L_x(t)}=1.
\]
The pointwise asymptotic uniform convexity and smoothness moduli agree **exactly**:
\[
\overline\delta_X(t;x)=\overline\rho_X(t;x)=L_x(t)-1.
\]
The corresponding global moduli are **different**:
\[
\boxed{\overline\delta_X(t)=L_P(t)-1,\qquad \overline\rho_X(t)=t,}
\]
where \(L_P(t)>1\) is the unique root of \(L_P(t)^{-P}+t/L_P(t)=1\). The minimum defining \(\overline\delta_X(t)\) is achieved **exactly** by those unit vectors supported on \(\{n:p_n=P\}\); the supremum defining \(\overline\rho_X(t)\) is **never** achieved by a fixed unit vector, but is approached by the coordinate unit vectors \(e_n\) as \(n\to\infty\).

Consequently, \(X\) is asymptotically uniformly convex but has the maximal possible asymptotic uniform smoothness modulus, so it is not asymptotically uniformly smooth in its specified norm. Its Kottman separation constant equals \(2\). For the natural example \(p_n=1+1/n\), one obtains \(P=2\) and
\[
\overline\delta_X(1)=\frac{\sqrt5-1}{2},\qquad
\overline\rho_X(1)=1,\qquad K(X)=2.
\]

## Assumptions and scope

The ground field is \(\mathbb R\), and coordinates are indexed by the positive integers. The Luxemburg modular and norm are defined by
\[
\Phi(z)=\sum_{n\ge1}|z_n|^{p_n},\qquad
\|z\|=\inf\{s>0:\Phi(z/s)\le1\}.
\]
The space consists of sequences of finite Luxemburg norm. Uniform upper and lower exponent bounds \(1<p_n\le P<\infty\) guarantee that every nonzero \(z\in X\) satisfies \(\Phi(z/\|z\|)=1\), that coordinate truncations converge in norm, and that coordinate projections are norm-one contractions.

For \(x\in S_X\) and \(0<t\le1\), the precise moduli are
\[
\overline\delta_X(t;x)=\sup_{\operatorname{codim}Y<\infty}\ \inf_{y\in Y,\,\|y\|\ge t}\bigl(\|x+y\|-1\bigr),
\]
\[
\overline\rho_X(t;x)=\inf_{\operatorname{codim}Y<\infty}\ \sup_{y\in Y,\,\|y\|\le t}\bigl(\|x+y\|-1\bigr).
\]
Here all \(Y\) are closed linear subspaces of finite codimension. The global moduli take the infimum and supremum, respectively, over \(x\in S_X\). These definitions agree with the standard asymptotic moduli in the cited background literature. The claim concerns **the original Luxemburg norm**; it makes no statement about equivalent renormings, optimality under renorming, or nonexpansive-mapping convergence rates.

## Proof

**1. Modular normalization.** For a nonzero vector \(z\), write \(s=\|z\|\). The bounds on the exponents imply continuity of \(\Phi(z/u)\) at \(u=s\): for \(u\) in any fixed interval strictly above zero, the terms are dominated by a constant times a summable modular evaluation. At the norm infimum, strict monotonicity then gives \(\Phi(z/s)=1\). In particular, \(\Phi(x)=1\) whenever \(x\in S_X\).

**2. Uniform tail root.** Define \(E_N=\{z:z_1=\cdots=z_N=0\}\), let \(x^{(N)}=(x_1,\ldots,x_N,0,\ldots)\), and put \(\epsilon_N=\sup_{n>N}(p_n-1)\), which tends to zero. For any \(y\in E_N\) with \(\|y\|=t\), the normalization in step 1 gives \(\Phi(y/t)=1\). For every \(u>\max\{1,t\}\), the number \(r=t/u\) lies in \((0,1)\), and hence
\[
 r^{1+\epsilon_N}\ \le\ \Phi(y/u)\ =\sum_{n>N}r^{p_n}|y_n/t|^{p_n}\ \le\ r.
\]
Since \(x^{(N)}\) and \(y\) have disjoint supports, \(\Phi((x^{(N)}+y)/u)=\Phi(x^{(N)}/u)+\Phi(y/u)\). As \(N\to\infty\), the first term converges to \(\Phi(x/u)\) while both bounds on the second converge to \(t/u\), **uniformly in the choice of the normalized tail vector**. The function \(u\mapsto\Phi(x/u)+t/u\) is continuous and strictly decreasing from a value exceeding \(1\) at \(u=\max\{1,t\}\) to \(0\) at infinity; it therefore has the unique root \(L_x(t)>\max\{1,t\}\). Evaluate the preceding bounds at any two fixed numbers \(u_-<L_x(t)<u_+\) with \(u_->\max\{1,t\}\). Eventually the modular of \(x^{(N)}+y\) at \(u_-\) exceeds \(1\) and at \(u_+\) is less than \(1\), uniformly over the tail sphere. Consequently,
\[
\sup_{y\in E_N,\,\|y\|=t}\bigl|\|x^{(N)}+y\|-L_x(t)\bigr|\longrightarrow0.
\]
The triangle inequality and \(\|x-x^{(N)}\|\to0\) yield the same uniform limit with \(x\) in place of \(x^{(N)}\).

**3. Finite-codimensional quantifiers.** For every closed finite-codimensional \(Y\) and every \(N\), the intersection \(Y\cap E_N\) contains nonzero vectors: an infinite-dimensional tail cannot be injected into the finite-dimensional quotient \(X/Y\). Thus \(Y\cap E_N\) contains a vector of norm exactly \(t\). The uniform tail root supplies the bound
\[
\inf_{y\in Y,\,\|y\|\ge t}\|x+y\|\le L_x(t)
\]
by sending \(N\to\infty\), and likewise
\[
\sup_{y\in Y,\,\|y\|\le t}\|x+y\|\ge L_x(t).
\]
For the reverse inequalities, take \(Y=E_N\). If \(\|y\|\ge t\), then the coordinatewise lattice inequality
\[
|x^{(N)}+(t/\|y\|)y|\le|x^{(N)}+y|
\]
implies \(\|x^{(N)}+y\|\ge\|x^{(N)}+(t/\|y\|)y\|\). Similarly, when \(\|y\|\le t\), enlarge \(y\) to norm \(t\) without decreasing \(\|x^{(N)}+y\|\). Together with the approximation \(\|x-x^{(N)}\|\to0\) and step 2, this proves the exact pointwise formulas for both moduli.

**4. Global extremes and equality.** For any \(u>1\), normalization gives
\[
\Phi(x/u)=\sum_n |x_n|^{p_n}u^{-p_n}\ge u^{-P}\sum_n|x_n|^{p_n}=u^{-P}.
\]
Equality holds precisely when \(x_n=0\) for every \(n\) with \(p_n<P\). Comparing the unique roots of this inequality plus \(t/u\) proves \(L_x(t)\ge L_P(t)\) and the stated complete set of minimizers. Conversely, strict \(p_n>1\) and \(\Phi(x)=1\) imply \(\Phi(x/u)<u^{-1}\) for every \(u>1\). At \(u=1+t\), the root expression is therefore strictly less than \(1\), proving \(L_x(t)<1+t\) for every fixed \(x\in S_X\). Yet with \(x=e_n\) the equation becomes \(u^{-p_n}+t/u=1\), and \(p_n\to1\) forces \(L_{e_n}(t)\to1+t\). Thus the global supremum equals \(t\), but no \(x\) achieves it.

**5. Consequences and boundary example.** The root \(L_P(t)\) is strictly greater than \(1\), so the space is asymptotically uniformly convex. The identity \(\overline\rho_X(t)=t\) prevents asymptotic uniform smoothness. For \(i,j\to\infty\) with \(i\ne j\), \(\|e_i-e_j\|\to2\) follows directly from \(u^{-p_i}+u^{-p_j}=1\) and \(p_i,p_j\to1\). The upper bound \(K(X)\le2\) is the triangle inequality, so \(K(X)=2\). When \(p_n=1+1/n\), \(P=2\) at the first coordinate, and the equation \(u^{-2}+u^{-1}=1\) gives \(u=(1+\sqrt5)/2\), yielding the displayed exact moduli.

## Verification

The proof is self-contained modulo elementary facts about the Luxemburg norm and finite-codimensional subspaces, which are justified in the steps above. A supplementary deterministic checker, `check_moduli.py`, normalizes finite-support vectors, solves the defining scalar equations by bisection, and compares them with far-tail perturbations for several parameter values and a mixed-exponent vector. The checker passes; numerical convergence is corroboration and is **not** used as proof of the infinite-dimensional or all-subspace statements. The root and all boundary quantifiers are established analytically.

## Relationship to prior work

Domínguez Benavides, Japón, and Lin (2026), arXiv:2610.10928v1, establish the fixed-point property for variable-exponent Lebesgue spaces under conditions encompassing the present Nakano examples and develop a projection-scheme approach, but their results on fixed points and one-sided disjoint-sum estimates do not give these exact pointwise/global asymptotic modulus formulas. Gonzalo, Jaramillo, and Troyanski (2007) give the standard definitions, finite-codimensional/tail techniques, and different Nakano smoothness results in the regime of exponents tending to an even integer. Georgiev, Zhelinski, and Zlatanov (2026), arXiv:2603.28404v2, study variational principles and Fréchet smoothness of Nakano and Musielak–Orlicz spaces, not these exact asymptotic moduli. Delpech (2009) studies asymptotic moduli and the Kottman constant of (single-function) Orlicz sequence spaces; full text was unavailable for comparison. No priority or exhaustive-literature claim is made from that restricted access.

The formula for the standard constant-exponent space \(\ell_p\), namely \((1+t^p)^{1/p}-1\) for both global moduli, is well known. It does **not** imply the present variable-exponent and attainment statements: the tail exponent determines the pointwise limiting equation, whereas the largest head exponent determines the global convexity extremizers.

## Limitations

The exact formulas require bounded exponents converging to \(1\), with all coordinates strictly above \(1\), and the **specified** Luxemburg norm. They are not claimed for general variable-exponent functions, arbitrary Musielak–Orlicz modulars, arbitrary pointwise infimum-exponent patterns, or equivalent norms. They do not provide a new fixed-point theorem. Although relevant public literature and research records were searched, unpublished or unindexed equivalents remain a priority risk. In particular, full-text comparison with Delpech (2009) could not be completed; only its abstract and bibliographic records were available. Independent mathematical review has not been performed.

## References

1. T. Domínguez Benavides, M. Japón, P. K. Lin, *Projection schemes and the fixed point property in nonreflexive Banach spaces*, arXiv:2610.10928v1 (first public version 7 October 2026), https://arxiv.org/abs/2610.10928.
2. R. Gonzalo, J. A. Jaramillo, S. L. Troyanski, *High Order Smoothness and Asymptotic Structure in Banach Spaces*, Journal of Convex Analysis **14** (2007), 249–269, https://www.heldermann-verlag.de/jca/jca14/jca0589_b.pdf.
3. P. Georgiev, V. Zhelinski, B. Zlatanov, *Perturbation Method in Musielak-Orlicz Sequence Spaces*, arXiv:2603.28404v2 (2 April 2026), https://arxiv.org/abs/2603.28404.
4. S. Delpech, *Asymptotic uniform moduli and Kottman constant of Orlicz sequence spaces*, Revista Matemática Complutense **22** (2009), 455–467, https://doi.org/10.5209/rev_REMA.2009.v22.n2.16285 (abstract and bibliographic information inspected; primary full text unavailable).
