# Exact Zbăganu phase diagram of the Banaś--Frączek plane
## Finding
For \(\lambda>1\), let \(R_\lambda^2=(\mathbb R^2,N_\lambda)\) be the real Banaś--Frączek plane
\[
N_\lambda(u,v)=\max\left\{\lambda|u|,\sqrt{u^2+v^2}\right\}.
\]
Then
\[
C_Z(R_\lambda^2)=
\begin{cases}
\lambda,&1<\lambda\le\sqrt2,\\[2mm]
2\sqrt{1-\lambda^{-2}},&\lambda\ge\sqrt2.
\end{cases}
\]
The complete maximizing set undergoes a phase transition at \(\lambda=\sqrt2\). For \(1<\lambda<\sqrt2\), every maximizer is equivalent under the signed-coordinate symmetries, vector sign changes, and order reversal to
\[
x=r\cos\alpha\,(\cos\alpha,\sin\alpha),\qquad
y=r\sin\alpha\,(-\sin\alpha,\cos\alpha),
\]
with \(r>0\) and
\[
\arccos(\lambda^{-1})\le\alpha\le\arcsin(\lambda^{-1}).
\]
At \(\lambda=\sqrt2\) only \(\alpha=\pi/4\) remains. For \(\lambda>\sqrt2\), every maximizer is equivalent to
\[
x=r\left(1,\sqrt{\lambda^2-1}\right),\qquad
y=r\left(-1,\sqrt{\lambda^2-1}\right),
\qquad r\ne0.
\]

## Assumptions and scope
The scalar field is real. The Zbăganu constant is
\[
C_Z(X)=
\sup_{\substack{x,y\in X\\(x,y)\ne(0,0)}}
\frac{\|x+y\|\,\|x-y\|}{\|x\|^2+\|y\|^2}.
\]
Write
\[
E(u,v)=\sqrt{u^2+v^2},
\qquad
F(u,v)=\lambda|u|,
\qquad
N_\lambda=\max\{E,F\}.
\]
The unit ball is the intersection of the Euclidean unit disk with the vertical strip \(|u|\le\lambda^{-1}\).

## Proof
Fix \(0\le\theta\le1\). Since a maximum dominates every convex combination,
\[
N_\lambda(z)^2
\ge
\theta E(z)^2+(1-\theta)F(z)^2.
\]
For \(z=(z_1,z_2)\), put
\[
A_\theta=\lambda^2-(\lambda^2-1)\theta.
\]
Then
\[
N_\lambda(z)^2\ge A_\theta z_1^2+\theta z_2^2.
\]

Take arbitrary \(x,y\) and put
\[
p=x+y,\qquad q=x-y,
\qquad
D=N_\lambda(x)^2+N_\lambda(y)^2.
\]
Because \(N_\lambda=\max\{E,F\}\),
\[
N_\lambda(p)N_\lambda(q)
=
\max\{E(p)E(q),\,E(p)F(q),\,F(p)E(q),\,F(p)F(q)\}.
\]

The pure Euclidean branch satisfies
\[
E(p)E(q)
\le
\frac{E(p)^2+E(q)^2}{2}
=
E(x)^2+E(y)^2
\le D.
\]
The pure strip branch satisfies
\[
F(p)F(q)
=
\lambda^2|x_1^2-y_1^2|
\le
\lambda^2(x_1^2+y_1^2)
\le D.
\]

It remains to bound a mixed branch. By the quadratic lower bound and the parallelogram identity for that quadratic form,
\[
D
\ge
\frac12\left(
A_\theta p_1^2+\theta p_2^2+
A_\theta q_1^2+\theta q_2^2
\right).
\]
Discarding the nonnegative \(\theta q_2^2\) term and applying the arithmetic--geometric mean inequality,
\[
D
\ge
|q_1|\sqrt{
A_\theta\left(A_\theta p_1^2+\theta p_2^2\right)}.
\]
Hence
\[
\frac{E(p)F(q)}{D}
\le
\frac{\lambda\sqrt{p_1^2+p_2^2}}
{\sqrt{A_\theta\left(A_\theta p_1^2+\theta p_2^2\right)}}
\le
\frac{\lambda}{\sqrt{A_\theta\theta}},
\]
because \(A_\theta\ge\theta\). The same bound holds for \(F(p)E(q)\).

Now
\[
A_\theta\theta
=
\lambda^2\theta-(\lambda^2-1)\theta^2.
\]
Its maximum on \([0,1]\) is \(1\) when \(1<\lambda\le\sqrt2\), attained at \(\theta=1\). When \(\lambda\ge\sqrt2\), its maximum is attained at
\[
\theta_*=\frac{\lambda^2}{2(\lambda^2-1)}
\]
and equals
\[
\frac{\lambda^4}{4(\lambda^2-1)}.
\]
Therefore
\[
C_Z(R_\lambda^2)
\le
\begin{cases}
\lambda,&1<\lambda\le\sqrt2,\\[2mm]
2\sqrt{1-\lambda^{-2}},&\lambda\ge\sqrt2.
\end{cases}
\]

For \(1<\lambda\le\sqrt2\), take
\[
x=(1,1),\qquad y=(-1,1).
\]
Then \(N_\lambda(x)=N_\lambda(y)=\sqrt2\),
\[
N_\lambda(x+y)=2,\qquad
N_\lambda(x-y)=2\lambda,
\]
so the ratio equals \(\lambda\).

