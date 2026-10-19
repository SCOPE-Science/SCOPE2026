# Sharp site-dephasing optimum for adjacency quantum walks on finite stars

## Finding

Let \(m\ge2\) be an integer. On the star graph \(K_{1,m}\), give every hub–leaf edge the same real hopping strength \(J>0\). In the one-particle Hilbert space \(\mathbb C^{m+1}\), let \(H=JA(K_{1,m})\), and evolve density matrices with the site-projector Haken–Strobl generator
\[
\mathcal L_\gamma(X)=-i[H,X]-\gamma\bigl(X-\operatorname{diag}X\bigr),\qquad \gamma>0.
\]
Here \(\operatorname{diag}X\) retains only the site-basis diagonal; hence each off-diagonal density-matrix entry is damped at rate \(\gamma\). The full characteristic polynomial on the \((m+1)^2\)-dimensional complex operator space is
\[
\begin{aligned}
\chi_{m,\gamma}(z)={}&z(z+\gamma)^{(m-1)(m-2)}
\bigl((z+\gamma)^2+mJ^2\bigr)^{m-1}\\
&\quad\cdot\bigl(z(z+\gamma)^2+mJ^2z+2J^2\gamma\bigr)^{m-1}\\
&\quad\cdot\bigl(z(z+\gamma)^2+4mJ^2z+2(m+1)J^2\gamma\bigr).
\end{aligned}
\]
In particular, zero is a simple eigenvalue. Define the asymptotic *spectral relaxation gap* by
\[
g_m(\gamma)=\min_{z\in\operatorname{spec}(\mathcal L_\gamma)\setminus\{0\}}\bigl(-\operatorname{Re}z\bigr).
\]
Then \(g_m(\gamma)\) has the following **unique global maximizer** and exact maximum:
\[
\boxed{
\begin{array}{c|cc}
&\gamma_*&g_m(\gamma_*)\\ \hline
m=2&2\sqrt 2\,J&\sqrt 2\,J\\[2pt]
m\ge3&\displaystyle\frac{(m-1)J}{\sqrt{m-2}}&\displaystyle\frac{J}{\sqrt{m-2}}
\end{array}}
\]
For increasing hub degree, the optimal dephasing rate grows as \(J\sqrt m\) while the best achievable spectral gap *decreases* as \(J/\sqrt m\). These statements concern spectral asymptotic decay rather than the optimization of a particular initial state, finite-time observable, or mixing norm.

## Assumptions and scope

The graph is a simple undirected star with at least two leaves. The Hamiltonian is the adjacency (tight-binding) Hamiltonian with no onsite energy offsets. Every site is acted on by a projector Lindblad operator \(\sqrt\gamma\,|j\rangle\!\langle j|\), which produces the displayed off-diagonal damping convention. No other dissipative channels occur. The spectral gap is taken over the entire operator space, not only over site-diagonal density matrices or a fixed initial state's orbit. The parameter \(\gamma\) ranges over all positive real values, while \(m\) ranges over all integers at least two.

## Proof

