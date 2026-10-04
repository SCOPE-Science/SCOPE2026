# Exact short-time entropy maximizers in the symmetric SU(2) quantum walk

## Finding

Consider the one-dimensional discrete-time quantum walk with coin basis \(|0\rangle,|1\rangle\), conditional shift
\[
|0,x\rangle\mapsto|0,x-1\rangle,
\qquad
|1,x\rangle\mapsto|1,x+1\rangle,
\]
initial state
\[
|\Psi_{\mathrm{in}}\rangle
=
\frac{|0\rangle+i|1\rangle}{\sqrt2}\otimes|0\rangle,
\]
and one-parameter coin
\[
U_\theta=U_{0,\theta,0}
=
\begin{pmatrix}
\cos\theta&\sin\theta\\
\sin\theta&-\cos\theta
\end{pmatrix},
\qquad
0\le\theta\le\frac\pi2.
\]
Let \(H_n(\theta)\) be the base-two Shannon entropy of the position distribution after \(n\) steps.

At two steps the exact distribution is
\[
p_2(-2)=p_2(2)=\frac{\cos^2\theta}{2},
\qquad
p_2(0)=\sin^2\theta.
\]
Therefore
\[
\boxed{\theta_2^*=\arcsin\!\left(\frac1{\sqrt3}\right)}
\]
is the unique maximizer on \([0,\pi/2]\). At this angle the distribution is exactly uniform on the three accessible sites, so
\[
\boxed{H_2(\theta_2^*)=\log_2 3.}
\]
For the Hadamard value \(\theta=\pi/4\),
\[
(p_2(-2),p_2(0),p_2(2))
=
\left(\frac14,\frac12,\frac14\right),
\]
and hence
\[
H_2\!\left(\frac\pi4\right)=\frac32<\log_2 3.
\]

At three steps the exact distribution is
\[
p_3(-3)=p_3(3)=\frac{\cos^4\theta}{2},
\qquad
p_3(-1)=p_3(1)=\frac{1-\cos^4\theta}{2}.
\]
Therefore
\[
\boxed{\theta_3^*=\arccos(2^{-1/4})}
\]
is the unique maximizer. At this angle all four accessible positions have probability \(1/4\), and
\[
\boxed{H_3(\theta_3^*)=2.}
\]
At the Hadamard angle the four probabilities are
\[
\left(\frac18,\frac38,\frac38,\frac18\right),
\]
so
\[
H_3\!\left(\frac\pi4\right)
=
3-\frac34\log_2 3
<2.
\]

Both exact entropy-maximizing angles satisfy
\[
\theta_3^*<\theta_2^*<\frac\pi4.
\]
At one step the symmetric initial coin state gives position probabilities \((1/2,1/2)\) independently of \(\theta\). Thus \(n=2\) is the earliest nontrivial time at which the Hadamard coin is strictly suboptimal for position-measurement entropy.

## Assumptions and scope

The walk, initial state, and coin convention are exactly those used in the symmetric one-dimensional walk studied by Chandrashekar, Srikanth, and Laflamme and subsequently discussed by Ide, Konno, and Machida. The quantity optimized here is the Shannon entropy of the position measurement, not coin-position entanglement entropy.

The theorem concerns the exact finite times \(n=1,2,3\). It does not assert a formula for the entropy-maximizing coin at arbitrary \(n\), and it does not contradict large-time or asymptotic entropy results. In particular, numerical behavior at tens or hundreds of steps may differ from these short-time exact optimizers.

## Proof

Write
\[
c=\cos\theta,
\qquad
s=\sin\theta.
\]
After one coin toss and shift, direct multiplication gives
\[
|\Psi_1\rangle
=
\frac{c+is}{\sqrt2}|0,-1\rangle
+
\frac{s-ic}{\sqrt2}|1,+1\rangle.
\]
Both coefficients have modulus squared \(1/2\), so
\[
H_1(\theta)=1
\]
for every \(\theta\).

Apply the coin and shift once more. The two outer positions receive only one path each, while the two paths arriving at the origin occupy orthogonal coin states. Their probabilities are
\[
p_2(-2)=\frac{c^2}{2},
\qquad
p_2(0)=s^2,
\qquad
p_2(2)=\frac{c^2}{2}.
\]
A probability distribution on three points has entropy at most \(\log_2 3\), with equality exactly for the uniform distribution. Uniformity here is equivalent to
\[
s^2=\frac13,
\qquad
c^2=\frac23.
\]
Because \(\sin^2\theta\) is strictly increasing on \([0,\pi/2]\), this gives the unique maximizer
\[
\theta_2^*=\arcsin(1/\sqrt3).
\]
At \(\theta=\pi/4\), the displayed \((1/4,1/2,1/4)\) distribution gives entropy \(3/2\).

