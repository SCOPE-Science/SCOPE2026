# Cyclic bigram certificates and all minimum attractors of distinct-run powers

## Finding

Let \(q\ge3\), let \(a_0,\ldots,a_{q-1}\) be distinct symbols, choose positive integers \(r_0,\ldots,r_{q-1}\), and let \(k\ge2\). Set
\[
P=a_0^{r_0}a_1^{r_1}\cdots a_{q-1}^{r_{q-1}},\qquad W=P^k,\qquad p=|P|=\sum_{j=0}^{q-1}r_j.
\]
A set \(\Gamma\) of positions is a *string attractor* when every nonempty contiguous factor of \(W\) has at least one occurrence whose position interval intersects \(\Gamma\). Denote the smallest cardinality by \(\gamma^*(W)\).

**Cyclic bigram theorem.** We have \(\gamma^*(W)=q\). A position set of size \(q\) is a string attractor if and only if it selects exactly one position of each letter and meets an occurrence of every factor
\[
E_j=a_ja_{j+1}\quad(0\le j\le q-2),\qquad E_{q-1}=a_{q-1}a_0.
\]
In particular, single letters and these cyclic bigrams form a complete, constant-factor-length certificate for optimal attractors, regardless of the number or lengths of the runs.

**Exact enumeration.** Let \(S\) range over subsets of \(\{0,\ldots,q-1\}\), use indices modulo \(q\), and define
\[
\begin{aligned}
m_j&=\begin{cases}k,&0\le j<q-1,\\ k-1,&j=q-1,\end{cases}\\
c_j&=\begin{cases}k-1,&r_j=1\text{ and }j\in\{0,q-1\},\\ k,&r_j=1\text{ and }1\le j\le q-2,\\0,&r_j\ge2,\end{cases}\\
A_j(S)&=kr_j-m_{j-1}\mathbf1_{j-1\in S}-m_j\mathbf1_{j\in S}
+c_j\mathbf1_{j-1\in S}\mathbf1_{j\in S}.
\end{aligned}
\]
The number of *all labeled position sets* of minimum size is exactly
\[
\boxed{N_q(\boldsymbol r,k)=\sum_{S\subseteq\{0,\ldots,q-1\}}(-1)^{|S|}\prod_{j=0}^{q-1} A_j(S).}
\]
This sum has \(2^q\) terms, independent of the run lengths and the number of repeated periods.

If every \(r_j\ge2\), the optimal sets are exactly the two following types:

1. Choose the last position of a run of every letter, with the chosen final-letter run not occurring in the last period.
2. Choose the first position of a run of every letter, with the chosen initial-letter run not occurring in the first period.

All other selected run copies are arbitrary. The two types are disjoint and therefore
\[
\boxed{N_q(\boldsymbol r,k)=2k^{q-1}(k-1)\quad\text{if all }r_j\ge2.}
\]
When every \(r_j=1\), only one boundary obstruction remains, and
\[
\boxed{N_q(\boldsymbol1,k)=k^q-k^{q-2}.}
\]

## Assumptions and scope

Positions are indexed from \(1\) to \(kp\). Alphabet symbols are pairwise distinct across the \(q\) runs of one period and appear in the fixed cyclic order. Run lengths and the number of periods are arbitrary positive integers subject to \(q\ge3\) and \(k\ge2\). The enumeration concerns all position sets of minimum cardinality, not inclusion-minimal supersets or cyclic equivalence classes. The word is a linear, not circular, word: the last copy has no transition back to a next copy.

## Proof

**1. Sharp cardinality bound.** Every attractor must meet an occurrence of each of the \(q\) one-letter factors; a single position cannot satisfy two different letters, so \(\gamma^*(W)\ge q\). Select the last position of each of the \(q\) runs in the first period. This set meets every one-letter factor and every transition bigram, including the final-to-initial transition at the boundary between the first and second periods. The sufficiency argument below shows it is an attractor, so equality holds.

**2. Why a short-factor certificate is sufficient.** Suppose \(\Gamma\) has exactly one position of each letter and meets every cyclic transition \(E_j\). Consider an arbitrary nonempty factor \(F\) of length \(L\).

If \(L\le p\) and \(F\) is contained in a constant-letter run, write \(F=a_j^L\). In *any* run of letter \(a_j\) (all such runs have length \(r_j\ge L\)), the union of occurrences of \(a_j^L\) covers every position of that run. Hence the selected \(a_j\) position is crossed.

If \(L\le p\) and \(F\) contains the period-boundary transition \(a_{q-1}a_0\), its fixed relative offset around that transition fits at *every* internal period boundary: the part of \(F\) on either side has length at most \(p-1\). The chosen position witnessing \(E_{q-1}\) is an endpoint of one such boundary and belongs to an occurrence of \(F\) aligned around that boundary.

Otherwise \(L\le p\) and \(F\) spans at least one transition \(E_j\) with \(j<q-1\), but no period boundary. Thus \(F\) is contained in a period copy of \(P\). Its occurrence in every full copy of \(P\) contains the transition of type \(E_j\) in that copy. One endpoint of the selected occurrence of \(E_j\) is chosen by \(\Gamma\), so a copy of \(F\) crosses \(\Gamma\).

