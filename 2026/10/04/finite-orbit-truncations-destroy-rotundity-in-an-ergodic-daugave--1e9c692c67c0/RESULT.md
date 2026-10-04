# Finite orbit truncations destroy rotundity in an ergodic Daugavet renorming
## Finding
Let \(\mathbb T=\mathbb R/\mathbb Z\) carry Lebesgue probability measure, fix an irrational \(\theta\), and write \(T_\theta(x)=x+\theta\pmod 1\). Let \((a_k)_{k\in\mathbb Z}\) be positive with
\[
\sum_{k\in\mathbb Z}a_k=1,
\qquad
\sum_{k\in\mathbb Z}\sqrt{a_k}<\infty.
\]
Define the full orbit norm on \(L_1(\mathbb T)\) by
\[
N(f)=\int_{\mathbb T}
\left(\sum_{k\in\mathbb Z}a_k|f(T_\theta^k x)|^2\right)^{1/2}dx.
\]
The Dantas--Kaasik--Perreau theorem applies because irrational rotation is invertible, measure preserving and ergodic: \(N\) is wMLUR and Gâteaux smooth, hence strictly convex, and the underlying atomless measure also gives the Daugavet property.

For every nonempty finite set \(F\subset\mathbb Z\), define the finite-window norm
\[
N_F(f)=\int_{\mathbb T}
\left(\sum_{k\in F}a_k|f(T_\theta^k x)|^2\right)^{1/2}dx.
\]
Then \((L_1(\mathbb T),N_F)\) contains an isometric copy of \(\ell_1^2\). Consequently \(N_F\) is not strictly convex, not Gâteaux smooth, and not wMLUR.

At the same time, if \(F_m\) is any increasing sequence of finite sets with \(\bigcup_mF_m=\mathbb Z\), then
\[
\sup_{\|f\|_1\le1}|N(f)-N_{F_m}(f)|
\le
\sum_{k\notin F_m}\sqrt{a_k}
\longrightarrow0.
\]
Thus no finite orbit horizon captures the rotundity or smoothness of this explicit ergodic renorming, even though finite horizons approximate the full norm uniformly on the \(L_1\)-unit ball.

## Assumptions and scope
The statement is for the explicit irrational-rotation model on \(\mathbb T\). All weights are strictly positive and satisfy the two summability conditions above. A finite truncation keeps the original weights on \(F\) and sets all other coordinates to zero. The claim concerns wMLUR, strict convexity, Gâteaux smoothness, the exact \(\ell_1^2\) obstruction, and uniform approximation to the full norm. It does not assert whether the truncated norms themselves have the Daugavet property, and it does not claim the same finite-window obstruction for every ergodic transformation.

For any \(k_0\in F\), measure preservation gives
\[
N_F(f)\ge\sqrt{a_{k_0}}\,\|f\|_1,
\]
while the triangle inequality in the finite Euclidean coordinate space gives
\[
N_F(f)\le\left(\sum_{k\in F}\sqrt{a_k}\right)\|f\|_1.
\]
Hence each \(N_F\) is an equivalent Banach norm on \(L_1(\mathbb T)\).

## Proof
Fix a nonempty finite \(F\subset\mathbb Z\). Choose an integer \(q\notin F-F\). The two finite integer sets
\[
-F
\quad\text{and}\quad
q-F
\]
are disjoint. Because \(\theta\) is irrational, the circle points \(s\theta\pmod1\), with \(s\in(-F)\cup(q-F)\), are pairwise distinct. Their minimum circular separation is therefore positive. Choose a nonempty interval \(I\subset\mathbb T\) short enough that the translates
\[
T_\theta^s I,
\qquad s\in(-F)\cup(q-F),
\]
are pairwise disjoint.

