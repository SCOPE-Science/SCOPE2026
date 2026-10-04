# The smallest returning-interval instance where the square-root measurement is strictly suboptimal
## Finding
Consider the returning quantum change-interval model with a known anomalous interval length \(i=2\), three admissible translations \(N=3\), uniform prior, and local pure-state overlap \(0<c<1\). Put \(r=c^2\). The three hypothesis states have Gram matrix
\[
G=\begin{pmatrix}
1&r&r^2\\
r&1&r\\
r^2&r&1
\end{pmatrix}.
\]
Then the square-root measurement (SRM) is strictly suboptimal for every \(0<r<1\):
\[
P_{\mathrm{opt}}(G)>P_{\mathrm{SRM}}(G).
\]
Moreover, this is the coordinatewise smallest strict failure in the known-length returning-interval family. The one-site family \(i=1\) has exact finite-size SRM optimality for every \(N\), and every case with \(N\le2\) has at most two hypotheses and hence an optimal SRM.

## Assumptions and scope
The states are the calibrated pure-state interval hypotheses of Chen and Ma, with a phase convention making the local overlap nonnegative. Their exact Gram formula is
\[
(G_{N,i})_{ab}=r^{\min(|a-b|,i)},\qquad r=c^2.
\]
Only the finite instance \(i=2\), \(N=3\), and \(0<c<1\) is claimed here. The endpoints \(c=0\) and \(c=1\) are excluded from strictness: at \(c=0\) the hypotheses are orthogonal, while at \(c=1\) they coincide. No claim is made that the displayed rotated measurement is globally optimal; it only supplies a strict improvement over the SRM.

## Proof
For \(0<r<1\), the determinant is
\[
\det G=(1-r^2)^2>0,
\]
so the three hypotheses are linearly independent. Let
\[
S=G^{1/2}.
\]
An ensemble with the same Gram matrix can be represented canonically by the state vectors \(S e_j\) in \(\mathbb C^3\). For this canonical realization the SRM is exactly the orthonormal measurement \(\{e_1,e_2,e_3\}\), because the average state is \(G/3\).

Use the reflection-adapted basis
\[
e_s=\frac{e_1+e_3}{\sqrt2},\qquad e_a=\frac{e_1-e_3}{\sqrt2},\qquad e_2.
\]
The antisymmetric direction has eigenvalue \(1-r^2\). On \(\operatorname{span}\{e_s,e_2\}\), the Gram matrix is
\[
A=\begin{pmatrix}1+r^2&\sqrt2 r\\ \sqrt2 r&1\end{pmatrix}.
\]
Set
\[
s=\sqrt{1-r^2},\qquad D=\sqrt{2+r^2+2s}.
\]
Since \(\det A=s^2\), the positive square root of this two-dimensional block is
\[
A^{1/2}=\frac{A+sI}{D}.
\]
Transforming back to the original basis gives the two entries needed below:
\[
S_{12}=\frac{r}{D}
\]
and
\[
S_{11}-S_{22}
=\frac{s}{2}\left(1-\frac{1+s}{D}\right).
\]
The latter is strictly positive. Indeed,
\[
D^2-(1+s)^2=2r^2>0,
\]
so \(D>1+s\).

Now rotate only the first two SRM measurement vectors:
\[
\mu_1(\theta)=\cos\theta\,e_1+\sin\theta\,e_2,
\qquad
\mu_2(\theta)=-\sin\theta\,e_1+\cos\theta\,e_2,
\qquad
\mu_3(\theta)=e_3.
\]
This remains an orthonormal projective measurement for every real \(\theta\). Its success probability is
\[
P(\theta)=\frac13\sum_{j=1}^3
\left|\langle\mu_j(\theta),Se_j\rangle\right|^2.
\]
At \(\theta=0\), this is the SRM success probability. Differentiating at zero gives
\[
P'(0)=\frac23 S_{12}(S_{11}-S_{22})
=\frac{rs}{3D}\left(1-\frac{1+s}{D}\right)>0.
\]
Therefore \(P(\theta)>P(0)\) for all sufficiently small positive \(\theta\), and hence
\[
P_{\mathrm{opt}}(G)\ge P(\theta)>P_{\mathrm{SRM}}(G).
\]

Minimality follows from two exact boundaries. Chen and Ma prove finite-size SRM optimality for \(i=1\) for every \(N\). If \(N=1\) there is nothing to discriminate, and if \(N=2\) the equal-prior binary pure-state ensemble is geometrically uniform, so its SRM is the minimum-error measurement. Thus \((i,N)=(2,3)\) is the first possible pair in both coordinates where strict failure can occur, and the calculation above proves that it does occur for every nontrivial overlap.

## Verification
The accompanying script `artifacts/verify.py` evaluates the closed-form square-root entries for several representative values of \(r\), checks directly that their matrix square reproduces the Gram matrix to floating-point tolerance, and verifies the strictly positive derivative and an explicit small-angle increase in success probability. These computations corroborate the algebra but are not used to justify the universal quantifier over \(0<r<1\), which follows from the displayed inequalities.

## Relationship to prior work
Chen and Ma derive the exact Gram matrix for a returning interval, prove that for each fixed \(i\) the SRM becomes Bayes-optimal asymptotically, and bound the finite-size optimum-SRM gap by \(O_{i,c}(N^{-1/2})\). They also prove exact finite-size SRM optimality for \(i=1\). Their full text does not state whether the SRM is exactly optimal or strictly suboptimal at the first nontrivial fixed-length instance \(i=2\), \(N=3\). The result above closes that smallest finite-size boundary and shows that the fixed-length asymptotic theorem is genuinely asymptotic once the interval has two sites.

General SRM literature gives optimality criteria and identifies geometrically uniform ensembles where the SRM is minimum-error optimal. Eldar and Forney prove finite-size optimality for geometrically uniform pure-state sets, while Dalla Pozza and Pierobon give broader symmetry-based conditions. The three-state returning-interval ensemble here has only reflection symmetry and is not a transitive geometrically uniform orbit: the middle hypothesis is fixed by reflection while the two endpoint hypotheses are exchanged. The strict improvement is established directly by the rotation calculation rather than inferred from a failed sufficient criterion. The full multi-anomaly ensemble studied by Llorens, Sentís, and Muñoz-Tapia has a different Johnson-scheme symmetry and finite-size SRM optimality; Chen and Ma explicitly note that restricting to contiguous intervals removes that transitivity.

## Limitations
The theorem is a sharp minimal finite-size boundary statement, not a formula for the exact Bayes optimum at \(i=2\), \(N=3\), and not a claim that SRM is strictly suboptimal for every \(N\ge3\). The constructive rotation provides a strict local improvement but is not asserted to be globally optimal. A residual literature risk is that the same three-state Gram family may have been analyzed under a different communications label; the inspected state-discrimination and quantum-change sources did not state this returning-interval specialization.

## References
1. X. Chen and X. Ma, *Quantum Change Interval: Exact Asymptotics for Minimum Error Localization*, arXiv:2608.24543v2 (2026); first public version 2026-08-25.
2. Y. C. Eldar and G. D. Forney, Jr., *On Quantum Detection and the Square-Root Measurement*, IEEE Transactions on Information Theory 47, 858–872 (2001).
3. N. Dalla Pozza and G. Pierobon, *On the Optimality of Square Root Measurements in Quantum State Discrimination*, Physical Review A 91, 042334 (2015), arXiv:1504.04908.
4. S. Llorens, G. Sentís, and R. Muñoz-Tapia, *Quantum multi-anomaly detection*, Quantum 8, 1452 (2024).
