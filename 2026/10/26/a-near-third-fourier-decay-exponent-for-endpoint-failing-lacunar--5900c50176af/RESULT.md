# A near-third Fourier-decay exponent for endpoint-failing lacunary maximal measures

## Finding

There exists one compactly supported absolutely continuous probability measure \(\mu\) on \(\mathbb R\) such that, for every \(0<\beta<1/3\),
\[
|\widehat{\mu}(\xi)|\le C_\beta(1+|\xi|)^{-\beta}\qquad(\xi\in\mathbb R),
\]
while the dyadic lacunary maximal operator
\[
M_\mu f(x)=\sup_{k\in\mathbb Z}|f*\mu_k(x)|
\]
is unbounded from \(H^1(\mathbb R)\) to \(L^{1,\infty}(\mathbb R)\). Here \(\mu_k\) is the pushforward of \(\mu\) under \(y\mapsto2^ky\), so \(f*\mu_k(x)=\int f(x-2^ky)\,d\mu(y)\).

## Assumptions and scope

The Fourier transform convention is \(\widehat{\nu}(\xi)=\int e^{-2\pi i x\xi}\,d\nu(x)\). The real Hardy space \(H^1(\mathbb R)\) is used with its atomic norm; in particular, a mean-zero function supported on an interval of length comparable to \(N^{-1}\), with height at most a constant times \(N\), is a uniformly bounded atom after a fixed normalization. The measure constructed below is a probability measure with support in \([1/2,5/2]\) and an integrable density. No smoothness or boundedness of that density is asserted. The same measure works for every exponent strictly below \(1/3\); the endpoint exponent \(1/3\) is not claimed.

## Proof

