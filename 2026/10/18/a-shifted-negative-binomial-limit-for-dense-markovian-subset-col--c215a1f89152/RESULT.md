# A shifted negative-binomial limit for dense Markovian subset collection

## Finding
Let \(n\ge6\). Uniformly choose an \((n-2)\)-subset \(H_1\) of \([n]\), and obtain \(H_{t+1}\) by independently choosing one included label and one excluded label uniformly and exchanging them. Collect a two-element set whenever it lies entirely in a visited \(H_t\). Let \(T_n\) be the first time \(t\ge1\) when all two-element sets have been collected. Then
\[
\mathbb E[z^{T_\infty}]=\frac{z^5}{(2-z)^2},\quad
\Pr(T_\infty=t)=\frac{t-4}{2^{t-3}}\ (t=5,6,\ldots),
\]
\[
d_{\mathrm{TV}}\bigl(\mathcal L(T_n),\mathcal L(T_\infty)\bigr)
\le\min\!\left\{1,\frac{17}{n-2}\right\},\quad
\mathbb E[T_n]\longrightarrow7.
\]
In particular, \(T_\infty\) is five plus the number of failures preceding two successes in independent fair trials; its variance is \(4\). For every finite \(n\ge6\),
\[
\Pr(T_n=5)=\frac{(n-4)(n-3)(2n-5)}{8(n-2)^3}.
\]

## Assumptions and scope
The chain samples its initial subset uniformly, and all choices of removed and inserted labels are conditionally independent and uniform given the current subset. One round is one visited subset, so time begins at \(t=1\). The claim concerns \(r=n-2\) and collected subset size \(s=2\) only. Throughout, the vertex-cover number of an edge set \(G\) is the smallest cardinality of a vertex set meeting every edge of \(G\).

## Proof
**Graph reduction.** Write \(E_t=[n]\setminus H_t\), a two-element set or graph edge. Consecutive omitted edges share one endpoint; their other endpoint is replaced uniformly from the \(n-2\) labels outside the current omitted edge. A pair \(S\) has never been collected through time \(t\) exactly when \(S\) meets every omitted edge \(E_1,\ldots,E_t\). Thus \(T_n\) is the first time the graph of omitted edges has minimum vertex-cover number at least \(3\). Repeated edges cause no difficulty.

**No-collision comparison.** Run an idealized exploration that always assigns a fresh label to the newly inserted omitted-edge endpoint. Retain either currently omitted endpoint with probability \(1/2\) at every exchange. The visited edges form a growing tree with a distinguished pendant edge. Coupling the endpoint-retention coins with those of the finite chain makes the two cover times equal up to the first reuse of a previously observed label.

**Tree computation.** Delete the distinguished pendant edge temporarily and denote its old endpoint by \(u\). Let \(A\) and \(B\) be the minimum vertex-cover sizes of the completed edges subject respectively to omitting and including \(u\). Initially \((A,B)=(0,1)\); the cover size including the pending edge is \(\min\{B,A+1\}\). Retaining \(u\) makes the deleted pendant edge permanent and gives \((A,B)\mapsto(A+1,B)\). Retaining the former pendant endpoint and making it the next old endpoint gives \((A,B)\mapsto(B,1+\min\{A,B\})\). Both moves are fair and independent. Absorption happens when \(\min\{B,A+1\}\ge3\). Only the states \((0,1),(1,1),(a,1)\) for \(a\ge2\), \((1,2)\), and \((a,2)\) for \(a\ge2\) occur before absorption. The first step moves deterministically to \((1,1)\). From \((1,1)\), one step moves to \((a,1)\) with \(a\ge2\), or to \((1,2)\), each with probability \(1/2\). A state \((a,1)\) loops with probability \(1/2\), otherwise moves to \((1,2)\). State \((1,2)\) moves deterministically to \((a,2)\) for \(a\ge2\). A state \((a,2)\) loops with probability \(1/2\), otherwise absorbs. Hence the ideal cover time equals \(5\) plus the sum of two independent geometric-failure counts with success probability \(1/2\). This gives the displayed generating function, mass function, expectation and variance.

