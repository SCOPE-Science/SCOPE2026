# Exact one-step extinction and optimal random mixing for the rule-60/102 diploid automaton

## Finding

Consider a binary periodic ring of size \(n\ge3\) with initially independent, fair bits, and synchronous sitewise independent choices between elementary cellular automata 60 and 102. If the right-neighbor rule is selected with probability \(\lambda\in[0,1]\), then the probability that the **entire ring** becomes zero after **one update** is exactly

\[
P_n(\lambda)=\frac{\alpha_+^n+\alpha_-^n+\lambda^n+(1-\lambda)^n}{2^n},\qquad
\alpha_\pm=\frac{1\pm\sqrt{1+4\lambda(1-\lambda)}}2.
\]

A second expression, with \(t=\lambda(1-\lambda)\), is

\[
P_n(\lambda)=2^{1-n}\sum_{j=0}^{\lfloor n/4\rfloor}
\frac{n}{n-2j}\binom{n-2j}{2j}t^{2j}.
\]

Consequently \(P_3(\lambda)=1/4\) for every mixing parameter. For every integer \(n\ge4\), the probability is **strictly increasing** in \(t\in[0,1/4]\); its only minimizing parameters are \(\lambda=0,1\), each giving \(2^{1-n}\), and its unique maximizing parameter is \(\lambda=1/2\). In particular \(P_4(1/2)=9/64\). For each fixed \(0<\lambda<1\),

\[
P_n(\lambda)\sim \left(\frac{1+\sqrt{1+4\lambda(1-\lambda)}}4\right)^n
\quad(n\to\infty).
\]

Thus the balanced mixture raises the **one-step** extinction probability over either unmixed rule by the exponentially growing factor

\[
\frac{P_n(1/2)}{P_n(0)}\sim
\frac12\left(\frac{1+\sqrt2}{2}\right)^n.
\]

## Assumptions and scope

The sites are indexed by \(\mathbb Z/n\mathbb Z\), with \(n\ge3\) and binary spins \(X_{0,i}\in\mathbb F_2\). Initially \(X_0\) is uniformly distributed on \(\mathbb F_2^n\). Independently of \(X_0\) and of one another, each site chooses a sign \(\sigma_i\in\{-,+\}\) with \(\Pr(\sigma_i=+)=\lambda\) and \(\Pr(\sigma_i=-)=1-\lambda\). The synchronous update is \(X_{1,i}=X_{0,i}\oplus X_{0,i+\sigma_i}\), with indices modulo \(n\), where \(+\) denotes the right-neighbor (rule 102) and \(-\) the left-neighbor (rule 60). The probability \(P_n(\lambda)\) is joint over the initial configuration and one draw of all sitewise rules. It is not a probability conditioned on an arbitrary prescribed initial configuration, nor an eventual hitting-time probability.

## Proof

Fix a rule-choice vector \(\sigma\). The event \(X_1=0\) imposes exactly the equalities \(X_{0,i}=X_{0,i+\sigma_i}\) for each \(i\). Regard these as edges of a functional directed graph: from vertex \(i\), direct one arrow to its selected neighbor. Each weak connected component supports exactly one arbitrary binary initial value. Hence, if \(c(\sigma)\) is the number of weak components, exactly \(2^{c(\sigma)}\) of the \(2^n\) initial configurations yield zero, giving conditional probability \(2^{c(\sigma)-n}\).

