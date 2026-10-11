# An effective dimension-free hyperplane projection gap from three- and four-dimensional models

## Finding
For every integer \(n\ge3\), one can specify a real \(n\)-dimensional normed space \(X_n\) for which **every** projection onto a hyperplane satisfies the same effective inequality
\[
\|P\|>1+\varepsilon_0,
\qquad
\varepsilon_0=\frac{1}{10^6(8\cdot7^5)^{2940}}>0.
\]
The key quantitative tool is valid more broadly. Let \(E\) be a real Banach space with \(\|Q\|\ge c>1\) for every projection \(Q\) onto any closed hyperplane, and let \(r=\min\{c-1,1\}\). If \(T\in\mathcal L(E)\) has a hyperplane as its fixed-point space and \(\|T-I\|\ge1\), then
\[
\|T\|>1+\frac{r^2}{10^6}.
\]
The stated coefficient is effective and dimension-free, not asserted to be best. The full existence assertion without a numerical constant is established in subsequent literature; the novel content here is its *explicit positive rational* value and the effective fixed-space lemma that produces it.

## Assumptions and scope
All spaces and maps are real and linear. A hyperplane means a closed linear subspace of codimension one. A projection onto a hyperplane \(F\subset E\) is a bounded map \(P:E\to E\) with \(P^2=P\) and range \(F\).

For an explicit three-dimensional seed \(E_3\), take the Minkowski gauge of the convex hull of the twelve points \(\pm(1,a,c),\pm(1,b,c),\pm(c,1,a),\pm(c,1,b),\pm(a,c,1),\pm(b,c,1)\), where \(a=-3/5\), \(b=-1/5\), and \(c=1/10\). Here \(\pm v\) indicates both signs of each displayed vector. Epperlein's Theorem 1.2 [1] proves that every hyperplane projection on \(E_3\) has norm at least \(101/100\).

For \(j=4,5\), let \(p_j=\lceil(j+2)/2\rceil\) and equip \(\mathbb R^j\) with the norm
\[
\|x\|_{E_j}=\left(\sum_{i=1}^j|x_i|^{2p_j}
+\left|\sum_{i=1}^j x_i\right|^{2p_j}
+\left|\frac1j\sum_{i=1}^j i x_i\right|^{2p_j}\right)^{1/(2p_j)}.
\]
Kobos's Corollary 1.2 and its construction [2] imply that every hyperplane projection on \(E_j\) has norm strictly larger than \(1+\alpha_j\), where \(\alpha_j=(8(j+3)^5)^{-30(j+3)^2}\). In particular, \(\alpha_4=(8\cdot7^5)^{-1470}\) and \(\alpha_5=2^{-34560}\).

For \(n\ge6\), choose any nonnegative integers \(a,b\) such that \(n=3a+4b\). Such a choice exists for every integer \(n\ge6\). Equip \(X_n=E_3^{\oplus_\infty a}\oplus_\infty E_4^{\oplus_\infty b}\) with the maximum of its component norms. For \(n\in\{3,4,5\}\), put \(X_n=E_n\).

## Proof
**1. A quantitative rank-one fixed-hyperplane lemma.** Let \(S=I-T\). Since \(\ker S\) is a hyperplane and \(\|S\|\ge1\), \(S\) has rank one and satisfies \(S^2=\lambda S\) for a real scalar \(\lambda\). Put \(d=r^2/10^6\). We show that \(\|T\|\le1+d\) is impossible.

If \(\lambda\le1/5\), set \(u=1-\lambda\ge4/5\). The rank-one identity gives
\[
T^4=I-(1+u+u^2+u^3)S.
\]
Consequently,
\[
\|T^4\|\ge(1+u+u^2+u^3)\|S\|-1
\ge\frac{244}{125}> (1+10^{-6})^4
\ge\|T\|^4,
\]
a contradiction. Thus \(\lambda>1/5\). Define \(P=I-S/\lambda\), which is a projection onto \(\ker S\), and write \(u=1-\lambda\). Then \(T=P+u(I-P)\). As \(u\) is an eigenvalue of \(T\), \(|u|\le\|T\|\le1+d\).

Let \(m=\lceil200/r\rceil\) and \(B_m=m^{-1}\sum_{k=0}^{m-1}T^k\). Since \(0<r\le1\),
\[
md\le\frac{201r}{10^6},\qquad
\|B_m\|\le(1+d)^m\le e^{md}
\le1+2md<1+\frac r{2000}.
\]
Here the elementary inequality \(e^s\le1+2s\) for \(0\le s\le1/2\) applies. The explicit powers yield
\[
B_m=\beta I+(1-\beta)P,
\qquad \beta=\frac{1-u^m}{m\lambda}.
\]
Using \(m\lambda>40/r\) and \(|u|^m\le1+r/2000\),
\[
|\beta|\le\frac{(2+r/2000)r}{40}<\frac r{19}.
\]
It follows that
\[
\|P\|\le\frac{\|B_m\|+|\beta|}{1-|\beta|}
<\frac{1+r/2000+r/19}{1-r/19}<1+r\le c.
\]
The strict penultimate inequality reduces to \(1-(2+r)/19-1/2000>0\), valid for \(0<r\le1\). This contradicts the lower bound on hyperplane projections and proves \(\|T\|>1+r^2/10^6\).

