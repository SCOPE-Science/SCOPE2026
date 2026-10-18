# A certified finite-game formula for Yost's index of \(\mathbb R\oplus_2 c_0\)

## Finding

Let \(X=\mathbb R\oplus_2 c_0\) be the **real** Banach space with \(\|(s,u)\|_X=(s^2+\|u\|_\infty^2)^{1/2}\). For the lower average-distance index of Yost,
\[
\mu_1(X)=\sup_{m\ge1}\sup_{x_1,\ldots,x_m\in S_X}\inf_{y\in S_X}\frac1m\sum_{i=1}^m\|x_i-y\|_X,
\]
set \(a(s)=\sqrt{1-s^2}\) and
\[
F(s,t)=\sqrt{(s-t)^2+\max\{1-s^2,1-t^2\}},\quad s,t\in[-1,1].
\]
Then the infinite-dimensional index has the **exact compact-game description**
\[
\boxed{\mu_1(X)=\max_{\nu\in\mathcal P([-1,1])}\min_{t\in[-1,1]}\int F(s,t)\,d\nu(s).}
\]
Here \(\mathcal P(I)\) is the set of Borel probability measures on the compact interval \(I\). In particular, the index admits a **certified, finite linear-program approximation of arbitrary precision**: for any integer \(N\ge1\), put \(\theta_i=i\pi/(2N)\) for \(0\le i\le N\), and
\[
K(\theta,\phi)=\frac12\sum_{\epsilon\in\{-1,1\}}\sqrt{(\epsilon\cos\theta-\cos\phi)^2+\max\{\sin^2\theta,\sin^2\phi\}}.
\]
Define \(V_N\) as the optimal value of the finite linear program
\[
\max z\quad\text{subject to}\quad w_i\ge0,\quad\sum_{i=0}^Nw_i=1,\quad z\le\sum_{i=0}^N w_i K(\theta_i,\theta_j)\quad(0\le j\le N).
\]
The **rigorous absolute-error guarantee** is
\[
\boxed{|V_N-\mu_1(X)|\le\pi/(4N).}
\]
Moreover, with \(t(X)\) the Whitley thinness index,
\[
\boxed{\frac{1+\sqrt2}{2}<\mu_1(X)<t(X)=\sqrt2.}
\]
Thus the ordinary thinness and the average-distance index separate on this elementary mixed Hilbertian–supremum-norm sum.

## Assumptions and scope

All scalars are real. The symbol \(c_0\) denotes all real sequences converging to zero, with their supremum norm. The suprema in the definition of \(\mu_1(X)\) may be taken over finite sequences, or equivalently over finite sets of pairwise distinct unit vectors (by an arbitrarily small perturbation when repetitions occur). The finite-dimensional optimization \(V_N\) is an **exact real-number linear program** with explicit real-algebraic/trigonometric coefficients; a floating-point solver alone does not certify its value. No claim is made that the limiting constant has a radical closed form, or that an optimizer of the probability game has finite support.

## Proof

