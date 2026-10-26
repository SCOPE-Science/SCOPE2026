# Four-run ambiguity in binary gapped pair decks is governed by a multiplication table

## Finding

Let \(w\) be a nonempty binary word and let \(\mathcal G_2(w)\) be the multiset consisting of every single letter and each ordered pair \(w_iw_j\) with \(j\ge i+2\), counted by index choices. Let \(z\) and \(t\) be the numbers of zeros and ones, and let \(q\) denote the number of occurrences of \(01\) as such a nonadjacent pair. A run is a maximal constant block.

**Theorem.** Every binary word of length at least \(3\) with at most three runs is uniquely determined, among *all* binary words, by \(\mathcal G_2(w)\). For \(t,z\ge2\), define
\[
R_{t,z}(p)=\#\{(i,j)\in\mathbb Z^2:1\le i\le t-1,\ 1\le j\le z-1,\ ij=p\}
\]
for every integer \(p\), with zero for nonpositive \(p\). Every deck of a four-run word with composition \((z,t)\) has an entire fiber of four-run words, of cardinality precisely
\[
F_{t,z}(q)=R_{t,z}(q+1)+R_{t,z}(tz-2-q).
\]
No word with another number of runs belongs to that fiber. If \(S_{t,z}=\{ij:1\le i<t,1\le j<z\}\), the **maximum size of a subset of four-run words with this composition and pairwise distinct gapped pair decks** is exactly
\[
K_{t,z}=2|S_{t,z}|-\#\{p\in S_{t,z}:tz-1-p\in S_{t,z}\}.
\]
Consequently, for lengths \(3,4,5\) every binary word is reconstructible. At length \(6\), there are exactly three nonsingleton fibers, each of size two:
\[
\{001101,010011\},\quad\{011001,100110\},\quad\{101100,110010\}.
\]
Finally, for every integer \(k\ge1\) there is a four-run gapped-pair-deck fiber of size at least \(k+1\), even though the number of runs remains four. The two length-\(2\) words \(01\) and \(10\) form a separate unavoidable short-length exception to the three-run statement.

## Assumptions and scope

Words are linear (not circular), indexed from \(1\); pair selections must be separated by at least one unselected position. The observation includes length-one subsequences; the empty subsequence is immaterial. The alphabet is exactly \(\{0,1\}\), and observations retain pair order and multiplicity. The fiber comprises all words of the same observed length, which itself is recovered from the singleton multiplicities. Four-run formulas apply for all integers \(t,z\ge2\), and the uniqueness assertion has domain \(|w|\ge3\).

## Proof

**Step 1: recovering the two run counts.** Let \(r_0\) and \(r_1\) count maximal zero-runs and one-runs, allowing zero when a letter is absent. Write \(g_{ab}\) for the observed multiplicity of the nonadjacent pair \(ab\). Of the \(\binom t2\) ordered pairs of ones, exactly \(t-r_1\) are adjacent; hence
\[
g_{11}=\binom t2-t+r_1,\qquad g_{00}=\binom z2-z+r_0.
\]
The singleton counts recover \(t,z\), then these two equalities recover both run counts. Thus no fiber can contain words with different pairs \((r_0,r_1)\). There are \(tz\) mixed ordered pairs at unrestricted distances; subtracting the \(r_0+r_1-1\) adjacent transitions gives
\[
g_{01}+g_{10}=tz-(r_0+r_1-1)
\]
for any word containing both letters. Therefore, at fixed composition and run counts, \(q=g_{01}\) determines all other entries of the deck.

**Step 2: at most three runs.** If one symbol is absent, the word is forced. For two runs, the only possibilities at fixed composition are \(0^z1^t\) and \(1^t0^z\), whose \(q\)-values are respectively \(tz-1\) and \(0\). They differ for \(t+z\ge3\); when \(t=z=1\), they coincide. For three runs with \((r_0,r_1)=(2,1)\), every word is \(0^a1^t0^{z-a}\) with \(1\le a<z\) and \(q=at-1\), which determines \(a\). With \((r_0,r_1)=(1,2)\), every word is \(1^{t-c}0^z1^c\) with \(1\le c<t\) and \(q=zc-1\), which determines \(c\). The run counts already exclude candidates with more runs, proving global uniqueness.

