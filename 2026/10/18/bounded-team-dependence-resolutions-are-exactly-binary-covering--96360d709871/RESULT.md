# Bounded-team dependence resolutions are exactly binary covering arrays

## Finding

Let \(k\ge1\), and let \(p_1,\ldots,p_k,q\) be distinct propositional variables. On propositional teams containing at most \(r\) valuations, consider the dependence atom \(\Delta_k := =(p_1,\ldots,p_k,q)\). A *flat resolution* is a global (inquisitive) disjunction of classical, truth-conditional formulas, and its *width* is its number of disjuncts. The minimum width \(w_k(r)\) of such a resolution of \(\Delta_k\), equivalent on all these bounded-size teams, is

\[
w_k(1)=1,\qquad w_k(r)=\operatorname{CAN}_2(2^k,\min\{r,2^k\})\quad(r\ge2),
\]

where \(\operatorname{CAN}_2(m,s)\) denotes the smallest number of rows in a binary covering array with \(m\) columns and strength \(s\). In particular, the classical strength-two covering-array theorem yields

\[
w_k(2)=\min\left\{N\ge1:\binom{N-1}{\lceil N/2\rceil}\ge2^k\right\}=k+\tfrac12\log_2 k+O(1).
\]

At the other extreme, \(w_k(r)=2^{2^k}\) for all \(r\ge2^k\). For two predictor variables, the exact width profile at successive bounds \(r=1,2,3,4\) is \(1,5,8,16\). Thus allowing larger information states changes the optimal flat disjunct count from one through a logarithmic-size covering problem to the full number of Boolean dependency functions.

## Assumptions and scope

We use standard propositional team semantics on the fixed variable set \(P=\{p_1,\ldots,p_k,q\}\). Let \(X=\{0,1\}^k\), of cardinality \(m=2^k\), and identify valuations on \(P\) with pairs \((x,b)\in X\times\{0,1\}\), where \(x\) is the predictor tuple and \(b\) is the value of \(q\). A team is an ordinary *set* of valuations, including the empty set. It satisfies \(\Delta_k\) exactly if no two valuations in the team have the same \(x\) and opposite values of \(b\).

A classical flat formula \(\alpha\) has a truth set \(S_\alpha\subseteq X\times\{0,1\}\) with \(T\models\alpha\) exactly when \(T\subseteq S_\alpha\). Every such truth set is definable by an ordinary classical propositional formula on \(P\). The global disjunction \(\alpha_1\mathbin{\mathbb V}\cdots\mathbin{\mathbb V}\alpha_d\) holds on \(T\) iff \(T\models\alpha_i\) for some \(i\); this is *not* splitting/tensor disjunction. All formula widths count only these global disjuncts, not their internal syntactic length.

A binary covering array with \(N\) rows, \(m\) labeled columns, and strength \(s\) is a binary matrix such that, for every selection of \(s\) columns, each binary pattern on them occurs as the corresponding restriction of some row. Let \(\operatorname{CAN}_2(m,s)\) denote the minimum feasible \(N\), for \(1\le s\le m\). We make no claim about efficient construction for arbitrary higher strengths.

## Proof

**Singleton regime.** Every team containing at most one valuation satisfies \(\Delta_k\). The flat tautology therefore expresses it on those teams with one disjunct, proving \(w_k(1)=1\).

**Lower bound for larger teams.** Fix \(r\ge2\) and any global disjunction of \(d\) classical flat formulas equivalent to \(\Delta_k\) on all teams of size at most \(r\). Each support set \(S_i\) of a disjunct cannot contain both \((x,0)\) and \((x,1)\) for any \(x\in X\), because the resulting two-element team violates \(\Delta_k\) but would satisfy the disjunction. Therefore \(S_i\) is the graph of a *partial* Boolean function from \(X\). Extend it arbitrarily to a total Boolean function \(f_i:X\to\{0,1\}\); this enlargement does not increase \(d\).

Put \(s=\min\{r,m\}\). For every subset \(A\subseteq X\) of size \(s\) and every assignment \(b:A\to\{0,1\}\), the team \(T_{A,b}=\{(x,b(x)):x\in A\}\) satisfies \(\Delta_k\) and has size at most \(r\). Hence it is contained in some \(S_i\), and in particular \(f_i|_A=b\). Thus the \(d\times m\) matrix having \(f_i(x)\) as its entries meets all \(s\)-column patterns: it is a binary strength-\(s\) covering array. Consequently \(d\ge\operatorname{CAN}_2(m,s)\).