**1. Full spectral reduction for \(m\ge3\).** Normalize \(J=1\) temporarily by dividing the generator and dephasing rate by \(J\). Label the hub \(0\), put \(\mathbf1=(1,\ldots,1)^\mathsf T\in\mathbb C^m\), and write a general operator as
\[
X=\begin{pmatrix}a&b^\mathsf T\\c&D\end{pmatrix}.
\]
The equations for its coordinates are
\[
\begin{aligned}
a'&=-i(\mathbf1^\mathsf Tc-b^\mathsf T\mathbf1),\\
b'&=-i(D^\mathsf T\mathbf1-a\mathbf1)-\gamma b,\\
c'&=-i(a\mathbf1-D\mathbf1)-\gamma c,\\
D'&=-i(\mathbf1b^\mathsf T-c\mathbf1^\mathsf T)-\gamma(D-\operatorname{diag}D).
\end{aligned}
\]
Decompose the leaf-index permutation module into the constant vector and the zero-sum subspace. The trivial component consists of \(a\), constant \(b,c\), one common leaf diagonal \(d\), and one common leaf off-diagonal \(e\). Its sum \(b+c\) has eigenvalue \(-\gamma\); the trace coordinate is stationary. On the remaining trace-zero three-dimensional subspace \(a=-md\), the variables \(q=b-c,d,e\) satisfy
\[
\begin{pmatrix}q\\d\\e\end{pmatrix}'=
\begin{pmatrix}
-\gamma&-2i(m+1)&-2i(m-1)\\
-i&0&0\\-i&0&-\gamma
\end{pmatrix}
\begin{pmatrix}q\\d\\e\end{pmatrix}.
\]
Its characteristic polynomial is
\[
P_{\rm tr}(z)=z(z+\gamma)^2+4mz+2(m+1)\gamma.
\]
For each independent zero-sum leaf vector \(v\), take hub–leaf entries \(b_i=Bv_i,c_i=Cv_i\), leaf diagonal \(D_{ii}=dv_i\), and off-diagonal entries \(D_{ij}=Rv_i+Sv_j\) for \(i\ne j\). With \(p=B+C\), \(q=B-C\), \(u=R+S\), \(w=R-S\), the evolution splits into
\[
\begin{pmatrix}p\\w\end{pmatrix}'=
\begin{pmatrix}-\gamma&im\\i&-\gamma\end{pmatrix}
\begin{pmatrix}p\\w\end{pmatrix},\qquad
\begin{pmatrix}q\\d\\u\end{pmatrix}'=
\begin{pmatrix}-\gamma&-2i&-i(m-2)\\-i&0&0\\-i&0&-\gamma\end{pmatrix}
\begin{pmatrix}q\\d\\u\end{pmatrix}.
\]
Thus each of the \(m-1\) standard leaf components contributes, respectively,
\[
P_{\rm coh}(z)=(z+\gamma)^2+m,
\qquad P_{\rm std}(z)=z(z+\gamma)^2+mz+2\gamma.
\]
Finally, a leaf block \(D\) having zero diagonal and zero row and column sums, with \(a=b=c=0\), simply decays at rate \(\gamma\). This residual space has dimension \(m^2-3m+1\). These invariant subspaces exhaust all \((m+1)^2\) matrix coordinates. Multiplying their factors, including the one additional trivial-sector eigenvalue \(-\gamma\), gives the asserted characteristic polynomial at \(J=1\). Restoring \(J\) in the Hamiltonian-induced terms gives the displayed general formula.

**2. Sharp unique optimizer for \(m\ge3\).** Again set \(J=1\), put \(s=\sqrt{m-2}\ge1\), \(x_*=1/s\), and \(\gamma_*=s+1/s\). The real-coefficient standard cubic
\[
P_{\rm std}(z)=z(z+\gamma)^2+mz+2\gamma
\]
satisfies the exact identity
\[
P_{\rm std}(-x_*)=-x_*(\gamma-\gamma_*)^2\le0,
\qquad P_{\rm std}(0)=2\gamma>0.
\]
Consequently, for every \(\gamma\ne\gamma_*\), that cubic has a real eigenvalue strictly between \(-x_*\) and \(0\). Thus \(g_m(\gamma)<x_*\) away from the proposed optimizer. At \(\gamma=\gamma_*\), set \(z=w-x_*\). The standard cubic factors as
\[
P_{\rm std}(w-x_*)=w\bigl[w^2+(2s+s^{-1})w+2(s^2+1)\bigr].
\]
Every other standard root has real part strictly less than \(-x_*\). The shifted trivial cubic is
\[
P_{\rm tr}(w-x_*)=w^3+(2s-s^{-1})w^2+(5s^2+6)w+(2s^3+3s-2s^{-1}).
\]
All three nonleading coefficients are positive; moreover their cubic Routh–Hurwitz determinant is
\[
(2s-s^{-1})(5s^2+6)-(2s^3+3s-2s^{-1})
=8s^3+4s-4s^{-1}>0.
\]
Hence every shifted trivial-cubic root has negative real part. All remaining eigenvalues have real part exactly \(-\gamma_*<-x_*\). Therefore \(g_m(\gamma_*)=x_*\), and the strict inequality away from \(\gamma_*\) proves uniqueness. Restore the factor \(J\).

