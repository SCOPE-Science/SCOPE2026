# Sharp fixed-mean renewal probing frontier for a two-state quantum detector

## Finding

For a coherent two-state system repeatedly tested for a transition by independent ideal projective measurements, **the exact minimum mean detection time under a prescribed mean time between measurements has three regimes**. Write the Hamiltonian (in units with \(\hbar=1\)) as
\[
H=E I+\begin{pmatrix}\delta&g\\\overline g&-\delta\end{pmatrix},\qquad
\Omega=\sqrt{\delta^2+|g|^2},\qquad \beta=\frac{|g|^2}{\Omega^2},
\]
with real \(E,\delta\), complex \(g\ne0\). Prepare the state \(|0\rangle\), test repeatedly for \(|1\rangle\), and require the i.i.d. nonnegative inter-test times \(\tau\) to have a prescribed finite mean \(m>0\). Put \(z=\Omega m\). Let \(x_*\in(\pi/4,\pi/2)\) be the unique positive solution of \(\tan x_*=2x_*\) (numerically \(x_*=1.1655611852072113\ldots\)), and write \(k=\sin^2(x_*)/x_*\). Then the infimum over **all** such waiting-time laws is
\[
\boxed{\inf_{\mathbb E\tau=m}\mathbb E T=\frac{m}{\beta F(z)},\qquad
F(z)=\begin{cases}
kz,&0<z\le x_*,\\
\sin^2z,&x_*\le z\le\pi/2,\\
1,&z\ge\pi/2.
\end{cases}}
\]
Here \(T\) is the elapsed physical time to the first successful detection, not the attempt count. The optimal inter-test laws are completely classified. For \(0<z<x_*\), place probabilities \(1-z/x_*\) and \(z/x_*\) at \(\tau=0\) and \(\tau=x_*/\Omega\). For \(x_*\le z\le\pi/2\), take \(\tau=m\) deterministically; this optimizer is unique. For \(z>\pi/2\), take **any** law supported on the Rabi-success maxima \(\tau=(\pi/2+j\pi)/\Omega\), \(j=0,1,\ldots\), with mean \(m\). These are all attaining laws, with the evident agreements at the two boundaries.

If strictly positive waiting times are required, the infimum in the first regime is not attained, but can be approached by two-point laws with the smaller time tending to zero; all other stated optimal laws remain admissible. Thus the constrained optimizer changes from a two-atom short/finite mixture, through a unique deterministic interval, to mixtures of resonant intervals. In particular, at a prescribed mean \(m=\pi/\Omega\), deterministic interrogation never detects, but equal mixing of the intervals \(\pi/(2\Omega)\) and \(3\pi/(2\Omega)\) gives finite mean detection time \(\pi/(\beta\Omega)\).

## Assumptions and scope

The Hilbert space is exactly two-dimensional and the system evolves unitarily between measurements under the time-independent Hermitian \(H\) above. The first measurement occurs after the first sampled interval, and each unsuccessful outcome projects onto the one-dimensional complement of the detected state. Thus every unsuccessful outcome restores \(|0\rangle\), up to a phase. The waiting times are independent of the quantum dynamics and measurement outcomes, identically distributed on \([0,\infty)\), and have \(0<m=\mathbb E\tau<\infty\). The result treats the first-passage (transition) experiment, not the return-to-initial-state experiment. There is no externally imposed reset, decoherence, observation-time overhead, or constraint on waiting-time variance. A distribution with vanishing single-trial success probability is assigned \(\mathbb E T=\infty\).

## Proof

