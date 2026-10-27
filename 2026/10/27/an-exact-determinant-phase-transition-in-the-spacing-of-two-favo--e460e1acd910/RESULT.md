# An exact determinant phase transition in the spacing of two favorable seasons for two-stage populations

## Finding

Fix an integer \(n\ge4\), and let a deterministic two-stage population follow \(z_{t+1}=M_tz_t\), with exactly two favorable seasons per period. Define the baseline matrix
\[
B=\begin{pmatrix}r&b\\c&d\end{pmatrix},\qquad A=B+\delta E_{11},
\]
where \(r,d\ge0\), \(r+d>0\), and \(b,c,\delta>0\). All matrices have nonnegative entries; no stochastic normalization is imposed. The long-run annual population multiplier for a period matrix \(P\) is \(\rho(P)^{1/n}\).

Up to cyclic rotation and time reversal, let \(k\in\{1,\ldots,n-1\}\) denote the separation of the two favorable seasons and define
\[
P_k=A B^{k-1} A B^{n-k-1}.
\]
Then **adjacent favorable seasons** (\(k=1\) or \(k=n-1\)) **strictly maximize** \(\rho(P_k)\). Among **nonadjacent placements** \(2\le k\le n-2\), the complete minimizer classification is:

- If \(rd>bc\), the most evenly spaced favorable seasons minimize growth: \(k\in\{\lfloor n/2\rfloor,\lceil n/2\rceil\}\), interpreted modulo reversal.
- If \(rd=bc\), every nonadjacent placement ties for the minimum.
- If \(rd<bc\), the unique minimizers up to cyclic rotation and reversal have exactly one intervening baseline season: \(k=2\) or \(k=n-2\).

The first period exhibiting distinct nonadjacent choices is \(n=6\). Writing \(T_k=\operatorname{tr}(P_k)\) for that period, the exact identities are
\[
T_1-T_2=bc\delta^2(bc+r^2+rd+d^2)>0,\quad
T_1-T_3=bc\delta^2(r+d)^2>0,
\]
\[
T_2-T_3=bc\delta^2(rd-bc).
\]
Thus the six-season minimizer reverses exactly at the determinant-zero surface \(rd=bc\); at equality the two nonadjacent schedules tie.

## Assumptions and scope

One favorable season increases only the first-stage self-recruitment entry by the same strictly positive amount \(\delta\); the remaining three vital rates are fixed across seasons. A period contains exactly two favorable seasons and \(n-2\) baseline seasons. The matrix \(B\) is primitive under the displayed conditions, even when one diagonal entry vanishes. The theorem concerns deterministic asymptotic growth of the linear population projection and makes no claims about finite-time abundance, nonlinear density regulation, stochastic environments, or mortality under management.

## Proof

**Trace reduction.** Put \(u_j=(B^j)_{11}\) for nonnegative integers \(j\), with \(u_0=1\). Expanding the two copies of \(A=B+\delta E_{11}\), and using cyclicity of trace, yields
\[
\operatorname{tr}(P_k)=\operatorname{tr}(B^n)+2\delta(B^{n-1})_{11}
+\delta^2u_{k-1}u_{n-k-1}.\tag{1}
\]
Every schedule has determinant \(\det(A)^2\det(B)^{n-2}\). Since products of the primitive nonnegative two-stage matrices have two real eigenvalues and a simple strictly dominating positive Perron root, and since the determinant is common, the Perron root increases strictly with trace: it is the larger root of \(x^2-Tx+D=0\), and its derivative with respect to \(T\) on this family is positive. Thus optimizing growth is exactly optimizing \(u_i u_{m-i}\) for \(m=n-2\) and \(i=k-1\).

**Adjacency maximizes strictly.** For any \(1\le i\le m-1\), matrix multiplication gives
\[
u_m-u_i u_{m-i}=(B^i)_{12}(B^{m-i})_{21}>0.\tag{2}
\]
Strictness follows from \(b,c>0\) and \(r+d>0\). For \(i=0,m\), the product equals \(u_m\), proving strict adjacency maximality.

**Spectral preparation.** The diagonal similarity of \(B\) with the symmetric matrix having off-diagonal entry \(\sqrt{bc}\) gives distinct real eigenvalues \(\lambda_+>|\lambda_-|\). Here \(\lambda_+>0\), \(\lambda_+\lambda_-=rd-bc\); the strict magnitude inequality follows from the positive trace \(r+d\). Positivity of \(b,c\) makes both spectral weights of the first-coordinate projection positive, hence
\[
u_j=\alpha\lambda_+^j+\beta\lambda_-^j,\quad
\alpha,\beta>0,\quad\alpha+\beta=1.\tag{3}
\]

