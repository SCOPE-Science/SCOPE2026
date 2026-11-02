# Sharp binary envelopes for multistate nonlinear voter dynamics

## Finding

**Theorem (pathwise binary comparison and exact fixation defect).** In the nonlinear imitation model defined below, distinguish a focal opinion \(A\), and write \(a_0\) for its initial population. Let \(X(t)\) be its random count in an arbitrary multistate system, and let \(Y(t)\) be its count in a binary system in which every initially non-\(A\) opinion is combined into a single alternative. The systems may be coupled with the same initial focal vertices so that, simultaneously for every \(t\ge0\),

\[
q>1:\quad X(t)\ge Y(t),\qquad
0<q<1:\quad X(t)\le Y(t),\qquad
q=1:\quad X(t)=Y(t).
\]

In fact, the nesting holds **vertex by vertex**, not merely for the counts. Define

\[
H_{N,q}(a)=
\frac{\displaystyle\sum_{r=0}^{a-1}\binom{N-1}{r}^{q-1}}
{\displaystyle\sum_{r=0}^{N-1}\binom{N-1}{r}^{q-1}},\qquad
0\le a\le N,
\]

where the empty numerator equals zero. If \(p_A\) is the probability that \(A\) eventually becomes the sole surviving opinion, then

\[
q>1:\quad p_A\ge H_{N,q}(a_0),\qquad
0<q<1:\quad p_A\le H_{N,q}(a_0),\qquad
q=1:\quad p_A=a_0/N.
\]

For \(q\ne1\), \(1\le a_0<N\), these inequalities are strict **if and only if** at least two distinct non-\(A\) opinions are initially represented. With a single opposing opinion, equality holds; hence each binary envelope is sharp at every population size and initial focal count. The comparison also holds for the full finite-time distribution of the focal count: for each integer threshold \(k\) and time \(t\ge0\), the respective inequality applies to \(\Pr\{X(t)\ge k\}\) versus \(\Pr\{Y(t)\ge k\}\).

There is an exact positive/negative correction identity, not just an inequality. If \(\mathbf n(t)\) is the vector of opinion counts, \(a(t)=n_A(t)\), and \(T\) is the first full consensus time, then

\[
\begin{aligned}
p_A-H_{N,q}(a_0)
&=\mathbb E\int_0^T
\frac{a(t)}{(N-1)^q}
\left[(N-a(t))^q-\sum_{\beta\ne A}n_\beta(t)^q\right]
\left[H_{N,q}(a(t))-H_{N,q}(a(t)-1)\right]dt,
\end{aligned}
\]

where the integrand is defined as zero when \(a(t)=0\). Its sign is that of \(q-1\), and its sign is strictly nonzero in each mixed initial state with at least two opposing opinions.

## Assumptions and scope

Fix integers \(N\ge2\), \(M\ge2\), and a real exponent \(q>0\). On the complete graph without self-loops, every vertex carries one of \(M\) opinions. For every ordered pair \(\beta\ne\alpha\), a vertex with opinion \(\beta\) changes to opinion \(\alpha\) independently at instantaneous rate \((n_\alpha/(N-1))^q\), where \(n_\alpha\) is the current number of vertices with opinion \(\alpha\). Thus the count-vector transition rate is

\[
\mathbf n\longrightarrow \mathbf n-\mathbf e_\beta+\mathbf e_\alpha
\quad\text{at rate}\quad
n_\beta\left(\frac{n_\alpha}{N-1}\right)^q.
\]

Only positive initial opinion counts can remain positive or shrink: absent opinions cannot reappear. The binary comparator uses precisely the same rate rule and initial focal vertex set, with all other vertices labelled as one opposing opinion. The number of possible labels can exceed the number of initially present labels; such unused labels are immaterial.

## Proof

**1. Almost-sure consensus.** The process is a finite-state continuous-time Markov chain. From any nonconsensus state and any surviving opinion, there exists a finite sequence of strictly positive-rate transitions that converts every other individual to that opinion. Therefore every nonabsorbing communicating class has a route to an absorbing consensus class. No nonconsensus class can be closed, and the first consensus time \(T\) is almost surely finite with finite expectation.

**2. Sitewise order for any real exponent.** Let \(S\) and \(B\) denote the sets of vertices labelled \(A\) in the multistate and binary models, respectively. At a non-\(A\) vertex the rate of entering \(A\) is \((|S|/(N-1))^q\) or \((|B|/(N-1))^q\). At an \(A\) vertex the multistate exit rate is

\[
d_S=(N-1)^{-q}\sum_{\beta\ne A}n_\beta^q,
\]

whereas the binary exit rate is \(d_B=(N-1)^{-q}(N-|B|)^q\).

For \(q>1\) and \(B\subseteq S\), the entrance rate at a vertex outside both sets is at least as large in the multistate model, while at a vertex in both sets,

\[
d_S\le (N-1)^{-q}(N-|S|)^q\le d_B.
\]

For \(0<q<1\) and \(S\subseteq B\), the entrance inequality is reversed and

\[
d_S\ge (N-1)^{-q}(N-|S|)^q\ge d_B.
\]

These are the elementary superadditivity and subadditivity inequalities for nonnegative summands raised to powers \(q>1\) and \(0<q<1\), respectively. Couple changes at equal binary statuses using a common part at the smaller of the two rates and an extra change in the model with the larger rate; changes at vertices with unequal statuses cannot break the prescribed order. Nonfocal-to-nonfocal updates in the multistate model do not change \(S\) and can be included with their original rates. Since the finite-state rates are uniformly bounded, this basic continuous-time coupling is nonexplosive and preserves its order after every jump. At \(q=1\), both relevant entrance and exit rates depend only on \(|S|\), so identical focal indicator sets can be maintained throughout. This proves the stronger sitewise claim, and hence all finite-time stochastic comparisons.

