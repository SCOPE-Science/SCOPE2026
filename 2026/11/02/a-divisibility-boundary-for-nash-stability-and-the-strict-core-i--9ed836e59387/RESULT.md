# A divisibility boundary for Nash stability and the strict core in bipartite fractional hedonic games

## Finding

**Theorem.** Let \(a,b\geq1\) be integers and let the valuation graph of a simple symmetric fractional hedonic game be the complete bipartite graph \(K_{a,b}\). Under strict unilateral Nash deviations, all Nash-stable coalition partitions are characterized by the following finite, necessary-and-sufficient inequalities. Write every coalition as a pair \((x_i,y_i)\), giving its numbers of players from the first and second type. A partition is Nash stable exactly when every block is mixed, \(x_i,y_i\geq1\), and for every pair of distinct blocks \(i,j\),

\[
-\min\{x_i,y_j\}\leq x_i y_j-y_i x_j\leq\min\{y_i,x_j\}.
\]

The maximum utilitarian welfare is \(2ab/(a+b)\), attained exactly by the partitions in which every block has type proportions \(a:b\). Moreover, **every Nash-stable partition is welfare-maximizing and belongs to the strict core if and only if \(\min\{a,b\}\) divides \(\max\{a,b\}\)**. In the divisible case, take \(a\leq b\), \(b=qa\) for an integer \(q\geq1\). All Nash blocks then have types \((s,qs)\), and the number of Nash-stable partitions of the labeled players is

\[
N_{a,qa}=a!\,(qa)!\,[z^a]\exp\!\left(\sum_{s\geq1}\frac{z^s}{s!\,(qs)!}\right).
\]

In the nondivisible case, let \(a\leq b\), \(b=qa+r\), \(q\geq1\), \(1\leq r<a\). A Nash-stable, welfare-suboptimal partition consists of \(a-r\) blocks of type \((1,q)\) and \(r\) blocks of type \((1,q+1)\). Its exact welfare deficit is

\[
\frac{2ab}{a+b}-W_{\mathrm{witness}}
=\frac{2r(a-r)}{(q+1)(q+2)((q+1)a+r)}>0.
\]

The strict core and the social optimum both contain the grand coalition for every \(a,b\), so the price of stability is one. The price of anarchy is one exactly in the divisible cases (and strictly greater than one otherwise). No exact nondivisible price-of-anarchy formula is asserted.

## Assumptions and scope

There are \(a\) distinctly labeled players of type \(A\) and \(b\) of type \(B\). Every player values each player of the opposite type at one, and every player of the same type, including themself, at zero. A player receives the average of their valuations of all coalition members, **including themself in the denominator**. Thus a type-\(A\) player in a coalition with \(x\) type-\(A\) and \(y\) type-\(B\) members receives \(y/(x+y)\), while a type-\(B\) player receives \(x/(x+y)\). Unilateral Nash moves may join any existing other block or form a singleton, and must yield strictly higher utility. The strict core excludes coalitions whose members all weakly gain and at least one strictly gains from leaving their current coalitions to form the proposed coalition. Social welfare sums every player's coalition utility. Partitions are unlabeled collections of blocks over labeled agents. All assertions range over **every** positive integer \(a,b\) and all their partitions, not just finite tested sizes.

## Proof

**1. Mixed-block necessity and the Nash determinant test.** In any partition, a player in a type-pure coalition has utility zero. Since both types occur globally, that player can join some coalition containing an opposite-type player and strictly gain. Thus Nash stability forces all blocks mixed. For distinct mixed blocks \(i=(x_i,y_i)\), \(j=(x_j,y_j)\), set \(\Delta_{ij}=x_i y_j-y_i x_j\). A type-\(A\) player in block \(i\) improves by joining \(j\) precisely when

\[
\frac{y_j}{x_j+y_j+1}>\frac{y_i}{x_i+y_i}
\quad\Longleftrightarrow\quad
\Delta_{ij}>y_i.
\]

In the reverse direction, a type-\(A\) player in \(j\) improves precisely when \(\Delta_{ij}<-y_j\). Similarly, the type-\(B\) improvements in directions \(i\to j\) and \(j\to i\) are respectively \(\Delta_{ij}<-x_i\) and \(\Delta_{ij}>x_j\). Excluding all four improving moves is therefore exactly the displayed interval. Once blocks are mixed, utilities are positive, so a move to a singleton (utility zero) cannot improve. This proves both necessity and sufficiency.

**2. Exact welfare optimum.** Every block, including a pure block, contributes \(2x_i y_i/(x_i+y_i)\) to welfare. The identity

\[
\frac{2ab}{a+b}-\sum_i\frac{2x_i y_i}{x_i+y_i}
=\frac12\left[\sum_i\frac{(x_i-y_i)^2}{x_i+y_i}-\frac{(a-b)^2}{a+b}\right]\geq0
\]

follows by expanding the squares and then applying Cauchy–Schwarz to \(\sum_i(x_i-y_i)=a-b\) with weights \(x_i+y_i\). Equality holds exactly when \((x_i-y_i)/(x_i+y_i)=(a-b)/(a+b)\) for every block, equivalently \(b x_i=a y_i\). The grand coalition attains equality and is Nash stable.

**3. Divisibility forces proportionality.** By type symmetry assume \(a\leq b\), and suppose \(b=qa\) with integer \(q\geq1\). For each Nash block put \(\delta_i=y_i-qx_i\). The integers \(\delta_i\) sum to zero. If not all vanish, there are blocks \(i,j\) with \(\delta_i<0<\delta_j\). Then

\[
\Delta_{ij}=x_i\delta_j-x_j\delta_i\geq x_i+x_j>x_j\geq\min\{y_i,x_j\},
\]

