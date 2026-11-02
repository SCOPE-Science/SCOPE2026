# Reciprocal shortcuts: an exact Braess-reversal law on directed Markov rings

## Finding
For every integer \(n\ge4\), offset \(2\le k\le n-2\), and nonnegative rates \(a,b\), take the unit-rate, one-way continuous-time Markov ring on \(\mathbb Z/n\mathbb Z\) and add a transition \(0\to k\) at rate \(a\) and \(k\to0\) at rate \(b\). Let \(L=-Q\) be the negative generator and define its integrated Kemeny relaxation by
\[
H=\sum_{\lambda\in\sigma(L)\setminus\{0\}}\frac1\lambda
=\int_0^\infty\bigl(\operatorname{tr}(e^{-tL})-1\bigr)\,dt.
\]
The nonzero spectral values are counted with algebraic multiplicity. Although individual values can be complex, the sum is real. The exact result is
\[
\boxed{H_{n,k}(a,b)=\frac{n-1}{2}+\frac{a(n-k)(k-2)+bk(n-k-2)}{2[n+a(n-k)+bk]}.}
\]
The theorem yields the following complete network-design consequences.

1. **Sharp reciprocal-chord Braess law.** For \(n=4,k=2\), the value is \(3/2\) for all nonnegative \(a,b\). For every \(n\ge5\), a genuinely bidirectional added chord with \(a=b=t>0\) increases relaxation by exactly
\[
H_{n,k}(t,t)-H_{n,k}(0,0)=\frac{t[k(n-k)-n]}{n(1+t)}>0.
\]
At fixed \(n,t\), the largest penalty occurs exactly when \(k\) is nearest to \(n/2\) (one offset if \(n\) is even, two if odd).

2. **Exact allocation of a fixed link budget.** For any fixed \(t=a+b>0\), if \(k<n/2\) the unique minimum is at \((a,b)=(t,0)\), and the unique maximum at \((0,t)\). If \(k>n/2\) the roles reverse. If \(k=n/2\), every split has equal relaxation. In particular, every positive split has strictly higher relaxation than the optimally oriented one-way shortcut unless \(k=n/2\).

3. **Sharp rate-induced reversal.** At \(k<n/2\), increasing \(a\) actually *decreases* \(H\) if and only if
\[
b>\frac{n(k-2)}{k(n-2k)}.
\]
At \(k>n/2\), increasing \(b\) decreases \(H\) if and only if
\[
a>\frac{n(n-k-2)}{(n-k)(2k-n)}.
\]
In these regimes the new reverse-oriented transition makes an already damaged network mix better in the integrated sense, without ever beating the unmodified ring when both rates are positive. For instance, \(n=7,k=3,b=3\) gives \(H(0,3)=57/16\), whereas \(H(1,3)=71/20<57/16\); both exceed \(H(0,0)=3\).

## Assumptions and scope
The original directed cycle has exactly the transitions \(i\to i+1\pmod n\), each at rate one. The two extra arrows have independent, nonnegative rates \(a,b\) and connect nonadjacent distinct vertices, so neither added arrow duplicates an existing base arrow. The system is irreducible for all rates because the original ring remains intact. We study the continuous-time negative generator, not the condition number, spectral gap, discrete-time normalization, or ordinary expected hitting time between a fixed pair. Rates are dimensionless relative to the unit base rate. All stated formulas and strict/equality cases include the endpoints \(a=0\) or \(b=0\).

## Proof
Put \(S_{i,j}=1\) if \(j\equiv i+1\pmod n\), and zero otherwise. Let \(e_j\) be the coordinate vectors. Then the negative generator is the rank-one update
\[
L=I-S+(a e_0-b e_k)(e_0-e_k)^\mathsf T.
\]
The rank-one form is noteworthy: two oppositely directed nonzero-rate arcs share a single incidence row vector. Set \(d=1+s\). Since \(S^n=I\),
\[
\operatorname{adj}(dI-S)=\sum_{j=0}^{n-1}d^{n-1-j}S^j,
\qquad\det(dI-S)=d^n-1.
\]
Applying the matrix determinant lemma in its polynomial adjugate form (thus also valid when \(d^n=1\)) gives
\[
\begin{aligned}
F(s)&=\det(sI+L)\\
&=d^n-1+a(d^{n-1}-d^{k-1})
+b(d^{n-1}-d^{n-k-1}).
\end{aligned}
\]
The off-diagonal adjugate entries used here are \((\operatorname{adj}(dI-S))_{k,0}=d^{k-1}\) and \((\operatorname{adj}(dI-S))_{0,k}=d^{n-k-1}\). Write \(F(s)=c_1s+c_2s^2+O(s^3)\). Direct binomial expansion gives
\[
\begin{aligned}
c_1&=n+a(n-k)+bk,\\
c_2&=\binom n2+a\left[\binom{n-1}{2}-\binom{k-1}{2}\right]
+b\left[\binom{n-1}{2}-\binom{n-k-1}{2}\right].
\end{aligned}
\]
Since the generator is irreducible, zero is a simple eigenvalue, all others have positive real part, and
\[
F(s)=s\prod_{j=1}^{n-1}(s+\lambda_j),\qquad H=\frac{c_2}{c_1}.
\]
Substituting the coefficients and collecting the baseline \((n-1)/2\) yields the boxed formula.

