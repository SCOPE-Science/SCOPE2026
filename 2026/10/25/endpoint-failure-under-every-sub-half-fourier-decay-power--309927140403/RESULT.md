# Endpoint failure under every sub-half Fourier-decay power

## Finding

For every fixed exponent \(0<\rho<1/2\), there is a compactly supported absolutely continuous probability measure \(\mu_\rho\) on \(\mathbb R\), supported in \([1/2,5/2]\), such that
\[
|\widehat{\mu_\rho}(\xi)|\le C_\rho(1+|\xi|)^{-\rho}
\qquad(\xi\in\mathbb R),
\]
but its dyadic lacunary maximal operator
\[
M_{\mu_\rho}f(x)=\sup_{k\in\mathbb Z}|f*(\mu_\rho)_k(x)|,
\qquad
\int g\,d(\mu_\rho)_k=\int g(2^k y)\,d\mu_\rho(y),
\]
is not bounded from \(H^1(\mathbb R)\) to \(L^{1,\infty}(\mathbb R)\). We use the Fourier-transform convention
\(\widehat\mu(\xi)=\int e^{-2\pi i\xi x}\,d\mu(x)\). The result approaches the natural \(1/2\) square-integrability threshold from below; it makes no assertion at \(\rho=1/2\).

## Assumptions and scope

The measures are positive Borel probability measures on \(\mathbb R\). The maximal operator uses dyadic dilations \(2^k\), \(k\in\mathbb Z\). Endpoint failure means that no finite constant \(A\) satisfies
\[
|\{x:M_{\mu_\rho}f(x)>\lambda\}|
\le A\lambda^{-1}\|f\|_{H^1}
\]
for all \(f\in H^1(\mathbb R)\) and \(\lambda>0\). Since
\(\|f\|_{L^1}\le\|f\|_{H^1}\), this failure also rules out weak type \((1,1)\).

## Proof

### 1. Uniform point selection

For \(N\ge2\), put
\[
I_j=[1+(j-1)/N,\,1+j/N],\qquad 1\le j\le N.
\]
There are absolute constants \(A,N_0\) such that, for each \(N\ge N_0\), centers \(x_j\in I_j\) can be chosen to satisfy
\[
\sup_{|\xi|\le N^3}
\left|\frac1N\sum_{j=1}^N e^{-2\pi i\xi x_j}
-\int_1^2e^{-2\pi i\xi x}\,dx\right|
\le A\sqrt{\frac{\log N}{N}}. \tag{1}
\]