**Matching upper bound.** Take a strength-\(s\) binary covering array with \(N=\operatorname{CAN}_2(m,s)\) rows, interpreting each row as a total Boolean function \(f_i:X\to\{0,1\}\). Define the ordinary classical formula \(\alpha_{f_i}\) whose truth set is the graph \(\Gamma_{f_i}=\{(x,f_i(x)):x\in X\}\); explicitly, it is the conjunction, over all \(x\in X\), of the classical implication from the conjunction specifying that predictor tuple \(x\) to the literal \(q\) or \(\neg q\), according to \(f_i(x)\).

If \(T\) is inconsistent with \(\Delta_k\), no \(\Gamma_{f_i}\) contains \(T\). If \(T\) satisfies \(\Delta_k\), it is the graph of a partial function on a predictor domain \(A\subseteq X\) of size \(t\le s\). Extend \(A\) to any size-\(s\) subset \(A'\subseteq X\) (possible because \(s\le m\)) and extend its output labeling arbitrarily. The covering property supplies a row \(f_i\) matching the extension and hence all of \(T\). Therefore the global disjunction of the \(N\) formulas \(\alpha_{f_i}\) agrees with \(\Delta_k\) on all teams of size at most \(r\), establishing equality.

**Consequences.** The strength-two binary covering-array theorem gives the displayed minimum-binomial-coefficient formula (Lawrence et al., Section 3.2.1, collecting earlier results). The central-binomial asymptotic yields \(w_k(2)=k+\tfrac12\log_2k+O(1)\). For \(s=m\), a covering array must contain every one of the \(2^m\) binary row patterns; taking them all attains the bound, yielding \(w_k(r)=2^{2^k}\) when \(r\ge m\). For \(k=2\), the covering-array optima at strengths two and three are five and eight, respectively, while strength four requires sixteen; the strength-three value follows also from the eight-row even-parity construction and the eight-pattern lower bound for any three columns.

## Verification

Run \(`python3 checker.py`\) with Python 3 and no third-party libraries. The standalone checker exhaustively searches selected binary covering arrays, obtaining widths four (two columns, strength two), five (four columns, strength two), and eight (four columns, strength three). It checks the associated flat-resolution semantics against the dependence predicate on every team up to the relevant bound: 11, 37, and 93 teams respectively. It checks all 112 required pair patterns in an explicit six-row, eight-column strength-two construction; verifies singleton behavior; and checks the full-graph count for two and four predictor valuations. This finite replay corroborates illustrative cases, not the infinite quantified theorem or the general published covering-array result, which are established by mathematical arguments.

## Relationship to prior work

Yang and Väänänen's *Propositional Logics of Dependence* (arXiv:1412.7998v3), especially Lemma 3.1 and Section 3, proves full disjunctive normal forms for downward-closed team properties using classical flat formulas. That foundational result gives the unbounded expressive translation, but does not analyze the minimal number of classical disjuncts when only bounded-cardinality teams are tested. Barbero, Girlando, Müller and Yang's 2026 *Labelled Sequent Calculi for Propositional Team Logics* develops the corresponding finite-atom team semantics, global disjunction, and proof theory; its focus is labelled calculi, not bounded-team resolution width.

The 2011 survey of binary covering arrays by Lawrence, Kacker, Lei, Kuhn and Forbes establishes the strength-two exact binomial formula and discusses general covering-array bounds, independent of team semantics. Neither the covering-array optimum nor the older full team normal form is claimed new. The finding is the *quantitative identification* of optimal bounded-team flat resolutions of one dependence atom with these covering-array numbers, and the resulting sharp team-size regimes.

## Limitations

The equality measures the minimum number of outer global disjuncts when the disjuncts are classical/flat and the available variables are fixed. It says nothing about minimum formula symbol count, optimal arbitrary nonflat disjuncts, split disjunction, additional logical connectives, or practical construction complexity. For general strengths at least three, many covering-array minima remain unknown, so the theorem transfers an exact finite optimization problem rather than supplying closed forms for all parameters. The general correspondence is proved, but its originality relative to obscure or unindexed literature is not independently established.

## References

1. F. Barbero, M. Girlando, V. Müller, and F. Yang, *Labelled Sequent Calculi for Propositional Team Logics*, arXiv:2606.31860v1, 2026-06-30; EPTCS 447 (2026), 117–136; DOI:10.4204/EPTCS.447.7.
2. F. Yang and J. Väänänen, *Propositional Logics of Dependence*, arXiv:1412.7998v3, Annals of Pure and Applied Logic 167 (2016), 557–589, especially Section 3 and Lemma 3.1; DOI:10.1016/j.apal.2016.03.003.
3. J. Lawrence, R. N. Kacker, Y. Lei, D. R. Kuhn, and M. Forbes, *A Survey of Binary Covering Arrays*, Electronic Journal of Combinatorics 18(1) (2011), P84, especially Section 3.2.1; DOI:10.37236/571.