**1. Exact renewal reduction.** Decompose \(H-EI\) into Pauli matrices. The unitary satisfies
\[
e^{-iHt}=e^{-iEt}\left[\cos(\Omega t)I-\frac{i\sin(\Omega t)}{\Omega}(H-EI)\right],
\]
so one test after duration \(t\) succeeds with probability \(q(t)=\beta\sin^2(\Omega t)\). The unsuccessful projector is \(|0\rangle\langle0|\), hence the post-failure normalized state is again \(|0\rangle\) up to phase. If \(s=\mathbb E q(\tau)>0\), attempts are independent and have unconditional success probability \(s\). For the geometric success index \(K\), the event \(\{K\ge i\}\) depends only on earlier intervals and measurements and is independent of \(\tau_i\). By Tonelli's theorem,
\[
\mathbb E T=\sum_{i\ge1}\mathbb E[\tau_i\mathbf1_{\{K\ge i\}}]
=m\sum_{i\ge1}(1-s)^{i-1}=\frac{m}{s}.
\]
If \(s=0\), successful detection is impossible, so \(\mathbb E T=\infty\). Consequently minimizing \(\mathbb E T\) at fixed \(m\) is equivalent to maximizing \(\mathbb E\sin^2X\) over laws of \(X=\Omega\tau\ge0\) with \(\mathbb E X=z\).

