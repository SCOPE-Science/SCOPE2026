# Sharp four-voter plurality gain under three-way modal competence

## Finding

**Theorem (sharp committee-size increment).** Fix a true label \(0\) among three possible labels \(0,1,2\). Let \(N\geq4\) individuals independently announce a label, with individual probability vectors \(p_i=(p_{i0},p_{i1},p_{i2})\). Suppose every individual is *weakly modally competent*: \(p_{i0}\geq p_{i1}\) and \(p_{i0}\geq p_{i2}\). A committee of size \(k\) is sampled uniformly among the \(\binom{N}{k}\) subsets. It elects a label by plurality, resolving a tie uniformly over all labels tied for first place. Write \(A_k\) for the unconditional probability that its election is correct. Then

\[
\boxed{0\leq A_4-A_3\leq\frac{1}{12}.}
\]

Both bounds are attained. The upper bound is attained for \(N=4\) by the four independent probability vectors

\[
(1,0,0),\quad(1,0,0),\quad(1/2,1/2,0),\quad(1/2,0,1/2).
\]

For this panel \(A_4=1\) and \(A_3=11/12\). The lower bound is attained when every individual always announces the correct label (and also for several less degenerate configurations). Thus an even-sized committee can gain up to \(1/12\) over a uniform random odd-sized subcommittee in three-way plurality, whereas in the binary independent-voter model, the corresponding three-to-four increment is identically zero under fair tie-breaking [Berend--Sapir].

## Assumptions and scope

Probabilities are conditional on the specified correct alternative; no prior over true states, preference ranking, rational-choice equilibrium, correlated errors, or strategic vote is assumed. The committee is selected independently of the votes and uniformly without replacement. The individual observations are independent, but need not be identically distributed. Each row \(p_i\) is a nonnegative probability distribution whose correct coordinate is no smaller than either individual incorrect coordinate. The word *modal* does not require the correct coordinate to exceed \(1/2\). Ties among winning labels are randomized uniformly; in particular a three-way tie chooses each label with probability \(1/3\). The theorem is pointwise in the unknown true label after relabeling it as \(0\).

## Proof

**Step 1: an exact four-vote influence identity.** For an ordered vote profile \(v=(v_1,v_2,v_3,v_4)\), let \(h(v)\) be the probability of correctly selecting label \(0\) with plurality and uniform tie-breaking. Define

\[
D(v)=h(v)-\frac14\sum_{i=1}^4h(v\setminus v_i).
\]

The second term is the accuracy averaged over the four possible three-person deletions, conditional on the full realized profile. Classifying the vote multiplicities shows \(D(v)=0\) unless the three labels occur with multiplicities \(2,1,1\). In that case, if label \(0\) is doubled, the four-person decision is certainly correct, whereas the deletion-average is \(2/3\), so \(D(v)=1/3\). If one of the incorrect labels is doubled, the four-person decision is certainly incorrect, whereas the deletion-average is \(1/6\), so \(D(v)=-1/6\). All remaining multiplicity patterns give zero by direct deletion. Let \(P_j\) denote the probability that all three labels appear and \(j\) is the doubled label. Taking expectation gives the exact identity

\[
A_4-A_3=\frac{2P_0-P_1-P_2}{6}.
\tag{1}
\]

**Step 2: a finite exact reduction over independent modally competent laws.** Let

\[
\mathcal P=\{(a,b,c):a+b+c=1,\;a,b,c\geq0,\;a\geq b,c\}.
\]

It is the convex hull of precisely four vectors:

\[
V_0=(1,0,0),\quad V_1=(1/2,1/2,0),\quad
V_2=(1/2,0,1/2),\quad V_3=(1/3,1/3,1/3).
\]

For completeness, for any \((a,b,c)\in\mathcal P\), set \(t=\max\{0,3(b+c-a)\}\) and write it as

\[
(a,b,c)=(a-b-c+t/3)V_0+(2b-2t/3)V_1+(2c-2t/3)V_2+tV_3.
\]

All four coefficients are nonnegative: if \(t>0\), the requirements \(t\leq3b\) and \(t\leq3c\) follow from \(a\geq c\) and \(a\geq b\), respectively; their sum is one. Since \(P_j\) and the gain in (1) are separately affine in each of four independent probability rows, the minimum and maximum over \(\mathcal P^4\) occur among the \(4^4=256\) vertex assignments.

The four row positions are exchangeable for the quantity in (1). Thus the 256 assignments reduce to the 35 sorted four-digit types in the exact table below; each digit \(j\) means using \(V_j\) as one row. Entries are exact rational gains obtained from (1), equivalently by summing the \(3^4=81\) possible ordered vote profiles for each type. The standalone program `VERIFY.py` performs both calculations with arbitrary-precision rationals, validates the profile identity for all 81 profiles, and prints the complete table.

