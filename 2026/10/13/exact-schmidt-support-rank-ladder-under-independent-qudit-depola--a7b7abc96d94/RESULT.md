# Exact Schmidt-support rank ladder under independent qudit depolarization
## Finding
A controlled-shift gate converts coherence in one \(d\)-level quantum system, with an incoherent ancilla initially in \(|0\rangle\), into bipartite entanglement. If the input is uniformly coherent on \(k\) of the \(d\) basis states, the ideal output is
\[
|\Phi_{d,k}\rangle=\frac1{\sqrt{k}}\sum_{j=0}^{k-1}|jj\rangle,
\qquad 1\le k\le d.
\]
These states interpolate naturally between a product input, rank-two entanglement, and a fully maximally entangled pair of \(d\)-level systems.

In contrast with global depolarization of the composite system, apply an independent local depolarizing channel to each output system:
\[
\mathcal D_p(X)=(1-p)X+\frac p d\operatorname{Tr}(X)I_d,
\qquad
\mathcal D_q(X)=(1-q)X+\frac q d\operatorname{Tr}(X)I_d,
\]
where \(d\ge3\) is an integer and \(p,q\in[0,1]\). Write
\[
\rho_{d,k;p,q}=(\mathcal D_p\otimes\mathcal D_q)
(|\Phi_{d,k}\rangle\langle\Phi_{d,k}|),
\quad
\mathcal N(\rho)=\frac{\|\rho^{T_B}\|_1-1}{2}.
\]
Set
\[
\Delta=d^2(1-p)(1-q)-d[p(1-q)+q(1-p)],
\qquad\Pi=pq.
\]
The exact negativity of the flat-support rank-\(k\) conversion is
\[
\boxed{\mathcal N_k=\frac{k-1}{2d^2}[\Delta-k\Pi]_+},
\qquad [u]_+=\max\{u,0\}.
\]

This formula yields the complete noise-dependent optimum **within the family of all \(d\) uniform-on-support inputs**, not among every possible Schmidt spectrum. If \(\Pi>0\) and \(\Delta\le2\Pi\), every such input has zero negativity. If \(\Pi>0\) and \(\Delta>2\Pi\), the maximum is positive and the maximizing rank is determined by the adjacent-score difference
\[
(k)(\Delta-(k+1)\Pi)-(k-1)(\Delta-k\Pi)
=\Delta-2k\Pi.
\]
In particular, the unique maximizer decreases as the noise parameters cross successive surfaces
\[
\boxed{\Delta=2k\Pi},\qquad 2\le k<d.
\]
At such a surface, precisely ranks \(k\) and \(k+1\) tie for the positive maximum; away from all surfaces the positive maximizer is unique. If \(\Pi=0\) and \(\Delta>0\), rank \(d\) is the unique maximizer; when \(\Pi=0\) and \(\Delta\le0\), every negativity is zero.

For equal local noise \(p=q=t\in(0,1)\), every support rank occurs as a unique optimum over a nonempty open interval. The switch between ranks \(k+1\) and \(k\) occurs exactly at
\[
\boxed{t_k=\frac d{d+1+\sqrt{2k+1}}},
\qquad 2\le k<d.
\]
As \(t\) increases from zero, the maximizing rank visits \(d,d-1,\ldots,2\), before all outputs in the family become PPT at
\[
\boxed{t_{\mathrm{death}}=\frac d{d+1+\sqrt3}}.
\]
The full-rank state's negativity, by contrast, reaches zero already at
\[
t_{\mathrm{full}}=1-\frac1{\sqrt{d+1}}.
\]
For example, in dimension \(d=3\) at \(p=q=1/2\),
\[
\boxed{\mathcal N_3=0,\qquad \mathcal N_2=\frac1{72}}.
\]
Thus uniform coherence distributed over *all* modes need not yield the largest surviving negativity under **local** depolarization, even though it maximizes the ideal output negativity.

The final death threshold above coincides with the already-known all-input entanglement-annihilation boundary of Lami and Huber; **that endpoint is not claimed as new**. The new result is the exact support-rank optimization and its complete sequence of intermediate transitions within this natural conversion family.

