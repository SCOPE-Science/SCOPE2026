# Exact loss spectrum and late-damping metrological deficit for multi-excitation Dicke probes

## Finding
For every integer \(N\ge4\), every excitation number \(2\le k\le N-1\), and every independent local amplitude-damping probability \(p\in[0,1]\), the complete eigenvalue spectrum of the damped symmetric Dicke input \(\lvert D_N^k\rangle\) admits the following polynomial-size description. For \(0\le s\le N\) and \(0\le j\le\min\{s,N-s\}\), define \(\lambda_{s,j}=0\) unless \(s\le k\) and \(j\le k-s\); otherwise define
\[
\lambda_{s,j}=\frac{p^{k-s}(1-p)^s}{\binom Nk}\binom{N-s-j}{k-s-j}\binom{N-k+s-j}{s-j}.
\]
Each \(\lambda_{s,j}\) has multiplicity \(d_j=\binom Nj-\binom N{j-1}\), taking \(\binom N{-1}=0\); the remaining eigenvalues are zero. Endpoints use the continuous convention \(0^0=1\).

For encoding a rotation *after damping* with a transverse collective-spin generator \(J_\phi=\cos\phi\,J_x+\sin\phi\,J_y\), the exact symmetric-logarithmic-derivative quantum Fisher information is
\[
F_{N,k}(p)=\sum_{s=0}^{N-1}\ \sum_{j=0}^{\min\{s,N-s-1\}}d_j(s+1-j)(N-s-j)\frac{(\lambda_{s,j}-\lambda_{s+1,j})^2}{\lambda_{s,j}+\lambda_{s+1,j}},
\]
with zero assigned when both eigenvalues vanish. Every transverse direction has the same value; the longitudinal generator has zero Fisher information. Thus the displayed value is the maximum over all unit collective-spin directions. In particular,
\[
F_{N,k}(0)=N+2k(N-k),\qquad F_{N,k}(1)=N,
\]
and the **strict late-loss deficit** obeys
\[
F_{N,k}(1-\epsilon)=N-2k(N-k+2)\epsilon+O_{N,k}(\epsilon^2)\qquad(\epsilon\downarrow0).
\]
For each admissible \(N,k\), there is consequently an interval just below full relaxation with \(0<F_{N,k}(p)<N\), despite a strict advantage \(F_{N,k}(0)>N\) before damping. The exact finite-population result requires only \(O(N^2)\) scalar spectral terms rather than diagonalization of a matrix of dimension \(2^N\).

## Assumptions and scope
Let \(\lvert0\rangle\) be the ground state, \(\lvert1\rangle\) the excited state, and
\[
\lvert D_N^k\rangle=\binom Nk^{-1/2}\sum_{|S|=k}\lvert S\rangle.
\]
The single-qubit amplitude-damping channel has Kraus operators \(K_0=\lvert0\rangle\langle0\rvert+\sqrt{1-p}\lvert1\rangle\langle1\rvert\) and \(K_1=\sqrt p\lvert0\rangle\langle1\rvert\). Apply this channel independently to every qubit before the unknown-angle unitary. Define \(J_\alpha=\frac12\sum_{a=1}^N\sigma_\alpha^{(a)}\), with \(\alpha\in\{x,y,z\}\). The normalizations refer to total, not per-qubit, quantum Fisher information. Different damping rates, collective decay, damping after encoding, and general input states are not asserted.

## Proof
**1. Output blocks and an inclusion Gram matrix.** Index the computational basis by subsets of excited positions. The output commutes with total excitation number and has no coherences between different surviving excitation numbers. At excitation level \(s\), its matrix entries indexed by \(s\)-sets \(S,T\) are
\[
\rho_s(S,T)=\frac{p^{k-s}(1-p)^s}{\binom Nk}\binom{N-|S\cup T|}{k-s}\quad(0\le s\le k).
\]
To see this directly, choose the common lost-excitation subset disjoint from both surviving sets; only an identical lost subset on bra and ket survives the Kraus sum. Thus \(\rho_s\) is the stated scalar times \(B_{s,r}B_{s,r}^{\mathsf T}\), where \(r=k-s\) and \(B_{s,r}(S,R)=\mathbf1_{S\cap R=\varnothing}\). Complementing columns turns \(B_{s,r}\) into the Boolean-lattice inclusion matrix \(W_{s,t}(S,T)=\mathbf1_{S\subseteq T}\), with \(t=N-k+s\).

**2. Exact spectrum, including null sectors.** On rank-\(s\) Boolean-lattice functions define the raising and lowering operators \(U,D=U^{\mathsf T}\). Directly on each subset, \(DU-UD=(N-2s)I\). Starting with a primitive vector at rank \(j\) in \(\ker D\), its normalized raising chain has dimension \(N-2j+1\), and the primitive multiplicity is \(d_j=\binom Nj-\binom N{j-1}\). Since \(W_{s,t}=D^{t-s}/(t-s)!\) on the appropriate ranks, the square of its singular value on rank-\(j\) chains is
\[
\binom{t-j}{s-j}\binom{N-s-j}{t-s}.
\]
Substituting \(t=N-k+s\) gives precisely the claimed \(\lambda_{s,j}\). All remaining chains have eigenvalue zero. Orthogonality of distinct primitive chains and the telescoping identity \(\sum_{j=0}^{\min(s,N-s)}d_j=\binom Ns\) establish completeness, not merely a rank bound.

