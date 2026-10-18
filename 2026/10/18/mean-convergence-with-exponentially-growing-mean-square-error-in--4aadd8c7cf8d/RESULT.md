# Mean convergence with exponentially growing mean-square error in default-initialized EControl

## Finding
Consider one-worker EControl on the noiseless scalar strongly convex objective \(f(x)=x^2/2\), with independent Bernoulli half-dropout compression, standard stored-gradient initialization, and fixed step \(\gamma=1/10\). For full error-control feedback \(\eta=1\), the expected iterate converges geometrically to the unique minimizer, yet its second moment is unbounded: for every integer \(t\ge0\),
\[
\max_{0\le j\le t}\mathbb E[x_j^2]\ge
\frac{61}{4771\cdot5213}\left(\frac{13}{10}\right)^t.
\]
For feedback \(\eta=1/2\), with the same objective, compression, step, and initialization, the entire algorithmic state converges geometrically in mean square. This statement is a strict separation between first-moment convergence, unstable full-feedback mean-square behavior, and stable moderated feedback; no assertion of pointwise divergence of \(\mathbb E[x_t^2]\) is needed.

## Assumptions and scope
Set \(x_0=1\), stored gradient \(h_0=\nabla f(x_0)=1\), and residual \(e_0=0\). At each iteration independently choose \(C_t(z)=z\) with probability \(1/2\), and \(C_t(z)=0\) otherwise. This is a randomized contractive compressor with contraction parameter \(\delta=1/2\). Apply the one-worker, exact-gradient EControl recursion
\[
\Delta_t=C_t(\eta e_t+x_t-h_t),\quad
 e_{t+1}=e_t+x_t-h_t-\Delta_t,\quad
 h_{t+1}=h_t+\Delta_t,\quad
 x_{t+1}=x_t-\tfrac1{10}h_{t+1}.
\]
The two cases are \(\eta=1\) and \(\eta=1/2\). All expectations are over the compressor draws; there is no gradient noise.

## Proof
Write \(v_t=(x_t,h_t,e_t)^\top\), \(s=1/10\). Dropout and transmission induce respectively the matrices
\[
A=\begin{pmatrix}1&-s&0\\0&1&0\\1&-1&1\end{pmatrix},\qquad
B_\eta=\begin{pmatrix}1-s&0&-s\eta\\1&0&\eta\\0&0&1-\eta\end{pmatrix}.
\]
Conditional on \(v_t\), each is used with probability \(1/2\).

For \(\eta=1\), use the rational symmetric matrix
\[
W=10^{-6}\begin{pmatrix}341000&-347500&171200\\-347500&366200&-148500\\171200&-148500&247000\end{pmatrix}.
\]
Direct exact arithmetic verifies that \(W\) and
\[
H=\tfrac12(A^\top WA+B_1^\top WB_1)-\tfrac{13}{10}W
\]
are positive definite. Their respective leading principal minors are
\[
\left(\frac{341}{1000},\frac{82359}{20000000},\frac{27082717}{62500000000}\right),\quad
\left(\frac{6071}{200000},\frac{1260269}{40000000000},\frac{282727743}{10^{15}}\right).
\]
Consequently, \(\mathbb E[v_t^\top Wv_t]\ge (13/10)^t v_0^\top Wv_0=(61/5000)(13/10)^t\). This certifies full-state mean-square growth without relying on an approximate eigenvalue.

To transfer this growth to the scalar iterate, define \(M_t=\max_{0\le j\le t}\mathbb E[x_j^2]\). From the update, for every \(t\ge1\), \(h_t=(x_{t-1}-x_t)/s\), hence \(\mathbb E[h_t^2]\le4M_t/s^2\); the same bound covers \(h_0=1\). At full feedback a successful compression zeros the next residual, while dropout sets it to \(e_t+x_t-h_t\). Thus
\[
\mathbb E[e_{t+1}^2]\le\tfrac34\mathbb E[e_t^2]+3(1+4/s^2)M_{t+1}.
\]
Since \(e_0=0\) and \(M_t\) is nondecreasing, geometric summation yields \(\mathbb E[e_t^2]\le12(1+4/s^2)M_t\). Therefore
\[
\mathbb E\|v_t\|_2^2\le(13+52/s^2)M_t=5213M_t.
\]
The positive-definite \(W\) satisfies \(v^\top Wv\le\operatorname{tr}(W)\|v\|_2^2\), where \(\operatorname{tr}(W)=4771/5000\), yielding the stated quantitative lower bound on \(M_t\).

Despite that growth, the mean obeys \(\mathbb E[v_{t+1}]=\overline B\,\mathbb E[v_t]\), with \(\overline B=(A+B_1)/2\). The positive-definite matrix
\[
R=\frac1{99}\begin{pmatrix}1160&-112&10\\-112&212&7\\10&7&218\end{pmatrix}
\]
satisfies \(R-\overline B^\top R\overline B=I\); its leading principal minors are \((1160/99,7072/297,15544/297)\). Thus \(\rho(\overline B)<1\), and \(\mathbb E x_t\to0\) geometrically.

At \(\eta=1/2\), let
\[
Q=\frac19\begin{pmatrix}1840&-1658&570\\-1658&1781&-452\\570&-452&395\end{pmatrix}.
\]
Exact arithmetic verifies \(Q-(A^\top QA+B_{1/2}^\top QB_{1/2})/2=I\), with positive leading principal minors \((1840/9,528076/81,108358000/729)\). Therefore the expected \(Q\)-energy decreases at least geometrically, since \(\|v\|_2^2\ge v^\top Qv/\lambda_{\max}(Q)\). In particular \(\mathbb E[x_t^2]\to0\) geometrically.

## Verification
Run `python3 verify.py` using the Python standard library. The checker performs exact rational matrix multiplication, verifies the three stated Lyapunov identities and all six Sylvester definiteness certificates, and confirms the initial quadratic energy and trace. Its finite computations verify the listed rational identities; the infinite-time conclusions follow from the preceding inequalities, not from finite iteration experiments.

## Relationship to prior work
Gao, Islamov, and Stich introduced EControl and its feedback parameter; their source analyzes small-step regimes and gives an example of instability at full feedback using a different initialization and deterministic Top-1 compression. Here the issue is present under the source-standard initialization on an exact scalar quadratic with independent half-dropout. More specifically, the theorem supplies a rigorous first-moment/second-moment separation and an exact same-step stability recovery by moderating feedback. Classical error feedback, EF21, DIANA, and MARINA use different memory or estimator recursions and do not directly imply these matrix inequalities.

## Limitations
The growth bound concerns the running maximum of iterate second moments; it does not prove that every individual second moment tends to infinity. The counterexample is a single worker, one scalar quadratic, independent half-dropout compression, a fixed \(1/10\) step, and two specific feedback values; it does not define the complete EControl stability region or contradict its sufficient convergence theorem. Full feedback instability in another setting was already noted in the source. Independent scientific validation has not been carried out.

## References
1. Y. Gao, R. Islamov, S. Stich, *EControl: Fast Distributed Optimization with Compression and Error Control*, arXiv:2311.05645v1 (first public 2023-11-06), https://arxiv.org/abs/2311.05645v1.
2. Related distinct algorithms and their overlap evidence are documented in the accompanying review and audit.