contradicting the Nash determinant bound. Hence \(y_i=qx_i\) in every Nash block. Conversely, any partition with these proportions has all \(\Delta_{ij}=0\), and is Nash stable. Step 2 proves welfare optimality. It also lies in the strict core: every player initially has the same type-specific payoff, namely \(b/(a+b)\) for type \(A\) and \(a/(a+b)\) for type \(B\). A hypothetical mixed blocking coalition would require both of its opposite-type fractions to be at least these two fractions, one strictly greater, which is impossible because the two fractions sum to one. A pure coalition gives zero payoff to its members, also impossible as a weak improvement.

**4. The sharp nondivisible obstruction.** Suppose instead \(b=qa+r\) with \(q\geq1\) and \(1\leq r<a\). Give each type-\(A\) player a separate coalition with either \(q\) or \(q+1\) type-\(B\) players, using exactly \(a-r\) blocks of the former size and \(r\) of the latter. Every determinant between distinct blocks is \(0\), \(1\), or \(-1\). Since each block has one type-\(A\) player and at least one type-\(B\) player, the determinant test permits all these values; the partition is Nash stable. Since there are two unequal block ratios, it is welfare-suboptimal by Step 2. Direct substitution of

\[
W_{\mathrm{witness}}=2\left(\frac{(a-r)q}{q+1}+\frac{r(q+1)}{q+2}\right)
\]

into the optimum yields the asserted positive exact deficit. The partition is also **not** in the strict core: choose a type-\(A\) player from a \((1,q)\) block and all \(q+1\) type-\(B\) players from a \((1,q+1)\) block. In their proposed coalition, the selected type-\(A\) player strictly improves while the selected type-\(B\) players retain payoff \(1/(q+2)\); this is a weakly blocking coalition. Thus the divisibility boundary holds for both welfare and the strict core.

**5. Exact labeled enumeration when divisible.** For \(b=qa\), every Nash coalition has \(s\geq1\) players of type \(A\) and \(qs\) of type \(B\). The exponential formula for a set of such mixed blocks assigns an \(s\)-block weight \(z^s/(s!(qs)!)\). Taking the coefficient of total first-type size \(a\), then labeling the \(a\) and \(qa\) members, gives precisely the stated expression; blocks themselves are unlabeled and counted once. This is valid for all \(a\geq1\). Combining Steps 2–4 also yields the price-of-stability and price-of-anarchy statements.

## Verification

The standalone reproducible checker is `verification/checker.py`. Run with `python verification/checker.py`; it needs only the Python standard library. For all \(25\) unordered size pairs with \(a+b\leq10\) and \(1\leq a\leq b\), it independently enumerates all \(684404\) labeled-player set partitions, tests unilateral deviations by exact rational cross multiplication **without using** the determinant characterization, separately applies the determinant test, and checks \(5155\) Nash-stable incidences against divisible-case optimality and the exponential coefficient formula. It verifies the explicit nondivisible witness and exact rational welfare deficit as well. The script passes. Exhaustive small cases corroborate, but do not replace, the algebraic proof for arbitrary size.

## Relationship to prior work

Fioravanti, Flammini, Kodric and Varricchio (arXiv:2311.11101, initially posted 2023-11-18) study approximate *coalitional core* stability for simple fractional hedonic games and motivate a sharper comparison of stability notions. The underlying complete-bipartite *Bakers and Millers* game and its **strict-core proportionality characterization are already established** by Aziz, Brandl, Brandt, Harrenstein, Olsen and Peters (arXiv:1705.10116, Theorem 5.3). Bilò, Fanelli, Flammini, Monaco and Moscardelli (JAIR 62, 2018, Lemma 12) already establish the complete-bipartite welfare-merging inequality. Those known statements are explicitly reused rather than claimed as new. The new assertion is the exact *unilateral Nash* determinant criterion, sharp arithmetic characterization of when all Nash partitions coincide with welfare-optimal strict-core partitions, nondivisible Nash witness with quantified loss, and divisible-case labeled Nash count. The restricted-location Bakers and Millers model of Krogmann, Lenzner and Skopalik (arXiv:2501.05334) uses a different choice constraint and welfare objective.

## Limitations

This is restricted to two positive agent populations, unweighted complete bipartite valuation graphs, averaging by coalition size, unrestricted unilateral entry, and strict improvement. Nondivisible instances may have many other Nash equilibria; no exact nondivisible total count or maximal welfare loss is claimed. The exponentiated generating function counts only the divisible family. The asserted scientific priority is based on inspected literature and available records, not proof of publication uniqueness. An independent audit has not been performed.

## References

1. S. Fioravanti, M. Flammini, B. Kodric and G. Varricchio, *ε-fractional Core Stability in Hedonic Games*, arXiv:2311.11101 (initial public version 2023-11-18). https://arxiv.org/abs/2311.11101
2. H. Aziz, F. Brandl, F. Brandt, P. Harrenstein, M. Olsen and D. Peters, *Fractional Hedonic Games*, arXiv:1705.10116 (2017 extended version of earlier conference work), Theorem 5.3. https://arxiv.org/abs/1705.10116
3. V. Bilò, A. Fanelli, M. Flammini, G. Monaco and L. Moscardelli, *Nash Stable Outcomes in Fractional Hedonic Games: Existence, Efficiency and Computation*, Journal of Artificial Intelligence Research 62 (2018), 315–371, Lemma 12. https://doi.org/10.1613/jair.1.11211
4. S. Krogmann, P. Lenzner and L. Skopalik, *The Bakers and Millers Game with Restricted Locations*, arXiv:2501.05334 (2025). https://arxiv.org/abs/2501.05334
