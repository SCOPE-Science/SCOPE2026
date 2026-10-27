# Quenched Brownian limits for cardinality-tied randomized bootstrap walks

## Finding

**Theorem (quenched completion of the independent time–cardinality model).** For any deterministic triangular array of parameters \(p_{m,k}\in[\varepsilon,1-\varepsilon]\), \(m\ge 1\), \(0\le k\le m\), with fixed \(0<\varepsilon\le 1/2\), construct the random environment and two walks below. For almost every environment, under the conditional law of the driving fair walk, for every \(T<\infty\),
\[
\left(N^{-1/2}X_{\lfloor Nt\rfloor},\;N^{-1/2}Y_{\lfloor Nt\rfloor}\right)_{0\le t\le T}
\ \Longrightarrow\ (B_t^{(1)},B_t^{(2)})_{0\le t\le T}
\]
in the Skorokhod \(J_1\) topology, where \(B^{(1)}\) and \(B^{(2)}\) are **independent standard Brownian motions**. This is a quenched, not merely annealed, functional invariance principle, without identical-distribution assumptions on \(p_{m,k}\).

More precisely, for almost every environment,
\[
\frac1N\sum_{j=0}^{\lfloor Nt\rfloor-1}\zeta_j\longrightarrow 0
\quad\text{in }L^2(\mathbb P_\xi),\quad\text{each fixed }t\ge0,
\]
and the associated cross-bracket processes converge uniformly on compact time intervals to zero in \(\mathbb P_\xi\)-probability.

## Assumptions and scope

