# Exact two-gap law and sharp total-variation rate for a simple random walk

## Finding

Let \(S_0=0\) and \(S_j=\sum_{i=1}^{j}X_i\), where the increments are independent and each equals \(-1\) or \(+1\) with probability \(1/2\). Sort the **\(n+1\) visited heights with multiplicity**, writing \(M_{0,n}\le M_{1,n}\le M_{2,n}\le\cdots\). For every integer \(n\ge2\), consider the two shifted lower order statistics
\[
H_n=(M_{1,n}-M_{0,n},\ M_{2,n}-M_{0,n}).
\]
Write
\[
u_k=\frac{\binom{2k}{k}}{4^k},\qquad
c_n=\frac12\frac{\binom{n-2}{\lfloor(n-2)/2\rfloor}}{2^{n-2}}.
\]
The **complete finite-horizon joint distribution** is
\[
\begin{array}{c|c}
(h_1,h_2)&\Pr(H_n=(h_1,h_2))\\ \hline
(0,0)&\frac14-\frac12u_{\lfloor n/2\rfloor}\\
(0,1)&\frac14\\
(1,1)&\frac12+\frac12u_{\lfloor n/2\rfloor}-c_n\\
(1,2)&c_n.
\end{array}
\]
No other pairs occur. In particular \(H_n\) converges to a random pair \(H_\infty\) with probabilities \(1/4,1/4,1/2,0\), respectively, and the **exact total-variation distance** (using \(\sup_B|\Pr(H_n\in B)-\Pr(H_\infty\in B)|\)) is
\[
\boxed{d_{\mathrm{TV}}(\mathcal L(H_n),\mathcal L(H_\infty))
=c_n\sim\frac1{\sqrt{2\pi n}}.}
\]
The sharp constant and exact finite-sample parity profile follow from the single exceptional state \((1,2)\).

## Assumptions and scope

The increments must be independent symmetric nearest-neighbor steps on the integer line. The initial height \(S_0\) is included, and ties between heights are **not removed** when sorting. The smallest three observations exist for \(n\ge2\); for \(n<2\) the random pair is not defined. The theorem is not asserted for continuously distributed increments, biased steps, conditioned bridges, or for vectors longer than two shifted statistics. No approximation in \(n\) is made in the four finite formulas.

## Proof

**1. Four possibilities and minimum multiplicities.** Since all steps are \(\pm1\), all visited integer heights between their minimum and maximum occur. Let \(R_n\) count visits to the overall minimum, among times \(0,\ldots,n\). If \(R_n\ge3\), the first two gaps equal \((0,0)\); if \(R_n=2\), they equal \((0,1)\). If \(R_n=1\), the pair is \((1,1)\), unless the level one above the minimum is visited only once, in which case it is \((1,2)\). This list is exhaustive because the path contains at least three time observations.

**2. Generating functions for the number of minimum visits.** Let \(a_m\) be the probability that a fresh walk is strictly above its start at each of its first \(m\) times; set \(a_0=1\). The reflection principle gives, for \(m\ge1\),
\[
a_m=\frac12\,u_{\lfloor m/2\rfloor},\qquad
A(z):=\sum_{m\ge0}a_mz^m
=\frac12\left(1+\frac{1+z}{\sqrt{1-z^2}}\right).
\]
Indeed the ballot/reflection count yields this expression directly for the even and odd cases. Let \(e_{2j}=\mathrm{Cat}_{j-1}/2^{2j}\) for \(j\ge1\), and let all other excursion probabilities vanish. These are the weights of a strictly positive excursion starting at zero and returning to zero for the first time at step \(2j\). The Catalan generating function gives
\[
E(z)=\sum_{j\ge1}e_{2j}z^{2j}=\frac{1-\sqrt{1-z^2}}2.
\]
Split any path with exactly \(r\) global-minimum visits at the first and last visits and at consecutive intervening minimum times. Traversed backwards from the first minimum, the initial piece is a strictly positive meander; the terminal piece after the last minimum is another strictly positive meander. Each of the \(r-1\) pieces between consecutive minimum visits is a strict-positive excursion. The pieces are unique and their step probabilities multiply. Hence, as a formal power-series identity,
\[
\sum_{n\ge0}\Pr(R_n=r)z^n=A(z)^2E(z)^{r-1},\qquad r\ge1.
\]
For \(r=1\), algebra simplifies \(A(z)^2\) to
\[
A(z)^2=\frac1{2(1-z)}+\frac{1+z}{2\sqrt{1-z^2}},
\]
so \(\Pr(R_n=1)=\tfrac12+\tfrac12u_{\lfloor n/2\rfloor}\). For \(r=2\), the key product simplifies exactly to
\[
A(z)^2E(z)=\frac{z^2}{4(1-z)}.
\]
Thus \(\Pr(R_n=2)=1/4\) for every \(n\ge2\), while
\[
\Pr(R_n\ge3)=1-\Pr(R_n=1)-\Pr(R_n=2)
=\frac14-\frac12u_{\lfloor n/2\rfloor}.
\]
Minimum-visit enumeration is a classical ingredient; the new target is its combination with occupation of the *adjacent* level and the resulting joint total-variation identity.

