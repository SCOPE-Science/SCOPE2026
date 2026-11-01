# The sharp two-to-three-seat boundary for local Distinctive Representation

## Finding
Let an approval election have \(n\ge1\) voters, at least \(k\) labeled candidates, and an exactly \(k\)-member committee. For each candidate \(c\), its supporter set is \(N_c\subseteq N\); different candidate labels may have the same supporters. Write \(q=\lceil n/k\rceil\). A committee has **justified representation** (JR) if every candidate has fewer than \(q\) supporters who approve no committee member. It has **Distinctive Representation** (DR) if it has JR and every elected candidate has exactly \(q\) supporters. The source's **Local DR** forbids a JR-preserving one-candidate exchange that strictly reduces \(\bigl||N_c|-q\bigr|\), apart from exchanges from a candidate supported by at least \(n/k\) voters to one supported by fewer than \(n/k\).

**Theorem.** For \(k=2\), whenever a DR committee exists, **every** Local-DR committee is itself DR. Consequently, any sequence of strictly improving, permitted JR-preserving exchanges started from any JR committee terminates at DR whenever DR is feasible. There is an exact linear-scan feasibility test: put \(q=\lceil n/2\rceil\), and let \(B\) be the multiset of distinct candidate labels having exactly \(q\) supporters. If \(n\) is odd, DR is feasible precisely when \(|B|\ge2\). If \(n=2q\) is even, DR is feasible precisely when \(|B|\ge2\) and either two candidates of \(B\) have different supporter sets, or (when all such sets equal \(A\)) no available candidate has a supporter set containing \(N\setminus A\). These conditions can be checked in \(O(n|C|)\) time with explicit incidence vectors.

The two-seat guarantee is sharp with respect to committee size. With \(k=3\), already six voters and five candidates with **pairwise different** supporter sets permit an exact-DR committee and also a Local-DR committee that fails DR. In this instance label the voters \(1,\ldots,6\) and candidates \(a,b,c,d,e\), with
\[
N_a=\{1,2,3,4\},\quad N_b=\{3,5\},\quad N_c=\{4,5\},\quad N_d=\{2,6\},\quad N_e=\{5,6\}.
\]
The committee \(\{b,c,d\}\) is DR, whereas \(\{a,b,e\}\) is Local DR but not DR.

## Assumptions and scope
Approval sets are arbitrary, including empty individual ballots and duplicate candidate supporter sets; candidate labels remain distinct. There are no weights or party restrictions. JR is the standard weak justified-representation property, not EJR, FJR, or reciprocal JR. Local DR means the one-exchange property in Definition 27 of Chingoma et al. (2026), including its asymmetric exception for crossing below quota. The algorithmic statement asserts termination of any strictly improving permissible JR-preserving path when DR exists; it does not claim all local optima attain DR when DR does not exist.

## Proof
First note the elementary **JR test**: write \(U(W)=\bigcup_{c\in W}N_c\). A cohesive unrepresented group exists exactly when some available candidate \(z\) has \(|N_z\setminus U(W)|\ge q\). In particular, if \(|U(W)|>n-q\), JR holds automatically. In the special case \(n=2q\), every pair whose supporter union contains more than \(q\) voters has JR.

**Exact two-seat feasibility.** When \(n=2q-1\), selecting any one candidate with exactly \(q\) supporters leaves at most \(q-1\) voters uncovered; thus every pair of such candidates has JR. When \(n=2q\), any two distinct \(q\)-element supporter sets have union of size at least \(q+1\) and hence satisfy JR. If all available \(q\)-support candidate sets are identical to \(A\), every possible candidate pair satisfying the DR support condition covers exactly \(A\); it fails JR exactly when an available candidate supports every voter in \(N\setminus A\). These observations give the claimed necessary-and-sufficient conditions, including duplicate-label cases.

**No spurious Local DR with two seats.** Fix a DR witness \(B\) and suppose a JR pair \(W\) is not DR. Every exchange below inserts a \(q\)-support candidate, so the exclusion for a replacement dropping below \(n/2\) never applies; each exchange strictly decreases the old candidate's absolute deviation from \(q\).

For odd \(n\), any committee containing a \(q\)-support candidate has JR. At least one candidate of a DR witness is outside a non-DR pair and can replace one of its non-\(q\) members, producing an allowed improvement.

Now let \(n=2q\). If \(W\) contains an elected candidate supported by more than \(q\) voters and its other member is not \(q\)-supported, replace that other member by an available \(q\)-support candidate; the large supporter set alone covers more than \(q\) voters, ensuring JR. If instead the other member \(d\) is \(q\)-supported, replace the oversized member with some other \(q\)-support candidate that preserves JR. Such a candidate exists: if any \(q\)-support candidate has a supporter set different from \(N_d\), that pair covers more than \(q\) voters; otherwise all \(q\)-support sets are identical, and feasibility of DR ensures that any pair of these candidates already satisfies JR.