## Assumptions and scope
The controlled-shift action is
\[
U_{\mathrm{CS}}|j\rangle|0\rangle=|jj\rangle.
\]
Input states are precisely the \(d\) flat-support pure states \(|\psi_k\rangle\). Any choice of \(k\) distinct computational basis labels gives the same answer because local depolarization is unitarily covariant and the partial-transpose singular values are basis independent. The channels act independently and *after* the unitary conversion. Their parameters use the trace-to-maximally-mixed convention specified above, rather than a Weyl-Pauli error-probability convention.

The output negativity, not the logarithmic negativity or relative entropy of entanglement, is optimized. Since logarithmic negativity is strictly increasing in negativity, it gives the same best rank within the family. The theorem does not optimize over nonuniform input amplitudes, mixed inputs, adaptive protocols, correlated noise, or other entanglement measures. Zero negativity means PPT; only where an additional separability theorem applies may it be called separable.

## Proof
For \(1\le k\le d\), let
\[
P_k=\sum_{j=0}^{k-1}|j\rangle\langle j|,
\quad \rho_0=|\Phi_{d,k}\rangle\langle\Phi_{d,k}|.
\]
Both reduced states of \(\rho_0\) are \(P_k/k\). Expanding the two local depolarizing maps independently gives
\[
\rho_{d,k;p,q}
=(1-p)(1-q)\rho_0
+\frac{p(1-q)}{dk}I_d\otimes P_k
+\frac{(1-p)q}{dk}P_k\otimes I_d
+\frac{pq}{d^2}I_d\otimes I_d.
\]
After transposing the second system, all offdiagonal terms occur in orthogonal two-dimensional subspaces spanned by \(|ij\rangle,|ji\rangle\) with \(0\le i<j<k\). Every such block is
\[
B_k=\begin{pmatrix}h_k&g_k\\g_k&h_k\end{pmatrix},
\quad
h_k=\frac{p(1-q)+(1-p)q}{dk}+\frac{pq}{d^2},
\quad g_k=\frac{(1-p)(1-q)}{k}.
\]
All remaining partial-transpose eigenvalues are diagonal and nonnegative. The two eigenvalues of \(B_k\) are \(h_k\pm g_k\), and therefore the negative part has magnitude
\[
[g_k-h_k]_+
=\frac1{kd^2}[
 d^2(1-p)(1-q)
-d(p(1-q)+(1-p)q)-kpq]_+
=\frac1{kd^2}[\Delta-k\Pi]_+.
\]
There are exactly \(k(k-1)/2\) such blocks. Summing their negative eigenvalue magnitudes proves
\[
\mathcal N_k=\frac{k-1}{2d^2}[\Delta-k\Pi]_+.
\]
This is an equality for every \(d,k,p,q\) in scope, including boundaries.

For rank selection, define the untruncated quadratic score
\[
f(k)=(k-1)(\Delta-k\Pi).
\]
Because \(k-1\ge0\), maximizing \(\mathcal N_k\) is equivalent to maximizing \([f(k)]_+\). The exact finite difference is
\[
f(k+1)-f(k)=\Delta-2k\Pi.
\]
For \(\Pi>0\), the sequence is strictly discretely concave, as its second difference is \(-2\Pi\). If \(\Delta\le2\Pi\), then \(\Delta-k\Pi\le0\) for every \(k\ge2\), so all negativities vanish. If \(\Delta>2\Pi\), rank two is positive. Strict discrete concavity then implies a single maximizer or exactly two adjacent tied maximizers, with tie equation \(\Delta=2k\Pi\) for an integer \(2\le k<d\). For \(\Pi=0\), the formula is linear in \(k-1\), giving rank \(d\) when \(\Delta>0\) and zero otherwise.