**1. Uniformly accurate point sets.** For each sufficiently large integer \(N\), let
\[
I_j=[1+(j-1)/N,1+j/N],\qquad 1\le j\le N.
\]
There are points \(x_j\in I_j\), in increasing order, such that
\[
\sup_{|\xi|\le N^3}\left|\frac1N\sum_{j=1}^N e^{-2\pi i\xi x_j}-\int_1^2e^{-2\pi i\xi x}\,dx\right|
\le C\sqrt{\frac{\log N}{N}}.\tag{1}
\]
To prove this, choose independent random points \(X_j\), each uniform on \(I_j\). The expectation of the empirical average is exactly the integral in (1), since the intervals partition \([1,2]\). For fixed \(\xi\), Hoeffding's inequality applied to real and imaginary parts gives
\[
\mathbb P\{|D_N(\xi)|>t\}\le4e^{-Nt^2/4},
\]
where \(D_N\) is the difference in (1). Also \(|D_N'(\xi)|\le7\pi\), uniformly in the sample. A mesh of spacing \(N^{-1}\) in \([-N^3,N^3]\) has \(O(N^4)\) points. Taking \(t=5\sqrt{(\log N)/N}\), the union bound makes the probability of a violation on the mesh less than one for all sufficiently large \(N\). The derivative bound extends the estimate from the mesh to the whole interval, proving (1).

**2. A family of absolutely continuous measures and its Fourier decay.** Fix the half-width \(r_N=N^{-3/2}\), and define
\[
K_N(x)=\frac{N^{1/2}}2\sum_{j=1}^N\mathbf{1}_{[x_j-r_N,x_j+r_N]}(x),\qquad d\mu_N(x)=K_N(x)\,dx.
\]
Each interval contributes mass \(1/N\), so \(\mu_N\) is a probability measure. For large \(N\), its support lies in \([1/2,5/2]\); since the points lie in ordered cells of length \(N^{-1}\), at most two of the short intervals overlap at any point, and \(\|K_N\|_\infty\le C N^{1/2}\).

Direct integration gives
\[
\widehat{\mu_N}(\xi)=\frac{\sin(2\pi\xi N^{-3/2})}{2\pi\xi N^{-3/2}}\cdot\frac1N\sum_{j=1}^Ne^{-2\pi i\xi x_j},
\]
with the quotient interpreted as one at \(\xi=0\). Hence its modulus is at most \(\min(1,CN^{3/2}/|\xi|)\) times the modulus of the empirical average. By (1) and the elementary bound on the Fourier transform of uniform measure on \([1,2]\), for \(1\le|\xi|\le N^3\),
\[
|\widehat{\mu_N}(\xi)|\le C\min(1,N^{3/2}/|\xi|)\left(|\xi|^{-1}+N^{-1/2}\sqrt{\log N}\right).\tag{2}
\]
For \(|\xi|\ge N^3\), the empirical average is at most one, so \(|\widehat{\mu_N}(\xi)|\le CN^{3/2}/|\xi|\).

Fix any \(0<\beta<1/3\). Split the frequencies into \(1\le|\xi|\le N^{3/2}\), \(N^{3/2}\le|\xi|\le N^3\), and \(|\xi|\ge N^3\). In the first range, (2) and \(N^{-1/2}\sqrt{\log N}\le C_\beta N^{-3\beta/2}\le C_\beta|\xi|^{-\beta}\) give the desired bound. In the second range, multiply the two terms in (2) by \(|\xi|^\beta\): the first is bounded by \(CN^{3/2}|\xi|^{\beta-2}\), and the second by \(CN|\xi|^{\beta-1}\sqrt{\log N}\). Both are uniformly bounded because \(\beta<1/3\); for the second term its maximum over this range is bounded by \(C N^{3\beta/2-1/2}\sqrt{\log N}\). In the third range, \(|\xi|^\beta|\widehat{\mu_N}(\xi)|\le C N^{3/2}|\xi|^{\beta-1}\le C N^{3\beta-3/2}\le C\). Frequencies of modulus at most one are handled by \(|\widehat{\mu_N}|\le1\). Thus, for every \(\beta<1/3\),
\[
|\widehat{\mu_N}(\xi)|\le C_\beta(1+|\xi|)^{-\beta}\tag{3}
\]
with a constant independent of all sufficiently large \(N\).

**3. Endpoint failure for a fixed mixture.** The geometric part of the lacunary-maximal counterexample uses only \(x_j\in I_j\), not the Fourier-approximation estimate. Write \(N=2^L\), and let
\[
a_N(x)=\frac N4\left(\mathbf{1}_{[-1/(10N),1/(10N)]}(x)-\mathbf{1}_{[9/(10N),11/(10N)]}(x)\right).
\]
This is a mean-zero \(H^1\) atom with norm at most one. Among indices in the middle half of \(\{1,\ldots,N\}\), a positive proportion satisfy \(x_j-x_{j-1}\ge1/(2N)\): group consecutive gaps in pairs and use \(x_{j+1}-x_{j-1}\ge1/N\). Call these indices \(\mathcal J_N\), and put
\[
E_k=\bigcup_{j\in\mathcal J_N}\left(2^kx_j-\frac1{20N},2^kx_j+\frac1{20N}\right),\qquad L/4\le k\le3L/8.
\]
For each such \(k\), the intervals are disjoint and \(|E_k|\ge c>0\); the sets are also disjoint as \(k\) varies because \(x_j\in[5/4,7/4]\) for these middle indices. Since \(2^kN^{-3/2}\le N^{-9/8}=o(N^{-1})\), the scaled spike around \(x_j\) lies entirely in the positive part of the atom whenever \(x\) is in its corresponding interval in \(E_k\). Its mass is \(1/N\), so its contribution to \(a_N* (\mu_N)_k(x)\) is a positive absolute constant. Earlier spikes lie outside the atom's support by the selected gap; later spikes cannot reach the atom's negative interval. Therefore
\[
a_N*(\mu_N)_k(x)\ge c\quad(x\in E_k),\qquad
\|M_{\mu_N}a_N\|_{1,\infty}\ge cL.\tag{4}
\]
The restricted range \([L/4,3L/8]\) still contains a constant multiple of \(L\) scales.

Choose a sufficiently large integer \(q\), set \(N_m=2^{q^{2m}}\), and define the single probability measure
\[
\mu=(q-1)\sum_{m=1}^\infty q^{-m}\mu_{N_m}.
\]
It is absolutely continuous and supported in \([1/2,5/2]\). Equation (3) and the summable positive weights imply the same Fourier-decay bound for \(\mu\), for every \(\beta<1/3\).

For completeness, the cross-scale estimates preserving (4) are as follows. At the scales \(q^{2m}/4\le k\le3q^{2m}/8\), the \(m\)-th component contributes at least \(c q^{1-m}\) on each \(E_k\). The components with \(\ell<m\) contribute in absolute value at most
\[
C2^{-k}\sum_{\ell<m}q^{-\ell}\|K_{N_\ell}\|_\infty
\le C N_m^{-1/4+(1/2)/q^2},
\]
which is negligible compared with \(q^{1-m}\) when \(q\) is large. The sum of components with \(\ell>m\) has convolution with \(a_{N_m}\) bounded in \(L^1\) by \(Cq^{-m}\); by Chebyshev's inequality, the set where its magnitude exceeds a fixed small multiple of \(q^{1-m}\) has measure at most \(C/q\). Choose \(q\) so this is smaller than half the uniform lower bound for \(|E_k|\). Removing those exceptional sets leaves a positive-measure subset of each \(E_k\) on which \(|a_{N_m}*\mu_k|\ge c q^{1-m}\). The scale ranges for different \(m\) are disjoint, and there are \(\asymp q^{2m}\) scales in the \(m\)-th range. Hence
\[
\|M_\mu a_{N_m}\|_{1,\infty}\ge c q^{1-m}q^{2m}=c q^{m+1}\longrightarrow\infty.
\]
Since \(\|a_{N_m}\|_{H^1}\le1\), the operator is not bounded from \(H^1\) to \(L^{1,\infty}\). This proves the claim.

## Verification

The empirical approximation is an existence proof: the Hoeffding tail bound, the \(O(N^4)\)-point mesh, and the uniform derivative estimate yield (1) for every sufficiently large integer \(N\). The Fourier estimate is uniform in \(N\) after splitting into the three stated frequency ranges; the strict inequality \(\beta<1/3\) is used to absorb the square-root logarithm. The endpoint lower bound is analytic and uses a positive-measure set at order \(\log N\) distinct scales; it is not inferred from finite numerical experiments. In the mixture, the lower-scale density bound \(\|K_{N_\ell}\|_\infty\le CN_\ell^{1/2}\), the superlacunary relation \(N_{m-1}=N_m^{1/q^2}\), and the summable high-scale tail control the two cross terms. No computer calculation is needed for the proof.

## Relationship to prior work

Zhou's 2026 preprint proves the same endpoint failure with Fourier decay exponent \(1/8\) and explicitly states that the optimal exponent is not determined. The present result sharpens the empirical approximation from order \(N^{-1/4}\) to order \(\sqrt{(\log N)/N}\), changes the spike half-width from \(N^{-2}\) to \(N^{-3/2}\), and restricts the bad-scale range to \([L/4,3L/8]\) so the geometric lower bound remains valid. These changes yield every exponent strictly below \(1/3\), for one fixed measure. Seeger–Wright (2011) and the 2017 problem collection record the broader endpoint questions; they do not state this quantitative improvement.

## Limitations

The argument does not prove Fourier decay at the endpoint exponent \(1/3\), determine the optimal exponent, or produce a smooth density. It treats the one-dimensional real-line operator; no claim is made here for singular measures or for a dimension-uniform construction. The result is a quantitative improvement of a known construction, not a new resolution of the general endpoint theory.

## References

1. X. Zhou, “Fourier decay and endpoint estimates for lacunary maximal operators,” arXiv:2610.21197 (2026), Theorem 1.1, Remark 1.2, Lemmas 2.1–2.2, Proposition 3.1, and the one-dimensional proof in §3.2.
2. A. Seeger and J. Wright, “Problems on averages and lacunary maximal functions,” *Banach Center Publications* 95 (2011), 235–250; arXiv:1007.4731.
3. L. Grafakos, D. Oliveira e Silva, M. Pramanik, A. Seeger, and B. Stovall, “Some problems in harmonic analysis,” arXiv:1701.06637 (2017), §10, Problems 14–15.
