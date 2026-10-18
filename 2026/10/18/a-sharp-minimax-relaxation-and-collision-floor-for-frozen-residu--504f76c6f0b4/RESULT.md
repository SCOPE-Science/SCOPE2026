# A sharp minimax relaxation and collision floor for frozen residual-weighted Kaczmarz batches

## Finding

Let \(d\ge2\) and \(k\ge1\) be integers. For the consistent identity system \(Ix=b\) in \(\mathbb R^d\), write \(e=x-b\ne0\). Select \(k\) rows independently **from the same frozen residual** with probabilities
\[
 p_i=\frac{e_i^2}{\|e\|_2^2},\qquad i=1,\ldots,d.
\]
All selected row corrections use this frozen residual. Their contributions are added, with per-correction relaxation \(\beta\ge0\). Let \(N_i\) denote the number of selections of row \(i\), so \(N\sim\operatorname{Multinomial}(k,p)\) and \(e_i^+=(1-\beta N_i)e_i\).

**Theorem.** The sharp worst-start, conditional one-batch expected squared-error factor is
\[
 \mathcal R_{d,k}(\beta)
 :=\sup_{e\ne0}\frac{\mathbb E[\|e^+\|_2^2\mid e]}{\|e\|_2^2}
 =\max\left\{
 (1-k\beta)^2,
 1-\frac{2k}{d}\beta+\frac{k(d+k-1)}{d^2}\beta^2
 \right\}.
\]
Every worst-case factor is witnessed either by a residual supported on a single coordinate or by a residual whose coordinates all have equal absolute magnitude.

Define the transition inequality
\[
 k(d-1)\le 2d-1.
\]
There is **exactly one** minimax relaxation over all \(\beta\ge0\):
\[
 \boxed{\displaystyle
 \beta_*=\begin{cases}
 \frac{d}{d+k-1},&k(d-1)\le2d-1,\\[4pt]
 \frac{2d}{k(d+1)-1},&k(d-1)>2d-1.
 \end{cases}}
\]
The sharp minimized expected squared-error factor is
\[
 \boxed{\displaystyle
 \mathcal R_{d,k}(\beta_*)=\begin{cases}
 \frac{d-1}{d+k-1},&k(d-1)\le2d-1,\\[4pt]
 \left(\frac{k(d-1)+1}{k(d+1)-1}\right)^2,&k(d-1)>2d-1.
 \end{cases}}
\]
Moreover, \(\mathcal R_{d,k}(\beta)<1\) **if and only if** \(0<\beta<2/k\). With an independent fresh batch at each round and probabilities recomputed from the new residual, every such choice gives the geometric mean-square upper bound \(\mathbb E\|e^{(t)}\|_2^2\le\mathcal R_{d,k}(\beta)^t\|e^{(0)}\|_2^2\) for integers \(t\ge0\).

For fixed \(d\), the best worst-case *one-batch* factor has the strictly positive concurrency limit
\[
 \lim_{k\to\infty}\min_{\beta\ge0}\mathcal R_{d,k}(\beta)
 =\left(\frac{d-1}{d+1}\right)^2.
\]
In contrast, if every row is chosen with fixed uniform probability \(1/d\) independently of the residual, the exact optimal worst-case single-batch factor is \((d-1)/(d+k-1)\to0\). Thus residual-conditioned sampling has an intrinsic collision-limited one-batch minimax floor, even though either policy can converge under repeated, appropriately relaxed batches.

## Assumptions and scope

This is a fully synchronous **frozen-snapshot additive** batch: each of the \(k\) independent selectors sees the same residual, computes its correction from that residual, and all corrections add. The rule is not the sequential or live-read Kaczmarz algorithm, a block orthogonal projection, or a policy that recomputes the residual after each within-batch update. There is no division by \(k\) in the displayed update; multiplying the update by \(1/k\) simply reparametrizes \(\beta\). All arithmetic is exact, the identity rows have unit length, and the system is consistent. Probabilities are defined whenever \(e\ne0\); at \(e=0\) the method has reached the solution and stops. The expectation is only over the independent draws within a batch, conditional on its starting error.

