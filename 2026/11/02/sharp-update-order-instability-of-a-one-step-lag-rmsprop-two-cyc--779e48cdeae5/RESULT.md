# Sharp update-order instability of a one-step-lag RMSProp two-cycle

## Finding

Consider the deterministic scalar quadratic-gradient recurrence with one-step stale preconditioning, defined precisely below. For every \(a,\varepsilon>0\), \(0<\beta<1\), it has exactly one primitive two-cycle if and only if \(h>2\varepsilon/a\). The cycle is \((q,a^2q^2)\leftrightarrow(-q,a^2q^2)\), with \(q=h/2-\varepsilon/a\).

**Sharp full-state stability theorem.** This orbit is locally exponentially attracting if and only if
\[
2\varepsilon/a<h<4\varepsilon/a.
\]
At \(h=4\varepsilon/a\) its two-step Jacobian has a conjugate pair on the unit circle, crossing transversely as \(h\) increases; nonlinear attraction or repulsion at equality is not determined here. For every \(h>4\varepsilon/a\) the same orbit is a hyperbolic local repeller. Thus the loss of local orbital attraction is sharp and the upper threshold is independent of the memory-decay parameter \(\beta\).

The exact node-to-spiral crossover of the attracting two-cycle occurs at
\[
h_{\mathrm{nf}}=\frac{16\varepsilon}{a(7+\beta)}.
\]
For \(2\varepsilon/a<h<h_{\mathrm{nf}}\), the two-step multipliers are distinct, positive, and smaller than one; at the crossover they are repeated and the Jacobian is defective; for \(h_{\mathrm{nf}}<h<4\varepsilon/a\), they are a complex conjugate pair with modulus less than one. For \(h>4\varepsilon/a\), they are complex conjugates of modulus greater than one.

## Assumptions and scope

Fix \(a>0\), \(\varepsilon>0\), \(0<\beta<1\), and \(h>0\), and set \(L(x)=a x^2/2\). The precisely specified *lagged* (not standard current-memory) map on \(\mathbb R\times[0,\infty)\) is
\[
F_h(x,v)=\left(x-\frac{hax}{\varepsilon+\sqrt v},\;\beta v+(1-\beta)a^2x^2\right).
\]
The spatial displacement divides by the memory \(v\) at the **beginning** of the iteration. The newly accumulated squared gradient is stored as the next memory; it is not used for the current spatial displacement. All local stability conclusions concern both coordinates \((x,v)\), not just the spatial projection. For a two-cycle, the two-step monodromy is evaluated in the order \(DF_h(P_-)DF_h(P_+)\).

## Proof

**1. Every primitive two-cycle is antipodal and has fixed memory.** Let \((x_0,v_0)\mapsto(x_1,v_1)\mapsto(x_0,v_0)\) be a period-two solution. The scalar equation preserves the set \(x=0\), whose memory recurrence contracts strictly; hence a primitive cycle must have \(x_0x_1\ne0\). Adding the two spatial displacements gives
\[
\frac{x_0}{\varepsilon+\sqrt{v_0}}=-\frac{x_1}{\varepsilon+\sqrt{v_1}}.
\]
In particular, the spatial values have opposite signs. Subtracting the two memory updates gives the identity
\[
(1+\beta)(v_1-v_0)=(1-\beta)a^2(x_0^2-x_1^2).
\]
If \(|x_0|>|x_1|\), then \(v_1>v_0\), making the left displacement magnitude \(|x_0|/(\varepsilon+\sqrt{v_0})\) *strictly larger* than the right displacement magnitude \(|x_1|/(\varepsilon+\sqrt{v_1})\), a contradiction. Reversing the inequality similarly contradicts the displacement identity. Therefore \(|x_0|=|x_1|\) and \(v_0=v_1\). As signs are opposite, \(x_1=-x_0\), and the memory recurrence forces \(v_0=v_1=a^2x_0^2\). Substituting into the spatial step gives \(h a/(\varepsilon+a|x_0|)=2\). Hence the stated unique primitive orbit exists exactly when \(q=h/2-\varepsilon/a>0\).

**2. Exact two-step characteristic polynomial.** Write \(P_+=(q,a^2q^2)\), \(P_-=(-q,a^2q^2)\) and \(S=\operatorname{diag}(-1,1)\). Since \(F_h(Sz)=SF_h(z)\), the two one-step Jacobians satisfy \(J_-=SJ_+S\). Differentiating the map and using \(\varepsilon+a q=h a/2\) gives
\[
J_+=\begin{pmatrix}-1&2/(a^2h)\\2(1-\beta)a^2q&\beta\end{pmatrix},\qquad
K=SJ_+=\begin{pmatrix}1&-2/(a^2h)\\2(1-\beta)a^2q&\beta\end{pmatrix}.
\]
The monodromy \(P=J_-J_+=K^2\) has eigenvalues equal to the squares of the two roots of
\[
\det(zI-K)=z^2-(1+\beta)z+d(h),\qquad
d(h)=\beta+4(1-\beta)\frac qh=2-\beta-\frac{4(1-\beta)\varepsilon}{a h}.
\]
This identity follows from the exact trace \(\operatorname{tr}K=1+\beta\) and determinant \(\det K=d(h)\). No small-amplitude approximation is used.

