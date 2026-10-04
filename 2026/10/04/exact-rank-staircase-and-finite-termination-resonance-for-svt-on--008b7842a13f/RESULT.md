# Exact rank staircase and finite-termination resonance for SVT on matching samples
## Finding
Consider the singular value thresholding (SVT) iteration of Cai, Candès, and Shen,
\[
X^k=\mathcal D_\tau(Y^{k-1}),\qquad
Y^k=Y^{k-1}+\delta P_\Omega(M-X^k),\qquad Y^0=0,
\]
with \(\tau>0\) and a constant step \(0<\delta<2\). Suppose the observation set is a matching,
\[
\Omega=\{(i_j,\ell_j):j=1,\ldots,r\},
\]
meaning that all row indices \(i_j\) are distinct and all column indices \(\ell_j\) are distinct. Assume every observed value \(m_j=M_{i_j,\ell_j}\) is nonzero and put \(s_j=|m_j|\).

Then each observed singular direction evolves independently. The exact first iterate at which the \(j\)-th direction is present is
\[
\kappa_j=\left\lfloor\frac{\tau}{\delta s_j}\right\rfloor+2.
\]
Consequently
\[
\operatorname{rank}(X^k)=\#\{j:k\ge\kappa_j\},
\]
so the rank is rigorously nondecreasing on this class. If \(x_j^k\) denotes the positive singular amplitude in that direction, then at activation
\[
0<x_j^{\kappa_j}\le \delta s_j,
\]
and for every \(n\ge0\),
\[
x_j^{\kappa_j+n}-s_j=(1-\delta)^n\bigl(x_j^{\kappa_j}-s_j\bigr).
\]
Thus an activated direction never disappears for \(0<\delta<2\).

At the resonant step \(\delta=1\), every direction reaches its exact observed amplitude after finitely many iterations. Its settling index is
\[
t_j=\left\lceil\frac{\tau}{s_j}\right\rceil+2,
\]
and the whole iteration reaches the fixed point \(P_\Omega(M)\) exactly by
\[
K_*=\max_j t_j
=\left\lceil\frac{\tau}{s_{\min}}\right\rceil+2,
\qquad s_{\min}=\min_j s_j.
\]

## Assumptions and scope
The claim uses the exact-arithmetic iteration printed as equation (2.7) in the SVT paper and the standard singular-value shrinker \(\mathcal D_\tau\). A matching observation pattern is a set of observed entries with no shared row and no shared column. Such a sampled matrix is, after row and column permutations, diagonal on its nonzero block, so its nonzero singular values are exactly the absolute observed entries.

The result is about this structured sampling class and a constant step satisfying \(0<\delta<2\). It does not claim rank monotonicity for arbitrary matrix-completion patterns. The finite-termination statement is specific to \(\delta=1\); for other steps in \((0,2)\), the post-activation law is geometric and is generally not finitely terminating.

## Proof
Write
\[
E_j=\operatorname{sgn}(m_j)e_{i_j}e_{\ell_j}^{\mathsf T}.
\]
Because the observed row indices and column indices are pairwise distinct, the matrices \(E_j\) have mutually orthogonal left singular vectors and mutually orthogonal right singular vectors. Hence every matrix of the form
\[
Y=\sum_{j=1}^r y_jE_j,\qquad y_j\ge0,
\]
has singular values \(y_1,\ldots,y_r\), and
\[
\mathcal D_\tau(Y)=\sum_{j=1}^r (y_j-\tau)_+E_j.
\]
Starting from \(Y^0=0\), the SVT iteration therefore stays in this span. With scalar amplitudes \(y_j^k\ge0\) and \(x_j^k\ge0\), it reduces exactly to
\[
x_j^k=(y_j^{k-1}-\tau)_+,
\qquad
y_j^k=y_j^{k-1}+\delta(s_j-x_j^k).
\]

Before activation, \(x_j^k=0\), so \(y_j^{k-1}=(k-1)\delta s_j\). The first positive amplitude occurs when
\[
(k-1)\delta s_j>\tau,
\]
which is exactly
\[
\kappa_j=\left\lfloor\frac{\tau}{\delta s_j}\right\rfloor+2.
\]
At that iteration,
\[
x_j^{\kappa_j}=(\kappa_j-1)\delta s_j-\tau,
\]
and the definition of the floor gives
\[
0<x_j^{\kappa_j}\le\delta s_j.
\]