**Quantitative coupling.** If \(j\) omitted edges have already been exposed without any repeated label, exactly \(j+1\) labels have been seen, of which at most \(j-1\) lie outside the currently omitted pair. The probability of a label collision at the next exchange is at most \((j-1)/(n-2)\). Summing these conditional hazards until the independent ideal stopping time and using the union bound gives
\[
\Pr(T_n\ne T_\infty)
\le \frac{\mathbb E[(T_\infty-1)(T_\infty-2)]}{2(n-2)}
=\frac{17}{n-2},
\]
since \(\mathbb E[T_\infty]=7\) and \(\operatorname{Var}(T_\infty)=4\). The coupling inequality bounds total variation.

**Expectations.** Conditional on any history, the next four exchanges form, with probability at least
\[
q_n=\frac{(n-3)(n-4)(n-5)}{8(n-2)^3}\ge\frac{3}{256},
\]
a run of four new omitted-edge endpoints in which each of the last three steps retains the most recently introduced endpoint. Together with the current edge these form a simple path of five edges; its minimum vertex-cover size is three. This forces collection irrespective of earlier edges. Thus \(\Pr(T_n>1+4k)\le(1-3/256)^k\) for all integers \(k\ge0\). These common exponentially decaying tails imply uniform integrability; convergence in total variation consequently yields \(\mathbb E[T_n]\to7\).

**Earliest completion.** A graph of fewer than five edges has vertex-cover number at most two, so \(T_n\ge5\). Enumerate the four transitions following the initial omitted edge, distinguishing a genuinely new endpoint from reuse of a previously visited endpoint other than the current pair. The histories achieving cover number three have either four new endpoints, with four favorable retention words, or three new endpoints, with ten favorable canonical retention/reuse histories. Their respective path counts are
\[
4(n-2)(n-3)(n-4)(n-5)
\quad\text{and}\quad10(n-2)(n-3)(n-4).
\]
The first factor counts the fresh-label choices, and the second counts those histories with one reused label. Every four-exchange history has probability \([2(n-2)]^{-4}\), giving
\[
\Pr(T_n=5)=\frac{4(n-2)(n-3)(n-4)(n-5)+10(n-2)(n-3)(n-4)}{[2(n-2)]^4}
=\frac{(n-4)(n-3)(2n-5)}{8(n-2)^3}.
\]
A restricted-growth canonical enumeration verifying the coefficients \(4\) and \(10\) is included in the standalone checker.

## Verification
Run \(`python3 checker.py`\) using only the Python standard library. The checker compares the tree-state recurrence with direct vertex-cover enumeration for every retention sequence through eleven transitions, checks exact probabilities against the shifted negative-binomial law, and reproduces the earliest-completion enumeration as a falling-factorial polynomial, with independent exact finite-sample checks. Finite computations supplement but do not substitute for the all-parameter analytical steps.

## Relationship to prior work
Athreya, S. Mukherjee and S. S. Mukherjee introduce the Markovian generalized coupon collector in which visited \(r\)-sets collect their \(s\)-subsets. Their principal asymptotic questions concern fixed \(r,s\) as the ground-set size grows. Here \(r=n-2\) diverges with \(n\); the omitted-edge and vertex-cover interpretation makes the dense regime behave differently. Classical subset coupon-collection results such as Adler and Ross concern independent rounds, not these adjacent-subset transitions. This analysis determines a dense-regime law with a finite-size total-variation bound and an exact five-step probability; it does not settle or contradict the fixed-parameter conjectures.

## Limitations
The result is restricted to missing exactly two labels and collecting two-element subsets. It supplies no quantitative bound on \(|\mathbb E[T_n]-7|\), although convergence is established. The earliest-completion expression concerns time five only. Literature comparisons do not exclude unindexed equivalent results.

## References
1. S. Athreya, S. Mukherjee, S. S. Mukherjee, *On a generalisation of the coupon collector problem*, arXiv:2304.01145, first posted 2023-04-03, https://arxiv.org/abs/2304.01145 ; later journal version https://doi.org/10.1007/s10959-025-01417-w .
2. I. Adler and S. M. Ross, *The coupon subset collection problem*, Journal of Applied Probability 38 (2001), 737–746.
