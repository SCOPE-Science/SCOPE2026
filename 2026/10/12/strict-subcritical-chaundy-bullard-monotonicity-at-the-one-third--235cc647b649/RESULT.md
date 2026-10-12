# Strict subcritical Chaundy–Bullard monotonicity at the one-third threshold
## Finding
For every real \(0<p\le 1/3\), define
\[
q_k(p)=\Pr\{\operatorname{Bin}(3k,p)\ge k\},\qquad k\ge1.
\]
Then
\[
q_{k+1}(p)<q_k(p)
\]
for every integer \(k\ge1\).

Therefore, for the equal-stake averages appearing in the simultaneous-bets problem at threshold \(t=1/3\), the unique maximizing number of bets is \(m=3\). Equivalently,
\[
\sup_{m\ge1}\Pr\!\left\{\frac{\operatorname{Bin}(m,p)}{m}\ge\frac13\right\}
=
1-(1-p)^3,
\]
and equality occurs only at \(m=3\).

This settles the full \(t=1/3\), \(0<p\le1/3\) slice of the generalized Chaundy–Bullard binomial-tail question identified as open in the motivating paper. It does not settle the separate optimization over arbitrary, unequal stakes.

## Assumptions and scope
The success probability satisfies \(0<p\le1/3\). All binomial variables use independent Bernoulli trials with common success probability \(p\). The strict result excludes \(p=0\), where every displayed tail probability is zero.

The simultaneous-bets application concerns equal stakes only. For an average of \(m\) Bernoulli variables, the event at threshold \(1/3\) is
\[
\operatorname{Bin}(m,p)\ge \left\lceil\frac m3\right\rceil.
\]
No assertion is made here that equal stakes maximize over all convex combinations; that stronger statement is Csóka's conjectural layer.

## Proof
Fix \(k\ge1\). Let
\[
X\sim\operatorname{Bin}(3k,p),\qquad T\sim\operatorname{Bin}(3,p)
\]
be independent. Then \(X+T\sim\operatorname{Bin}(3k+3,p)\). Comparing the events \(\{X\ge k\}\) and \(\{X+T\ge k+1\}\), all terms cancel except the three boundary levels \(X=k,k-1,k-2\). Hence
\[
q_k(p)-q_{k+1}(p)
=
\Pr\{X=k\}\Pr\{T=0\}
-
\Pr\{X=k-1\}\Pr\{T\ge2\}
-
\Pr\{X=k-2\}\Pr\{T=3\},
\]
where the last term is zero when \(k=1\).

Using
\[
\frac{\Pr\{X=k-1\}}{\Pr\{X=k\}}
=
\frac{k}{2k+1}\frac{1-p}{p}
\]
and
\[
\frac{\Pr\{X=k-2\}}{\Pr\{X=k\}}
=
\frac{k(k-1)}{(2k+1)(2k+2)}\left(\frac{1-p}{p}\right)^2,
\]
together with
\[
\Pr\{T=0\}=(1-p)^3,
\quad
\Pr\{T\ge2\}=p^2(3-2p),
\quad
\Pr\{T=3\}=p^3,
\]
gives
\[
q_k(p)-q_{k+1}(p)
=
\Pr\{X=k\}(1-p)R_k(p),
\]
where
\[
R_k(p)
=
\frac{9k^2p^2-15k^2p+4k^2+9kp^2-17kp+6k+2p^2-4p+2}
{2(k+1)(2k+1)}.
\]
Differentiate:
\[
R_k'(p)
=
\frac{(3k+1)\bigl(6kp-5k+4p-4\bigr)}{2(k+1)(2k+1)}.
\]
For \(0<p\le1/3\), the parenthesis is at most
\[
2k-5k+\frac43-4=-3k-\frac83<0,
\]
so \(R_k\) is strictly decreasing throughout this interval. At the right endpoint,
\[
R_k(1/3)=\frac{2(3k+2)}{9(k+1)(2k+1)}>0.
\]
Thus \(R_k(p)>0\) for every \(0<p\le1/3\). Since \(\Pr\{X=k\}>0\) and \(1-p>0\), one obtains
\[
q_k(p)-q_{k+1}(p)>0.
\]

