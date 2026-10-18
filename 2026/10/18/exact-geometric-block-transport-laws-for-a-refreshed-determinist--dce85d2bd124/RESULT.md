# Exact geometric-block transport laws for a refreshed deterministic-arrow walk

## Finding
Consider the one-dimensional globally refreshed nearest-neighbor walk described below. Set \(a=q(1-q)\), \(b=2q-1\), \(z=1-p\), \(H=1-z+az^2\), and \(K=1+z-az^2\). For the displacement \(D\) in one geometric-length frozen-environment block, the exact distribution is
\[
\begin{aligned}
\mathbb P(D=0)&=\frac{2az}{1+z},\\
\mathbb P(D=k)&=\frac{q(1-q^2z^2)}{1+z}(qz)^{k-1}, &&k\ge1,\\
\mathbb P(D=-k)&=\frac{(1-q)(1-(1-q)^2z^2)}{1+z}((1-q)z)^{k-1}, &&k\ge1.
\end{aligned}
\]
The almost-sure speed and annealed central-limit variance for every \(q,p\in(0,1)\) are
\[
 v(p)=\frac{bpK}{(1+z)H},
\qquad
 \sigma^2(p)=\frac{4ap(1-az^2)^2}{(1+z)H^2}+\frac{4ab^2pz^2K(2-az^3)}{(1+z)^3H^3}.
\]
The formulas extend continuously to \(p=1\), where \(v(1)=b\) and \(\sigma^2(1)=4a\). In particular, for \(0<p<1\),
\[
\frac{dv}{dp}=\frac{2abz(2-az^3)}{(1+z)^2H^2},
\]
so the speed increases strictly with the refresh rate if \(q>1/2\) and decreases strictly if \(q<1/2\). For \(q=1/2\), the variance simplifies to
\[
\sigma^2(p)=\frac{p(2+z)^2}{(2-z)^2(1+z)}
\]
and increases strictly with \(p\). In contrast, for each \(q\ne1/2\), \(\sigma^2(p)\) has at least one global maximizer strictly inside \((0,1)\). No uniqueness of such a maximizer is asserted.

## Assumptions and scope
At the beginning of each block sample independent signs \((\eta_x)_{x\in\mathbb Z}\), each with \(\mathbb P(\eta_x=+1)=q\in(0,1)\). During this block the walker started at zero moves deterministically according to \(x\mapsto x+\eta_x\). After every step, independently refresh the *entire* arrow field with probability \(p\in(0,1]\). Thus one block has length \(T\), with \(\mathbb P(T=t)=p(1-p)^{t-1}\) for integers \(t\ge1\); \(D\) denotes its signed displacement. Repeated blocks are independent after translations and time regenerations. Velocity and central-limit variance refer to the annealed walk \(X_n\) at deterministic integer time \(n\), with \((X_n-nv(p))/\sqrt n\Rightarrow N(0,\sigma^2(p))\). The deterministic environment has no ellipticity: arrow probabilities equal zero or one at each site.

## Proof
**Block geometry.** Condition on the first arrow pointing right. Let \(L\ge1\) be the number of consecutive right arrows encountered from the origin before the first left arrow; then \(\mathbb P(L=j\mid\eta_0=+1)=(1-q)q^{j-1}\). The frozen path advances one unit each step until step \(L\), then alternates between sites \(L\) and \(L-1\). Given \(\eta_0=-1\), apply reflection with \(q\) replaced by \(1-q\). Consequently the block displacement is zero only after entering the nearest two-cycle and ending at an even step. Summing the geometric clock over the possible terminal phases yields
\[
\mathbb P(D=k\mid \eta_0=+1)=\frac{1-q^2z^2}{1+z}(qz)^{k-1}\quad(k\ge1),
\qquad
\mathbb P(D=0\mid\eta_0=+1)=\frac{(1-q)z}{1+z}.
\]
Reflecting and multiplying by the initial-arrow probabilities gives the displayed two-sided geometric distribution. Its total mass is one; all the tails are summable.