**Positive determinant.** When \(rd>bc\), both eigenvalues in (3) are positive. The sequence \(u_j\) is strictly log-convex: by Cauchy--Schwarz or expansion,
\[
u_{j-1}u_{j+1}-u_j^2
=\alpha\beta\lambda_+^{j-1}\lambda_-^{j-1}(\lambda_+-\lambda_-)^2>0
\quad(j\ge1).\tag{4}
\]
Consequently \(u_i u_{m-i}\) decreases strictly as the two indices approach one another, and is minimal at \(i=\lfloor m/2\rfloor,\lceil m/2\rceil\).

**Zero determinant.** When \(rd=bc\), \(\lambda_-=0\). Equation (3) gives \(u_i u_{m-i}=\alpha^2\lambda_+^m\) for all \(1\le i\le m-1\), so every nonadjacent placement ties.

**Negative determinant.** When \(rd<bc\), write \(\lambda_-=-t\lambda_+\) with \(0<t<1\). The terms depending on \(i\) in the product (3), divided by the positive factor \(\alpha\beta\lambda_+^m\), are precisely
\[
h_i=(-t)^i+(-t)^{m-i}.\tag{5}
\]
By reflection it suffices to consider \(1\le i\le m/2\). For even \(m\), the terms with even \(i\) are positive while those with odd \(i\) are negative; among the negative terms the quantity \(t^i+t^{m-i}\) is strictly largest at \(i=1\) (strict convexity of the exponential function). For odd \(m\), \(h_i=(-1)^i(t^i-t^{m-i})\) in the first half. The positive difference \(t^i-t^{m-i}\) strictly decreases with \(i\); hence its most negative signed value is at \(i=1\). The reflected choice \(i=m-1\) is the only other minimizer.

**Six-year sharp transition.** At \(n=4,5\), there is only one class of nonadjacent placements modulo cyclic rotation and reversal, so a reversal between nonadjacent types is impossible. At \(n=6\), the trace differences in the finding follow by inserting \(u_0,u_1,u_2,u_3,u_4\) into (1) and factoring, so the strict ordering changes with the sign of \(rd-bc\). For concrete strictly positive examples with \(\delta=2/5\): \((r,b,c,d)=(3/5,1/5,1/5,3/5)\) has determinant positive, whereas \((1/5,3/5,3/5,1/5)\) has determinant negative. This finishes the proof.

## Verification

The accompanying pure-Python exact-arithmetic program `verify.py` checks (1) against direct matrix products at all cyclic spacings for \(n=4,\ldots,16\), across seventeen admissible rational parameter sets covering all determinant signs and zero diagonal values. It checks the optimal spacings and all three six-year trace factorizations, totaling 1,989 exact cyclic schedule comparisons. Run `python verify.py` in the unpacked directory. Its saved output is `verification.txt`. These finite checks reproduce algebraic identities but do not substitute for the preceding proof for arbitrary real parameters and arbitrary periods.

## Relationship to prior work

Periodic matrix population models and their sensitivity calculus are established by Caswell and Trevisan (1994). Mertens, van den Bosch and Heesterbeek (2002) investigated how crop-rotation order changes weed demographic growth, evaluating up to six-year schedules in a structured seed-depth model. That work motivates the question but does not in its accessible abstract provide the universal exact two-stage all-period comparison or the determinant-sign reversal derived here. Tuljapurkar and Haridas (2006) treat temporal environmental correlation in stochastic population growth, a different random-environment objective. General matrix product/spectral-radius ordering literature provides additional related theory. The current theorem depends on a rank-one enhancement of the first-stage entry and exact two favorable years; it does not purport to cover arbitrary pairs of seasonal matrices.

## Limitations

A deterministic linear two-stage model is an idealization of actual reproduction and survival. The sign of \(rd-bc\) is not a blanket recommendation for crop management; minimizing pest growth versus maximizing desirable population growth are opposite objectives. The result describes period-averaged asymptotic multipliers, not transient maxima, noise robustness, or populations governed by density dependence. An equivalent abstract matrix-rearrangement theorem may exist in literature not available in the consulted materials; no independent bibliographic or mathematical audit is claimed.

## References

1. Caswell, H., and M. C. Trevisan (1994). *Sensitivity analysis of periodic matrix models*. Ecology 75:1299--1303. DOI: 10.2307/1937455. Publication date: 1994-07-01.
2. Mertens, S. K., F. van den Bosch, and J. A. P. Heesterbeek (2002). *Weed populations and crop rotations: exploring dynamics of a structured periodic system*. Ecological Applications 12:1125--1141. DOI: 10.1890/1051-0761(2002)012[1125:WPACRE]2.0.CO;2.
3. Tuljapurkar, S., and C. V. Haridas (2006). *Temporal autocorrelation and stochastic population growth*. Ecology Letters. DOI: 10.1111/j.1461-0248.2006.00881.x.
4. Altenberg, L. (2013). *On the ordering of spectral radius product inequalities*. SIAM Journal on Matrix Analysis and Applications. DOI: 10.1137/130906179.
