# Extremal-process convergence for Weibull branching random walks in an i.i.d. branching environment

## Context

This record studies a supercritical branching random walk in an i.i.d. branching environment (BPRE) with stretched-exponential/Weibull displacements. The homogeneous Galton-Watson analogue was proved by Dyszewski and Gantert, while Bhattacharya and Palmowski treated regularly varying displacements in an i.i.d. branching environment. The point here is the interaction between Weibull precise large deviations and the random environment.

## Assumptions and scales

Let \(Y=(Y_j)_{j\ge0}\) be i.i.d. and let the offspring law in generation \(j\) have conditional mean \(m_j=m(Y_j)\). Put
\[
L_n(Y)=\sum_{j=0}^{n-1}\log m_j,\qquad W_n=Z_n e^{-L_n(Y)}.
\]
Assume the usual supercritical BPRE integrability ensuring \(L_n/n\to\mu>0\), \(W_n\to W\) in \(L^1\) and almost surely, and \(\{W=0\}=\{\text{extinction}\}\). Assume also the summability condition
\[
\upsilon(Y^-)=\sum_{j\ge0}e^{-L_j^-}\,
 \mathbb P(Z_j^->0\mid Y^-)<\infty
\]
for an independent time-reversed environment \(Y^-\).

Displacements are i.i.d., independent of the genealogy, centered with variance one, and have
\[
\mathbb P(X>x)=a(x)e^{-R(x)},\qquad R(x)=x^r\ell(x),\quad 0<r<1,
\]
under the smoothness and moment hypotheses used for the precise stretched-exponential large-deviation theorem of Dyszewski--Gantert.

Define \(d_n(Y)\) by \(R(d_n(Y))=L_n(Y)\) and
\[
a_n(Y)=\frac1{R'(d_n(Y))}.
\]
With the truncated cumulant polynomial \(K\), define
\[
\Psi_n(z;Y)=\inf_{s\in[0,1]}
\{R(d_n(Y)+z-nK'(s))+n(sK'(s)-K(s))\},
\]
let \(\tau_n(Y)\) be the smallest solution of
\(\Psi_n(\tau_n(Y);Y)=L_n(Y)\), and put
\(b_n(Y)=d_n(Y)+\tau_n(Y)\).
The same regular-variation bookkeeping as in the homogeneous theorem gives the familiar \(r=2/3\) transition: \(\tau_n=o(a_n)\) for \(r<2/3\), while for \(r>2/3\) the correction is of order \(nR'(d_n)\). The exact definition through \(\Psi_n\), rather than an unqualified deterministic error expansion, is used here.

## Corrected result

Let \(\{\iota_k\}\) be the points of a Poisson point process on \(\mathbb R\) with intensity \(a e^{-x}\,dx\). Conditional on \(Y^-\), let \(T_k\) be i.i.d. with
\[
\mathbb P(T=k\mid Y^-)
=\frac1{\upsilon(Y^-)}
 \sum_{j\ge0}e^{-L_j^-}
 \mathbb P(Z_j^-=k\mid Y^-),\qquad k\ge1.
\]
Take the marks independent of \(W\) and of the base Poisson process conditional on the displayed environment variables. Then, annealed (and equivalently after conditioning on survival in the nonextinct component),
\[
\mathfrak S_{a_n(Y)^{-1}}\mathfrak T_{-b_n(Y)}V_n
\ \Rightarrow\
\Lambda
=
\mathbf 1_{\{W>0\}}
\sum_k T_k\,
\delta_{\iota_k+\log(\upsilon(Y^-)W)} .
\]

The plus sign is essential with the convention
\(\mathfrak T_b\sum\delta_x=\sum\delta_{x+b}\).
Indeed, translating a Poisson process of intensity \(ae^{-x}dx\) by
\(+\log c\) multiplies its intensity by \(c\). Consequently the Laplace exponent contains the factor
\[
aW\sum_{j\ge0}e^{-L_j^-}
 \int \mathbb E[1-e^{-Z_j^-f(x)}\mid Y^-]e^{-x}\,dx,
\]
and the maximum satisfies
\[
\mathbb P\!\left[
 \frac{M_n-b_n(Y)}{a_n(Y)}\le x\ \middle|\ W>0
\right]
\longrightarrow
\mathbb E\!\left[
 e^{-a\,\upsilon(Y^-)W e^{-x}}
 \mid W>0
\right].
\]
The same point-process limit determines upper order statistics.

The published homogeneous Dyszewski--Gantert display writes the coordinate as
\(\iota_k-\log(\upsilon W)\), but its immediately following Laplace functional,
maximum corollary, and marked-process intensity all contain the multiplicative
factor \(\upsilon W\). With their stated translation convention, those formulas
are consistent with \(+\log(\upsilon W)\), not the displayed minus sign. This
record uses the internally consistent sign.

## Proof structure

The displacement large-deviation input is the homogeneous precise estimate. Conditional on the environment, the first-moment factor \(m^n\) is replaced by \(e^{L_n(Y)}\). Since \(L_n/n\to\mu\), the trimming arguments excluding no-big-jump, multiple-big-jump, and intermediate-jump classes retain the same exponential margins almost surely. Deterministic separation scales can be chosen so that shared-ancestry terms vanish.

For a fixed lag \(j\), the last \(j\) environments have the same law as
\((Y_0^-,\dots,Y_{j-1}^-)\) and are independent of the early bulk. Combining this reversal with
\(Z_{n-j}e^{-L_{n-j}}\to W\) gives the displayed Cox intensity. The assumed summability of \(\upsilon(Y^-)\) controls the tail in \(j\).

## Environment-dependent centering

The random centering is genuinely necessary when the environment itself has nontrivial \(\sqrt n\)-scale fluctuations. In particular, if
\(0<\operatorname{Var}(\log m_0)<\infty\), then the delta method gives
\[
\frac{d_n(Y)-\bar d_n}{\bar a_n}
=(L_n-n\mu)+o_{\mathbb P}(\sqrt n),
\]
so its standard deviation is asymptotic to
\(\sqrt{n\,\operatorname{Var}(\log m_0)}\). Thus a deterministic centering at the \(a_n\)-scale cannot work in that nondegenerate case. No such impossibility is claimed for a deterministic environment or under assumptions too weak to supply this variance statement.

## Limitations

The statement is annealed and uses the homogeneous precise-large-deviation analysis as a black box after conditioning on the environment. The time-reversed recent environment prevents a fixed quenched limit in genuinely nondegenerate environments. The theorem does not cover the endpoints \(r=0,1\), convergence rates, or weaker BPRE martingale hypotheses. The deterministic-centering obstruction additionally requires nondegenerate environmental fluctuations as stated above.

## Reproducibility

The support computation is in `artifacts/check_centering.py`. It illustrates the \(\sqrt n\) environmental centering fluctuations for a two-point environment and a small-generation one-big-jump mechanism; it is not a proof of the point-process theorem.

## References

- P. Dyszewski and N. Gantert, *The extremal point process for branching random walk with stretched exponential displacements*, arXiv:2212.06639.
- A. Bhattacharya and Z. Palmowski, *Extreme positions of regularly varying branching random walk in random environment*, arXiv:2101.05369 / Extremes (2025).
