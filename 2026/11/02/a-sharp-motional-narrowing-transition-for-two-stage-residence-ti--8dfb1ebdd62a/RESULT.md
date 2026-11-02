# A sharp motional-narrowing transition for two-stage residence times

## Finding
For stationary symmetric frequency modulation with independent Erlang-two residence times, the absorption spectrum has **one central peak** or **exactly two symmetric off-center peaks**, with no three-peak phase. The unique transition occurs at
\[
\left(\frac{\Delta}{\kappa}\right)^2=y_*,\qquad
 y_*^4+11y_*^3+10y_*^2-24y_*-32=0,\quad y_*=1.53440426264242\ldots.
\]
For \(0<\Delta/\kappa\le\sqrt{y_*}\), the sole global spectral maximum is at zero detuning; at equality it is quartically flat. For \(\Delta/\kappa>\sqrt{y_*}\), zero is a strict local minimum and the two nonzero global maxima are unique and symmetric. Their positive squared frequency is the unique positive root of the explicit quintic in the proof. At equal mean residence time, the corresponding exponential-switching process splits its lines already at \(\Delta/\kappa=1/\sqrt2\); thus the two-stage critical amplitude is larger by exactly \(\sqrt{2y_*}=1.75180150852910\ldots\).

## Assumptions and scope
Let \(\Delta,\kappa>0\). Let \(\Xi(t)\) be a stationary, symmetric alternating-renewal process with values \(+1\) and \(-1\). Each consecutive residence time in either sign is independent, with density \(\kappa^2 t e^{-\kappa t}\) on \(t>0\). The process must be stationary at observation time, rather than started at a renewal; this condition matters for non-exponential holding times.

Equivalently, use a stationary four-state continuous-time Markov chain cycling \(1\to2\to3\to4\to1\), each stage at rate \(\kappa\), with signal signs \((+,+,-,-)\). Its invariant distribution is uniform on all four stages. The two-stage holding-time law follows by adding two independent exponential stage durations.

Define the coherence \(C(t)=\mathbb E\exp(i\Delta\int_0^t\Xi(u)\,du)\). Its normalized spectral line is \(I(\omega)=\pi^{-1}\operatorname{Re}\int_0^\infty e^{-i\omega t}C(t)\,dt\), for real \(\omega\). The integral is understood as its limiting Laplace transform; for strictly positive parameters the coherence decays exponentially. The origin of frequencies is the mean transition frequency, so that \(I\) is even and integrates to one. No radiative linewidth, additional Gaussian static disorder, or nonstationary initialization is included.

## Proof
Write \(Q=\kappa\begin{psmallmatrix}-1&1&0&0\\0&-1&1&0\\0&0&-1&1\\1&0&0&-1\end{psmallmatrix}\), \(Z=\operatorname{diag}(1,1,-1,-1)\), and \({\bf1}=(1,1,1,1)^T\). The finite-state Feynman–Kac formula, initially for \(\operatorname{Re}z>0\), gives
\[
\widehat C(z)=\tfrac14{\bf1}^T(zI-Q-i\Delta Z)^{-1}{\bf1}
=\frac{z^3+4\kappa z^2+(6\kappa^2+\Delta^2)z+4\kappa^3+\kappa\Delta^2}
{(z^2+2\kappa z+\Delta^2)(z^2+2\kappa z+2\kappa^2+\Delta^2)}.
\]
For \(\Delta>0\), the tilted generator has no eigenvalue on the imaginary axis: if a modulus-preserving eigenvector existed, equality in the dissipative Dirichlet form would require its four entries to be equal; the distinct entries of \(Z\) would then force \(\Delta=0\). Thus the analytic boundary value at \(z=i\omega\) is legitimate.

Introduce \(y=(\Delta/\kappa)^2>0\) and \(x=(\omega/\kappa)^2\ge0\), and set \(J_y(x)=\pi\kappa I(\kappa\sqrt{x})\). Direct real-part calculation yields
\[
J_y(x)=\frac{y\{x^2+(6-2y)x+y^2+6y+8\}}
{[x^2+(4-2y)x+y^2][x^2-2yx+(y+2)^2]}.
\]
Both denominator factors are positive for \(x\ge0\) because they are respectively \((x-y)^2+4x\) and \((x-y)^2+4(y+1)\); the numerator is also positive. Differentiation gives
\[
J'_y(x)=-\frac{2yP_y(x)}{[x^2+(4-2y)x+y^2]^2[x^2-2yx+(y+2)^2]^2},
\]
where the exact quintic is
\[
\begin{aligned}
P_y(x)={}&x^5+(11-5y)x^4+(10y^2-20y+40)x^3\\
&+(-10y^3-6y^2-32y+52)x^2\\
&+(5y^4+28y^3+24y^2-8y+32)x\\
&-(y+2)(y^4+11y^3+10y^2-24y-32).
\end{aligned}
\]
The quartic \(f(y)=y^4+11y^3+10y^2-24y-32\) has precisely one positive root by Descartes' rule of signs; \(f(1)=-34\) and \(f(2)=64\), so \(1<y_*<2\). In particular, \(P_y(0)=-(y+2)f(y)\) changes sign once.

