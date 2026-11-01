# Sharp global hyperplane-shadow stability for the five-dimensional cross-polytope

## Finding
Let \(C_5=\operatorname{conv}\{\pm e_1,\ldots,\pm e_5\}\subset\mathbb R^5\), let \(u\in\mathbb S^4\), and denote the four-dimensional Euclidean volume of its orthogonal hyperplane shadow by
\[
B(u)=\operatorname{vol}_4\bigl(\operatorname{proj}_{u^\perp}C_5\bigr).
\]
Set \(\mathcal A=\{\pm e_1,\ldots,\pm e_5\}\). Then the sharp global stability inequality is
\[
\boxed{\frac23-B(u)\ge\frac{25-7\sqrt5}{96}\,\operatorname{dist}(u,\mathcal A)^2.}
\]
The coefficient cannot be increased. Equality occurs precisely when \(u\in\mathcal A\) or \(u\) is one of the 32 signed body diagonals \((\pm1,\ldots,\pm1)/\sqrt5\). The diagonal equality configurations, not directions infinitesimally close to \(\mathcal A\), determine the best coefficient.

## Assumptions and scope
All distances are ambient Euclidean chord distances between unit normal vectors, not angles or distances between unoriented Grassmannian subspaces. The convex body is the fixed unit-coordinate cross-polytope in dimension five. The projection volume is taken with the induced Euclidean four-measure. The theorem makes no assertion about other dimensions, arbitrary cross-polytopes, or general codimensions.

For independent symmetric signs \(\varepsilon_i\in\{-1,1\}\), let
\[
N(u)=\mathbb E\left|\sum_{i=1}^5\varepsilon_i u_i\right|,
\qquad a(u)=\max_i|u_i|.
\]
The theorem is equivalent to the sharp endpoint Rademacher inequality
\[
1-N(u)\ge c\,[1-a(u)],\qquad c=\frac{25-7\sqrt5}{32},
\]
because \(B(u)=\frac23N(u)\) and \(\operatorname{dist}(u,\mathcal A)^2=2[1-a(u)]\).

## Proof
**Projection normalization.** Every facet of \(C_5\) is a four-simplex \(\operatorname{conv}\{s_1e_1,\ldots,s_5e_5\}\), indexed by \(s\in\{-1,1\}^5\), with four-volume \(\sqrt5/24\) and outward unit normal \(s/\sqrt5\). The Cauchy projection formula therefore gives
\[
B(u)=\frac12\sum_{s\in\{-1,1\}^5}\frac{\sqrt5}{24}
\left|\left\langle\frac{s}{\sqrt5},u\right\rangle\right|
=\frac1{48}\sum_s|s\cdot u|=\frac23N(u).
\]
Signed coordinate permutations leave \(N\), \(a\), and \(B\) unchanged. We may consequently take \(u\) in the closed cone
\[
\mathcal C=\{u\in\mathbb R^5:u_1\ge u_2\ge\cdots\ge u_5\ge0\},\qquad\|u\|_2=1.
\]
Here \(a(u)=u_1\). The target is \(N(u)-cu_1\le1-c\).

**Finite support-function reduction.** Let \(\mathcal S=\{(1,s_2,s_3,s_4,s_5):s_i\in\{-1,1\}\}\), a set of 16 signs. For each assignment \(\tau:\mathcal S\to\{-1,1\}\), put
\[
v_\tau=\frac1{16}\sum_{s\in\mathcal S}\tau(s)s.
\]
The identity \(|z|=\max\{z,-z\}\) implies
\[
N(u)=\max_{\tau\in\{-1,1\}^{\mathcal S}}v_\tau\cdot u.
\]
Thus it suffices to bound \((v_\tau-ce_1)\cdot u\) for precisely \(2^{16}=65536\) assignments. Let \(\Pi_{\mathcal C}\) be the Euclidean projection onto \(\mathcal C\). The usual orthogonal projection inequality for closed convex cones (Moreau decomposition followed by Cauchy–Schwarz) gives, for every unit \(u\in\mathcal C\),
\[
(v_\tau-ce_1)\cdot u\le\|\Pi_{\mathcal C}(v_\tau-ce_1)\|_2.
\]

