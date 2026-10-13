# Exact optimal dephasing and inverse-size relaxation on complete quantum networks

## Finding

For every integer \(n\ge3\), real nonzero hopping amplitude \(g\), and site-dephasing rate \(\gamma>0\), the Markovian continuous-time quantum walk on the complete graph \(K_n\) has an exact relaxation spectrum and a uniquely optimal dephasing rate. Let \(\mathbf 1\) be the all-ones column vector, \(J=\mathbf1\mathbf1^{\mathsf T}\), \(P_j=|j\rangle\langle j|\), and
\[
\mathcal L(X)=-i[g(J-I),X]+\gamma\sum_{j=1}^n\left(P_jXP_j-\tfrac12\{P_j,X\}\right)
=-ig[J,X]-\gamma(X-\operatorname{diag}X).
\]
The full complex characteristic polynomial of this \(n^2\)-dimensional superoperator is
\[
\boxed{\chi_{\mathcal L}(z)=z(z+\gamma)^{(n-1)(n-2)}\big[z((z+\gamma)^2+n^2g^2)+2n\gamma g^2\big]^{n-1}.}
\]
Its unique stationary density matrix is \(I/n\). Write \(h=2/n\) and \(\alpha=n|g|/\gamma\); exactly one \(w\in(0,h)\) obeys
\[
\frac{w(1-w)^2}{h-w}=\alpha^2.
\]
The Liouvillian spectral gap, defined as the smallest strictly positive decay rate among its nonzero eigenvalues, is **exactly** \(\Delta_n(g,\gamma)=\gamma w\). This is a simple eigenvalue within each of \(n-1\) identical three-dimensional blocks and is strictly dominant over all other decaying eigenvalues.

At fixed \(n,g\), the gap is uniquely maximized among all \(\gamma>0\) at
\[
\boxed{\gamma_*=\frac{\sqrt n\,(n-1)}{\sqrt{n-2}}|g|,\qquad\Delta_{\max}=\sqrt{\frac{n}{n-2}}|g|.}
\]
The corresponding root is \(w_*=1/(n-1)\). In the weak- and strong-dephasing limits, respectively,
\[
\Delta_n\sim\frac{2\gamma}{n}\quad(\gamma\downarrow0),\qquad
\Delta_n\sim\frac{2ng^2}{\gamma}\quad(\gamma\uparrow\infty).
\]
At fixed positive \(\gamma\) and nonzero \(g\), \(\Delta_n\sim2\gamma/n\) as \(n\to\infty\), whereas \(\Delta_{\max}\to|g|\) after optimal retuning. Thus increasing the degree of a complete network **slows** its fixed-noise asymptotic quantum relaxation, while an optimally tuned noise rate grows linearly with network size.

For a walker initially localized at any vertex \(j\), each population has the exact form
\[
\langle k|e^{t\mathcal L}(P_j)|k\rangle=\frac1n+\beta(t)\left(\delta_{jk}-\frac1n\right),
\qquad
\int_0^\infty e^{-st}\beta(t)\,dt
=\frac{(s+\gamma)^2+n(n-2)g^2}{s((s+\gamma)^2+n^2g^2)+2n\gamma g^2}
\]
for real \(s>0\). The slow eigenvalue has a strictly positive residue in the last rational function, so the site-distribution total-variation distance has a positive prefactor times \(e^{-\Delta_n t}\) asymptotically. This confirms that the gap governs the physical localized-start population relaxation, not merely an operator-space mode.

## Assumptions and scope

The network is the homogeneous complete simple graph on \(n\ge3\) sites. The Hamiltonian is \(H=g(J-I)\) with \(g\in\mathbb R\setminus\{0\}\). Each vertex has the **same** independent Markovian pure-dephasing projector Lindblad operator \(\sqrt\gamma P_j\), with \(\gamma>0\). There are no traps, losses, other baths, or interactions. The initial localized preparation is \(P_j\) and the mixing assertion concerns its instantaneous site populations as \(t\to\infty\). The spectrum and stationary-state claims concern arbitrary initial matrices/density operators. The gap is a spectral asymptotic rate, not an optimization of a particular finite-time tolerance.

## Proof

