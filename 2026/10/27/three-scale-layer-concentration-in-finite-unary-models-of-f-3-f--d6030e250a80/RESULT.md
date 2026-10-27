# Three-scale layer concentration in finite unary models of \(f^3=f^2\)

## Finding
For an integer \(n\ge1\), choose uniformly one total unary operation \(f:[n]\to[n]\) satisfying \(f(f(f(x)))=f(f(x))\) for all \(x\in[n]\). Define \(R\) as the number of fixed points, \(S\) as the number of nonfixed points whose images are fixed, and \(T=n-R-S\). Each element has forward distance zero, one, or two to a fixed point. If \(r\ge1\), \(s\ge1\), \(t\ge0\), and \(r+s+t=n\), the exact number of models of this profile is
\[
N_n(r,s,t)=\frac{n!}{r!s!t!}r^s s^t.
\]
The exceptional profile \((n,0,0)\) has one model; profiles with \(s=0<t\) are impossible. The full trivariate exponential generating function is
\[
\sum_{n\ge0}\frac{z^n}{n!}\sum_f u^{R(f)}v^{S(f)}w^{T(f)}
=\exp\bigl(uz\exp(vz\exp(wz))\bigr).
\]
Let \(a=a_n>0\) solve uniquely
\[
n=a\exp(a\exp a)\,[1+a\exp a(1+a)],
\]
and put \(b=a\exp a\), \(r_*=a\exp b\), \(s_*=br_*\), \(t_*=as_*\). Then for every fixed \(0<\varepsilon<1/4\) some \(c_\varepsilon>0\) satisfies, for all sufficiently large \(n\),
\[
\Pr\bigl(|R-r_*|>\varepsilon r_*\ \text{or}\ |S-s_*|>\varepsilon s_*\bigr)
\le \exp\bigl(-c_\varepsilon n/W(\log n)\bigr).
\]
Consequently, in probability,
\[
R\sim\frac{n}{\log n\,W(\log n)},\qquad
S\sim\frac{n}{W(\log n)},\qquad \frac{T}{n}\longrightarrow1.
\]
Here \(W(x)\) is the positive solution to \(W(x)\exp(W(x))=x\).

## Assumptions and scope
Models are labelled, nonempty, finite, and have exactly one total unary function, without additional predicates or weights. The measure is uniform over the models satisfying the displayed universal identity. This is a theorem about their **joint depth statistics**, not about all finite unary functions, a random recursive-tree model, or conditional distribution given a different axiom.

## Proof
**Exact enumeration.** The identity implies \(f^2(x)\) is fixed, so the functional digraph is a disjoint union of inward-pointing rooted trees of height at most two. Choose disjoint depth-zero, depth-one, and depth-two vertex subsets of sizes \(r,s,t\); send each depth-one vertex to any of the \(r\) roots and each depth-two vertex to any of the \(s\) depth-one vertices. These assignments are bijective with models of the specified profile. A root with its set of depth-one children, each with its set of depth-two children, is counted by \(uz\exp(vz\exp(wz))\). A finite unordered set of these components gives the displayed generating function.

**Strict concavity.** For continuous \(r,s,t=n-r-s>0\), define the factorial-free log-weight
\[
F(r,s)=-r\log r-s\log s-t\log t+s\log r+t\log s.
\]
Set \(a=t/s\), \(b=s/r\). The stationary equations are
\[
F_r=\log(t/(rs))+s/r=0,\qquad
F_s=\log(rt/s^2)+t/s=0.
\]
They are equivalent to \(b=a\exp a\), \(r=a\exp b\), and \(n=r[1+b(1+a)]\). The final right-hand side increases strictly from zero to infinity with \(a>0\); hence a unique interior critical point exists and equals \((r_*,s_*)\). The negative Hessian is
\[
H=\begin{pmatrix}
1/r+1/t+s/r^2 & -1/r+1/t+1/s\\
-1/r+1/t+1/s & 1/t+3/s+t/s^2
\end{pmatrix}.
\]
Its diagonal entries are positive. Direct expansion yields
\[
\det(H)\,r^2s^2t=r^2s+rt^2+5rst+3rs^2+st^2+2s^2t+s^3>0.
\]
Thus \(F\) is strictly concave, with its unique global maximum at the critical point. On the boundary with \(t=0\) use the continuous extension \(t\log t=0\); the exceptional identity map is treated separately.

