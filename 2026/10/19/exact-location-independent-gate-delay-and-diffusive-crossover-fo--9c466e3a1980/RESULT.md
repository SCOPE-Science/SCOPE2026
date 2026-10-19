# Exact location-independent gate delay and diffusive crossover for complementary endpoint escape

## Finding
For each integer \(N\ge1\), let \(T_{N,i}(\kappa)\) be the mean time until the walker reaches the endpoint currently open for absorption, when the initial gate is chosen uniformly between the two complementary configurations. The complete, exact position profile is
\[
T_{N,i}(\kappa)=\frac{i(N-i)}{2}+C_N(\kappa),\qquad
C_N(\kappa)=\frac{N+1}{2\left[\kappa+\sinh\theta\,\coth(N\theta/2)\right]},
\quad \theta=\operatorname{arcosh}(1+\kappa).
\]
Thus every starting-site difference is **exactly independent of gate-switching rate**. The gate-dependent delay \(C_N\) is strictly decreasing in switching rate and obeys
\[
\lim_{\kappa\downarrow0}C_N=\frac{N(N+1)}{4},\qquad
C_N\sim\frac{N+1}{4\kappa}\quad(\kappa\to\infty).
\]
The natural finite-size crossover occurs on the diffusive rate scale \(\kappa=c/N^2\): if \(i_N/N\to x\in[0,1]\), then
\[
\lim_{N\to\infty}\frac{T_{N,i_N}(c/N^2)}{N^2}=
\frac{x(1-x)}{2}+\frac{\tanh(\sqrt{c/2})}{2\sqrt{2c}}\quad(c>0).
\]
The crossover term extends continuously to \(1/4\) at \(c=0\). It approaches \(1/(2\sqrt{2c})\) for large \(c\).

## Assumptions and scope
The vertex set is \(\{0,1,\ldots,N\}\), \(N\ge1\). The position is a nearest-neighbor continuous-time random walk, with *each existing directed edge* assigned rate one: an interior vertex has two potential jumps at total rate two, while an endpoint has one at rate one. A separate independent telegraph environment takes states L and R and flips between them at equal rate \(\kappa>0\). In state L, vertex \(0\) is instantly absorbing and \(N\) reflecting; in state R, vertex \(N\) is instantly absorbing and \(0\) reflecting. A particle already sitting on the now-absorbing endpoint at a gate flip is killed immediately. The initial gate is independent and uniformly distributed; an initially active endpoint is killed at time zero. Expectations include both independent exponential clocks. The theorem makes no statement about nonstationary initial gate distributions, biased jumps, nonexponential gating or higher moments.

## Proof
Write \(A_i\) and \(B_i\) for expected remaining absorption times starting with gates L and R, respectively. The finite killed chain is transient because from every surviving state there is a positive-probability bounded-time route to a killing state. Therefore its mean vector is the unique solution of the backward linear equations. At internal vertices \(1\le i\le N-1\), first-step decomposition yields
\[
-1=A_{i-1}-2A_i+A_{i+1}+\kappa(B_i-A_i),\qquad
-1=B_{i-1}-2B_i+B_{i+1}+\kappa(A_i-B_i).
\]
The instantly absorbing boundary values are \(A_0=B_N=0\). The reflecting-boundary equations are
\[
-1=B_1-B_0+\kappa(A_0-B_0),\qquad
-1=A_{N-1}-A_N+\kappa(B_N-A_N).
\]
Reflection symmetry gives \(A_i=B_{N-i}\). Put \(M_i=(A_i+B_i)/2\) and \(H_i=(A_i-B_i)/2\). The interior equations decouple to
\[
M_{i-1}-2M_i+M_{i+1}=-1,\qquad
H_{i-1}-2H_i+H_{i+1}=2\kappa H_i.
\]
Because \(M_0=M_N=C\) and \(H_0=-C\), \(H_N=C\), their unique solutions, also consistent when \(N=1\) (no interior sites), are
\[
M_i=\frac{i(N-i)}2+C,\qquad
H_i=C\frac{\sinh((i-N/2)\theta)}{\sinh(N\theta/2)},
\qquad \cosh\theta=1+\kappa.
\]
In the left reflecting-boundary equation substitute \(B_0=2C\) and \(B_1=M_1-H_1\). The identity
\[
\frac{H_1}C=\sinh\theta\,\coth(N\theta/2)-\cosh\theta
\]
reduces that boundary equation to \(2C[\kappa+\sinh\theta\,\coth(N\theta/2)]=N+1\). This gives the displayed exact formula; reflection symmetry verifies the right endpoint equation too.

