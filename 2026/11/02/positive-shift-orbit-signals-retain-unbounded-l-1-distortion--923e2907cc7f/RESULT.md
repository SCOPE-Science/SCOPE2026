# Positive shift-orbit signals retain unbounded \(L_1\) distortion

## Finding
Let \(H=\ell_2(\mathbb Z;\mathbb R)\), let \(S^k x(j)=x(j-k)\), and put
\[
\mathcal P=\{x\in H:\|x\|_2=1,\ x(j)\ge0\text{ for every }j\in\mathbb Z\}.
\]
Equip the quotient with \(d([x],[y])=\inf_{k\in\mathbb Z}\|x-S^k y\|_2\). Then \(\mathcal P/\mathbb Z\) has **infinite bilipschitz distortion into real \(L_1\)**. In fact, for every integer \(n\ge1\), every invertible real matrix \(A\in GL_n(\mathbb R)\), every finite set \(E\subset\mathbb R^n/\mathbb Z^n\) with metric
\[
\rho_A(x,y)=\min_{u\in\mathbb Z^n}\|A(x-y-u)\|_2,
\]
and every \(\varepsilon>0\), the set \(E\), after uniform rescaling, embeds into \(\mathcal P/\mathbb Z\) with bilipschitz distortion at most \(1+\varepsilon\).

## Assumptions and scope
All Hilbert spaces and signals are **real**. The coordinatewise positivity assumption is literal and includes zero coordinates; signals are unit vectors. The target class is an arbitrary real \(L_1\) space, not just finite-dimensional \(\ell_1\). The group acts by integer translation. No theorem about strictly positive sequences, finite-support-only signals as a whole, or \(L_p\) targets with \(p>1\) is claimed. Constants in the finite-witness lower bound are absolute but not optimized.

## Proof
**1. A nonnegative bandlimited torus model.** Fix \(n\) and \(A\in GL_n(\mathbb R)\). Write \(C=(-\tfrac12,\tfrac12)^n\) in frequency space and choose \(t>0\) small enough that \(4Q_t\subset C\), where \(Q_t=t A^T[-1,1]^n\). With Fourier convention \(\widehat f(\xi)=\int f(s)e^{-2\pi i\langle s,\xi\rangle}ds\), let
\[
h_t(\xi)=\mathbf1_{Q_t}(\xi),\quad f_t=\mathcal F^{-1}h_t,\quad g_t=f_t^2.
\]
The symmetry of \(Q_t\) makes \(f_t\) real, hence \(g_t\ge0\). The function \(g_t\) is continuous, nonzero, and belongs to \(L_1\cap L_2(\mathbb R^n)\): indeed \(f_t\in L_2\cap L_\infty\), so \(f_t^2\in L_1\cap L_2\). Its Fourier transform \(\widehat g_t=h_t*h_t\) is supported in \(2Q_t\). For all \(x,y\in\mathbb R^n\), the Fourier transform of \(g_t(\cdot-x)g_t(\cdot-y)\) is supported in \(4Q_t\subset C\). The zero-alias Poisson identity therefore gives
\[
\sum_{v\in\mathbb Z^n}g_t(v-x)g_t(v-y)
=\int_{\mathbb R^n}g_t(s-x)g_t(s-y)ds.
\]
This is justified, for example, by applying Fourier-series Parseval to the bandlimited functions, or by approximating the compactly supported Fourier transforms; all displayed series converge absolutely by Cauchy–Schwarz and the sampling identity. In particular
\[
M_t:=\sum_{v\in\mathbb Z^n}g_t(v-x)^2=\int g_t(s)^2ds>0
\]
is independent of \(x\). Define \(F_t(x)(v)=M_t^{-1/2}g_t(v-x)\). Thus \(F_t(x)\) is a **coordinatewise nonnegative unit vector**, and \(F_t(x+u)=\tau_uF_t(x)\) for \(u\in\mathbb Z^n\).

**2. Its distance kernel is isotropic after applying \(A\).** Fourier Plancherel gives
\[
\|F_t(x)-F_t(y)\|_2^2=2\bigl(1-\Phi(tA(x-y))\bigr),
\]
where \(\Phi(z)=\int_{[-2,2]^n}\cos(2\pi\langle z,\eta\rangle)\,d\nu(\eta)\), and \(\nu\) is the product probability measure with one-dimensional density proportional to \((2-|\eta|)^2\). Indeed \(\widehat g_t\) is the convolution of two parallelepiped indicators, so its squared modulus, after changing variables \(\xi=tA^T\eta\), is exactly this product density. Its mean is zero and its covariance is \(\frac25 I\), by the elementary integral
\[
\frac{\int_{-2}^{2}\eta^2(2-|\eta|)^2d\eta}{\int_{-2}^{2}(2-|\eta|)^2d\eta}=\frac25.
\]
Therefore, with \(\kappa=2\pi\sqrt{2/5}\),
\[
2(1-\Phi(z))\le\kappa^2\|z\|_2^2,
\qquad
2(1-\Phi(z))=\kappa^2\|z\|_2^2+o(\|z\|_2^2)
\]
as \(z\to0\). Since \(\nu\) has a nonempty open support, \(\Phi(z)<1\) for every \(z\ne0\). By the Riemann–Lebesgue lemma \(\Phi(z)\to0\) as \(\|z\|\to\infty\). Consequently, for each \(\varepsilon>0\) there exists \(c>0\) such that
\[
2(1-\Phi(z))\ge\min\{\kappa^2\|z\|_2^2/(1+\varepsilon)^2,c\}
\quad\text{for all }z\in\mathbb R^n.
\]
Here the local part uses the Taylor expansion uniformly in direction; the lower bound outside a small ball follows from continuity, strict inequality, and decay.

