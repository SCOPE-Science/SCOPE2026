# Bernoulli convolution and logarithmic collapse in order-decreasing chain contractions

## Finding
For every integer \(n\geq1\), let \(S_n\) be the monoid of order-preserving, order-decreasing, nonexpansive full maps \(f:[n]\to[n]\), with composition as multiplication. Encode \(f\) by the \(n-1\) increments \(\epsilon_i(f)=f(i+1)-f(i)\in\{0,1\}\). For \(0\leq p\leq1\), let \(\mu_p\) be the probability measure on \(S_n\) under which these increments are independent Bernoulli variables with success probability \(p\).

**Bernoulli convolution theorem.** For any \(p,q\in[0,1]\), independent \(F\sim\mu_p\) and \(G\sim\mu_q\) satisfy
\[
F\circ G\sim\mu_{pq}.
\]
Thus \(\mu_{p_1}*\cdots*\mu_{p_k}=\mu_{\prod_{j=1}^k p_j}\) for arbitrary \(k\geq1\), including endpoint probabilities. For \(n\geq2\), the measures form a multiplicative one-parameter submonoid of probability measures on a generally noncommutative transformation monoid.

In particular, for \(k\geq1\) independently and uniformly selected elements of \(S_n\), let \(H_k\) be their composition. Every specified \(h\in S_n\) of image rank \(r\) has exactly
\[
(2^k-1)^{n-r}
\]
ordered \(k\)-factor representations. Consequently,
\[
\Pr\{\operatorname{rank}(H_k)=r\}
 =\binom{n-1}{r-1}2^{-k(r-1)}(1-2^{-k})^{n-r},
\quad1\leq r\leq n.
\]
Equivalently, \(\operatorname{rank}(H_k)-1\sim\operatorname{Bin}(n-1,2^{-k})\). For \(n=1\), the monoid has only the identity, which is also the constant map.

The unique absorbing element for \(n\geq2\) is \(z(i)=1\). Starting at the identity and multiplying by new independent uniform elements, the time \(T_n\) to first hit \(z\) has the exact distribution
\[
\Pr\{T_n\leq k\}=(1-2^{-k})^{n-1},\qquad k\geq0,
\]
with \(\Pr\{T_n\leq0\}=0\) for \(n\geq2\). The total-variation distance to the absorbing law after \(k\) steps is exactly
\[
d_n(k)=1-(1-2^{-k})^{n-1}.
\]
There is a total-variation cutoff at \(\log_2(n-1)\) with a bounded-width (lattice) window: for integer sequences \(k_n\geq0\), distance tends to \(1\) if \(k_n-\log_2(n-1)\to-\infty\), and tends to \(0\) if that difference tends to \(+\infty\). More precisely, when \((n-1)2^{-k_n}\to\lambda\in(0,\infty)\), the distance tends to \(1-e^{-\lambda}\), and the excess rank converges in law to \(\operatorname{Pois}(\lambda)\).

## Assumptions and scope
The chain \([n]\) carries its usual integer order and metric; a nonexpansive map satisfies \(|f(i)-f(j)|\leq|i-j|\). Full means defined everywhere. For measures, all factor maps and all increment variables stipulated independent really are independent. Composition \(F\circ G\) applies \(G\) first. The count is for labeled ordered tuples of factors. The rank is cardinality of the image, not semigroup generating rank. The cutoff concerns new independent uniform factors, **not** repeated powers of a single randomly selected map. At \(p=0\) and \(p=1\), probabilities are interpreted directly as degenerate Bernoulli laws, without an ambiguous \(0^0\) convention.

## Proof
**Normal form.** Since every order-decreasing map satisfies \(f(1)=1\), order preservation and contraction give \(0\leq f(i+1)-f(i)\leq1\). Conversely any prescribed binary word \((\epsilon_1,\ldots,\epsilon_{n-1})\) gives the unique map
\[
f(i)=1+\sum_{j=1}^{i-1}\epsilon_j,
\]
which is nondecreasing, nonexpansive, and satisfies \(1\leq f(i)\leq i\). This establishes the binary-word bijection and \(|S_n|=2^{n-1}\). It also establishes \(\operatorname{rank}(f)=f(n)=1+\sum\epsilon_i\) and that \(\mu_{1/2}\) is uniform.

**The full increment law under multiplication.** Write \(U_j=F(j+1)-F(j)\) and \(V_i=G(i+1)-G(i)\). If \(C=F\circ G\) and \(W_i=C(i+1)-C(i)\), then
\[
W_i=\begin{cases}0,&V_i=0,\\U_{G(i)},&V_i=1.\end{cases}
\]
For fixed \(G\), the indices \(G(i)\) for which \(V_i=1\) are exactly the distinct integers \(1,\ldots,G(n)-1\) in increasing order. Since the \(U_j\) are independent Bernoulli-\(p\), the selected variables remain independent even conditioned on the entire map \(G\). For independent formal variables \(t_i\),
\[
\mathbb E\!\left[\prod_{i=1}^{n-1}t_i^{W_i}\mid G\right]
 =\prod_{i=1}^{n-1}(1-pV_i+pV_it_i).
\]
Taking expectation over independent Bernoulli-\(q\) variables \(V_i\) gives
\[
\mathbb E\prod_{i=1}^{n-1}t_i^{W_i}
 =\prod_{i=1}^{n-1}(1-pq+pq t_i).
\]
This is the joint probability-generating polynomial of independent Bernoulli-\(pq\) increments and proves the measure convolution identity. Associativity gives the arbitrary-factor version.

