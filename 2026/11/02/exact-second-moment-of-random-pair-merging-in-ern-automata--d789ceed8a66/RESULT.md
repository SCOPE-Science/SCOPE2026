# Exact second moment of random pair merging in Černý automata

## Finding

Let an unordered pair of distinct states be selected uniformly from an \(n\)-state Černý automaton, independently of an infinite stream of unbiased, independently drawn input letters. Let \(\tau_n\) be the first number of letters after which both selected states coincide. For every integer \(n\ge 2\),

\[
\mathbb E\tau_n=\frac{(n-1)(2n^2+n-4)}3,
\]
\[
\boxed{\mathbb E\tau_n^2=\frac{16n^6-32n^5-16n^4+66n^3-15n^2-87n+52}{15}},
\]
\[
\boxed{\operatorname{Var}(\tau_n)=\frac{28n^6-76n^5+47n^4+68n^3-130n^2-61n+76}{45}}.
\]

In particular, the coefficient of variation does not vanish:
\[
\lim_{n\to\infty}\frac{\sqrt{\operatorname{Var}(\tau_n)}}{\mathbb E\tau_n}=\sqrt{\frac75}.
\]
The principal new assertion is the exact second-moment and variance law; the first-moment calculation is given to specify the same probability experiment and to support the variance subtraction.

## Assumptions and scope

The state set is \(Q_n=\{0,1,\ldots,n-1\}\). Letter \(a\) sends state \(0\) to \(1\) and fixes each other state. Letter \(b\) sends state \(i\) to \(i+1\pmod n\). Every input letter is \(a\) or \(b\) with probability \(1/2\), independently over time. The starting pair is independent and uniform over the \(\binom n2\) *unordered* two-element subsets; \(\tau_n\) counts all letters, including steps that leave the pair unchanged. The expectations and variance above average jointly over the initial pair and the infinite random stream. They are not the variance conditional on any fixed pair.

For explicit statements about every initial pair, set \(k=\lfloor n/2\rfloor\), and, for \(1\le r\le k\), let \(m_r=n\), except that \(m_k=k\) when \(n=2k\). Each pair has exactly one representation
\[
P_{r,s}=\{(-s)\bmod n,(r-s)\bmod n\},\quad 0\le s<m_r.
\]
Define
\[
X_r=2(n-1)^2+(r-1)(4n^2-12n+4)-(r-1)(r-2)(4n-2),
\]
\[
D_r=4n^2-12n+4-(r-1)(8n-4),
\]
\[
J_r=\begin{cases}0,&n=2k\text{ and }r=k,\\D_r/2,&\text{otherwise}.\end{cases}
\]
Then the conditional first moment is
\[
T_{r,s}:=\mathbb E[\tau_n\mid P_{r,s}]=X_r+2s+J_r\mathbf1_{s\ge r}.
\]
The convention at the even-diameter layer is essential: there \(m_k=k\), so the exceptional phase \(s=k\) is absent.

## Proof

**1. Pair coordinates and absorption.** Rotation by \(b\) sends \(P_{r,s}\) to \(P_{r,s-1}\), with the index \(s\) read modulo \(m_r\). The letter \(a\) fixes the pair except at \(s=0\) and, if present, at \(s=r\). At \(s=0\), it merges \(r=1\), and otherwise sends \(P_{r,0}\) to \(P_{r-1,n-1}\). For \(r<k\), it sends \(P_{r,r}\) to \(P_{r+1,r}\); when \(n\) is odd and \(r=k\), it sends \(P_{k,k}\) to \(P_{k,n-1}\). For even \(n=2k\), that last exceptional phase does not exist. These cases follow directly from the two letter actions. Every pair has a finite merging word, so a fixed positive probability of reaching the absorbing singleton in some bounded number of future letters holds uniformly over the finite pair state space. Thus the first two moments are finite, and their absorbing-chain Bellman systems have unique solutions.

**2. First moments.** The Bellman equation \(2T(P)=2+T(Pa)+T(Pb)\), with \(T\) zero on singletons, gives the displayed \(T_{r,s}\) by substitution. Off the exceptional phases the increment is \(T_{r,s}-T_{r,s-1}=2\). At \(s=r\), the additional increment is \(J_r\); the equations at \(s=0\) and at the top-distance layer supply the polynomial \(X_r\) and the stated boundary value of \(J_r\). The formulas remain valid for \(n=2,3\) by direct substitution.

