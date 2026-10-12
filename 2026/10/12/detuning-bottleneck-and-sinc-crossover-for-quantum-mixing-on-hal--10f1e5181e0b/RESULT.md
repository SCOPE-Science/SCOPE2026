# Detuning bottleneck and sinc crossover for quantum mixing on half-flux even cycles

## Finding

**Theorem (sharp detuning scale and crossover).** Let \(n\ge4\) be even, label the vertices of a cycle by \(\mathbb Z/n\mathbb Z\), and define the backward cyclic shift \(S e_j=e_{j-1}\). With \(\theta_*=\pi/n\), put
\[
H_\theta=e^{i\theta}S+e^{-i\theta}S^*,\qquad
U_\theta(t)=e^{-itH_\theta},\qquad
C_{T,\theta}(u,v)=\frac1T\int_0^T |U_\theta(t)_{uv}|^2\,dt.
\]
Let \(P\) be the antipodal permutation, \(P e_j=e_{j+n/2}\), and let \(J\) denote the all-one matrix. The exactly half-flux long-time average is
\[
\lim_{T\to\infty}C_{T,\theta_*}=\frac{J+I-P}{n}.
\]
For every \(0<|\delta|\le\pi/(2n)\), the detuned average is uniform:
\[
\lim_{T\to\infty}C_{T,\theta_*+\delta}=\frac Jn.
\]
Define the entrywise-accuracy hitting time, with no monotonicity presupposed, by
\[
\tau_n(\delta)=\inf\left\{T>0:\max_{u,v}\left|C_{T,\theta_*+\delta}(u,v)-\frac1n\right|\le\frac1{2n}\right\}.
\]
Then
\[
\boxed{\frac{\sqrt{3/(8n)}}{|\delta|}\le\tau_n(\delta)
\le\frac{\pi(n-1)}{2\sin(\pi/n)|\delta|}.}
\]
In particular, for each fixed even \(n\), the finite-time approach to uniform average mixing has the **sharp exponent** \(\tau_n(\delta)=\Theta_n(|\delta|^{-1})\) as the magnetic flux approaches its half-flux value.

The crossover is explicitly resolved at antipodal vertices. Write \(\operatorname{sinc}(x)=\sin(x)/x\) for nonzero \(x\) and \(\operatorname{sinc}(0)=1\). For every \(s>0\) and every vertex \(u\), the limit from either sign of detuning is
\[
\boxed{\lim_{\delta\to0^\pm}
C_{s/|\delta|,\theta_*+\delta}(u,u+n/2)
=\frac1n-\frac2{n^2}\sum_{k=0}^{n/2-1}
\operatorname{sinc}\!\left(4s\sin\frac{(2k+1)\pi}{n}\right).}
\]
The right side tends to zero as \(s\downarrow0\) and to \(1/n\) as \(s\to\infty\). The half-flux and infinite-time limits therefore do not commute.

## Assumptions and scope

The graph is a nearest-neighbor cycle with an even number \(n\ge4\) of vertices. Both directions around each edge have hopping magnitude one and conjugate magnetic phases, so \(H_\theta\) is Hermitian. The observation-time distribution is **uniform on \([0,T]\)** and is not an arbitrarily optimized random-time law. The phase is expressed per oriented edge; total magnetic flux is \(n\theta\) modulo \(2\pi\). All statements involve fixed finite \(n\), nonnegative evolution time, and the indicated range of detunings. The crossover takes the detuning limit at a fixed positive scaled time \(s\).

## Proof

