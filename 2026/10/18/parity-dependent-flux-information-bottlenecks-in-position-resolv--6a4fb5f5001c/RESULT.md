# Parity-dependent flux-information bottlenecks in position-resolved quantum ring walks

## Finding

**Theorem (global parity law for position-readout flux information).** Fix an integer \(n\ge3\), coherent hopping \(J>0\), and a magnetic flux \(\phi\in\mathbb R\). On the sites \(\mathbb Z/n\mathbb Z\), let \(S|j\rangle=|j+1\rangle\) and
\[
H_\phi=J\bigl(e^{i\phi/n}S+e^{-i\phi/n}S^\dagger\bigr),\qquad
|\psi_\phi(t)\rangle=e^{-itH_\phi}|0\rangle.
\]
Let \(p_j(\phi,t)=|\langle j|\psi_\phi(t)\rangle|^2\), and let the ordinary single-shot *position* Fisher information, wherever the support is regular, be
\[
\mathcal I_n(\phi,t)=\sum_{j:p_j(\phi,t)>0}
\frac{(\partial_\phi p_j(\phi,t))^2}{p_j(\phi,t)}.
\]
At points where some probabilities vanish, this definition is the pointwise ordinary score information, not the potentially different limiting Hellinger information.

For every \(t\ge0\), all position scores vanish simultaneously at
\[
\begin{cases}
\phi\in\pi\mathbb Z,&n\text{ even},\\
\phi\in\pi/2+\pi\mathbb Z,&n\text{ odd}.
\end{cases}
\]
Conversely, no other flux is position-score blind for *all* positive observation times. Indeed, for each fixed flux outside the corresponding exceptional set, the following sharp small-time laws hold (\(t\downarrow0\)):
\[
\boxed{\displaystyle
\mathcal I_{2r}(\phi,t)
=\frac{4\sin^2(\phi/2)}{(r!)^2}(Jt)^{2r}+O((Jt)^{2r+2}),
\qquad r\ge2,\quad\phi\notin\pi\mathbb Z;}\tag{E}
\]
\[
\boxed{\displaystyle
\mathcal I_{2r+1}(\phi,t)
=\frac{8\cos^2\phi}{((r+1)!)^2}(Jt)^{2r+2}+O((Jt)^{2r+4}),
\qquad r\ge1,\quad\phi\notin\pi/2+\pi\mathbb Z.}\tag{O}
\]
The leading information in (E) comes solely from the antipodal vertex \(r\); in (O) it comes from the two farthest vertices \(r\) and \(r+1\). These expansions are for each fixed nonexceptional flux; uniformity at an exceptional flux is **not** asserted.

For comparison, in the *fixed, uniformly distributed Peierls-phase encoding specified above*, the pure-state quantum Fisher information is exactly
\[
\boxed{\mathcal F_{Q,n}(\phi,t)=\frac{8J^2t^2}{n^2}}\qquad(n\ge3,\ t\ge0).
\]
Thus position measurement loses a factor of order \((Jt)^{n-2}\) on even cycles and \((Jt)^{n-1}\) on odd cycles at generic fixed flux. Unlike the classical information, the quantum information is sensitive to a parameter-dependent change of local phase reference (gauge); it is claimed only for the explicitly fixed Hamiltonian encoding, not as a gauge-independent sensing resource.

## Assumptions and scope

The system is a *simple* \(n\)-cycle with \(n\ge3\), uniform nearest-neighbor hopping, no onsite potential, noiseless unitary evolution, initial state \(|0\rangle\), and an ideal resolving measurement of all vertices at one known time \(t\). The flux \(\phi\) is the total oriented phase around the ring; each bond carries \(\phi/n\). The parameter derivative is taken at fixed site basis. The physical site probabilities are gauge invariant, although the state QFI is not invariant under an arbitrary \(\phi\)-dependent change of Hilbert-space identification. We use \(\hbar=1\).

At exceptional values, probabilities may be exactly zero: for example, the antipodal probability on an even ring vanishes at \(\phi=\pi\) for every time. The ordinary score definition above correctly states that all first derivatives vanish there. It does **not** say that nearby fluxes have identical distributions or preclude singular, second-order inference. Observation-time zeros can create similar nonregular score behavior at isolated times.

## Proof

