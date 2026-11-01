# A sharp reversible line and odd–even correlation law for a two-parameter probabilistic cellular automaton

## Finding

For the finite-state stochastic interpolation between elementary cellular automaton rules 23, 77, 178, and 232, **Markov-chain reversibility occurs precisely at the unbiased-tie parameter** \(p=1/2\), for every periodic ring size \(N\ge3\) and every \(0<r<1\). At that parameter, the entire stationary distribution is an explicitly solvable second-neighbor Ising measure. The ring's parity then dictates whether adjacent spins are statistically independent or correlated, with an exact finite-size crossover near deterministic majority dynamics.

In more detail, define
\[
J=-\frac14\log(4r(1-r)),\qquad h=2\sqrt{r(1-r)},\qquad q=\tanh J=\frac{1-h}{1+h},\qquad m=\frac{N}{\gcd(N,2)}.
\]
Here \(0\le q<1\). At \(p=1/2\), the unique invariant law is
\[
\pi_{N,r}(s)=\frac1Z\exp\left(J\sum_{i\in\mathbb Z/N\mathbb Z}s_i s_{i+2}\right),\qquad s_i\in\{-1,+1\}.
\]
If \(N\) is even, the complete configurations on even and odd sites are independent; in particular \(\mathbb E_\pi[s_i s_{i+d}]=0\) for odd \(d\). For any other \(d\), take the unique \(k\in\{0,\ldots,m-1\}\) with \(2k\equiv d\pmod N\). The exact correlation is
\[
\mathbb E_\pi[s_i s_{i+d}]=\frac{q^k+q^{m-k}}{1+q^m}.
\]
At \(q=0\), use \(q^0=1\), and the value for \(k=0\) is one. Thus
\[
\mathbb E_\pi[s_i s_{i+1}]=
\begin{cases}
0,&N\text{ even},\
\displaystyle\frac{q^{(N-1)/2}(1+q)}{1+q^N},&N\text{ odd}.
\end{cases}
\]
Writing \(M=N^{-1}\sum_i s_i\), one also has \(\mathbb E_\pi M=0\) and
\[
N\operatorname{Var}_\pi(M)=\frac{1+q}{1-q}\,\frac{1-q^m}{1+q^m}.
\]
For odd \(N\to\infty\) and \(r\uparrow1\) with \(N\sqrt{1-r}\to\xi\in[0,\infty)\), the adjacent correlation converges to \(\operatorname{sech}(2\xi)\). For every even size it remains identically zero. All assertions also hold under replacing \(r\) with \(1-r\), since their stationary laws coincide on the reversible line.

## Assumptions and scope

Fix an integer \(N\ge3\), periodic indices, and \(0<p,r<1\). At each discrete time, every new spin is drawn independently conditional on the entire old configuration. Its probability of being \(+1\) is \(r\) if its two neighbors are both \(+1\), and \(1-r\) if both are \(-1\). If the neighbors disagree, the probability is \(p\) when the old center is \(+1\), and \(1-p\) when it is \(-1\). Thus \(p\) is the *probability of retaining the center spin when neighbors disagree*. All \(2^N\) transition probabilities are strictly positive. Reversibility means the stationary Markov law satisfies detailed balance, **not** invertibility of a deterministic cellular automaton.

## Proof

**Necessity of the reversible line.** Let \(A\) be the configuration of all negative spins, let \(B\) have only its last spin positive, and let \(C\) have only its last two spins positive. Denote by \(P(X,Y)\) the single-step transition probability. Since all entries are positive, Kolmogorov's cycle criterion applies. Direct multiplication of the local update probabilities gives, for every \(N\ge3\),
\[
\frac{P(A,B)P(B,C)P(C,A)}{P(A,C)P(C,B)P(B,A)}=\left(\frac{1-p}{p}\right)^2.
\]
For \(N\ge4\), the numerator's three factors are \((1-r)r^{N-1}\), \(p(1-p)(1-r)r^{N-3}\), and \(p^2(1-p)^2r^{N-4}\); the denominator's are \((1-r)^2r^{N-2}\), \(p^3(1-p)r^{N-4}\), and \(p^2r^{N-2}\). The \(N=3\) factors are respectively \((1-r)r^2\), \(p(1-p)(1-r)\), \((1-p)^2(1-r)\), and \((1-r)^2r\), \(p(1-p)(1-r)\), \(p^2r\). The ratio must be one under detailed balance. Since \(p\in(0,1)\), this forces \(p=1/2\).

