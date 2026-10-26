# Gaussian summand counts for every periodic \(f\)-decomposition

## Finding
Let \(f:\mathbb Z_{\ge0}\to\mathbb Z_{\ge0}\) be any periodic function of positive period \(m\). Define \(a_j=1\) for \(j\le0\) and, for \(n\ge1\),
\[
a_n=a_{n-1}+a_{n-1-f(n-1)}.
\]
An \(f\)-legal subset \(S\subseteq\{0,\ldots,n-1\}\) satisfies: whenever \(i\in S\), none of \(i-f(i),\ldots,i-1\) is in \(S\). Indices below zero are ignored. Every integer \(x\in[0,a_n)\) has exactly one expression \(x=\sum_{i\in S}a_i\) using an \(f\)-legal subset. For \(x\) chosen uniformly in that interval, let \(X_n=|S|\).

**Theorem.** There are effectively computable constants \(\mu_f>0\) and \(\nu_f>0\) such that, as \(n\to\infty\),
\[
\mathbb E X_n=\mu_fn+O_f(1),\qquad
\operatorname{Var}(X_n)=\nu_fn+O_f(1),\qquad
\frac{X_n-\mathbb EX_n}{\sqrt{\operatorname{Var}(X_n)}}\ \Longrightarrow\ \mathcal N(0,1).
\]
The same conclusions hold for integers chosen uniformly from the consecutive interval \([a_n,a_{n+1})\), counting the summands in their unique legal decompositions. Thus Gaussian behavior holds for **every** periodic, nonnegative \(f\), without exceptions or a supplementary nondegeneracy condition.

## Assumptions and scope
The period \(m\ge1\) and all values of \(f\) are fixed while \(n\) tends to infinity. Values of \(f\) may be zero and may exceed the period. Put \(F=\max_{0\le j<m}f(j)\). A word of \(n\) binary digits records selected summands \(a_0,\ldots,a_{n-1}\); the statistic counts selected indices, not their arithmetic magnitudes. The interval \([0,a_n)\) includes zero, represented by the empty subset. No assertion is made for nonperiodic functions.

Define a matrix \(T_j(u)\), of size \(F+1\), with row/column indices \(s\in\{0,\ldots,F\}\). For each \(s\), add \(1\) in column \(\min(F,s+1)\); if \(s\ge f(j)\), also add \(u\) in column \(0\). These additions are made even when the two columns coincide (in particular \(F=0\)). Set
\[
P(u)=T_0(u)T_1(u)\cdots T_{m-1}(u).
\]
Let \(\lambda(u)\) be the analytic continuation near \(u=1\) of the Perron eigenvalue of the primitive nonnegative matrix \(P(1)\). The constants are
\[
\mu_f=\frac1m\left.\frac{d}{dt}\log\lambda(e^t)\right|_{t=0},\qquad
\nu_f=\frac1m\left.\frac{d^2}{dt^2}\log\lambda(e^t)\right|_{t=0}>0.
\]
These formulas are a finite-matrix procedure for any supplied period.

## Proof
**1. Exact bijection between integers and legal words.** Let \(B_n\) be the number of legal binary subsets of indices below \(n\), with \(B_n=1\) when \(n\le0\). Splitting according to whether index \(n-1\) is selected gives
\[
B_n=B_{n-1}+B_{n-1-f(n-1)}=a_n.
\]
The usual largest-summand induction establishes the stronger interval property. An illegal repetition cannot occur, and every legal sum with largest index \(j\) lies in \([a_j,a_{j+1})\): lower selected indices are at most \(j-f(j)-1\), whose legal sums fill \([0,a_{j-f(j)})\). The two choices at each stage fill the adjacent intervals \([0,a_j)\) and \([a_j,a_{j+1})\) without overlap. Induction proves the claimed bijection, including the empty sum.

