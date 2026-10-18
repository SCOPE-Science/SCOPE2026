# A weak limit for the root-doubling recursive tree via a contracting jump chain

## Finding

Let \(B_n\) be the number of non-root vertices after \(n\) steps in the root-doubling random recursive tree of Björnberg and Mailler, initially \(B_0=0\). Then **the full sequence** has a nondegenerate weak limit
\[
\frac{B_n}{n}\ \Rightarrow\ X_\infty.
\]
The limit is the **unique invariant law** \(\pi\) of the piecewise-deterministic Markov process on \([1,\infty)\) with drift \(\dot x=1-x\), jumps \(x\mapsto2x\) at rate \(1/x\), and generator
\[
\mathcal A f(x)=(1-x)f'(x)+\frac{f(2x)-f(x)}{x}.
\]
It admits an explicit distributional construction. Let \(U_1,U_2,\ldots\) be independent uniforms on \((0,1)\), and let \(Z\) have the unique stationary law of the contracting iteration
\[
Z_{j+1}=\frac{1-U_{j+1}+U_{j+1}Z_j}{2},\qquad 0<Z_j\le\frac12.
\]
Take \(Z\) independent of a further uniform \(U\), set \(H=1/Z\) and
\[
T=\log\!\left(1+H\frac{1-U}{U}\right).
\]
For every bounded measurable \(f\), the limit law is described by
\[
\int f(x)\,\pi(dx)
=\frac{\mathbb E\!\left[\int_0^T f(1+(H-1)e^{-s})\,ds\right]}{\mathbb E T}.
\]
In particular \(\mathbb E X_\infty=2\) and \(\operatorname{Var}(X_\infty)=1\), and all its moments equal the previously computed constants
\[
\mathbb E X_\infty^k=\prod_{j=1}^k\frac{j-1+2^j}{j}\quad (k\ge1).
\]
The new assertion is **weak convergence and identification of the law**, not discovery of the moment values.

## Assumptions and scope

At each integer step, independently conditionally on the current finite rooted tree, choose one of its vertices uniformly. If the root is chosen, attach two copies of the entire current rooted tree beneath a fresh root; otherwise attach a single child to the selected non-root vertex. \(B_n\) counts all non-root vertices, so the root-choice update is \(B_{n+1}=2B_n+2\), and the other update is \(B_{n+1}=B_n+1\). The statement concerns this original root-only, unweighted, discrete-time model, and convergence in distribution on \([1,\infty)\). It does not assert almost-sure convergence.

## Proof

**1. Exact chain and tightness.** Conditionally on \(B_n=b\),
\[
B_{n+1}=\begin{cases}b+1,&\text{with probability }b/(b+1),\\2b+2,&\text{with probability }1/(b+1).\end{cases}
\]
Consequently the conditional expected increment is exactly \(2\), so \(\mathbb E B_n=2n\). Since \(B_n\ge n\), the normalized variables \(X_n=B_n/n\) lie in \([1,\infty)\), and \(\sup_n\mathbb P(X_n>R)\le2/R\). The exact conditional squared-increment identity \(\mathbb E[(B_{n+1}-B_n)^2\mid B_n=b]=b+4\) additionally gives \(\mathbb E B_n^2=5n^2-n\).