**3. Exceptional two-leaf star.** When \(m=2\), direct computation in the nine-dimensional operator space yields the same characteristic formula; in particular,
\[
P_{\rm std}(z)=(z+\gamma)(z^2+\gamma z+2J^2).
\]
The quadratic pair has real part \(-\gamma/2\) up to \(\gamma=2\sqrt2J\), and above that point its larger real root is \((-\gamma+\sqrt{\gamma^2-8J^2})/2\), whose negative decreases strictly with \(\gamma\). Its best possible spectral gap is therefore \(\sqrt2J\), uniquely at \(\gamma=2\sqrt2J\). At this value the shifted trivial cubic, with \(z=w-\sqrt2J\), is
\[
w^3+\sqrt2Jw^2+6J^2w+2\sqrt2J^3,
\]
which is strictly Hurwitz by positivity and \((\sqrt2J)(6J^2)>2\sqrt2J^3\). The remaining eigenvalues are faster. Hence the full gap attains exactly that bound, uniquely.

## Verification

The independent matrix construction in `verify_star_lindblad.py` explicitly builds the \((m+1)^2\)-by-\((m+1)^2\) superoperator. Symbolic characteristic polynomials agree exactly with the claimed factorization for \(m=2,3,4\). Eigenvalues from full matrices for \(m=2,\ldots,8\), three positive hopping strengths, and seven noncritical dephasing strengths per pair agree with the claimed factor roots over 5,880 matched eigenvalues. Direct spectral-gap evaluations at the proposed optimizers also agree with the exact values. The script requires NumPy, SciPy, and SymPy and can be run as `python verify_star_lindblad.py` from the directory containing the file. The finite checks corroborate but do not replace the analytic proof for arbitrary \(m\).

## Relationship to prior work

Bressanini, Benedetti, and Paris (2022) study classicalization under site dephasing on several graph topologies, including stars; their coherent generator is the graph *Laplacian*, their metric is quantum–classical dynamical distance, and their dephasing-rate inversion is analyzed numerically rather than through the entire tight-binding adjacency Liouvillian spectrum. Adithya and collaborators (2025) numerically analyze stability of related graph-topology/noise combinations, again using a Laplacian coherent generator and initial-state-dependent observables, without an all-star-degree exact spectral optimizer. Caruso (2014) optimizes quantum stochastic-walk trapping efficiency with edge-jump noise, a different generator and objective. None of these inspected statements implies the full polynomial and unique global adjacency-generator optimum above. The equivalence between site-projector Lindblad noise and off-diagonal Haken–Strobl damping is standard and not claimed as new.

## Limitations

The tight-binding adjacency Hamiltonian on a star is not identical to a Laplacian Hamiltonian, because the degree matrix of a star is not scalar. The spectral optimum does not imply finite-time trace-distance optimality for every initial state or optimized trapping performance. The theorem assumes homogeneous edge couplings, homogeneous positive dephasing rates, no onsite detuning, a single excitation, Markovian site dephasing, and a simple unweighted star topology. Possible implicit appearances of the same exact optimizer in prior star-network master-equation literature require independent assessment; no independent audit has been performed.

## References

1. G. Bressanini, C. Benedetti, M. G. A. Paris, *Decoherence and classicalization of continuous-time quantum walks on graphs*, arXiv:2204.01836 (first posted 2022-04-04), Quantum Information Processing **21**, 317 (2022), DOI:10.1007/s11128-022-03647-x.
2. Adithya L J, J. Nokkala, J. Piilo, C. Meena, *Stability of Continuous Time Quantum Walks in Complex Networks*, arXiv:2507.17880 (first posted 2025-07-23).
3. F. Caruso, *Universally optimal noisy quantum walks on complex networks*, New Journal of Physics **16**, 055015 (2014), DOI:10.1088/1367-2630/16/5/055015.