**3. A closed solution of the second-moment Bellman equations.** Put \(U_{r,s}=\mathbb E[\tau_n^2\mid P_{r,s}]\). From \(\tau_n=1+\tau_n'\) before absorption and the preceding first-moment equation,
\[
2U(P)=4T(P)-2+U(Pa)+U(Pb),\qquad U(\{i\})=0.
\]
Define the following explicit polynomials (all indices lie in their stated finite ranges):
\[
Y_1=\frac{2(n-1)(4n^4-6n^3-6n^2+13n-9)}3,
\]
\[
d_r=\frac43\bigl[4n^5-10n^4+19n^2-13n+(8n^2-26n+17)r
+(-24n^3+36n^2-6)r^2+(16n^2-16n+4)r^3\bigr],
\]
\[
Y_r=Y_1+\sum_{j=1}^{r-1}d_j,
\qquad
K_r=\begin{cases}0,&n=2k\text{ and }r=k,\\d_r/2+(2r-1)D_r,&\text{otherwise},\end{cases}
\]
\[
B_{r,s}=s(4X_r-2)+4s(s+1)+4J_r\max\{0,s-r+1\}.
\]
The complete conditional second-moment solution is
\[
\boxed{U_{r,s}=Y_r+B_{r,s}+K_r\mathbf1_{s\ge r}.}
\]
The algebraic verification is finite but uniform in \(n\): at ordinary phases, \(B_{r,s}-B_{r,s-1}=4T_{r,s}-2\). At the exceptional \(s=r<k\), the jump equation reduces to \(2K_r=d_r+2(2r-1)D_r\), exactly the definition above; at the odd terminal phase it reduces to \(K_k=B_{k,n-1}-B_{k,k}\). At phase zero, the \(r=1\) equation is \(Y_1=4X_1-2+B_{1,m_1-1}+K_1\mathbf1_{m_1>1}\). For \(r>1\), the phase-zero equations are
\[
d_{r-1}=4X_r-2+B_{r-1,n-1}+K_{r-1}+B_{r,m_r-1}+K_r\mathbf1_{m_r>r}.
\]
Substitution of the displayed polynomials verifies these identities for both parity regimes; at \(n=2\), the one-state pair chain gives \(T=2\), \(U=6\). Since the second-moment Bellman system has a unique solution, the formula for \(U_{r,s}\) is exact for every \(n\ge2\).

**4. Sum over every starting pair.** With \(m=m_r\), summing the explicit conditional second moments over the phases of the \(r\)-th layer gives
\[
\sum_{s=0}^{m-1} U_{r,s}=mY_r+\frac{m(m-1)}2(4X_r-2)
+\frac{4m(m-1)(m+1)}3
+2J_r(m-r)(m-r+1)+K_r(m-r).
\]
For the even top layer \(m=r=k\), the final two terms are zero. Summing this identity over \(1\le r\le k\), substituting \(Y_r,Y_1,d_r,X_r,J_r,K_r\), and applying the standard finite power-sum identities gives the following two explicit polynomial reductions:
\[
\sum_{r,s}U_{r,s}=\frac{2k(2k-1)}{15}(512k^6-512k^5-128k^4+264k^3-30k^2-87k+26),\quad n=2k,
\]
\[
\sum_{r,s}U_{r,s}=\frac{2k(2k+1)}{15}(512k^6+1024k^5+512k^4+8k^3+14k^2-47k-8),\quad n=2k+1.
\]
In both parities the expression simplifies to
\[
\sum_{r=1}^k\sum_{s=0}^{m_r-1}U_{r,s}
=\binom n2\frac{16n^6-32n^5-16n^4+66n^3-15n^2-87n+52}{15}.
\]
Likewise, summing \(T_{r,s}\) gives \(\binom n2(n-1)(2n^2+n-4)/3\). Divide by \(\binom n2\), subtract the square of the mean, and compare the leading coefficients to obtain both displayed conclusions. No asymptotic approximation enters either finite-length identity.

## Verification

Two dependency-free Python files, `verify_random.py` and `verify_second.py`, reproduce the expectations directly from the letter actions. Run `python verify_random.py` and `python verify_second.py` in the same directory. They check all \(85{,}320\) unordered pair states across \(2\le n\le80\), both moment Bellman equations, both displayed aggregate polynomial identities, and independently solve the mean and second-moment absorption systems by exact rational Gaussian elimination for all \(2\le n\le11\), covering \(220\) additional exact state comparisons per moment. Their observed outputs are `VERIFY_OK` and `VERIFY_SECOND_OK`. These finite computations corroborate but do not replace the all-integer polynomial identities and absorbing-chain proof above.

For illustration, the mean and second moment at \(n=2\) are \(2\) and \(6\); at \(n=3\), they are \(34/3\) and \(806/3\); at \(n=4\), they are \(32\) and \(6472/3\). At \(n=5\), the second moment is \(49164/5\).

## Relationship to prior work

Gusev (2014) analyzes exactly the independent random-letter Černý model, derives first-moment recurrences, and gives formulas for the worst initial pairs for both parities and arbitrary Bernoulli bias. Those results explain why the expectations are finite and cubic in \(n\), but neither its theorems nor the inspected full Section 3 state an exact **second** moment, the variance for a uniformly sampled initial pair, or the limiting coefficient of variation above. The recent Lipin–Volkov (2026) paper and Szykuła (2026) survey study deterministic and adversarial aspects of the same Černý family, rather than these random-input fluctuations. This result concerns a different, explicitly specified random-pair observable and is not a claim of a new worst-pair first-moment bound. Mathematical priority beyond the checked texts and indexed records is not independently certified.

## Limitations

The theorem applies to the classical Černý transition graph, a fair binary letter source, an independent **uniform unordered** initial pair, and the first time the selected pair merges. It does not calculate the hitting-time distribution, moments of order three and above, conditional variance for every specific initial pair in simplified closed form, all-state reset time, biased input streams, or random automata sampled from a distribution. The polynomial proof does not itself establish publication priority; independent mathematical audit remains outstanding.

## References

- A. E. Lipin and M. V. Volkov, *Adversarial Synchronization*, arXiv:2601.18362, first public January 26, 2026, https://arxiv.org/abs/2601.18362.
- M. Szykuła, *Synchronizing Automata: Open Problems*, arXiv:2608.24245, first public August 25, 2026, https://arxiv.org/abs/2608.24245.
- V. V. Gusev, *Synchronizing automata with random inputs*, arXiv:1404.6731, first public April 27, 2014, https://arxiv.org/abs/1404.6731.