Indeed, choose independent \(X_j\) uniformly on \(I_j\), and define
\[
D_N(\xi)=\frac1N\sum_{j=1}^N e^{-2\pi i\xi X_j}
-\int_1^2e^{-2\pi i\xi x}\,dx.
\]
For each fixed \(\xi\), Hoeffding's inequality applied to the real and imaginary parts gives
\[
\mathbb P(|D_N(\xi)|>t)\le4e^{-Nt^2/4}.
\]
Differentiation and \(1\le X_j\le2\) give the deterministic bound
\(|D_N'(\xi)|\le7\pi\). The grid
\(\Gamma_N=\{m/N:|m|\le N^4\}\) has \(O(N^4)\) points and mesh \(1/N\) on \([-N^3,N^3]\). Taking \(t=A\sqrt{\log N/N}\), the union bound for a grid value exceeding \(t/2\) is at most
\[
C N^4e^{-Nt^2/16}=C N^{4-A^2/16}<1
\]
when \(A\) is a sufficiently large fixed constant and \(N\) is large. The derivative bound then extends the grid estimate to the full interval because \(7\pi/(2N)\le t/2\). This proves (1).

### 2. Fourier decay at a tunable exponent

Fix \(0<\rho<1/2\). Choose \(b\in(0,1/2)\) so that
\[
\rho<\alpha:=\frac{1}{2(1+b)},
\]
and choose \(\theta\) with \(0<\theta<b\). Fix a small constant \(\varepsilon>0\), for example \(\varepsilon=1/100\), and set
\[
r_N=\varepsilon N^{-1-b},\qquad
K_N(x)=\frac{1}{2Nr_N}\sum_{j=1}^N
\mathbf1_{[x_j-r_N,\,x_j+r_N]}(x),\qquad
d\mu_N(x)=K_N(x)\,dx.
\]
Each interval contributes mass \(1/N\), so \(\mu_N\) is a probability measure. For all sufficiently large \(N\), its support lies in \([1/2,5/2]\). Direct integration gives
\[
\widehat{\mu_N}(\xi)
=\frac{\sin(2\pi\xi r_N)}{2\pi\xi r_N}
\left(\frac1N\sum_{j=1}^N e^{-2\pi i\xi x_j}\right),
\]
with the quotient interpreted as \(1\) at zero. Hence
\[
|\widehat{\mu_N}(\xi)|
\le \min\{1,CN^{1+b}/|\xi|\}
\left|\frac1N\sum_{j=1}^N e^{-2\pi i\xi x_j}\right|. \tag{2}
\]
For \(1\le s=|\xi|\le N^3\), (1) implies
\[
\left|\frac1N\sum_{j=1}^N e^{-2\pi i\xi x_j}\right|
\le C\left(s^{-1}+\sqrt{\frac{\log N}{N}}\right). \tag{3}
\]

Set \(\Phi_\alpha(s)=(1+s)^{-\alpha}\sqrt{\log(2+s)}\). We claim
\[
|\widehat{\mu_N}(\xi)|\le C_b\Phi_\alpha(|\xi|) \tag{4}
\]
with a constant independent of \(N\). For \(1\le s\le N^{1+b}\), (2)–(3) give the bound \(C(s^{-1}+\sqrt{\log N/N})\). The \(s^{-1}\) term is bounded by \(C\Phi_\alpha(s)\). For \(s\le N\), \(\Phi_\alpha(s)\gtrsim N^{-\alpha}\), which dominates \(\sqrt{\log N/N}\) since \(\alpha<1/2\). For \(N\le s\le N^{1+b}\),
\[
\Phi_\alpha(s)\gtrsim
N^{-(1+b)\alpha}\sqrt{\log N}
=N^{-1/2}\sqrt{\log N},
\]
which also dominates the discrepancy term.

For \(N^{1+b}\le s\le N^3\), (2)–(3) and \(s^{-1}\le\sqrt{\log N/N}\) yield
\[
|\widehat{\mu_N}(\xi)|
\le C\frac{N^{1+b}}{s}\sqrt{\frac{\log N}{N}}
\le C\Phi_\alpha(s).
\]
For the last inequality, use
\(s^{1-\alpha}\sqrt{\log(2+s)}
\gtrsim N^{(1+b)(1-\alpha)}\sqrt{\log N}
=N^{1/2+b}\sqrt{\log N}\).
Finally, for \(s\ge N^3\), the trivial bound on the empirical average gives
\[
|\widehat{\mu_N}(\xi)|\le CN^{1+b}/s\le C\Phi_\alpha(s),
\]
because \(3(1-\alpha)>1+b\) for \(0<b<1/2\). The range \(s\le1\) follows from \(|\widehat{\mu_N}|\le1\). This proves (4).

Since \(\rho<\alpha\), the logarithm can be absorbed into the power:
\[
\Phi_\alpha(s)\le C_{\alpha,\rho}(1+s)^{-\rho}.
\]
Thus each selected finite-scale measure has the desired \(\rho\)-decay, uniformly in \(N\).

### 3. The endpoint obstruction survives the narrower bumps

The endpoint lower bound uses only \(x_j\in I_j\), not the Fourier approximation (1). Let \(N=2^L\) be large and define the \(H^1\) atom
\[
a_N(x)=\frac N4\left(
\mathbf1_{[-1/(10N),\,1/(10N)]}(x)
-\mathbf1_{[9/(10N),\,11/(10N)]}(x)\right).
\]
It has mean zero, is supported in an interval of length \(4/N\), and satisfies \(\|a_N\|_\infty=N/4\), so \(\|a_N\|_{H^1}\le1\).

Among indices \(N/4<j<3N/4\), let \(\mathcal J_N\) consist of those with \(x_j-x_{j-1}\ge1/(2N)\). There are \(\gtrsim N\) such indices, since each pair of adjacent gaps spans at least \(1/N\). For each integer \(k\) with \(\theta L\le k\le bL\), put
\[
E_k=\bigcup_{j\in\mathcal J_N}
\left(2^kx_j-\frac1{20N},\,2^kx_j+\frac1{20N}\right).
\]
For large \(N\), intervals within each \(E_k\) are disjoint and \(|E_k|\gtrsim1\). The sets \(E_k\) are disjoint across \(k\), since \(x_j\in[5/4,7/4]\).

For \(x\in E_k\), the contribution of the bump centered at \(x_j\) to \(a_N*(\mu_N)_k(x)\) is a fixed positive constant: the argument of \(a_N\) stays inside its positive interval because \(2^k r_N\le\varepsilon/N\). Earlier bumps contribute zero, since the scaled gap is at least \(2^k/(2N)\ge N^a/(2N)\), which exceeds the atom's support scale for large \(N\). Later bumps contribute nonnegatively, because their arguments cannot enter the negative interval \([9/(10N),11/(10N)]\). Therefore
\[
a_N*(\mu_N)_k(x)\ge c_0\qquad(x\in E_k), \tag{5}
\]
where \(c_0>0\) is independent of \(N\) and \(k\). There are \(\asymp(b-a)L\) such scales, so the finite-scale weak-\(L^1\) lower bound grows proportionally to \(L\).

Now choose a sufficiently large even integer \(q\) and let
\[
N_m=2^{q^{2m}},\qquad
\mu_\rho=(q-1)\sum_{m=1}^{\infty}q^{-m}\mu_{N_m}.
\]
The weights sum to one. Thus \(\mu_\rho\) is an absolutely continuous probability measure with support in \([1/2,5/2]\). The uniform estimate (4) passes through the mixture, giving
\[
|\widehat{\mu_\rho}(\xi)|\le C_\rho(1+|\xi|)^{-\rho}.
\]

It remains to show that the mixture retains the endpoint obstruction. Fix \(m\) and test with \(a_{N_m}\), using scales \(\theta L_m\le k\le bL_m\), where \(L_m=\log_2N_m=q^{2m}\). The \(m\)-th mixture component contributes at least \(c q^{1-m}\) on \(E_k\) by (5). The earlier components are pointwise negligible: since
\(\|K_{N_\ell}\|_\infty\le C N_\ell^{1+b}\),
\(2^{-k}\le N_m^{-a}\), and
\(N_{m-1}=N_m^{1/q^2}\), their total is bounded by
\[
Cq^{2-m}N_m^{-\theta+(1+b)/q^2}=o(q^{1-m})
\]
after choosing \(q\) so that \((1+b)/q^2<\theta\). The later components have \(L^1\) contribution \(O(q^{-m})\), so Chebyshev's inequality shows that the set where their contribution exceeds \(c q^{1-m}\) has measure \(O(1/q)\). Choose \(q\) large enough that this bad set removes less than half the measure of each \(E_k\). The remaining sets have measure \(\gtrsim1\) and are disjoint over \(\asymp(b-a)L_m\) scales. Consequently,
\[
\|M_{\mu_\rho}a_{N_m}\|_{L^{1,\infty}}
\gtrsim q^{1-m}(b-a)L_m
\asymp q^{m+1}\longrightarrow\infty,
\]
while \(\|a_{N_m}\|_{H^1}\le1\). This proves the endpoint failure.

## Verification

The concentration estimate uses Hoeffding's inequality with threshold \(A\sqrt{\log N/N}\) and an \(O(N^4)\)-point grid. The exact sinc formula and the three frequency ranges prove the tunable bound with exponent \(\alpha=1/[2(1+b)]\). The bump radius \(r_N=\varepsilon N^{-1-b}\) is small enough that the finite-scale atom argument remains valid on all scales \(\theta L\le k\le bL\). In the mixture, the earlier components are suppressed by \(2^{-k}\|K_{N_\ell}\|_\infty\), and the later components are controlled in \(L^1\); these are analytic estimates, not finite numerical tests.

## Relationship to prior work

Zhou's Theorem 1.1 gives an absolutely continuous counterexample with Fourier decay exponent \(1/8\) and failure of \(H^1\to L^{1,\infty}\) boundedness. Remark 1.2 explicitly says that \(1/8\) comes from the construction and is not claimed optimal. The present argument improves the concentration threshold in Lemma 2.1 to \(C\sqrt{\log N/N}\) and replaces the bump radius \(N^{-2}\) by a tunable \(\varepsilon N^{-1-b}\). Restricting the atom test to scales \(\theta L\le k\le bL\) preserves \(\asymp L\) disjoint levels while allowing the Fourier cutoff \(N^{1+b}\). This yields \(\alpha=1/[2(1+b)]\), and hence every decay exponent below \(1/2\), without changing the endpoint blow-up mechanism.

Seeger and Wright's earlier theorem obtains the endpoint bound under additional dimensional and smoothing hypotheses. Grafakos et al. list the decay-only endpoint questions that Zhou's result answers negatively. Neither source supplies the sub-half family proved here.

## Limitations

The construction is one-dimensional. For each \(\rho<1/2\), the measure depends on parameters \(a,b,q\) chosen for that \(\rho\); the claim does not assert a single measure works for every \(\rho\). No result is claimed at \(\rho=1/2\), and no optimality statement beyond the sub-half range is made. The centers are selected existentially rather than by an explicit deterministic algorithm.

## References

1. Xiaojing Zhou, “Fourier decay and endpoint estimates for lacunary maximal operators,” arXiv:2610.21197v1, submitted 15 October 2026, especially Theorem 1.1, Remark 1.2, Lemmas 2.1–2.2, Proposition 3.1 and §3.2. https://arxiv.org/abs/2610.21197
2. Andreas Seeger and James Wright, “Problems on averages and lacunary maximal functions,” arXiv:1007.4731 (2010), §1. https://arxiv.org/abs/1007.4731
3. Loukas Grafakos, Diogo Oliveira e Silva, Malabika Pramanik, Andreas Seeger and Betsy Stovall, “Some Problems in Harmonic Analysis,” arXiv:1701.06637v1 (2017), §10, Problems 14–15. https://arxiv.org/abs/1701.06637
