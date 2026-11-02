# The longest unbalanced border determines stopped binary pattern bias

## Finding

Let \(w=w_1\cdots w_k\) be any nonempty binary word. In an independent sequence of fair bits \((X_i)_{i\ge1}\), let \(\tau_w\) be the first index at which \(w\) finishes, and define the expected empirical proportion of ones at that stopping time by
\[
q_w=\mathbb E\!\left[\frac{X_1+\cdots+X_{\tau_w}}{\tau_w}\right].
\]
A nonempty *self-border* of length \(j\) is a prefix of \(w\) which is also its length-\(j\) suffix. The full word is included as a border. Write \(J(w)\subseteq\{1,\ldots,k\}\) for these lengths and set
\[
d_j=2\sum_{i=1}^{j}w_i-j\qquad(j\in J(w)).
\]
If some \(d_j\ne0\), let \(b=\max\{j\in J(w):d_j\ne0\}\). Then
\[
\boxed{\operatorname{sgn}(q_w-\tfrac12)=\operatorname{sgn}(d_b).}
\]
If all \(d_j=0\), then \(q_w=1/2\). In particular,
\[
\boxed{q_w=\tfrac12\quad\Longleftrightarrow\quad
 \text{every nonempty self-border of }w\text{ has equally many zeros and ones}.}
\]
The implication from equal stopped frequency to balanced borders resolves precisely the \(q\)-statement of Conjecture 6.1 in Bóna–Maga–Richey, and the sign rule is stronger.

## Assumptions and scope

Only binary words of positive finite length and independent Bernoulli\((1/2)\) input bits are considered. Self-borders are nonempty and include the entire word. The statistic is \(\mathbb E[N(\tau_w)/\tau_w]\), **not** \(\mathbb E[N(\tau_w)]/\mathbb E[\tau_w]\) and **not** the limiting one-frequency \(\rho_w\) in the long-word avoidance shift. Every such stopping time is finite almost surely: splitting the sequence into disjoint blocks of length \(k\) yields \(\Pr(\tau_w>mk)\le(1-2^{-k})^m\).

## Proof

**1. A positive-kernel formula.** The joint stopping-time probability generating function established as Fact 2.9, equation (2.12), by Bóna–Maga–Richey is
\[
\Phi(x,y)=\mathbb E[x^{\tau_w}y^{N(\tau_w)}]
=\frac1{H(x,y)},\quad
H(x,y)=1+\left(1-\frac{x(1+y)}2\right)
\sum_{j\in J(w)}(2/x)^j y^{-c_j},
\]
where \(c_j=\sum_{i=1}^j w_i\). For \(0<x<1\), introduce
\[
B(x)=\sum_{j\in J(w)}(2/x)^j,\quad
M(x)=\sum_{j\in J(w)}c_j(2/x)^j,\quad
L(x)=\sum_{j\in J(w)}j(2/x)^j.
\]
Then \(H(x,1)=1+(1-x)B(x)>0\), and direct differentiation gives
\[
\partial_yH(x,1)=-xB(x)/2-(1-x)M(x),\qquad
\partial_xH(x,1)=-B(x)-(1-x)L(x)/x.
\]
The integral \(1/t=\int_0^1 x^{t-1}\,dx\) and absolute convergence permit us to write
\[
q_w=\int_0^1\frac{\partial_y\Phi(x,1)}x\,dx,
\quad
\frac12=\frac12\int_0^1\partial_x\Phi(x,1)\,dx,
\]
since \(\Phi(1,1)=1\) and \(\Phi(0,1)=0\). Subtract and use \(\Phi=1/H\) to obtain the *exact* identity
\[
\boxed{q_w-\tfrac12=\int_0^1
\frac{1-x}{2x[1+(1-x)B(x)]^2}
\left(\sum_{j\in J(w)}d_j(2/x)^j\right)\,dx.}\tag{1}
\]
The multiplier outside the sum is strictly positive on \((0,1)\). The integral converges at zero: the denominator has order \(x^{-2k}\), while the numerator has order at worst \(x^{-k-1}\), giving \(O(x^{k-1})\). At one, the integrand is \(O(1-x)\).

