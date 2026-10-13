# Exact Markov error floor for the always-move direct structured search

## Finding
Consider Algorithm 5, the direct structured derivative-free update search, from Xie (2026). In the scalar matrix case, take
\[
f(w)=\\frac12 w^2,\qquad w_0=0,
\]
fix a probing radius \\(h>0\\) and update radius \\(\\eta>0\\), and at every iteration draw \\(q\\) independent Rademacher candidates \\(H_i=\\xi_i\\in\\{-1,+1\\}\\). When the directional scores tie, choose the first sampled minimizer. Put \\(p=2^{-q}\\).

Then \\(N_t=w_t/\\eta\\) is exactly a nearest-neighbor Markov chain on \\(\\mathbb Z\\). From \\(n>0\\), it moves to \\(n-1\\) with probability \\(1-p\\) and to \\(n+1\\) with probability \\(p\\); the rule is reflected for \\(n<0\\); and from \\(0\\) it moves to \\(\\pm1\\) with probability \\(1/2\\) each. The transition law is independent of \\(h\\).

Therefore the fixed-step iterates never converge for any \\(\\eta>0\\). If \\(q=1\\), then \\(N_t\\) is simple symmetric random walk and
\[
\\mathbb E f(w_t)=\\frac{\\eta^2 t}{2},
\qquad
\\limsup_{t\\to\\infty} f(w_t)=\\infty\quad\\text{almost surely}.
\]
If \\(q\\ge2\\), the chain is irreducible and positive recurrent. Its invariant law is
\[
\\pi_0=\\frac{1-2p}{2(1-p)},
\qquad
\\pi_{\\pm n}=\\frac{1-2p}{4(1-p)^2}
\\left(\\frac{p}{1-p}\\right)^{n-1},\qquad n\\ge1.
\]
Although the chain has period two, its ergodic time average exists, and
\[
\\frac1T\\sum_{t=0}^{T-1} f(w_t)
\\longrightarrow
\\frac{\\eta^2}{4(1-2^{1-q})^2}
\quad\\text{almost surely}.
\]
In particular, increasing \\(q\\) does not remove the fixed-step floor: the right-hand side tends to \\(\\eta^2/4\\) as \\(q\\to\\infty\\).

## Assumptions and scope
The result concerns the source's Algorithm 5 exactly as an always-move, fixed-update-radius method. The source leaves the candidate-vector sampling distribution open, so the theorem fixes the natural scalar symmetric specialization \\(u_i=1\\), \\(v_i=\\xi_i\\), with independent Rademacher \\(\\xi_i\\). This is a valid rank-one specialization of the printed algorithm. The first-minimizer tie rule is stated because every candidate score ties at \\(w=0\\). Exact function values are assumed, and no claim is made for the source's separate symmetric two-point modification, for adaptive \\(\\eta\\), or for an added acceptance test.

The objective is strongly convex and smooth, and the phenomenon is not caused by nonconvexity, finite-difference bias in the ranking, or function noise. The probing radius \\(h\\) may be arbitrary and positive.

## Proof
For a candidate \\(\\xi_i\\in\\{-1,+1\\}\\), the source score becomes
\[
s_i=\\frac{f(w+h\\xi_i)-f(w)}{h}
=w\\xi_i+\\frac h2.
\]
The common term \\(h/2\\) does not affect the ranking. If \\(w>0\\), every candidate \\(-1\\) has smaller score than every candidate \\(+1\\), so the selected step is inward unless all \\(q\\) samples are \\(+1\\). That exceptional event has probability \\(p=2^{-q}\\). The argument is symmetric when \\(w<0\\). At \\(w=0\\), all scores are equal, and choosing the first sampled minimizer yields an unbiased Rademacher step. Since \\(w_0=0\\) and every update has magnitude \\(\\eta\\), all iterates lie on \\(\\eta\\mathbb Z\\), proving the stated transition law for \\(N_t=w_t/\\eta\\).

Every increment satisfies \\(|w_{t+1}-w_t|=\\eta\\). A convergent sequence must have successive increments tending to zero, so no sample path can converge when \\(\\eta>0\\).

For \\(q=1\\), selection is vacuous and the successive directions are independent Rademacher variables. Hence \\(w_t=\\eta\\sum_{j=0}^{t-1}\\xi_j\\), so \\(\\mathbb E[w_t^2]=\\eta^2t\\) and the displayed expectation follows. Standard recurrence and unboundedness of one-dimensional simple symmetric random walk give the almost-sure limsup statement.

