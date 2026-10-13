# Three-noise degeneracy breaks the published SECIHRV ergodicity proof
## Finding
For the stochastic SECIHRV model of Hussain and Alharthi, the proof of Theorem 4.2 does not establish the stated uniqueness and ergodicity conclusion. The obstruction is structural and parameter-independent.

The state is \(x=(x_1,\ldots,x_7)\in\mathbb R_+^7\), and the source drives it with exactly three independent Brownian motions. Writing the three diffusion columns as \(\sigma_1,\sigma_2,\sigma_3\in\mathbb R^7\), its covariance matrix is
\[
A(x)=\sum_{r=1}^3\sigma_r(x)\sigma_r(x)^\top.
\]
In the printed system the fifth and sixth coordinates contain no stochastic term at all. Therefore
\[
A(x)e_5=0,\qquad A(x)e_6=0
\]
for every positive state. Consequently the uniform-ellipticity inequality required in Lemma 3.3 and Remark 3.4,
\[
\zeta^\top A(x)\zeta\ge M_1\lVert\zeta\rVert^2\qquad(M_1>0),
\]
cannot hold on any nonempty open set: choosing \(\zeta=e_5\) or \(e_6\) makes the left side zero and the right side positive.

There is a second independent obstruction in the Lyapunov part of Theorem 4.2. The displayed function is a weighted sum of a square involving coordinates \(1,2,3,4,6,7\) and three squares involving \(x_4,x_6,x_7\). It contains no \(x_5\). Thus, for every \(t>-x_5^*\),
\[
V(x^*+t e_5)=0.
\]
So the function is not positive definite about \(x^*\) and is not radially unbounded. Likewise Eq. (50) constrains only \(x_1,x_2,x_4,x_6,x_7\); \(x_3\) and \(x_5\) remain free. Its nonempty level set therefore contains unbounded positive rays and cannot be contained in any bounded neighborhood \(U\), contrary to the final step of the proof.

## Assumptions and scope
The claim concerns the printed seven-dimensional Itô system (4), Lemma 3.3, Remark 3.4, and Theorem 4.2 of the cited article. No restriction on the positive biological parameters removes the two kernel directions, because coordinates \(5\) and \(6\) have no direct Brownian term in system (4). The noncoercivity statement uses only the exact displayed definition of \(V\) in Eqs. (40)–(42), and the unbounded-cylinder statement uses only Eq. (50).

The conclusion is about proof coverage, not the truth value of the stationary-distribution theorem. Degenerate diffusions can possess unique invariant measures, but they require an additional argument such as a Markov-semigroup, irreducibility, support, or hypoelliptic analysis. None of those replacements is proved here.

## Proof
From system (4), define the amplitudes \(a=\xi_1\beta_0x_1\), \(b=\xi_2\upsilon x_1\), and \(c=\xi_3\rho x_2\). The diffusion columns have the form
\[
\sigma_1=(-a,a,0,0,0,0,0)^\top,
\]
\[
\sigma_2=(-b,0,0,0,0,0,b)^\top,
\]
\[
\sigma_3=(0,-c,\varepsilon c,(1-\varepsilon)c,0,0,0)^\top.
\]
Every column has zero fifth and sixth entries. Hence \(e_5\) and \(e_6\) are in the kernel of \(A=\sum_r\sigma_r\sigma_r^\top\). In particular \(\operatorname{rank}A\le3<7\), and for \(\zeta=e_5\),
\[
\zeta^\top A\zeta=0<M_1= M_1\lVert\zeta\rVert^2
\]
for every \(M_1>0\). This contradicts the uniform-positive-definiteness condition that the source states as the nondegenerate criterion behind Lemma 3.3.

Next, Eqs. (40)–(42) define \(V\) using no occurrence of \(x_5\). Set all coordinates except the fifth equal to their endemic values. Then all displayed squared terms vanish, regardless of the positive fifth coordinate, and therefore \(V(x^*+t e_5)=0\). The claims that \(V\) is positive definite and that \(V(x)\to\infty\) as \(\lVert x\rVert\to\infty\) are both false for the displayed function.

Finally, let \(F>0\) and use the positive coefficients \(m_1,m_2,m_3\) from Theorem 4.2. Fix
\[
x_1=\theta_1x_1^*+\sqrt{F/m_1},\quad
x_2=\theta_2x_2^*,\quad
x_4=\theta_3x_4^*,\quad
x_6=\theta_3x_6^*,\quad
x_7=\theta_2x_7^*.
\]
For every \(x_3>0\) and \(x_5>0\), Eq. (50) is then satisfied exactly. Letting either free coordinate tend to infinity proves that the displayed level set is unbounded. Therefore no bounded open set can contain it, so the final bounded-neighborhood argument in Theorem 4.2 does not follow.

## Verification
The accompanying `verify.py` reconstructs the three diffusion columns, forms \(A=GG^\top\) in exact rational arithmetic, verifies the two coordinate kernel directions, evaluates the published Lyapunov form along an unbounded \(x_5\)-ray, and constructs an unbounded family satisfying the displayed Eq. (50) level-set equation. It prints `VERIFY_OK` when all exact checks pass.

## Relationship to prior work
The motivating article itself states uniform ellipticity as the criterion used in its Lemma 3.3 and then claims uniqueness and ergodicity in Theorem 4.2. Earlier stochastic-epidemic literature explicitly treats degenerate diffusion as a different problem: Cao, Liu, Wen, Liu, and Zu (2019) note that uniform ellipticity is unavailable for their degenerate SIR diffusion and instead use Markov-semigroup methods. Dieu, Nguyen, Du, and Yin (2016) likewise develop ergodicity for a degenerate stochastic SIR model using a dedicated asymptotic analysis. These papers show that degeneracy does not by itself make uniqueness impossible; rather, it requires hypotheses and arguments different from the nondegenerate criterion printed in the 2026 SECIHRV proof.

Exact-title, DOI, theorem-language, rank-deficiency, ellipticity, and Lyapunov-coercivity searches found no published correction or source-specific statement of the three obstructions above. No inspected publication or public correction located during the literature comparison states an implication-equivalent SECIHRV ergodicity defect.

## Limitations
This result does not prove nonexistence or nonuniqueness of an invariant measure for the SECIHRV SDE. It proves that the published Theorem 4.2 argument does not establish its conclusion through the stated uniform-ellipticity/Khasminskii route. A future proof could potentially exploit drift-mediated noise propagation, support properties, Hörmander-type brackets, or Markov-semigroup theory; those questions are not resolved here.

The result also does not reassess the paper's extinction theorem, sensitivity plots, or numerical discretization.

## References
1. S. Hussain and T. N. Alharthi, “A stochastic SECIHRV dynamical system and 3D sensitivity analysis of influenza transmission under environmental uncertainty,” *Boundary Value Problems* 2026, 54 (2026). DOI: 10.1186/s13661-026-02256-2. Published 31 March 2026.
2. Z. Cao, X. Liu, X. Wen, L. Liu, et al., “A regime-switching SIR epidemic model with a ratio-dependent incidence rate and degenerate diffusion,” *Scientific Reports* 9, 10696 (2019). DOI: 10.1038/s41598-019-47131-6.
3. N. T. Dieu, D. H. Nguyen, N. H. Du, and G. Yin, “Classification of asymptotic behavior in a stochastic SIR model,” *SIAM Journal on Applied Dynamical Systems* 15 (2016), 1062–1084. DOI: 10.1137/15M1043315.