To rule out hidden secondary peaks, a polynomial discriminant calculation, verified by exact symbolic expansion, gives
\[
\operatorname{disc}_{x}P_y=65536y(y+2)(4y+5)^2H(y),
\]
with
\[
H(y)=512000y^6-79872y^5-954624y^4+729856y^3+1396656y^2+239112y+729.
\]
Crucially, \(H(y)>0\) on the entire positive half-line. An explicit positivity certificate is: for \(0\le y<1\), put \(y=t/(1+t)\), \(t\ge0\), and expand
\[
(1+t)^6H\left(\frac{t}{1+t}\right)=729+243486t+2603151t^2+8722180t^3+12016935t^4+6987006t^5+1843857t^6.
\]
For \(y\ge1\), put \(y=1+t\), \(t\ge0\), and expand
\[
H(1+t)=1843857+4076136t+4739760t^2+6352640t^3+6326016t^4+2992128t^5+512000t^6.
\]
All displayed coefficients are strictly positive, hence the discriminant never vanishes for \(y>0\). Consequently, real roots of \(P_y\) cannot collide or split at a positive value of \(x\). Their positive count can change only through \(x=0\), at \(y=y_*\).

At \(y=1\), \(P_1(x)=x^5+6x^4+30x^3+4x^2+81x+102>0\) for every \(x\ge0\). At \(y=2\), \(P_2(x)=x^5+x^4+40x^3-116x^2+416x-256\) has exactly one positive root: \(P_2(0)<0\), its leading coefficient is positive, and its derivative is strictly positive for \(x\ge0\) because \(120x^2-232x+416>0\) (its discriminant is negative) and all other derivative terms are nonnegative. Continuity and the nonvanishing discriminant now prove that \(P_y\) has zero positive roots for \(y<y_*\) and exactly one for \(y>y_*\). At equality it has the simple root \(x=0\) and no positive roots. Since \(J'_y\) has the opposite sign to \(P_y\), all claimed peak counts follow; the critical expansion starts at negative order \(x^2\), namely negative order \(\omega^4\).

For the comparator with exponentially distributed holding times of the same mean \(2/\kappa\), the jump rate is \(\lambda=\kappa/2\), and the well-known two-state resolvent has spectrum proportional to \(\{(\Delta^2-\omega^2)^2+4\lambda^2\omega^2\}^{-1}\). Its origin becomes a minimum precisely when \(\Delta^2>2\lambda^2=\kappa^2/2\). This proves the exact ratio \(\sqrt{2y_*}\), not merely a numerical comparison.

## Verification
Run `python check_erlang2.py` with SymPy, NumPy and SciPy installed. The checker reconstructs the four-stage resolvent algebraically, checks the rational spectral formula, differentiates to obtain the exact quintic, verifies its discriminant identity, checks both global positivity certificates coefficient-by-coefficient, isolates the critical root, and compares the formula against 150 independently assembled numerical matrix resolvents over varying detunings, rates, and observed frequencies. The finite checks are supplementary: the positive-coefficient and no-root-collision arguments prove the classification for all real positive parameters.

## Relationship to prior work
The stochastic Kubo–Anderson lineshape and its ordinary exponential-switching doublet are classical [1]. Jung, Barkai and Silbey [2] developed a stationary arbitrary-renewal expression for dichotomous frequency modulation; its generic response formula encompasses the present Erlang holding law but does not state the explicit Erlang-two peak-count partition or its critical algebraic constant. Šanda and Mukamel [3] developed related stationary continuous-time-random-walk spectroscopy, focusing on power-law waiting times and higher-order optical response. Seki and Marumoto [4] treated hopping-mediated motional narrowing in a different Gaussian static-disorder setting. Here the distinctive assertion is the **global exact one-versus-two peak classification and sharp mean-matched exchange comparison**, not the general renewal formula, resolvent method, or the qualitative motional-narrowing phenomenon.

## Limitations
The model fixes identical shape-two holding laws in both signs, symmetric stationary occupation, and zero additional homogeneous dephasing. The quartic transition constant depends on these assumptions. The initial forward holding-time distribution is the stationary residual-life law, not a freshly drawn Erlang residence; substituting a renewal-start initial state changes the spectrum. Independent historical-priority review is not claimed: general renewal formulas may permit derivation of the present special case, and coverage outside the inspected literature remains possible. No general statement for higher Erlang shapes or asymmetric holding distributions is established.

## References
[1] P. W. Anderson, “A mathematical model for the narrowing of spectral lines by exchange or motion,” *J. Phys. Soc. Jpn.* **9**, 316 (1954), DOI: 10.1143/JPSJ.9.316 (historical foundational reference; complete text not inspected).

[2] Y. Jung, E. Barkai and R. J. Silbey, “Dispersive Lineshape Theory,” arXiv:cond-mat/0008234, first submitted 2000-08-16. https://arxiv.org/html/cond-mat/0008234v1

[3] F. Šanda and S. Mukamel, “Anomalous continuous-time random-walk spectral diffusion in coherent third-order optical response,” *Phys. Rev. E* **73**, 011103 (2006), DOI: 10.1103/PhysRevE.73.011103. https://mukamel.ps.uci.edu/publications/pdfs/526.pdf

[4] K. Seki and K. Marumoto, “Motional Narrowing under Markovian and Non-Markovian Hopping Transitions in Inhomogeneous Broadened Absorption Line Shape,” arXiv:1905.01400, first submitted 2019-05-04. https://arxiv.org/abs/1905.01400