**Three scales.** The saddle identities give \(n=a\exp b[1+b(1+a)]\) and \(b=a\exp a\). Taking logarithms shows \(b\sim\log n\). Thus \(a=W(b)\sim W(\log n)\). Moreover \(r_*=n/[1+b(1+a)]\), \(s_*=br_*\), and \(t_*=as_*\), yielding the three stated scales. In particular \(t_*/n\to1\), while \(r_*,s_*\to\infty\).

**Quantitative concentration.** Fix \(0<\varepsilon<1/4\). In the rectangle \(|r-r_*|\le\varepsilon r_*\), \(|s-s_*|\le\varepsilon s_*\), the third coordinate satisfies \(t=n-r-s\sim n\) uniformly as \(n\to\infty\). Multiplying the negative Hessian on both sides by \(\operatorname{diag}(r_*,s_*)\), its entries are respectively of orders \(s_*\), \(s_*\), and \(t_*\), with the first diagonal bounded below by a positive multiple of \(s_*\) and the final diagonal asymptotically larger, since \(t_*/s_*=a\to\infty\). The matrix is therefore bounded below by \(c s_* I\) for a constant \(c>0\) depending on \(\varepsilon\). Integrating twice along segments from the maximum proves a gap of at least \(c'\varepsilon^2s_*\) in \(F\) on the rectangle's boundary. Global concavity preserves this lower gap beyond the rectangle by restriction to rays from the maximum.

Uniform elementary Stirling estimates give
\[
\log N_n(r,s,t)=\log(n!)+n+F(r,s)+O(\log n)
\]
throughout the feasible integer profiles with \(r,s,t\ge1\), also when \(t=0\) by interpreting \(0\log0=0\). Taking the nearest feasible integer profile to the saddle incurs only \(O(\log n)\) in this logarithm. There are fewer than \(n^2\) profiles; comparing their total mass outside the rectangle with this one interior profile yields \(\exp[-c''\varepsilon^2s_*+O(\log n)]\). The exceptional identity profile has weight one and is exponentially negligible by the same comparison. Since \(s_*\sim n/W(\log n)\) and \(s_*/\log n\to\infty\), the stated tail follows.

## Verification
The attached standalone `checker.py` exhaustively enumerates all \(n^n\) unary functions for \(1\le n\le6\), tests the identity and computes each profile; it exactly matches the formula in every case. The totals for those six sizes are \(1,3,16,101,756,6607\). Independent symbolic expansion verifies the displayed positive Hessian determinant. These finite checks corroborate, but do not replace, the global concavity and concentration proof.

## Relationship to prior work
Koponen (2026) investigates finite-model approximations of \(\omega\)-categorical theories and gives bounded-height DAGs as closure-controlled examples (Example 2.2), without counting uniform labelled depth strata. Koponen and Tousinejad (2024/2025) establish logical convergence results for random expansions **of prescribed bounded-height base trees**, rather than the uniform distribution over the bases themselves. Skau and Kristensen (2019) study higher-order Bell-number generating functions and an asymptotic in the *iteration order* with fixed size, not this fixed-depth joint-size concentration regime. The exponential construction resembles nested combinatorial assemblies, but its exact depth profile, unique saddle and joint concentration are not stated in the inspected texts.

## Limitations
No independence or outside audit is asserted. The proof concerns a single two-step stabilization identity, not arbitrary unary function theories or any fixed-height extension. The rate gives fixed-relative-error concentration, not a central limit or local limit theorem. Earlier general weighted-forest saddlepoint literature may contain an equivalent joint-depth statement; the originality assessment is limited to the specified searches and inspected primary sources.

## References
1. Vera Koponen, *A characterization of the finite model property for \(\omega\)-categorical theories*, arXiv:2610.16163v1, first posted 2026-10-12, https://arxiv.org/abs/2610.16163, especially Example 2.2 and Sections 2--3.
2. Vera Koponen and Yasmin Tousinejad, *Random expansions of trees with bounded height*, arXiv:2410.11775, first posted 2024-10-15, https://arxiv.org/abs/2410.11775, abstract, introduction, and assumptions on prescribed trees.
3. Ivar Henning Skau and Kai Forsberg Kristensen, *An asymptotic Formula for the iterated exponential Bell Numbers*, arXiv:1903.07979, 2019, https://arxiv.org/abs/1903.07979, Sections 1 and 3.