Let \((\xi_j)_{j\ge1}\) be independent fair signs and set \(S_m=\#\{j\le m:\xi_j=-1\}\). Independently, let \(B_{m,k}\), indexed by integers \(m\ge1\) and \(0\le k\le m\), be **mutually independent** Bernoulli variables with \(\mathbb P(B_{m,k}=1)=p_{m,k}\). Define
\[
\zeta_0=1,\qquad
\zeta_m=(-1)^{\sum_{k=0}^{m}B_{m,k}\binom{S_m}{k}},
\qquad
X_n=\sum_{j=1}^n\xi_j,\qquad
Y_n=\sum_{j=1}^n\zeta_{j-1}\xi_j.
\]
The integer exponent matters only modulo two. The environment is the full independent collection \(B\); conditioning fixes all its values, leaving only the independent fair signs \(\xi\) random. These are precisely the inclusion-induced Boolean-coefficient rules for which all coefficients indexed by subsets of the same cardinality at time \(m\) are **tied** to the common bit \(B_{m,k}\). Dependence among subset coefficients at the same cardinality is therefore complete, despite independence among the \((m,k)\)-blocks.

## Proof

**1. A conditional-mean identity.** Let \(\mathcal H=L^2(\mathbb P_\xi)\). For each \(m\ge1\), view \(F_m=\zeta_m\) as an \(\mathcal H\)-valued random variable over the environment probability space. The \(F_m\) are independent because they use disjoint environment rows. Write \(h_m=\mathbb E_B F_m\in\mathcal H\). If \(S_m=s\), Bernoulli independence gives the exact identity
\[
h_m(\xi)=\prod_{\substack{0\le k\le s\\\binom{s}{k}\text{ odd}}}(1-2p_{m,k}).
\]
Lucas's parity theorem states that \(\binom{s}{k}\) is odd precisely when the one-bits of \(k\) form a subset of the one-bits of \(s\). Thus the number of odd coefficients in row \(s\) is exactly \(2^{\operatorname{pop}(s)}\), where \(\operatorname{pop}(s)\) is the number of one-bits in the binary expansion of \(s\). Put \(q=1-2\varepsilon<1\). Then
\[
|h_m(\xi)|\le q^{2^{\operatorname{pop}(S_m)}}.
\]

**2. Uniform decay of the deterministic bias.** The random variable \(S_m\) is \(\operatorname{Bin}(m,1/2)\), whose largest point mass is bounded by \(C/\sqrt m\). Put \(L_m=1+\lfloor\log_2 m\rfloor\). For every fixed integer \(r\ge1\), there are at most \(\sum_{j=0}^{r-1}\binom{L_m}{j}\) integers \(0\le s\le m\) with fewer than \(r\) binary one-bits. Splitting according to that event yields
\[
\|h_m\|_{\mathcal H}^2\le
\frac C{\sqrt m}\sum_{j=0}^{r-1}\binom{L_m}{j}
+q^{2^{r+1}}.
\]
For fixed \(r\), the first term tends to zero. Sending \(r\) to infinity proves \(\|h_m\|_{\mathcal H}\to0\). The argument is uniform over every array of Bernoulli parameters in the stipulated interval. It also applies at \(\varepsilon=1/2\), interpreted with \(q=0\).

**3. Almost-sure Hilbert-space averaging.** The independent centered \(\mathcal H\)-valued variables \(D_m=F_m-h_m\) satisfy \(\|D_m\|_{\mathcal H}\le2\). Consequently
\[
\sum_{m\ge1}\frac{\mathbb E_B\|D_m\|_{\mathcal H}^2}{m^2}<\infty.
\]
The Hilbert-space martingale \(\sum_{m=1}^nD_m/m\) therefore converges almost surely in \(\mathcal H\). Kronecker's lemma, applied in this Banach space, gives \(N^{-1}\sum_{m=1}^ND_m\to0\) in \(\mathcal H\) for almost every environment. Separately, Cesàro averaging of \(\|h_m\|_{\mathcal H}\to0\) gives \(N^{-1}\sum_{m=1}^Nh_m\to0\). Hence
\[
\left\|\frac1N\sum_{m=0}^{N-1}\zeta_m\right\|_{L^2(\mathbb P_\xi)}\to0
\quad\text{for almost every }B.
\]
The fixed initial term \(\zeta_0=1\) is negligible. A finite time mesh and the deterministic bound \(|\zeta_m|\le1\) upgrade convergence at fixed rescaled times to uniform-on-compact convergence in conditional probability.

**4. The quenched martingale limit.** Fix any environment from the full-measure set in step 3. With respect to the driving-sign filtration, \((X_n,Y_n)\) is a two-dimensional martingale with bounded increments \((\xi_j,\zeta_{j-1}\xi_j)\). Its predictable covariance matrix at step \(j\) is
\[
\begin{pmatrix}1&\zeta_{j-1}\\\zeta_{j-1}&1\end{pmatrix}.
\]
By step 3, the rescaled predictable quadratic-variation process converges in probability, uniformly on each compact time interval, to \(tI_2\). The bounded-jump martingale functional central limit theorem (whose Lindeberg condition is immediate) yields a two-dimensional standard Brownian limit. A Gaussian Brownian motion with covariance \(I_2\) has independent coordinates, completing the proof. The almost-sure exceptional set in the environment can be chosen common to all integer time horizons and hence to every finite \(T\).

## Verification

The standalone `verification.py` uses only Python's standard library. It checks the Lucas parity identity in 131,841 integer instances, enumerates the actual Bernoulli law for 45 small cases with heterogeneous rational parameters and compares exact expectations to the product formula, and checks the stated analytic bias bounds against computed binomial expectations at five larger sizes. Run `python verification.py`; captured output appears in `verification_output.txt`. These are finite checks of proof ingredients, **not** proof of the infinite limit; the Hilbert-space law of large numbers and martingale functional central limit theorem provide that proof.

## Relationship to prior work

Hamza and Tournier, *Are random random walks normal?*, arXiv:2610.01658v1 (first submitted 1 October 2026), introduce the inclusion-induced time-by-cardinality coefficient model with independent blocks, coefficients tied within a cardinality block and parameters bounded away from zero and one. Their summary records **annealed** Brownian convergence for this model (Corollary 9) and identifies its quenched counterpart as unresolved. The theorem above establishes that stronger conditional assertion for the entire stated parameter class.

Collevecchio, Hamza, Shi and Williams (2022), *Limit theorems and ergodicity for general bootstrap random walks*, give the deterministic bracket criterion for Brownian limits of adapted sign transformations. That criterion does not by itself establish the required almost-sure property of a random coefficient environment. The present calculation supplies that missing verification for the tied-cardinality model. The inclusion-induced independent-*subset* family, a time-constant Pascal-sign scenery, and the totally unordered Boolean basis have different coefficient independence assumptions and do not by themselves imply the stated row-by-cardinality quenched limit.

## Limitations

The theorem requires independence across distinct time–cardinality blocks and a uniform positive separation of all Bernoulli parameters from \(0\) and \(1\). It does not assert a limit if these assumptions fail, a quantitative almost-sure convergence rate, or almost-sure convergence of the cross-bracket under the driving-walk law. The full body of the closest 2026 manuscript beyond its accessible introductory model and result table was not exhaustively inspectable; independent priority review should compare any additional appendices, updates or related unpublished work. No independent audit has been performed.

## References

1. K. Hamza and L. Tournier, *Are random random walks normal?*, arXiv:2610.01658v1, first public 2026-10-01, https://arxiv.org/abs/2610.01658.
2. A. Collevecchio, K. Hamza, M. Shi and R. J. Williams, *Limit theorems and ergodicity for general bootstrap random walks*, Electronic Journal of Probability 27 (2022), article 92, DOI:10.1214/22-EJP818; https://arxiv.org/abs/2010.16000.
3. É. Lucas, classical binomial-coefficient parity theorem; used solely for the stated exact count of odd coefficients.