**2. Exact logarithmic-grid structure.** Put \(\delta_n=\log((n+1)/n)\), and \(\phi_t(x)=1+(x-1)e^{-t}\). An ordinary update gives \(X_{n+1}=\phi_{\delta_n}(X_n)\), while a root event gives \(X_{n+1}=2\phi_{\delta_n}(X_n)\). The latter has probability \(1/(nX_n+1)\). For the proposed continuous-time process started at \(x\), the probability of no jump on \([0,t]\) is
\[
\exp\left[-\int_0^t\frac{ds}{\phi_s(x)}\right]
=\frac{x}{e^t+x-1}.
\]
At \(t=\delta_n\) this yields **exactly** \(\mathbb P(\text{at least one jump})=1/(nx+1)\), the discrete root-event probability. If one jump occurs at some \(s\le\delta_n\), the final continuous state is \(1+2(x-1)e^{-\delta_n}+e^{s-\delta_n}\), whereas the discrete post-jump state is \(2+2(x-1)e^{-\delta_n}\); the difference is at most \(1-e^{-\delta_n}\le\delta_n\). Two or more continuous jumps in this interval occur with probability at most \(\delta_n^2/2\) because every jump intensity is at most \(1\). On any fixed logarithmic-time interval \([0,T_0]\), couple intervals using these common first-jump events. For starting states in \([1,R]\), the number of jumps is dominated by a Poisson variable of mean \(T_0+1\) in a standard rate-one dominating-clock construction; on an event with at most \(K\) jumps the states remain in a bounded interval depending only on \(R,K,T_0\). The flow and jump map are Lipschitz on that interval, and a mismatch in first-jump decisions from discrepant starting states has conditional probability at most \(C_{R,K}\delta_n\) times their state discrepancy, by differentiating \(1/(nx+1)\). Summing the local \(O(\delta_n)\) displacements only on jump intervals and the \(O(\delta_n^2)\) multiple-jump errors, then using a discrete Grönwall bound, gives convergence of transition expectations uniformly over \(x\in[1,R]\): for any bounded Lipschitz \(f\) and fixed \(T_0\),
\[
\sup_{x\in[1,R]}\left|\mathbb E_x f(X_{\lfloor ne^{T_0}\rfloor}^{(n)})-P_{T_0}f(x)\right|\longrightarrow0,
\]
where \(X^{(n)}\) denotes the normalized discrete chain started at time \(n\) with value \(x\), and \(P_t\) is the continuous semigroup. Indeed \(\sum_{j\ge n}\delta_j^2=O(1/n)\); the fixed \(K\) event carries all but arbitrarily small probability. Integer rounding of the terminal time changes the limit by at most one further vanishing step. This argument also applies uniformly to starting states in the actual reachable lattice within \([1,R]\).

**3. Unique attracting invariant law.** The continuous process is nonexplosive: its total jump rate is at most one, and its flow stays in \([1,\infty)\). Its generator satisfies
\[
\mathcal A V(x)=2-x,\qquad V(x)=x,
\]
and hence \(P_tV(x)=2+(x-2)e^{-t}\). Fix \(R>4\), and then \(t_*\) sufficiently large that \(e^{t_*}>2R-1\) and the Foster drift outside \([1,R]\) is strict. Starting from any \(x\in[1,R]\), the event of **exactly one jump** by \(t_*\), at time \(s\in(0,t_*)\), leads to endpoint
\[
1+2(x-1)e^{-t_*}+e^{s-t_*}.
\]
Because the jump hazard is positive and bounded above and below on the relevant compact trajectories, its density has a uniform positive lower bound on the common open interval \((1+(2R-1)e^{-t_*},2)\), which lies inside \([1,R]\). Thus \([1,R]\) is a small set for the \(t_*\)-skeleton, and that skeleton is aperiodic with the usual irreducibility in its accessible class. The displayed strict linear drift and small-set minorization give, by the standard split-chain regeneration/Foster–Lyapunov argument, a unique invariant probability \(\pi\) and
\[
\sup_{x\in[1,R]}\|P_t(x,\cdot)-\pi\|_{\mathrm{TV}}\longrightarrow0
\quad(t\to\infty).
\]
This reasoning does not use moment determinacy.

**4. Convergence of the whole discrete sequence.** Let \(f\) be bounded Lipschitz and \(\epsilon>0\). Choose \(R\) with \(2/R<\epsilon\), then choose \(T_0\) so that \(\sup_{x\in[1,R]}|P_{T_0}f(x)-\pi(f)|<\epsilon\). For large \(N\), write \(n=\lfloor Ne^{-T_0}\rfloor\), so \(N/n\to e^{T_0}\). Condition on \(X_n\), use the finite-horizon approximation in step 2 on \([1,R]\), and control the complement by \(\mathbb P(X_n>R)\le2/R\). This shows \(\limsup_{N\to\infty}|\mathbb Ef(X_N)-\pi(f)|\le(1+4\|f\|_\infty)\epsilon\). As \(\epsilon\) is arbitrary, \(X_N\Rightarrow\pi\).