**3. Sharp stability window.** For a real monic quadratic \(z^2-tz+d\), both roots lie strictly inside the unit disk precisely when \(1-t+d>0\), \(1+t+d>0\), and \(1-d>0\). Here \(t=1+\beta\), and for any existing nontrivial two-cycle \(d(h)>\beta\), so the first two inequalities are automatic. The third is equivalent to
\[
2-\beta-\frac{4(1-\beta)\varepsilon}{ah}<1
\quad\Longleftrightarrow\quad h<4\varepsilon/a.
\]
Because \(q>0\), the map is smooth on a neighborhood of both cycle points. This strict Schur condition implies local exponential attraction of the orbit under the full two-step map.

At \(h=4\varepsilon/a\), \(d=1\), and \(|1+\beta|<2\), so the roots of the polynomial for \(K\) are distinct conjugate numbers of modulus one. The derivative \(d'(h)=4(1-\beta)\varepsilon/(ah^2)>0\) establishes transversal radial crossing. For \(h>4\varepsilon/a\), \(d(h)>1\) and the discriminant is negative by Step 4; the eigenvalues of \(K^2\) therefore both have modulus \(d(h)>1\), giving a hyperbolic repelling periodic orbit. No nonlinear bifurcation type is inferred at the equality.

**4. Node-to-spiral threshold.** The discriminant of the polynomial for \(K\) is
\[
\Delta(h)=(1+\beta)^2-4d(h)=(1-\beta)^2-\frac{16(1-\beta)q}{h}.
\]
As \(q/h=1/2-\varepsilon/(ah)\) increases strictly with \(h\), its sole zero on the existence branch is \(h_{\mathrm{nf}}=16\varepsilon/[a(7+\beta)]\). Direct comparison shows \(2\varepsilon/a<h_{\mathrm{nf}}<4\varepsilon/a\). For \(\Delta>0\), the roots of \(K\) are positive (positive trace and determinant) and strictly smaller than one in the stable window. At \(\Delta=0\), \(K\) has a repeated positive root with nonzero off-diagonal entry, hence a nontrivial Jordan block. For \(\Delta<0\), its roots are conjugate with modulus \(\sqrt{d(h)}\); their squares have modulus \(d(h)\). This proves all stated spectral regimes.

## Verification

The accompanying standalone `verify.py` uses exact SymPy algebra to differentiate the *defined lagged map*, evaluate the two exact cycle points, check the reflection factorization of its full monodromy, verify the trace/determinant and discriminant identities, and test representative strict inequalities at rational parameter values. Run `python verify.py` with SymPy installed. The analytical proof, not the finite parameter checks, establishes the unrestricted parameter claims.

## Relationship to prior work

Loh, Mireles-James, Xu, and Tao, *The Dynamics of RMSProp Beyond the Stability Threshold*, arXiv:2610.30078v1 (2026), define and study epsilon-outside RMSProp with the **newly updated** second moment in the denominator. Their Lemma 5.1, Theorems 5.2–5.3 and 5.7 establish period-two structure, existence threshold and local stability near onset for that distinct map, and their Section 8.3 presents scalar numerical observations. Their statements do not imply stability thresholds for a recurrence that instead uses the *previous* second moment in each spatial update. The exact timing distinction changes the Jacobian, even though the symmetric orbit has the same coordinates.

Li, Zaheer, Liu, Reddi, McMahan, and Smith, *Differentially Private Adaptive Optimization with Delayed Preconditioners*, ICLR 2023, arXiv:2212.00309, motivate delaying preconditioners, with a blockwise SGD/RMSProp hybrid and a different privacy/noise setting. That algorithm is **not** the present noiseless, every-step, one-lag recurrence. It neither states nor implies the exact two-cycle stability window proved here. Related spectral conclusions for other adaptive algorithms do not transfer across update rules without a conjugacy or implication, neither of which is present here.

## Limitations

This theorem concerns precisely the deterministic one-coordinate quadratic map with a one-step stale denominator; it is neither a statement about the ordinary current-memory RMSProp algorithm nor about the block-delayed DP2 algorithm. It proves local orbital stability/repulsion, not global basin dynamics, convergence for arbitrary initialization, or the presence or stability of any invariant curve beyond the loss-of-stability boundary. At the critical unit-modulus boundary, nonlinear behavior is unresolved, including the possible special low-order resonance for certain memory-decay values. Historical priority is assessed against inspected literature, not certified exhaustively.

## References

- K. Loh, J. Mireles-James, Z. Xu, and M. Tao, *The Dynamics of RMSProp Beyond the Stability Threshold*, arXiv:2610.30078v1, first publicly available 2026-10-21, https://arxiv.org/abs/2610.30078.
- T. Li, M. Zaheer, K. Z. Liu, S. J. Reddi, H. B. McMahan, and V. Smith, *Differentially Private Adaptive Optimization with Delayed Preconditioners*, ICLR 2023, arXiv:2212.00309, https://arxiv.org/abs/2212.00309.