For the sign classification write \(D=n+a(n-k)+bk>0\). Its excess numerator is a sum of nonnegative terms because \(k\ge2\) and \(n-k\ge2\). Both coefficients vanish simultaneously exactly at \(n=4,k=2\). For equal rates \(a=b=t\), their sum equals \(2[k(n-k)-n]\), and for \(n\ge5\), \(k(n-k)\ge2(n-2)>n\). Maximizing \(k(n-k)\) on the allowed integer interval proves the antipodal claim.

For the fixed budget \(a+b=t\), differentiating the formula with respect to \(a\) while replacing \(b=t-a\) gives
\[
\frac{dH}{da}\Big|_{a+b=t}
=\frac{(2k-n)[2n+k(n-k)t]}{2[n+a(n-k)+(t-a)k]^2}.
\]
Its sign is precisely the sign of \(2k-n\), proving both strict allocation results and the midpoint indifference.

For unconstrained independent rate changes, direct differentiation yields
\[
\begin{aligned}
\frac{\partial H}{\partial a}
&=\frac{(n-k)[n(k-2)+bk(2k-n)]}{2D^2},\\
\frac{\partial H}{\partial b}
&=\frac{k[n(n-k-2)+a(n-k)(n-2k)]}{2D^2}.
\end{aligned}
\]
The strict threshold conditions follow by solving these linear inequalities, including equality at the precise thresholds. The numerical example is obtained by exact substitution. This concludes all dimensions and boundary values, not merely a finite enumeration.

## Verification
A companion standalone Python file, `verify.py`, uses only the standard library and exact rational arithmetic. It constructs the generators independently, computes \(c_1\) and \(c_2\) by sums of principal minors using fraction-based Gaussian elimination, and checks the characteristic polynomial against independent exact determinants at two test arguments. It also checks budget allocation, the symmetry formula, the exceptional four-state case, and the seven-state reversal. The executed checks are recorded in `VERIFICATION.md`; exhaustive symbolic reasoning above is the proof for unbounded \(n\).

## Relationship to prior work
Catral, Kirkland, Neumann and Sze established general discrete-time Kemeny identities and perturbation principles, including one-row changes, and their Section 6 treats graph structures with Kemeny constants independent of probabilities. Kirkland's 2010 directed-graph paper solves an unconstrained discrete-time optimum on a prescribed digraph, rather than this two-rate continuous-time unit-cycle objective. Kirkland and Zeng gave a directed-forest expression and demonstrated an edge-addition analogue of Braess' paradox for **undirected tree random walks**; their example class and normalization differ from the directed continuous-time rings considered here. A pre-existing one-extra-directed-shortcut calculation gives the \(b=0\) specialization; it does not determine the joint dependence on reciprocal rates or the directional nonmonotonicity and fixed-budget allocation laws. The contribution claimed here is the complete two-rate reciprocal-link classification, not the determinant lemma or general Markov perturbation methods.

## Limitations
This is not a classification for arbitrary networks, heterogeneous ring rates, more than one reciprocal pair, discrete-time transition normalizations, or any spectral-gap notion. The value is the integrated continuous-time spectral Kemeny functional; an increase in this value does not assert worsening of every possible mixing-time measure. The symmetric chord penalty compares to the base ring, whereas the directional reversal compares two already-augmented networks. Reproduced finite exact checks strengthen confidence but do not replace the all-dimensional proof. Specialized unindexed historical treatments might contain equivalent formulas; independent expert validation has not been performed.

## References
- M. Catral, S. Kirkland, M. Neumann, N.-S. Sze, *The Kemeny Constant for Finite Homogeneous Ergodic Markov Chains*, Journal of Scientific Computing 45 (2010), 151–166. https://doi.org/10.1007/s10915-010-9382-1 . Open full text: https://mural.maynoothuniversity.ie/id/eprint/2185/
- S. Kirkland, *Fastest expected time to mixing for a Markov chain on a directed graph*, Linear Algebra and its Applications 433 (2010), 1988–1996. https://doi.org/10.1016/j.laa.2010.07.016 . Open full text: https://www.hamilton.ie/skirkland/min_kemeny_final.pdf
- S. Kirkland and Z. Zeng, *Kemeny's constant and an analogue of Braess' paradox for trees*, Electronic Journal of Linear Algebra 31 (2016), 444–464. https://doi.org/10.13001/1081-3810.3222 . Open full text: https://emis.de/ft/34491
