# Prime-factor switching rigidity for tight observation of a planar rotation

## Finding

Let \(N\ge 2\) and let a planar state rotate between samples by \(R_{\pi/(2N)}\), the counterclockwise rotation through \(\pi/(2N)\). At each of the \(N\) observation times choose exactly one of the two coordinate sensors, with independent equal-variance observation noise and no process noise. A *switch* means that the selected coordinate differs between two consecutive observation times, without wrapping the last observation back to the first.

The following is a complete answer to the switching-budget question for attaining the isotropic, information-optimal finite-horizon observation Gramian.

**Theorem.** Put \(p(N)=\min\{p:p\text{ is an odd prime divisor of }N\}\), when this set is nonempty. The posterior covariance under an isotropic Gaussian prior is a scalar matrix, equivalently the observation Gramian is scalar, if and only if the associated binary sensor-sign polynomial vanishes at \(\exp(i\pi/N)\).

1. If \(N\) is a power of two, no choice of one sensor at each time gives an isotropic Gramian.
2. Otherwise an isotropic schedule exists, its least possible number of switches is exactly \(p(N)-1\), and **the only two isotropic schedules attaining this minimum** are the complementary schedules that alternate the sensor after each block of exactly \(N/p(N)\) observations.
3. In the entire infinite subfamily \(N=2^a p^b\), where \(a\ge0\), \(b\ge1\), and \(p\) is an odd prime, **all** isotropic schedules are classified: choose an arbitrary binary word of length \(M=N/p\) and repeat it in \(p\) blocks, complementing all bits in alternate blocks. There are precisely \(2^M\) such schedules (without quotienting by simultaneous sensor exchange).

Whenever an isotropic schedule exists it is simultaneously optimal, among all one-sensor-per-time schedules, for maximum smallest information eigenvalue, maximum information determinant, and minimum trace of posterior covariance with any fixed isotropic positive prior and equal observation-noise variances. The count and the switching minimum concern exact isotropy: for power-of-two horizons, this result makes no claim about which non-isotropic schedule is optimal.

## Assumptions and scope

The unknown initial state is \(x_0\in\mathbb R^2\) and evolves without process noise by
\[
x_{t+1}=R_\theta x_t,\qquad \theta=\frac{\pi}{2N},\quad t=0,\ldots,N-2.
\]
At time \(t\), the sensor index \(a_t\in\{1,2\}\) is chosen and
\[
y_t=e_{a_t}^{\mathsf T}x_t+\nu_t,\qquad \nu_t\stackrel{\mathrm{ind}}{\sim}\mathcal N(0,\sigma^2),\quad \sigma>0.
\]
For covariance comparisons, the independent prior is \(x_0\sim\mathcal N(0,\alpha^{-1}I_2)\) with \(\alpha>0\). Write \(s_t=1\) when \(a_t=1\) and \(s_t=-1\) when \(a_t=2\). Define the switch count
\[
k(s)=\sum_{t=1}^{N-1}\boldsymbol 1\{s_t\ne s_{t-1}\},
\]
and the sign polynomial \(P_s(z)=\sum_{t=0}^{N-1}s_tz^t\). The information Gramian for the initial state is
\[
W_s=\frac1{\sigma^2}\sum_{t=0}^{N-1}R_\theta^{-t}e_{a_t}e_{a_t}^{\mathsf T}R_\theta^t.
\]
Its trace is \(N/\sigma^2\) for every schedule.

## Proof

