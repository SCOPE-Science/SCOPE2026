# The sharp spatial injectivity-radius variance of every flat Klein bottle

## Finding

Let \(K_{a,b}\) be the flat Klein bottle with Euclidean covering transformations \((x,y)\mapsto(x+a,-y)\) and \((x,y)\mapsto(x,y+b)\), with \(a,b>0\). This is the standard normal form for all complete flat Klein bottles. Let \(P\) be sampled by normalized Riemannian area, \(i(P)\) its pointwise geodesic injectivity radius, and \(s=a/b\). The scale-invariant spatial variance
\[
W(s)=\frac{\operatorname{Var}(i(P))}{\operatorname{area}(K_{a,b})}
\]
satisfies the sharp inequality
\[
0\le W(s)\le \frac{64Q^3}{27H^4},\qquad
Q=\sqrt3-\log(2+\sqrt3),\quad H=2\sqrt3-\log(2+\sqrt3).
\]
The upper equality holds at exactly one aspect ratio \(s_*=8Q/(3H^2)=0.240099811412893\ldots\); the sharp value is \(0.007976414224378\ldots\). The lower equality holds exactly for \(s\ge1\). The profile is an explicit cubic up to \(1/(2\sqrt3)\) and thereafter strictly decreases until \(s=1\).

## Proof

**Spatial law as a consequence of the known deck-displacement formula.** In these normal-form coordinates the fundamental rectangle is \([0,a)\times[0,b)\) and has area \(ab\). By the closest-translate formulas in Sabourau, Proposition 6.18, the shortest nontrivial orientation-preserving deck displacement is \(\min(2a,b)\); the shortest orientation-reversing displacement at \((x,y)\) is \(\sqrt{a^2+\operatorname{dist}(2y,b\mathbb Z)^2}\). The pointwise injectivity radius is half the lesser of the two, since the Euclidean cover has no conjugate points (see also Sabourau, Lemma 5.1). With \(y\) uniform modulo \(b\), \(2y/b\) modulo one is uniform. Folding about \(1/2\) gives \(D=\operatorname{dist}(2y,b\mathbb Z)/b\) uniform on \([0,1/2]\). Thus \(L_s=2i(P)/b\) has the law of \(\min(1,2s,\sqrt{s^2+D^2})\) and \(W(s)=\operatorname{Var}(L_s)/(4s)\).

For use in the calculation, let \(c=\min(1,2s)\), \(u=\min(c,\sqrt{s^2+1/4})\), and \(v=\min(1/2,\sqrt{c^2-s^2})\) for \(0<s<1\). The cumulative distribution is zero below \(s\), is \(2\sqrt{\ell^2-s^2}\) on \(s\le\ell<u\), and is one at and above \(u\); this follows by solving \(\sqrt{s^2+D^2}\le \ell\) below the cap. The density on \((s,u)\) is \(2\ell/\sqrt{\ell^2-s^2}\). An atom of mass \(1-2v\) occurs at \(u\) if this mass is positive. This gives mass \(1-2\sqrt3s\) for \(s<1/(2\sqrt3)\) and \(1-2\sqrt{1-s^2}\) for \(\sqrt3/2<s<1\), with no atom at either transition or between them. At \(s\ge1\) the law is the point mass at one. These pushforward formulas are supporting consequences, not an independent novelty claim.

**Exact early-regime variance.** Integration over \(D\le v\), adding the capped event of probability \(1-2v\), gives
\[
\begin{aligned}
\mathbb E L_s&=v\sqrt{s^2+v^2}+s^2\operatorname{arsinh}(v/s)+(1-2v)c,\\
\mathbb E L_s^2&=2s^2v+\tfrac23 v^3+(1-2v)c^2.
\end{aligned}
\]
For \(0<s\le s_0=1/(2\sqrt3)\), insert \(c=2s\), \(v=\sqrt3s\), and \(\operatorname{arsinh}(\sqrt3)=\log(2+\sqrt3)\). The moments become \(2s-Hs^2\) and \(4s^2-4\sqrt3s^3\). Subtracting the square of the first moment and dividing by \(4s\) gives
\[
W(s)=Qs^2-\frac{H^2}{4}s^3.
\]
Since \(0<\operatorname{arsinh}(\sqrt3)<\sqrt3\), \(Q>0\). The cubic increases up to its unique positive critical point \(s_*\) and decreases after it. To see that \(s_*<s_0\), put \(q=\log(2+\sqrt3)/\sqrt3\). Strict Jensen for the strictly convex function \(z\mapsto(1+z)^{-1/2}\) gives \(q=\int_0^1(1+3t^2)^{-1/2}\,dt>1/\sqrt2>2/3\). The inequality \(s_*<s_0\) is equivalent to \(3q^2+4q-4>0\), which follows. Substitution gives the claimed sharp value.

**Strict all-aspect comparison.** For \(s\ge s_0\), the \(2s\) cap is redundant: for \(s\le 1/2\) the square-root term is at most \(2s\) on the full support of \(D\), and for \(s\ge1/2\) the cap one is at most \(2s\). Hence for \(t>s\ge s_0\), couple both variables using the same \(D\); then
\[
L_t=g(L_s),\qquad g(x)=\min\bigl(1,\sqrt{x^2+t^2-s^2}\bigr).
\]
The identity holds also on the set where \(L_s=1\), since that set remains capped. On \([0,1]\), \(g\) has Lipschitz constant at most \((1+t^2-s^2)^{-1/2}<1\): the derivative of the square-root expression is increasing in \(x\) with that upper bound, and capping cannot increase it. Using an independent copy and the squared pairwise-difference formula for variance thus gives
\[
\operatorname{Var}(L_t)\le \frac{\operatorname{Var}(L_s)}{1+t^2-s^2}.
\]
For every \(s<1\), sufficiently small \(D>0\) lies in the uncapped region where \(L_s\) varies strictly with \(D\), so the variance is positive. The contraction and the increasing denominator \(4s\) imply strict decrease of \(W\) on \([s_0,1)\), whereas \(W=0\) on \([1,\infty)\). This makes the early cubic's maximum global and unique.

## Verification and scope

The included `check_injectivity.py` provides finite consistency tests (standard-library Python 3.10 or later) of the deck minimum, the first two moments, and the early-regime constants. The continuous proof above, not sampling, establishes global uniqueness and all boundary cases. The result concerns the spatial variance of the pointwise injectivity radius under area sampling on a fixed flat Klein bottle. It is not a theorem about conformal variance, nonuniform sampling, or curved metrics.

## Relationship to prior work

Sabourau's Proposition 6.18, whose stated target is the largest embedded disk, already supplies both position-dependent deck-displacement branches used above. Davis and Recio-Mitter develop related closest-translate and cut-locus methods. Eyll's systolic stability uses a variance of the conformal factor, not this spatial observable. The contribution here is the sharp area-normalized spatial variance inequality with its unique maximizing aspect ratio, particularly the strict comparison beyond the first cap transition. The checked comparisons do not establish absolute historical priority.

## References

1. S. Sabourau, *Systole, inradius and rigidity of cusped hyperbolic 3-manifolds*, arXiv:2606.06777, Lemma 5.1 and Proposition 6.18. https://arxiv.org/abs/2606.06777
2. D. M. Davis and D. Recio-Mitter, *The geodesic complexity of n-dimensional Klein bottles*, New York Journal of Mathematics **27** (2021), 296–318. https://arxiv.org/abs/1912.07411
3. J. Eyll, *Stability of Systolic Inequalities for the Möbius Strip and Klein Bottle*, Journal of Geometric Analysis (2025). https://doi.org/10.1007/s12220-025-02197-9
