# Exact logarithmic covering and positive critical gauge for irrational contracted rotations

## Finding

Consider the interval contracted rotation \(f_{\lambda,\delta}(x)=\{\lambda x+\delta\}\), where \(0<\lambda<1/3\), \(\rho\in(0,1)\) is irrational, and the unique translation giving rotation number \(\rho\) is
\[
\delta=(1-\lambda)\left(1+\sum_{k=1}^{\infty}\lambda^k(\lfloor(k+1)\rho\rfloor-\lfloor k\rho\rfloor)\right).
\]
Let \(K_{\lambda,\rho}\subset[0,1]\) be the **closed** invariant Cantor set, namely the closure of the limit set of \(f_{\lambda,\delta}\), with both lateral images at the unique discontinuity included. Let \(N_K(r)\) be the least number of closed real intervals of diameter at most \(r\) that cover \(K\). Then **for every integer** \(n\ge1\),
\[
\boxed{N_{K_{\lambda,\rho}}\left(\frac{\lambda^n}{1-\lambda}\right)=n+1.}
\]
In particular,
\[
\boxed{\lim_{r\downarrow0}\frac{N_{K_{\lambda,\rho}}(r)}{\log(1/r)}=\frac1{|\log\lambda|}.}
\]

If \(\rho\) has bounded continued-fraction partial quotients, then, for the gauge \(h_s(r)=[\log(e/r)]^{-s}\) on \(0<r\le1\), the closed invariant set satisfies
\[
\boxed{0<\mathcal H^{h_1}(K_{\lambda,\rho})<\infty,\qquad
\mathcal H^{h_s}(K_{\lambda,\rho})=\begin{cases}
\infty,&0<s<1,\\0,&s>1.
\end{cases}}
\]
Thus the inverse-logarithm gauge is genuinely critical in this parameter range. The positivity answers, in the bounded-type strongly contracting case, the invariant-set lower-bound question explicitly posed in Janson--Öberg, Problem 6.4 (2019). The result concerns the invariant **attractor**, not the exceptional set of translation parameters.

## Assumptions and scope

All logarithms are natural. The rotation number \(\rho\) is irrational and lies strictly between zero and one. The contraction satisfies \(0<\lambda<1/3\) for the **exact covering** assertion. The additional assumption on \(\rho\) for the **Hausdorff-gauge** lower bound is bounded type: its continued-fraction coefficients \(a_j\) satisfy \(1\le a_j\le A\) for one finite \(A\). The golden-mean rotation \(\rho=(\sqrt5-1)/2\) is an explicit example. At discontinuity points of the orbit coding, both one-sided limits are included in \(K\). This compact completion agrees with the two-sided invariant Cantor set \(\Lambda_\pm\) of Janson--Öberg; it need not agree setwise with the uncompleted image of the right-continuous map.

For a compact set \(E\subset\mathbb R\), \(N_E(r)\) is an **interval covering number**, not a packing number or a minimal cover by arbitrary sets of prescribed radius. \(\mathcal H^{h_s}\) denotes the standard Hausdorff measure associated with gauge \(h_s\), extended continuously and monotonically for larger arguments if necessary.

## Proof

**Step 1: exact Sturmian coding of the closed limit set.** The contracted-rotation semiconjugacy of Laurent--Nogueira and the explicit invariant-set description of Janson--Öberg give a monotone map \(\varphi\) from the circle into the interval, with the closed Cantor set equal to its image together with lateral limits. In particular, for \(0\le t<1\),
\[
\varphi(t)=\frac\delta{1-\lambda}+(1-\lambda)\sum_{j=0}^{\infty}\lambda^j\lfloor t-(j+1)\rho\rfloor.
\]
Define the binary mechanical symbols
\[
\epsilon_j(t)=\lfloor t-j\rho\rfloor-\lfloor t-(j+1)\rho\rfloor\in\{0,1\},\qquad j\ge0.
\]
The identity obtained by telescoping the geometrically weighted differences is
\[
\varphi(t)=\sum_{j=0}^{\infty}\lambda^j\bigl(\delta-\epsilon_j(t)\bigr).
\]
For a one-sided limit of \(\varphi\), take the corresponding one-sided limit of each mechanical symbol. The series converges uniformly in the symbols, so the identity extends to both lateral codings. Consequently \(K\) is exactly the image of the **closed** mechanical Sturmian shift under the above series map.