**Fibers and ranks.** For a specified output \(h\) of rank \(r\), there are \(r-1\) one-increments and \(n-r\) zero-increments, so under \(\mu_{2^{-k}}\) its probability equals \(2^{-k(r-1)}(1-2^{-k})^{n-r}\). There are \(2^{k(n-1)}\) ordered \(k\)-tuples, all equally likely. Multiplying and simplifying yields the stated integer fiber count \((2^k-1)^{n-r}\). Exactly \(\binom{n-1}{r-1}\) binary words have rank \(r\), proving the rank distribution.

**Absorption and cutoff.** Every element fixes \(1\), so the constant map \(z\) satisfies \(fz=zf=z\). In the binary normal form, \(H_k=z\) means all \(n-1\) independent increments vanish, giving \((1-2^{-k})^{n-1}\). Since \(z\) is absorbing, the first-hitting-time distribution follows. Total variation from \(\delta_z\) is the mass outside \(z\). If \(m=n-1\), then \((1-2^{-k})^m\to e^{-\lambda}\) when \(m2^{-k}\to\lambda\) and \(k\to\infty\); the usual binomial-to-Poisson limit proves the stated critical-window law. The two cutoff tails follow directly from the bounds \(1-(1-x)^m\leq mx\) and \((1-x)^m\leq e^{-mx}\). Integer time causes unavoidable lattice-phase fluctuations, so no unrestricted continuous centered limit profile is asserted.

## Verification
The accompanying standalone script `verify_random_contractions.py` constructs all elements directly from their value vectors, implements map composition independently of the proof's increment-selection formula, and checks exact rational-measure convolution for \(n\leq6\) and several biased and degenerate parameters. It also exhaustively checks uniformly chosen ordered products for \(n\leq6\) and up to four factors (the four-factor check uses \(n\leq5\)), and checks the closed rank probabilities by exact arithmetic at larger sizes. Execute with `python verify_random_contractions.py`. Passing output: `VERIFY_OK_BERNOULLI_CONVOLUTION_CONTRACTIONS`. Finite checks are corroboration, not proof of universal statements.

## Relationship to prior work
Adeshola and Umar (arXiv:1303.7428, submitted 29 March 2013), §4, give one-element rank/fixed-point distributions for the same order-preserving, order-decreasing full contraction monoid; their Corollaries 4.4 and 4.7 supply \(\binom{n-1}{r-1}\) and \(2^{n-1}\). They do not state multiplication-convolution closure, individual product-fiber counts at every length, or cutoff. Zubairu, Umar and Ali (arXiv:2204.07427, submitted 15 April 2022) analyze Green relations, generators and semigroup rank on the same monoid, but not these probabilistic laws. Higgins's 1990 chapter on random products in transformation semigroups and 1992 treatment of probabilistic questions for the larger order-preserving monoid are particularly relevant historical comparators; only their accessible summaries, not the full chapters, could be inspected. The special Bernoulli convolution statement is not asserted to be absent from their unavailable full texts. No priority over general binomial thinning, classical Poisson approximation, or standard cutoff terminology is claimed.

## Limitations
These laws require independent factors and identically distributed increment bits within each factor; no convolution closure is asserted for arbitrary laws, heterogeneous increment parameters, partial maps, all monotone maps, or contractions that are not order-decreasing. The integer-time cutoff has a lattice window; a single universal centered limit curve without subsequence qualification would be incorrect. Historical priority remains uncertain for restricted probabilistic results implicit in unavailable older works. Independent mathematical review has not been performed.

## References
1. A. D. Adeshola and A. Umar, *Combinatorial results for certain semigroups of order-preserving full contraction mappings of a finite chain*, arXiv:1303.7428v1 (29 March 2013), revised v2 (2013), https://arxiv.org/abs/1303.7428.
2. M. M. Zubairu, A. Umar and M. J. Aliyu, *On certain Semigroup of Order-decreasing Full Contraction Mappings of a Finite Chain*, arXiv:2204.07427v1 (15 April 2022), https://arxiv.org/abs/2204.07427.
3. P. M. Higgins, *Random Products in Semigroups of Mappings*, in *Lattices, Semigroups, and Universal Algebra* (1990), pp. 89–99, DOI:10.1007/978-1-4899-2608-1_10 (abstract/preview only inspected).
4. P. M. Higgins, *Combinatorial aspects of transformation semigroups*, in *Techniques of Semigroup Theory* (1992), pp. 187–236, DOI:10.1093/oso/9780198535775.003.0006 (abstract/preview only inspected).
