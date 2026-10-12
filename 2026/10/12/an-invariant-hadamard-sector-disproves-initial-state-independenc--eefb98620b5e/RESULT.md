# An invariant Hadamard sector disproves initial-state independence for a nonreversal quantum walk

## Finding

Consider the square-lattice nonreversal quantum walk defined in “Nonreversal and nonrepeating quantum walks,” arXiv:1303.1966. Choose its admissible parameters
\[
\lambda=\frac1{\sqrt2},\qquad \gamma=0,
\]
with all six coin phases equal to zero. The resulting coin is
\[
C_{\mathrm{rev}}=\frac1{\sqrt2}
\begin{pmatrix}
1&0&1&0\\
0&-1&0&1\\
1&0&-1&0\\
0&1&0&1
\end{pmatrix}.
\]
It preserves the two-dimensional sector
\[
\mathcal H_0=\operatorname{span}\{|x+\rangle,|y-\rangle\},
\]
and, in the ordered basis \((|x+\rangle,|y-\rangle)\), its restriction is exactly
\[
H=\frac1{\sqrt2}
\begin{pmatrix}
1&1\\
1&-1
\end{pmatrix}.
\]

Let \((X_t,Y_t)\) be the lattice position after \(t\) steps. For states remaining in \(\mathcal H_0\), set \(Z_t=X_t+Y_t\). Every step is either \(x+\) or \(y-\), so pathwise
\[
X_t=\frac{t+Z_t}{2}.
\]
The embedded process \(Z_t\) is the standard one-dimensional Hadamard walk. Its weak-limit moments give, for initial coin \(|x+\rangle\),
\[
\lim_{t\to\infty}\frac{\mathbb E[Z_t]}{t}=I,
\qquad
\lim_{t\to\infty}\frac{\mathbb E[Z_t^2]}{t^2}=I,
\]
and for initial coin \(|y-\rangle\),
\[
\lim_{t\to\infty}\frac{\mathbb E[Z_t]}{t}=-I,
\qquad
\lim_{t\to\infty}\frac{\mathbb E[Z_t^2]}{t^2}=I,
\]
where
\[
I=\frac1{2\pi}\int_{-\pi}^{\pi}\frac{\cos^2 k}{1+\cos^2 k}\,dk
=1-\frac1{\sqrt2}.
\]
Consequently,
\[
\boxed{\lim_{t\to\infty}\frac{\mathbb E[X_t^2]}{t^2}=1-\frac{3\sqrt2}{8}}
\]
for initial coin \(|x+\rangle\), while
\[
\boxed{\lim_{t\to\infty}\frac{\mathbb E[X_t^2]}{t^2}=\frac{\sqrt2}{8}}
\]
for initial coin \(|y-\rangle\). Their difference is
\[
1-\frac1{\sqrt2}>0.
\]
Thus the source paper's numerically motivated conjecture that all even-total-degree joint moments of the nonreversal walk are independent of the initial coin state is false. The failure occurs in the leading ballistic coefficient of the second moment, rather than only at finite time.

## Assumptions and scope

The walk, direction basis, and nonreversal coin family are those of arXiv:1303.1966. The parameter point above is admissible because the source allows \(0\le \gamma^2+\lambda^2\le1\). It lies on the boundary subfamily \(\gamma=0\), so it has measure zero under any absolutely continuous random sampling of the two real coin parameters. This explains why a large random scan can miss the obstruction without implying that the numerical work was incorrectly executed.

The statement compares two pure initial coin states at the origin. It concerns the asymptotic coefficient of the Cartesian moment \(\mathbb E[X_t^2]\). It does not claim that the conjecture fails for generic parameter choices, for all strictly interior coins, for radial moments, or for every even joint moment.

## Proof

The displayed matrix follows by substituting \(\lambda=1/\sqrt2\), \(\gamma=0\), and zero phases into the source's nonrepeating coin and then applying its reversal permutation. Direct multiplication gives
\[
C_{\mathrm{rev}}^{\dagger}C_{\mathrm{rev}}=I_4,
\qquad
\det C_{\mathrm{rev}}=1.
\]
The first and third basis vectors are coupled only to each other, and the second and fourth are coupled only to each other. In particular, on \(\mathcal H_0=\operatorname{span}\{|x+\rangle,|y-\rangle\}\) the coin is the two-state Hadamard matrix \(H\).

Let \(N_+\) and \(N_-\) be the numbers of \(x+\) and \(y-\) steps along a path in this sector. Then
\[
t=N_++N_-,\qquad Z_t=N_+-N_-,\qquad X_t=N_+=\frac{t+Z_t}{2}.
\]
Therefore
\[
\frac{X_t^2}{t^2}
=\frac14+\frac12\frac{Z_t}{t}+\frac14\frac{Z_t^2}{t^2}.
\]