For every \(n\ge1\), the set of length-\(n\) words \((\epsilon_0,\ldots,\epsilon_{n-1})\) has **exactly \(n+1\) distinct elements**. This is the classical Sturmian factor-complexity property. It can also be read directly from the partition of \([0,1)\) by the \(n\) distinct irrational rotation points \(\{j\rho\}\), \(1\le j\le n\). Every factor occurs on an open arc of positive length; adjoining the two lateral codes introduces no further factors. Write \(K_w\) for the nonempty compact set of points with a given initial word \(w\) of length \(n\). There are exactly \(n+1\) such sets and their union is \(K\).

**Step 2: sharp separation between prefixes.** If two infinite binary sequences share their first \(n\) digits, the distance between their real-series images is bounded by
\[
\sum_{j=n}^{\infty}\lambda^j=\frac{\lambda^n}{1-\lambda}=:r_n.
\]
Thus each \(K_w\) fits inside a closed real interval of length at most \(r_n\). Conversely, if two sequences disagree first at digit \(j\le n-1\), then the leading discrepancy has magnitude \(\lambda^j\), while all later differences together have magnitude at most \(\lambda^{j+1}/(1-\lambda)\). Therefore their images differ in absolute value by at least
\[
\lambda^j\frac{1-2\lambda}{1-\lambda}\ge\lambda^{n-1}\frac{1-2\lambda}{1-\lambda}.
\]
For \(0<\lambda<1/3\), this last quantity is **strictly larger** than \(r_n\). A closed interval of diameter at most \(r_n\) cannot meet two distinct \(K_w\), so any cover needs at least \(n+1\) intervals; the preceding diameter bound gives a cover with exactly \(n+1\). This proves the exact covering formula, for every \(n\) and every irrational \(\rho\) under the stated restriction on \(\lambda\).

**Step 3: logarithmic interval-count asymptotic.** The function \(r\mapsto N_K(r)\) is nonincreasing. The geometric scales \(r_n=\lambda^n/(1-\lambda)\) have fixed logarithmic spacing \(|\log\lambda|\). Whenever \(r_{n+1}<r\le r_n\), the exact identities give \(n+1\le N_K(r)\le n+2\), up to the endpoint convention for the inequalities. Since \(\log(1/r)=n|\log\lambda|+O(1)\), the stated limit follows.

**Step 4: bounded-type control of cylinder masses.** Let \(m\) denote Lebesgue probability on the rotation circle, and push it forward through \(\varphi\) to a probability \(\mu\) supported on \(K\); the countably many discontinuity parameters have zero \(m\)-mass. Each depth-\(n\) symbolic cylinder has preimage one of the \(n+1\) arcs formed by the points \(\{j\rho\}\), \(0\le j\le n\). Let \(\Delta_n\) be the largest such arc length. Suppose the partial quotients of \(\rho\) are bounded above by \(A\). Let \(p_k/q_k\) be continued-fraction convergents with \(q_k\le n+1<q_{k+1}\). Since \(|\rho-p_k/q_k|<1/(q_kq_{k+1})\), the \(q_k\) points \(\{j\rho\}\) for \(0\le j<q_k\) lie within circular distance \(1/q_{k+1}\) of the permuted uniform grid \(\{j/q_k\}\). Every gap between these points has length at most \(1/q_k+2/q_{k+1}\le3/q_k\); additional rotation points only decrease the maximum gap. Moreover \(q_{k+1}\le(A+1)q_k\), hence
\[
\Delta_n\le\frac{3(A+1)}{n+1}.
\]
The displayed inequality is valid for all sufficiently large \(n\); finitely many small indices can be absorbed into its constant. Therefore \(\mu(K_w)\le C/(n+1)\) for every depth-\(n\) word.

