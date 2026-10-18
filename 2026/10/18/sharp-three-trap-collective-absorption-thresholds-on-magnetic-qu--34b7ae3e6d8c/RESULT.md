# Sharp three-trap collective absorption thresholds on magnetic quantum cycles

## Finding

A finite coherent cycle can retain a permanently surviving state against **each of three absorbing sites taken in pairs**, yet undergo **certain eventual absorption when all three are activated**. This cannot happen on any cycle smaller than \(60\) vertices at zero magnetic flux: the smallest example is \(C_{60}\), with sinks at \(\{0,3,5\}\). If every pair must be dark at **both zero and half-quantum flux**, the smallest example is \(C_{105}\), with sinks \(\{0,3,10\}\). At half-quantum flux alone, the phenomenon is possible precisely for odd cycle lengths with at least three distinct prime divisors. These sharp thresholds follow from an exact all-set spectral and localized-survival theorem.

For an arbitrary nonempty proper sink set \(T\subset\mathbb Z/N\mathbb Z\) on a cycle with \(N\ge3\), choose \(a\in T\) and set
\[
g=\gcd\bigl(N,\{t-a:t\in T\}\bigr),\qquad
h=\gcd\bigl(N,\{2(t-a):t\in T\}\bigr).
\]
The gcd is unchanged by representatives, and each sink has any strictly positive local loss rate. If \(d_\Phi\) denotes the dimension of the fully nondecaying subspace, then
\[
d_\Phi=\begin{cases}
\lfloor(h-1)/2\rfloor,&\Phi\equiv0\pmod{2\pi},\\
\lfloor g/2\rfloor,&\Phi\equiv\pi\pmod{2\pi}\ \text{and}\ N/g\text{ is odd},\\
0,&\text{otherwise}.
\end{cases}
\]
For a particle initially localized at \(x\), its exact ultimate no-absorption probability is \(s_\Phi(x)=\langle x|P_{\mathcal D}|x\rangle\). At zero flux,
\[
s_0(x)=\begin{cases}0,&h\mid 2(x-a),\\ h/(2N),&h\nmid 2(x-a).\end{cases}
\]
At half flux, \(s_\pi(x)=0\) when \(N/g\) is even. When \(N/g\) is odd,
\[
s_\pi(x)=\begin{cases}
0,&g\mid x-a,\\
g/N,&g\text{ even and }x-a\equiv g/2\pmod g,\\
g/(2N),&\text{otherwise}.
\end{cases}
\]
At all other fluxes, \(s_\Phi(x)=0\) for every \(x\). Thus all ultimate survival probabilities are independent of the positive strengths of the individual absorbers.

Let \(\omega_{\rm odd}(N)\) denote the number of distinct odd prime divisors of \(N\). There is a triple of distinct sinks for which each two-sink restriction has a nonzero dark space while the full three-sink set has none at zero flux **if and only if**
\[
\omega_{\rm odd}(N)+\mathbf 1_{4\mid N}\ge3.
\]
At half flux the same pairwise-versus-collective effect occurs **if and only if** \(N\) is odd and \(\omega_{\rm odd}(N)\ge3\). The latter criterion is also exactly the existence criterion for one triple exhibiting the effect at both flux values.

## Assumptions and scope

Work in the single-excitation Hilbert space \(\mathbb C^N\), \(N\ge3\), with periodic vertex labels and uniform nonzero real hopping \(J\). The magnetic Hamiltonian and lossy no-jump generator are
\[
H_\Phi=J\sum_{x\in\mathbb Z/N\mathbb Z}\bigl(e^{i\Phi/N}|x+1\rangle\langle x|+e^{-i\Phi/N}|x\rangle\langle x+1|\bigr),
\qquad K_\Phi=H_\Phi-\frac i2\sum_{a\in T}\kappa_a|a\rangle\langle a|,
\]
with every \(\kappa_a>0\) and an arbitrary nonempty proper \(T\). For a unit initial vector \(\psi\), the no-jump survival at time \(t\ge0\) is \(\|e^{-iK_\Phi t}\psi\|^2\). A *dark state* is an eigenvector of \(H_\Phi\) that vanishes at every sink. A *pairwise-dark, collectively-bright triple* is a set of three distinct sink sites for which every two-site restriction possesses a dark state but the full triple does not. This definition concerns existence of dark initial states, not positive survival from every initial vertex.

