# Sharp conditioning of two-tap cyclic Gabor operator bands

## Finding
Fix an integer \(N\ge 3\), a nonzero separation \(a\in\mathbb Z_N\) of additive order \(L=N/\gcd(N,a)\ge3\), and a complex coefficient \(z\ne0\). Normalize the two-site window as
\[
 g_{a,z}=\frac{e_0+z e_a}{\sqrt{1+|z|^2}}.
\]
Let \(\mathcal M_{a,z}\) consist of all \(N^2\) cyclic Gabor intensity-lifting measurements, defined precisely below. They observe the Hermitian matrix band with diagonal offsets \(0,+a,-a\), of real dimension \(3N\).

Set \(x=|z|^2\), and
\[
 s_L^2=\begin{cases}0,&L\text{ even},\\ \sin^2(\pi/(2L)),&L\text{ odd},\end{cases}
 \qquad m_L=3-4s_L^2,\qquad
 X_L=\frac{m_L+\sqrt{m_L^2-4}}2.
\]
For each fixed separation with \(L\ge3\), the smallest possible spectral condition number of the lifted measurements **on their entire observable operator band** is
\[
 \boxed{\inf_{z\ne0}\kappa(\mathcal M_{a,z}|_{\mathcal B_a})=\sqrt{5-4s_L^2}.}
\]
Equality holds **exactly** when \(|z|^2\in\{X_L,X_L^{-1}\}\); the argument of \(z\) is unrestricted. In particular, equal tap powers are optimal only for step order \(L=3\). For even \(L\), equal tap powers make the restricted map noninjective, whereas the optimal tap-power ratio is the square of the golden ratio (or its reciprocal) and the sharp condition number is \(\sqrt5\), independent of \(L\).

If the step may also be chosen, write \(p_*\) for the smallest odd prime divisor of \(N\), when one exists. The sharp two-tap design value over all non-antipodal separations is
\[
 \boxed{\kappa_{\mathrm{best}}(N)=
 \begin{cases}
 \sqrt{5-4\sin^2(\pi/(2p_*))},&\text{if }N\text{ has an odd prime factor},\\
 \sqrt5,&\text{if }N\text{ is a power of two}.
 \end{cases}}
\]
In the first regime, the optimizing differences are exactly those of order \(p_*\), with the optimal ratios specified above; in the second, every difference of order at least four is optimal when equipped with either golden-ratio tap-power weighting. These are **linear inverse-operator conditioning** results, not universal nonlinear phase-retrieval stability statements.

## Assumptions and scope
The ambient Hilbert space is \(\mathbb C^N\), with indices modulo \(N\). Put \(\omega=e^{2\pi i/N}\), \((T_u f)(j)=f(j-u)\), and \((M_vf)(j)=\omega^{vj}f(j)\). For any matrix \(H\), set
\[
 \mathcal M_{a,z}(H)_{u,v}=
 (M_vT_ug_{a,z})^*H(M_vT_ug_{a,z}),
 \qquad (u,v)\in\mathbb Z_N^2.
\]
Its domain is given the Hilbert–Schmidt norm and its codomain the **unaveraged** Euclidean norm. The observable band is
\[
 \mathcal B_a=\{H\in M_N(\mathbb C):H_{j,k}=0\text{ unless }k-j\in\{0,a,-a\}\}.
\]
For Hermitian operators the domain is the real Hilbert space \(\mathcal B_a\cap\mathrm{Herm}(N)\) with the same Frobenius metric. All singular values below are those of the complexification, equivalently of the real Hermitian restriction with multiplicity. Condition number means largest divided by smallest singular value on the **fixed full band**, and is infinite if the restriction is noninjective. No attempt is made to reconstruct matrices outside \(\mathcal B_a\).