**2. Tangent point and global supporting slope.** Put \(f(x)=\sin^2x\). On \((0,\pi/2)\), the sign of \(\frac{d}{dx}[f(x)/x]\) equals the sign of \(2x\cos x-\sin x\); the equation for an interior stationary point is \(\tan x=2x\). The derivative of \(\tan x-2x\) is \(\sec^2x-2\), which is negative on \((0,\pi/4)\) and positive on \((\pi/4,\pi/2)\). As \(\tan x-2x<0\) just above zero and tends to \(+\infty\) at \(\pi/2\), exactly one positive root \(x_*\) exists, in \((\pi/4,\pi/2)\). The quotient \(f(x)/x\) increases up to \(x_*\) and decreases to \(\pi/2\). For \(x\ge\pi/2\), \(f(x)/x\le1/x\le2/\pi<k\) (the last inequality follows from the strict interior maximum over \((0,\pi/2)\)). Thus \(f(x)\le kx\) for all \(x\ge0\), with equality there only at \(x=0,x_*\). At \(x_*\), tangency gives \(f'(x_*)=k\).

**3. A global concave majorant.** Define the displayed piecewise \(F\) also at zero by \(F(0)=0\). It majorizes \(f\) on \([0,\infty)\): on \([0,x_*]\) by step 2; on \([x_*,\pi/2]\) by equality; after \(\pi/2\) by \(f\le1\). The left and right derivatives agree at both joints: \(f'(x_*)=k\) and \(f'(\pi/2)=0\). On the middle interval, \(f''(x)=2\cos(2x)<0\) because \(x_*>\pi/4\); the other pieces are linear and constant. Hence \(F\) is concave globally. Jensen's inequality for the integrable \(X\) yields
\[
\mathbb E\sin^2X=\mathbb Ef(X)\le\mathbb EF(X)\le F(\mathbb EX)=F(z).
\]

**4. Sharpness and equality cases.** For \(0<z<x_*\), the two-point law on \(\{0,x_*\}\) with mean \(z\) achieves \(\mathbb Ef=kz\). Equality in the two bounds forces support on the contact points \(0,x_*\), giving the specified unique weights. For \(x_*\le z\le\pi/2\), deterministic \(X=z\) achieves \(f(z)=F(z)\), while strict concavity of the relevant curved segment and the contact-point set force any maximizer to be this deterministic law. For \(z>\pi/2\), any distribution supported on \(\{\pi/2+j\pi:j\in\mathbb Z_{\ge0}\}\) and having mean \(z\) achieves \(\mathbb Ef=1\). Such a law exists by mixing the two consecutive maxima bracketing \(z\). Conversely, equality with \(F(z)=1\) requires \(f(X)=1\) almost surely, so precisely those laws are optimal. For \(0<z<x_*\), excluding \(X=0\) excludes attainment because the contact set below \(x_*\) contains no other positive point; replacing its zero atom by a small positive time and adjusting both weights achieves a sequence converging to the stated infimum.

Combining steps 1–4 establishes the exact frontier and all equality conditions. The small-budget limit is \(\lim_{m\downarrow0}\inf\mathbb ET=1/(\beta\Omega k)\), finite, whereas strictly periodic probing with interval \(m\) gives \(m/[\beta\sin^2(\Omega m)]\sim1/(\beta\Omega^2m)\). This finite limiting optimum relies on permitting arbitrarily uneven intervals when the prescribed mean approaches zero.

## Verification

The independent reproducibility script `artifacts/verify.py` requires Python 3 with NumPy, SciPy, and mpmath. Run it from a directory containing that relative file by `python artifacts/verify.py`. It checks transition probabilities directly by matrix exponentiation for nonzero detuning and complex couplings, high-precision tangency, explicit two-point laws in all regimes, sampled global majorization, finite-grid linear programming and 800 random finite-support waiting-time distributions. These computations corroborate, but do not replace, the fully analytic inequalities and equality characterization above.

## Relationship to prior work

Kulkarni and Majumdar, arXiv:2305.15123, §6.1, Eq. (135), derive the general renewal mean-detection expression for a two-level system, but do not determine the **maximum over waiting-time laws of each prescribed mean** or its phase boundaries. Kessler, Barkai and Ziegler, arXiv:2012.01763, prove a general i.i.d.-probing mean-time identity and study exponential/Gamma timing laws; the fixed-mean all-laws extremal problem remains distinct. Belan and Parfenyev, arXiv:1909.03226, prove that an unconstrained optimal periodic protocol is globally best among measurement protocols; their theorem is compatible with, but does not calculate, the sharp frontier at a mean interval fixed away from the unconstrained optimum. Del Vecchio Del Vecchio and Majumdar, arXiv:2509.08556, treat Poissonian probes on a complete graph and explicitly identify comparison of different protocols as future work.

A publicly available result entitled *Exact renewal-protocol optimum for first detection on the fully connected quantum model* (published-finding corpus identifier `1683e0413749`) proves the related unconstrained all-renewal optimum for a bright state using the same scalar sinusoidal efficiency ratio; **that already covers the low-mean constant-time value** and is credited here. It does **not** give the exact prescribed-mean frontier with a unique deterministic intermediate regime and an indefinitely extendable family of resonant high-mean optimizers. The present contribution is specifically this global fixed-budget classification and all equality cases, rather than the known unconstrained minimum or the known renewal identity. The fully connected special case is mathematically comparable to a two-level bright/dark reduction and therefore is not treated as unrelated merely because the underlying Hilbert-space dimension is larger.

## Limitations

The theorem requires a projectively renewed two-state transition and i.i.d. inter-test intervals with fixed mean, and assumes the ideal ability to use arbitrarily small intervals and arbitrary timing mixtures. Zero-length intervals are a mathematical relaxation; excluding them changes attainment, not the infimum, only in the short-mean regime. Measurement overhead, entropy or variance budgets, correlated/adaptive protocols, multi-level dynamics with nontrivial post-failure states, and noisy measurement are not covered. The concave-envelope method is standard mathematics; novelty is asserted only for the explicit, fully classified fixed-mean physical optimization, with publication priority remaining subject to further external verification.

## References

1. M. Kulkarni and S. N. Majumdar, “First detection probability in quantum resetting via random projective measurements,” arXiv:2305.15123 (first posted 2023-05-24), §6.1, Eq. (135). https://arxiv.org/abs/2305.15123
2. D. A. Kessler, E. Barkai, and K. Ziegler, “The first detection time of a quantum state under random probing,” arXiv:2012.01763 (2020). https://arxiv.org/abs/2012.01763
3. S. Belan and V. Parfenyev, “Optimal Measurement Protocols in Quantum Zeno Effect,” arXiv:1909.03226 (2019). https://arxiv.org/abs/1909.03226
4. G. Del Vecchio Del Vecchio and S. N. Majumdar, “Optimal detection of quantum states via projective measurements,” arXiv:2509.08556 (2025). https://arxiv.org/abs/2509.08556
5. “Exact renewal-protocol optimum for first detection on the fully connected quantum model,” published mathematical research record, identifier 1683e0413749 (2026).