**Sufficiency and stationary law.** Put \(b=\frac12\operatorname{artanh}(2r-1)\). At \(p=1/2\), the product transition kernel is
\[
P(s,t)=\prod_i\frac{\exp\{b\,t_i(s_{i-1}+s_{i+1})\}}{2\cosh[b(s_{i-1}+s_{i+1})]}.
\]
Let \(W(s)=\prod_i2\cosh[b(s_{i-1}+s_{i+1})]\). Then
\[
W(s)P(s,t)=\exp\left(b\sum_i t_i(s_{i-1}+s_{i+1})\right)
=W(t)P(t,s),
\]
where the final equality uses the symmetry of nearest-neighbor incidence on a cycle. Thus \(W/Z\) satisfies detailed balance. The identity
\[
\cosh[b(s_{i-1}+s_{i+1})]=\sqrt{\cosh(2b)}\,\exp\left(\tfrac12\log\cosh(2b)\,s_{i-1}s_{i+1}\right)
\]
gives \(J=\frac12\log\cosh(2b)=-\frac14\log(4r(1-r))\). Since every transition is positive, Perron–Frobenius theory gives uniqueness and convergence to \(\pi\) from every initial distribution.

**Exact correlations and parity.** The edges \(i\leftrightarrow i+2\) form \(\gcd(N,2)\) disjoint cycles, each of length \(m=N/\gcd(N,2)\). For even \(N\) this is a product of two independent, zero-field Ising cycles; for odd \(N\), a single cycle. The standard two-eigenvalue transfer matrix, with eigenvalues \(2\cosh J\) and \(2\sinh J\), gives the Ising-cycle partition function \(Z_m=(2\cosh J)^m+(2\sinh J)^m\) and the distance-\(k\) correlation \((q^k+q^{m-k})/(1+q^m)\). Summing the correlations over the connected subcycle gives the claimed magnetization variance. Since all first moments vanish by global spin inversion, the zero cross-parity correlation for even \(N\) follows from full independence.

**Weak-noise crossover.** Put \(h=2\sqrt{r(1-r)}\). Then \(q=(1-h)/(1+h)=\exp[-2\operatorname{artanh}h]\). Along odd sizes with \(N\sqrt{1-r}\to\xi\), one has \(Nh\to2\xi\), \(q^N\to\exp(-4\xi)\), and \(q^{(N-1)/2}\to\exp(-2\xi)\). Substitution yields \(2e^{-2\xi}/(1+e^{-4\xi})=\operatorname{sech}(2\xi)\). This limit is absent on even rings, where adjacent correlations are identically zero.

## Verification

The accompanying `verify_noisy_pca.py` independently enumerates configurations and constructs the full simultaneous-update transition matrix. It checks the Kolmogorov three-state ratio for \(N=3,\ldots,8\) and multiple interior parameter pairs; it also checks detailed balance, the normalized stationary density, all two-point correlations, the susceptibility, the \(r\leftrightarrow1-r\) symmetry, and full even/odd-sublattice factorization. The program reports 1269 successful finite diagnostics. These numerical tests do not establish the statements for arbitrary \(N\); the proof above does.

## Relationship to prior work

Muñoz and Nuño (2026) introduced the precise two-parameter probabilistic rule, established its transition formulation, and analyzed small cyclic sizes. The non-reversibility witness and the all-size sharp parameter classification are not stated in its inspected full text. The reversible heat-bath construction and its Gibbs-like stationary distribution are established generally in earlier work, particularly Cirillo, Louis, Ruszel and Spitoni (2013), Section 2, equations (2.4)–(2.6). The present proof *specializes* that known construction; its existence by itself is not claimed as new. The transfer-matrix correlation identity is also standard for a zero-field Ising cycle; the result applies it to the precisely delimited reversible line of the newer two-parameter automaton and establishes the parity-separated stationary observable laws and low-noise crossover. Related Ising parallel-update behavior was studied by Nareddy and Machta (2019/2020). The claim is about this joint sharp model classification and its consequences, not about inventing parallel heat-bath PCA or Ising transfer matrices.

## Limitations

Only finite cyclic rings with \(N\ge3\), strictly interior \(0<p,r<1\), and independent synchronous site updates are covered. Boundary deterministic rules, infinite-volume phase-transition questions, asynchronous updating, and the stationary law off the reversible line are not classified. The finite tests are not a proof of the all-size statement. Historical priority against unindexed specialized work, particularly past general characterizations of reversible probabilistic cellular automata, remains subject to further inspection; that qualification does not affect the direct mathematical derivation.

## References

1. F. J. Muñoz and J. C. Nuño, *Probabilistic Cellular Automata: between deterministic Wolfram's rules 23, 77, 178 and 232*, arXiv:2603.27799 (first posted 29 March 2026), https://arxiv.org/html/2603.27799.
2. E. N. M. Cirillo, P.-Y. Louis, W. M. Ruszel and C. Spitoni, *Effect of self-interaction on the phase diagram of a Gibbs-like measure derived by a reversible Probabilistic Cellular Automata*, arXiv:1307.8234; Eurandom Report 2013-030, especially Section 2, https://www.eurandom.tue.nl/reports/2013/030-report.pdf.
3. V. R. Nareddy and J. Machta, *Kinetic Ising Models with Self-interaction: Sequential and Parallel Updating*, arXiv:1911.03289 (2019), published in Physical Review E 101, 012122 (2020), https://arxiv.org/abs/1911.03289.