**3. Fisher information from all support-to-kernel transitions.** The raising operator \(J_+=J_x+iJ_y\) connects adjacent ranks \(s,s+1\) within the same primitive chain, with squared matrix element \((s+1-j)(N-s-j)\). The general spectral definition
\[
F(\rho,J_x)=2\sum_{a,b:\,\lambda_a+\lambda_b>0}\frac{(\lambda_a-\lambda_b)^2}{\lambda_a+\lambda_b}|\langle a|J_x|b\rangle|^2
\]
includes eigenvectors with zero eigenvalue. Since \(J_x=(J_++J_-)/2\), combining both orientations of every adjacent edge produces exactly the double sum in the Finding. The state commutes with \(J_z\), so the longitudinal Fisher information is zero. Conjugating by \(e^{-i\phi J_z}\) proves rotational invariance throughout the transverse plane; the Fisher-information matrix therefore has only the two equal transverse eigenvalues and a zero longitudinal eigenvalue.

**4. Boundaries and the late-loss coefficient.** At \(p=0\) the sole populated spectral value is \(\lambda_{k,0}=1\), and adjacent transitions yield \((k+1)(N-k)+k(N-k+1)=N+2k(N-k)\). At \(p=1\) the sole populated value is \(\lambda_{0,0}=1\), so \(F=N\). To obtain the first correction, put \(\epsilon=1-p\) and expand the only eigenvalues of order at most one:
\[
\lambda_{0,0}=1-k\epsilon+O(\epsilon^2),\quad
\lambda_{1,0}=\frac{k(N-k+1)}N\epsilon+O(\epsilon^2),\quad
\lambda_{1,1}=\frac{k(k-1)}{N(N-1)}\epsilon+O(\epsilon^2).
\]
All other populated eigenvalues are \(O(\epsilon^2)\). The terms with \((s,j)=(0,0),(1,0),(1,1)\) then give the linear coefficient
\[
-Nk-(N+2)\frac{k(N-k+1)}N+(N-1)(N-2)\frac{k(k-1)}{N(N-1)}=-2k(N-k+2).
\]
The remaining nonnegative terms are \(O(\epsilon^2)\) because their eigenvalues are individually of that order. This proves the expansion and the sub-shot-noise interval near full damping. For \(0<p<1\), \(\lambda_{1,1}>0\) but \(\lambda_{k,1}=0\); adjacent links in the same primitive rank-one chain force at least one positive Fisher summand. Thus \(F>0\) throughout the open damping interval. No assertion is made about uniqueness of the shot-noise crossing.

## Verification
The standalone `verify.py` uses only NumPy and constructs the full \(2^N\)-dimensional density operator independently from the Kraus loss masks, diagonalizes it, and evaluates the exact spectral Fisher definition. It also directly diagonalizes inclusion Gram matrices and compares their eigenvalues with the claimed binomial spectrum. Its bounded finite cases and endpoint tests are listed in `VERIFICATION.md`. The analytic chain argument and endpoint expansion, not the finite tests, prove the arbitrary-size statement.

## Relationship to prior work
Ozaydin (2014) analyzes one-excitation \(W\) states; this theorem deliberately excludes \(k=1\) and attributes no new single-excitation result. Tóth and Apellaniz (2014) give the general Dicke-state metrological framework; Apellaniz *et al.* (2015) address observable-based lower bounds for noisy Dicke states, not the exact amplitude-damping loss spectrum. Sudha *et al.* (2026) plot collective-spin Fisher information for a balanced eight-qubit Dicke state under local amplitude damping and compare engineered superpositions, but do not state the exact all-\(N,k\) spectrum or the universal first-order sub-shot-noise coefficient established here. Reduced-pair concurrence is a different invariant and does not, by itself, determine collective-spin Fisher information. General representation-theoretic machinery is not claimed as original.

## Limitations
The theorem concerns independent homogeneous zero-temperature amplitude damping applied before collective-spin parameter encoding. It gives no optimal measurement protocol, no nonidentical-channel result, and no theorem about the number or uniqueness of crossover points. The all-parameter symbolic formula has been mathematically proved but not independently audited for publication priority. The closest modern balanced-state numerical comparison is genuinely related and remains a residual priority risk for narrower consequences.

## References
1. F. Ozaydin, *Quantum Fisher Information of W States in Decoherence Channels*, arXiv:1403.2376 (first submitted 2014-03-10). https://arxiv.org/abs/1403.2376
2. G. Tóth and I. Apellaniz, *Quantum metrology from a quantum information science perspective*, arXiv:1405.4878 (first submitted 2014-05-19). https://arxiv.org/abs/1405.4878
3. I. Apellaniz, M. Kleinmann, O. Gühne and G. Tóth, *Optimal witnessing of the quantum Fisher information with few measurements*, arXiv:1511.05203 (first submitted 2015-11-16). https://arxiv.org/abs/1511.05203
4. Sudha, B. N. Karthik, K. S. Akhilesh and A. R. Usha Devi, *Dicke superposition probes for noise-resilient Heisenberg and super-Heisenberg metrology*, arXiv:2601.23043 (first submitted 2026-01-30). https://arxiv.org/abs/2601.23043
