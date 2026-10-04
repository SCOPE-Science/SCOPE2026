# Sharp tolerance to antisymmetric endpoint detuning in missing-link complete-graph state transfer

## Finding

Consider the single-excitation \(XY\) Hamiltonian on the complete graph with one missing edge, \(K_n^{-}\), where the missing edge joins the input vertex \(i\) and output vertex \(j\). Use the source normalization in which every present edge contributes hopping \(2\), and let
\[
n\ge4.
\]

The source obtains perfect transfer by applying the same endpoint energy shift
\[
\Delta_i=\Delta_j=2n-6.
\]
Now keep the mean endpoint shift at this optimal value but allow a differential calibration error
\[
\Delta_i=2n-6+\frac{\delta}{2},
\qquad
\Delta_j=2n-6-\frac{\delta}{2},
\qquad
\delta\in\mathbb R.
\]

Then the exact maximum input-output transfer fidelity over all times is
\[
\boxed{
F_{\max}(n,\delta)
=
\left(
\frac{32(n-2)}
{32(n-2)+\delta^2}
\right)^2.
}
\]
All maximizing times are
\[
\boxed{
t_k
=
\frac{2(2k+1)\pi}
{\sqrt{32(n-2)+\delta^2}},
\qquad
k=0,1,2,\ldots.
}
\]

Consequently,
\[
F_{\max}=1
\quad\Longleftrightarrow\quad
\delta=0.
\]
Thus an arbitrarily small nonzero endpoint imbalance destroys exact perfect transfer, but its quantitative effect is sharply controlled.

For any required fidelity
\[
0<\eta\le1,
\]
the exact calibration window is
\[
\boxed{
F_{\max}\ge\eta
\quad\Longleftrightarrow\quad
|\delta|
\le
\sqrt{
32(n-2)
\left(
\eta^{-1/2}-1
\right)
}.
}
\]

For fixed differential error,
\[
1-F_{\max}(n,\delta)
=
\frac{\delta^2}{16(n-2)}
+
O(n^{-2})
\qquad
(n\to\infty).
\]
On the natural error scale
\[
\delta=c\sqrt n,
\]
one obtains the nontrivial limit
\[
\boxed{
\lim_{n\to\infty}
F_{\max}(n,c\sqrt n)
=
\left(
\frac{32}{32+c^2}
\right)^2.
}
\]

The absolute differential-detuning tolerance therefore grows like \(\sqrt n\), whereas exact perfect state transfer remains rigidly confined to zero mismatch.

## Assumptions and scope

The graph is the complete graph on \(n\) vertices with precisely the input-output edge deleted. The Hamiltonian is restricted to the single-excitation subspace and uses the source convention of hopping \(2\) on every present edge.

Only the endpoint diagonal energies are perturbed. Their mean is fixed at the source's optimal value \(2n-6\), and their difference is
\[
\delta=\Delta_i-\Delta_j.
\]
All other diagonal energies remain zero.

The result is deterministic and concerns a systematic antisymmetric endpoint calibration error. It is distinct from independent random frequency disorder on all sites.

## Proof

Introduce the normalized symmetry-adapted states
\[
|+\rangle
=
\frac{|i\rangle+|j\rangle}{\sqrt2},
\qquad
|-\rangle
=
\frac{|i\rangle-|j\rangle}{\sqrt2},
\]
and
\[
|r\rangle
=
\frac{1}{\sqrt{n-2}}
\sum_{v\ne i,j}|v\rangle.
\]
The subspace spanned by these three vectors is invariant and contains both the input and output states.

Write
\[
E_0=2n-6.
\]
In the ordered basis
\[
(|+\rangle,|-\rangle,|r\rangle),
\]
subtracting the irrelevant scalar \(E_0I\) leaves
\[
M=
\begin{pmatrix}
0 & \delta/2 & 2\sqrt{2(n-2)}\\
\delta/2 & 0 & 0\\
2\sqrt{2(n-2)} & 0 & 0
\end{pmatrix}.
\]
Set
\[
\Omega
=
\frac12
\sqrt{32(n-2)+\delta^2}.
\]
A direct multiplication gives
\[
M^3=\Omega^2 M.
\]
Therefore
\[
e^{-iMt}
=
I
-
i\frac{\sin(\Omega t)}{\Omega}M
+
\frac{\cos(\Omega t)-1}{\Omega^2}M^2.
\]