## Proof

**1. Exact multinomial moment.** Since \(N_i\sim\operatorname{Binomial}(k,p_i)\),
\[
 \mathbb E N_i=kp_i,\qquad
 \mathbb E N_i^2=kp_i+k(k-1)p_i^2.
\]
Set \(S_j(p)=\sum_i p_i^j\). Substituting \(e_i^2/\|e\|_2^2=p_i\) gives the exact identity
\[
 \frac{\mathbb E[\|e^+\|_2^2\mid e]}{\|e\|_2^2}
 =1-k(2\beta-\beta^2)S_2(p)+k(k-1)\beta^2 S_3(p).\tag{1}
\]
Every probability vector in the closed simplex is realized by a real error vector, by taking \(e_i=\sqrt{p_i}\).

**2. Cubic-simplex extremal lemma.** For every \(d\ge2\), \(a\ge0\), and real \(b\), the maximum of \(aS_3(p)-bS_2(p)\) over the \(d\)-simplex is attained either at \(p=(1/d,\ldots,1/d)\) or at a vertex. To see this, choose a maximizer having as few positive entries as possible. For any pair of its positive entries \(u,v\), keep their sum \(s=u+v\) fixed and vary their split. Their contribution to the objective equals
\[
 a(u^3+v^3)-b(u^2+v^2)
 =as^3-bs^2+(2b-3as)uv.\tag{2}
\]
If \(2b-3as>0\), replacing distinct \(u,v\) by equal halves strictly increases the objective. If it is negative, merging them strictly increases the objective. If it is zero, merging leaves the objective unchanged but decreases the positive support, contradicting the maximizer's support minimality. Consequently all positive entries are equal. If there are \(m\) of them, the objective is \(a/m^2-b/m\). As a convex function of \(1/m\in[1/d,1]\), this is at most the maximum of its values at \(m=d\) and \(m=1\), proving the lemma. The argument includes \(a=0\), and imposes no sign restriction on \(b\).

Apply this lemma to (1) with \(a=k(k-1)\beta^2\) and \(b=k(2\beta-\beta^2)\). At a vertex (1) becomes \((1-k\beta)^2\). At the uniform vector it becomes \(1-2k\beta/d+k(d+k-1)\beta^2/d^2\). Both witness vectors are attainable, so their maximum is not merely a bound: it is the exact sharp factor.

**3. Unique global minimax step.** Denote the vertex and uniform quadratics by \(V(\beta)\) and \(U(\beta)\), respectively. Their difference factors exactly as
\[
 U(\beta)-V(\beta)
 =\frac{k(d-1)\beta}{d^2}
 \left(2d-[k(d+1)-1]\beta\right).\tag{3}
\]
For positive \(\beta\), they cross at \(\beta_c=2d/[k(d+1)-1]\). The uniform quadratic has its unique minimum at \(\beta_u=d/(d+k-1)\), and the vertex quadratic has its minimum at \(1/k<\beta_c\). Equation (3) shows that the upper envelope is \(U\) before \(\beta_c\) and \(V\) after it. Therefore its unique global minimizer is \(\min\{\beta_u,\beta_c\}\). The inequality \(\beta_u\le\beta_c\) is equivalent to \(k(d-1)\le2d-1\). Substitution yields both displayed branches, including equality at the transition. The zero step and all sufficiently large steps give factor at least one, so there is no boundary minimizer overlooked.

**4. Sharp strict-contraction window.** If \(\beta\le0\) or \(\beta\ge2/k\), a vertex residual gives squared factor at least one (for the stated domain \(\beta\ge0\), the first case is \(\beta=0\)). Conversely, when \(0<\beta<2/k\), both \(V(\beta)<1\) and \(U(\beta)<1\), since \(2/k\le2d/(d+k-1)\). The exact envelope is then strictly below one. Conditioning on each new batch starting error and iterating proves the claimed geometric mean-square bound.