It remains to translate this to all average sizes \(m\). For each \(j\ge1\), the three sizes \(m=3j-2,3j-1,3j\) have the same success threshold \(j\). Adding a Bernoulli trial strictly increases \(\Pr\{\operatorname{Bin}(m,p)\ge j\}\) when \(0<p<1\), so within each block the largest probability occurs uniquely at \(m=3j\), where it equals \(q_j(p)\). The strict decrease of \(q_j(p)\) then makes \(m=3\) the unique global maximizer.

## Verification
The bundled `verify.py` uses exact rational arithmetic. For several rational values of \(p\) in \((0,1/3]\) and many values of \(k\), it checks the binomial tails directly, verifies the exact closed form for \(q_k-q_{k+1}\), and confirms positivity. It also checks the three-size block reduction for a deterministic finite grid.

A successful run ends with
`VERIFY_OK exact_tail_pairs=180 block_checks=72`.

These finite exact checks are regression tests only. Strict monotonicity for all real \(p\) in the claimed interval follows from the analytic factorization and derivative argument above.

## Relationship to prior work
Fokkink, Meester, and Pelekis formulate the simultaneous-bets problem and, in their final section on binomial tails, recall the Chaundy–Bullard theorem: for integer \(a>1\), the sequence
\[
\Pr\{\operatorname{Bin}(ka,1/a)\ge k\}
\]
strictly decreases in \(k\). They then state the expected generalization that
\[
\Pr\{\operatorname{Bin}(\lfloor k/t\rfloor,p)\ge k\}
\]
should be maximized at \(k=1\) whenever \(p\le1/a\le t\), and explicitly describe that generalization as unknown. Setting \(a=3\) and \(t=1/3\) produces exactly the family treated here. The present result strengthens maximum-at-one on this slice to strict decrease for every \(0<p\le1/3\).

The same paper proves a stronger arbitrary-stake statement at isolated points \(t=1/3\), \(p=1/b\) for integers \(b\ge3\). Those isolated points do not imply the fixed-\(p\) binomial monotonicity on the intervening continuum.

Fokkink, Papavassiliou, and Pelekis later study monotonicity of centered tail probabilities for sums with integer means. Their discussion recovers the classical Chaundy–Bullard case \(p=1/a\), where the threshold equals the mean. For \(p<1/3\), the present threshold \(k\) lies strictly above the mean \(3kp\), so that centered-tail theorem does not imply this subcritical result.

Targeted searches using the exact family \(\operatorname{Bin}(3k,p)\), the generalized Newton–Pepys/Chaundy–Bullard terminology, and the parameter range \(p\le1/3\) did not locate a covering published statement.

## Limitations
The theorem settles only the equal-stake binomial candidate problem at the one-third threshold. It does not establish that equal stakes are optimal among all convex combinations, so it does not by itself prove Csóka's conjecture on the full \(t=1/3\) slice.

The originality search cannot exclude an equivalent older inequality phrased under a different Newton–Pepys or binomial-tail terminology. The proof is nevertheless independent and self-contained.

## References
1. R. Fokkink, L. Meester, and C. Pelekis, *Optimizing stakes in simultaneous bets*, arXiv:2002.06804v1, first public 17 February 2020; ALEA 20 (2023), 153–165, DOI:10.30757/ALEA.v20-07.
2. R. Fokkink, S. Papavassiliou, and C. Pelekis, *On the monotonicity of tail probabilities*, Probability and Mathematical Statistics 42 (2022), 133–141, DOI:10.37190/0208-4147.00050.
3. T. W. Chaundy and J. E. Bullard, *John Smith's problem*, The Mathematical Gazette 44 (1960), 253–260, DOI:10.2307/3614890.
4. K. Jogdeo and S. M. Samuels, *Monotone Convergence of Binomial Probabilities and a Generalization of Ramanujan's Equation*, Annals of Mathematical Statistics 39 (1968), 1191–1195, DOI:10.1214/aoms/1177698243.