For \(\lambda\ge\sqrt2\), put
\[
s=\sqrt{\lambda^2-1},
\qquad
x=(1,s),\qquad
y=(-1,s).
\]
Both vectors lie on the circle--strip transition rays and have norm \(\lambda\). Moreover
\[
N_\lambda(x+y)=2s,\qquad
N_\lambda(x-y)=2\lambda,
\]
so the ratio is
\[
\frac{4\lambda s}{2\lambda^2}
=
2\sqrt{1-\lambda^{-2}}.
\]
This proves the value formula.

For completeness, consider equality. In the regime \(1<\lambda<\sqrt2\), the pure branches are bounded by \(1<C_Z\), so a maximizer must come from a mixed branch. Using \(\theta=1\), equality forces the relevant chord \(q\) to be horizontal, forces
\[
E(p)=E(q),
\]
and forces
\[
N_\lambda(x)=E(x),\qquad N_\lambda(y)=E(y).
\]
After the allowed symmetries one may write
\[
x=r\cos\alpha\,(\cos\alpha,\sin\alpha),\qquad
y=r\sin\alpha\,(-\sin\alpha,\cos\alpha).
\]
The two disk-activity conditions are exactly
\[
\lambda\cos\alpha\le1,\qquad
\lambda\sin\alpha\le1,
\]
which give
\[
\arccos(\lambda^{-1})\le\alpha\le\arcsin(\lambda^{-1}).
\]
Conversely every such pair gives one horizontal chord, one Euclidean chord of the same Euclidean length, and ratio \(\lambda\).

When \(\lambda>\sqrt2\), \(\theta_*\) is interior. Equality in
\[
N_\lambda(z)^2
\ge
\theta_*E(z)^2+(1-\theta_*)F(z)^2
\]
forces
\[
E(z)=F(z)
\]
for each of \(z=x,y\). Equality in the mixed-branch bound also forces \(p_1=0\) and \(q_2=0\). Hence, up to the allowed symmetries,
\[
x=(r,rs),\qquad y=(-r,rs),
\qquad s=\sqrt{\lambda^2-1}.
\]
The converse was already checked. At \(\lambda=\sqrt2\), the low-regime angle interval collapses to \(\alpha=\pi/4\), which is the same pair as the high-regime formula with \(s=1\).

## Verification
The upper bound treats all four possible branch products \(EE\), \(EF\), \(FE\), and \(FF\), so no facet case is omitted. The optimized quadratic minorant is exact at the high-parameter extremizers, while the Euclidean minorant is exact in the low-parameter regime.

A direct numerical stress test over several values of \(\lambda\) was used only to locate the candidate phase diagram before the symbolic proof. It is not used as evidence.

The two lower-bound families were substituted into the original definition exactly. Equality conditions were then traced backward through every inequality in the proof, yielding the stated complete maximizing sets.

## Relationship to prior work
Llorens-Fuster, Mazcuñán-Navarro, and Reich introduced the Zbăganu constant into a systematic study with the Ptolemy constant, proved general inequalities, and computed both constants for several concrete spaces. Their accessible publisher material identifies the Zbăganu definition, the fixed-point motivation, and the structure of their examples, but the complete article body was not available in the checked lawful route, so no whole-document noncoverage claim is made.

Banaś and Frączek introduced the plane
\[
N_\lambda(u,v)=\max\left\{\lambda|u|,\sqrt{u^2+v^2}\right\}
\]
as Example 4.1 in their 1993 deformation paper. The complete public PDF was inspected, including the page defining the norm and its moduli. That paper predates the Zbăganu constant and therefore does not contain the present invariant.

Later work computes the Ptolemy constant, von Neumann--Jordan constant, Banach--Mazur distance, and other geometric constants for this family or close generalizations. Those statements do not imply the present Zbăganu phase formula: the high branch
\[
2\sqrt{1-\lambda^{-2}}
\]
is neither the known von Neumann--Jordan branch nor the known first-regime Ptolemy value. Targeted searches for the Banaś--Frączek space together with Zbăganu terminology, \(R_\lambda^2\) aliases, and the candidate closed form located no equivalent statement.

## Limitations
The theorem is specific to the real two-dimensional Banaś--Frączek norm. It does not treat the generalized \(p\)-family
\[
\max\{\lambda|x_1|,\|x\|_p\}.
\]

The exact 1993 article is available in full but exposes only year-level bibliographic dating in the checked source. The row's exact first-public-date field therefore uses the earliest checked scientific source with a verified day-level public date, the 2010 Zbăganu article. The inaccessible body of that 2010 paper remains the principal originality residual: the accessible publisher material shows several concrete Zbăganu examples, but it does not expose every example statement.

## References
1. J. Banaś and K. Frączek, “Deformation of Banach spaces,” *Commentationes Mathematicae Universitatis Carolinae* 34 (1993), 47--53; MSC 46B20.
2. E. Llorens-Fuster, E. M. Mazcuñán-Navarro, and S. Reich, “The Ptolemy and Zbăganu constants of normed spaces,” *Nonlinear Analysis* 72 (2010), 3984--3993, DOI 10.1016/j.na.2010.01.030; published 2010-06-01; primary MSC 46B20.
3. Z. Zuo, “The Ptolemy constant of absolute normalized norms on \(\mathbb R^2\),” *Journal of Inequalities and Applications* 2012, Article 107, DOI 10.1186/1029-242X-2012-107.