**1. Permutation-invariant decomposition.** Set \(u=\mathbf1\), and for each vector \(x\in\mathbb C^n\) with \(u^{\mathsf T}x=0\), define
\[
D_x=\operatorname{diag}(x),\quad P_x=xu^{\mathsf T}+ux^{\mathsf T},\quad Q_x=xu^{\mathsf T}-ux^{\mathsf T}.
\]
These three assignments each give independent copies of the standard \((n-1)\)-dimensional coordinate-sum-zero module. Let
\[
W=\{X:\operatorname{diag}X=0,\ Xu=0,\ u^{\mathsf T}X=0\}.
\]
Its dimension is \(n^2-3n+1\) for \(n\ge3\). Directly using the diagonal, row sums and column sums gives the direct vector-space decomposition
\[
M_n(\mathbb C)=\mathbb CI\ \oplus\ \mathbb C(J-I)\ \oplus W\ \oplus\ \{D_x,P_x,Q_x:u^{\mathsf T}x=0\}.
\]
The last set denotes the direct sum of the three parameterized families. Its total dimension is \(3(n-1)\); the overall dimension is \(n^2\). Both \(J-I\) and \(W\) have zero diagonal and commute with \(J\), so \(\mathcal L=-\gamma\) there. Also \(\mathcal L(I)=0\). The remaining action is explicitly
\[
\mathcal L(D_x)=igQ_x,\quad
\mathcal L(P_x)=2\gamma D_x-\gamma P_x+ingQ_x,\quad
\mathcal L(Q_x)=ingP_x-\gamma Q_x.
\]
Thus for each independent \(x\), the generator in the ordered basis \((D_x,P_x,Q_x)\) is
\[
M=\begin{pmatrix}0&2\gamma&0\\0&-\gamma&ing\\ig&ing&-\gamma\end{pmatrix},\quad
\det(zI-M)=z((z+\gamma)^2+n^2g^2)+2n\gamma g^2.
\]
Multiplying the scalar factors with their correct dimensions proves the displayed characteristic polynomial, including all algebraic multiplicities. No assumption of generic distinct cubic roots is needed for the factorization.

**2. Unique decay root and dominance.** Scaling a cubic eigenvalue as \(z=\gamma\zeta\) gives
\[
f(\zeta)=\zeta(\zeta+1)^2+\alpha^2(\zeta+h).
\]
A real negative root \(\zeta=-w\) with \(0<w<h\) exists exactly when \(F(w)=\alpha^2\), with \(F(w)=w(1-w)^2/(h-w)\). Its derivative has the same positive sign as \((1-w)(h-3hw+2w^2)\). Since \(0<h\le2/3\),
\[
h-3hw+2w^2\ge h-\frac{9h^2}{8}>0,
\]
and \(F\) runs continuously from zero to infinity. Hence there is exactly one such \(w\). Polynomial division yields
\[
f(\zeta)=(\zeta+w)\big(\zeta^2+(2-w)\zeta+c\big),\quad c=\frac{h(1-w)^2}{h-w}>0.
\]
If the quadratic roots are nonreal, their real parts are \(-1+w/2<-w\), since \(w<h\le2/3\). If real, their sum is \(-(2-w)\), while their value polynomial at \(-w\) is
\[
w^2-(2-w)w+c
=\frac{(1-w)(h-3hw+2w^2)}{h-w}>0.
\]
The quadratic derivative at \(-w\) is \(2-3w>0\), so \(-w\) lies strictly **to the right** of both real quadratic roots. Finally \(-1<-w\), so \(-\gamma w\) is strictly the dominant nonstationary eigenvalue. The identity
\[
\operatorname{Re}\langle X,\mathcal L(X)\rangle_{\mathrm{HS}}=-\gamma\|X-\operatorname{diag}X\|_{\mathrm{HS}}^2
\]
shows that a purely imaginary eigenoperator is diagonal, then commutation with \(J\) forces it to be scalar. Thus the stationary state is uniquely \(I/n\), with no additional imaginary-axis modes.

**3. Unique optimization.** The root equation gives a bijection from \(\gamma\in(0,\infty)\) to \(w\in(h,0)\) with reversed orientation. Eliminating \(\gamma\) yields
\[
\Delta_n=n|g|\frac{\sqrt{w(h-w)}}{1-w}.
\]
The logarithmic derivative has numerator \(h+(h-2)w\) after multiplication by the positive factor \(2w(h-w)(1-w)\). It changes sign exactly once, at \(w=h/(2-h)=1/(n-1)\), from positive to negative. Substitution proves the unique optimizer and the optimal gap. The stated three asymptotic laws follow from \(F(w)\sim w/h\) as \(w\downarrow0\), from \(F(w)\to\infty\) as \(w\uparrow h\), and from \(w/h\to1\) at fixed positive rates as \(n\to\infty\).