**1. Spectral decomposition and finite-time average.** The Fourier eigenvectors \(f_k(j)=n^{-1/2}e^{2\pi i kj/n}\), with indices \(k=0,\ldots,n-1\), diagonalize \(S\), hence \(H_\theta\), with eigenvalues
\[
\lambda_k(\theta)=2\cos\left(\theta+\frac{2\pi k}{n}\right).
\]
For any displacement \(d\in\mathbb Z/n\mathbb Z\), direct integration of the squared Fourier sum gives
\[
C_{T,\theta}(u,u+d)=\frac1{n^2}\sum_{k,l=0}^{n-1}
 e^{2\pi i(k-l)d/n}\,F_T\!\left(\lambda_k(\theta)-\lambda_l(\theta)\right),
\]
where
\[
F_T(\omega)=\frac1T\int_0^T e^{-it\omega}\,dt
=e^{-i\omega T/2}\operatorname{sinc}(\omega T/2).
\]
Thus \(F_T(0)=1\) and \(|F_T(\omega)|\le\min\{1,2/(T|\omega|)\}\) for \(\omega\ne0\).

**2. Half-flux resonance.** At \(\theta_*\), the only repeated eigenvalues are the pairs \((k,n-1-k)\); every such pair has two distinct indices because \(n\) is even. At infinite time only equal-eigenvalue terms remain. The off-diagonal character contribution is therefore
\[
\frac2{n^2}\sum_{k=0}^{n/2-1}\cos\left(\frac{2\pi(2k+1)d}{n}\right).
\]
This sum is \(n/2\) when \(d=0\), is \(-n/2\) when \(d=n/2\), and vanishes for all other displacements. Hence the stationary matrix is \((J+I-P)/n\). More strongly, the two members of every pair have opposite Fourier coefficients at displacement \(n/2\), so their amplitudes cancel for every time \(t\): \(U_{\theta_*}(t)_{u,u+n/2}=0\).

**3. Exact splitting and gap bound.** The cosine difference identity gives, for distinct indices,
\[
|\lambda_k(\theta_*+\delta)-\lambda_l(\theta_*+\delta)|
=4\left|\sin\left(\frac{\pi(k+l+1)}n+\delta\right)\right|
  \left|\sin\left(\frac{\pi(k-l)}n\right)\right|.
\]
If \(k+l+1\) is divisible by \(n\), the first sine has absolute value \(|\sin\delta|\). Otherwise, for \(|\delta|\le\pi/(2n)\) it is at least \(\sin(\pi/(2n))\ge|\sin\delta|\). The second sine is at least \(\sin(\pi/n)\). Consequently, for every nonzero permitted detuning, all eigenvalues are simple and
\[
\Delta_{\min}\ge4\sin(\pi/n)|\sin\delta|
\ge\frac8\pi\sin(\pi/n)|\delta|.
\]
There are \(n(n-1)\) ordered unequal-index terms in the finite-time Fourier sum. The diagonal terms add up to \(1/n\), and bounding every other term yields the **all-entry estimate**
\[
\max_{u,v}\left|C_{T,\theta_*+\delta}(u,v)-\frac1n\right|
\le\frac{\pi(n-1)}{4n\sin(\pi/n)T|\delta|}.
\]
This proves both the uniform infinite-time limit and the asserted upper bound for \(\tau_n(\delta)\).

**4. Matching order from destructive interference.** Since \(S\) and \(S^*\) have norm one,
\[
\|H_{\theta_*+\delta}-H_{\theta_*}\|
\le2|e^{i\delta}-1|\le2|\delta|.
\]
Duhamel's identity therefore bounds the difference of the unitary propagators by \(2|\delta|t\) in operator norm. The antipodal amplitude at exactly half-flux vanishes; hence
\[
C_{T,\theta_*+\delta}(u,u+n/2)
\le\frac1T\int_0^T 4\delta^2t^2\,dt
=\frac43\delta^2T^2.
\]
Attaining an all-entry deviation at most \(1/(2n)\) requires this antipodal average to be at least \(1/(2n)\). Rearrangement gives \(T\ge\sqrt{3/(8n)}\,|\delta|^{-1}\), proving the lower bound.

