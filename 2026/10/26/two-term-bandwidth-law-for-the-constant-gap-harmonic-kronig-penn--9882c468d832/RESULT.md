# Two-term bandwidth law for the constant-gap harmonic Kronig–Penney lattice

## Finding
For every fixed integer \(n\geq0\), the \(n\)-th spectral band (numbered from zero) of the self-adjoint periodic harmonic Kronig–Penney operator at its repulsive exactly-solvable coupling \(\gamma=a\) has width
\[
\boxed{\displaystyle
w_n(a)=\frac{2^{n+2}}{n!\sqrt\pi}\,a^{2n+1}e^{-a^2}
\left(1-\frac{(n+1)^2}{2a^2}+O_n(a^{-4})\right),\qquad a\to\infty.}
\]
The coefficient \((n+1)^2/2\) is the first explicit relative correction: it combines the boundary confinement correction of the \(n\)-th well state with subtraction of the preceding level's exponentially small displacement. In particular, \(w_{n+1}(a)/w_n(a)\sim 2a^2/(n+1)\) for fixed \(n\). The formula is not uniform when \(n\) grows with \(a\).

## Assumptions and scope
For \(a>0\), let
\[
\mathcal L_a=-\frac{d^2}{dx^2}+[x^2-1]_{2a}
+2a\sum_{j\in\mathbb Z}\delta(x-(2j+1)a)
\]
act in \(L^2(\mathbb R)\), where \([x^2-1]_{2a}\) denotes the \(2a\)-periodic extension of \(x^2-1\) from \((-a,a)\). Its domain is piecewise \(H^2\), with continuity at each defect and derivative jump \(\psi'(x+)-\psi'(x-)=2a\psi(x)\). Bands are connected components of the absolutely continuous spectrum, in increasing energy order, labelled \(B_0,B_1,\dots\). Let \(\Lambda_n(a)\) denote the \(n\)-th Dirichlet eigenvalue, numbered from zero, of \(-d^2/dx^2+x^2-1\) on \((-a,a)\), and set \(\delta_n(a)=\Lambda_n(a)-2n\), with \(\delta_{-1}(a)=0\). All limits here keep \(n\) fixed as \(a\to\infty\).

## Proof
**Step 1: exact band-edge reduction.** At coupling \(\gamma=a\), the even/odd Weber solutions obey the ladder identities
\[
W_+'(a,E)+aW_+(a,E)=-E W_-(a,E-2),\qquad
W_-'(a,E)+aW_-(a,E)=W_+(a,E-2).
\]
Consequently the Dirichlet edges are \(\{\Lambda_n(a)\}\), and the other edges are the exact ground energy \(0\) and \(\{2+\Lambda_n(a)\}\) (Gibbons–Veselov, Proposition 5.1). Standard Dirichlet domain exhaustion gives \(\Lambda_n(a)\downarrow2n\) for fixed \(n\). We shall show \(\delta_n>\delta_{n-1}>0\) for all sufficiently large \(a\). The spectral interlacing then identifies
\[
B_0(a)=[0,\Lambda_0(a)],\qquad
B_n(a)=[2+\Lambda_{n-1}(a),\Lambda_n(a)]\quad(n\geq1),
\]
and hence \(w_n(a)=\delta_n(a)-\delta_{n-1}(a)\) exactly for such \(a\).

