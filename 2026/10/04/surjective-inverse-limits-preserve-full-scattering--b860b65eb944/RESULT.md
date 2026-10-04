# Surjective inverse limits preserve full-scattering
## Finding
Let \((X,T)=\varprojlim (X_r,T_r)\) be an inverse sequence of nonempty compact metric dynamical systems. Assume every bonding map is continuous and surjective, the bonding maps commute with the dynamics, and every stage \((X_r,T_r)\) is full-scattering. Then the inverse-limit system \((X,T)\) is full-scattering.

As a consequence, every countable Cartesian product of full-scattering compact metric dynamical systems is full-scattering. Indeed, Hui Xu proved in 2026 that every finite product of full-scattering systems is full-scattering; the countable product is the inverse limit of its finite coordinate products.

## Assumptions and scope
For a finite open cover \(\mathcal U\), write \(N(\mathcal U)\) for the least cardinality of a subcover. For an infinite set \(A=\{a_1<a_2<\cdots\}\subset\mathbb Z_+\), write
\[
c_A(\mathcal U,n)=N\!\left(\bigvee_{i=1}^n T^{-a_i}\mathcal U\right).
\]
A finite open cover is nontrivial when none of its members is dense. A compact metric dynamical system is full-scattering when \(c_A(\mathcal U,n)\to\infty\) for every infinite \(A\subset\mathbb Z_+\) and every nontrivial finite open cover \(\mathcal U\).

The inverse system is indexed by the positive integers. Each canonical projection \(\pi_r:X\to X_r\) is therefore surjective because the bonding maps are surjective and the spaces are nonempty compact metric spaces. The countable-product corollary assumes nonempty factors and coordinatewise dynamics.

## Proof
Fix an infinite \(A=\{a_1<a_2<\cdots\}\subset\mathbb Z_+\) and a nontrivial finite open cover \(\mathcal U=\{U_1,\ldots,U_m\}\) of \(X\). Empty members may be deleted. Since each \(U_j\) is non-dense, choose a nonempty open set
\[
O_j\subset X\setminus\overline{U_j}.
\]

For every \(j\), choose a point of \(O_j\). The inverse-limit topology has a basis of finite-coordinate cylinders, and a finite collection of coordinates can be pushed to one later stage. Hence there are a common stage \(r\) and nonempty open sets \(V_j\subset X_r\) such that
\[
\pi_r^{-1}(V_j)\subset O_j
\qquad (1\le j\le m).
\]
By regularity of the compact metric space \(X_r\), choose a closed set \(F_j\subset V_j\) with nonempty interior, and put \(W_j=X_r\setminus F_j\). Every \(W_j\) is open and non-dense.

The family \(\mathcal W=\{W_1,\ldots,W_m\}\) covers \(X_r\). Otherwise some \(y\in X_r\) would lie in every \(F_j\). Surjectivity of \(\pi_r\) gives \(x\in X\) with \(\pi_r(x)=y\). Then
\[
x\in\pi_r^{-1}(F_j)\subset\pi_r^{-1}(V_j)\subset O_j
\]
for every \(j\), so \(x\notin U_j\) for every \(j\), contradicting that \(\mathcal U\) covers \(X\). Thus \(\mathcal W\) is a nontrivial finite open cover of \(X_r\).

Moreover, \(U_j\cap\pi_r^{-1}(F_j)=\varnothing\), hence
\[
U_j\subset\pi_r^{-1}(W_j).
\]
Therefore \(\mathcal U\) refines \(\pi_r^{-1}\mathcal W\). Equivariance of \(\pi_r\) implies
\[
\bigvee_{i=1}^n T^{-a_i}\pi_r^{-1}\mathcal W
=
\pi_r^{-1}\!\left(\bigvee_{i=1}^n T_r^{-a_i}\mathcal W\right).
\]
For any finite cover \(\mathcal C\) of \(X_r\), surjectivity of \(\pi_r\) gives
\[
N(\pi_r^{-1}\mathcal C)=N(\mathcal C),
\]
because a subfamily covers \(X_r\) exactly when its pullback covers \(X\). Since refinement can only increase the least subcover cardinality,
\[
c_A(\mathcal U,n)
\ge
N\!\left(\bigvee_{i=1}^n T_r^{-a_i}\mathcal W\right).
\]
The right-hand side tends to infinity because \((X_r,T_r)\) is full-scattering. This proves that \((X,T)\) is full-scattering.

For the countable-product statement, let \((Y_j,S_j)\) be full-scattering systems. By Xu's finite-product theorem, each finite product
\[
P_r=\prod_{j=1}^r Y_j
\]
is full-scattering. The coordinate projections \(P_{r+1}\to P_r\) are continuous and surjective, and
\[
\prod_{j=1}^\infty Y_j
\cong
\varprojlim P_r.
\]
The inverse-limit theorem therefore applies.

## Verification
The proof uses only four points that can be checked directly from the definitions: a non-dense open-cover member has a nonempty open hole; every finite family of inverse-limit cylinder neighborhoods can be represented at one common stage; surjective pullback preserves the minimum subcover cardinality; and refinement reverses the desired inequality for minimum subcover size. The contradiction proving that \(\mathcal W\) covers the stage also uses surjectivity explicitly.

No finite experiment, numerical calculation, or unproved asymptotic step is used. The countable-product corollary additionally uses Xu's finite-product theorem.

## Relationship to prior work
Huang and Ye developed the open-cover complexity formulation of scattering notions. Hui Xu's 2026 preprint proves that every finite product of full-scattering systems is full-scattering. The present finding supplies a different permanence principle: full-scattering survives surjective inverse limits. It then upgrades Xu's finite-product theorem to countably infinite Cartesian products.

The inspected 2026 source states and proves finite-product closure. Searches for the same terminology together with “inverse limit,” “countable product,” and “infinite product” did not locate a statement implying the inverse-limit theorem or its countable-product corollary. This negative search evidence is not by itself a novelty proof; the main comparison is with the full statement and proof of the highly relevant 2026 source.

## Limitations
Surjectivity of the bonding maps is used twice: to make the canonical projections onto each stage surjective and to preserve minimum subcover cardinalities under pullback. The argument does not establish the theorem for arbitrary non-surjective inverse systems.

The result is qualitative: it proves divergence of open-cover complexity but gives no quantitative lower rate beyond that already available at a chosen finite stage. The literature comparison is strongest against the directly relevant 2026 full-text source; older full-scattering literature was checked at the statement and bibliographic level but was not exhaustively re-read.

## References
1. Hui Xu, “\(\Delta^*\)-Mixing and Products of Full-Scattering Systems,” arXiv:2609.27790v1, first public version 17 August 2026.
2. Wen Huang and Xiangdong Ye, “Topological complexity, return times and weak disjointness,” *Ergodic Theory and Dynamical Systems* 24 (2004), 825–846, DOI 10.1017/S0143385703000543.
