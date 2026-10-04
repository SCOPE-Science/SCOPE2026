# The canonical rank-one AQEC comparator is never fixed-noise stationary
## Finding
For the approximate quantum error-correction family introduced in arXiv:2609.00778v1, let \(d\ge 2\) be the logical dimension and \(0<p<1\) the noise parameter. Consider the paper's canonical rank-one encoder obtained by polar-normalizing \(Q_p(I\otimes |0\rangle)\), together with its partial-trace decoder. This encoder-decoder pair is not a stationary point of the rank-one entanglement-fidelity objective at any fixed positive noise strength.

More explicitly, define
\[
\lambda_1=1-\frac{p}{d^2-2},\qquad
\lambda_4=\frac{d^2-1+p}{d^2},\qquad
\lambda_5=\frac{1-p}{d^2},
\]
\[
\lambda_2=\frac{(1-\lambda_1)(d^2\lambda_1-1)}{d^2\lambda_4},\qquad
\lambda_3=\frac{2(1-\lambda_1)^2}{d^2\lambda_4},
\]
and
\[
a=\sqrt{\frac{d\lambda_4}{d^2-1}},\quad b=\sqrt{d\lambda_5},\quad
c=\frac{b-a}{d},\quad g=\frac{d+1-p}{d(d+1)}.
\]
The canonical encoder belongs to the isometric path
\[
V_\theta|0\rangle=\cos\theta\,|00\rangle+\frac{\sin\theta}{\sqrt{d-1}}\sum_{j=1}^{d-1}|jj\rangle,
\qquad
V_\theta|j\rangle=|j0\rangle\quad(1\le j<d),
\]
at the angle \(\theta=\theta_p\) determined by
\[
\cos\theta_p=\frac{a+c}{\sqrt g},\qquad
\sin\theta_p=\frac{\sqrt{d-1}\,c}{\sqrt g}.
\]
If \(F_p(\theta)\) is the entanglement fidelity obtained from \(V_\theta\) and the same partial-trace decoder, then
\[
F_p'(\theta_p)>0.
\]
Consequently, every sufficiently small positive displacement \(\theta_p\mapsto\theta_p+\delta\) improves the paper's canonical rank-one pair at the same fixed \(p\).

## Assumptions and scope
The claim uses exactly the finite-dimensional noise family and normalization in arXiv:2609.00778v1. The logical dimension is any integer \(d\ge2\); the parameter range is \(0<p<1\). The endpoint \(p=0\), where the perturbative problem degenerates to exact correction, is excluded. The theorem disproves fixed-\(p\) exact optimality of the displayed canonical rank-one pair; it does not identify the globally optimal rank-one encoder, determine \(F_1^{\mathrm{opt}}\), or compute the full higher-order optimized high-rank gap.

## Proof
Let \(|\psi\rangle=d^{-1/2}\sum_j|jj\rangle\), \(\pi=|\psi\rangle\langle\psi|\), and
\[
Q_p=a(I-\pi)+b\pi.
\]
For \(C=Q_p(I\otimes|0\rangle)\), direct evaluation gives
\[
C|0\rangle=(a+c)|00\rangle+c\sum_{j=1}^{d-1}|jj\rangle,
\qquad
C|j\rangle=a|j0\rangle\quad(j\ge1),
\]
with
\[
C^\dagger C=\operatorname{diag}(g,a^2,\ldots,a^2).
\]
Thus the polar-normalized isometry in the source is exactly \(V_{\theta_p}\) above.

For the partial-trace decoder define
\[
w(\theta)=\frac{\cos\theta+\sqrt{d-1}\sin\theta}{\sqrt d},
\]
\[
T(\theta)=(d-1)a+a\cos\theta+\frac{b-a}{\sqrt d}\,w(\theta).
\]
Evaluating the Kraus traces in the source channel gives the exact one-variable fidelity
\[
F_p(\theta)=\lambda_3+\frac{\lambda_1-\lambda_3}{d}T(\theta)^2
+\frac{\lambda_2}{d\lambda_4}
\left(w(\theta)-\sqrt{\lambda_5}\,T(\theta)\right)^2.
\]
The cosine-sine coefficient vector in \(T\) is
\[
\left(a+c,\sqrt{d-1}\,c\right)=\sqrt g\left(\cos\theta_p,\sin\theta_p\right),
\]
so \(T'(\theta_p)=0\). Moreover,
\[
w'(\theta_p)=\frac{\sqrt{d-1}\,a}{\sqrt d\sqrt g}>0,
\quad
w(\theta_p)=\sqrt{\frac{\lambda_5}{g}},
\quad
T(\theta_p)=(d-1)a+\sqrt g.
\]
Hence
\[
F_p'(\theta_p)=\frac{2\lambda_2}{d\lambda_4}
\left(w(\theta_p)-\sqrt{\lambda_5}T(\theta_p)\right)w'(\theta_p).
\]
All prefactors are positive for \(d\ge2\) and \(0<p<1\). The remaining factor is
\[
w(\theta_p)-\sqrt{\lambda_5}T(\theta_p)
=\sqrt{\lambda_5}\left(\frac{1-g}{\sqrt g}-(d-1)a\right).
\]
Both terms being compared are positive, and squaring is legitimate. Exact simplification yields
\[
(1-g)^2-(d-1)^2a^2g
=\frac{p(d^2-1+p)}{d(d+1)^2}>0.
\]
Therefore \(F_p'(\theta_p)>0\), proving strict local improvability for every allowed \(d\) and \(p\).

## Verification
The accompanying `artifacts/verify.py` reconstructs the source parameters, checks the closed scalar fidelity against a direct Kraus-matrix calculation for several dimensions and noise strengths, and verifies the decisive rational identity exactly for multiple rational \(p\) values and dimensions. These finite checks corroborate the symbolic proof; they are not used as an infinite-dimensional or all-parameter certificate.

## Relationship to prior work
Li and Jiang construct the high-rank noise family, the polar-normalized rank-one comparator, and the quadratic small-noise separation from rank-one encoders. Their supplement explicitly states that higher-order corrections to the rank-one optimum are undetermined, that no closed form for the exact rank-one optimum is obtained, and that exact optimality of the displayed comparator pair at fixed positive \(p\) remains open. The present calculation answers that last question negatively: the displayed pair is never even stationary once \(p>0\).

Earlier iterative AQEC optimization work provides numerical and variational machinery for improving encoders and decoders, while general fidelity/channel-capacity results motivate restricted encoding classes. Neither supplies the source-specific all-\(d\), all-\(p\) derivative identity above.

## Limitations
This result is local and comparative. It does not solve the global fixed-noise rank-one optimization problem, does not determine the optimal decoder after moving the encoder, and does not change the source's leading small-noise high-rank advantage. It only establishes that the canonical rank-one comparator used there cannot be the exact finite-noise optimum for any \(0<p<1\).

## References
1. B. Li and L. Jiang, *High-Rank Encoding Can Improve Approximate Quantum Error Correction*, arXiv:2609.00778v1 (2026).
2. M. Reimpell and R. F. Werner, *Iterative Optimization of Quantum Error Correcting Codes*, arXiv:quant-ph/0307138.
3. H. Barnum, E. Knill, and M. A. Nielsen, *On Quantum Fidelities and Channel Capacities*, arXiv:quant-ph/9809010.