**2. Quantitative transfer to finite maximum-norm sums.** Suppose \(V_1,\ldots,V_k\) are nonzero real Banach spaces of dimension at least three such that each hyperplane projection on \(V_i\) has norm at least \(c_i>1\). Put \(r_* = \min_i\min\{c_i-1,1\}\). Every hyperplane projection \(R\) on \(X=(\bigoplus_{i=1}^kV_i)_\infty\) then satisfies \(\|R\|>1+r_*^2/10^6\).

Indeed, take \(0\ne x=(x_i)\in\ker R\) and an index \(i\) with \(\|x_i\|=\|x\|\). Choose a norm-one functional \(f_i\) with \(f_i(x_i)=\|x_i\|\). Define an isometric embedding \(U:V_i\to X\) by \((Uy)_i=y\) and \((Uy)_j=f_i(y)x_j/\|x_i\|\) for \(j\ne i\). Thus \(U(x_i)=x\) and the \(i\)-th coordinate projection \(\pi_i:X\to V_i\) satisfies \(\pi_i U=I\). The operator \(B=\pi_i R U\) has \(\|B\|\le\|R\|\), fixes the codimension-one subspace \(U^{-1}(\operatorname{ran}R)\), and vanishes at the nonzero vector \(x_i\). Therefore its full fixed-point space is this hyperplane and \(\|B-I\|\ge1\). Step 1 applied to \(B\) on \(V_i\) gives \(\|R\|\ge\|B\|>1+r_*^2/10^6\).

**3. All dimensions.** For \(E_3\), take \(c_3=101/100\). For \(E_4\), take \(c_4=1+\alpha_4\). Hence \(r_*=\alpha_4\) for any sum containing only \(E_3\) and \(E_4\), and Step 2 proves a strict lower bound of \(1+\alpha_4^2/10^6=1+\varepsilon_0\) for every \(n\ge6\). For the three low dimensions the quoted results provide lower bounds \(1+1/100\), \(1+\alpha_4\), and \(1+\alpha_5\), respectively; each exceeds \(1+\varepsilon_0\). Indeed \(8\cdot7^5>2^{17}\), so
\[
\varepsilon_0<2^{-49980}<2^{-34560}=\alpha_5,
\]
and \(\varepsilon_0<\alpha_4<1/100\). This completes the construction. The elementary representations \(6=3+3\), \(7=3+4\), and \(8=4+4\), followed by repeatedly adding three, cover all \(n\ge6\).

## Verification
The fixed-hyperplane proof is analytic and uses no infinite-dimensional computation. The standalone script `verify_explicit_shadiness.py` checks the exact rational inequalities in its quantitative bounds, the numerical comparison of seed constants, and the decomposition \(n=3a+4b\) on a finite diagnostic interval. It does **not** replace the unrestricted integer argument or reproduce the computer-assisted 2025 source theorem.

To execute the diagnostic in Python 3, run `python verify_explicit_shadiness.py`; it prints `EXPLICIT_SHADINESS_RATIONAL_CHECK_OK` on success.

## Relationship to prior work
Epperlein [1], first publicly posted 2025-09-18, establishes the explicit 12-vertex three-dimensional space and its sharp-for-that-proof lower bound of \(1.01\); this foundational computational input is not new here. Kobos [2], first posted in 2015, supplies the explicit dimension-specific gap \(\alpha_j\) and the formulas for \(E_4,E_5\). Bosznay and Garay [3] proved qualitative existence in individual dimensions.

Kobos's later 2026 paper [4] establishes the existence of an **unspecified** dimension-independent constant for all hyperplane projections and describes the graph-subspace embedding used in Step 2. In particular, neither the qualitative uniform-existence theorem nor that graph observation is claimed as new. Its Section 3 explicitly notes that the non-effective mean-ergodic transfer left an *explicit numerical* uniform constant unavailable. The stated contribution is the elementary effective rank-one transfer and the concrete universal rational \(\varepsilon_0\), which is not numerically implied by an unspecified positive constant.

## Limitations
The universal constant is extremely small and no claim of optimality or practical numerical strength is made. The conclusion is for **real** normed spaces and **hyperplane** projections; extension to projections of higher codimension is unproved. The cited lower bounds for the three seed models are treated as established literature rather than independently regenerated certificates. The rational checker only validates supporting arithmetic and finite diagnostics; it does not prove the cited computer-assisted seed theorem. The 2026 qualitative theorem already covers the bare existence statement. Unindexed effective formulations in earlier projection literature remain a residual originality risk.

## References
[1] J. Epperlein, *Lower Bounds for the Shadiness Constant of Finite-Dimensional Normed Spaces*, arXiv:2509.14819v1 (2025), Theorem 1.2. https://arxiv.org/abs/2509.14819

[2] T. Kobos, *A uniform estimate of the relative projection constant*, arXiv:1508.03518v5 (first posted 2015), Corollary 1.2 and Section 5. https://arxiv.org/abs/1508.03518

[3] A. P. Bosznay and B. M. Garay, *On norms of projections*, Acta Sci. Math. 50 (1986), 87–92.

[4] T. Kobos, *Finite-dimensional normed spaces without small-norm hyperplane projections*, arXiv:2610.09113v1 (2026), Theorem 1.1 and Section 3. https://arxiv.org/abs/2610.09113
