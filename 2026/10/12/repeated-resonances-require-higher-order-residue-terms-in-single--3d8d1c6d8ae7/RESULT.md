# Repeated resonances require higher-order residue terms in single-runway quantum-graph scattering
## Finding
For the single-runway discrete-time quantum-graph scattering framework of Cottrell, the impulse-response residue formula remains valid without a simplicity assumption, but the displayed pure-exponential form in Theorem 2.10 requires every nonzero root of the denominator polynomial to be simple. Repeated nonzero roots are admissible in the stated framework and contribute a polynomial in the time index multiplying the exponential.

An explicit four-state family demonstrates the missing case. Put \(r=-1/\sqrt6\) and, in the ordered basis \((|\mathrm{in}\rangle,e_2,e_3,|\mathrm{out}\rangle)\), define
\[
U_\alpha=\begin{pmatrix}
0&0&0&\alpha\\
\sqrt3/6&-\sqrt6/3&-1/2&0\\
2\sqrt2/3&1/3&0&0\\
1/6&-\sqrt2/3&\sqrt3/2&0
\end{pmatrix}.
\]
For every \(|\alpha|=1\), \(U_\alpha\) is unitary and satisfies \(U_\alpha|\mathrm{out}\rangle=\alpha|\mathrm{in}\rangle\). Its characteristic polynomial is
\[
C(z,\alpha)=z^2(z-r)^2-\alpha(1-rz)^2.
\]
Thus the open operator \(U_0\) has a repeated nonzero resonance \(r\), with \(|r|<1\), and the corresponding scattering function is
\[
S(z)=\frac{(1-rz)^2}{z^2(z-r)^2}.
\]
The impulse response is therefore
\[
h[n]=0\quad(n<2),
\]
and, for \(n\ge2\),
\[
h[n]=6\,\delta_{n,2}+\frac{5(5n-17)}{36}\,r^{\,n-4}.
\]
The second term is linear in \(n\) times an exponential, so it cannot be represented by the pure-exponential sum asserted in Theorem 2.10 for distinct roots. In that theorem's coefficient formula, the factor \(\eta_j-\eta_k\) in the denominator is also singular when two roots coincide.

The multiplicity-aware replacement is immediate from the source's contour formula. If
\[
f(z)=z^s\prod_{\ell=1}^q(z-\eta_\ell)^{m_\ell},
\]
where the nonzero \(\eta_\ell\) are distinct and \(q_\ell(z)=f(z)/(z-\eta_\ell)^{m_\ell}\), then the contribution of \(\eta_\ell\) is
\[
h_\ell[n]=-
\frac{1}{(m_\ell-1)!}
\left.
\frac{d^{m_\ell-1}}{dz^{m_\ell-1}}
\left(z^{n-1}\frac{g(z)}{q_\ell(z)}\right)
\right|_{z=\eta_\ell}.
\]
Consequently a resonance of multiplicity \(m_\ell\) contributes an exponential multiplied by a polynomial in \(n\) of degree at most \(m_\ell-1\). The source's pure-exponential statement is recovered exactly when all nonzero resonances are simple.

## Assumptions and scope
The result concerns the finite-dimensional single-runway unitary closure used in Cottrell's scattering construction. The variable \(\alpha\) closes the outgoing runway state back to the incoming runway state, and physical closures satisfy \(|\alpha|=1\). The scattering function is the source's rational function \(S(z)=-g(z)/f(z)\), and the impulse response is defined by its Laurent/Fourier coefficients. No claim is made about continuous metric-graph Schrödinger scattering or about infinite-dimensional graph Hamiltonians.

The explicit matrix is a valid instance because its lower-left \(3\times3\) block
\[
V=\begin{pmatrix}
\sqrt3/6&-\sqrt6/3&-1/2\\
2\sqrt2/3&1/3&0\\
1/6&-\sqrt2/3&\sqrt3/2
\end{pmatrix}
\]
satisfies \(V^{\mathsf T}V=I\) and \(\det V=1\). Hence \(U_\alpha\) is unitary for \(|\alpha|=1\).