Whenever \(x_j^k>0\), shrinkage is on the affine branch and
\[
x_j^{k+1}=y_j^k-\tau
=x_j^k+\delta(s_j-x_j^k).
\]
Therefore the error \(e_j^k=x_j^k-s_j\) obeys
\[
e_j^{k+1}=(1-\delta)e_j^k.
\]
At activation, \(0<x_j^{\kappa_j}\le\delta s_j\). If \(0<\delta\le1\), then \(-s_j<e_j^{\kappa_j}\le0\). If \(1<\delta<2\), then \(-s_j<e_j^{\kappa_j}\le(\delta-1)s_j<s_j\). Thus in all cases
\[
|e_j^{\kappa_j}|<s_j.
\]
Since \(|1-\delta|<1\), every later error has smaller magnitude, so every later amplitude remains strictly positive. This proves both the geometric formula and the exact rank staircase.

For \(\delta=1\), the first active update sends any active amplitude to \(s_j\) in one further step. If \(\tau/s_j\) is an integer, the activation amplitude is already \(s_j\); otherwise it becomes \(s_j\) at the next iterate. These two cases combine as
\[
t_j=\left\lceil\frac{\tau}{s_j}\right\rceil+2.
\]
Taking the maximum over \(j\) gives \(K_*\).

Finally, \(P_\Omega(M)\) is the unique minimizer of the finite-\(\tau\) regularized problem associated with the SVT iteration,
\[
\min_X\ \tau\|X\|_*+\frac12\|X\|_F^2
\quad\text{subject to}\quad P_\Omega(X)=P_\Omega(M).
\]
Indeed, with
\[
Q=\sum_{j=1}^r E_j,
\]
we have \(\|Q\|_2=1\). Every feasible \(X\) therefore satisfies
\[
\|X\|_*\ge\langle Q,X\rangle=\sum_{j=1}^r s_j
=\|P_\Omega(M)\|_*.
\]
Also
\[
\|X\|_F^2\ge\sum_{j=1}^r s_j^2
=\|P_\Omega(M)\|_F^2,
\]
with equality in the Frobenius inequality only when every unobserved entry is zero. Hence the displayed objective has the unique feasible minimizer \(P_\Omega(M)\), agreeing with the fixed point reached at \(\delta=1\).

## Verification
The accompanying `verify.py` replays the scalar reduction with exact rational arithmetic over several threshold, step, and observed-amplitude values, including steps on both sides of \(1\). It verifies the activation formula, the exact geometric error recurrence, positivity after activation, a multi-direction rank staircase, and the finite settling formula for \(\delta=1\). The program returns `VERIFY_OK`.

The finite replay checks the implementation of the formulas but is not used as an infinite proof. The proof above establishes the statement for arbitrary finite matching observation sets and arbitrary real parameters in the stated ranges.

## Relationship to prior work
Cai, Candès, and Shen introduce the SVT iteration and explicitly emphasize that the rank of the iterates is empirically nondecreasing. Their analysis proves convergence for a standard constant-step range, and their implementation discussion derives a first zero-iterate skipping rule by observing how long \(Y^k\) remains below the threshold. Those facts are prior work and are not claimed here.

The contribution here is the full per-direction activation schedule on matching samples, the resulting exact rank formula, the post-activation contraction law, and the \(\delta=1\) finite-termination resonance. The source paper's initial-step calculation concerns the common all-zero phase; it does not provide the later direction-by-direction staircase or the exact settling law on this sampling class.

Linearized-Bregman literature develops related shrinkage and kicking ideas for \(\ell_1\) problems. In particular, Yin analyzes the linearized Bregman method and discusses accelerated variants and parameter updates. That literature motivates checking whether the scalarized SVT dynamics are already implied by a broader support-identification result, but the inspected source material does not state the matching-sample matrix theorem above.

## Limitations
Matching samples are deliberately structured and do not model the overlapping observation graphs used in typical matrix-completion instances. Once two observed entries share a row or column, the singular directions couple and the scalar decomposition used here fails. The theorem therefore supplies an exact solvable class and a benchmark, not a proof of rank monotonicity in general.

A residual originality risk remains that an unindexed thesis, implementation note, or a more specialized linearized-Bregman treatment contains the same matching-sample reduction. Targeted searches for exact SVT activation, rank-staircase, finite-termination, and matching-pattern formulations did not surface such a statement, but failed search is not a proof of novelty.

## References
1. Jian-Feng Cai, Emmanuel J. Candès, and Zuowei Shen, *A Singular Value Thresholding Algorithm for Matrix Completion*, arXiv:0810.3286v1, October 18, 2008; SIAM Journal on Optimization 20 (2010), 1956--1982, DOI 10.1137/080738970.
2. Wotao Yin, *Analysis and Generalizations of the Linearized Bregman Method*, Optimization Online, May 28, 2009; SIAM Journal on Imaging Sciences 3 (2010), 856--877.
3. Shiqian Ma, Donald Goldfarb, and Lifeng Chen, *Fixed point and Bregman iterative methods for matrix rank minimization*, Optimization Online, November 21, 2008.