Under symmetric noise set
\[
x=\frac{d(1-t)}t>0.
\]
Then
\[
\frac\Delta\Pi=x^2-2x,
\quad\text{and}\quad
\Delta=2k\Pi\iff x=1+\sqrt{2k+1}.
\]
Solving for \(t\) yields the stated threshold \(t_k\). Because the thresholds strictly decrease with increasing \(k\), they are crossed in the order \(d-1,d-2,\ldots,2\) as noise increases. Each strict inequality interval is nonempty, proving the full rank ladder. The last positive rank is \(k=2\), whose negativity vanishes at \(\Delta=2\Pi\). This corresponds to \(x=1+\sqrt3\) and gives \(t_{\mathrm{death}}\). For \(k=d\), the zero-negativity condition is \(\Delta=d\Pi\), equivalent for \(t\in[0,1]\) to
\[
(1-t)^2=\frac1{d+1},
\]
which gives \(t_{\mathrm{full}}\).

For \(d=3\) and \(p=q=1/2\), direct substitution gives \(\Delta=3/4\) and \(\Pi=1/4\). Hence
\[
\mathcal N_3=\frac{2}{18}[3/4-3/4]_+=0,
\qquad
\mathcal N_2=\frac1{18}[3/4-1/2]=\frac1{72}.
\]
This completes the proof.

## Verification
The formula is proved analytically by the full partial-transpose block decomposition, and the rank ladder by exact finite differences. No extrapolation from finite examples is used.

The standalone checker in `artifacts/verify.py` constructs the full \(d^2\)-by-\(d^2\) density matrix after two independent depolarizing channels, computes its partial transpose and eigenvalues, and compares the negativity against the symbolic formula. It also tests the integer-rank maximizer across and at the predicted transition points, and checks the \(d=3\) rational example. Its numpy dependency is recorded in `artifacts/requirements.txt`. These numerical checks replay the proof rather than replace it.

## Relationship to prior work
Ali, Rostom, Al-Kuwari, Kuniyil, Rahim, and Haddadi develop controlled-shift conversion from qudit coherence to maximally correlated entanglement and calculate negativities under **independent phase damping, global depolarization, and independent amplitude damping**. Their Section V.B explicitly defines global depolarization on the \(d^2\)-dimensional composite system and distinguishes it from a product of local depolarizing channels. That published result neither states the independent-local channel formula proved here nor determines its optimal flat-support rank.

Lami and Huber give an exact all-input entanglement-annihilation characterization for products of local depolarizing channels; their Corollary 8 includes the symmetric disappearance threshold. In the convention of the present theorem, that known universal threshold is exactly \(t_{\mathrm{death}}\). Consequently its endpoint is prior work and cannot be used as an originality claim. Their full theorem concerns channel-level elimination of **all** entanglement, not the intermediate rank-by-rank maxima of the output negativity produced by flat-support coherence inputs. Its rank-two witness establishes sharpness of the final endpoint but does not imply which rank maximizes **the magnitude** of negativity at each lesser noise strength.

Earlier entanglement-robustness results for local **qubit** channels similarly do not cover the high-dimensional sequence of ranks \(2,3,\ldots,d\). The present calculation isolates that sequence in a naturally motivated class of high-dimensional coherence resources and gives exact transition surfaces for possibly unequal local noise strengths.

## Limitations
Optimization is over the discrete family of states uniformly coherent on exactly \(k\) basis modes. It is not asserted to be globally optimal among arbitrary pure Schmidt spectra: a general nonuniform amplitude vector has unequal partial-transpose pair-block diagonals, and additional optimization would be required.

Nor is the result a new entanglement-annihilation threshold or a general separability criterion; those questions are treated separately in the cited literature. Independent local depolarization after conversion, rather than global depolarization or a pre-conversion noise process, is essential to the formulas. Other channels, correlated noise, and local dimensions smaller than the stated domain are outside the rank-ladder claim.

## References
1. A. Ali, A. M. Rostom, S. Al-Kuwari, H. Kuniyil, M. T. Rahim, and S. Haddadi, *High-dimensional coherence to entanglement transduction under canonical noise*, arXiv:2606.16695v1 (first public 2026-06-15).
2. L. Lami and M. Huber, *Bipartite depolarizing channels*, arXiv:1603.02158v1 (2016), especially Theorem 7 and Corollary 8.
3. S. N. Filippov, V. V. Frizen, and D. V. Kolobova, *Ultimate entanglement robustness of two-qubit states against general local noises*, arXiv:1708.08208 (2017).