**1. Exact winding expansion and its parity structure.** The commuting shifts diagonalize the evolution. The generating identity
\[
\exp[-iJt(z+z^{-1})]=\sum_{q\in\mathbb Z}(-i)^qJ_q(2Jt)z^q
\]
(with the ordinary integer-order Bessel functions \(J_q\)) yields the absolutely convergent formula
\[
\psi_j(\phi,t):=\langle j|\psi_\phi(t)\rangle
=\sum_{q\equiv j\ (\mathrm{mod}\ n)}(-i)^qJ_q(2Jt)e^{iq\phi/n}.\tag{1}
\]
Since \(J_q(2Jt)\) is real for real \(t\) and \(J_{-q}(z)=(-1)^qJ_q(z)\), (1) is valid for both winding directions. Writing \(q=j+mn\), its squared modulus is a uniformly convergent Fourier series in \(\phi\), and its coefficient at winding-frequency \(\ell=m-m'\) has relative phase \((-i)^{n\ell}\) times a real factor. For even \(n\), all such phases are real: each \(p_j\) is an even Fourier cosine series in \(\phi\). For odd \(n\), odd winding-frequency coefficients are purely imaginary and even winding-frequency coefficients are real. Accordingly, \(p_j\) consists only of \(\sin((2k+1)\phi)\) and \(\cos(2k\phi)\), plus a constant. Uniform convergence of all flux derivatives at fixed \(t\) follows from factorial Bessel tails. Consequently,
\[
\partial_\phi p_j(\phi,t)=0
\quad\text{at }\quad
\phi\in\pi\mathbb Z\ (n\text{ even}),\qquad
\phi\in\pi/2+\pi\mathbb Z\ (n\text{ odd}),\tag{2}
\]
for every vertex and every time. This proves the exact parity-dependent first-order blindness, including the zero-probability cases.

**2. Short-time paired paths.** Put \(x=Jt\). The Bessel expansion \(J_m(2x)=x^m/m!+O(x^{m+2})\) for each fixed nonnegative integer \(m\) shows that the first flux dependence in a site probability is caused by interference of the shortest clockwise and counterclockwise routes, whose lengths sum to \(n\). For any non-antipodal vertex at distance \(d<n/2\), its leading probability is of order \(x^{2d}\), while \(\partial_\phi p_j=O(x^n)\). Thus its information is \(O(x^{2n-2d})\). At the starting vertex the leading probability is one and the derivative is at most \(O(x^n)\), giving \(O(x^{2n})\); the potentially stronger parity cancellation is not required. These estimates are valid for each fixed flux as \(x\downarrow0\), with the leading shortest-path coefficient nonzero.

**3. Even rings.** If \(n=2r\), the unique antipode \(j=r\) has *two* length-\(r\) paths, of opposite winding. From (1),
\[
\psi_r(\phi,t)=\frac{2(-i)^r x^r}{r!}\cos(\phi/2)+O(x^{r+2}),
\]
\[
p_r(\phi,t)=\frac{2x^{2r}}{(r!)^2}(1+\cos\phi)+O(x^{2r+2}),\quad
\partial_\phi p_r(\phi,t)=-\frac{2x^{2r}}{(r!)^2}\sin\phi+O(x^{2r+2}).\tag{3}
\]
For \(\phi\notin\pi\mathbb Z\), \(1+\cos\phi\ne0\) and the ratio in the definition of information gives
\[
\frac{(\partial_\phi p_r)^2}{p_r}
=\frac{4x^{2r}}{(r!)^2}\sin^2(\phi/2)+O(x^{2r+2}).\tag{4}
\]
Every other vertex has distance at most \(r-1\), so its contribution is \(O(x^{2r+2})\) or smaller, proving (E). The coefficient is strictly positive at every flux except \(\phi\in2\pi\mathbb Z\); \(\phi\in(2\mathbb Z+1)\pi\) is instead covered by the exact blindness result (2), with nonregular vanishing antipodal support. Hence the listed fluxes are *exactly* the all-time blind points for even rings.

**4. Odd rings.** For \(n=2r+1\), the farthest sites are \(j=r\) and \(j=r+1\), with shortest route length \(r\) and the opposite route length \(r+1\). The two-path expansions are
\[
\begin{aligned}
p_r(\phi,t)&=\frac{x^{2r}}{(r!)^2}-\frac{2x^{2r+1}}{r!(r+1)!}\sin\phi+O(x^{2r+2}),\\
p_{r+1}(\phi,t)&=\frac{x^{2r}}{(r!)^2}+\frac{2x^{2r+1}}{r!(r+1)!}\sin\phi+O(x^{2r+2}).
\end{aligned}\tag{5}
\]
Differentiating the convergent winding series gives opposite leading scores of magnitude \(2x^{2r+1}|\cos\phi|/[r!(r+1)!]\). Each farthest vertex therefore contributes
\[
\frac{(\partial_\phi p_j)^2}{p_j}
=\frac{4x^{2r+2}\cos^2\phi}{((r+1)!)^2}+O(x^{2r+3}),\tag{6}
\]
where the \(O(x^{2r+3})\) term cancels in the *sum* over the reflected vertex pair, since \(p_r(\phi,t)=p_{r+1}(-\phi,t)\). More explicitly, the same even-in-\(x\) factor multiplies the leading route and the coefficient of the interference is an odd-power series in \(x\); writing \(p_\pm=A(x)\pm B(x,\phi)\), one has \(A(x)=a x^{2r}[1+O(x^2)]\) and \(B(x,\phi)=b x^{2r+1}\sin\phi+O(x^{2r+3})\). The sum \((B')^2[(A+B)^{-1}+(A-B)^{-1}]=2A(B')^2/(A^2-B^2)\) has relative error \(O(x^2)\). The remaining vertices contribute \(O(x^{2r+4})\) or smaller. Summing the pair proves (O). Its coefficient is nonzero exactly when \(\cos\phi\ne0\); (2) accounts for the excluded values. This proves the claimed *complete* first-order blind-flux classification.

**5. Exact quantum Fisher information in the specified phase encoding.** As \(H_\phi\) and \(\partial_\phi H_\phi\) are polynomials in the commuting unitaries \(S,S^\dagger\), the local encoding generator equals \(t\partial_\phi H_\phi\). For \(n\ge3\), \(\langle0|S|0\rangle=\langle0|S^2|0\rangle=0\). Direct expansion yields
\[
\langle0|\partial_\phi H_\phi|0\rangle=0,\qquad
\langle0|(\partial_\phi H_\phi)^2|0\rangle=\frac{2J^2}{n^2}.
\]
Using the exact pure-state formula \(\mathcal F_Q=4(\langle\partial_\phi\psi|\partial_\phi\psi\rangle-|\langle\psi|\partial_\phi\psi\rangle|^2)\) proves the announced \(8J^2t^2/n^2\). Ratios with (E) and (O) give the stated loss exponents at fixed generic flux. This finishes the proof.

## Verification

Run `python verify.py` after installing `requirements.txt`; the standalone program builds the cycle Hamiltonians, computes matrix exponentials, uses independent Hermitian diagonalization, checks score derivatives against finite differences, and compares the exact Fisher information with the derived short-time constants and exact blind-point symmetries. Its observed output is:

`VERIFY_OK 784 finite probability, Fisher, symmetry and leading-coefficient checks`

The verifier uses finite rings \(3\le n\le11\) and selected flux/time values; the proof above, not the finite experiments, covers all \(n\), \(\phi\), and \(t\) claimed. Every tested density is normalized; the QFI is computed from state derivatives, not by substituting the theorem's value.

## Relationship to prior work

Zanoli, Ragazzi, Bordone, and Paris (2026) analyze a magnetic-phase perturbation on a continuous-time ring and compute quantum metrological performance for *ground-state* or *unperturbed-ground-state initialized* schemes. For those states the purely magnetic encoding is a global phase, so their zero-QFI assertion is correct in its stated scope. The present preparation \(|0\rangle\), a coherent superposition of every Fourier eigenmode, is different; no site-resolved flux-score parity classification or the two sharp short-time laws follows from their ground-state results alone.

Luppi (arXiv:2608.12519v1, first submitted 12 August 2026) gives exact return-amplitude and sequential Lüders-measurement/Leggett–Garg formulas for chiral walks, including cycle winding sectors and a parity-sensitive *return* observable. Return probabilities are not the complete position distribution; the farthest-site Fisher coefficients in (E) and (O), their distinct exponents, and the complete regular score-blindness classification are different statements. The paper explicitly raises flux metrology from localized preparations as a future direction. The original full manuscript could not be directly inspected in this review, so implicit prior coverage is a documented residual risk rather than ruled out.

Amorim, Cerutti, de Sá Neto, and de Oliveira (2026) compare classical and quantum Fisher information for a *discrete-time coined* walk with absorbing boundary while estimating the input coin state. Their measurement, encoded parameter and graph are different. Earlier continuous-time graph metrology by Seveso, Benedetti, and Paris addresses estimation of a *tunneling amplitude* and related local measurements, not the present magnetic-flux parity classification.

## Limitations

The comparison with quantum Fisher information presupposes a specified parameter-independent reference for the site kets and the *uniform* Peierls-phase assignment. Parameter-dependent diagonal gauge changes do not preserve that state QFI, whereas the resolved site probabilities and their classical Fisher information are gauge invariant. At zero-probability, flux-symmetric points, ordinary score Fisher information is nonregular: its point value zero may differ from limits approached from nearby fluxes. The statements do not establish the optimal practical POVM, multiparameter robustness, any noisy/dephased sensing law, or uniform-in-flux error bounds near special points. The original full text of Luppi's closely relevant preprint was not accessible; possible implicit priority coverage requires independent literature review.

## References

1. L. Zanoli, G. Ragazzi, P. Bordone, M. G. A. Paris, “Quantum walks on a ring as a versatile single-parameter sensor,” *Frontiers in Quantum Science and Technology* **5** (2026), article 1894991. DOI: 10.3389/frqst.2026.1894991 (first verifiable public article: 2026-08-04).
2. P. Luppi, “Flux control of measurement back-action and Leggett–Garg correlations in chiral quantum walks,” arXiv:2608.12519v1 (first submitted 2026-08-12).
3. E. P. M. Amorim, L. R. Cerutti, O. P. de Sá Neto, M. C. de Oliveira, “Absorption-based qubit estimation in discrete-time quantum walks,” *APS Open Science* **1** (2026), 000015. DOI: 10.1103/zns5-vzyy.
4. L. Seveso, C. Benedetti, M. G. A. Paris, “The walker speaks its graph: global and nearly-local probing of the tunnelling amplitude in continuous-time quantum walks,” *J. Phys. A* **52** (2019), 105304; arXiv:1809.09211.
