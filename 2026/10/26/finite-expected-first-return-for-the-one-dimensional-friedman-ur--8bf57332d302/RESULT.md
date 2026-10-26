# Finite expected first return for the one-dimensional Friedman urn walk

## Finding
Let \(\tau\) be the first return to the origin after the initial draw in the one-dimensional Friedman urn walk. Then
\[
\mathbb E\tau<\infty,\qquad \Pr(\tau>n)=O(n^{-3/2}).
\]
This proves the finite-mean-first-return conjecture stated by Balaji and Mahmoud. The result concerns the first return from the specified initial state, not the existence of a stationary distribution of a time-homogeneous position chain.

## Assumptions and scope
The urn starts with one white ball, no blue balls, and the walker at \(X_0=0\). At each integer time a uniformly chosen ball is replaced and one ball of the opposite color is added. A white (respectively blue) draw moves the walker by \(+1\) (respectively \(-1\). Thus \(X_1=1\) deterministically. Let \(\tau=\inf\{n\ge2:X_n=0\}\), possibly infinity, and for \(n\ge1\) define \(u_n=\Pr(\tau>n)\) and \(A_n=n\mathbb E[X_n\mathbf1_{\{\tau>n\}}]\). The claim applies to every integer \(n\ge1\).

## Proof
**1. Exact urn drift.** After \(n\) draws, the numbers of white and blue balls are \(1+(n-X_n)/2\) and \((n+X_n)/2\). Hence for every attainable position \(x\),
\[
\Pr(X_{n+1}=x+1\mid X_n=x)=\frac{n+2-x}{2(n+1)},\quad
\mathbb E[X_{n+1}\mid X_n=x]=\frac{nx+1}{n+1}.
\]
On \(\{\tau>n\}\), the walker has a positive integer position. A step from position one to zero contributes zero to \(X_{n+1}\mathbf1_{\{\tau>n+1\}}\). Thus, with the walk killed at zero,
\[
(n+1)\mathbb E[X_{n+1}\mathbf1_{\{\tau>n+1\}}]
=n\mathbb E[X_n\mathbf1_{\{\tau>n\}}]+u_n,
\]
so \(A_{n+1}=A_n+u_n\), \(A_1=1\); in particular \(A_n\) is nondecreasing.

**2. Comparison with symmetric gambler's ruin.** When \(x\ge1\), the displayed right-jump probability does not exceed \(1/2\). Using identical independent uniforms for each next-step decision therefore couples the surviving walk, started from \(X_n=x\), below an ordinary simple symmetric random walk started from \(x\), up to the first hit of zero. By the reflection principle, for every positive integer \(x\) and \(m\ge1\),
\[
\Pr_x(\text{simple walk avoids zero through }m)
=\Pr(-x<S_m\le x)\le\frac{2x}{\sqrt{m+1}},
\]
where \(S_m\) is the sum of \(m\) independent fair signs. The last inequality follows from the central-binomial bound \(\sup_k\Pr(S_m=k)\le1/\sqrt{m+1}\) and the fact that the interval contains at most \(2x\) integers. Consequently,
\[
u_{2n}\le\frac{2}{\sqrt{n+1}}\mathbb E[X_n\mathbf1_{\{\tau>n\}}]
=\frac{2A_n}{n\sqrt{n+1}}.
\]

**3. Finite renewal sum by a discrete bootstrap.** Since \(u_j\) is nonincreasing, for every integer \(j\ge2\), setting \(k=\lfloor j/2\rfloor\) gives
\[
u_j\le u_{2k}\le b_j A_k,\qquad
b_j=\frac{2}{k\sqrt{k+1}}.
\]
The series \(\sum_{j\ge2}b_j\) converges. Choose an integer \(J\ge2\) with \(\sum_{j\ge J}b_j\le1/2\). For \(N\ge J\), monotonicity of \(A_n\) and the exact recurrence yield
\[
A_{N+1}=A_J+\sum_{j=J}^{N}u_j
\le A_J+A_{N+1}\sum_{j=J}^{N}b_j
\le A_J+\tfrac12 A_{N+1}.
\]
Therefore \(A_{N+1}\le2A_J\) for all \(N\ge J\). Writing \(M=\sup_{n\ge1}A_n<\infty\), we obtain \(u_{2n}\le2M/(n\sqrt{n+1})\); monotonicity gives the same \(O(n^{-3/2})\) bound at odd times. Thus \(\mathbb E\tau=\sum_{n\ge0}u_n<\infty\). This also forces \(\tau<\infty\) almost surely.

## Verification
A standalone exact-rational dynamic program `verify_friedman.py` computes the surviving position distribution for eighty steps and checks, at each step, the transition probabilities, drift bounds, identity \(A_{n+1}=A_n+u_n\), and distribution mass. Its output is recorded in `verification_output.txt`. The infinite-tail theorem follows analytically from Steps 1–3, not from a finite experiment.

## Relationship to prior work
Balaji and Mahmoud (2026, Section 5) explicitly conjecture finiteness of the one-dimensional Friedman walk's first-return mean based on simulation, while deriving Eulerian-number marginals and recurrence statements. The present proof supplies the conjectured integrability and a quantitative survival bound. Bertoin (2022) investigates first-return tails for elephant random walks; in his standard \(p=0\) setup the first return is deterministic at time two. The Friedman urn's initial one-white/zero-blue configuration instead produces a nontrivial first-return problem; related elephant-walk embeddings make historical general-theorem overlap a residual priority risk. This claim does not assert a new first-order urn marginal law.

## Limitations
The \(n^{-3/2}\) bound is an upper bound; neither a matching lower bound nor an exact asymptotic constant is claimed. The result concerns the specific one-dimensional initialization, not arbitrary initial urn inventories or the two-dimensional question. The position process is time-inhomogeneous; finite initial first-return expectation is not equated with invariant-law positive recurrence. Independent review has not been performed.

## References
1. S. Balaji and H. Mahmoud, *Urn-driven random walks*, first public arXiv:2504.14813 (21 April 2025), Discrete Mathematics & Theoretical Computer Science 28 (2026), DOI: 10.46298/dmtcs.15546. See Sections 4–5.
2. J. Bertoin, *Counting the zeros of an elephant random walk*, arXiv:2105.09569 (2021), concerning elephant-walk return times and their initial-condition dependence.
3. Classical reflection principle and the central-binomial point-mass bound for simple symmetric random walk.
