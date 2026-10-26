# Exact three-regime dephasing-axis control of the single-qubit Liouvillian spectral gap

## Finding
Fix a coherent angular frequency \(\omega>0\) and a dephasing rate \(\Gamma>0\). Consider the single-qubit semigroup
\[
\mathcal L(\rho)=-i[(\omega/2)\sigma_z,\rho]+(\Gamma/2)\big((n\cdot\sigma)\rho(n\cdot\sigma)-\rho\big),\qquad n=(\sin\theta,0,\cos\theta),\quad 0\le\theta\le\pi/2.
\]
Write \(u=(\omega/\Gamma)^2\), \(z=\sin^2\theta\), and \(g(\theta)\) for the negative of the largest real part of the three Bloch-block eigenvalues, excluding the always-present identity-mode zero eigenvalue. Then the global optimum, taken over all orientations of the single Hermitian dephasing axis, is
\[
\boxed{\frac{\max_\theta g(\theta)}{\Gamma}=
\begin{cases}
(1-\sqrt{1-4u})/2,&0<u\le1/4,\\
2/3-\sqrt{(1/3-u)/3},&1/4\le u\le1/3,\\
2/3,&u\ge1/3.
\end{cases}}
\]
The unique optimizing value \(z_*\in[0,1]\) is
\[
\boxed{z_*(u)=\begin{cases}
1,&0<u\le1/4,\\
2/3+\big(2/27+2((1/3-u)/3)^{3/2}\big)/u,&1/4\le u\le1/3,\\
2/3+2/(27u),&u\ge1/3.
\end{cases}}
\]
The intermediate optimum is a second-order Liouvillian exceptional point (EP2), the junction at \(u=1/3\) is a third-order exceptional point (EP3), and the high-frequency branch attains the trace upper bound with one real mode and a complex pair sharing the same real part. These are conclusions about **spectral exponential decay rates**, not about minimum finite-time trace distance; at exceptional points polynomial prefactors occur.

## Assumptions and scope
All parameters \(\omega,\Gamma\) are fixed positive real numbers; only the dephasing direction is optimized. We use Pauli matrices and \(\hbar=1\). Rotation around the Hamiltonian axis removes the azimuth of \(n\), while reversing \(n\) leaves the generator unchanged; consequently the stated interval for \(\theta\) covers the physically distinct spectral possibilities. The maximally mixed state is stationary. For \(z>0\) it is the unique stationary state, since the nontrivial Bloch spectrum has negative real parts. At \(z=0\), the dephasing operator commutes with the Hamiltonian, leaving a stationary Bloch direction and gap zero. Thus the rate definition still makes sense on the closed angle interval.

## Proof
Express the density operator as \(\rho=(I+r\cdot\sigma)/2\). The Hermitian jump gives \(\dot r=\omega e_z\times r-\Gamma(r-n(n\cdot r))\), so the nontrivial Liouvillian eigenvalues are the eigenvalues of
\[
A=\begin{pmatrix}
-\Gamma\cos^2\theta&-\omega&\Gamma\sin\theta\cos\theta\\
\omega&-\Gamma&0\\
\Gamma\sin\theta\cos\theta&0&-\Gamma\sin^2\theta
\end{pmatrix}.
\]
Dividing by \(\Gamma\), its characteristic polynomial is exactly
\[
p_{u,z}(\lambda)=\lambda^3+2\lambda^2+(1+u)\lambda+uz.
\]
For \(u>0\) and \(z>0\), the cubic Routh–Hurwitz inequalities hold: all coefficients are positive and \(2(1+u)>uz\). Hence all roots have strictly negative real parts. Define the spectral abscissa \(a(u,z)=\max\{\operatorname{Re}\lambda:p_{u,z}(\lambda)=0\}\), so optimizing the gap is minimizing \(a\).

**Weak coherent drive, \(0<u\le1/4\).** For \(z=1\), factorization gives \(p_{u,1}(\lambda)=(\lambda+1)(\lambda^2+\lambda+u)\). Its slowest root is \(r=(-1+\sqrt{1-4u})/2\). If \(z<1\), then \(p_{u,z}(r)=-u(1-z)<0\); because this real cubic tends to positive infinity on the positive real axis, a real root lies strictly to the right of \(r\). Therefore \(z=1\) uniquely minimizes the spectral abscissa and the first branch follows, including the endpoint.

**Intermediate drive, \(1/4<u<1/3\).** Put \(x=\lambda+2/3\) and \(s=\sqrt{(1/3-u)/3}>0\). The characteristic equation becomes
\[
x^3-3s^2x+b=0,\qquad b=u(z-2/3)-2/27.
\]
For every real \(b\), the largest real part of these three roots is at least \(s\), with equality **only** at \(b=2s^3\). To verify this elementary bound: for \(|b|<2s^3\) the cubic has three real roots, the largest strictly exceeds \(s\) except at the double-root endpoint \(b=2s^3\); for \(b<-2s^3\) its single real root exceeds \(2s\); and for \(b>2s^3\) its single real root is below \(-2s\), so the conjugate pair has common real part larger than \(s\). At \(b=2s^3\), the polynomial factors as \((x-s)^2(x+2s)\). The equality condition gives exactly the stated middle formula for \(z_*(u)\). It is feasible and unique: it decreases continuously from \(1\) at \(u=1/4\) to \(8/9\) at \(u=1/3\). The optimizing roots are \(-2/3+s\) (double) and \(-2/3-2s\) (simple), yielding the middle gap formula. The two-dimensional eigenspace needed for a semisimple double root is excluded by a nonzero rank-two minor of \(A-\Gamma(-2/3+s)I\), for \(\omega>0\) and \(0<z_*<1\); the repeated root is a genuine EP2.