For \(L>p\), take any occurrence of \(F\) and all its translations by multiples of \(p\) that remain inside \(W\). The earliest such occurrence begins at a position at most \(p\), and the last one ends at a position at least \((k-1)p+1\). Consecutive occurrence intervals overlap because \(L>p\); their union therefore covers every position of
\[
[p,(k-1)p+1].
\]
Every endpoint of any internal period-boundary factor \(a_{q-1}a_0\) lies in this interval. The chosen endpoint witnessing \(E_{q-1}\) is therefore crossed by an occurrence of \(F\). This proves sufficiency for all factors, including ones longer than a period. Necessity follows directly from the attractor definition and the one-letter lower bound.

**3. Exact counting by forbidden transitions.** Once one position has been chosen per letter, the only remaining requirements are that the \(q\) directed transition factors be hit. There are \(m_j=k\) occurrences of \(E_j\) for \(j<q-1\), and \(m_{q-1}=k-1\) of the last-to-first transition. Fix a subset \(S\) of transitions whose occurrences must *not* be hit. The selected position of letter \(a_j\) then must avoid the outgoing endpoints of the \(m_j\) occurrences of \(E_j\), and the incoming endpoints of the \(m_{j-1}\) occurrences of \(E_{j-1}\). These two prohibited sets of positions overlap precisely when \(r_j=1\): the overlap size is \(k\) for an interior run type and \(k-1\) for the first or last run type, owing to the missing terminal boundary. Hence there are exactly \(A_j(S)\) legal choices of letter \(a_j\). Different letters have disjoint position sets, so multiplying over \(j\) and applying inclusion–exclusion over missing transitions proves the stated formula.

**4. Structural regimes.** Suppose all run lengths are at least two. Any position chosen for a letter can witness at most one of its two incident cyclic transitions: the incoming one only at a run's first position, and the outgoing one only at its last position. Since all \(q\) cyclic transitions must be hit by precisely \(q\) chosen positions, each position must witness exactly one transition. On a cyclic graph, choosing one endpoint of every edge with each vertex used once has exactly two orientations: all outgoing or all incoming. The single terminal edge has only \(k-1\) occurrences, giving \(k^{q-1}(k-1)\) choices for each orientation. If all run lengths are one, every internal transition is hit automatically by the position of either of its incident letters; the final-to-initial transition alone can fail. Its failure occurs exactly when the selected \(a_0\) lies in the first period and the selected \(a_{q-1}\) in the last period, with \(k^{q-2}\) choices for the other letters. Subtracting this from \(k^q\) completes the proof.

## Verification

The standalone program `verify.py` independently forms all literal contiguous factors and unions the position intervals of their actual occurrences. It enumerates every candidate with exactly one selected position per letter, tests full factor coverage against the short-factor criterion, and separately evaluates the inclusion–exclusion sum. All combinations included in the test loop are checked; the finite test is not substituted for the proof.

Running `python verify.py` yielded:

```text
VERIFY_OK families=307 candidate_sets=125015 distinct_factor_profiles=29362 literal_vs_local_and_IE=TRUE all_long_runs=TRUE all_singletons=TRUE
```

The checked families include alphabet sizes from \(2\) through \(5\), positive run lengths at most \(3\) for smaller alphabets (at most \(2\) for the largest), and two through four periods subject to a length cap. The binary instances in the verifier are boundary consistency tests, not part of the new theorem's scope.

## Relationship to prior work

The structural problem is motivated by the search for *all* smallest string attractors, rather than just their minimum size. Dvořáková and Hendrychová classify minimum attractors for pseudopalindromic prefixes of Rote sequences, a distinct binary aperiodic setting. Mantaci, Restivo, Romana, Rosone and Sciortino establish general inequalities for attractors under word powers, including \(\gamma^*(u)\le\gamma^*(u^k)\le\gamma^*(u)+1\), but these inequalities do not imply a complete classification of optimal positions or the exact counting polynomial for the present distinct-run cycles. Restivo, Romana and Sciortino examine infinite-word attractor profiles rather than optimal-set counts for this finite family.

The presently assessed contribution is the equivalence between universal factor coverage and the cyclic bigram certificate **for every alphabet size \(q\ge3\)**, followed by the all-run-length enumeration and the run-length-independent rigid regime. General attractor definitions, alphabet-size lower bounds, and prior binary cases are not claimed as new.

## Limitations

This theorem concerns integer powers of periods containing exactly one run of each distinct symbol; it does not classify optimal attractors of arbitrary periodic words, general alphabets with repeated nonadjacent symbols inside a period, or arbitrary position sets larger than the minimum. The exhaustive program checks finite instances only. An equivalent result outside the inspected literature remains an originality risk; there is no independent scientific audit.

## References

1. L. Dvořáková and V. Hendrychová, *String attractors of Rote sequences*, arXiv:2308.00850, first public version 1 August 2023; Discrete Mathematics & Theoretical Computer Science 26:3 (2024). https://arxiv.org/abs/2308.00850
2. S. Mantaci, A. Restivo, G. Romana, G. Rosone and M. Sciortino, *String Attractors and Combinatorics on Words*, arXiv:1907.04660, 10 July 2019; related journal article *A combinatorial view on string attractors*, Theoretical Computer Science 850 (2021), 236–248. https://arxiv.org/abs/1907.04660
3. A. Restivo, G. Romana and M. Sciortino, *String Attractors and Infinite Words*, arXiv:2206.00376, 1 June 2022. https://arxiv.org/abs/2206.00376