**Exact finite certificate.** Let \(D=10^{10}\), \(Q=2921101299\), and \(c_0=Q/D\). Squaring positive rational expressions verifies
\[
c_0<\frac{25-7\sqrt5}{32}<c_0+\frac1D.
\]
For every assignment \(\tau\) except the two assignments indexed by integer masks 65535 and 65256 in lexicographic sign order, the accompanying exact-integer program `proof_certificate.py` proves
\[
\left\|\Pi_{\mathcal C}(v_\tau-c_0e_1)\right\|_2\le\frac7{10}.
\]
The program visits all 65536 masks, not a sample. It uses integer pool-adjacent-violators blocks to compute the Euclidean isotonic projection exactly. To avoid denominators it multiplies \(v_\tau-c_0e_1\) by \(D\), multiplies the squared projection norm by 60 (divisible by all possible block lengths 1 through 5), and checks an integer inequality. For a block of length \(k\) with integer sum \(s\), its contribution is \((60/k)s^2\) when \(s>0\), and zero otherwise. Nonexpansiveness of metric projection yields
\[
\|\Pi_{\mathcal C}(v_\tau-ce_1)\|_2\le\frac7{10}+\frac1D<1-c
\]
for every nonexceptional assignment. Both strict inequalities are elementary exact comparisons using the displayed bound on \(c\).

The two exceptional assignments have exact vectors \(v_\tau=e_1\) and \(v_\tau=(3/8,3/8,3/8,3/8,3/8)\), respectively. For \(e_1\) the projected norm is \(1-c\), with equality only at \(u=e_1\). In the other case, pooling all five coordinates yields
\[
\Pi_{\mathcal C}(v_\tau-ce_1)=\left(\frac38-\frac c5\right)(1,1,1,1,1),
\qquad\sqrt5\left(\frac38-\frac c5\right)=1-c.
\]
Equality in the Cauchy–Schwarz bound forces \(u=(1,1,1,1,1)/\sqrt5\). Therefore \(N(u)\le1-c(1-u_1)\) for every unit \(u\in\mathcal C\), with precisely these two equality representatives.

**Sharpness.** The coordinate-axis representative has \(N(e_1)=1\). At the diagonal \(u_\Delta=(1,1,1,1,1)/\sqrt5\), elementary sign counting gives \(N(u_\Delta)=3\sqrt5/8\). Hence
\[
\frac{1-N(u_\Delta)}{1-1/\sqrt5}
=\frac{25-7\sqrt5}{32}=c.
\]
The two representatives and signed coordinate permutations give the claimed equality cases and optimal coefficient after reverting to \(B\).

## Verification
Run `python3 proof_certificate.py` with a standard Python 3 interpreter. The program makes no network calls and requires no third-party packages. It verifies every signed gradient, the exceptional-gradient vectors, the rational enclosure for \(c\), and the strict integer norm bounds. Its maximum nonexceptional integer value is 2917995876580389748020, corresponding to mask 65520, strictly below the certified cutoff \(60(7D/10)^2=2940000000000000000000\). The symbolic two exceptional calculations and the geometric Cauchy normalization are established above; the finite checker is a transparent exhaustive lemma rather than a numerical or randomized experiment.

## Relationship to prior work
Ivanov's 2018/2020 study of cross-polytope projections, the earlier hyperplane case of the projection conjecture, and his July 2026 all-codimension maximal-projection theorem give the sharp value \(2/3\) and coordinate-axis equality in this hyperplane setting. This theorem does not claim that bound as new. Jakimiuk's August 2026 stability theorem directly establishes an upper Rademacher comparison of the same form \(N(u)\le1-c(1-u_1)\) for an unspecified universal positive coefficient, with no optimized five-dimensional value or the diagonal equality class. The present result supplies that exact sharp coefficient and complete equality classification in dimension five. Xie's October 2026 Szarek stability theorem controls the *opposite*, lower Khintchine endpoint near two-sparse minimizers. The 2015 FKN-extension theorem gives a dimension-free but nonsharp qualitative rigidity bound; it does not state this exact optimum.

## Limitations
The equality classification and constant are proved only for the fixed five-dimensional hyperplane problem. The projective stability for arbitrary codimension or general dimension is not settled here. The exact integer certificate proves one finite-dimensional inequality and does not by itself imply a universal-dimensional formula. Although accessible close primary texts and relevant mathematical records were compared, unindexed or unpublished historical refinements may exist; independence and external validation have not been performed.

## References
- G. Ivanov, *The maximal volume of projections of the cross-polytope*, arXiv:2607.12072 (first public 2026-07-13), https://arxiv.org/abs/2607.12072.
- J. Jakimiuk, *Stability of extremal hyperplane projections of balls in \(\ell_p^n(\mathbb R)\)*, arXiv:2608.21787 (2026-08-22), https://arxiv.org/abs/2608.21787.
- G. Ivanov, *On the volume of projections of the cross-polytope*, arXiv:1808.09165 (first public 2018-08-28), https://arxiv.org/html/1808.09165v3.
- X. Xie, *Stability of Szarek's inequality with best constant*, arXiv:2610.07526 (2026-10-05), https://arxiv.org/abs/2610.07526.
- J. Jendrej, K. Oleszkiewicz and J. O. Wojtaszczyk, *On some extensions of the FKN theorem*, Theory of Computing **11** (2015), 445–469, DOI:10.4086/toc.2015.v011a018.