**Strong coherent drive, \(u\ge1/3\).** Every normalized Bloch generator has trace \(-2\). The average real part of its three eigenvalues is \(-2/3\), hence the spectral abscissa cannot lie below \(-2/3\), equivalently \(g\le2\Gamma/3\). Equality forces the real part of each eigenvalue to be \(-2/3\). Because a real cubic has a real root, the depressed cubic in \(x\) must have the real root \(x=0\), so necessarily \(b=0\). This determines the **unique** optimizer \(z=2/3+2/(27u)\), which lies in \([0,1]\) for all \(u\ge1/3\). Conversely, this choice produces
\[
p_{u,z_*}(\lambda)=(\lambda+2/3)\big((\lambda+2/3)^2+u-1/3\big).
\]
Thus its eigenvalues are \(-2/3\) and \(-2/3\pm i\sqrt{u-1/3}\), attaining the trace bound. At \(u=1/3\), \(z_*=8/9\) and all roots coincide at \(-2/3\). The actual Bloch matrix then satisfies \((A/\Gamma+2I/3)^3=0\) but \((A/\Gamma+2I/3)^2\ne0\), proving an EP3 rather than a semisimple triple root. Continuity establishes both junction values; the endpoint at \(u=1/4\) is the critical EP2 in the perpendicular-axis two-by-two block. This completes the global proof for every positive parameter.

## Verification
Run the standalone `check_gap.py` from this package with Python 3, NumPy and SymPy: `python check_gap.py`. It symbolically checks the Bloch characteristic polynomial; exact cubic factorizations at four rational parameter witnesses; nilpotency of the EP3 Jordan part; and dense numerical comparisons between the proposed global maximizer and \(1001\) angles for each of \(17\) distinct coupling ratios. It also checks trace and determinant identities independently. An execution against the embedded source completed \(17097\) assertions successfully. The exact algebra and the preceding proof establish the all-parameter theorem; the finite numerical grid alone does not.

## Relationship to prior work
Am-Shallem, Kosloff and Moiseyev [1] analyze exceptional-point curves, their explicit Bloch characteristic polynomial, and the EP3 cusp for a general driven two-level Bloch model. The EP2 and EP3 *phenomena* are therefore not new claims. Their objective is locating exceptional points for parameter estimation; the present result fixes the Hamiltonian magnitude and the Hermitian dephasing strength, then solves the **global optimization over the relative axis angle** with all three sharp drive regimes and unique controls. The same cubic mechanism underlies both discussions, so the general EP-curve locus [1] is directly related, but its reported EP equations alone do not state the angle-constrained spectral-gap optimization theorem.

Kumar, Snizhko, Gefen and Rosenow [2] determine relaxation-optimal EP regimes in a related but **nonunital**, rank-one amplitude-damping/measurement-induced steering generator, optimizing over controls subject to target-state purity. Their problem does not include the present unital Hermitian-jump semigroup, fixed coherent frequency, or the displayed \(1/4\) and \(1/3\) transitions. Zhou and coauthors [3] optimize spectral gaps for dissipative three-level atoms and ion cooling, rather than this constrained qubit generator. Wu and coauthors [4] directly characterize pure-dephasing qubit exceptional points and higher-order Liouvillian degeneracies; their EP-location results are prior art and not claimed here. The present contribution is the exact full-angle spectral-gap optimum, not discovery of qubit EPs or the general trace-average bound.

## Limitations
The result is for a single qubit, one time-homogeneous Hermitian rank-one dephasing jump, a fixed coherent Hamiltonian frequency, a fixed dissipative strength, and the asymptotic *spectral* decay exponent. No global statement is made about finite-time channel contraction prefactors, transient nonnormal amplification, general Lindblad jump sets, non-Markovian reservoirs, state-dependent targets or optimal control with time-dependent axes. The relationship with larger general Bloch-optimization theorems not located by the targeted searches remains a historical-priority risk; an independent literature audit has not been undertaken.

## References
[1] M. Am-Shallem, R. Kosloff and N. Moiseyev, *Exceptional points for parameter estimation in open quantum systems: Analysis of the Bloch equations*, arXiv:1411.6364 (first public 2014-11-24), https://arxiv.org/html/1411.6364v5 .

[2] P. Kumar, K. Snizhko, Y. Gefen and B. Rosenow, *Optimized Steering: Quantum State Engineering and Exceptional Points*, arXiv:2101.07284 (first public 2021-01-18), https://arxiv.org/html/2101.07284v4 .

[3] Y.-L. Zhou et al., *Accelerating relaxation through Liouvillian exceptional point*, Phys. Rev. Research 5, 043036 (2023), https://doi.org/10.1103/PhysRevResearch.5.043036 .

[4] Z.-Z. Wu et al., *Experimental witness of quantum jump induced high-order Liouvillian exceptional points*, Nature Communications (2026), https://www.nature.com/articles/s41467-026-68705-9 .