Since
\[
|i\rangle
=
\frac{|+\rangle+|-\rangle}{\sqrt2},
\qquad
|j\rangle
=
\frac{|+\rangle-|-\rangle}{\sqrt2},
\]
the transition amplitude simplifies to
\[
\langle j|e^{-iHt}|i\rangle
=
e^{-iE_0t}
\frac{16(n-2)}
{32(n-2)+\delta^2}
\left[
\cos(\Omega t)-1
\right].
\]
Hence
\[
F(t)
=
\left(
\frac{16(n-2)}
{32(n-2)+\delta^2}
\right)^2
\left[
1-\cos(\Omega t)
\right]^2.
\]

Because
\[
0\le 1-\cos(\Omega t)\le2,
\]
the global maximum is obtained exactly when
\[
\cos(\Omega t)=-1.
\]
This gives the displayed maximizing times and
\[
F_{\max}
=
\left(
\frac{32(n-2)}
{32(n-2)+\delta^2}
\right)^2.
\]

The exact target-fidelity condition follows by solving the preceding expression for \(|\delta|\).

For fixed \(\delta\), write
\[
x_n=\frac{\delta^2}{32(n-2)}.
\]
Then
\[
F_{\max}=(1+x_n)^{-2}
=
1-2x_n+O(x_n^2),
\]
which yields
\[
1-F_{\max}
=
\frac{\delta^2}{16(n-2)}
+
O(n^{-2}).
\]

Finally, for
\[
\delta=c\sqrt n,
\]
division by \(n\) in numerator and denominator gives
\[
F_{\max}
\longrightarrow
\left(
\frac{32}{32+c^2}
\right)^2.
\]

## Verification

`verify_endpoint_detuning.py` constructs the full source-normalized Hamiltonian action on the three symmetry-adapted vectors and verifies the reduced matrix entry by entry.

It independently evaluates the matrix exponential by a convergent power series and compares the resulting input-output probability with the closed formula for deterministic values of \(n\), \(\delta\), and \(t\).

It also checks the exact maximizing times, the target-fidelity inequality, the fixed-error asymptotic, and the \(\delta=c\sqrt n\) scaling limit.

The finite replay is supplementary. The global maximization is analytic because the exact time dependence reduces to a single cosine.

## Relationship to prior work

Casaccino, Lloyd, Mancini, and Severini solve the equal-endpoint-shift problem analytically for the complete graph and for the complete graph with the input-output edge removed. For the latter graph they identify
\[
\Delta_i=\Delta_j=2n-6
\]
as an exact perfect-transfer setting and give its transfer time.

The same paper studies disorder numerically by adding independent Gaussian fluctuations to site frequencies or couplings and averaging the transfer fidelity. That calculation does not give an exact deterministic law for unequal endpoint shifts.

The present result keeps the mean endpoint control at the published optimum but resolves a differential endpoint calibration error exactly. The symmetry breaking couples the bright and antisymmetric endpoint modes, yet the missing-link geometry leaves a three-level matrix satisfying a cubic closure relation. This produces a closed global fidelity maximum and an exact calibration window.

Later work on robustness of energy-landscape control studies sensitivity and uncertainty for optimized spin-network controllers, especially ring geometries. It motivates the robustness question but does not supply the missing-link complete-graph formula above.

Targeted searches for unequal endpoint shifts, antisymmetric endpoint detuning, frequency mismatch, and complete-graph-minus-edge state transfer did not locate an equivalent closed maximum-fidelity law.

## Limitations

The theorem fixes the mean endpoint shift at the published optimum. Simultaneous common-mode and differential calibration errors lead to a different reduced matrix and are not classified here.

The result assumes identical hopping \(2\) on every present edge. Coupling disorder is not included.

The \(\sqrt n\) robustness statement concerns absolute endpoint-energy mismatch in the source normalization; it is not a claim about every implementation or every noise model.

A residual literature risk remains because broader weighted-graph and robust-control treatments may contain an equivalent formula in another normalization even though targeted searches did not locate one.

## References

1. A. Casaccino, S. Lloyd, S. Mancini, and S. Severini, “Quantum state transfer through a qubit network with energy shifts and fluctuations,” arXiv:0904.4510, first submitted 28 April 2009; *International Journal of Quantum Information* 7 (2009), 1417–1427, DOI: 10.1142/S0219749909006085.
2. S. P. O'Neil, F. C. Langbein, E. Jonckheere, and S. Shermer, “Robustness of Energy Landscape Controllers for Spin Rings under Coherent Excitation Transport,” arXiv:2303.00142; *Research Directions: Quantum Technologies* 1 (2023), e12, DOI: 10.1017/qut.2023.5.
