# Critical adaptive SARAH+ stopping: almost-sure termination with infinite mean work and output risk

## Finding
For a two-term, strongly convex scalar quadratic, removing only the hard iteration cap from the adaptive gradient-norm stopping rule of SARAH+ produces a first-passage stopping time which is almost surely finite but has infinite expectation. More strongly, the squared norm of the returned iterate has infinite expectation. A finite hard cap prevents these infinities at each fixed horizon, but the exact expected squared error obeys a lower bound proportional to the cap.

Specifically, for the model and update rule below,
\[
\mathbb P(T=2j+1)=\frac{1}{2^{2j+1}(j+1)}\binom{2j}{j},\qquad \mathbb P(T<\infty)=1,\qquad \mathbb ET=\infty,
\]
\[
\mathbb E[x_{T+1}^2]=\mathbb E[F(x_{T+1})]=\infty,
\qquad
\mathbb E[x_{\min(T,N)+1}^2]\ge\frac{x_0^2}{2}\left\lfloor\frac{N-1}{2}\right\rfloor\quad(N\ge1).
\]
In particular, the unbounded-time statement describes an **uncapped extension of the rule**, not the finitely capped algorithm in the original publication.

## Assumptions and scope
Let \(f_1(x)=x^2/2\), \(f_2(x)=3x^2\), and \(F(x)=(f_1(x)+f_2(x))/2=7x^2/4\), where \(x\in\mathbb R\). Both component objectives are smooth and strongly convex; their unique common minimizer is zero. Choose any deterministic \(x_0\ne0\), learning rate \(\eta=1/2\), and an exact initial full gradient \(v_0=F'(x_0)=7x_0/2\); set \(x_1=x_0-\eta v_0\). For integers \(t\ge1\), independently draw \(I_t\) uniformly from \(\{1,2\}\), compute
\[
v_t=v_{t-1}+f'_{I_t}(x_t)-f'_{I_t}(x_{t-1}),
\qquad x_{t+1}=x_t-\eta v_t.
\]
Stop on the **first** \(t\ge1\) satisfying the SARAH+ squared-gradient threshold \(|v_t|^2\le\gamma|v_0|^2\) with \(\gamma=1/4\). Denote this stopping time by \(T\). The uncapped output is \(x_{T+1}\), after applying the gradient step corresponding to \(v_T\). Under a hard cap allowing at most \(N\) stochastic recursive updates, the output is \(x_{\min(T,N)+1}\). This matches the order of gradient computation, gradient update, and termination checking in Algorithm 2 of Nguyen et al. (2017), with maximum inner loop size \(m=N+1\).

The step size here is outside the source's sufficient small-step convergence regime. The theorem concerns one inner pass with an exact initial gradient, not repeated outer iterations or a global complexity bound for SARAH+.

## Proof
**1. Reduction to fair first passage.** Write \(a_1=1\), \(a_2=6\). Since \(f_i'(x)=a_i x\), the recursion yields exactly
\[
v_t=(1-\eta a_{I_t})v_{t-1}
=\begin{cases}\tfrac12v_{t-1}&I_t=1,\\-2v_{t-1}&I_t=2.\end{cases}
\]
Because \(v_0\ne0\), the integer-valued process \(W_t=\log_2|v_t/v_0|\) is a simple symmetric random walk started at zero, with independent increments \(-1,+1\). The stopping condition is \(W_t\le-1\). Unit jumps imply \(T\) is the first hitting time of \(-1\). By the reflection principle/ballot count, a first hit at \(2j+1\) has exactly \(C_j=\binom{2j}{j}/(j+1)\) admissible sample strings, each of probability \(2^{-(2j+1)}\). The Catalan generating identity
\[
\sum_{j\ge0} C_j z^j=\frac{1-\sqrt{1-4z}}{2z}
\]
at \(z=1/4\) gives \(\sum_{j\ge0}\mathbb P(T=2j+1)=1\). Stirling's formula gives \(\mathbb P(T=2j+1)\sim[2\sqrt\pi\,j^{3/2}]^{-1}\); therefore \(\mathbb ET\), whose terms have order \(j^{-1/2}\), diverges.

**2. Rare stopped outputs.** For each integer \(h\ge1\), define the disjoint cylinder event \(E_h\) that the first \(h\) draws select component \(2\), followed by \(h+1\) draws selecting component \(1\). On \(E_h\), the walk goes up to level \(h\), then down to \(-1\) without earlier hitting \(-1\). Therefore \(T=2h+1\) and \(\mathbb P(E_h)=2^{-(2h+1)}\). Let \(P_j=v_j/v_0\) with \(P_0=1\). Its stopped partial sum on this event is exactly
\[
S_h=\sum_{j=0}^{2h+1}P_j
=\sum_{j=0}^{h}(-2)^j+(-2)^h\sum_{s=1}^{h+1}2^{-s}
=\frac53(-2)^h+\frac13-\frac12(-1)^h.
\]
The recursion telescopes to \(x_{T+1}=x_0-\eta v_0S_h=x_0(1-7S_h/4)\). Since the correction \(1/3-(-1)^h/2\) has absolute value at most \(5/6\),
\[
|S_h|\ge\frac53 2^h-\frac56\ge\frac54 2^h,
\qquad
\left|1-\frac74S_h\right|\ge\frac{35}{16}2^h-1\ge2^h.
\]
The last two inequalities hold for every \(h\ge1\). Hence \(x_{T+1}^2\ge4^h x_0^2\) on \(E_h\). Disjointness and nonnegativity imply
\[
\mathbb E[x_{T+1}^2]\ge x_0^2\sum_{h\ge1}\mathbb P(E_h)4^h
=\frac{x_0^2}{2}\sum_{h\ge1}1=\infty.
\]
Multiplying by \(7/4\) gives \(\mathbb E[F(x_{T+1})]=\infty\). For a deterministic cap \(N\), the same events are fully observed whenever \(2h+1\le N\), and the identical disjoint-event calculation gives
\[
\mathbb E[x_{\min(T,N)+1}^2]\ge\frac{x_0^2}{2}\#\{h\ge1:2h+1\le N\}
=\frac{x_0^2}{2}\max\left\{0,\left\lfloor\frac{N-1}{2}\right\rfloor\right\}.
\]
The maximum may be omitted because \(N\ge1\). Every finite-cap output has finite second moment because it is a finite-valued function of finitely many Bernoulli draws.

**3. Deterministic comparison.** Replacing the recursive gradient by the exact full gradient at each iteration multiplies the iterate by \(1-\eta(7/2)=-3/4\), so the deterministic full-gradient method converges geometrically. The infinite-risk result is not due to nonconvexity or instability of the corresponding full-gradient iteration.

## Verification
Run `python3 verify.py` with Python 3 and no third-party dependencies. The verifier performs 201 exact-rational checks including the two-curvature path formula, first-passage Catalan counts through 15 draws, exact finite capped-path enumeration through 13 draws, and the deterministic comparison. These finite checks are diagnostics, not proofs of the infinite-time or infinite-moment assertions; those assertions follow from the analytic path and Catalan arguments above.

## Relationship to prior work
Nguyen, Liu, Scheinberg, and Takáč introduce the SARAH recursion and the SARAH+ norm-ratio stopping rule in Algorithm 2, explicitly with a finite maximum inner-loop size for robustness. Their analysis imposes sufficient small learning-rate restrictions and does not provide the uncapped critical first-passage distribution or a lower bound increasing with a finite cap for this example. The present statement retains that finite cap when assessing the actual algorithm; it analyzes the uncapped limit separately. Li, Ma, and Giannakis analyze last-iterate convergence of SARAH and a probabilistic refresh variant under safe learning-rate conditions. Zhong, Li, and Lahiri prove high-probability guarantees for a modified recursive-gradient algorithm. None of these inspected claims implies this exact stopped-output counterexample, though priority beyond the inspected literature remains uncertain. The Catalan first-passage calculation is classical and is not claimed as a new combinatorial result; its coupling to the signed recursive-gradient trajectory is the proposed increment.

## Limitations
This is a single-epoch, scalar, exact-arithmetic, two-component counterexample at a learning rate beyond the published sufficient convergence regime. It does not disprove those regimes, does not assert infinite expected work for the **capped** SARAH+ algorithm, and gives no conclusion about repeated outer loops or almost-sure divergence of the returned iterate. The linear-in-cap statement is a lower bound, not an exact asymptotic rate.

## References
1. L. M. Nguyen, J. Liu, K. Scheinberg, M. Takáč, *SARAH: A Novel Method for Machine Learning Problems Using Stochastic Recursive Gradient*, arXiv:1703.00102, initial posting 2017-03-01. Algorithm 2 and Section 4. https://arxiv.org/html/1703.00102v2
2. B. Li, M. Ma, G. B. Giannakis, *On the Convergence of SARAH and Beyond*, arXiv:1906.02351, initially posted 2019-06-05. Sections 2–4 and associated convergence theorems. https://arxiv.org/html/1906.02351v2
3. Y. Zhong, J. Li, S. Lahiri, *Probabilistic Guarantees of Stochastic Recursive Gradient in Non-Convex Finite Sum Problems*, arXiv:2401.15890, initially posted 2024-01-29. https://arxiv.org/abs/2401.15890
