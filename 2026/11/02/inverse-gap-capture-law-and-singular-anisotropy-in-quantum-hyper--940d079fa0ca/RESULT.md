# Inverse-gap capture law and singular anisotropy in quantum hypercubes

## Finding

**Flat-spectral capture theorem.** Let \(N\ge2\) and let \(H\) be a Hermitian \(N\times N\) matrix with pairwise distinct real eigenvalues \(E_1,\ldots,E_N\) and normalized eigenvectors \(\phi_1,\ldots,\phi_N\). Suppose a normalized absorber state \(v\) has a flat spectral measure:
\[
|\langle\phi_j,v\rangle|^2=1/N\qquad(1\le j\le N).
\]
For every local population-loss rate \(\kappa>0\), let
\[
L=-\mathrm i H-\frac\kappa2|v\rangle\langle v|,\qquad
\rho(t)=e^{Lt}\frac{I}{N}e^{L^\dagger t}.
\]
Then absorption is complete, and the exact mean capture time, including the initial probability at the absorber, is
\[
\boxed{T(\kappa)=\int_0^\infty\operatorname{tr}\rho(t)\,dt
=\frac N\kappa+\frac{2\kappa}{N^2}\sum_{1\le j<k\le N}\frac1{(E_j-E_k)^2}.}
\]
Writing \(S=\sum_{j<k}(E_j-E_k)^{-2}>0\), the **unique** optimal positive loss rate and its sharp minimum are
\[
\boxed{\kappa_*=\sqrt{\frac{N^3}{2S}},\qquad
T_*=2\sqrt{\frac{2S}{N}}.}
\]
The formulas are independent of the phases of the overlaps and of any other details of the eigenvectors.

**Weighted-hypercube singularity.** Fix an integer \(d\ge2\), hopping scale \(J>0\), and \(0\le\varepsilon<(2^d-1)^{-1}\). On the binary cube \(\{0,1\}^d\), use the one-excitation adjacency Hamiltonian
\[
H_\varepsilon=J\sum_{i=0}^{d-1}(1+\varepsilon2^i)X_i,
\]
where \(X_i\) flips bit \(i\), and absorb at any one vertex at rate \(\kappa>0\). Set \(N=2^d\), \(a(U)=\sum_{i\in U}2^i\), and the positive rational number
\[
C_d=\sum_{m=0}^{d}\ \sum_{\substack{U,V\subseteq\{0,\ldots,d-1\}\\|U|=|V|=m,\ U<V}}
\frac{1}{(a(U)-a(V))^2},
\]
where \(U<V\) means each unordered distinct pair is taken once (in any fixed total order). For every \(0<\varepsilon<(2^d-1)^{-1}\), the eventual capture probability from the maximally mixed state is one. At \(\varepsilon=0\) it is exactly \((d+1)/2^d<1\). Moreover,
\[
\boxed{\lim_{\varepsilon\downarrow0}\varepsilon^2 T(\kappa,\varepsilon)
=\frac{\kappa C_d}{2N^2J^2},\quad
\lim_{\varepsilon\downarrow0}\frac{\kappa_*(\varepsilon)}{\varepsilon}
=J\sqrt{\frac{2N^3}{C_d}},\quad
\lim_{\varepsilon\downarrow0}\varepsilon T_*(\varepsilon)
=\frac1J\sqrt{\frac{2C_d}{N}}.}
\]
Thus any fixed positive absorber rate gives a sharp inverse-square divergence of the mean as the hopping anisotropy is removed, while globally tuning that rate improves the divergence to the sharp inverse-first-power law. For \(d=2\), \(C_2=1\); for \(d=3\), \(C_3=49/18\).

## Assumptions and scope

All spaces are finite-dimensional; \(\hbar=1\), and \(\kappa\) is the *population* decay rate (the non-Hermitian amplitude generator has \(-\kappa/2\)). No dephasing, spontaneous loss away from the absorber, or repeated projective measurements are present. The initial state is \(I/N\), which includes the absorber site; other initial ensembles need not satisfy the same formula. The flat-spectrum theorem requires both simple eigenvalues and all eigenvector overlaps having exactly squared magnitude \(1/N\). The hypercube result uses real positive hopping strengths, a site-local absorber, and the stated strict perturbation interval.