## Proof

**1. Exact lossless subspace.** Write \(\Gamma=\sum_{a\in T}\kappa_a|a\rangle\langle a|\). For \(\dot\psi=-iK_\Phi\psi\),
\[
\frac d{dt}\|\psi(t)\|^2=-\langle\psi(t),\Gamma\psi(t)\rangle\le0.
\]
The joint eigenspaces of \(H_\Phi\) lying in \(\ker\Gamma\) reduce both \(H_\Phi\) and \(K_\Phi\). On their orthogonal complement, any eigenvalue \(z\) of \(K_\Phi\) has \(\operatorname{Im}z<0\): equality in the dissipativity identity would force its eigenvector into \(\ker\Gamma\) and hence into a dark \(H_\Phi\)-eigenspace. Finite-dimensional Jordan theory therefore makes the complementary semigroup decay. Hence \(\lim_{t\to\infty}\|e^{-iK_\Phi t}\psi\|^2=\|P_{\mathcal D}\psi\|^2\) for **all** positive rates, with no weak-loss approximation.

**2. Magnetic degeneracies and divisibility.** Bloch eigenvectors have components \(N^{-1/2}e^{2\pi ikx/N}\), and eigenvalues \(2J\cos((2\pi k-\Phi)/N)\). A repeated eigenvalue is possible only when \(\Phi\equiv0\) or \(\pi\pmod{2\pi}\). An unpaired Bloch state never vanishes at a sink. At these two fluxes the paired momenta are negatives modulo \(2\pi\); the unique vector in each two-dimensional energy eigenspace vanishing at \(a\) is a normalized sine wave. Its other sink values vanish precisely when
\[
N\mid(2k-p)(t-a)\quad\text{for every }t\in T,
\qquad p=0\text{ or }1\ \text{according as }\Phi=0\text{ or }\pi.
\]
For \(p=0\), the admissible non-self-paired modes have frequencies \(2\pi j/h\), with \(1\le j\le\lfloor(h-1)/2\rfloor\). For \(p=1\), solutions exist only if \(N/g\) is odd, in which case they have frequencies \((2j+1)\pi/g\), with \(0\le j<\lfloor g/2\rfloor\). The counted modes are mutually orthogonal because their energies are distinct. This proves the dimension formula.

**3. Sitewise survival.** Each sine state has probability \((2/N)\sin^2(q(x-a))\) at vertex \(x\). Summing over the admissible zero-flux frequencies uses
\[
\sum_{j=1}^{\lfloor(h-1)/2\rfloor}\sin^2(2\pi jy/h)=\begin{cases}
0,&h\mid2y,\\ h/4,&h\nmid2y.
\end{cases}
\]
At half flux the corresponding odd-frequency sum is zero for \(y\equiv0\pmod g\), equals \(g/2\) for \(y\equiv g/2\pmod g\) when \(g\) is even, and equals \(g/4\) elsewhere. Multiplying by \(2/N\) gives both asserted survival profiles.

**4. Arithmetic classification of three-trap obstruction.** At zero flux, a pair at separation \(\delta\) is dark exactly when \(\gcd(N,2\delta)\ge3\). This means \(\delta\) is divisible by **at least one odd prime dividing \(N\)** or, when \(4\mid N\), \(\delta\) is even. For each such effective prime, equality of sites modulo that prime (modulo \(2\) for the exceptional even condition) defines an equivalence relation. If two of the three pairwise edges share the same qualifying congruence, transitivity forces **all three sinks** into that congruence class; hence the triple is dark. With fewer than three effective primes, three dark edges must repeat a congruence (pigeonhole), so no obstruction occurs.

