# Fourth-order skewness-induced speed in a balanced regenerating random environment

## Finding

Let the environment consist of independent, identically distributed site probabilities \(\omega_x\in[0,1]\), with \(\mathbb E\omega_0=1/2\). A nearest-neighbor walker moves to the right from site \(x\) with probability \(\omega_x\) and otherwise to the left. Immediately after each step, independently with probability \(p\in(0,1]\), the **entire** environment is replaced by a fresh independent site field. Let \(v(p)=\lim_{n\to\infty}X_n/n\), whose almost-sure existence follows from the regenerative law of large numbers.

Put \(s=\operatorname{Var}(\omega_0)\) and \(\mu_3=\mathbb E[(\omega_0-1/2)^3]\). For every such site law, as \(p\uparrow1\),

\[
\boxed{v(p)=4s\mu_3(1-p)^4+O((1-p)^6).}
\]

The fifth-order coefficient in \(1-p\) vanishes **identically**, without symmetry assumptions. More quantitatively, for every \(p\in[1/2,1]\),

\[
\boxed{\bigl|v(p)-4s\mu_3(1-p)^4\bigr|\le 8(1-p)^6.}
\]

If \(s>0\) and \(\mu_3\ne0\), the speed is nonzero and has the sign of \(\mu_3\) for all sufficiently large \(p<1\), although \(v(1)=0\). For example, the law placing masses \(1/3,2/3\) on \(1/4,5/8\), respectively, has \(s=1/32\), \(\mu_3=-1/256\), and

\[
 v(p)=-\frac{(1-p)^4}{2048}+O((1-p)^6).
\]

Its reflected environment, obtained by replacing every right probability with its complement, has the opposite local speed. If \(\mu_3=0\), the theorem asserts only \(v(p)=O((1-p)^6)\); it does **not** assert that the speed vanishes identically.

## Assumptions and scope

All sites and all successive regenerated environments are independent and have the same arbitrary probability law on \([0,1]\). No ellipticity, density, or higher-moment assumptions are needed because the transition probabilities are bounded. The resampling probability \(p\) refers to complete spatial resampling **after** a walker step, not independent single-site updates. The statement is annealed with respect to the environments and the walk. Its speed is the almost-sure long-run velocity under their joint law. The fixed first moment \(1/2\) is essential to this formulation. The expansion applies as \(p\uparrow1\), not necessarily near \(p=0\).

## Proof

**1. Regenerative reduction.** Let \(Z_m\) be the walk started at zero in a single frozen iid site environment for \(m\) steps, and set \(f_m=\mathbb EZ_m\). Each fresh-environment block has length \(G\) satisfying \(\Pr(G=m)=p(1-p)^{m-1}\). Its displacement has the law of \(Z_G\), independently across blocks after annealing. The renewal-reward law therefore gives, with \(z=1-p\),

\[
 v(p)=\frac{\mathbb EZ_G}{\mathbb EG}
      =p^2\sum_{m=1}^{\infty}f_m z^{m-1}
      =(1-z)^2\sum_{m=1}^{\infty}f_m z^{m-1}.
\]

This regenerative identity and analytic dependence on \(p\) are established in Martin–Nagel (2026), particularly their formula (3.1). They are treated here as prior results. Absolute convergence follows directly from \(|f_m|\le m\) for \(|z|<1\).

**2. Exact short-block identities.** Write \(M_j=\mathbb E\omega_0^j\), so \(M_0=1\) and \(M_1=1/2\). For nonnegative integers \(r,l\), define the finite polynomial

\[
 Q_{r,l}=\mathbb E[\omega_0^r(1-\omega_0)^l]
   =\sum_{j=0}^{l}(-1)^j\binom lj M_{r+j}.
\]

For every \(m\in\{1,\ldots,6\}\) and every sign word \(\varepsilon=(\varepsilon_1,\ldots,\varepsilon_m)\in\{-1,+1\}^m\), set \(x_0=0\) and \(x_t=\sum_{j=1}^t\varepsilon_j\). Let \(R_x\) and \(L_x\) count right and left departures from site \(x\) along that word. Independence of site probabilities, *not* independence of successive steps in a frozen field, gives the **finite exact identity**

\[
 f_m=\sum_{\varepsilon\in\{-1,+1\}^m}x_m
       \prod_{x:\,R_x+L_x>0}Q_{R_x,L_x}.
 \tag{1}
\]

Equation (1) is an explicit sum of at most \(64\) terms, with no limiting or numerical approximation. Expanding it, substituting \(M_0=1\), \(M_1=1/2\), collecting equal monomials, and factoring produces the complete table

\[
\begin{aligned}
 f_1&=f_2=f_3=f_4=0,\\
 f_5&=-\tfrac14(4M_2-1)(6M_2-4M_3-1),\\
 f_6&=-\tfrac12(4M_2-1)(6M_2-4M_3-1).
\end{aligned}
\tag{2}
\]

The full finite enumeration and symbolic reductions in (2), including all \(2^m\) sign words at each of the six lengths, are supplied as reproducible exact arithmetic in `verify.py`. In particular the identities are **exact polynomial equalities** for all admissible site laws, not interpolations from a sample of laws. One can verify (2) from (1) by ordinary finite distributivity and the binomial theorem; the finite computation merely organizes these specified algebraic steps.

