# The first-excess global secure-set spectrum of sunlet graphs

## Finding

Let \(H_n=C_n\circ K_1\) be the sunlet on \(2n\) vertices, where \(n\ge3\). A **global secure set** is a dominating set \(S\) satisfying
\[
 |N_{H_n}[X]\cap S|\ge |N_{H_n}[X]\setminus S|
 \quad\text{for every nonempty }X\subseteq S.
\]
The global security number is \(n\). There are exactly two global secure sets of size \(n\): all cycle vertices and all pendant vertices. **The main result** is a complete classification of the next layer: exactly
\[
 \boxed{n(3n-5)}
\]
global secure sets have size \(n+1\).

More precisely, give each attached cycle-vertex/leaf pair one of the states \(A\) (both vertices selected), \(B\) (cycle vertex selected, leaf omitted), or \(C\) (leaf selected, cycle vertex omitted). Every global secure set of size \(n+1\) has a unique \(A\), and, reading cyclically from just after that position, its remaining \(n-1\) states form exactly one of the words
\[
 B^pC^q,\qquad C^pB^q
 \quad(p,q\ge0,\ p+q=n-1),
\]
or
\[
 B^pCB^q\qquad(p,q\ge1,\ p+q=n-2).
\]
Uniform words are counted once. Thus, for a fixed position of \(A\), there are \(2n-2\) distinct two-run words and \(n-3\) three-run words, giving \(3n-5\) configurations. All statements count **vertex subsets** of the labelled graph, not orbits modulo rotation.

## Assumptions and scope

All graphs are finite, simple, and undirected. The core vertices of \(H_n\) are \(c_i\) with indices in \(\mathbb Z/n\mathbb Z\), and each \(c_i\) has exactly one private leaf \(\ell_i\). The core edges are \(c_ic_{i+1}\). In a graph, \(N[X]\) denotes the union of the closed neighborhoods of the vertices of \(X\). The notion of **security** here is the all-subsets neighborhood inequality above; it is **not** the different one-guard swap version of secure domination.

Every dominating set selects at least one of \(c_i,\ell_i\) for every \(i\), because \(\ell_i\) can only be dominated by those two vertices. Consequently the size-\(n\) and size-\(n+1\) layers have, respectively, zero and exactly one pair of state \(A\), and all other pairs have state \(B\) or \(C\).

## Proof

**1. Reduction of exponentially many inequalities to core sets.** Fix a vertex selection encoded by states in \(\{A,B,C\}\), so every pair is represented. Define its security surplus at \(X\subseteq S\) by
\[
 d(X)=|N[X]\cap S|-|N[X]\setminus S|.
\]
Adjoining a selected leaf to an attack set cannot decrease the surplus: a selected leaf adds itself (a \(+1\) contribution), and can add only its supporting core vertex (a contribution \(+1\) or \(-1\)). Hence deleting selected leaves from an attack set cannot increase its surplus. In addition, when an attack set contains *only* selected leaves, every leaf brings a distinct selected leaf and at most its one unselected supporting core, hence its surplus is nonnegative. Therefore it suffices to check \(d(U)\ge0\) for all sets \(U\) of selected **core** vertices, including the empty set.

Let \(I\subseteq\mathbb Z/n\mathbb Z\) be the indices of the cores in \(U\), let \(N_C[I]\) denote its closed neighborhood in the underlying cycle, and write \(\sigma_i=1\) for state \(A\) or \(B\) and \(\sigma_i=-1\) for state \(C\). For at most one state \(A\), at position \(r\) if present, direct accounting of core and leaf contributions gives the exact identity
\[
 \boxed{d(U)=2\mathbf1_{\{r\in I\}}
       +\sum_{i\in N_C[I]\setminus I}\sigma_i.}\tag{1}
\]
Indeed, each selected \(B\)-core in \(U\) contributes its selected core and unselected leaf, which cancel; an \(A\)-core in \(U\) contributes two selected vertices; every external core reached from \(U\) contributes its own state sign, without reaching its private leaf. If there is no \(A\), omit the first term. Identity (1) is also valid for \(I=\varnothing\), giving zero.

**2. Minimum configurations.** The domination lower bound gives \(|S|\ge n\). At equality there is no \(A\). If the cycle word uses both \(B\) and \(C\), choose \(U\) to be the set of **all** selected \(B\)-cores. Then \(N_C[I]\setminus I\) consists solely of \(C\)-positions and contains at least one position (a \(B\)-\(C\) boundary). By (1), \(d(U)<0\). The two uniform words pass (1) trivially: the all-\(B\) word has only positive external signs, while the all-\(C\) word has no selected cores. The reduction also checks attacks containing leaves. Thus the global security number is \(n\), with exactly the two stated minimizers. The numerical minimum agrees with earlier general leaf-corona results; its value is background, not the novelty claim.

**3. Necessity for the first-excess layer.** Now \(S\) has size \(n+1\), so there is a unique \(A\). Rotate the indexing so that the state \(A\) is at index zero, and read the remaining \(n-1\) states as an ordinary linear word \(w\).

If a maximal \(B\)-run of \(w\) is bordered by \(C\) on **both** sides, let \(U\) consist of all cores in that run. These cores are disjoint from the root \(A\), and their only external neighbors are the two distinct bordering \(C\)-cores. Thus (1) gives \(d(U)=-2\), a contradiction. Therefore every \(B\)-run meets an endpoint of \(w\). This implies that \(w\) is either a word with one \(B\)-run, of the form \(B^pC^q\) or \(C^pB^q\), or has two endpoint \(B\)-runs, of the form \(B^pC^rB^q\) with \(p,q,r\ge1\).