## Proof
**Step 1: exact band decomposition.** For \(H\in\mathcal B_a\), let \(d_u=H_{u,u}\), \(b_u=H_{u,u+a}\), and \(c_u=H_{u+a,u}\). Because \(L\ge3\), the three bands are disjoint. Writing \(x=|z|^2\), direct expansion of the rank-one measurement gives
\[
 \mathcal M_{a,z}(H)_{u,v}
 =\frac{d_u+x d_{u+a}+z\omega^{va} b_u+\overline z\,\omega^{-va} c_u}{1+x}.
 \tag{1}
\]
The three characters of \(v\), namely \(1,\omega^{va},\omega^{-va}\), are distinct and pairwise orthogonal because \(L\ge3\). Parseval in \(v\) therefore yields the exact identity
\[
 \|\mathcal M_{a,z}(H)\|_2^2=
 \frac{N}{(1+x)^2}\sum_{u\in\mathbb Z_N}
 \left(|d_u+x d_{u+a}|^2+x|b_u|^2+x|c_u|^2\right).
 \tag{2}
\]
Meanwhile \(\|H\|_F^2=\sum_u(|d_u|^2+|b_u|^2+|c_u|^2)\). Hence the two off-diagonal bands contribute exactly \(2N\) singular values equal to \(\sqrt{Nx}/(1+x)\). The diagonal band is the cyclic map \(d\mapsto\sqrt N(d+xT_{-a}d)/(1+x)\); its \(N\) singular values are
\[
 \frac{\sqrt N}{1+x}|1+x\omega^{ka}|,
 \qquad k=0,1,\ldots,N-1.
 \tag{3}
\]
Thus (2) independently proves the complete nonzero spectrum of the restricted lifting. It also proves rank \(3N\) except at \(x=1\) with even \(L\), when exactly \(N/L\) of the diagonal singular values vanish and the restricted rank is \(3N-N/L\). These rank and spectral reductions are specializations of the general Gabor-projector spectrum in Goldberger–Kang–Okoudjou; the new assertion is the sharp global parameter and separation design below.

**Step 2: condition number.** The maximum value in (3) is \(\sqrt N\), attained at \(k=0\), and the off-diagonal value never exceeds it. If \(L\) is even, the character \(-1\) occurs and the least diagonal numerator is \(|x-1|\). If \(L\) is odd, the nearest character to \(-1\) has angular distance \(\pi/L\), and the least squared numerator is \((x-1)^2+4x\sin^2(\pi/(2L))\). Both cases are captured by
\[
 \kappa(x;L)=\frac{1+x}{\min\{\sqrt{x},\sqrt{D_L(x)}\}},
 \qquad D_L(x)=(x-1)^2+4xs_L^2.
 \tag{4}
\]
The formula is invariant under \(x\mapsto x^{-1}\), so take \(x\ge1\). Let \(m_L=3-4s_L^2\). Since \(0\le s_L^2\le1/4\), the equation \(D_L(x)=x\) is \(x^2-m_Lx+1=0\), with unique larger root \(X_L\ge1\). The smaller root is its reciprocal. On \([1,X_L]\), the minimum in (4) is \(\sqrt{D_L(x)}\); on \([X_L,\infty)\), it is \(\sqrt{x}\).

To prove *global* optimality and uniqueness, set \(\beta=2s_L^2-1\) and observe that
\[
 \frac{d}{dx}\frac{(1+x)^2}{D_L(x)}
 =\frac{2(1-\beta)(1-x)(1+x)}{D_L(x)^2}.
 \tag{5}
\]
Thus the squared condition number strictly decreases on \((1,X_L]\) when this interval is nonempty. On \([X_L,\infty)\), it equals \(x+2+x^{-1}\), strictly increasing for \(x>1\). The unique minimum with \(x\ge1\) is consequently \(x=X_L\), with the endpoint case \(L=3\) giving \(X_L=1\). By reciprocity the only optimal values on \((0,\infty)\) are \(X_L\) and \(X_L^{-1}\). Since \(X_L+X_L^{-1}=m_L\), the optimal squared condition number is \(m_L+2=5-4s_L^2\), as claimed.

**Step 3: optimal separation.** Even orders yield \(\sqrt5\). For odd orders \(L\ge3\), the sharp value \(\sqrt{5-4\sin^2(\pi/(2L))}\) is strictly increasing in \(L\) and strictly less than \(\sqrt5\). All possible orders of nonzero differences are divisors of \(N\); the smallest permitted odd order is the smallest odd prime divisor \(p_*\). If there is none, \(N\) is a power of two and every allowed order is even. This proves the global design law and characterizes every optimal step and amplitude. Phases of \(z\) do not enter (2).

