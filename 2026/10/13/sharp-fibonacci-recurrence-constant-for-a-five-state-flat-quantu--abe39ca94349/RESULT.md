# Sharp Fibonacci recurrence constant for a five-state flat quantum kick

## Finding

Let \(A\) be the adjacency matrix of the cycle on five sites, and let \(U(t)=\exp(itA)\). Write \(\omega=\exp(2\pi i/5)\) and let \(E_0,E_1,E_2\) denote its mutually orthogonal spectral projectors, corresponding in order to the eigenvalues \(2\), \((\sqrt5-1)/2\) and \(-(\sqrt5+1)/2\). Set
\[
H=E_0+\omega E_1+\omega^4E_2,\qquad V(t)=e^{-2it}U(t),\qquad d(t)=\|V(t)-H\|_{\mathrm{op}}.
\]
The matrix \(H\) is a complex Hadamard unitary: every computational-basis entry has modulus \(1/\sqrt5\). The following *phase-anchored, target-specific* recurrence constant is exact:
\[
\boxed{\liminf_{t\longrightarrow\infty}t\,d(t)=\frac{4\pi^2}{25\sqrt5}=0.706211403259\ldots.}
\]
There is no finite time with \(d(t)=0\), but arbitrarily small errors occur. The upper liminf is attained along the explicit pulse lengths \(t_r=2\pi F_{4r}/5\), where \(F_j\) is the usual Fibonacci sequence. For \(\varepsilon\downarrow0\), the first positive time at error below \(\varepsilon\) is of order \(\varepsilon^{-1}\), with two strictly positive constant bounds. At these pulses all transition probabilities are within \(O(\varepsilon)\) of \(1/5\), since the target is flat.

## Assumptions and scope

All times are real and nonnegative; the nearest-neighbour Hamiltonian \(A\) has unit hopping coefficient. The operator norm is the matrix spectral norm. Anchoring means division by the eigenphase \(e^{2it}\) of the constant Fourier mode before measuring distance to the particular Gaussian-phase target \(H\). The result does not minimize over a free global phase, over other flat targets, or directly over probability-flatness defects. The first-time observable is \(T(\varepsilon)=\inf\{t\ge0:d(t)<\varepsilon\}\). The theorem's limits require \(t\to\infty\) or \(\varepsilon\downarrow0\), not a fixed finite search window.

## Proof

**1. Exact flat reference.** The Fourier spectral characters are indexed by residues \(j\in\mathbb Z/5\mathbb Z\); the eigenvalue of the character \(j\) is \(2\cos(2\pi j/5)\). The corresponding target eigenphase is \(\omega^{j^2}\), because \(j^2\) is \(0,1,4\) on the Fourier classes \(0,\pm1,\pm2\). Thus
\[
H_{xy}=\frac15\sum_{j=0}^4\omega^{j^2+j(x-y)}.
\]
The squared magnitude of the numerator is \(\sum_{h=0}^4\omega^{h^2+h(x-y)}\sum_{s=0}^4\omega^{2hs}=5\), as \(2\) is invertible modulo \(5\). Consequently \(|H_{xy}|^2=1/5\); unitarity also follows from its unit-modulus spectral phases.

**2. Reduction to one quadratic irrational.** Put
\[
a_1=\frac{\sqrt5-5}{2}<0,\quad a_2=\frac{-\sqrt5-5}{2}<0,\quad \alpha=\frac{1/\sqrt5-1}{2},\quad t_k=\frac{2\pi k}{5}.
\]
Since \(a_1+a_2=-5\), orthogonality of projectors gives
\[
d(t)=\max\{|e^{ia_1t}-\omega|,\ |e^{ia_2t}-\omega^4|\}.
\]
At integer sample \(t_k\), the two residual phases are opposite. With \(\|x\|_{\mathbb R/\mathbb Z}=\min_{m\in\mathbb Z}|x-m|\),
\[
d(t_k)=2\sin\!\left(\pi\left\|k\alpha-\frac15\right\|_{\mathbb R/\mathbb Z}\right).
\]
The congruence \(k\alpha-1/5\in\mathbb Z\) is impossible: it would make \(\sqrt5\) rational for \(k>0\), while \(k=0\) also fails. The same phase-sum argument shows no nonsampled \(t\) can satisfy both phases exactly. Quadratic irrational rotations are dense, so \(\inf d(t)=0\).

**3. Quantized Diophantine obstruction.** For integers \(k\ge1\) and \(m\), put \(N=5k+10m+2\). Direct multiplication gives
\[
10\left|k\alpha-\frac15-m\right|=|\sqrt5k-N|=\frac{|5k^2-N^2|}{\sqrt5k+N}
\]
whenever \(N>0\), which holds for the minimizing \(m\) and large \(k\). If \(k\) is even, \(N\equiv2\pmod{10}\); if odd, \(N\equiv7\pmod{10}\). Hence in both cases \(N^2-5k^2\equiv4\pmod{20}\). This integer is never zero and has absolute value at least \(4\). Therefore
\[
\liminf_{k\to\infty} k\left\|k\alpha-\frac15\right\|_{\mathbb R/\mathbb Z}\ge\frac1{5\sqrt5}.
\]
For \(k=F_{4r}\) and \(N=L_{4r}\), with \(L_j\) the Lucas numbers, the identities \(L_{4r}^2-5F_{4r}^2=4\) and \(L_{4r}-5F_{4r}\equiv2\pmod{10}\) hold. They follow from Binet's formulas and the Fibonacci recurrences (or directly by induction in steps of four). This chooses an admissible \(m\) with the minimal integer norm \(4\), yielding equality in the limiting bound. The sampled-time limit follows:
\[
\liminf_{k\to\infty} t_kd(t_k)=\frac{2\pi}{5}\cdot2\pi\cdot\frac1{5\sqrt5}=\frac{4\pi^2}{25\sqrt5}.
\]