**1. Reduction from the unit sphere to one scalar coordinate.** For each \(x_i=(s_i,u_i)\in S_X\) one has \(\|u_i\|_\infty=a(s_i)\). Given \(t\in[-1,1]\) and any coordinate \(n\), consider \(y_n=(t,a(t)e_n)\in S_X\). Since each \(u_i\in c_0\),
\[
\lim_{n\to\infty}\|x_i-y_n\|_X=F(s_i,t).
\]
Consequently,
\[
\inf_{y\in S_X}\frac1m\sum_i\|x_i-y\|_X\le\min_{t\in[-1,1]}\frac1m\sum_i F(s_i,t).
\]
Conversely, fix any finite list \(s_1,\ldots,s_m\in[-1,1]\) and use the \(2m\) unit vectors \(x_i^\pm=(s_i,\pm a(s_i)e_1)\). If \(y=(t,v)\in S_X\), write \(b=|v_1|\), \(c=\sup_{j\ge2}|v_j|\). Then \(\max(b,c)=a(t)\). For each \(i\), the nonnegative function
\[
h_i(r)=\sqrt{(s_i-t)^2+\max\{r,c\}^2},\quad r\ge0,
\]
is convex and nondecreasing. Jensen's inequality and \((|a-b|+|a+b|)/2=\max(a,b)\) for nonnegative \(a,b\) imply
\[
\frac{\|x_i^+-y\|_X+\|x_i^--y\|_X}{2}\ge h_i(\max\{a(s_i),b\})=F(s_i,t).
\]
Taking the average over \(i\) gives the reverse inequality after minimizing over \(y\), because the upper bound is attained as a limit with a fresh coordinate. Thus
\[
\inf_{y\in S_X}\frac1{2m}\sum_{i=1}^m(\|x_i^+-y\|_X+\|x_i^--y\|_X)=\min_t\frac1m\sum_iF(s_i,t).
\]
An arbitrarily small perturbation of coincident source vectors preserves the limit, so distinct-point formulations give the same supremum. Finite empirical measures, including those with repeated atoms, are weakly dense in \(\mathcal P([-1,1])\). Since \(F\) is jointly continuous on a compact square, the map \(\nu\mapsto\min_t\int F(s,t)\,d\nu(s)\) is weakly continuous: the corresponding integrals converge uniformly in \(t\), by uniform continuity of \(F\) and a finite-net argument. Compactness of the probability-measure space now proves the first boxed identity, including attainment of the maximum.

**2. Symmetric angular game.** The functional \(\nu\mapsto\min_t\int F(s,t)d\nu(s)\) is concave (a minimum of linear functionals) and invariant under reflection \(s\mapsto-s\). Its value therefore never decreases if \(\nu\) is replaced by the mean of \(\nu\) and its reflection. For such a symmetric measure, the minimum in \(t\) may be restricted to \([0,1]\), and the law of \(|s|\) gives exactly the angular kernel \(K\) under \(|s|=\cos\theta\), \(t=\cos\phi\). Hence
\[
\mu_1(X)=\max_{\sigma\in\mathcal P([0,\pi/2])}\min_{0\le\phi\le\pi/2}\int K(\theta,\phi)\,d\sigma(\theta).
\]

**3. Certification by finite games.** Holding one angular argument fixed, each of the two summands in \(K\) is \(1\)-Lipschitz in the other argument. Indeed, in any region where the maximum of the squared sine terms picks the varying sine, the inside vector's derivative has Euclidean norm \(1\); in the complementary region only the cosine varies and its derivative has absolute value at most \(1\). At switching points the function is continuous and the piecewise bound extends globally. Taking an arithmetic mean preserves this Lipschitz constant, in either variable.

Nearest-grid rounding on \([0,\pi/2]\) changes an angle by at most \(\delta=\pi/(4N)\). Rounding an arbitrary source measure to the grid changes the minimum payoff by at most \(\delta\), while replacing the continuous minimizing response by the grid changes any fixed source payoff by at most \(\delta\). Thus the continuous game's value is at most \(V_N+\delta\). Conversely, choosing the optimizing grid weights as a continuous source distribution gives a continuous minimum at least \(V_N-\delta\). Therefore \(|V_N-\mu_1(X)|\le\delta\), for every \(N\ge1\).

**4. Separation from Whitley thinness.** For every finite family of unit vectors \(x_i=(s_i,u_i)\), a fresh-coordinate test vector \((0,e_n)\) has limiting distance \(\sqrt{1+s_i^2}\le\sqrt2\) from every \(x_i\). This proves \(t(X)\le\sqrt2\). Conversely, with the two unit vectors \((1,0)\) and \((-1,0)\), every \(y=(t,v)\in S_X\) has maximal distance \(\sqrt{2+2|t|}\ge\sqrt2\), so \(t(X)=\sqrt2\).

For a symmetric source measure, compare the two minimizing responses \(t=0\) and \(t=1\). Their payoff average is bounded by the maximum on \([0,1]\) of
\[
H(r)=\frac12\left(\sqrt{1+r^2}+\sqrt{1+\sqrt{1-r^2}}\right).
\]
The first summand of \(H\) equals \(\sqrt2\) only at \(r=1\), while the second equals \(\sqrt2\) only at \(r=0\). Thus the continuous function \(H\) is strictly smaller than \(\sqrt2\) everywhere on the compact interval, establishing \(\mu_1(X)<\sqrt2\).