## Verification
The reproducible standalone program `verify_two_tap_band.py` forms the actual \(N^2\) Gabor rank-one projectors and computes the complex singular values of the full lifting without using its predicted Fourier formula. It tests all eligible separations for \(3\le N\le11\), with four amplitude choices per separation, including the proposed optimum and the singular equal-power boundary. Its 200 direct SVD comparisons over 50 separation geometries agree with (3) to maximum absolute discrepancy \(1.22\times10^{-14}\), and all 14 boundary rank defects have predicted size. It also tests the separation minimax formula for \(3\le N\le16\). Run `python verify_two_tap_band.py` with Python 3 and NumPy. The provided `VERIFIER_OUTPUT.txt` contains the actual recorded output. Finite numerical checks corroborate but do not establish the all-\(N\) theorem; the proof is (1)–(5).

## Relationship to prior work
Alaifari and Wellershoff [1] derive discrete Gabor ambiguity relations and nonlinear phase-retrieval stability estimates. Goldberger, Kang and Okoudjou [2, Theorem 2] give the general projector-Gram eigenvalue formula and [2, Proposition 3] describe possible ranks for two-site windows. These earlier results imply the *individual-window* singular spectra (3) and the rank statement; neither is advanced as a stand-alone novelty claim here. The contribution is instead the exact all-dimensions min–max design over tap powers and cyclic separations, including its parity law, least-odd-prime transition, and complete optimizer classification. Bartusel [3] studies phase-retrieval injectivity, a distinct nonlinear criterion.

The 2026 result *Exact local conditioning and optimal weighting for two-tap cyclic spectrograms* [4] concerns the real Jacobian of the **nonlinear map at a flat signal**, with a different operator, objective, and optimal gain. In particular, the sharp restricted linear-operator condition numbers in the present theorem remain at most \(\sqrt5\) when the taps are optimally weighted, even though flat-signal nonlinear phase retrieval may have much worse sensitivity as dimension grows. The result *Sharp operator-span capacity of two-sparse multi-window Gabor systems* [5] optimizes rank over collections of windows, not noise amplification of an individual observable band. The spectral framework in [2] makes (3) accessible; the exact minimax rule in (4)–(5) and the optimal arithmetic step classification were not found in the inspected comparisons. Equivalent unindexed descriptions in sparse POVM design remain a priority risk.

## Limitations
Only two nonzero window taps at separation of order at least three, all Gabor shifts, and the observable \(3N\)-real-dimensional Hermitian band are considered. In general the map is not informationally complete on **all** Hermitian matrices: it has \(N^2-3N\) invisible complex operator directions when the band is proper. For \(N>3\), neither global phase retrieval of arbitrary signals nor noise stability for recovering arbitrary rank-one projectors follows from the bound \(\kappa_{\mathrm{best}}\). The case of antipodal separation of order two has overlapping off-diagonal bands and is outside the claim. Channel-dependent or heteroscedastic noise may lead to a different design objective. No independent mathematical audit has been performed.

## References
[1] R. Alaifari and M. Wellershoff, *Stability estimates for phase retrieval from discrete Gabor measurements*, first public arXiv:1901.05296v1, 12 January 2019. https://arxiv.org/html/1901.05296v4 .

[2] A. Goldberger, S. Kang and K. A. Okoudjou, *Towards a classification of incomplete Gabor POVMs in \(\mathbb C^d\)*, first public arXiv:2106.01509v1, 2 June 2021. https://arxiv.org/html/2106.01509v1 .

[3] D. Bartusel, *Injectivity conditions for STFT phase retrieval on \(\mathbb Z\), \(\mathbb Z_d\) and \(\mathbb R^d\)*, first public arXiv:2206.06729v1, 14 June 2022. https://arxiv.org/html/2206.06729v1 .

[4] *Exact local conditioning and optimal weighting for two-tap cyclic spectrograms*, publicly indexed research result, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-exact-local-conditioning-and-optimal-weighting-for-two-tap-cycli--52be44b25eaa .

[5] *Sharp operator-span capacity of two-sparse multi-window Gabor systems*, publicly indexed research result, https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-sharp-operator-span-capacity-of-two-sparse-multi-window-gabor-sy--b553eeb756ed .
