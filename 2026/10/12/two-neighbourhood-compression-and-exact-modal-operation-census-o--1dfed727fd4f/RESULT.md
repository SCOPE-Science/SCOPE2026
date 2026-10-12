# Two-neighbourhood compression and exact modal-operation census on finite Heyting chains

## Finding

Fix an integer \(n\ge 1\) and the linearly ordered intuitionistic frame \(C_n=\{0<1<\cdots<n-1\}\). Consider **all continual constructive-neighbourhood frames** on this fixed base, with both monotone modalities \(\Box\) and \(\Diamond\) as defined below, and identify frames exactly when their induced ordered pairs of operators on the upset algebra \(\operatorname{Up}(C_n)\) coincide.

**Theorem.** Every such frame has a truth-equivalent representative with at most **two neighbourhoods at each world**, preserving every bimodal intuitionistic formula under every persistent valuation. Two is sharp for every \(n\ge2\). The exact number of different ordered pairs of induced modal operations is

\[
 A_n=1+\sum_{m=1}^{n}\left[
 \binom{n+m-1}{m}^{2}
 +\binom{n+m-2}{m-1}\left(\binom{n+m-1}{m-1}-1\right)
 +\binom{n+m-1}{m-1}
 \right].
\]

For \(n=1,2,3,4,5,6\), respectively, the counts are \(3,22,224,2634,33462,444987\). The count concerns **semantic operations on the fixed finite chain**, not the number of syntactically distinct modal formulas or accessibility frames.

## Assumptions and scope

A neighbourhood function assigns to each world \(i\) a possibly empty family \(N(i)\subseteq\mathcal P(C_n)\) of (possibly empty) subsets. A frame is *continual* if \(N(i)\ne\varnothing\) and \(i\le j\) imply \(N(j)\ne\varnothing\). A valuation maps every propositional variable to an upset. Intuitionistic implication has the usual persistent Kripke meaning. The modal clauses are

\[
 i\Vdash\Box\varphi\iff
 \forall j\ge i\;\exists S\in N(j)\;\forall u\in S\;(u\Vdash\varphi),
\]
\[
 i\Vdash\Diamond\varphi\iff
 \forall j\ge i\;\forall S\in N(j)\;\exists u\in S\;(u\Vdash\varphi).
\]

No separate frame assumptions corresponding to \(N,P,T,D,K\), intersection closure, seriality, or downward closure of neighbourhood families are imposed. The object is the unrestricted *continual* semantics of intuitionistic monotone modal logic.

## Proof

**1. Local threshold signatures.** Every formula has an upset as its truth set, by structural induction: propositional cases and implication are persistent, and either displayed modal clause at \(i\) entails the same clause at every \(j\ge i\). Write \(U_t=\{t,\ldots,n-1\}\) for \(0\le t<n\), and \(U_n=\varnothing\). For a set \(S\subseteq C_n\), use \(\min\varnothing=n\) and \(\max\varnothing=-1\). Define

\[
 b_i=\max_{S\in N(i)}\min S,\qquad
 d_i=\min_{S\in N(i)}\max S,
\]

with outer maximum of an empty family equal to \(-1\), and outer minimum of an empty family equal to \(n\). Then \(\exists S\in N(i):S\subseteq U_t\) holds exactly when \(t\le b_i\), while \(\forall S\in N(i):S\cap U_t\ne\varnothing\) holds exactly when \(t\le d_i\). Therefore

\[
 \Box U_t=\{i:t\le B_i\},\quad
 \Diamond U_t=\{i:t\le D_i\},\quad
 B_i=\min_{j\ge i}b_j,\quad D_i=\min_{j\ge i}d_j.
\]

Both complete modal operators are thus determined by the two effective threshold arrays \((B_i)\) and \((D_i)\). Conversely, assigning a propositional variable to each upset \(U_t\) shows that distinct arrays induce distinct modal operations, already at depth one.

**2. Exact local realizability and compression.** The possible pairs \((b_i,d_i)\) are precisely

\[
 E=(-1,n),\qquad F=(n,-1),\qquad
 \{(b,d):0\le b,d<n\}.
\]

Indeed, \(E\) means \(N(i)=\varnothing\); \(F\) means that \(N(i)\) contains the empty set; all remaining nonempty neighbourhood families have both coordinates in \(\{0,\ldots,n-1\}\). Conversely, \(E\) is represented by no neighbourhoods, and \(F\) by the single neighbourhood \(\varnothing\). For ordinary coordinates \(b\le d\), the single interval \(\{b,b+1,\ldots,d\}\) realizes \((b,d)\). For \(b>d\), exactly the two singleton neighbourhoods \(\{b\}\) and \(\{d\}\) realize it. These choices preserve each local threshold and the property of being continual, and hence preserve the full operators and, by formula induction, truth of every formula for every upset valuation.

The two-neighbourhood bound is sharp: for \(n\ge2\), let the top world have neighbourhood family \(\{\{0\},\{n-1\}\}\) and every lower world have an empty family. This frame is continual, and its top-world signature is \((n-1,0)\). A family of size at most one can have only signature \(E\), \(F\), or an ordinary pair satisfying \(b\le d\). Because the top-world modal truth table recovers the local pair, no one-neighbourhood-per-world frame can induce the same two operations.