## Proof
Direct determinant expansion gives
\[
\det(zI-U_\alpha)=z^2(z-r)^2-\alpha(1-rz)^2,
\qquad r=-1/\sqrt6.
\]
At \(\alpha=0\), the nonzero root \(r\) has algebraic multiplicity two. Moreover,
\[
\dim\ker(U_0-rI)=1,
\qquad
\dim\ker(U_0-rI)^2=2,
\]
so the repeated root is a genuine size-two Jordan resonance rather than a removable duplicate factor.

Taking \(f(z)=z^2(z-r)^2\) and \(g(z)=-(1-rz)^2\) yields
\[
S(z)=-\frac{g(z)}{f(z)}
=\frac{(1-rz)^2}{z^2(z-r)^2}.
\]
With \(w=z^{-1}\),
\[
S=w^2\frac{(w-r)^2}{(1-rw)^2}.
\]
Expanding \((1-rw)^{-2}=\sum_{k\ge0}(k+1)r^kw^k\) and collecting coefficients gives the stated formula for \(h[n]\). Equivalently, the repeated pole at \(z=r\) is evaluated by the order-two residue formula, which differentiates \(z^{n-1}g(z)/q(z)\) and creates the linear factor in \(n\).

For general multiplicity \(m_\ell\), the contour identity
\[
h[n]=-
\sum_{\zeta\in Z(f)}
\operatorname{Res}_{z=\zeta}
\left(z^{n-1}\frac{g(z)}{f(z)}\right)
\]
reduces at \(\eta_\ell\ne0\) to the displayed higher-order derivative formula. Differentiating \(z^{n-1}\) at most \(m_\ell-1\) times produces a polynomial in \(n\) of degree at most \(m_\ell-1\), completing the correction.

## Verification
The included checker verifies exactly that \(V^{\mathsf T}V=I\), \(\det V=1\), the characteristic polynomial has the claimed factorization, and the repeated root has a size-two Jordan chain. It also expands the rational scattering function and checks the closed coefficient formula through thirteen coefficients. These finite coefficient checks supplement, but do not replace, the analytic generating-function and residue proof.

## Relationship to prior work
Cottrell's paper proves the contour-residue representation and factors the denominator into roots inside the unit disk. Its Theorem 2.5 explicitly notes that higher-degree roots can occur for closures away from the unit circle, while Theorem 2.10 subsequently writes coefficients using denominators \(\eta_j-\eta_k\) and concludes that the impulse response is a sum of exponentially decaying signals. The explicit family above shows that the repeated-root case is not merely formal: it occurs within the same finite-dimensional closure architecture.

The generic signal-processing fact that repeated poles produce polynomially weighted exponentials is standard and is not claimed as new. The contribution here is the source-specific identification of the missing hypothesis, an admissible finite quantum-graph realization with a double nonzero resonance, and the corresponding multiplicity-aware replacement for the source theorem. General metric-quantum-graph scattering formalisms are also prior and address a different continuous model.

## Limitations
This result does not classify which multiplicity patterns are realizable for arbitrary graph sizes, nor does it address perturbative splitting of a repeated resonance. The explicit example establishes existence of an admissible repeated nonzero resonance and disproves the unrestricted pure-exponential conclusion; it does not imply that repeated resonances are generic. A source-specific correction may exist in an unindexed erratum or downstream note that was not located in the checked literature.

## References
1. Seth S. Cottrell, “A Simple Method for Finding the Scattering Coefficients of Quantum Graphs,” arXiv:1503.00253; DOI: 10.1063/1.4931082.
2. V. Caudrelier and E. Ragoucy, “Direct computation of scattering matrices for general quantum graphs,” arXiv:0907.5359.
3. J. O. Smith III, “Repeated Poles,” in *Introduction to Digital Filters*, DSPRelated online notes.