**2. Dominance of the last nonzero imbalance.** Let \(d_j^*=2\sum_{i=1}^j w_i-j\) be defined for *every* prefix length \(j\), not only borders. Then
\[
|d_{j+1}^*-d_j^*|=1.
\]
Suppose the last imbalanced border is \(b\) and \(d_b>0\). Since \(d_b\ge1\), every \(j<b\) satisfies
\[
d_j^*\ge d_b-(b-j)\ge 1-(b-j).
\]
For every real \(T\ge2\), all bordered terms after \(b\) vanish, so the signed border polynomial satisfies
\[
\begin{aligned}
Q(T)&=\sum_{j\in J(w)}d_jT^j\\
&\ge T^b-\sum_{j=1}^{b-1}\max\{0,b-j-1\}T^j\\
&=T^b\left(1-\sum_{h=2}^{b-1}(h-1)T^{-h}\right)\\
&>T^b\left(1-\sum_{h=2}^{\infty}(h-1)T^{-h}\right)
=T^b\left(1-\frac1{(T-1)^2}\right)\ge0.
\end{aligned}
\]
The strict inequality remains valid at \(T=2\), where the final bound is zero: the finite sum is strictly smaller than the infinite sum. Thus \(Q(T)>0\) for every \(T\ge2\). If \(d_b<0\), apply the same argument to \(-d_j^*\), whose increments also have absolute value one, obtaining \(Q(T)<0\). If every border is balanced, \(Q\equiv0\).

**3. Apply (1).** Since \(T=2/x>2\) for \(0<x<1\), the integrand in (1) has throughout the sign of \(d_b\), and is never zero when \(d_b\ne0\). Its integral has the same strict sign. When all border imbalances vanish, the integral is exactly zero. All claimed equivalences follow. \(\square\)

## Verification

The standalone Python checker `verify.py` computes borders and evaluates \(Q(T)\) at four distinct \(T\ge2\) for every one of the \(1022\) binary words of lengths one through nine, amounting to 4,088 polynomial-sign comparisons. It independently evaluates the integral in (1) numerically for named test words; for lengths up to four, it also computes the expected stopped empirical proportion by a separate prefix-automaton dynamic program, testing agreement with the analytic identity. The output in `verification_output.txt` records the successful replay. These finite checks test normalization and implementation, not the universal theorem; the proof above is all-length.

## Relationship to prior work

Bóna–Maga–Richey (2026), Definition 2.5, Fact 2.9, Proposition 3.3 and Conjecture 6.1, define the stopped statistic, provide the generating function used above, prove balance suffices, and explicitly conjecture that it is necessary. Their equation (3.8) treats the no-proper-border case, while their Theorem 3.8 relates stopped and avoidance frequencies subject to a weighted sum. Neither gives the sign classification by the *longest imbalanced border* for arbitrary mixed signs. The present conclusion supplies the previously unproved necessity for the stopped statistic; it does **not** settle the parallel conjecture about \(\rho_w\).

Chandgotia–Marcus–Richey–Wu (2024) develop autocorrelation polynomials, expected hitting times, and entropy/shift comparisons, but do not state an exact result for \(\mathbb E[N(\tau_w)/\tau_w]\). Guibas–Odlyzko (1981) supply historical string-overlap and waiting-time machinery, not claimed here as new. Older inaccessible full texts or unindexed work could still contain equivalent statements; no absolute priority claim is made.

## Limitations

The theorem assumes an independent *fair* binary sequence and a *single* finite forbidden pattern. It concerns the empirical fraction stopped on the *first* occurrence; it neither classifies longer-run avoidance density nor biased-coin, multiple-pattern, or larger-alphabet analogues. The use of the published exact bivariate generating function is explicit. Independent mathematical verification and comprehensive publication-priority verification have not been performed.

## References

1. Bóna, Maga and Richey, Letter frequency in shifts of finite type with one forbidden word, arXiv:2606.06655v2 (2026), https://arxiv.org/abs/2606.06655.
2. Chandgotia, Marcus, Richey and Wu, Shifts of Finite Type Obtained by Forbidding a Single Pattern, arXiv:2409.09024 (2024), https://arxiv.org/abs/2409.09024.
3. Guibas and Odlyzko, String overlaps, pattern matching, and nontransitive games, J. Comb. Theory A 30 (1981) 183–208, https://doi.org/10.1016/0097-3165(81)90005-4.
