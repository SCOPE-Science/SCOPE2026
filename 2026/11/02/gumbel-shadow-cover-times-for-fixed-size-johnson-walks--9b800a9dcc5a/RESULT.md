# Gumbel shadow-cover times for fixed-size Johnson walks

## Finding
Fix integers \(1\le s<r\). Let \(H_0\) be a uniformly random \(r\)-subset of \([n]\), and independently at each transition remove a uniformly random member of \(H_t\) and replace it with a uniformly random member of \([n]\setminus H_t\). Write \(T_n\) for the first transition index at which **every** \(s\)-subset of \([n]\) has occurred inside at least one of \(H_0,\ldots,H_{T_n}\). Set
\[
m_n=\binom ns,\qquad \beta=\binom{r-1}{s-1},\qquad a_n=\frac{m_n}{\beta}.
\]
Then, as \(n\to\infty\) with \(r,s\) fixed,
\[
\Pr\!\left\{\frac{T_n}{a_n}-\log m_n\le x\right\}\longrightarrow \exp(-e^{-x})\qquad(x\in\mathbb R),
\]
and
\[
\mathbb ET_n\sim a_n\log m_n=\frac{r}{s\binom rs}\binom ns\log\binom ns.
\]
More precisely, if \(U_n(x)\) counts \(s\)-subsets not encountered through time \(\lfloor a_n(\log m_n+x)\rfloor\), then \(U_n(x)\Rightarrow\mathrm{Poisson}(e^{-x})\). The case \(r=3,s=2\) has scale \(a_n=\binom n2/2\) and mean cover time asymptotic to \(n^2\log n/2\). The claimed regime is **fixed \(r,s\)**; no assertion is made for parameters growing with \(n\).

## Assumptions and scope
The chain is the non-lazy simple walk on Johnson graph \(J(n,r)\); its stationary law is uniform on \(\binom{[n]}r\). The initial law is stationary. One time unit is one replacement. Using a count of visited rounds instead of a count of transitions shifts \(T_n\) by one, immaterial in the limits. For the proof we assume \(n\) is sufficiently large, depending only on fixed \(r,s\). The methods below also extend to the previously understood diagonal \(r=s\), but only the strict inequality is asserted as the new finding.

## Proof
**Step 1: a finite forbidden-shadow chain.** Fix \(k\ge1\), independent of \(n\), and distinct target sets \(F_1,\ldots,F_k\in\binom{[n]}s\). Put \(S=\bigcup_i F_i\), \(d=|S|\le ks\), and \(B_t=H_t\cap S\). Its state space consists of subsets \(B\subseteq S\) with \(|B|\le r\). For each such \(B\), write \(b=|B|\) and \(w=n-d-r+b\). In one step its transition probabilities include
\[
P_n(B,B\setminus\{u\})=\frac{w}{r(n-r)}\ (u\in B),\quad
P_n(B,B\cup\{v\})=\frac{r-b}{r(n-r)}\ (v\in S\setminus B),
\]
\[
P_n(B,(B\setminus\{u\})\cup\{v\})=\frac{1}{r(n-r)}\ (u\in B,\ v\in S\setminus B),\quad
P_n(B,B)=\frac{(r-b)w}{r(n-r)},
\]
with all other transitions zero (and coinciding cases added when appropriate). The stationary mass of each individual state \(B\) is \(\pi_n(B)=\binom{n-d}{r-b}/\binom nr\). Since \(r,s,k\) are fixed, these form bounded-dimensional matrices. As \(n\to\infty\), \(P_n\) tends to the chain that removes each present element of \(S\) with probability \(1/r\) and otherwise stays put. The state \(\varnothing\) is its unique absorbing state, and the remaining eigenvalues are \(1-b/r\) with \(1\le b\le r\). Thus \(I-P_n\) has a uniformly bounded inverse on the row-vector subspace of total mass zero for all sufficiently large \(n\).