Now suppose \\(q\\ge2\\), so \\(p<1/2\\). Let \\(r=p/(1-p)\\). Detailed balance between zero and one requires
\[
\\frac{\\pi_0}{2}=\\pi_1(1-p),
\]
and detailed balance on each positive edge requires \\(\\pi_n p=\\pi_{n+1}(1-p)\\). Reflection gives equal masses at \\(n\\) and \\(-n\\). Thus
\[
\\pi_n=\\pi_1r^{n-1},\qquad n\\ge1.
\]
Normalizing \\(\\pi_0+2\\sum_{n\\ge1}\\pi_n=1\\) gives exactly the displayed invariant law. It is summable because \\(r<1\\); for an irreducible countable-state chain, the existence of this invariant probability implies positive recurrence.

Its second moment is obtained from
\[
\\sum_{n\\ge1}n^2r^{n-1}=\\frac{1+r}{(1-r)^3}.
\]
Substitution yields
\[
\\sum_{n\\in\\mathbb Z}n^2\\pi_n
=\\frac1{2(1-2p)^2}.
\]
The Markov-chain ergodic theorem applies to the integrable function \\(n\\mapsto n^2\\) even though the chain is periodic. Since \\(f(w_t)=\\eta^2N_t^2/2\\), its almost-sure Cesaro average is therefore
\[
\\frac{\\eta^2}{4(1-2p)^2}
=\\frac{\\eta^2}{4(1-2^{1-q})^2}.
\]
Taking \\(q\\to\\infty\\) gives \\(\\eta^2/4\\).

## Verification
The included `verify_markov.py` checks the score ordering, detailed-balance identities, normalization, and second-moment formula exactly with rational arithmetic for multiple \\(q\\ge2\\), and independently enumerates the \\(q=1\\) random walk for small horizons to confirm \\(\\mathbb E[N_t^2]=t\\). The infinite-horizon recurrence, positive recurrence, nonconvergence, and ergodic limit are proved analytically above; finite replay is not used as a substitute for those arguments.

## Relationship to prior work
Xie's source explicitly warns that Algorithm 5's always-move rule need not decrease the objective and suggests an acceptance test or line search. It also reports weak empirical performance for the fixed-step always-move variant. The present result sharpens that qualitative warning into an exact stochastic law on the simplest strongly convex problem: the candidate count changes a birth--death drift but cannot remove the nonzero constant-step time-average floor.

Roberts and Royer's randomized direct-search framework, continuing the probabilistic-descent line of Gratton, Royer, Vicente, and Zhang, uses a sufficient-decrease acceptance condition and shrinks the step after unsuccessful polling. Its full-text Algorithm 1 therefore has a different state evolution: rejected trial points leave the iterate unchanged and reduce the step size. Those convergence results do not imply the invariant law here, whose mechanism is precisely that the source algorithm always moves by the fixed radius \\(\\eta\\).


## Limitations
The theorem is intentionally source-specific. It does not claim that all sampling laws for Algorithm 5 have the same invariant distribution, nor that the source's symmetric two-point variant has this behavior. The tie-breaking rule matters only at the exact minimizer and is fixed explicitly. The invariant distribution for \\(q\\ge2\\) is not a pointwise limit from \\(w_0=0\\) because the chain has period two; the proved asymptotic statement is the almost-sure Cesaro objective average. Adding an acceptance test, adapting \\(\\eta\\), or permitting zero moves changes the mechanism and falls outside the claim.

## References
1. P. Xie, “Derivative-Free Structured Updates for Muon,” arXiv:2609.17759v1, 2026. Algorithm 5 and Sections 2.4, 3.4, 3.8, 4.
2. L. Roberts and C. W. Royer, “Direct Search Based on Probabilistic Descent in Reduced Spaces,” arXiv:2204.01275v2; SIAM Journal on Optimization 33 (2023), 3057–3082. DOI:10.1137/22M1488569.
3. S. Gratton, C. W. Royer, L. N. Vicente, and Z. Zhang, “Direct Search Based on Probabilistic Descent,” SIAM Journal on Optimization 25 (2015), 1515–1541. DOI:10.1137/140961602.