| Sorted vertex type | \(A_4-A_3\) |
|:--|--:|
| `0000` | \(0\) |
| `0001` | \(0\) |
| `0002` | \(0\) |
| `0003` | \(0\) |
| `0011` | \(0\) |
| `0012` | \(1/12\) |
| `0013` | \(1/18\) |
| `0022` | \(0\) |
| `0023` | \(1/18\) |
| `0033` | \(2/27\) |
| `0111` | \(0\) |
| `0112` | \(1/16\) |
| `0113` | \(1/24\) |
| `0122` | \(1/16\) |
| `0123` | \(1/18\) |
| `0133` | \(5/108\) |
| `0222` | \(0\) |
| `0223` | \(1/24\) |
| `0233` | \(5/108\) |
| `0333` | \(1/27\) |
| `1111` | \(0\) |
| `1112` | \(1/32\) |
| `1113` | \(1/48\) |
| `1122` | \(1/24\) |
| `1123` | \(1/36\) |
| `1133` | \(1/54\) |
| `1222` | \(1/32\) |
| `1223` | \(1/36\) |
| `1233` | \(1/54\) |
| `1333` | \(1/108\) |
| `2222` | \(0\) |
| `2223` | \(1/48\) |
| `2233` | \(1/54\) |
| `2333` | \(1/108\) |
| `3333` | \(0\) |

Every table entry lies between \(0\) and \(1/12\), and the type `0012` attains \(1/12\). This establishes the sharp four-individual bound for **all** probability vectors in the modal polytope, not just the listed extreme cases.

**Step 3: arbitrary larger panels.** A uniform random committee of size four from \(N\) individuals, followed by uniformly deleting one member, produces a uniformly random committee of size three: each three-person subset has exactly \(N-3\) possible four-person extensions, and

\[
\frac{N-3}{4\binom{N}{4}}=\frac1{\binom{N}{3}}.
\]

Therefore \(A_4-A_3\) for the \(N\)-person panel is the average of the four-person increments over all \(\binom{N}{4}\) four-person subsets. Each such increment is in \([0,1/12]\) by Step 2, so their average is too. This completes the proof.

## Verification

Running `python VERIFY.py` with a standard Python 3 interpreter recomputes all \(256\) extreme independent laws with `fractions.Fraction`, all \(81\) ordered vote profiles, and all \(35\) permutation types. It independently calculates \(A_4\), the mean three-person deletion accuracy \(A_3\), and the doubled-label probabilities in identity (1). It also checks that uniformly deleting one person from a uniform random four-person subset reproduces a uniform random three-person subset for sample-population sizes \(4\) through \(11\) by exact combinatorial arithmetic. Expected first lines are:

```text
VERIFY_OK extreme_laws=256 permutation_types=35 vote_profiles=81 min_gain=0 max_gain=1/12
VERIFY_OK witness_accuracy_four=1 witness_accuracy_random_three=11/12
VERIFY_OK uniform_sampling_identity_n=4..11
```

The general-population part of Step 3 is a symbolic combinatorial proof, not an extrapolation from testing finitely many \(N\). The extreme-point argument establishes the infinite continuum of allowed individual probabilities from a finite exact table.

## Relationship to prior work

Saari (2002) analyzes three-alternative positional voting and plurality profiles; this provides the earlier voting-rule framework but does not, in its accessible abstract, state a distribution-free finite random-subcommittee accuracy increment. The accessible original article text of Berend and Sapir (2005), especially Theorem 1, treats independently voting *binary* experts and proves the odd-to-even random-subcommittee equality \(A_3=A_4\); that theorem cannot imply the strict positive three-label witness here because the outcome space and three-way ties differ. Goertz and Maniquet (2011) analyze three-alternative plurality for strategic information aggregation with large Poisson electorates and equilibrium strategies, rather than exact finite four-versus-three accuracy over heterogeneous independently specified label laws. Their full working paper was compared through its model, theorem statements, proofs, and conclusions. The elementary combinatorial and convexity techniques in this proof are not claimed as new.

## Limitations

The claim is a sharp upper and lower bound for one **specific pair of committee sizes** under three labels and uniform plurality ties; it does not address other size pairs, more than three labels, abstentions, unequal tie-breaking, correlated votes, or strategic behavior. Marginal modal competence alone is a weak assumption; if individuals can each be systematically most likely wrong, monotonicity need not follow. The evidence is an exact proof and internal rational verifier, not independent scientific validation. Comparable finite-jury bounds may exist in literature not accessible in full, particularly earlier plurality-profile work; novelty is therefore subject to scholarly confirmation.

## References

1. Donald G. Saari. "Adopting a Plurality Vote Perspective." *Mathematics of Operations Research* **27** (2002), 45–64. DOI: 10.1287/moor.27.1.45.340. First publicly posted online 2002-02-01, according to the publisher's bibliographic page. https://doi.org/10.1287/moor.27.1.45.340
2. Daniel Berend and Luba Sapir. "Monotonicity in Condorcet Jury Theorem." *Social Choice and Welfare* **24** (2005), 83–92. DOI: 10.1007/s00355-003-0293-z. The author-uploaded full article is available at https://www.researchgate.net/publication/2919154_Monotonicity_in_Condorcet_Jury_Theorem
3. Johanna M. M. Goertz and François Maniquet. "On a Three-Alternative Condorcet Jury Theorem." CESifo Working Paper 3457 (2011). Full working paper: https://www.ifo.de/DocDL/cesifo1_wp3457.pdf