**Step 3: complete four-run fibers.** Such a word has \(r_0=r_1=2\) and is exactly one of two types. Type A is \(0^a1^b0^c1^d\), with \(a+c=z\), \(b+d=t\) and all four exponents positive. All \(01\) pairs number \(at+cd=zt-bc\); two of them are adjacent. Hence \(q=zt-2-bc\). For each ordered \((b,c)\) with \(1\le b<t\), \(1\le c<z\), the remaining exponents \(a=z-c\), \(d=t-b\) are uniquely forced. So type-A words realizing \(q\) are counted by \(R_{t,z}(zt-2-q)\). Type B is \(1^a0^b1^c0^d\), with \(a+c=t\), \(b+d=z\). There are \(bc\) unrestricted \(01\) pairs, one adjacent, hence \(q=bc-1\). Each eligible \((b,c)\) again uniquely fixes \(a=t-c\), \(d=z-b\). Thus type-B words realizing \(q\) are counted by \(R_{t,z}(q+1)\). The two types are disjoint and exhaust four-run words. Step 1 excludes any other run count from the fiber. This proves the formula.

**Step 4: optimal distinct-deck code.** At fixed \((z,t)\), the set of possible \(q\) from type B is \(S_{t,z}-1\), and that from type A is \(zt-2-S_{t,z}\). Their intersection has cardinality \(\#\{p\in S_{t,z}:zt-1-p\in S_{t,z}\}\). Each observed \(q\) determines exactly one deck by Step 1. One representative from each different deck yields a reconstruction code, and two representatives with the same deck cannot both belong to one. Inclusion-exclusion proves \(K_{t,z}\).

**Step 5: smallest nontrivial length and unbounded multiplicity.** For \(t+z\le5\), a four-run word has \(t,z\ge2\) and at least one of \(t-1,z-1\) equal to one, so the product map in each type is injective. Its type-A \(q\)-values are at least \(t+z-3\); its type-B values are at most \((t-1)(z-1)-1\). The former strictly exceed the latter for \(t+z\le5\). Together with Step 2 this shows uniqueness at lengths \(3,4,5\). At length \(6\), only \(t=z=3\) can have a collision: \(S_{3,3}=\{1,2,4\}\), where product \(2\) has two representations and product \(4\) has one. The two orientation sets overlap only at \(q=3\), giving precisely the three listed doubletons; all other compositions and words are singletons. For unbounded fibers choose \(t=z=2^k+1\) and \(p=2^k\). The \(k+1\) distinct pairs \((b,c)=(2^j,2^{k-j})\) for \(0\le j\le k\) all yield type-B four-run words with the same \(q=p-1\), and hence the same entire deck. \(\square\)

## Verification

The self-contained Python 3 script `verify_gapped.py` independently enumerates the nonadjacent pairs by position. It exhausts all binary words of lengths \(1\) through \(14\), checks recovery for at most three runs at lengths \(3\)–\(14\), checks the exact four-run fiber formula, and verifies the three length-six doubletons. It independently tests the exact optimum distinct-profile formula for all \(2\le t,z\le11\) and checks \(k+1\)-member four-run fibers for \(1\le k\le8\). The execution produced `VERIFY_OK` and `OPTIMAL_PROFILE_COUNT_OK`. The proof does not depend on a finite cutoff.

## Relationship to prior work

Golm, Nahvi, Gabrys and Milenkovic introduced the gapped deck and reported a length-six collision for the two-deck setting, but did not provide this all-composition, four-run factorization/fiber formula or the optimal restricted code counts in their reported results. Chrisnata, Kiah, Rao Karingula, Vardy, Yaakobi and Yao study ordinary (ungapped) \(k\)-decks, whose equality criterion does not apply to the nonadjacent-pair observation. Adjacent substring-pair spectra likewise retain different information. This theorem isolates a sharp, intrinsic run-structure boundary of the gapped observation: fixed four-run complexity supports arbitrarily high ambiguity.

## Limitations

No formula is asserted for fibers containing five or more runs or for nonbinary alphabets. This is exact for the length-one-plus-gapped-pair observation, not for pair-only decks, conventional adjacent substrings, or arbitrary \(s\)-gapped longer subsequences. Under the literal definition, the length-two words \(01\) and \(10\) have the same observation because no separated pair exists; the first nontrivial collision at length at least three occurs at six. Searches do not prove bibliographic uniqueness; potentially unindexed specialized reconstruction classifications remain a residual originality risk. Independent audit has not been performed.

## References

1. R. Golm, M. Nahvi, R. Gabrys, O. Milenkovic, *The Gapped \(k\)-Deck Problem*, arXiv:2201.12671, first submitted 2022-01-29, https://arxiv.org/abs/2201.12671.
2. J. Chrisnata, H. M. Kiah, S. Rao Karingula, A. Vardy, E. Yaakobi, H. Yao, *On the Number of Distinct \(k\)-Decks: Enumeration and Bounds*, Advances in Mathematics of Communications, 2021 early access, DOI: 10.3934/amc.2021032, https://www.aimsciences.org/article/doi/10.3934/amc.2021032.