**Step 2: one-step flux and the leading killed eigenvalue.** Declare a state forbidden when it contains at least one \(F_i\), and let \(A\) denote the corresponding state set; let \(Z=A^c\). Let \(Q_n=P_n|_{Z\times Z}\), with Perron root \(\lambda_{n,F}\). Its stationary entrance flux is
\[
\phi_{n,F}=\Pr_{\pi_n}(B_0\in Z,B_1\in A)
=\Pr_{\pi_n}(B_0\in A,B_1\in Z),
\]
where the equality follows from detailed balance. For any specified \(F_i\), \(\Pr_{\pi_n}(F_i\subseteq H_0)=\binom rs/\binom ns\). A triple or higher multiple overlap among two *distinct* forbidden targets requires at least \(s+1\) specified vertices and has probability \(O_{r,s,k}(n^{-s-1})\). Conditional on a state containing exactly one target \(F_i\), the probability of leaving the forbidden set at the next step is \(s/r+O_{r,s,k}(n^{-1})\): one must remove a member of \(F_i\), and replacing it by another prescribed vertex capable of completing another target has probability \(O(n^{-1})\). Consequently,
\[
\phi_{n,F}=\frac{k(s/r)\binom rs}{\binom ns}+O_{r,s,k}(n^{-s-1})
=\frac{k\beta}{m_n}+O_{r,s,k}(n^{-s-1}). \tag{1}
\]
The killed chain is irreducible on \(Z\) for large \(n\) because every safe set can shed its special vertices and be rebuilt by adding special vertices along safe subsets. It is reversible with respect to the restriction of \(\pi_n\). Its variational Rayleigh quotient at the constant function shows
\[
1-\lambda_{n,F}\le \frac{\phi_{n,F}}{\pi_n(Z)}=O_{r,s,k}(n^{-s}). \tag{2}
\]
Let \(\nu\) be its normalized positive left Perron eigenvector, extended by zero on \(A\). Then \(\nu P_n-\nu\) has negative mass \(-(1-\lambda_{n,F})\nu\) on \(Z\) and positive total mass \(1-\lambda_{n,F}\) on \(A\), so its total variation norm is \(O(n^{-s})\). The bounded inverse for \(I-P_n\) on mean-zero rows therefore implies \(\|\nu-\pi_n\|_1=O_{r,s,k}(n^{-s})\). From a safe state, entering \(A\) in one replacement requires inserting a designated missing vertex, so \(\sup_{B\in Z}P_n(B,A)=O_{r,s,k}(n^{-1})\). Thus
\[
1-\lambda_{n,F}=\nu P_n(A)
=\phi_{n,F}+O_{r,s,k}(n^{-s-1})
=\frac{k\beta}{m_n}+O_{r,s,k}(n^{-s-1}). \tag{3}
\]
This argument does **not** assume that overlapping targets behave independently.

**Step 3: uniform survival probabilities.** The matrix \(Q_n\) converges to the pure-deletion matrix on the downward-closed safe states. That limiting matrix has a simple eigenvalue \(1\), with every other eigenvalue among \(1-b/r\), \(b\ge1\). Standard finite-matrix spectral projection around the isolated eigenvalue \(1\) gives constants \(C=C(r,s,k)\) and \(\rho=\rho(r,s,k)<1\) such that, with the stationary initial distribution,
\[
\Pr\{F_i\not\subseteq H_j\ \forall i\le k,\ 0\le j\le t\}
=c_{n,F}\lambda_{n,F}^{t}+O_{r,s,k}(\rho^t), \tag{4}
\]
where \(c_{n,F}=1+O_{r,s,k}(n^{-1})\). All error constants are uniform in the choice of the distinct targets: for fixed \(k,s\), there are only finitely many intersection patterns up to relabeling. Equation (4) follows either by a fixed-radius resolvent contour enclosing the remaining spectrum or by the corresponding finite-dimensional spectral decomposition; it does not assert that the subleading eigenvalues are all simple.