**1. Spectrum and exact optimality equivalence.** For \(v=(\cos\varphi,\sin\varphi)^{\mathsf T}\),
\[
vv^{\mathsf T}=\frac12\begin{pmatrix}1+\cos(2\varphi)&\sin(2\varphi)\\\sin(2\varphi)&1-\cos(2\varphi)\end{pmatrix}.
\]
The unnormalized observation direction at time \(t\) makes angle \(-t\theta\) or \(\pi/2-t\theta\), according to sensor choice. With \(\zeta=\exp(i\pi/N)\), its doubled-angle complex phase is \(s_t\zeta^{-t}\). Hence the two eigenvalues of \(W_s\) are exactly
\[
\lambda_\pm(W_s)=\frac{N\pm|P_s(\zeta)|}{2\sigma^2}.
\]
Thus \(W_s=N I_2/(2\sigma^2)\) precisely when \(P_s(\zeta)=0\). Among positive semidefinite two-by-two matrices of trace \(N/\sigma^2\), equality of the eigenvalues uniquely maximizes the smaller eigenvalue and determinant. With prior precision \(\alpha I_2\), posterior covariance \(C_s=(\alpha I_2+W_s)^{-1}\) has
\[
\operatorname{tr}C_s=\frac1{\alpha+\lambda_+(W_s)}+\frac1{\alpha+\lambda_-(W_s)},
\]
which is strictly increasing in \(|P_s(\zeta)|\) for fixed positive \(\alpha\). Consequently an attainable zero of \(P_s(\zeta)\) is simultaneously optimal for all three criteria.

**2. The root-of-unity ingredient.** We use the following classical consequence of Lam and Leung's classification of minimal vanishing sums of roots of unity [3, Theorems 3.3 and 4.8]: if \(\zeta\) is primitive of order \(2N\), a nonempty vanishing sum of its powers with positive unit coefficients and **no two opposite summands** is impossible when \(N\) is a power of two; otherwise such a sum has at least \(p(N)\) terms. A sum with exactly \(p(N)\) terms is necessarily a rotated regular \(p(N)\)-gon, namely a coset of the subgroup of \(p(N)\)-th roots. For clarity, decompose any vanishing sum into minimal vanishing subsums. The cited results say that the minimal sums of weight smaller than the smallest odd prime divisor are opposing pairs, whereas the first non-pair minimal sums are prime polygons, and no asymmetric minimal sum has as few terms as that smallest odd prime. With only the prime \(2\) available, every minimal subsum is an opposing pair. These conclusions also follow by repeatedly splitting root exponents according to their odd-prime components over the corresponding cyclotomic subfields.

**3. Switching lower bound and rigidity.** Let \(J=\{t\in\{1,\ldots,N-1\}:s_t\ne s_{t-1}\}\), so \(|J|=k(s)\). Using \(\zeta^N=-1\), the exact telescoping identity is
\[
(1-\zeta)P_s(\zeta)=s_0+s_{N-1}+2\sum_{t\in J}s_t\zeta^t.
\]
If \(k(s)\) is even, then \(s_{N-1}=s_0\), and \(P_s(\zeta)=0\) implies
\[
s_0+\sum_{t\in J}s_t\zeta^t=0
\]
with \(k(s)+1\) unit-root summands. If \(k(s)\) is odd, then \(s_{N-1}=-s_0\) and
\[
\sum_{t\in J}s_t\zeta^t=0
\]
with \(k(s)\) summands. In either case, the exponents of the terms before multiplication by a sign are distinct in \(\{0,\ldots,N-1\}\); absorbing the signs into \(\zeta^N=-1\) cannot create an opposing pair. The root-of-unity ingredient proves impossibility for power-of-two \(N\), and otherwise forces \(k(s)\ge p(N)-1\).

Equality has even switch count \(p(N)-1\). The resulting \(p(N)\)-term vanishing sum contains \(s_0\), so it is precisely the coset of \(p(N)\)-th roots containing \(s_0\). Its other exponents modulo \(N\) are exactly \(M,2M,\ldots,(p(N)-1)M\), where \(M=N/p(N)\). Every switch location is therefore one of these positions. Since there are exactly \(p(N)-1\) switches, all these positions occur, giving the alternating equal-length blocks. This leaves only the two choices of initial sensor.

**4. Existence.** For any odd prime \(p\mid N\), take \(M=N/p\) and \(s_t=(-1)^{\lfloor t/M\rfloor}\). Then
\[
P_s(z)=\left(\sum_{r=0}^{M-1}z^r\right)\left(\sum_{j=0}^{p-1}(-z^M)^j\right).
\]
Since \(-\zeta^M\) is a primitive \(p\)-th root of unity, the second factor vanishes at \(z=\zeta\). The construction has exactly \(p-1\) switches. Taking the least such \(p\) proves the switching optimum and its attainability.