**4. No nonsampled improvement in the limit.** Consider a sequence \(t\to\infty\) for which \(t\,d(t)\) remains bounded; necessarily \(d(t)\to0\). Choose the unique small real phase residuals \(u=a_1t-2\pi/5-2\pi m_1\) and \(v=a_2t-8\pi/5-2\pi m_2\). Since their sum is \(-5t\) modulo \(2\pi\), there is a positive integer \(k\) such that \(t=t_k+h\) with \(|h|=O(d(t))\). At \(t_k\), the residuals are \(e\) and \(-e\), where \(e=2\pi(k\alpha-1/5-m)\) is the small representative; thus
\[
u=e+a_1h,\qquad v=-e+a_2h.
\]
As \(a_1,a_2<0\), when \(e>0\) any \(h>0\) makes the second residual more negative, while any \(h<0\) makes the first more positive. When \(e<0\), any \(h>0\) makes the first more negative, while any \(h<0\) makes the second more positive. Equivalently, \(\max(|u|,|v|)\ge|e|\). Because both residuals are small, the chord-length map is monotone, giving \(d(t)\ge d(t_k)\). Also \(t/t_k\to1\). The sampled lower limit is therefore a lower limit for arbitrary real times; the Fibonacci sequence supplies the matching upper limit. This proves the boxed equality.

**5. First-hit order.** The positive lower liminf, together with absence of any finite exact hit and compactness of bounded time intervals, yields \(T(\varepsilon)\ge c/\varepsilon\) for small \(\varepsilon\). For the upper bound, the quadratic irrational \(\alpha\) has bounded continued-fraction partial quotients. Given a convergent denominator \(q\), the residues \(\{k\alpha\}\) for \(0\le k<q\) lie within \(1/q\) of the full rational grid \(\{j/q\}\), because the convergent differs by less than \(1/(qq')\), where \(q'\) is the next denominator. Hence every target on the circle, including \(1/5\), is within \(3/(2q)\) of one of these residues. Bounded quotients permit a choice \(q=O(1/\varepsilon)\) with \(q\ge C/\varepsilon\). Then the corresponding \(k<q\) gives \(d(t_k)<\varepsilon\), proving \(T(\varepsilon)\le C'/\varepsilon\). No uniform-optimality claim for other targets is used.

## Verification

Run `python3 verify.py` using Python's standard library. It independently constructs the five-mode Fourier matrices, checks all \(25\) Gaussian-sum flatness identities, computes spectral evolution on seven unrelated times and confirms row normalization, verifies Lucas/Fibonacci norm and congruence identities, and checks the integer norm obstruction over \(599\) sample integers. It reports the finite-check outcome and sharp constant. These checks do not replace the infinite-time limiting argument above.

## Relationship to prior work

Godsil–Mullin–Roy (2017), Section 9, defines exactly this flat spectral target and proves that every prime cycle can approach it arbitrarily closely by Kronecker's theorem. Its qualitative existence theorem is **not** new here; the present result resolves the *sharp target-specific time–error liminf constant* and an optimal-order first-hit bound for the first nontrivial prime cycle. The current generalized kicked-Ising study of Pathak–Ebisu–Prosen (2026) identifies the kick \(\exp[-ib(X+X^\dagger)]\) and the special role of flatness for dual-unitarity in higher local dimension; our sign convention corresponds to \(b=-t\). Cao–Zhu (2026) treats exact/nonexact mixing of other cycles and \(\varepsilon\)-mixing for prime-square cycles, not the exact five-cycle rate coefficient. Existing quantum-walk mixing-time studies under stochastic decoherence use a different observable and are not contradicted. No exact general optimal mixing time, probability-flatness lower bound, or full dual-unitary many-body result is claimed.

## Limitations

The constant depends on the fixed spectral phase gauge and on the specified five-dimensional Gaussian-phase Hadamard gate; it is **not** a claim about phase-optimized distance, all possible flat targets, or the earliest approximately uniform *probability* profile. Quantities at moderate times may differ significantly from the limiting coefficient. A latent earlier arithmetic specialization of the 2017 construction may exist; the source comparison establishes no universal originality guarantee. The integer norm certificate proves the liminf but not a complete list of all near-optimal pulse times.

## References

1. C. Godsil, N. Mullin and A. Roy, “Uniform Mixing and Association Schemes,” *Electronic Journal of Combinatorics* **24**(3), P3.22 (2017), especially Lemma 9.1 and Theorem 9.2. https://www.combinatorics.org/ojs/index.php/eljc/article/download/v24i3p22/pdf
2. T. Pathak, H. Ebisu and T. Prosen, “Spread of Entanglement in Generalized Kicked Ising Chain,” arXiv:2608.09695v1 (first posted August 10, 2026), Section III. https://arxiv.org/abs/2608.09695
3. X. Cao and C. Zhu, “Uniform mixing and \(\varepsilon\)-uniform mixing on cycles,” arXiv:2607.04207v1 (first posted July 5, 2026), Sections 4–5. https://arxiv.org/abs/2607.04207