In the latter case, if \(r\ge2\), choose \(U\) to be **all** \(B\)-cores. The external reached core positions are the root \(A\) and the two distinct \(C\)-cores bordering the interior \(C\)-run. The surplus is then \(+1-1-1=-1\) by (1), again impossible. Hence \(r=1\). This proves that every admissible word belongs to the claimed list.

**4. Sufficiency for every listed word.** In each listed word, the \(C\)-positions form a single contiguous block in the tail; when a \(C\)-block is surrounded by two \(B\)-runs it has length **one**.

Take any set \(I\) of selected core indices. If the root \(A\) belongs to \(I\), the first term of (1) is \(+2\). At most two positions from one terminal \(C\)-block, and at most one position from a singleton interior \(C\)-block, can belong to \(N_C[I]\setminus I\). Every remaining external contribution is positive, so \(d(U)\ge 2-2=0\).

If the root does **not** belong to \(I\), then \(I\) consists of \(B\)-positions. At most one \(C\)-position can be adjacent to \(I\): in the monotone words only one \(B\)-\(C\) boundary exists, and in the three-run words the entire \(C\)-block is one vertex. If no \(C\) is reached, all terms in (1) are nonnegative. Otherwise, select a \(B\)-core of \(I\) adjacent to that \(C\)-position. Moving from this vertex in the direction *away from* that \(C\) and toward the root \(A\), there is a consecutive chain of \(B\)-positions terminating at \(A\). Follow the chain until meeting the first position outside \(I\). This position is either an unselected \(B\)-core or the root \(A\); it lies in \(N_C[I]\setminus I\) and has sign \(+1\). It offsets the unique possible negative \(C\) contribution, giving \(d(U)\ge0\). This argument holds at \(n=3\) as well, where the closing cycle edge is just the edge to the root.

By the reduction in Step 1, every listed word is a global secure set.

**5. Counting.** Let \(L=n-1\). There are \(L+1=n\) words \(B^pC^{L-p}\) and another \(n\) words \(C^pB^{L-p}\). The two uniform words appear in both lists, so their union has \(2n-2\) words. The words \(B^pCB^q\), with \(p,q\ge1\) and \(p+q=n-2\), number \(n-3\); they are disjoint from the first group. The root position \(A\) is unique, so choices of its \(n\) labelled positions cannot give duplicates. The final answer is \(n[(2n-2)+(n-3)]=n(3n-5)\), as claimed. Every boundary case \(n\ge3\) is included by these formulas.

## Verification

Run the standard-library script `python verify.py` in this package. It builds the original \(2n\)-vertex graph and directly checks **all** nonempty attack sets for **all** dominated pair-state configurations of sizes \(n\) and \(n+1\), for each \(3\le n\le8\). It independently checks the core-charge identity and checks the reduced criterion through \(n=11\). The exact reproducible output includes `VERIFY_OK`. These finite experiments corroborate but do not substitute for Steps 1–5, which prove the claim for all \(n\ge3\).

## Relationship to prior work

The all-subsets security definition is due to Brigham, Dutton, and Hedetniemi. Zeng, Xue, Zeng, and Wang (2026) apply precisely this notion to odd-order Sierpiński graphs and motivate asking for structural sharpness beyond minimum values. Jesse-Józefczyk (2014, Chapter 3, Proposition 3.1) proves the global security minimum \(n\) for every connected one-leaf corona, but does **not** enumerate the next-to-minimal layer of sunlets. Menon and Chithra (2022/2023, Section 5) give secure-domination bounds for general corona operations, not the present \(n+1\) classification. Other literature sometimes uses *secure domination* for a different exchange-of-one-guard condition; those formulations must not be identified. The new mathematical statement is the complete cyclic-word classification and \(n(3n-5)\) first-excess enumerator, not the known minimum \(n\).

## Limitations

The result is for the one-leaf corona of a simple cycle, \(n\ge3\), and counts the minimum and first-excess layers only. It does not give the full security polynomial, classify higher-excess layers, or solve arbitrary one-leaf coronas. Priority outside the inspected primary literature is not certified, and no independent mathematical audit has been performed.

## References

1. Qingcheng Zeng, Yumei Xue, Cheng Zeng, and Dehui Wang, *Secure Domination in Odd-order Sierpiński Graphs*, arXiv:2610.28222 (first posted 2026-10-20), https://arxiv.org/abs/2610.28222 .
2. Katarzyna Jesse-Józefczyk, *Secure Sets in Graphs*, doctoral thesis, Adam Mickiewicz University (2014), Chapter 3, Proposition 3.1, https://repozytorium.amu.edu.pl/server/api/core/bitstreams/b7479010-1a60-4396-aca8-2b6621919f7b/content .
3. Manju K. Menon and M. R. Chithra, *Secure domination of some graph operators*, Indian Journal of Pure and Applied Mathematics 54 (2023), 1170–1176, DOI:10.1007/s13226-022-00331-9 .
4. R. C. Brigham, R. D. Dutton, and S. T. Hedetniemi, *Security in graphs*, Discrete Applied Mathematics 155 (2007), 1708–1714, DOI:10.1016/j.dam.2007.03.009 .
5. Y. Y. Ho and R. D. Dutton, *Global secure sets of grid-like graphs*, Discrete Applied Mathematics 159 (2011), 490–496, DOI:10.1016/j.dam.2010.12.013 (bibliographic and abstract comparison only; full text not accessible).