**Block moments and renewal CLT.** Write \(M(w)=\mathbb E[w^D]\). The derived law gives the Laurent generating function
\[
M(w)=\frac{2az}{1+z}+\frac{q(1-q^2z^2)}{1+z}\frac{w}{1-qzw}
+\frac{(1-q)(1-(1-q)^2z^2)}{1+z}\frac{w^{-1}}{1-(1-q)z/w}.
\]
Differentiate at \(w=1\) to obtain \(\mathbb ED=M'(1)=v/p\) and \(\mathbb ED^2=M''(1)+M'(1)\). Since \(T\) is geometric,
\[
\mathbb ET=1/p,\quad\mathbb ET^2=(1+z)/p^2,\quad
\mathbb E(TD)=\frac{\mathbb ED}{p}+z\frac{d}{dz}\mathbb ED,
\]
where the derivative holds \(q\) fixed and accounts for the dependence of \(D\) on \(T\). Substituting these identities into
\[
 v=\mathbb ED/\mathbb ET=p\mathbb ED,
 \qquad\sigma^2=p\mathbb E[(D-vT)^2]
\]
and factoring the rational expressions gives the two stated formulas. The pairs \((D,T)\) are iid across blocks and \(|D|\le T\) with geometric tails, so the renewal-reward strong law and central limit theorem apply. The unfinished final block has \(o_{\mathbb P}(\sqrt n)\) displacement and duration, by the geometric tail bound, transferring the central limit theorem to deterministic time.

**Monotonicity and variance phase.** Direct differentiation gives the displayed velocity derivative. Because \(a>0\), \(z\in(0,1)\), and \(2-az^3>0\), its sign is the sign of \(b\). At \(q=1/2\), differentiating the reduced variance with respect to \(z\) gives
\[
\frac{d\sigma^2}{dz}=\frac{6z^2(z+2)}{(z-2)^3(1+z)^2}<0\qquad(0<z<1),
\]
so it increases with \(p=1-z\). For \(q\ne1/2\), the exact rational expression shows
\[
\sigma^2(1-z)=4a+12ab^2z^2+O(z^3)
\quad(z\downarrow0),\qquad
\lim_{p\downarrow0}\sigma^2(p)=0.
\]
The positive quadratic term implies variance is strictly larger than \(\sigma^2(1)=4a\) for sufficiently small positive \(z\). Continuity of the rational expression on the compact interval \(p\in[0,1]\) (with \(q\) fixed) and the zero value at \(p=0\) therefore force at least one global maximum inside \((0,1)\). The local endpoint sign already follows from general earlier results; the full-rate formula and global conclusion use the explicitly derived block law.

## Verification
The accompanying `check.py` executes symbolic normalization, first/second block-moment derivations, exact rational simplification of the regenerative variance, sign/endpoint identities, and exact enumeration of frozen arrow paths for several rational biases and times through six. It independently checks finite geometric-clock mixtures with a rigorous tail error of at most \(z^8\). The completed checker reports 280 exact distribution assertions and confirms all symbolic identities. Finite tests are supplementary, not a proof of the all-parameter statement.

## Relationship to prior work
Martin and Nagel (2026) introduce the globally resampled environment model, prove general renewal-reward LLN/CLT identities, obtain speed differentiability and examples of nonmonotonic speed, and establish a biased-diffusivity local minimum at full refresh. These general facts are *prior work*, not asserted as new here. The new claim is the full two-sided geometric one-block law for non-elliptic deterministic arrows and its exact rational all-rate speed/variance, providing a global drift-monotonicity and variance-interior-maximum contrast in this natural solvable model. Avena and den Hollander (2019) treat cooling random environments with deterministic resampling times, not the exact global geometric-refresh model above. A general theorem about arrow walks or renewal rewards could make parts of this explicit specialization previously implicit; independent priority checking remains necessary.

## Limitations
Only iid arrows on the one-dimensional integer lattice, global iid geometric refreshes, and annealed fluctuations are covered; there are no statements for partially refreshed fields, quenched central limits, dependent sites, higher dimensions, or unique variance maxima. The variance-endpoint expansion and general renewal limit principles are already known. These finite formulas alone do not establish novelty against inaccessible or unidentified stronger primary sources. Independent scientific review has not been performed.

## References
1. R. Martin and J. Nagel, *Random walk in a regenerating random environment*, arXiv:2610.11919v1 (first publicly posted 2026-10-08), https://arxiv.org/html/2610.11919v1; especially Theorems 2.1 and 2.4 and equations (1.4), (1.7).
2. L. Avena and F. den Hollander, *Random walks in cooling random environments*, arXiv:1610.00641 (2016), https://arxiv.org/abs/1610.00641.