Set
\[
f=\chi_I,
\qquad
g=\chi_{T_\theta^q I}.
\]
For \(k\in F\), the function \(f(T_\theta^k x)\) can be nonzero only when \(x\in T_\theta^{-k}I\). Similarly, \(g(T_\theta^k x)\) can be nonzero only when \(x\in T_\theta^{q-k}I\). By construction the two unions
\[
\bigcup_{k\in F}T_\theta^{-k}I
\quad\text{and}\quad
\bigcup_{k\in F}T_\theta^{q-k}I
\]
are disjoint. Hence, at every point outside a null set, at least one of the two finite vectors
\[
(\sqrt{a_k}f(T_\theta^k x))_{k\in F},
\qquad
(\sqrt{a_k}g(T_\theta^k x))_{k\in F}
\]
is zero. Therefore, for all scalars \(\alpha,\beta\),
\[
N_F(\alpha f+\beta g)
=
|\alpha|N_F(f)+|\beta|N_F(g).
\]
After normalizing \(u=f/N_F(f)\) and \(v=g/N_F(g)\), one obtains
\[
N_F(\alpha u+\beta v)=|\alpha|+|\beta|.
\]
Thus \(\operatorname{span}\{u,v\}\) is linearly isometric to \(\ell_1^2\). In particular,
\[
N_F\left(\frac{u+v}2\right)=1,
\]
so \(N_F\) is not strictly convex. Also
\[
N_F(u+t v)=1+|t|,
\]
so the directional derivative at \(t=0\) does not exist and \(N_F\) is not Gâteaux smooth. Since wMLUR implies strict convexity, \(N_F\) is not wMLUR either.

It remains to prove uniform approximation. For any finite \(F\) and any \(f\in L_1(\mathbb T)\), the elementary inequality \(\sqrt{A+B}-\sqrt A\le\sqrt B\) for \(A,B\ge0\) yields
\[
0\le N(f)-N_F(f)
\le
\int_{\mathbb T}
\left(\sum_{k\notin F}a_k|f(T_\theta^k x)|^2\right)^{1/2}dx.
\]
Using \(\|(c_k)\|_2\le\|(c_k)\|_1\), Tonelli's theorem and measure preservation,
\[
N(f)-N_F(f)
\le
\sum_{k\notin F}\sqrt{a_k}
\int_{\mathbb T}|f(T_\theta^k x)|dx
=
\left(\sum_{k\notin F}\sqrt{a_k}\right)\|f\|_1.
\]
Because \(\sum_k\sqrt{a_k}<\infty\), the tail tends to zero along every finite exhaustion of \(\mathbb Z\), proving the uniform bound.

## Verification
The proof is analytic and uses no finite computation or extrapolation. The only external mathematical inputs are the published properties of the full infinite-coordinate norm and the standard ergodicity of irrational rotations. The finite-window obstruction itself is proved directly by a disjoint-translate construction, and the approximation rate follows from a pointwise square-root inequality plus absolute summability of \(\sqrt{a_k}\).

The boundary cases used in the proof were checked explicitly: \(F\) must be nonempty so that \(N_F\) is a norm; \(q\notin F-F\) is always available because \(F-F\) is finite; irrationality is exactly what makes the finitely many required circle translates distinct; and no limiting argument is used to infer the exact \(\ell_1^2\) identity.

## Relationship to prior work
Dantas, Kaasik and Perreau introduce the infinite-coordinate orbit norm above and prove that ergodicity is equivalent to strict convexity, Gâteaux smoothness, and absence of an isometric copy of \(\ell_1^2\) when every orbit coordinate carries a positive weight. They also prove wMLUR under ergodicity and the Daugavet property for atomless measure spaces. Their construction and proof use the full bi-infinite orbit and do not state a finite-support or finite-window truncation theorem.

Doucha studies invariant strictly convex renormings under group actions, including actions on \(L_1[0,1]\), but does not analyze these weighted Euclidean orbit norms, their finite-window truncations, or the exact \(\ell_1^2\) obstruction above. The present statement therefore isolates a different issue: approximation of a specific recent orbit norm by finite coordinate windows and the failure of rotundity at every finite stage.

## Limitations
The theorem is deliberately confined to irrational rotations, where the required finite family of orbit translates can be separated by elementary geometry. A broader result for general aperiodic or ergodic transformations would require a separate measurable-dynamics argument and is not claimed here. No statement is made about the Daugavet property of \(N_F\), nor about quantitative moduli of convexity or smoothness beyond the exact \(\ell_1^2\) obstruction.

The literature comparison cannot exclude an uncatalogued observation phrased in different terminology, especially because the focal preprint is recent. The checked focal version does not contain a truncation or finite-support statement, and the broader invariant-renorming paper does not imply this finite-window claim.

## References
1. Sheldon Dantas, Jaan Kristjan Kaasik, Yoël Perreau, *A strictly convex and smooth Banach space with the Daugavet property*, arXiv:2609.12562v1, 2026. See Sections 3.1--3.2 and Theorem 3.4.
2. Michal Doucha, *Invariant strictly convex renormings*, arXiv:2508.16182v1, 2025.