**Step 2: a two-term displacement of the confined oscillator level.** Fix \(n\). Set \(u_n(x)=H_n(x)e^{-x^2/2}\), where \(H_n\) is the physicists' Hermite polynomial. Then
\[
(-d^2/dx^2+x^2-1)u_n=2n u_n,\qquad
I_n:=\int_0^\infty u_n(x)^2\,dx=2^{n-1}n!\sqrt\pi.
\]
Let \(y(x,E)\) solve the same differential equation at energy \(E\) with Cauchy data at \(x=0\) identical to those of \(u_n\). In particular \(y(x,2n)=u_n(x)\). Its parity equals that of \(u_n\), so a zero of \(y(a,E)\) determines the corresponding Dirichlet eigenvalue on \((-a,a)\). Differentiate at \(E=2n\), writing \(v_E(x)=\partial_E y(x,E)|_{E=2n}\). The inhomogeneous equation gives the *exact* Wronskian identity
\[
\frac{d}{dx}\bigl(u_n v_E'-u_n'v_E\bigr)=-u_n^2,
\qquad
u_n(x)v_E'(x)-u_n'(x)v_E(x)=-\int_0^x u_n(t)^2\,dt.
\]
Choose \(R\) larger than every positive zero of \(H_n\), and define the growing homogeneous solution for \(x\geq R\) by
\[
q_n(x)=u_n(x)J_n(x),\qquad
J_n(x)=\int_R^x\frac{dt}{u_n(t)^2}.
\]
It satisfies \(u_nq_n'-u_n'q_n=1\). Variation of parameters for \(v_E\) on \([R,\infty)\) gives
\[
v_E(x)=-\left(\int_0^x u_n(t)^2dt\right)q_n(x)+c_n(x)u_n(x),
\qquad c_n'(x)=u_n(x)q_n(x).
\]
Since \(u_n(x)q_n(x)=O(x^{-1})\), we have \(c_n(x)=O_n(\log x)\). Moreover, the omitted tail in \(I_n\) is exponentially small. It follows that
\[
\partial_Ey(a,2n)=-I_n\,u_n(a)J_n(a)
\left(1+O_n(a^{K_n}e^{-a^2})\right)
\]
for some finite \(K_n\). Analytic dependence of the initial-value solution on \(E\), together with the standard large-positive-argument estimates for the two Kummer solutions, bounds its second energy derivative by \(e^{a^2/2}\) times a fixed power of \(a\) in a small fixed-index neighbourhood. Taylor's formula and the simple Dirichlet root therefore give
\[
\delta_n(a)=\frac{1}{I_nJ_n(a)}
\left(1+O_n(a^{K'_n}e^{-a^2})\right).
\]
Here and below, an exponentially small factor multiplying a fixed power can be absorbed into every fixed inverse-power remainder. The root is positive, and the argument uses an exponentially small neighbourhood of the already identified \(n\)-th Dirichlet branch; it makes no inference from a finite numerical scan.

The Hermite leading polynomial terms are
\[
H_n(t)=2^nt^n\left(1-\frac{n(n-1)}{4t^2}+O_n(t^{-4})\right).
\]
Elementary endpoint Laplace expansion of \(J_n\) now yields
\[
\begin{aligned}
J_n(a)&=2^{-2n}\int_R^a e^{t^2}t^{-2n}
\left(1+\frac{n(n-1)}{2t^2}+O_n(t^{-4})\right)dt\\
&=\frac{e^{a^2}}{2^{2n+1}a^{2n+1}}
\left(1+\frac{n^2+n+1}{2a^2}+O_n(a^{-4})\right).
\end{aligned}
\]
Indeed, the integration-by-parts correction to \(\int e^{t^2}t^{-2n}dt\) is \((2n+1)/(2a^2)\), and the inverse-Hermite correction is \(n(n-1)/(2a^2)\); their sum is \((n^2+n+1)/(2a^2)\). Therefore
\[
\boxed{\displaystyle
\delta_n(a)=\frac{2^{n+2}}{n!\sqrt\pi}\,a^{2n+1}e^{-a^2}
\left(1-\frac{n^2+n+1}{2a^2}+O_n(a^{-4})\right).}
\]
This also independently recovers the leading confined-oscillator shift of Gannot (2014), with an explicitly evaluated next coefficient.

**Step 3: subtract consecutive edges.** For \(n\geq1\), the leading ratio of successive displacements is
\[
\frac{\delta_{n-1}(a)}{\delta_n(a)}=\frac{n}{2a^2}+O_n(a^{-4}).
\]
In particular \(\delta_n>\delta_{n-1}\) for sufficiently large \(a\), justifying Step 1. Subtracting gives
\[
\begin{aligned}
w_n(a)&=\delta_n(a)-\delta_{n-1}(a)\\
&=\frac{2^{n+2}}{n!\sqrt\pi}a^{2n+1}e^{-a^2}
\left(1-\frac{n^2+n+1+n}{2a^2}+O_n(a^{-4})\right),
\end{aligned}
\]
which is the stated formula. For \(n=0\), \(w_0=\delta_0\) gives the same answer. Taking consecutive leading terms gives the claimed bandwidth ratio.

## Verification
The companion `verify.py` independently evaluates the parity-reduced Dirichlet equations
\[
{}_1F_1\left(-m-\frac{\delta}{4};\,s+\frac12;\,a^2\right)=0,
\qquad n=2m+s,\quad s\in\{0,1\},
\]
using arbitrary-precision root finding. It compares exact differences of adjacent roots to the leading and two-term formulas at three separation values, checks the shifted Dirichlet/Robin boundary identity, and checks the even/odd coefficient reduction. The script reported 61 passing assertions on its scientific test conditions. The proof is the variation-of-parameters argument above; finite numerical experiments are not a proof for all indices or arbitrarily large separation.

## Relationship to prior work
Gibbons and Veselov (2026, arXiv:2610.00879v1), Proposition 5.1, derive exact band edges and the constant gap length \(2\), and explicitly identify precise exponential shrinkage of the lowest bands at large separation as requiring further investigation (Section 7). Their formulas supply the exact edge reduction but not the two-term band-width asymptotics. Gannot (2014, arXiv:1410.0068), Corollary 1.1, gives the leading exponential Dirichlet harmonic-oscillator level shift with relative \(O(a^{-2})\) error; the general theorem guarantees a full asymptotic expansion but does not evaluate this next coefficient or the difference of consecutive shifts. Helffer, Kachmar and Nicoleau (2026, arXiv:2609.28076v1), Appendix B, give leading Kummer first-parameter zero asymptotics in a related singular oscillator. Moore and Marsiglio (2026, arXiv:2605.08032v1) study truncated oscillator wells separated by flat barrier regions, not the delta-defect lattice at \(\gamma=a\). Standard Kummer asymptotics are recorded in NIST DLMF §13.7. This identifies the actual scope of the contribution: an explicit first relative correction for *band widths*, not the generic existence of exponentially small confinement shifts or the constant-gap property.

## Limitations
The expansion holds for each fixed nonnegative band index as \(a\to\infty\); its constants and validity threshold may depend on that index. It provides neither a uniform result at indices growing with \(a\) nor a quasimomentum-resolved dispersion law. Leading confined-oscillator behavior and general all-order expansion existence are known; an earlier unlocated explicit specialization of that expansion could duplicate the displayed correction, so independent priority verification remains necessary. No independent scientific audit was performed.

## References
1. J. Gibbons and A. P. Veselov, *On spectrum of the harmonic Kronig–Penney model*, arXiv:2610.00879v1 (first public 2026-10-01), Sections 4, 5, 7. https://arxiv.org/html/2610.00879v1
2. O. Gannot, *Effects of confinement for single-well potentials*, arXiv:1410.0068 (2014), Theorem 1 and Corollary 1.1. https://arxiv.org/abs/1410.0068
3. B. Helffer, A. Kachmar and F. Nicoleau, *Spectral Asymptotics of a Singular Harmonic Oscillator with Aharonov–Bohm Flux*, arXiv:2609.28076v1 (2026), Appendix B, Eq. (B.9). https://arxiv.org/pdf/2609.28076
4. C. Moore and F. Marsiglio, *Analytical Solution to the Kronig-Penney Model with Harmonic Oscillator Wells: Insights to Tight-Binding*, arXiv:2605.08032v1 (2026), Sections II–IV. https://arxiv.org/html/2605.08032v1
5. NIST Digital Library of Mathematical Functions, §13.7, confluent hypergeometric asymptotics. https://dlmf.nist.gov/13.7