For completeness, the needed one-dimensional Hadamard moments can be recovered directly in Fourier space. With Fourier convention
\[
\widehat\psi(k)=\sum_z\psi(z)e^{-ikz},
\]
the one-step matrix is
\[
U(k)=\operatorname{diag}(e^{-ik},e^{ik})H.
\]
Write its two eigenvalues as \(e^{-i\omega(k)}\) and \(-e^{i\omega(k)}\), where
\[
\sin\omega(k)=\frac{\sin k}{\sqrt2}.
\]
The group velocity is
\[
v(k)=\omega'(k)=\frac{\cos k}{\sqrt{1+\cos^2 k}}.
\]
If \(P_+(k)\) and \(P_-(k)\) are the two spectral projectors, the elementary two-by-two projector identity gives
\[
\langle0|(P_+-P_-)|0\rangle=v(k),
\qquad
\langle1|(P_+-P_-)|1\rangle=-v(k).
\]
The standard compactly supported weak-limit calculation for coined walks therefore yields
\[
\lim_{t\to\infty}\frac{\mathbb E[Z_t]}t=\pm I,
\qquad
\lim_{t\to\infty}\frac{\mathbb E[Z_t^2]}{t^2}=I,
\]
with the plus sign for initial \(|0\rangle\) and the minus sign for initial \(|1\rangle\), and
\[
I=\frac1{2\pi}\int_{-\pi}^{\pi}v(k)^2\,dk.
\]
Since
\[
\frac{\cos^2 k}{1+\cos^2 k}=1-\frac1{1+\cos^2 k},
\]
and the standard trigonometric integral gives
\[
\frac1{2\pi}\int_{-\pi}^{\pi}\frac{dk}{1+\cos^2 k}=\frac1{\sqrt2},
\]
we obtain \(I=1-1/\sqrt2\). The bounded support \(|Z_t/t|\le1\) justifies passage from weak convergence to these first two moments.

Substitution into the identity for \(X_t^2/t^2\) gives
\[
\frac{1+3I}{4}=1-\frac{3\sqrt2}{8}
\]
for initial \(|x+\rangle\), and
\[
\frac{1-I}{4}=\frac{\sqrt2}{8}
\]
for initial \(|y-\rangle\). This proves the stated asymptotic separation.

## Verification

The bundled checker verifies using exact integer and rational arithmetic that the scaled four-state coin is orthogonal with determinant one, that the stated Hadamard sector is invariant, and that finite-time one-dimensional Hadamard moments have the required reflection identities. It also verifies the final radical identities numerically to high precision. Running `python3 verify.py` prints `VERIFY_OK`.

The proof itself does not infer an infinite-time statement from the finite checks. The asymptotic step is the analytic Fourier weak-limit calculation given above and is also a standard consequence of the cited one-dimensional quantum-walk limit theorems.

## Relationship to prior work

The source paper proves initial-state independence of even-total-degree asymptotic moments for its nonrepeating walk and then states a conjecture that the same phenomenon holds for the nonreversal walk. For the nonreversal case it reports numerical tests over hundreds of coins and roughly a thousand initial states per coin, and says that all tested even-total-degree joint moments appeared independent of the initial condition. The present parameter choice belongs to the same nonreversal family but exposes an invariant Hadamard block on the boundary \(\gamma=0\), yielding an exact counterexample at degree two.

The one-dimensional Hadamard weak limit itself is classical; it is used here as a reduction tool, not claimed as new. Later work using the nonrepeating coin for state transfer addresses a different walk family and objective, and does not imply the present nonreversal moment statement.

## Limitations

The counterexample lies on the admissible boundary \(\gamma=0\). No conclusion is drawn about a generic nonreversal coin or about whether a corrected conjecture may hold under an explicit nondegeneracy condition such as \(\gamma\lambda\ne0\). The result also does not address the source's proven nonrepeating-walk moment theorem.

Only the second Cartesian moment is needed to refute the universal nonreversal conjecture. Higher moments and the full set of exceptional parameter strata are not classified here.

## References

1. “Nonreversal and nonrepeating quantum walks,” arXiv:1303.1966; DOI:10.1103/PhysRevA.89.042332. First public arXiv version: 2013-03-08.
2. N. Konno, “Quantum Random Walks in One Dimension,” arXiv:quant-ph/0206103, later published in *Quantum Information Processing* 1 (2002), 345–354.
3. G. Grimmett, S. Janson, and P. F. Scudo, “Weak limits for quantum random walks,” arXiv:quant-ph/0309135, *Physical Review E* 69, 026119 (2004).