For the third step, direct propagation from the two-step amplitudes gives the outer-site probabilities
\[
p_3(-3)=p_3(3)=\frac{c^4}{2}.
\]
Normalization and left-right symmetry give
\[
p_3(-1)=p_3(1)=\frac{1-c^4}{2}.
\]
A four-point distribution has entropy at most \(2\), with equality exactly when all four probabilities are \(1/4\). Hence
\[
\frac{c^4}{2}=\frac14,
\]
so
\[
c^4=\frac12,
\qquad
\theta_3^*=\arccos(2^{-1/4}).
\]
Since \(\cos\theta\) is strictly decreasing on \([0,\pi/2]\), this maximizer is unique.

At \(\theta=\pi/4\), one has \(c^4=1/4\), giving
\[
\left(\frac18,\frac38,\frac38,\frac18\right).
\]
Its entropy is
\[
-2\cdot\frac18\log_2\frac18
-2\cdot\frac38\log_2\frac38
=
3-\frac34\log_2 3.
\]
Finally,
\[
\sin^2\theta_2^*=\frac13<\frac12=\sin^2\frac\pi4
\]
and
\[
\cos^4\theta_3^*=\frac12>\frac14=\cos^4\frac\pi4,
\]
so both exact maximizers lie strictly below \(\pi/4\).

## Verification

`verify_short_time_entropy.py` independently implements the coin and conditional shift with complex amplitudes. It checks the closed position-distribution formulas at \(101\) deterministic values of \(\theta\), verifies the exact uniform distributions at \(\theta_2^*\) and \(\theta_3^*\), reproduces the two Hadamard entropy values, and performs a dense finite-grid stress test around both unique maximizers.

The grid is supplementary. The global optimality statements follow from the information-theoretic entropy bound and the exact uniformizing parameters proved above.

## Relationship to prior work

Chandrashekar, Srikanth, and Laflamme introduced this symmetric walk and coin parametrization as a framework for tuning one-dimensional discrete-time quantum walks. In their measurement-entropy discussion they state that the Hadamard coin \(\theta=\pi/4\) has maximum uncertainty and therefore maximum measurement entropy. The entropy plot used to support that discussion is for much larger times: \(50\), \(100\), \(250\), and \(500\) steps.

Their published erratum corrects the general unitary parametrization and one displayed equation, while explicitly stating that the figures and conclusions are unaffected. It does not address the short-time entropy-maximization statement.

Ide, Konno, and Machida later summarize the same numerical conclusion more explicitly, saying that the position entropy is suggested to be increasing on \([0,\pi/4]\) and decreasing on \([\pi/4,\pi/2]\) for any \(n\). The exact two- and three-step distributions above show that this finite-time statement is false: the first strict failure occurs already at \(n=2\), and at both \(n=2\) and \(n=3\) a non-Hadamard coin attains the absolute entropy upper bound by making the accessible positions exactly uniform.

The result does not challenge the long-time entanglement analysis in the later paper or the possibility that Hadamard is distinguished in an asymptotic regime. It only resolves the finite-time universal statement at the earliest nontrivial steps.

## Limitations

Only the first three step numbers are classified. No claim is made that the sequence of finite-time entropy maximizers has a simple closed form for all \(n\), or that the short-time maximizers describe the large-\(n\) limit.

The result uses the specific symmetric initial coin state from the cited model. Other initial coin states can alter the position distribution and its entropy optimizer.

A residual literature risk remains because short-time walk distributions are elementary to derive and an equivalent observation may exist in unindexed notes, numerical studies, or a different coin-angle convention. Targeted searches did not locate the exact angles \(\arcsin(1/\sqrt3)\) and \(\arccos(2^{-1/4})\) as entropy maximizers for this model.

## References

1. C. M. Chandrashekar, R. Srikanth, and R. Laflamme, “Optimizing the discrete time quantum walk using a SU(2) coin,” *Physical Review A* 77, 032326 (2008), arXiv:0711.1882, DOI: 10.1103/PhysRevA.77.032326.
2. C. M. Chandrashekar, R. Srikanth, and R. Laflamme, “Erratum: Optimizing the discrete time quantum walk using a SU(2) coin,” *Physical Review A* 82, 019902 (2010), DOI: 10.1103/PhysRevA.82.019902.
3. Y. Ide, N. Konno, and T. Machida, “Entanglement for discrete-time quantum walks on the line,” *Quantum Information and Computation* 11 (2011), 855–866, arXiv:1012.4164.