The survival integral is the unconditional mean of the absorption time because \(-\tfrac{d}{dt}\operatorname{tr}\rho(t)=\kappa\langle v,\rho(t)v\rangle\), the initial trace is one, and under the assumptions the limiting trace vanishes. At \(\varepsilon=0\) in the cube, a dark subspace remains; hence the unconditional mean is infinite, whereas the displayed finite-time formulas apply only to \(\varepsilon>0\).

## Proof

**1. Stable loss dynamics.** In the eigenbasis of \(H\), absorb overlap phases into the eigenvectors to take \(v=N^{-1/2}(1,\ldots,1)^T\) and \(H=\operatorname{diag}(E_1,\ldots,E_N)\). If \(Lx=\lambda x\) and \(\operatorname{Re}\lambda=0\), taking the real part of \(\langle x,Lx\rangle\) forces \(\langle v,x\rangle=0\). Then \(Hx\) is an eigenmultiple of \(x\); spectral simplicity says \(x\) is a coordinate eigenvector, whose overlap with \(v\) is nonzero, a contradiction. Since every eigenvalue of \(L\) has nonpositive real part, all have strictly negative real part. Therefore \(\rho(t)\to0\) and \(X=\int_0^\infty\rho(t)\,dt\) exists, is Hermitian, and satisfies
\[
\mathrm i[H,X]+\frac\kappa2(PX+XP)=\frac I N,
\qquad P=vv^\dagger.
\]

**2. Exact integrated density matrix.** Put \(u=Xv\), \(\Delta_{jk}=E_j-E_k\), and \(s_j=\sum_{\ell\ne j}\Delta_{j\ell}^{-1}\). From the diagonal entries of the Lyapunov equation, \(\operatorname{Re}u_j=1/(\kappa\sqrt N)\). The off-diagonal entries, followed by their imaginary parts and the identity \(u=Xv\), yield
\[
\operatorname{Im}u_j=\frac{s_j}{N\sqrt N},\qquad
X_{jk}=-\frac\kappa{2N^2}\frac{s_j-s_k}{\Delta_{jk}}
+\frac{\mathrm i}{N\Delta_{jk}}\quad(j\ne k).
\]
The diagonal entries then obey
\[
X_{jj}=\frac1\kappa+\frac\kappa{2N^2}\sum_{k\ne j}
\frac{s_j-s_k}{\Delta_{jk}}.
\]
Consequently
\[
\operatorname{tr}X=\frac N\kappa+\frac\kappa{N^2}
\sum_{j<k}\frac{s_j-s_k}{\Delta_{jk}}.
\]
For each unordered triple of distinct energy levels, the three terms
\[
\frac1{(E_i-E_\ell)(E_j-E_\ell)}+
\frac1{(E_i-E_j)(E_\ell-E_j)}+
\frac1{(E_j-E_i)(E_\ell-E_i)}
\]
sum to zero. Expanding each difference \((s_j-s_k)/\Delta_{jk}\) separates its direct contribution \(2/\Delta_{jk}^2\) from exactly those cancelling triple terms. Thus
\[
\sum_{j<k}\frac{s_j-s_k}{\Delta_{jk}}=2\sum_{j<k}\frac1{\Delta_{jk}^2},
\]
proving the mean-time identity. As \(S>0\), the sum \(N/\kappa+(2S/N^2)\kappa\) has the displayed unique minimizer and minimum.

**3. Binary-cube spectrum and the singular limits.** The commuting bit flips have Walsh eigenvectors whose coordinate moduli all equal \(N^{-1/2}\). Their distinct signed-sum energies at \(\varepsilon>0\) are indexed by subsets \(U\) and equal
\[
E_U(\varepsilon)=J\big[d-2|U|+\varepsilon(2^d-1-2a(U))\big].
\]
For subsets of equal cardinality, binary uniqueness makes \(a(U)\ne a(V)\), so the gap is \(2J\varepsilon|a(U)-a(V)|>0\). For subsets of differing cardinalities, the gap cannot vanish because \(\varepsilon(2^d-1)<1\). Therefore the flat-spectrum theorem applies for the entire strict interval.

At \(\varepsilon=0\), the eigenvalue depends only on \(|U|\), giving \(d+1\) distinct levels. Each such eigenspace has a one-dimensional component coupled to the absorber, and all orthogonal components are dark. Hence the accessible dimension is \(d+1\) and the uniform-mixture capture fraction is \((d+1)/N\). For positive \(\varepsilon\), all eigenvalues are simple and the absorber is cyclic, so the fraction is one.