**5. Critical-window profile.** Fix \(s>0\) and let \(T=s/|\delta|\). In the exact finite-time Fourier sum, every nonpaired off-diagonal frequency remains bounded away from zero as \(\delta\to0\), and its contribution goes to zero. For \(k=0,\ldots,n/2-1\) and \(l=n-1-k\), put \(\alpha_k=(2k+1)\pi/n\). Their exact splitting is
\[
\lambda_k(\theta_*+\delta)-\lambda_l(\theta_*+\delta)
=-4\sin\alpha_k\sin\delta.
\]
At antipodal displacement, the character factor \(e^{2\pi i(k-l)(n/2)/n}\) is \(-1\). The two ordered terms of the pair add to
\[
-\frac2{n^2}\operatorname{Re}F_T(-4\sin\alpha_k\sin\delta)
=-\frac2{n^2}\operatorname{sinc}(4T\sin\alpha_k\sin\delta),
\]
using the identity \(\cos z\operatorname{sinc}z=\operatorname{sinc}(2z)\). As \(\delta\to0^\pm\), the last sinc tends to \(\operatorname{sinc}(4s\sin\alpha_k)\). This gives the stated finite sum. Its endpoints follow because there are \(n/2\) summands and all \(\sin\alpha_k\) are positive. All limiting steps involve only finitely many terms at fixed \(n\).

## Verification

Running `python3 verify.py` uses only the Python standard library. It checks 24 direct instantaneous antipodal cancellations, 88 resonant stationary displacement entries, 3,144 spectral-gap comparisons, 24 independent time-quadrature tests of the exact Fourier integral, and 24 near-critical scaling comparisons on even cycles from four to eighteen vertices. It reports `VERIFY_OK` with quadrature residual under \(3\cdot10^{-8}\) and critical-window residual under \(2.3\cdot10^{-5}\). Finite tests corroborate, but do not replace, the unrestricted analytical argument.

## Relationship to prior work

Coutinho, Baptista, Godsil, Spier and Werner provide the established spectral-projector approach to average quantum mixing; the present Hermitian magnetic Hamiltonians are outside their integral-adjacency setup. Adamczak and collaborators prove nonuniform average mixing for standard real-symmetric cycles, not flux-threaded chiral cycles. Carlson and collaborators study mixing under nonnegative **real** edge weights rather than complex magnetic phases. Levine and collaborators prove that every simple-spectrum Hermitian cyclic circulant has a uniform **infinite-time** average; that theorem already accounts for the qualitative detuned limit here and is not claimed as new. It does not give the half-flux finite-time bottleneck, explicit inverse-detuning bounds, or sinc crossover. The contribution assessed here is the combined sharp critical finite-time law and exact antipodal scaling profile, not the Fourier diagonalization or the general simple-spectrum result.

## Limitations

The constants in the mixing-time inequalities are explicit but are not asserted to be optimal. Only the divergence exponent is sharp for each fixed even size; no uniform-in-size sharp mixing asymptotics are claimed. The closed crossover concerns antipodal entries, not an independently optimized sampling law. The theorem does not apply to cycles of odd order, generic inhomogeneous hoppings, dissipative evolution, decoherence, or a time-periodic magnetic field. Additional literature may express the same crossover through general nearly degenerate spectral perturbation theory; independent examination remains warranted.

## References

1. G. Coutinho, P. Ferreira Baptista, C. Godsil, T. Jung Spier and R. Werner, *Irrational quantum walks*, arXiv:2208.08971v1 (first publicly posted 18 August 2022). https://arxiv.org/abs/2208.08971
2. L. Levine, J. J. Mesapam, B. Mustico, C. Tamon, G. Tucker and H. Zhan, *Uniform Mixing in Chiral Quantum Walks*, arXiv:2605.04414v2, Section 5 (2026). https://arxiv.org/html/2605.04414v2
3. W. Adamczak et al., *Non-uniform mixing of quantum walk on cycles*, arXiv:0708.2096v1 (2007). https://arxiv.org/abs/0708.2096
4. W. Carlson et al., *Universal Mixing of Quantum Walk on Graphs*, arXiv:quant-ph/0608044v1 (2006). https://arxiv.org/abs/quant-ph/0608044