Conversely, choose any three distinct effective primes. The Chinese remainder theorem permits site residues such that, for the three chosen moduli, precisely one different pair agrees at each modulus: respectively \(a=b\ne c\), \(a=c\ne b\), and \(b=c\ne a\). At every other effective prime choose residues not all equal. Then each pair is dark, but no effective prime divides **every** relative difference, so the triple is bright. This proves the exact zero-flux criterion. The smallest cycle with three effective primes is \(4\cdot3\cdot5=60\), giving \(T=\{0,3,5\}\): pairwise dark dimensions are \(2,4,1\), whereas the triple dimension is zero.

At half flux, a pair is dark precisely when \(g_\delta=\gcd(N,\delta)\ge2\) and \(N/g_\delta\) is odd. If \(N\) is even, every pair separation must be divisible by the full power of two in \(N\); therefore all three sinks share that congruence class and the triple has a dark space. If \(N\) is odd, the criterion becomes equality modulo some odd prime dividing \(N\), and the same three-edge congruence argument applies. The least odd number with three distinct prime factors is \(3\cdot5\cdot7=105\), giving \(T=\{0,3,10\}\). Each pair then has dark dimensions \(1,2,3\) at both fluxes, while the triple has dimension zero at both. No smaller cycle has the simultaneous effect.

## Verification

The accompanying independent NumPy program constructs the full Bloch Hamiltonian and determines the nullspace of the sink evaluation map in every numerically degenerate energy sector. It compares dark dimensions and every localized survival probability against the closed formulas. It passes \(9{,}852\) full-spectral configurations and \(128{,}670\) sitewise comparisons, with exhaustive sink subsets through \(N=10\), reproducible sampled subsets through \(N=28\), and flux values \(0\), \(\pi\), and \(0.31\). Additional independent diagonalizations verify every pair and triple in both sharp examples \(N=60\) and \(N=105\). The program also exhaustively checks that no smaller candidate exists for either individual flux cutoff. Analytical proofs, not finite experiments, establish the all-size and sharp-minimum statements. Run `python verification.py` with NumPy installed.

## Relationship to prior work

Agliari, Mülken and Blumen (2009, arXiv:0903.3288v1) develop the non-Hermitian absorbing quantum walk on a cycle and exhibit stationary zero-loss states for periodic trap placements. **Their Eq. (22) already gives the first-order zero-flux decay correction for an arbitrary set of sinks.** Neither that general expression nor its existing periodic cases is claimed as a new discovery. The specific contribution here is the exact flux-resolved all-set localized-survival profile and, especially, the arithmetic **if-and-only-if collective-trap obstruction** together with the sharp first possible sizes \(60\) and \(105\). A previously established two-sink magnetic-cycle calculation is a special case and is not claimed as new. Gönülol and collaborators (2010, arXiv:1008.0085) study a coined discrete-time walk with traps and do not establish the present continuous-time complex-hopping three-trap cutoff.

## Limitations

This is single-particle, continuous-time, finite-cycle coherent dynamics with strictly positive **onsite absorptive** rates and homogeneous hopping. Zero loss rates, coherent driving, dephasing, on-site disorder, long-range hopping, and stroboscopic projective detection are outside the theorem. The nondecaying component is an exact asymptotic projection; the proof does not give finite-time decay constants or robustness under perturbation of the flux. The strong related 2009 arbitrary-trap perturbation formula means that the zero-flux algebraic component should not be interpreted as wholly independent of earlier work; the remaining originality claim concerns the complete sharp collective obstruction and magnetic phase comparison. Searches cannot rule out differently indexed prior statements.

## References

1. E. Agliari, O. Mülken and A. Blumen, *Continuous-time quantum walks and trapping*, arXiv:0903.3288v1 (first publicly posted 19 March 2009), https://arxiv.org/html/0903.3288v1 . Particularly Sections III–VI and Eq. (22).
2. M. Gönülol, E. Aydiner, Ö. E. Müstecaplıoğlu and collaborators, *Survival probability in a one-dimensional quantum walk on a trapped lattice*, arXiv:1008.0085 (first publicly posted 31 July 2010), https://arxiv.org/html/1008.0085v3 .