**3. Exact binary fixation probability.** When there are only two opinions, the focal count is a birth-death chain on \(\{0,\ldots,N\}\), with rates

\[
\lambda_a=(N-a)\left(\frac a{N-1}\right)^q,
\qquad
\mu_a=a\left(\frac{N-a}{N-1}\right)^q.
\]

For \(1\le a<N\), the ratio is \(\mu_a/\lambda_a=(a/(N-a))^{1-q}\). Consequently

\[
\prod_{j=1}^r\frac{\mu_j}{\lambda_j}
=\binom{N-1}{r}^{q-1}.
\]

Solving the harmonic recurrence \(\lambda_a(H(a+1)-H(a))+\mu_a(H(a-1)-H(a))=0\) with \(H(0)=0\) and \(H(N)=1\) gives the displayed \(H_{N,q}\). Because monochromatic consensus is absorbing and the coupling gives a pathwise focal-set inclusion, it immediately yields the fixation bounds.

**4. Exact defect and strictness.** Apply the full multistate generator to \(f(\mathbf n)=H_{N,q}(n_A)\). The gain term agrees with the binary chain at the same focal count; only the loss term differs. The binary harmonic recurrence yields exactly

\[
(\mathcal L f)(\mathbf n)=
\frac{n_A}{(N-1)^q}
\left[(N-n_A)^q-\sum_{\beta\ne A}n_\beta^q\right]
[H_{N,q}(n_A)-H_{N,q}(n_A-1)].
\]

Since \(H_{N,q}\) is strictly increasing at every interior count, this expression has the sign of \(q-1\). For \(q\ne1\), equality in the power-sum inequality holds precisely when at most one competing opinion has positive count. Dynkin's formula stopped at the almost surely finite consensus time, followed by bounded convergence, gives the exact integral identity; the integrand is bounded on the finite state space and \(\mathbb E T<\infty\). If two competing opinions are initially present, the integrand is strictly signed until the first jump; the initial exponential holding time has strictly positive expectation. Thus the correction is strict. Conversely, if only one competing opinion initially survives, there are exactly two opinions forever, so the correction vanishes identically. For \(q=1\), \(H_{N,1}(a)=a/N\) and the correction is zero.

## Verification

The standalone program `verify.py` constructs the exact finite-state transition generator for each specified population and opinion count, solves the absorbing fixation equations, and compares finite-time tail probabilities against the binary chain by matrix exponentiation. Executing it with Python and NumPy, SciPy, and SymPy passes 2,540 numerical fixation-state comparisons across \(q\in\{1/2,1,2,3\}\), 882 strictly nonbinary comparisons, 19,392 finite-time upper-tail comparisons, and 157 additional exact-rational absorption comparisons for \(q=2\). This checks finite instances; the preceding coupling and harmonic arguments, not computation, prove the all-size statements.

For four initially different opinions, each represented by one vertex, permutation symmetry gives \(p_A=1/4\). The binary bound is \(H_{4,2}(1)=1/8\) for \(q=2\), and \(H_{4,1/2}(1)=1/(2+2/\sqrt3)\approx0.316987\) for \(q=1/2\). Both strict directions appear already at the smallest four-opinion example.

## Relationship to prior work

Ramirez, Vazquez, San Miguel, and Galla [1] define this nonlinear multistate imitation chain and explicitly explain that its focal count is not a closed binary Markov process when \(q\ne1\): its loss rate depends on the entire competitor count vector (their Sec. IV.1, Eqs. (27)--(28)). The present result **does not** claim binary lumpability; it establishes a pathwise binary envelope and a sharp exact fixation correction despite the failure of lumpability. Their Secs. III and IV discuss binary and multistate ordering, deterministic drift and metastable consensus behavior, but do not state the sitewise stochastic ordering, finite-time distributional envelope, strict fixation characterization, or stopped-generator defect identity.

The classical multistate voter work [2] concerns the linear \(q=1\) case, where lumpability and fixation proportional to initial frequency are known. Nonlinear binary \(q\)-voter models [3] and noisy multistate voter models [4] have distinct dynamics or state spaces. Standard birth-death harmonic functions and monotone couplings are used here as proof methods, not claimed as discoveries. A specialized equivalent comparison in uninspected literature cannot be ruled out.

## Limitations

The comparison requires the homogeneous complete graph, the common power exponent \(q>0\), and the precisely specified independent continuous-time adoption rates. It does not assert a full exact multicolor exit distribution, a stochastic ordering of the total consensus time, or an analogous graph-independent bound for heterogeneous or spatial networks. While the mathematical argument is self-contained and finite checks support it, independent external validation and an exhaustive publication-priority search have not been performed.

## References

[1] L. S. Ramirez, F. Vazquez, M. San Miguel, and T. Galla, *Ordering dynamics of nonlinear voter models*, arXiv:2310.20548 (first posted 2023-10-31); *Physical Review E* **109**, 034307 (2024), DOI: 10.1103/PhysRevE.109.034307. https://arxiv.org/abs/2310.20548

[2] M. Starnini, A. Baronchelli, and R. Pastor-Satorras, *Ordering dynamics of the multi-state voter model*, arXiv:1207.5810 (2012). https://arxiv.org/abs/1207.5810

[3] C. Castellano, M. A. Muñoz, and R. Pastor-Satorras, *Nonlinear q-voter model*, *Physical Review E* **80**, 041129 (2009), DOI: 10.1103/PhysRevE.80.041129.

[4] F. Herrerías-Azcué and T. Galla, *Consensus and diversity in multistate noisy voter models*, *Physical Review E* **100**, 022304 (2019), DOI: 10.1103/PhysRevE.100.022304.