Finally, split the exact spectral sum \(S(\varepsilon)\) into pairs with equal and unequal cardinality. Equal-cardinality gaps give exactly \(C_d/(4J^2\varepsilon^2)\); all remaining gaps tend to nonzero integers times \(2J\) and contribute \(O(1)\). Substitution into the exact mean and its optimizer gives all three limits. In particular \(C_d>0\) for \(d\ge2\). This is a proof for every fixed dimension, not an extrapolation from small cubes.

## Verification

The accompanying standard-library program `verify.py` uses exact rational arithmetic. It constructs the proposed integrated density matrix and substitutes it into both real and imaginary parts of the full Lyapunov equation for seven nondegenerate rational spectra of sizes \(3,4,5,6,4,8,16\). An independent rational Gaussian elimination of the complete Lyapunov linear system recovers the same trace in three cases. It checks spectral simplicity in weighted cubes of dimensions \(2,3,4\), the exact coefficients \(C_2=1\), \(C_3=49/18\), and \(C_4=2401501/396900\), and finite-perturbation lower bounds in dimensions \(2\) through \(5\). The emitted results are in `CHECK_OUTPUT.txt`. The general identities are proved above; finite checks are not used to infer the universal assertions.

To reproduce: run `python3 verify.py` in the folder containing the supplied two files. Only the Python standard library is required.

## Relationship to prior work

Varbanov, Krovi and Brun (2008) introduced continuous-time quantum hitting times under Poisson-distributed projective monitoring. Their measurement-conditioned dynamics differ from the single local imaginary absorber here, and their general hitting-time framework does not supply the present explicit flat-spectral inverse-square-gap sum or the anisotropic cube limit in the material inspected. Agliari, Mülken and Blumen (2009) studied continuous-time coherent trapping, especially rings, using non-Hermitian loss and mean survival probabilities; their ring arrangements and asymptotic analyses do not imply this all-simple-spectrum mean-time identity in the examined text.

Novo, Chakraborty, Mohseni, Neven and Omar (first preprint 2014) established the homogeneous hypercube's \((d+1)/2^d\) capture efficiency by Krylov-space reduction, and calculated the mean transfer time for a different modified complete graph. We use the homogeneous efficiency as an acknowledged benchmark, not a novelty claim. Novo, Mohseni and Omar (first preprint 2013) investigated disorder and dephasing on hypercubes, but varied on-site energies and used a recombination/dephasing transport model, rather than the anisotropic edge couplings and loss-only mean-time optimization stated here. The new statement is the exact inverse-gap identity, its sharp global rate optimum, and the resulting two different divergence exponents for bond-anisotropic cubes.

## Limitations

The result concerns a finite, single-excitation, Markovian local-loss model with no competing recombination. Ultimate capture probability at arbitrarily large times may be experimentally misleading near the isotropic limit because the mean diverges; the theorem quantifies that slowdown but does not give the full first-passage distribution. The spectral identity requires a flat local spectral measure and fails without modification for general nonflat eigenvector overlaps. The perturbative limits hold for each fixed cube dimension, not uniformly as dimension grows. Neither finite-temperature dynamics nor multiple-excitation effects are covered. Historical priority has not been independently certified; a general rank-one non-Hermitian sum rule hidden in broader literature remains the chief originality risk.

## References

1. M. Varbanov, H. Krovi, and T. A. Brun, *Hitting time for the continuous quantum walk*, arXiv:0803.3446 (first public version 2008-03-24), https://arxiv.org/abs/0803.3446.
2. E. Agliari, O. Mülken, and A. Blumen, *Continuous-Time Quantum Walks and Trapping*, arXiv:0903.3288 (first public version 2009-03-19), https://arxiv.org/abs/0903.3288.
3. L. Novo, M. Mohseni, and Y. Omar, *Disorder-assisted quantum transport in suboptimal decoherence regimes*, arXiv:1312.6989 (first public version 2013-12-25), https://arxiv.org/abs/1312.6989.
4. L. Novo, S. Chakraborty, M. Mohseni, H. Neven, and Y. Omar, *Systematic Dimensionality Reduction for Quantum Walks: Optimal Spatial Search and Transport on Non-Regular Graphs*, arXiv:1412.7209 (first public version 2014-12-22), https://arxiv.org/abs/1412.7209.
5. American Mathematical Society, *MSC2020: 81Q35, quantum mechanics on graphs, lattices and other special spaces*, https://mathscinet.ams.org/msc/msc2020.html?btn=Current&t=81Q35.