Every finite outdegree-one directed graph has one directed cycle per weak component. Here directed cycles can only be adjacent two-cycles or a tour of the entire ring: a directed cycle of length at least three must proceed continually in one cyclic direction, so uses all \(n\) sites. For a nonconstant sign vector \(\sigma\), a full tour is impossible; its directed cycles are therefore the adjacent two-cycles occurring precisely where \(\sigma_i=+\) and \(\sigma_{i+1}=-\). Put \(k(\sigma)=\#\{i:\sigma_i=+,\ \sigma_{i+1}=-\}\), with cyclic indices. Thus \(c(\sigma)=k(\sigma)\) for every nonconstant sign vector. The two constant sign vectors each have \(c=1\) but \(k=0\).

Let the row and column labels of a transfer matrix be \(+, -\), in that order, and set

\[
T_\lambda=\begin{pmatrix}\lambda&2(1-\lambda)\\\lambda&1-\lambda\end{pmatrix}.
\]

In the cyclic product of matrix entries, the column's orientation supplies its Bernoulli probability; the transition \(+\to-\) supplies an additional factor two. It follows that

\[
\operatorname{tr}(T_\lambda^n)
=\sum_{\sigma\in\{+,-\}^n}\Pr(\sigma)2^{k(\sigma)}.
\]

Correcting the two constant orientations gives the exact conditional-average kernel size

\[
2^nP_n(\lambda)=\operatorname{tr}(T_\lambda^n)+\lambda^n+(1-\lambda)^n.
\]

The matrix has trace \(1\), determinant \(-t\), and eigenvalues \(\alpha_\pm\) given in the finding, proving the first formula even at the degenerate parameter endpoints.

For the polynomial form define \(S_n(t)=\alpha_+^n+\alpha_-^n\), with \(S_0=2\), \(S_1=1\). Both eigenvalues solve \(z^2-z-t=0\), so \(S_n(t)=S_{n-1}(t)+tS_{n-2}(t)\). The characteristic roots of the recurrence with \(t\) replaced by \(-t\) are \(\lambda\) and \(1-\lambda\), hence \(\lambda^n+(1-\lambda)^n=S_n(-t)\). For each \(n\ge1\), induction using the recurrence gives

\[
S_n(t)=\sum_{j=0}^{\lfloor n/2\rfloor}
\frac{n}{n-j}\binom{n-j}{j}t^j.
\]

Adding \(S_n(t)+S_n(-t)\) deletes the odd powers. This proves the second formula. Every surviving coefficient is positive; for \(n\le3\) there is only the constant term, whereas for \(n\ge4\) the \(j=1\) term is present and strictly positive. As \(\lambda(1-\lambda)\) has unique maximum \(1/4\) at \(\lambda=1/2\) and vanishes exactly at the two endpoints, the optimization assertions follow.

Finally, for fixed \(0<\lambda<1\) we have \(\alpha_+>1\), while \(|\alpha_-|<1\) and \(\max\{\lambda,1-\lambda\}<1\). The \(\alpha_+^n\) term therefore dominates. Substitution of \(\lambda=1/2\) and comparison with the exact deterministic-endpoint value yields the displayed exponential ratio.

## Verification

Run the standalone Python 3 program `verify_extinction.py` using only the standard library. It checks the formula by direct enumeration of all initial bit strings and all sitewise rule-choice vectors for \(3\le n\le9\) at seven rational mixing parameters; it also evaluates zero-preimage counts by a separate rank computation over \(\mathbb F_2\). For \(10\le n\le49\), it compares the polynomial formula to a separate Lucas-type recurrence on five rational parameter values. It additionally checks strict monotonicity for \(4\le n\le49\) on a rational parameter grid. In all, 295 size/parameter comparisons passed. These finite computations corroborate, but are not substitutes for, the proof for all integer ring sizes.

## Relationship to prior work

Cirillo, Vliem, Schuricht and Spitoni [1] define precisely this sitewise diploid mixture of rules 60 and 102 and show that for the balanced mixture and finite rings the zero state is ultimately absorbing almost surely. Their primary text (Sections II–V, especially Theorems 1–2) studies long-time stationary behavior, block approximation and a positive-probability multi-step route from arbitrary initial configurations. It does not give the exact probability of a one-step all-zero update from a fair random initial ring, nor the strict finite-size mixing optimum or the exponential gain. Those are the claims established here. Earlier work of Cirillo, Nardi and Spitoni [2] analyzes mixtures involving the null elementary rule; this is not an exact formula for the 60/102 mixture. The general technique of a two-state transfer matrix is classical and is not claimed as new. The novelty assertion is limited to this model-specific exact extinction law and its parameter optimization.

## Limitations

The random initial state must be the uniform product measure; no statement is made for other initial laws or individually prescribed configurations. The update must choose rules **independently at each site**; choosing one global rule for the whole ring each time would be a different model. The conclusion concerns precisely one synchronous update and does not establish a global phase boundary, relaxation rate, or an expectation of eventual extinction time. The strict optimization requires \(n\ge4\), whereas \(n=3\) is exactly flat. Rings of size \(n\le2\) are excluded because their left and right neighbor geometry degenerates. Historical priority cannot be proved by a finite literature search, despite comparison with the most directly relevant full text.

## References

[1] E. N. M. Cirillo, J. L. Vliem, D. Schuricht, C. Spitoni, *Inefficiency of the block approximation in diploid Probabilistic Cellular Automata*, arXiv:2602.13839 (first public 2026-02-14), https://arxiv.org/abs/2602.13839. Also *Physical Review E* 114, 014154 (2026), DOI:10.1103/qksd-scrd.

[2] E. N. M. Cirillo, F. R. Nardi, C. Spitoni, *Phase transitions in random mixtures of elementary cellular automata*, arXiv:2102.07626 (2021), https://arxiv.org/abs/2102.07626.

[3] E. N. M. Cirillo, G. Lancia, C. Spitoni, *Block approximations for probabilistic mixtures of elementary cellular automata*, arXiv:2408.09201 (2024), https://arxiv.org/abs/2408.09201.