**Step 5: mass distribution and the critical gauge.** Take a sufficiently small \(r\) and the largest positive integer \(n\) with \(r\le r_n\). Then \(n=\log(1/r)/|\log\lambda|+O(1)\). By Step 2, a real interval \(I\) of diameter at most \(r\) meets at most one depth-\(n\) cylinder (because their mutual distance exceeds \(r_n\)). From Step 4,
\[
\mu(I)\le\frac C{n+1}\le\frac{C'}{\log(e/r)}=C' h_1(r).
\]
The same bound extends to all larger \(r\) by increasing \(C'\). For any countable sufficiently fine cover \(\{U_i\}\) of \(K\),
\[
1=\mu(K)\le\sum_i\mu(U_i)\le C'\sum_i h_1(\operatorname{diam}U_i),
\]
so \(\mathcal H^{h_1}(K)\ge1/C'>0\). For the upper bound, Step 2 provides \(n+1\) intervals of diameter at most \(r_n\), whence
\[
\mathcal H^{h_1}(K)\le\liminf_{n\to\infty}(n+1)h_1(r_n)=\frac1{|\log\lambda|}<\infty.
\]
For \(s>1\) the same cover has total \(h_s\)-cost tending to zero. For \(0<s<1\), the ratio \(h_s(r)/h_1(r)\to\infty\) as \(r\downarrow0\), so the positive \(h_1\)-measure forces infinite \(h_s\)-measure. This completes the proof.

## Verification

The standalone `CHECK.py` is a reproducible exact-rational consistency test. It constructs mechanical words at every length from 1 to 20 for four reduced rational approximants of golden-mean rotation and checks the \(n+1\) factor count. It also checks the strict prefix separation inequality at 30 scales for each of five rational contractions below \(1/3\). The combined test passes 230 exact-rational checks. Rational approximants and finitely many scales are **not** substitutes for the irrationality argument, continued-fraction bound, or Hausdorff-measure proof; those steps are established above for the quantified infinite families.

## Relationship to prior work

Laurent and Nogueira, *Rotation number of contracted rotations*, arXiv:1704.05130 (first public 2017-04-17), establish the irrational-rotation parameter and the underlying monotone coding; their focus is rotation numbers and arithmetic properties. Janson and Öberg, *A piecewise contractive dynamical system and Phragmén's election method* (2019), equations (37), (101), Theorem 6.3, establish the closed Cantor invariant set and **finite upper** \(h_1\)-measure for all contraction parameters. Their **Problem 6.4** explicitly asks for positive gauge measure, conjecturing in particular that the inverse-logarithm gauge may be sharp for golden-mean-type slopes. The present contribution is its **strict positivity** for every bounded-type rotation with \(0<\lambda<1/3\), together with the exact all-depth covering formula and logarithmic interval-count constant. The published upper-bound result is acknowledged as prior, not represented as new.

Bugeaud, Kim, Laurent and Nogueira (arXiv:2001.00380) investigate arithmetic transcendence of points of these Cantor sets rather than logarithmic gauge size. General Sturmian word complexity and the standard mass-distribution principle are used as established methods. No new dimension-zero conclusion or new symbolic rotation conjugacy is claimed.

## Limitations

The interval-covering equality is proved only for \(0<\lambda<1/3\), and is not asserted at the boundary or beyond. The positive Hausdorff-gauge lower bound requires bounded-type \(\rho\); no sharp characterization for Liouville or all irrational slopes is proved. Hausdorff-measure positivity is not a claim of a computed **exact numerical** measure. Although the proof makes the new comparison with the published problem explicit, full global publication-priority certainty and independent scientific audit remain outstanding.

## References

1. M. Laurent and A. Nogueira, *Rotation number of interval contracted rotations*, arXiv:1704.05130, initial submission 2017-04-17; Journal of Modern Dynamics **12** (2018), 175--191. https://arxiv.org/abs/1704.05130
2. S. Janson and A. Öberg, *A piecewise contractive dynamical system and Phragmén's election method*, Bulletin de la Société Mathématique de France **147** (2019), 395--441, DOI:10.24033/bsmf.2787, notably Sections 5--6 and 8--9 and Problem 6.4. https://www.numdam.org/item/10.24033/bsmf.2787.pdf
3. Y. Bugeaud, D. H. Kim, M. Laurent and A. Nogueira, *On the Diophantine nature of the elements of Cantor sets arising in the dynamics of contracted rotations*, arXiv:2001.00380 (2020), later Annali della Scuola Normale Superiore di Pisa **22** (2021), 1691--1704. https://arxiv.org/abs/2001.00380
