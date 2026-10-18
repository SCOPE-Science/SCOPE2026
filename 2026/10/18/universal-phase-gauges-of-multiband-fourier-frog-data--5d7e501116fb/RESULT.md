# Universal phase gauges of multiband Fourier FROG data

## Finding
Let \(N\ge3\) be an integer, let \(L\mid N\), and let \(S\subset\{0,\ldots,N-1\}\) be a finite union of disjoint integer bands
\[
I_j=\{b_j,b_j+1,\ldots,b_j+\ell_j\},\quad
0\le b_1<b_1+\ell_1<b_2<\cdots<b_r+\ell_r<N/2,
\quad\ell_j\ge2.
\]
For Fourier coefficients \(A=(A_s)_{s\in S}\), the discrete second-harmonic frequency-resolved optical gating (FROG) trace is
\[
\mathcal F_{k,m}(A)=\frac1{N^2}\left|
 \sum_{\substack{s,t\in S\\s+t=k}}
 A_s A_t\,e^{2\pi i t mL/N}\right|^2,
\qquad 0\le k<N,\quad 0\le m<N/L.
\]
Define the *universal diagonal phase-gauge group* \(\mathcal G(S)\) to comprise exactly the phase vectors \(u=(u_s)_{s\in S}\in\mathbb T^S\) satisfying \(\mathcal F_{k,m}(uA)=\mathcal F_{k,m}(A)\) for **every** complex coefficient vector \(A\in\mathbb C^S\), every \(k\), and every sampled delay \(m\). The classification is
\[
\boxed{\mathcal G(S)=\left\{u_s=e^{i(\tau s+\gamma_j)}\text{ for }s\in I_j:\
 \tau,\gamma_j\in\mathbb R/2\pi\mathbb Z,\quad
 \gamma_i+\gamma_j\equiv\gamma_h+\gamma_k\pmod{2\pi}
 \text{ whenever }(I_i+I_j)\cap(I_h+I_k)\ne\varnothing\right\}.}
\]
Here \(i\le j\) and \(h\le k\), including repeated indices, and \(I_i+I_j\) denotes the integer Minkowski sum interval. If \(M\) is the integer matrix whose rows are \(e_i+e_j-e_h-e_k\) for these overlapping pairs of sum intervals, then
\[
\boxed{\mathcal G(S)\cong\mathbb T\times\ker(M:\mathbb T^r\to\mathbb T^{\#\mathrm{rows}}).}
\]
Writing the nonzero Smith invariant factors of \(M\) as \(d_1,\ldots,d_\rho\), its connected dimension is \(1+r-\rho\) and its number of connected components is \(\prod_{j=1}^\rho d_j\). The classification is exact for any number and lengths of bands, and requires no genericity assumption on the Fourier amplitudes.

In particular, for two bands \(S=\{0,\ldots,a\}\cup\{b,\ldots,b+c\}\), where \(a,c\ge2\), \(b>a\), and \(2(b+c)<N\), there is a **sharp phase-gap threshold**:
\[
\boxed{\mathcal G(S)\cong
\begin{cases}
\mathbb T^3,&b>\max(2a,a+c),\\
\mathbb T^2,&b\le\max(2a,a+c).
\end{cases}}
\]
The extra circle in the first regime rotates the second band independently after the unavoidable common scalar and linear-frequency phases; it survives **every** FROG delay for **every** input. If the two-band Fourier coefficients have unit modulus and common phase within each band, with relative phase \(\delta\), the precise number of zero-delay frequency rows whose intensities depend nontrivially on \(\delta\) is
\[
\boxed{H(a,b,c)=\max(0,2a-b+1)+\max(0,a+c-b+1).}
\]
Thus \(H=0\) exactly in the independent-band-phase regime.

## Assumptions and scope
Here \(\mathbb T=\{z\in\mathbb C:|z|=1\}\); the zero vector and coefficients with zero entries are included in the universal quantifier. The frequency support is known and exactly contained in the displayed bands, but individual coefficient vectors may vanish within them. The frequency cutoff \(2\max S<N\) prevents modular pair-sum wraparound. The trace formula is obtained by taking \(x_n=N^{-1}\sum_s A_s e^{2\pi isn/N}\), forming \(x_nx_{n+mL}\), and applying the unnormalized length-\(N\) discrete Fourier transform in \(n\). The sign of the exponent at the delay is a convention and does not affect the proof. Our classification concerns diagonal phase symmetries **uniform over all possible coefficient vectors**, not the full ambiguity fiber of any particular signal, and does not assert generic phase retrieval when the universal gauge is minimal.

For \(r=1\) the matrix \(M\) is empty and the universal gauge is the standard scalar-plus-frequency-slope two-torus. For arbitrary \(r\) no assumption that the overlap graph is connected, or that its relation lattice is primitive, is needed; the Smith factors record finite component obstructions exactly. The two-band formulas are stated with integer endpoints and no wraparound.

## Proof
**Step 1: Universality is equivalent to preservation of every pair-sum phase.** Write \(Z_k(A)=\sum_{s+t=k}A_sA_t\), with ordered pairs. The delay-zero trace is \(N^{-2}|Z_k(A)|^2\). If the phase gauge preserves this polynomial for every independent complex variable \(A_s\), compare coefficients of each monomial \(A_pA_q\overline{A_vA_w}\) for distinct unordered pairs \(\{p,q\}\ne\{v,w\}\) with \(p+q=v+w=k\). Its coefficient is a positive integer multiple of \(u_pu_q\overline{u_vu_w}\), with no other unordered pair decomposition generating the same monomial. The original coefficient is the same positive integer without the phase. Thus
\[
\boxed{u_pu_q=u_vu_w\quad\text{whenever }p+q=v+w.}\tag{1}
\]
Conversely, under (1), every summand of the complex FROG amplitude at a fixed \(k,m\) is multiplied by a common phase (depending on \(k\), not \(m\)); hence the whole amplitude receives that phase and all intensities are preserved. This proves that even the *complete collection of delays* imposes exactly the universal phase restrictions already visible at delay zero. This is a universal-polynomial statement, not an assertion about fixed-input fibers.

**Step 2: Each band has affine phase; all bands have one slope.** Since \(\ell_j\ge2\), the equal sums \(2s=(s-1)+(s+1)\) inside a band force \(u_s^2=u_{s-1}u_{s+1}\). Consecutive phase quotients \(u_{s+1}/u_s\) are therefore constant along each band. Denote that quotient by \(e^{i\tau_j}\). For any two bands \(I_i,I_j\), the equal-sum pairs
\[
(b_i+1)+b_j=b_i+(b_j+1)
\]
force \(e^{i\tau_i}=e^{i\tau_j}\). Thus a common \(\tau\) exists and there are unique \(\gamma_j\) modulo \(2\pi\) such that \(u_s=e^{i(\tau s+\gamma_j)}\) on \(I_j\). The parameters are unique because the adjacent quotient fixes \(\tau\) and an individual coefficient then fixes each \(\gamma_j\).

**Step 3: Exactly the Minkowski-overlap constraints remain.** The set of sums from a band pair \((i,j)\) is the full integer interval \(I_i+I_j\); every such integer has a representing pair. The product of transformed phases of any representation from that type is \(e^{i(\tau k+\gamma_i+\gamma_j)}\). Condition (1) therefore imposes equality of the band-pair offsets precisely when two corresponding sum intervals intersect. This gives the displayed complete parametrization. Its relation matrix has integer entries \(e_i+e_j-e_h-e_k\), so Smith normal form gives the connected dimension and the number of components. No other relations occur, by the converse in Step 1.

**Step 4: Sharp two-band transition and sensitive-row census.** Set \(I=[0,a]\), \(J=[b,b+c]\). The three unordered sum intervals are
\[
2I=[0,2a],\quad I+J=[b,b+a+c],\quad 2J=[2b,2b+2c].
\]
Because \(b>a\), the first and last never meet. The first meets the middle exactly when \(b\le2a\), and the middle meets the last exactly when \(b\le a+c\). Either overlap forces \(2\gamma_I=\gamma_I+\gamma_J\) or \(\gamma_I+\gamma_J=2\gamma_J\), hence \(\gamma_I=\gamma_J\). When neither overlaps the offsets are independent. This proves the sharp two-band group dichotomy.

For the flat within-band test vector \(A_s=1\) on \(I\) and \(A_s=e^{i\delta}\) on \(J\), let \(U_k,V_k,W_k\) be the ordered counts of representations of \(k\) from \(I+I\), the two cross types, and \(J+J\), respectively. Then
\[
N^2\mathcal F_{k,0}(A)=|U_k+V_ke^{i\delta}+W_ke^{2i\delta}|^2.
\]
The supports of \(U\) and \(W\) are disjoint. Whenever \(U_kV_k>0\), or \(V_kW_k>0\), the expression contains a strictly positive multiple of \(\cos\delta\) and is nonconstant; otherwise it is constant. Consequently the sensitive rows are exactly the two *disjoint* overlap intervals \([b,2a]\) and \([2b,b+a+c]\), when nonempty. Their integer cardinalities give \(H(a,b,c)\).

## Verification
Two independent finite-lattice checks accompany the proof. `artifacts/frog_phase_check.py` enumerates complete integer pair-sum relations for 195 two-band configurations, checks their exact Smith normal forms and the sharp threshold, and compares six full small FROG traces numerically. `artifacts/test_multiband.py` independently compares the original full pair-sum relation matrix with the compressed interval-overlap matrix for 280 randomly generated unions containing two through five bands, checking ranks and Smith torsion. Both scripts were executed successfully; their verbatim output is in `artifacts/checks.txt`. These tests check specified finite instances only; Steps 1–4 prove the theorem for the entire stated family. The scripts require Python 3, NumPy and SymPy and are executable from the package root.

For example, bands \([0,2]\), \([6,8]\), \([12,14]\) have \((I_1+I_3)=(I_2+I_2)=[12,16]\). The single resulting independent band-offset equation is \(\gamma_1+\gamma_3=2\gamma_2\); it reduces the universal group from dimension four to three. This illustrates why pairwise nonintersection of the original bands does not by itself predict FROG identifiability.

## Relationship to prior work
The FROG measurement model and its generic bandlimited reconstruction problem were developed in the works of Bendory, Sidorenko and Eldar (2017), and Bendory, Edidin and Eldar (2017 preprint; later journal article). Their generic identifiability results concern nonzero generic vectors in a consecutive band and do not decide the universal gauge dimension for a fixed union of disconnected bands, a nongeneric family inside the consecutive-band model. Li, Ma and Han (2021) prove FROG reconstruction results for analytic signals, with parity-related phenomena; their hypotheses and conclusions likewise differ from the universal all-input diagonal-gauge problem here. The known phase relationships for power/bispectrum of unequal two-block supports solve a different, third-order measurement problem and do not imply the quartic FROG trace threshold. Likewise, random-phase fourth-moment variance formulas for sparse trigonometric polynomials do not classify FROG invariance at all delays. The algebraic reduction to pair-sum/Freiman-type characters is standard motivation; the exact integer-band overlap classification, Smith-form evaluation, and the sharp FROG blind-gap count are the mathematical assertions assessed here. No exhaustive novelty guarantee is claimed.

## Limitations
The theorem characterizes only phase multipliers that work for **every** Fourier coefficient vector on the given support. It neither lists nor excludes further ambiguities of a fixed special input. In particular, disappearance of the extra universal phase circle is a necessary structural condition for identifiability, **not** a sufficiency theorem for generic or global phase retrieval. Flat-input sensitivity at delay zero detects a cosine of the band phase and does not uniquely recover its signed angle from that single row. The integer-band and no-wrap hypotheses are essential to the stated compact matrix formula; arbitrary sparse supports admit the pair-sum characterization (1) but need not share the interval compression. Stability, noise robustness, and continuous-time models are not addressed. Earlier additive-combinatorial or optical phase-retrieval literature may contain equivalent formulations, and priority is not independently established.

## References
1. T. Bendory, P. Sidorenko, Y. C. Eldar, *On the Uniqueness of FROG Methods*, arXiv:1701.02831 (first posted 11 January 2017), IEEE Signal Processing Letters 24 (2017), 722–726, doi:10.1109/LSP.2017.2690358.
2. T. Bendory, D. Edidin, Y. C. Eldar, *On Signal Reconstruction from FROG Measurements*, arXiv:1706.08494 (first posted 26 June 2017), Applied and Computational Harmonic Analysis 48 (2020), 1030–1044, doi:10.1016/j.acha.2018.10.003.
3. Y. Li, Y. Ma, D. Han, *FROG-measurement based phase retrieval for analytic signals*, arXiv:2103.08660 (first posted 8 March 2021), Applied and Computational Harmonic Analysis 55 (2021), 199–222, doi:10.1016/j.acha.2021.05.005.
4. *Sharp asymmetric bispectral identifiability and minimal phase sampling*, published mathematical research record, 11 October 2026, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-sharp-asymmetric-bispectral-identifiability-and-minimal-phase-sa--52a1191ef6d6 .
5. *Random-phase fourth-moment variance detects the non-Sidon relations of a finite integer support*, published mathematical research record, 11 October 2026, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-random-phase-fourth-moment-variance-detects-the-non-sidon-relati--dcec63467712 .
