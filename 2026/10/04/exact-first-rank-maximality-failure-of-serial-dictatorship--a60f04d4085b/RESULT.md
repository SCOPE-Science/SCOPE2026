# Exact first rank-maximality failure of serial dictatorship
## Finding
Consider one-sided house allocation with the same number of agents and objects, complete strict preferences, and a fixed priority order for serial dictatorship. The serial-dictatorship outcome is rank-maximal for every \(2\times2\) preference profile.

For three agents and three objects there are
\[
6^3=216
\]
labeled strict-preference profiles. Exactly
\[
54
\]
of them have a serial-dictatorship outcome that is not rank-maximal. Thus the exact impartial-culture incidence is
\[
\frac{54}{216}=\frac14.
\]

For a matching \(M\), write its rank signature as
\[
\rho(M)=(x_1,x_2,x_3),
\]
where \(x_j\) is the number of agents receiving their \(j\)-th choice. A rank-maximal matching lexicographically maximizes this signature.

Among the \(54\) failing profiles, the rank-maximal set consists of one matching in \(36\) profiles and two matchings in \(18\). The exact signature improvement distribution is
\[
(2,0,1)\longrightarrow(2,1,0)
\]
for \(24\) profiles, and each of
\[
(1,1,1)\longrightarrow(2,0,1),\qquad
(1,2,0)\longrightarrow(2,0,1),
\]
\[
(1,1,1)\longrightarrow(1,2,0),\qquad
(1,1,1)\longrightarrow(2,1,0),\qquad
(1,2,0)\longrightarrow(2,1,0)
\]
for \(6\) profiles.

Under relabeling of the three objects, the \(54\) failures form exactly \(9\) classes, all of orbit size \(6\). Normalizing agent \(1\)'s ranking to \(A\succ B\succ C\), the nine representatives are
\[
(ABC,ABC,BAC),\quad
(ABC,ABC,BCA),\quad
(ABC,ACB,ACB),
\]
\[
(ABC,ACB,CAB),\quad
(ABC,ACB,CBA),\quad
(ABC,BCA,BAC),
\]
\[
(ABC,CAB,ACB),\quad
(ABC,CBA,ACB),\quad
(ABC,CBA,CAB).
\]

Hence three agents are the first balanced market size at which fixed-priority serial dictatorship can sacrifice the lexicographically maximal rank profile.

## Assumptions and scope
Every agent has a strict complete ranking of all objects. Serial dictatorship processes agents in a fixed exogenous order and gives each agent her most-preferred still-available object.

Rank-maximality is defined by the lexicographic rank signature \(\rho(M)\): first maximize the number of first choices, subject to that maximize second choices, and so on. All perfect matchings are feasible because preferences are complete and the market is balanced.

The theorem compares the deterministic serial-dictatorship outcome with the full set of rank-maximal matchings. It does not impose a tie-break among multiple rank-maximal matchings.

## Proof
For \(2\times2\), if the two agents have distinct first choices, serial dictatorship gives both first choices and is trivially rank-maximal. If they share a first choice, at most one agent can receive a first choice in any matching; serial dictatorship gives one first choice and the other agent's second choice, so its signature is the unique lexicographically maximal signature \((1,1)\).

For \(3\times3\), the finite domain has \(216\) preference profiles and six perfect matchings per profile. The verifier computes the serial-dictatorship outcome and the signature of every perfect matching. The lexicographic maximum is then exact by direct comparison.

Two independent descriptions of rank-maximality are checked. The first directly lexicographically maximizes \(\rho(M)\). The second assigns rank weights \(4^2,4,1\) to first-, second-, and third-choice edges and maximizes the resulting integer score. Because at most three agents contribute at any rank, base \(4\) makes this scalar objective exactly equivalent to lexicographic signature maximization. The two implementations return identical rank-maximal sets for all \(216\) profiles.

Serial dictatorship is also replayed in two independently organized implementations. The complete failure set has size \(54\). Canonicalizing each failure by the unique object relabeling that sends agent \(1\)'s ranking to \(ABC\) produces exactly the nine representatives listed above, each with six labeled realizations.

The rank-maximal-set-size and signature-transition counts sum to the same \(54\) failures, providing independent internal marginals.

## Verification
The embedded `verify_sd_rankmax_3x3.py` uses only the Python standard library and exact integer arithmetic.

It verifies:
- all four \(2\times2\) profiles are rank-maximal under serial dictatorship;
- all \(216\) \(3\times3\) profiles and all six perfect matchings of each;
- equality of two serial-dictatorship implementations;
- equality of direct lexicographic and steep-base integer implementations of rank-maximality;
- exactly \(54\) failures;
- rank-maximal-set sizes \(36\) unique and \(18\) doubleton cases;
- the full six-cell signature-transition histogram;
- exactly nine object-relabeling classes, each of size six.

Run:

`python3 verify_sd_rankmax_3x3.py`

The first output line must be `VERIFY_OK`.

## Relationship to prior work
Serial dictatorship is a classical deterministic allocation mechanism and underlies random serial dictatorship in house-allocation theory. Abdulkadiroğlu and Sönmez study random serial dictatorship and its relation to the core from random endowments.

Irving, Kavitha, Mehlhorn, Michail, and Paluch define the signature of a one-sided matching and define a rank-maximal matching as one with lexicographically maximum signature. Their work develops algorithms for computing such matchings and motivates rank-maximality as a practical one-sided matching criterion.

The inspected primary rank-maximal paper defines and algorithmically studies the objective but does not state this fixed-priority serial-dictatorship \(2\times2\)-to-\(3\times3\) boundary, the exact \(54/216\) prevalence, the nine object-symmetry classes, or the signature-transition census. Targeted searches for those formulations did not locate an equivalent published classification.

## Limitations
The exact census is restricted to balanced markets with at most three agents, strict complete preferences, and one fixed serial-dictatorship priority. The theorem does not classify larger markets, random priorities, incomplete preference lists, ties, capacities, or other profile-based matching criteria.

The novelty search cannot exclude an unindexed exercise, lecture note, code repository, or supplementary computation containing the same small-market census.

## References
1. A. Abdulkadiroğlu and T. Sönmez, “Random Serial Dictatorship and the Core from Random Endowments in House Allocation Problems,” *Econometrica* 66 (1998), 689–701. DOI: 10.2307/2998580.
2. R. W. Irving, T. Kavitha, K. Mehlhorn, D. Michail, and K. E. Paluch, “Rank-Maximal Matchings,” *Proceedings of SODA 2004*, 68–75; journal version in *ACM Transactions on Algorithms* 2 (2006), 602–610.