If neither member exceeds \(q\) supporters and precisely one member has \(q\) supporters, replace the undersized member by another \(q\)-support candidate using the same argument (with the unchanged \(q\)-support member).

Finally, suppose both elected supporter sets are smaller than \(q\). Take any available \(q\)-support candidate \(t\). If replacing the first member \(u\) of \(W=\{u,v\}\) by \(t\) preserves JR, it is improving. Otherwise a JR obstruction for \(\{t,v\}\) requires \(q\) unrepresented voters. Since \(|N_t|=q\) and \(n=2q\), necessarily \(N_v\subseteq N_t\) and there is an available candidate whose supporters contain the whole complement \(N\setminus N_t\). As \(\{u,v\}\) is JR and \(N_v\subseteq N_t\), candidate \(u\) must cover at least one voter outside \(N_t\). Hence \(|N_t\cup N_u|>q\), so replacing \(v\) by \(t\) preserves JR and is improving. Thus no non-DR JR pair is locally optimal. Each exchange reduces the nonnegative integer \(\sum_{c\in W}\bigl||N_c|-q\bigr|\), proving finite termination at DR.

**Three-seat obstruction.** In the stated election \(q=2\). The exact-DR committee \(\{b,c,d\}\) covers voters \(2,3,4,5,6\); just one voter is unrepresented, so it has JR. The committee \(\{a,b,e\}\) covers all six voters and hence has JR, but candidate \(a\) has four supporters. Its only strictly deviation-improving exchanges are \(a\to c\) and \(a\to d\). The former leaves voters \(1,2\) unrepresented and the latter leaves voters \(1,4\) unrepresented; in either case both uncovered voters support candidate \(a\), violating JR. Every other exchange fails to reduce the support deviation strictly. Thus \(\{a,b,e\}\) is Local DR but not DR, even though \(\{b,c,d\}\) is DR. This proves sharpness in the number of seats.

## Verification
The included standalone `verify.py` implements JR directly from the candidate-wise condition; it does not assume the theorem's structural feasibility test. It independently enumerates exact-DR committees and Local-DR committees, checks the formula, and checks the three-seat witness. Running `python3 verify.py` produced:

`VERIFY_OK two_seat_unique_support_profiles=211380 random_profiles_including_duplicates=18000 three_seat_distinct_support_witness=6v_5c`

The exhaustive part ranges over elections with \(1\le n\le5\), nonempty pairwise-distinct candidate support sets and \(2\le|C|\le5\), whenever enough distinct sets exist. The pseudorandom component is seeded, uses \(2\le n\le10\), includes repeated supporter sets, and is not exhaustive. The analytical argument proves the unrestricted theorem; finite checks are corroboration only.

## Relationship to prior work
Chingoma, Grossi, Lindeboom and Maly (2026) introduce DR and Local DR, establish general DR decision hardness, give polynomial local search, and exhibit a Local-DR trap with four elected candidates (their Proposition 29). The present result distinguishes the two-seat regime, gives its exact feasibility structure, proves that **every** local optimum is globally zero-deviation whenever feasible, and reduces the first possible local trap to three seats with five distinct-support candidates. Existing justified-representation literature establishes that JR committees exist; it does not itself address the support-size local objective defining DR. These conclusions are not a consequence of the general existence of JR or of general local-search termination.

## Limitations
A Local-DR committee can fail DR when exact DR is infeasible, and the proof gives no general optimization guarantee at three or more seats. The five-candidate construction demonstrates a local trap, not that every initialization or tie-breaking choice of the published algorithm enters it. No uniqueness or minimality is claimed for the number of voters or candidates in the three-seat example. The claims have not undergone independent peer review. Although searches of the accessible mathematical records and relevant publications identified no equivalent result, differently worded or unindexed prior work remains a provenance risk.

## References
1. Julian Chingoma, Davide Grossi, Feline Lindeboom and Jan Maly, *Diverse Representation in Approval-Based Committee Voting*, arXiv:2609.29332v1, public September 24, 2026. https://arxiv.org/html/2609.29332
2. Haris Aziz, Markus Brill, Vincent Conitzer, Edith Elkind, Rupert Freeman and Toby Walsh, *Justified Representation in Approval-Based Committee Voting*, AAAI 2015. https://doi.org/10.1609/aaai.v29i1.9324
3. Edith Elkind, Piotr Faliszewski, Ayumi Igarashi, Pasin Manurangsi, Ulrike Schmidt-Kraepelin and Warut Suksompong, *The Price of Justified Representation*, arXiv:2112.05994. https://arxiv.org/abs/2112.05994
