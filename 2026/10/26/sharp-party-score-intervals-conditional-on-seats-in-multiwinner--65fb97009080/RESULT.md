# Sharp party-score intervals conditional on seats in multiwinner Borda voting

## Finding

Let \(m\ge2\) candidates be partitioned into two nonempty parties, of sizes \(r\) and \(m-r\), and let \(1\le k\le m\) seats be awarded by \(k\)-Borda. If some winning committee gives the first party exactly \(t\) seats, where
\[
\max\{0,k-(m-r)\}\le t\le\min\{r,k\},
\]
then its normalized aggregate Borda score \(\psi\) satisfies the following **sharp and complete** interval:
\[
\boxed{
\frac{r(r-1)+t(m-r-k+t)}{m(m-1)}
\ \le\ \psi\ \le\ 
\frac{r(2m-r-k-1)+t(r+k-t)}{m(m-1)}.
}
\]
Both endpoints occur for finite electorates admitting such a winning committee. Every rational number in the interval occurs for a finite electorate; every rational number strictly between the endpoints occurs with a **unique** winning committee containing exactly \(t\) first-party candidates.

For a party receiving **no seats** (\(t=0\)), its aggregate score can approach
\[
\frac{r(2m-r-k-1)}{m(m-1)}.
\]
In particular, taking \(r=m-k\), this upper endpoint is \(1-k/m\). Thus, for every fixed \(k\), there are arbitrarily large elections with no first-party winner although that party's aggregate Borda score is arbitrarily close to \(1\). The statement concerns normalized scores and party affiliations, **not** first-choice vote shares or cohesion of party supporters.

## Assumptions and scope

Every voter supplies a strict complete ranking of the \(m\) labeled candidates. A candidate ranked in position \(j\in\{1,\ldots,m\}\) receives \(m-j\) Borda points. A \(k\)-Borda committee is any \(k\)-element set maximizing the sum of its members' total Borda scores, equivalently a selection of the \(k\) candidates with largest individual totals; ties may give multiple winning committees. Both parties contain at least one candidate, but neither party-list rankings nor within-party voter cohesion are assumed. The electorate is finite and nonempty. For \(i\) in the first party let \(s_i\) be their total Borda score and set
\[
\psi=\frac{\sum_{i\in A}s_i}{n\,m(m-1)/2},
\]
where \(n\) is the number of voters. This is the Borda specialization of the aggregate party score in Boratyn–Stolicki (2026). Exactly two parties are needed only to name the complement; the inequalities apply to any designated group of candidates versus all other candidates jointly.

## Proof

Put \(S_j=\sum_{a=0}^{j-1}(m-1-a)=j(2m-j-1)/2\) for \(0\le j\le m\). Divide all Borda totals by \(n\), obtaining a score vector \(v\). Each ballot assigns a permutation of \((m-1,m-2,\ldots,0)\), so \(v\) is their average. The elementary rearrangement inequality consequently says that for any fixed nonnegative coefficient vector with \(t\) entries equal to \(1\), \(h\) entries equal to \(\alpha\in[0,1]\), and all other entries \(0\), its dot product with \(v\) is at most \(S_t+\alpha(S_{t+h}-S_t)\). This follows per ballot by exchanging inverted coefficient-score pairs, then averaging; no infinite-dimensional argument is needed.

Fix a winning committee \(W\) of size \(k\) and let \(T=W\cap A\), \(L=A\setminus W\), and \(U=W\setminus A\). Their sizes are respectively \(t\), \(r-t\), and \(k-t\). Since \(W\) comprises the highest-scoring candidates, \(v_u\ge v_\ell\) for all \(u\in U\) and \(\ell\in L\). With \(X=\sum_{\ell\in L}v_\ell\), \(Y=\sum_{u\in U}v_u\), \(h=r+k-2t\), and \(\alpha=(r-t)/h\) for \(h>0\), we obtain \(X\le\alpha(X+Y)\). This includes either empty-set case by continuity of the elementary inequality (when \(U=\varnothing\), \(\alpha=1\); when \(L=\varnothing\), \(\alpha=0\)). When \(h=0\), both sets are empty and omit the middle term entirely. Therefore
\[
\sum_{i\in A}v_i=\sum_{i\in T}v_i+X
\le\sum_{i\in T}v_i+\alpha\sum_{i\in L\cup U}v_i
\le S_t+\alpha(S_{t+h}-S_t).
\]
For \(h>0\), the average of the positional Borda scores at positions \(t+1\) through \(t+h\) equals \((2m-r-k-1)/2\). Substitution, including the \(h=0\) boundary, yields
\[
\sum_{i\in A}v_i\le
\frac{r(2m-r-k-1)+t(r+k-t)}2.
\]
Dividing by \(S_m=m(m-1)/2\) gives the asserted upper bound. Interchanging the two parties, and using that the complementary party has \(m-r\) candidates and wins \(k-t\) seats, gives \(1-\psi\) bounded above by the same expression with those substituted parameters. Algebra gives the asserted lower bound.

To attain the upper endpoint, label \(t\) elected first-party candidates \(T\), the \(r-t\) unelected first-party candidates \(L\), and the \(k-t\) elected complementary candidates \(U\). Rank the members of \(T\) in the first \(t\) positions in a fixed order. Rotate cyclically the \(h=r+k-2t\) members of \(L\cup U\) through the next \(h\) positions over \(h\) ballots (one ballot if \(h=0\)); put all other candidates below them in any fixed order. Every candidate in the middle block has the same average score. Thus \(T\cup U\) is a winning committee and equality holds in both inequalities. When \(h=0\), all selected first-party candidates occupy the highest positions and the same conclusion holds. The lower endpoint follows from the party-swapped construction, with the *same* labeled committee \(T\cup U\).