For the strict lower bound, choose the symmetric source distribution which gives mass \(1/2\) to \(s=0\) and mass \(1/4\) to each of \(s=1,-1\). Its payoff at response \(t\in[0,1]\) is \(H(t)\), and \(H(0)=H(1)=(1+\sqrt2)/2\). Setting \(q=\sqrt{1-t^2}\) rewrites \(2H(t)=\sqrt{2-q^2}+\sqrt{1+q}\), a **strictly concave** function of \(q\in[0,1]\) with equal endpoint values. Therefore every interior response pays strictly more than the endpoints. Now mix in a sufficiently small positive amount of the symmetric two-atom distribution on \(s=\pm1/\sqrt2\). This extra distribution pays \(\sqrt{3/2}\) at \(t=0\) and \(\sqrt{1+1/\sqrt2}\) at \(t=1\), both strictly greater than \((1+\sqrt2)/2\). Continuity together with the strict interior gap shows that the perturbed distribution's minimum payoff is strictly larger than \((1+\sqrt2)/2\). This proves the final strict inequality.

## Verification

The reduction uses exact norm identities, convexity, compactness and the angular Lipschitz estimate; no finite experiment is substituted for these arguments. The LP coefficients are explicit and reproducible from the displayed formula. A numerical LP exploration (not an exact certificate) gave approximately \(V_{128}=1.2403134\), \(V_{512}=1.2403169\), and \(V_{2048}=1.2403171\). Only the proved bound \(|V_N-\mu_1(X)|\le\pi/(4N)\), and not unverified floating-point digits, carries certified accuracy. The formula and its error estimate hold at every integer grid size \(N\ge1\).

## Relationship to prior work

The motivating 2014 study by Abrahamsen, Langemets, Lima and Nygaard defines Yost's lower average-distance index in Section 1, compares it with Whitley's thinness, and analyzes the latter on \(\ell_p\)-sums; its displayed results do not give this mixed-sum average-distance formula. Papini's 2001 *Averaging at any level* establishes structural properties of the average-distance index and a symmetric-family reduction but does not analyze this particular Hilbertian scalar–\(c_0\) sum. Baronti, Casini and Papini's 1998 article computes classical-space indices, including \(c_0\), according to its accessible abstract; the full text was not inspected, and possible unrecorded mixed-sum results remain a bibliographic risk. These distinctions matter: a thinness bound, a \(c_0\) value, or an abstract symmetric-source reduction does not supply the present exact scalar kernel, adversarial pair construction, finite LP, and uniform error guarantee.

## Limitations

This theorem is restricted to the stated real Banach space, not arbitrary \(\ell_p\)-sums or complex scalars. It does not identify the compact game's exact numerical value in elementary constants, prove finite support of an optimal source measure, or certify the optional floating-point illustrations. Independent mathematical verification has not been performed. A full-text comparison with the 1998 Baronti–Casini–Papini publication was unavailable; that residual literature risk is explicitly retained.

## References

1. T. A. Abrahamsen, J. Langemets, V. Lima and O. Nygaard, *On thickness and thinness of Banach spaces*, arXiv:1402.0996, v1 publicly submitted 2014-02-05; especially Introduction and Proposition 2.6. https://arxiv.org/abs/1402.0996
2. P. L. Papini, *Averaging at any level*, Acta Math. Univ. Comenianae **70** (2001), 269–280; Sections 1–4. https://studylib.net/doc/10829585/269-averaging-at-any-level
3. M. Baronti, E. Casini and P. L. Papini, *On the average distance property and the size of the unit sphere*, Atti Sem. Mat. Fis. Univ. Modena (1998); accessible abstract only. https://hdl.handle.net/11383/1792393
4. A. Hinrichs and J. Wenzel, *The average distance property of classical Banach spaces II*, Bull. Aust. Math. Soc., published online 2009-04-17; abstract reviewed. https://www.cambridge.org/core/journals/bulletin-of-the-australian-mathematical-society/article/average-distance-property-of-classical-banach-spaces-ii/EC68FA417BC0968100EFE65364F20AB6