**5. Concurrency limit and fixed-uniform comparison.** For every fixed \(d\ge2\), the second branch applies for all sufficiently large \(k\). Dividing its numerator and denominator by \(k\) gives the stated positive limit. Under fixed-uniform row selection, \(N_i\sim\operatorname{Binomial}(k,1/d)\), independently of the current error. Every coordinate has the same expected squared multiplier \(U(\beta)\). Thus its exact minimax value is \(U(\beta_u)=(d-1)/(d+k-1)\), which tends to zero. No claim about wall-clock speed, individual trajectories under general asynchronous scheduling, or the exact long-run optimal rate follows from this comparison.

## Verification

The standalone file `verify.py` requires only Python 3 and reproduces the multinomial moment independently by enumerating all count vectors; it checks exact rational simplex cases, both maximizing witnesses, sharp minimax branches and strict local uniqueness over extensive dimension and batch ranges, and an independent seeded multinomial Monte Carlo experiment. Running `python verify.py` on the embedded file produces `ALL_CHECKS_PASSED 98917`. The Monte Carlo example at \(d=3\), \(k=6\), \(\beta=\beta_*\), and \(p=(0.61,0.25,0.14)\) yielded approximately \(0.264191\) against the exact conditional factor \(0.264518\). The proof above, not the finite verification grid, establishes the quantifiers for all \(d\), \(k\), and \(\beta\).

Three small exact checkpoints are: at \((d,k)=(2,2)\), \(\beta_*=2/3\) with factor \(1/3\); at \((d,k)=(2,4)\), \(\beta_*=4/11\) with factor \(25/121\); and at \((d,k)=(3,3)\), \(\beta_*=6/11\) with factor \(49/121\).

## Relationship to prior work

Coleman's 2026 analyses of residual-power sampling and asynchronous Kaczmarz explain the tension between residual concentration and colliding stale updates, but study synchronous single-coordinate progress and measured lock-free hardware behavior rather than the exact minimax one-batch law under an explicitly frozen shared residual [1,2]. The source's use of \(\ell=2\) corresponds to the squared-residual probabilities in this theorem. Tondji and Lorenz analyze minibatch-averaged Kaczmarz updates, including relaxation choices for fixed, row-norm-based sampling [3]. Their fixed sampling is not the state-dependent sampling in (1); the fixed-uniform comparator above matches the corresponding simple orthogonal specialization after normalization. The new claim is the exact all-dimension endpoint extremal law, its phase transition and unique minimax relaxation, and the nonzero best-one-batch concurrency floor for residual-conditioned frozen snapshots. It does not claim originality for Kaczmarz, multinomial moments, collision phenomena, or classical averaging algorithms.

## Limitations

The identity system is the orthogonal, condition-one benchmark; correlated rows, heterogeneous normalization, nonlinearity, and stale reads of different ages can behave differently. The probabilities depend on the **current** initial residual of each batch, but within a batch every update uses that same old value. In particular, the theorem must not be applied to live residual reads or sequential updates. The positive limit is for the worst single-batch expected squared-error ratio; it is **not** a lower bound on accuracy after repeatedly refreshed batches. The Monte Carlo checks do not certify infinite-domain extrema independently of the algebraic argument. Relevant unindexed treatments of snapshot minibatches or general stochastic mirror-descent equivalences may contain equivalent consequences; independent bibliographic validation has not been performed.

## References

[1] Evan Coleman, *Residual-Weighted Randomized Jacobi: Sharpened Bounds via Residual Concentration and Asynchronous Extension*, arXiv:2606.01232, first submitted May 31, 2026; full text consulted via the openly accessible author's research copy, particularly Sections 3–6 and the collision discussion.

[2] Evan Coleman, *Adaptive Row Selection Meets Asynchrony in Randomized Kaczmarz*, arXiv:2607.08313, first submitted July 9, 2026; openly accessible full text consulted, especially Sections 2, 3, 5 and 6.

[3] Lionel Tondji and Dirk A. Lorenz, *Faster randomized block sparse Kaczmarz by averaging*, *Numerical Algorithms* 93 (2023), 1417–1451; published online December 28, 2022; DOI:10.1007/s11075-022-01473-x. Sections 1, 4 and 5 consulted via the open-access journal version.