**2. Finite-state counting.** After reading some digits, let the state \(s\) equal the number of consecutive unselected positions since the last selected position, capped at \(F\). Initially \(s=F\), since all positions preceding index zero are unselected. Writing zero moves to \(\min(F,s+1)\); writing one is legal precisely when \(s\ge f(j)\), moves to zero, and contributes the weight \(u\). For \(n=qm+r\), where \(0\le r<m\), the exact summand-count polynomial is
\[
Z_n(u)=\sum_{x=0}^{a_n-1}u^{X_n(x)}
=e_F^{\mathsf T}P(u)^qT_0(u)\cdots T_{r-1}(u)\mathbf1.
\]
Here \(e_F\) is the basis vector for state \(F\), and the empty product is the identity.

**3. Primitivity at every period.** Choose a sufficiently large multiple \(N\) of \(m\). From any initial state, an all-zero word of length \(N\) ends in state \(F\). To end at any state \(s<F\), write zeros until position \(N-s-1\), write a single one there, then write \(s\) zeros. For \(N\ge2F+2\), the position of that one is reached from state \(F\) and is therefore allowed whatever the value of \(f\). This realizes a positive entry between every ordered pair of states in \(P(1)^{N/m}\). Thus \(P(1)\) is primitive, including the one-state case \(F=0\).