**4. Physical population decay.** Write \(P_j=I/n+D_x\), where \(x=e_j-u/n\). In the same invariant block, let the evolving coefficients of \((D_x,P_x,Q_x)\) be \((a(t),b(t),c(t))\), initially \((1,0,0)\). Its diagonal population contrast equals \(\beta(t)=a(t)+2b(t)\). Solving the three linear Laplace-transform equations gives
\[
\widetilde a(s)=\frac{(s+\gamma)^2+n^2g^2}{s((s+\gamma)^2+n^2g^2)+2n\gamma g^2},\quad
\widetilde b(s)=\frac{-ng^2}{s((s+\gamma)^2+n^2g^2)+2n\gamma g^2}.
\]
Their combination is the displayed \(\widetilde\beta\). At \(s=-\gamma w\), the numerator is \(\gamma^2(1-w)^2+n(n-2)g^2>0\). The denominator has a simple root there, with positive derivative because its other two roots lie strictly to the left (and are either both real or a complex pair). The residue is therefore strictly positive. The remaining poles decay strictly faster, even if accompanied by polynomial factors from repeated roots. For every initial site, the total-variation distance is exactly \((n-1)|\beta(t)|/n\), hence its nonzero leading exponential decay rate is \(\Delta_n\).

## Verification

The self-contained numerical file `verify.py` constructs the full \(n^2\)-dimensional Lindblad matrix directly from its matrix-element action, independently of the invariant-block derivation. It checks the predicted complete spectra and gaps over several site counts, hopping amplitudes and dephasing strengths; it also compares the predicted Laplace transform to resolvent entries and the population profile to full matrix exponentials. Its optimization tests compare the predicted unique maximum with multiple neighboring rates. Run `python3 verify.py` after installing packages in `requirements.txt`. These finite tests are checks, not substitutes for the all-\(n\) proof above.

## Relationship to prior work

Solenov and Fedichkin (arXiv:quant-ph/0506096, first submitted 13 June 2005) treat local monitoring and position-basis decoherence for **cycle** graphs, deriving population dynamics and mixing estimates. Their graph and resulting spectrum differ. Bressanini, Benedetti and Paris (arXiv:2204.01836, DOI:10.1007/s11128-022-03647-x) study the **same site-projector Haken--Strobl generator** on several graphs, including complete graphs, but evaluate a quantum--classical distance and its numerical convergence behavior rather than deriving this full Liouvillian polynomial, exact spectral-gap optimization or its inverse-size scaling. Alterman, Berman and Strauch (arXiv:2309.00164) analytically study a complete graph under dephasing **with a designated irreversible trap and recombination**, optimizing transfer efficiency and transfer rate; these quantities are different from the trace-preserving full-generator spectral gap without any trap. The present claim is the complete-graph exact spectral and intrinsic relaxation optimization, not the earlier general noise-assisted mixing observation, cycle bounds, or trapped-transfer optimizers.

## Limitations

The model assumes uniform dephasing, homogeneous all-to-all hopping, and \(n\ge3\); no assertion is made for site-dependent rates, disorder, trapping, interactions, or other graph families. The maximized quantity is the asymptotic spectral-gap exponent (also realized by localized site populations), not a universal optimum for every finite observation time or every distance measure. Similar spectral facts may have been derived in broader symmetry-reduced open-system literature not located in the stated sources; external independent publication-priority review has not been performed. The particular numerical tests cover only finite instances, while the algebraic proof covers the full quantified domain.

## References

1. D. Solenov and L. Fedichkin, *Continuous-time Quantum Walks on a Cycle Graph*, arXiv:quant-ph/0506096 (first submitted 2005-06-13), Phys. Rev. A 73, 012313 (2006), DOI:10.1103/PhysRevA.73.012313.
2. G. Bressanini, C. Benedetti and M. G. A. Paris, *Decoherence and classicalization of continuous-time quantum walks on graphs*, arXiv:2204.01836 (2022), Quantum Information Processing 21, 317, DOI:10.1007/s11128-022-03647-x.
3. S. Alterman, J. Berman and F. W. Strauch, *Optimal Conditions for Environment-Assisted Quantum Transport on the Fully Connected Network*, arXiv:2309.00164 (2023), Phys. Rev. E 109, 014310 (2024), DOI:10.1103/PhysRevE.109.014310.
4. L. Fedichkin, D. Solenov and C. Tamon, *Mixing and Decoherence in Continuous-Time Quantum Walks on Cycles*, arXiv:quant-ph/0509163 (first submitted 2005-09-22), Quantum Information and Computation 6, 263--276 (2006).