Mix the two endpoint ballot profiles in any rational proportion by repeating their finitely many ballots until integer multiplicities are obtained. Both endpoint profiles admit the same winning committee, so their mixtures do too. The aggregate party score varies affinely and covers every rational value in the closed interval. At every strict mixture, every elected candidate beats every unelected candidate: a selected first-party candidate is strictly ahead of any first-party loser in the upper-endpoint construction, and of any complementary-party loser there as well; a selected complementary-party candidate is strictly ahead of any first-party loser in the lower-endpoint construction and of any complementary-party loser there as well. All remaining elected-versus-unelected comparisons are strict in at least one endpoint construction and weak in the other. Positional Borda weights are strictly decreasing, so strict mixing gives a unique winning committee. Empty comparison classes cause no difficulty. This proves completeness and the uniqueness assertion.

For the last claim, set \(r=m-k\) and \(t=0\); the upper expression simplifies to \((m-k)/m\). Keeping \(k\) fixed and increasing \(m\), choose any rational score just below that achievable endpoint to obtain a uniquely winning all-complement committee and a first-party score approaching \(1\).

## Verification

The accompanying `verify.py` uses only the Python standard library and exact rational arithmetic. It independently constructs cyclic endpoint profiles for every feasible parameter tuple with \(2\le m\le12\), checks exact endpoint equality and a strict mixed profile, exhaustively verifies all one- and two-ballot profiles for \(2\le m\le5\), and checks additional deterministic-seed profiles. Its run passed 304959 assertions. These finite checks supplement, rather than replace, the all-size proof.

An explicit 51-voter example has \(m=10\), \(r=8\), \(k=2\), and \(t=0\). Take five copies of each of the ten cyclic rotations of all ten candidates, plus one ballot ranking the two complementary-party candidates first and second and the eight first-party candidates afterward. The two complementary candidates are the unique winners, while the first party receives exactly \(1828/2295>79/100\) of the total Borda score. The exact optimal upper bound for these parameters is \(4/5\).

## Relationship to prior work

Boratyn and Stolicki (2026), *Allocation Proportionality of OWA-Based Committee Scoring Rules*, arXiv:2602.10083, defines the aggregate party score, defines the separable \(k\)-Borda rule, and primarily measures proportionality empirically. Its Sections 4–7 were inspected; they do not give a sharp feasible interval conditional on party candidate count and seats won. The current contribution fixes those prior definitions, derives the complete two-party numerical envelope, and identifies the candidate-cardinality obstruction for the proposed score metric. The rearrangement principle and Borda scoring rule themselves are classical and are not claimed as new.

Boratyn et al., *Spoiler Susceptibility in Party Elections* (DOI:10.3233/FAIA251258), considers Borda party totals but subsequently apportions seats through separate seat-allocation methods, rather than selecting the top \(k\) individual candidates. Darmann and Klamler, *Proportional Borda Allocations* (DOI:10.1007/s00355-016-0982-z), assigns indivisible items to agents under proportionality constraints; its Borda item-allocation statements do not imply this inverse score-versus-seat interval. Grofman, Feld and Fraenkel's threshold-of-exclusion paper (DOI:10.1016/j.mathsocsci.2016.11.004, Sections 1–3 and the full five-page original text inspected) analyzes the largest share of *voters in a supporting bloc* that can be denied representation. Their general scoring-rule calculation is not a bound on the fraction of all candidate Borda points accruing to an affiliated party with a prescribed number of candidates and elected seats. In particular, the party score considered here need not equal the share of voters who support that party. Published literature under other terminology may exist; absence in a finite search does not certify priority.

## Limitations

The theorem applies to complete strict ranked ballots, additive \(k\)-Borda, and the aggregate Borda measure; it does not establish bounds for nonlinear OWA rules such as Chamberlin–Courant or PAV, actual party-level vote shares, party-list ballots, or multiple-district elections. Achieving an endpoint can require ties, and the theorem explicitly distinguishes tie-admitting endpoints from unique-winner interior realizations. Candidates of the same party need not form a cohesive group in the profile. The complete 2017 threshold-of-exclusion paper was inspected via the author-hosted lawful copy; its party-vote-share criterion is distinct. A broader, differently named inverse-scoring result in the remaining literature could still establish priority. No independent audit is claimed.

## References

1. D. Boratyn and D. Stolicki, *Allocation Proportionality of OWA-Based Committee Scoring Rules*, arXiv:2602.10083 (first public version 2026-02-10), https://arxiv.org/abs/2602.10083.
2. D. Boratyn, W. Słomczyński, D. Stolicki, and S. Szufa, *Spoiler Susceptibility in Party Elections*, DOI:10.3233/FAIA251258, https://journals.sagepub.com/doi/10.3233/FAIA251258.
3. A. Darmann and C. Klamler, *Proportional Borda Allocations*, *Social Choice and Welfare* 47 (2016), 543–558, DOI:10.1007/s00355-016-0982-z.
4. B. Grofman, S. Feld, and J. Fraenkel, *Finding the Threshold of Exclusion for All Single Seat and Multi-Seat Scoring Rules*, *Mathematical Social Sciences* 85 (2017), 52–56, DOI:10.1016/j.mathsocsci.2016.11.004.