**5. Full prime-power-family schedule census.** For \(N=2^a p^b\), with \(p\) odd, put \(M=N/p\). The cyclotomic identity
\[
\Phi_{2N}(z)=\sum_{j=0}^{p-1}(-1)^jz^{jM}
\]
has degree \((p-1)M\). Since \(\zeta\) has minimal polynomial \(\Phi_{2N}\), \(P_s(\zeta)=0\) if and only if \(\Phi_{2N}\) divides \(P_s\) over \(\mathbb Z[z]\). The quotient has degree at most \(M-1\) and integer coefficients because division is by a monic polynomial. Multiplication by the displayed cyclotomic factor places its coefficients into \(p\) nonoverlapping blocks of length \(M\). Since every coefficient of \(P_s\) is \(\pm1\), each coefficient of the quotient must be \(\pm1\). Conversely, every such quotient produces a binary sign polynomial vanishing at \(\zeta\). There are exactly \(2^M\) binary choices, proving the complete classification and count.

## Verification

The companion script `verify_sensor_schedule.py` requires only Python's standard library. Its exact-integer polynomial long division enumerates every schedule (modulo simultaneous exchange of both sensor labels) for \(2\le N\le16\), checking the zero condition, least switches, unique extremizer, and, where applicable, the complete prime-power-family census. It separately checks the explicit construction at further horizons through \(N=75\), and numerically cross-checks the Gramian eigenvalue identity. Run `python verify_sensor_schedule.py` in the package directory. The recorded successful output is:

```
EXACT_CYCLOTOMIC_OK n=2..16 schedules= 65534
CONSTRUCTIVE_CYCLOTOMIC_OK additional n=18..75
GRAM_SPECTRUM_OK exact finite model; floating angular cross-check
```

Finite exhaustive testing is not the proof for arbitrary \(N\); that rests on Steps 1–5, including the cited classical root-of-unity lemma.

## Relationship to prior work

Dutta, Wilde and Smith [1] formulate broad constrained finite-horizon sensor scheduling and Kalman covariance optimization through mixed-integer convex optimization. Liu, Fardad, Masazade and Varshney [2] investigate periodic sensor scheduling with costs and a steady-state objective. Neither work states a sharp least-switch census for an exact finite-horizon rotating two-sensor observation model. Lam and Leung [3] establish the root-of-unity structural theorem used explicitly in Step 2; no new classification of abstract minimal vanishing sums is asserted here. The distinguishing application is the exact reduction from noisy rotating observations to binary cyclotomic polynomials, together with simultaneous A/D/E optimality, switch-count rigidity, and the complete prime-power schedule census. These are exact finite-horizon statements, not general results about Kalman filters with process noise.

## Limitations

The rotation angle is tuned to \(\pi/(2N)\), the horizon has exactly \(N\) observations, one of two orthogonal coordinate sensors is active each time, measurement noise is independent and homoscedastic, and the state has no process noise. The analysis does not determine the best anisotropic schedule for power-of-two horizons or under angular perturbation, switching penalties that allow nonoptimal information, unequal sensor costs, or nonisotropic priors. The cyclotomic ingredient is classical; independent priority verification of its stated sensing application remains desirable.

## References

[1] S. Dutta, N. Wilde and S. L. Smith, *A Unified Approach to Optimally Solving Sensor Scheduling and Sensor Selection Problems in Kalman Filtering*, arXiv:2304.02692, first submitted 2023-04-05. https://arxiv.org/html/2304.02692v2

[2] S. Liu, M. Fardad, E. Masazade and P. K. Varshney, *Optimal Periodic Sensor Scheduling in Networks of Dynamical Systems*, arXiv:1305.5601, first submitted 2013-05-24. https://arxiv.org/html/1305.5601v2

[3] T. Y. Lam and K. H. Leung, *On Vanishing Sums of Roots of Unity*, arXiv:math/9511209, first submitted 1995-11-13; in particular Theorems 3.3 and 4.8. https://arxiv.org/pdf/math/9511209