**3. Nearly isometric embedding of every flat torus.** Let \(R_A\) be the diameter of \((\mathbb R^n/\mathbb Z^n,\rho_A)\). Shrink \(t\) further so that \(\kappa^2 t^2R_A^2/(1+\varepsilon)^2\le c\). The induced quotient map \(x\mapsto[F_t(x)]\) then satisfies for all \(x,y\)
\[
\frac{\kappa t}{1+\varepsilon}\rho_A(x,y)
\le d_n([F_t(x)],[F_t(y)])\le\kappa t\rho_A(x,y).
\]
The upper bound uses a lattice translate realizing \(\rho_A\); the lower bound applies the capped quadratic estimate to *every* lattice translate. Thus any flat torus embeds, after rescaling, with arbitrarily small distortion into the quotient of the **nonnegative** unit sphere of \(\ell_2(\mathbb Z^n)\).

**4. Positive finite coding from \(\mathbb Z^n\) to \(\mathbb Z\).** Approximate finitely many nonnegative unit representatives by truncated, renormalized nonnegative finite-support representatives. Quotient distances vary by at most the sum of the individual \(\ell_2\) errors. For finite common support \(K\subset\mathbb Z^n\), choose an integer \(s\) larger than twice the coordinate differences of \(K\), and encode
\[
\varphi(v)=\sum_{j=1}^{n}s^{j-1}v_j\in\mathbb Z.
\]
The map \(\varphi\) is injective on \(K-K\), so transporting coordinates \(v\mapsto\varphi(v)\) preserves every relevant translate correlation and hence the quotient distances exactly (off this finite difference set, all correlations vanish). It clearly preserves nonnegativity and unit norm. Taking truncations sufficiently fine yields arbitrarily small additional distortion for any prescribed finite set.

**5. \(L_1\) obstruction.** Khot–Naor proved the existence, for arbitrarily large \(n\), of flat \(n\)-tori with \(L_1\) distortion at least \(c\sqrt n\) for some universal \(c>0\). If \(\mathcal P/\mathbb Z\) embedded into a real \(L_1\) space with finite distortion \(D\), Step 4 would yield, with arbitrarily small excess, \(D\)-bounded embeddings of every finite subset of every such torus. Finite determination of \(L_1\)-distortion (obtainable via an \(L_1\) ultraproduct) would imply all these flat tori embed in \(L_1\) with distortion \(\le D\), contradicting Khot–Naor. This also gives finite witness sets whose required \(L_1\) distortion grows like \(\sqrt n\) along an unbounded sequence of \(n\). \(\square\)

## Verification
The nonnegative sampling normalization can be independently checked with the one-dimensional choice \(Q_t=[-1/16,1/16]\): \(f_t(s)=\sin(2\pi s/16)/(\pi s)\), \(g_t=f_t^2\), and the lattice sum \(\sum_vg_t(v-x)^2\) is constant in \(x\); numerical evaluations at shifts \(0,0.15,0.41,0.97\), truncated to \(-10000\le v\le10000\), all gave \(0.00130208333333\) to displayed precision. Exact normalization, full inequalities, and infinite distortion are proved analytically above; finite sampling is only a supplementary check. The raw computation involved \(20,001\) coordinates at each of four shifts. The covariance ratio \(2/5\) was also verified symbolically.

## Relationship to prior work
Das and Rosendal (2026, arXiv:2610.31468v1, Theorem 3.2) constructed near-isometric flat-torus embeddings into the *unrestricted real sphere* shift quotient. Their Fourier indicator construction takes signed values; it does not establish that the embedded signals are nonnegative. Their finite coding result (Proposition 4.1) preserves signs, so it can be reused once a nonnegative high-rank model is built. The new step here is a **positive Fourier-square, no-alias sampling model** that satisfies both unit normalization and the exact shift action. Khot and Naor (2005/2006) already provide strong \(L_1\)-distortion lower bounds for flat tori; those lower bounds are used, not newly proved. The resulting positive-signal quotient obstruction is distinct from the known unrestricted-sphere obstruction.

## Limitations
Only the nonnegative real unit-sphere quotient and arbitrary real \(L_1\) targets are covered. No sharp distortion for a fixed finite witness, no upper bound in other target classes, and no claim of strictly positive coordinatewise signals is established. Complete publication-priority verification remains subject to older metric-invariant and positive signal-orbit literature; independent mathematical audit has not been performed.

## References
1. A. Das and C. Rosendal, *A sphere obstruction for the Hilbert shift quotient*, arXiv:2610.31468v1 (first public 2026-10-22), Sections 2–4. https://arxiv.org/html/2610.31468v1
2. S. Khot and A. Naor, *Nonembeddability theorems via Fourier analysis*, Mathematical Annalen 334 (2006), 821–852, Section 5; public earlier preprint arXiv:math/0510547. https://cs.nyu.edu/~khot/papers/nonembed-final-new.pdf
3. O. Haviv and O. Regev, *The Euclidean distortion of flat tori*, related contextual account of Khot–Naor's \(L_1\) lower bound. https://cims.nyu.edu/~regev/papers/embeddingtori.pdf