**5. Explicit occupation law.** Starting at a post-jump location \(H\ge2\), the no-jump survival law in step 2 gives the waiting time \(T=\log(1+H(1-U)/U)\). The pre-jump location is \(H/[U+H(1-U)]\); thus the reciprocal of the next post-jump location obeys
\[
Z'=\tfrac12(1-U+UZ).
\]
For the same uniforms, the distance between two reciprocal trajectories contracts by a factor at most \(1/2\) per jump. This yields a unique stationary post-jump reciprocal law. Moreover \(Z'\ge(1-U)/2\) implies \(\mathbb E|\log Z|<\infty\); the inequality \(T\le\log H-\log U\) proves \(0<\mathbb ET<\infty\). The normalized expected occupation measure of the stationary jump cycles is invariant: integrating \(\mathcal A f\) over a cycle cancels the continuous-flow endpoint difference with the jump compensator and leaves \(\mathbb E[f(H')-f(H)]=0\). Uniqueness identifies it with \(\pi\).

**6. Moments.** The prior exact moment asymptotics of Björnberg–Mailler and bounded higher moments give uniform integrability of each fixed power; weak convergence then transfers those previously known moments to \(\pi\). In particular its mean is \(2\) and its second moment \(5\), hence variance \(1\). Alternatively these identities follow by integrating \(\mathcal A x^k=(k-1+2^k)x^{k-1}-kx^k\) against \(\pi\) after truncation and the established finite-moment bounds.

## Verification

`verify.py` is standalone and uses only the Python standard library. It checks the exact two-branch transition probabilities, first and second moment identities for finite \(n\), the inverse-affine jump map and the one-step no-jump probability formula, and the stationary moment recurrence. Its finite computations are diagnostics; the all-\(n\) and weak-limit arguments are the analytical steps above.

## Relationship to prior work

Björnberg and Mailler, *A random recursive tree model with doubling events* (arXiv:2501.18466; first public January 30, 2025), Proposition 1.1(a) proves the limiting moment formula and tightness. **Remark 1.2 explicitly states that weak convergence is not established**, because the growth of those moments defeats the usual Carleman argument. The present result closes precisely that gap by using logarithmic-time Markov-process dynamics and regeneration rather than moment uniqueness. Their height and degree results are different observables. General stationary-law theory for state-dependent-intensity piecewise-deterministic processes (e.g. Czapla, arXiv:2303.11576) gives background tools for the auxiliary process but does not by itself identify the discrete root-doubling tree's limiting distribution.

## Limitations

The claim is weak convergence of the **root-only** doubling model, not convergence almost surely or in total variation (the finite-\(n\) laws are atomic). It provides no explicit Lebesgue density, rate of weak convergence, or assertion that the moment sequence determines its distribution. It does not cover doubling events at arbitrary vertices. The regeneration argument uses standard Harris/Doeblin theory, and the stochastic approximation step requires the stated uniform finite-horizon coupling; neither a finite simulation nor knowledge of the limiting moments alone proves weak convergence.

## References

1. J. E. Björnberg and C. Mailler, *A random recursive tree model with doubling events*, arXiv:2501.18466, first posted 2025-01-30. Full open text: https://arxiv.org/html/2501.18466v3 . See Proposition 1.1, Remark 1.2 and Section 2.1.
2. D. Czapla, *On the Existence and Uniqueness of Stationary Distributions for Some Piecewise Deterministic Markov Processes With State-Dependent Jump Intensity*, arXiv:2303.11576 (2023), https://arxiv.org/abs/2303.11576 . General background; an identical tree-size theorem is not claimed there.
3. S. P. Meyn and R. L. Tweedie, *Markov Chains and Stochastic Stability*, 2nd ed., Cambridge University Press (2009), Chapter 15, for geometric drift/minorization criteria.