**3. The unique-next-level event.** Suppose the minimum is visited once and the adjacent level is also visited once. A minimum at an interior time would have two distinct time-neighbors at the adjacent level, so the unique minimum must occur at an endpoint. With the minimum at the initial endpoint, the first two steps must be \(+1,+1\); all subsequent heights must remain at least two above the minimum. Conversely this condition ensures exactly one minimum visit and exactly one visit to the next level. There is a symmetric time-reversed endpoint possibility, disjoint for \(n\ge2\). Since the weak nonnegative-walk persistence probability over \(m\) steps is
\[
b_m=\Pr(S_1\ge0,\ldots,S_m\ge0)
=\frac{\binom m{\lfloor m/2\rfloor}}{2^m},\quad b_0=1,
\]
reflection gives
\[
\Pr(H_n=(1,2))=2\left(\frac14\right)b_{n-2}
=\frac12\frac{\binom{n-2}{\lfloor(n-2)/2\rfloor}}{2^{n-2}}=c_n.
\]
Consequently \(\Pr(H_n=(1,1))=\Pr(R_n=1)-c_n\). Together with Step 2, this proves all four entries.

**4. Sharp distance, boundaries, and limit.** Writing \(k=\lfloor n/2\rfloor\), elementary binomial identities give
\[
c_{2k}=\tfrac12u_{k-1}>\tfrac12u_k\quad(k\ge1),\qquad
c_{2k+1}=\tfrac12u_k\quad(k\ge1).
\]
Therefore, relative to the candidate limiting probabilities \((1/4,1/4,1/2,0)\), the masses at \((0,0)\) and \((1,1)\) are never larger, the mass at \((0,1)\) agrees exactly, and the mass at \((1,2)\) exceeds its limit by \(c_n\). Probability conservation shows that the negative deviations sum to \(-c_n\). Their half-absolute sum, the total-variation distance, is precisely \(c_n\). Finally, central-binomial asymptotics yield \(u_k\sim(\pi k)^{-1/2}\), hence \(c_n\sim(2\pi n)^{-1/2}\). The derivation also includes the smallest possible horizon \(n=2\), where \(c_2=1/2\).

## Verification

The accompanying `verify.py` uses exact rational arithmetic and enumerates all \(2^n\) paths for \(2\le n\le14\). It independently checks the four formula entries, normalization, and total variation against the displayed limit. It also checks the binomial parity identities for \(1\le k\le30\). Run `python3 verify.py` from the extracted directory. These finite checks detect transcription and low-horizon errors; **the generating-function and endpoint arguments above**, not the enumeration, prove the result for every \(n\ge2\).

## Relationship to prior work

Pitman and Tang, *Extreme order statistics of random walks* (arXiv:2007.13991, first submitted 2020-07-28), prove total-variation convergence of finite vectors of minimum-shifted order statistics (Theorem 1.1), describe the limiting nearest-neighbor occupation process (Section 4), and derive limiting mean gaps (equation (4.3)). Their Proposition 1.6 gives a non-sharp rate under **continuous** increment laws; it does not give the present exact finite-horizon lattice two-gap law or its sharp rate. The current result is a quantitative finite-sample refinement within the symmetric nearest-neighbor model, not a result for continuous increments.

The earlier Kirschenhofer–Prodinger paper, *Return statistics of simple random walks* (1996), studies return numbers and maximum-visit counts, including a particular conditioned-bridge formulation in Section 3, by generating functions. Its maximum-multiplicity method and the standard ballot/Catalan identities are acknowledged antecedents. The inspected Sections 2–3 do not supply a law involving **both** the lowest two order-statistic gaps of the unconditioned path or the above exact total-variation distance. Aneja–Sen (1972) has an older rank-order-statistics title and unavailable complete text; equivalent coverage there or elsewhere is not excluded solely by searches.

## Limitations

This is a statement about the **first two** shifted order statistics, not about the entire minimum-centered point process. The limit and the classical counts of visits to a minimum are not claimed as original in isolation. Sharpness refers to the exact \(n\)-dependent total-variation identity, not to an optimal uniform approximation over other walk classes. Bibliographic priority is not independently established; a plausible inaccessible older rank-statistics paper remains a named residual risk. No independent audit has been performed.

## References

1. J. Pitman and W. Tang, *Extreme order statistics of random walks*, arXiv:2007.13991, original submission 2020-07-28; *Annales de l'Institut Henri Poincaré, Probabilités et Statistiques* 59 (2023), 97–116. DOI:10.1214/22-AIHP1254. https://arxiv.org/html/2007.13991v2
2. P. Kirschenhofer and H. Prodinger, *Return statistics of simple random walks*, *Journal of Statistical Planning and Inference* 54 (1996), 67–74. https://www.math.tugraz.at/~prodinger/inference.pdf
3. K. G. Aneja and K. Sen, *Random Walk and Distributions of Rank Order Statistics*, *SIAM Journal on Applied Mathematics* 23 (1972), 276–287. DOI:10.1137/0123029. Full text not inspected.