**4. Quasi-power and Gaussian limit.** By the Perron–Frobenius theorem and analytic perturbation of a simple eigenvalue, there is a neighborhood of \(t=0\) in which
\[
\mathbb E e^{tX_{qm+r}}=
C_r(t)\left(\frac{\lambda(e^t)}{\lambda(1)}\right)^q(1+O(\theta^q)),
\]
with \(0<\theta<1\), \(C_r\) analytic and nonzero, \(C_r(0)=1\), and error analytic and uniform in a smaller neighborhood. Consequently, defining
\[
\kappa(t)=\log\lambda(e^t)-\log\lambda(1),
\]
we obtain \(\mathbb EX_{qm+r}=q\kappa'(0)+O(1)\) and \(\operatorname{Var}(X_{qm+r})=q\kappa''(0)+O(1)\). Once \(\kappa''(0)>0\) is shown, substitute \(t=i\tau/\sqrt{q\kappa''(0)}\) into the logarithm of this moment-generating function, subtract the exact mean, and expand to second order. The characteristic functions converge to \(e^{-\tau^2/2}\), proving the normal limit. The finitely many possible remainders \(r\) do not change the leading constants.

**5. Strict positivity of the variance.** Regard each legal \(m\)-digit block taking state \(i\) to state \(j\) as a directed edge, carrying the integer reward \(K\) equal to the number of ones in that block. Let \(v\) be a positive right eigenvector of \(P(1)\) with Perron eigenvalue \(\lambda(1)\). Assign to each edge from \(i\) to \(j\) the probability \(v_j/(\lambda(1)v_i)\). The row sums equal one, and the resulting edge-valued Markov chain is finite, irreducible, and aperiodic. Its stationary mean reward per edge is \(\bar K=\kappa'(0)\), and its asymptotic variance per edge is \(\kappa''(0)\).

For completeness, write \(Q\) for this chain's state transition matrix and \(g(i)=\mathbb E[K-\bar K\mid i]\). Since \(g\) has stationary mean zero, the finite-state Poisson equation \((I-Q)h=g\) has a solution. The variables \(\xi=K-\bar K+h(j)-h(i)\) along consecutive transitions are martingale differences. The centered accumulated reward differs from their sum by the bounded boundary term \(h(\text{initial})-h(\text{final})\). Therefore its asymptotic variance equals \(\mathbb E_\pi\xi^2\). If this vanished, every allowed edge would obey \(K-\bar K=h(i)-h(j)\); hence along every closed walk of length \(q\) the total reward would equal \(q\bar K\).

But the all-zero block is a self-loop at state \(F\), of reward zero, forcing \(\bar K=0\). For sufficiently large \(q\), a word of length \(qm\) with a single one followed by at least \(F\) zeros is another allowed closed walk from \(F\) to \(F\), of reward one. This contradicts zero reward on every closed walk. Thus \(\kappa''(0)>0\). The same two closed walks show \(\bar K>0\): the stationary transition law assigns positive probability to a positive-reward edge. This completes the proof of the first assertion.

**6. Intervals between consecutive sequence terms.** For all sufficiently large \(n\), each integer in \([a_n,a_{n+1})\) has its largest summand \(a_n\), with all lower summands indexed below \(n-f(n)\). Subtracting \(a_n\) identifies this interval bijectively with \([0,a_{n-f(n)})\). Hence its summand-count variable has exactly the distribution \(1+X_{n-f(n)}\). Since \(f\) is bounded, the proved limit and the linear mean/variance estimates apply with \(n-f(n)=n+O_f(1)\).

## Verification
The independent finite-counting routes in `verify.py` compare an exhaustive binary-word enumeration, a state-by-state weighted automaton enumeration, and the recurrence for \(a_n\). The script examines 507 (period, length) instances, covering every period of length at most three over \(\{0,1,2\}\) and additional larger-gap patterns. It also checks positivity of a specified power of the unweighted period transition matrix for those patterns. Run `python3 verify.py`; the expected final marker is `VERIFY_OK`. These finite tests do not establish the infinite limit; the Perron, analytic and variance arguments above do.

## Relationship to prior work
Demontigny, Do, Kulkarni, Miller, Moon and Varma (arXiv:1309.5599v1, first public September 22, 2013) prove existence and uniqueness of the associated \(f\)-sequences, a Gaussian limit for a special \(b\)-bin periodic pattern, and explicitly ask in their Section 5, Question (3), whether all periodic \(f\) have Gaussian summand counts. The theorem above addresses that stated gap, replacing the special generating function by a general finite-state weighted count and verifying the nonzero variance for **every** periodic pattern. The corresponding 2014 Kentucky-sequence paper establishes normality for a different single bin rule, but not the full arbitrary-periodic assertion. The 2013 signed Skipponacci paper treats a distinct signed-representation system. Bertoni, Choffrut, Goldwurm and Lonati (2003, Theorems 2–4) establish positive linear variance and a central limit theorem for a symbol count in a fixed finite-state rational language when its one-letter transition matrix is primitive. That powerful general theorem motivates the spectral method and covers homogeneous primitive languages; it does not literally assert the present all-periodic \(f\) theorem: the natural one-digit phase-augmented matrix has period \(m\), whereas the primitive one-period matrix here assigns polynomial block rewards ranging from zero to \(m\), not just a single-letter mark. The present proof supplies the specific primitivity and zero-variance exclusion for every periodic forbidden-gap rule. These differences limit a direct implication from the 2003 theorem; a different coding or an unlocated general statement may nonetheless imply this result, an explicit originality risk.

## Limitations
No independent mathematical audit has been performed. Literature searching cannot rule out an equivalent formulation in works on finite automata, regular languages, or numeration systems; this is the principal originality risk. The theorem assumes a *fixed* finite period and nonnegative integer-valued \(f\). It neither treats arbitrary nonperiodic \(f\) nor supplies a uniform Berry–Esseen estimate as \(f\) varies. Numerical histograms are only consistency checks.

## References
- P. Demontigny, T. Do, A. Kulkarni, S. J. Miller, D. Moon, U. Varma, *Generalizing Zeckendorf's Theorem to f-decompositions*, arXiv:1309.5599v1 (2013), Sections 2, 4 and 5. https://arxiv.org/abs/1309.5599
- M. Catral, P. Ford, P. Harris, S. J. Miller, D. Nelson, *Generalizing Zeckendorf's Theorem: The Kentucky Sequence*, arXiv:1409.0488v1 (2014). https://arxiv.org/abs/1409.0488
- P. Demontigny, T. Do, A. Kulkarni, S. J. Miller, U. Varma, *A Generalization of Fibonacci Far-Difference Representations and Gaussian Behavior*, arXiv:1309.5600v1 (2013). https://arxiv.org/abs/1309.5600
- A. Bertoni, C. Choffrut, M. Goldwurm and V. Lonati, *On the number of occurrences of a symbol in words of regular languages*, Theoretical Computer Science 302 (2003), 431–456, DOI 10.1016/S0304-3975(02)00892-7, Theorems 2–4. https://air.unimi.it/handle/2434/4940