**3. Continual-prefix decomposition.** The local state \(E\) occurs precisely where \(N(i)=\varnothing\). Continuality implies that these positions form an initial segment \(0,\ldots,k-1\) for a unique \(0\le k\le n\). If \(k=n\), the frame has the single all-empty-family operation pair. Otherwise the remaining suffix has length \(m=n-k\) and all local states lie in \(\{F\}\cup\{0,\ldots,n-1\}^2\). In the effective threshold array, \(B_i=-1\) exactly on the preceding initial segment, while \(B_i\ge0\) on the suffix. Thus contributions from different \(k\) are disjoint, and it remains to count signatures of a nonempty suffix of length \(m\).

**4. Counting suffix signatures.** Within that suffix, \((B_i)\) and \((D_i)\) are nondecreasing in the world index, and \(D_i=-1\) holds on an initial segment of length \(t\), \(0\le t\le m\). Every ordinary local state can be chosen independently to realize any desired nondecreasing pair of ordinary thresholds.

If \(t=0\), both arrays are ordinary nondecreasing \(m\)-tuples in \(\{0,\ldots,n-1\}\); there are \(\binom{n+m-1}{m}^2\) choices. If \(t=m\), the top local state must be \(F\), giving \(D_i=-1\) throughout and \(B_{m-1}=n\). The other \(m-1\) values form an arbitrary nondecreasing tuple in \(\{0,\ldots,n\}\), giving \(\binom{n+m-1}{m-1}\) choices.

For \(1\le t<m\), write \(r=m-t\). The boundary at which \(D\) drops from an ordinary value to \(-1\) must use the local state \(F\), so the value of \(B\) is unchanged across that boundary. If this common value is \(v\), the lower \(t-1\) values of \(B\) can be chosen in \(\binom{v+t-1}{t-1}\) ways; the upper \(r\) values of \(B\) in \(\binom{n-v+r-2}{r-1}\) ways; and the upper \(r\) values of \(D\) in \(\binom{n+r-1}{r}\) ways. Vandermonde convolution gives

\[
 \sum_{v=0}^{n-1}\binom{v+t-1}{t-1}\binom{n-v+r-2}{r-1}
 =\binom{n+m-2}{m-1}.
\]

Consequently the middle cases contribute

\[
 \binom{n+m-2}{m-1}\sum_{r=1}^{m-1}\binom{n+r-1}{r}
 =\binom{n+m-2}{m-1}\left(\binom{n+m-1}{m-1}-1\right).
\]

All possibilities in these three cases are realizable by the local normal forms of Step 2, and the cases are disjoint. Adding the one all-empty frame and summing over suffix lengths proves the displayed exact formula.

## Verification

The accompanying standalone `verify.py` uses only the Python standard library. Run `python3 verify.py`. It exhaustively enumerates all local neighbourhood families for up to three worlds and checks every possible upset at each world; it compares the closed count against explicit semantic-profile enumeration through four worlds. It also checks 4,800 deterministic random nested-formula instances against their compressed neighbourhood models and compares the symbolic binomial formula with an independently implemented finite-state recurrence through eight worlds. The expected final line is `VERIFY_OK`. The unbounded assertions are proved above rather than inferred from finite enumeration.

## Relationship to prior work

De Groot's *Intuitionistic monotone modal logic via translation* (arXiv:2507.13746, first posted 18 July 2025) introduces the relevant continual constructive neighbourhood semantics and proves completeness for the logic. Dalmonte and de Groot, *Intuitionistic Monotone Modal Logic: Proof Theory and Semantics* (arXiv:2606.31870, first posted 30 June 2026), investigate cut-free calculi, modal axiomatic extensions, and semantics. Their general frame semantics is retained here; the result instead identifies the exact fixed-chain quotient under **both** induced operators, its binomial census, and a sharp two-neighbourhood representative. No originality is claimed for the established logic, the semantic clauses, persistence, or the individual stars-and-bars identities.

## Limitations

The quotient and enumeration are for fixed labelled finite **chains** with arbitrary continual neighbourhood families, not for arbitrary finite posets or for frames constrained by extra \(N,P,T,D,K\) axioms. The two-neighbourhood bound concerns semantic equivalence over all persistent valuations on that same chain; it is not a bound on the number of worlds or proof-system complexity. No claim is made about first-order model equivalence, unique raw frame representatives, or completeness of a census for other frame classes.

## References

1. J. de Groot, *Intuitionistic monotone modal logic via translation*, arXiv:2507.13746 (version 1 publicly posted 18 July 2025); open-access journal text, *Journal of Logic and Computation* 36(4), 2026, DOI: 10.1093/logcom/exag017.
2. T. Dalmonte and J. de Groot, *Intuitionistic Monotone Modal Logic: Proof Theory and Semantics*, arXiv:2606.31870 (version 1 publicly posted 30 June 2026); *Electronic Proceedings in Theoretical Computer Science* 447 (2026), 278–298, DOI: 10.4204/EPTCS.447.16.