**Step 4: factorial moments and cover time.** For fixed real \(x\), set \(t_n(x)=\lfloor a_n(\log m_n+x)\rfloor\). By (3)--(4), uniformly over fixed distinct targets,
\[
\Pr\{F_1,\ldots,F_k\text{ all unseen through }t_n(x)\}
=m_n^{-k}e^{-kx}(1+o(1)), \tag{5}
\]
because \(t_n(x)O(n^{-s-1})=O((\log n)/n)=o(1)\). Hence the number \(U_n(x)\) of unseen \(s\)-subsets satisfies
\[
\mathbb E[(U_n(x))_k]=(m_n)_k m_n^{-k}e^{-kx}(1+o(1))\longrightarrow e^{-kx}
\]
for each fixed positive integer \(k\). The factorial-moment theorem (or Bonferroni bounds) yields the Poisson limit, and \(\{T_n\le t_n(x)\}=\{U_n(x)=0\}\) gives the Gumbel law.

**Step 5: the expectation.** The Gumbel convergence implies \(T_n/(a_n\log m_n)\to1\) in probability, and therefore the expected cover time is at least \((1-o(1))a_n\log m_n\). For fixed \(\varepsilon>0\), use a union bound after \(t_0=\lceil(1+\varepsilon)a_n\log m_n\rceil\) and (4) with \(k=1\):
\[
\sum_{t\ge t_0}\Pr(T_n>t)
\le C m_n\left(\frac{\lambda_{n,1}^{t_0}}{1-\lambda_{n,1}}+
\frac{\rho^{t_0}}{1-\rho}\right)
=O(a_n m_n^{-\varepsilon/2})=o(a_n\log m_n).
\]
It follows that \(\limsup \mathbb ET_n/(a_n\log m_n)\le1+\varepsilon\), and \(\varepsilon\downarrow0\) proves the expectation asymptotic.

## Verification
Run `python verify.py` with Python 3 and NumPy. The program forms exact rational transition matrices for the projected killed chain, compares survival probabilities against independently generated full Johnson-graph trajectories at six small configurations, and checks the predicted leading eigenvalue rate for six single- and multiple-target patterns at three larger sizes. The executed program reported **556 passing assertions/checks**. Exact finite computations do not establish the all-\(n\) theorem; Steps 1--5 are the proof. The numerical eigenvalue comparisons are asymptotic diagnostics and not certified infinite bounds.

## Relationship to prior work
Athreya, S. Mukherjee, and S. S. Mukherjee formulated the first-order Markovian super-coupon cover-time asymptotic as Conjecture 2.4 and proved its diagonal case \(r=s\) (Theorem 2.5). Their independent-round model has a Gumbel limit, but that independence is not available for the Johnson walk. The present result proves Conjecture 2.4 for **all fixed strict pairs \(1\le s<r\)** and adds the associated Poisson/Gumbel law. Godbole and Janson studied independently sampled random covering designs, not Markovian successive blocks. General finite-state Markov hitting-time and Perron--Frobenius methods underlie this argument, but the required uniform comparisons of overlapping missing subsets and the resulting cover constant are derived explicitly here. No claim of absolute literature priority or external audit is made.

## Limitations
The proof requires \(r,s\) and the factorial-moment order to remain fixed while \(n\to\infty\). It does not give an explicit total-variation convergence rate for the count of missed subsets, a centered expectation correction of order \(a_n\), or results for \(r=r(n)\), \(s=s(n)\). The initial \(r\)-set is uniform; arbitrary deterministic initializations are not addressed here. The factorial-moment argument is not a finite enumeration. Historical priority and independent verification remain open.

## References
1. S. Athreya, S. Mukherjee, and S. S. Mukherjee, *On a generalisation of the coupon collector problem*, arXiv:2304.01145 (first posted 2023-04-03; v2, 2023-09-12), Conjecture 2.4 and Theorems 2.3, 2.5. https://arxiv.org/pdf/2304.01145
2. S. Athreya, S. Mukherjee, and S. S. Mukherjee, *On a Generalisation of the Coupon Collector Problem*, Journal of Theoretical Probability 38, article 54 (2025), DOI: 10.1007/s10959-025-01417-w. https://link.springer.com/article/10.1007/s10959-025-01417-w
3. A. P. Godbole and S. Janson, *Random covering designs*, Journal of Combinatorial Theory, Series A 75 (1996), 85--98, DOI: 10.1006/jcta.1996.0065. https://digitalcommons.mtu.edu/michigantech-p/3964/