Now \(4M_2-1=4s\) and

\[
 6M_2-4M_3-1=-4\mu_3.
\]

Thus (2) gives \(f_5=4s\mu_3=:A\) and \(f_6=8s\mu_3=2A\). The first potentially nonzero frozen-block mean consequently occurs at **five steps**, and the six-step mean is exactly twice that value. This second identity is responsible for cancellation of the next coefficient of the long-run speed.

**3. Cancellation and uniform remainder.** Substitution of the exact table into the renewal series gives

\[
\begin{aligned}
 v(p)&=(1-z)^2\left(Az^4+2Az^5+\sum_{m\ge7}f_mz^{m-1}\right)\\
 &=Az^4+A(-3+2z)z^6+(1-z)^2\sum_{m\ge7}f_mz^{m-1}.
\end{aligned}
\]

For real \(0\le z\le1/2\), the tail satisfies

\[
 (1-z)^2\sum_{m\ge7}|f_m|z^{m-1}
 \le (1-z)^2\sum_{m\ge7}mz^{m-1}
 =z^6(7-6z).
\]

Since \(s\le1/4\) and \(|\mu_3|\le1/8\), one has \(|A|\le1/8\). Therefore

\[
 |v(p)-Az^4|\le z^6\bigl[3|A|+7-6z\bigr]<8z^6,
\]

which proves the uniform bound and the claimed expansion. If \(A\ne0\), choosing \(0<z<\min\{1/2,\sqrt{|A|/16}\}\) makes the remainder smaller than one-half the leading term and establishes its sign.

**4. A centered, skew concrete law.** With probability \(1/3\), let \(\omega_0=1/4\); with probability \(2/3\), let \(\omega_0=5/8\). Direct exact rational calculation gives \(\mathbb E\omega_0=1/2\), \(s=1/32\), and \(\mu_3=-1/256\). Hence \(A=-1/2048\). Reflection \(\omega\mapsto1-\omega\) fixes \(s\) and negates \(\mu_3\), proving the opposite-sign example.

## Verification

Execute `python verify.py` with `sympy>=1.12` (`requirements.txt`). The program independently (i) enumerates all frozen sign words of lengths one through six and symbolically proves each identity in (2), and (ii) averages exact-rational finite-state Markov chains over all frozen two-point site assignments for three different centered site laws. The tests do not approximate coefficients or use floating point numbers. In this package the run completed successfully: **six full symbolic identities and eighteen independent exact-rational Markov calculations passed**. These finite checks verify the only nonstandard finite polynomial identities used in the proof. The infinite renewal formula is justified analytically in Step 1, and the all-order remainder is bounded analytically in Step 3.

## Relationship to prior work

Martin and Nagel (2026), *Random walk in a regenerating random environment*, prove the regenerative speed series and smoothness, and calculate \(v''(1)=-4\operatorname{Var}(\omega_0)(2\mathbb E\omega_0-1)\); their stated local extremum criterion assumes a nonzero mean one-step drift. Therefore, that curvature formula vanishes identically in the balanced case examined here. Their general series implies that higher coefficients are in principle accessible from frozen finite-time displacement moments, but does **not** evaluate those moments or determine the leading order and direction in the balanced, skew case. The new evaluated fourth-order identity, exact fifth-order cancellation, and uniform sixth-order error bound answer that unresolved local sign question for an arbitrary centered site law.

Avena, Chino, da Costa and den Hollander (2019) study *cooling* environments with intervals of deterministic increasing lengths; their asymptotic speed is inherited from the frozen model in the cooling regime. Their hypotheses and conclusions do not produce this geometric short-block, complete-refresh expansion. Classical static one-dimensional random-environment theorems likewise determine static transience or speed from different observables and do not imply a fourth-order expansion in the independent geometric refresh probability without additional finite-path analysis.

## Limitations

The result does not determine the sign of the speed at moderate or rare refresh probabilities, its global monotonicity, or the speed when \(\mu_3=0\). It concerns one spatial dimension, nearest-neighbor jumps, iid site probabilities and **global** regeneration only. It is not a general theorem for local-update environments. The sharp coefficient and its cancellation are new evaluations of a previously known regenerative series, not a new construction of that series. A broader unpublished coefficient identity or an earlier high-order expansion may exist; independent priority assessment has not been performed. All scientific claims here have received self-review only.

## References

- R. Martin and J. Nagel, *Random walk in a regenerating random environment* (first public version 2026-10-08), arXiv:2610.11919v1, especially Theorem 2.1 and equations (3.1), (3.5)–(3.7). https://arxiv.org/abs/2610.11919
- L. Avena, Y. Chino, C. da Costa and F. den Hollander, *Random walk in cooling random environment: ergodic limits and concentration inequalities*, Electronic Journal of Probability **24** (2019), article 38, DOI:10.1214/19-EJP296. Preprint: https://arxiv.org/abs/1803.03295
- F. Solomon, *Random walks in a random environment*, Annals of Probability **3** (1975), 1–31 (static-environment comparison only).