For a rational alternative, set \(h_0=0\), \(h_1=1\), and \(h_{j+1}=2(1+\kappa)h_j-h_{j-1}\) for \(j\ge1\). Then \(h_j=\sinh(j\theta)/\sinh\theta\) and
\[
C_N=\frac{(N+1)h_N}{2[(1+2\kappa)h_N+1-h_{N-1}]}.
\]
This gives an exact rational expression without floating-point hyperbolic functions. In particular \(N=1\) gives \(C_1=1/[2(1+\kappa)]\).

To prove strict monotonicity, let \(D(\theta)=\cosh\theta-1+\sinh\theta\,\coth(N\theta/2)\). Its first summand has positive derivative. For the second, multiplying the derivative by \(2\sinh^2(N\theta/2)\) gives
\[
\cosh\theta\,\sinh(N\theta)-N\sinh\theta>0
\]
for every \(\theta>0\), \(N\ge1\); indeed \(\sinh(N\theta)\ge N\sinh\theta\) and \(\cosh\theta>1\). Since \(\theta\) strictly increases with \(\kappa\), \(C_N=(N+1)/(2D)\) strictly decreases. The fixed-size limits follow by elementary \(\theta\to0\) and \(\theta\to\infty\) asymptotics. For diffusive scaling, \(N\theta\to\sqrt{2c}\), while \(N\sinh\theta\to\sqrt{2c}\) and \(N\kappa\to0\). Substitution yields the claimed limit; \(i_N(N-i_N)/(2N^2)\to x(1-x)/2\).

## Verification
The standalone `verify_antiphase.py` constructs the full transient continuous-time Markov generator (including instantaneous killing upon a flip), independently solves its exact rational backward equations by Gaussian elimination, and compares them to the recurrence formula. A run checked 520 exact source/starting-site comparisons for all lengths \(1\le N\le13\) at five positive rational flip rates, then 9 numerical convergence checks and 24 finite-size monotonicity comparisons. All passed. The code is a finite diagnostic only; the preceding derivation proves the quantified theorem.

## Relationship to prior work
Ammari, Garnier, Kang, Lee and Sølna (2011) study *alternately open* boundary gates in a smooth two-dimensional domain, proving narrow-gate asymptotics and a switching-rate effect. Their boundary-system framework motivates the present complementary-gate model, but their main results are not the exact, all-size **discrete interval** profile or its rate-versus-length crossover. In contrast, Bressloff and Lawley (2016) treat Brownian diffusion on intervals and trees with **all endpoints simultaneously** absorbing in one gate state and reflecting in the other, or series interior gates; this does not imply the antiphase finite-lattice formula. Lawley (2016) gives general boundary-value equations for switching systems, a methodological predecessor rather than an explicit finite-path solution. Bressloff and Lawley (2015) analyze a one-gated-boundary diffusion model. The path's site-independent additive delay, closed rational recurrence and diffusive crossover are the proposed additional facts, not the known coupled backward equations or qualitative monotonicity.

## Limitations
Originality is assessed relative to inspected accessible primary text and published-result searches; there may be an equivalent formulation in unindexed or differently termed gated-first-passage literature. The theorem is for symmetric unit-rate nearest-neighbor jumps and a **uniform initial telegraph state**. It gives only the mean, not absorption-time distributions or independent-particle statistics. The \(\kappa\to0\) endpoint is a limit from positive switching rather than a claim of ergodicity at zero. Computations on finite lengths are supplemental checks, not evidence of an infinite theorem by themselves. Independent validation has not been performed.

## References
1. H. Ammari, J. Garnier, H. Kang, H. Lee, K. Sølna, “The Mean Escape Time for a Narrow Escape Problem with Multiple Switching Gates,” *Multiscale Modeling & Simulation* 9 (2011), 817–833; doi:10.1137/100817103. Earliest journal-public date 2011-06-29; publicly accessible author PDF: https://josselin-garnier.org/wp-content/uploads/2013/12/escape.pdf.
2. P. C. Bressloff, S. D. Lawley, “Diffusion on a Tree with Stochastically Gated Nodes,” *J. Phys. A: Math. Theor.* 49 (2016), 245601; doi:10.1088/1751-8113/49/24/245601. Author-uploaded full text at https://www.researchgate.net/publication/302979790_Diffusion_on_a_tree_with_stochastically_gated_nodes.
3. S. D. Lawley, “Boundary Value Problems for Statistics of Diffusion in a Randomly Switching Environment: PDE and SDE Perspectives,” arXiv:1602.07398v1 (2016), https://arxiv.org/pdf/1602.07398.
4. P. C. Bressloff, S. D. Lawley, “Escape from a Potential Well with a Randomly Switching Boundary,” *J. Phys. A: Math. Theor.* 48 (2015), 225001; doi:10.1088/1751-8113/48/22/225001.
