# Loopless ternary cyclic digram profiles: exact capacity and complete singleton classification

## Finding

Consider nonempty cyclic words on the labeled alphabet \(\{0,1,2\}\), with no equal cyclic neighbors, and identify words up to rotation but **not** reversal or relabeling. For a word \(w\) of length \(n\), its *directed digram profile* is the six-tuple \(M(w)=(N_{01},N_{10},N_{12},N_{21},N_{20},N_{02})\), where \(N_{ij}\) counts all cyclic occurrences of the ordered adjacent pair \(ij\), with multiplicity. Thus \(N_{00}=N_{11}=N_{22}=0\). Let \(C_n\) denote the number of realizable profiles at length \(n\), and \(U_n\) the number of profiles having **exactly one** realizing necklace.

**Theorem.** The ordinary generating functions, valid as formal power series, are
\[
\sum_{n\ge1}C_nz^n=\frac{1+z^3}{(1-z^3)(1-z^2)^3}-1
\]
and
\[
\sum_{n\ge1}U_nz^n=\frac{3z^2+6z^4+6z^5}{1-z^2}+\frac{2z^3+6z^5}{1-z^3}-3z^4-6z^5.
\]
For \(n\ge6\), \(U_n\) depends only on \(n\bmod6\), with values
\[
\begin{array}{c|rrrrrr}n\bmod6&0&1&2&3&4&5\\\hline U_n&11&6&15&8&9&12\end{array}.
\]
The initial values are \(U_1=0\), \(U_2=3\), \(U_3=2\), \(U_4=6\), and \(U_5=6\). In particular, \(C_n=n^3/72+O(n^2)\), the exact eventual quasipolynomial periods of \(C_n\) and \(U_n\) are both \(6\), and \(U_n/C_n=O(n^{-3})\). The maximum size of a zero-error code for this observation model (one representative per profile) is exactly \(C_n\).

The following stronger **individual-profile classification** holds. Every nonzero realizable profile has a *unique* description of one of two forms:

1. **Zero circulation:** \(N_{01}=N_{10}=x\), \(N_{12}=N_{21}=y\), \(N_{20}=N_{02}=z\), with \(x,y,z\ge0\) and \(x+y+z\ge1\). It is uniquely reconstructible precisely when either exactly one of \(x,y,z\) is positive, or exactly two are positive and their minimum is \(1\).
2. **Nonzero circulation:** after choosing one of the two cyclic orientations, the six directed counts are \((x+t,x,y+t,y,z+t,z)\), with \(t\ge1\) and \(x,y,z\ge0\), in the orientation \(0\to1\to2\to0\); or its edge-reversed version. This profile is uniquely reconstructible precisely when \(x=y=z=0\), or exactly one of \(x,y,z\) is positive and either its value or \(t\) equals \(1\).

These two cases give a decision rule, an exact count of all profiles, and an exact count of uniquely reconstructible profiles at every length.

## Assumptions and scope

The alphabet symbols and directed adjacency are labeled and ordered. A necklace is an orbit under rotation only: reflection is not identified. The observation includes **all** cyclic directed length-two factors and their multiplicities, with no missing or corrupted reads. The constraint forbids each of \(00,11,22\), including across the cyclic boundary. Length \(n=1\) is impossible under this constraint. No probabilistic source model or biological claim is assumed. An optimal zero-error code may choose any single realization from each profile.

## Proof

**1. Balanced-flow parametrization and realizability.** Set \(a=N_{01}-N_{10}\). Conservation of incoming and outgoing edges at each symbol implies
\[
N_{01}-N_{10}=N_{12}-N_{21}=N_{20}-N_{02}=a.
\]
If \(a=0\), take \(x=N_{01}\), \(y=N_{12}\), \(z=N_{20}\). If \(a=t>0\), take \(x=N_{10}\), \(y=N_{21}\), \(z=N_{02}\); if \(a=-t<0\), reverse all arcs. These choices are bijective and have total edge lengths \(n=2(x+y+z)\) and \(n=3t+2(x+y+z)\), respectively. Every such nonzero flow has connected non-isolated support: positive \(t\) supplies an oriented three-cycle, and when \(t=0\), each positive undirected pair supplies a two-cycle, and any two edges of the three-vertex triangle share a vertex. The standard Euler-circuit criterion for connected balanced directed multigraphs therefore produces a cyclic word with precisely these directed counts. Conversely, every cyclic word induces such a balanced flow. Hence the parametrization is exhaustive and has no spurious profiles.

**2. Counting all profiles.** The zero-circulation term is the generating function for nonnegative triples of total weight \(2\), excluding the all-zero triple:
\[
(1-z^2)^{-3}-1.
\]
For positive circulation, the two orientations each contribute \(\sum_{t\ge1}z^{3t}(1-z^2)^{-3}\). Summing proves the stated expression for \(\sum C_nz^n\). In particular, for \(n\ge1\) the exact coefficient is
\[
C_n=\mathbf1_{2\mid n}\binom{n/2+2}{2}
+2\sum_{\substack{t\ge1,\,3t\le n\\2\mid(n-3t)}}\binom{(n-3t)/2+2}{2},
\]
where the indicator term is zero when \(n\) is odd. (The formula is only used for \(n\ge1\), so the zero profile is excluded automatically.) Expansion at \(z=1\) gives a fourth-order pole with leading part \(1/(12(1-z)^4)\), yielding \(C_n=n^3/72+O(n^2)\).

**3. Two-switch observation.** If a cyclic directed word has an edge occurrence \(uv\) with \(u\ne v\), replacing that occurrence by the length-three walk \(u\to v\to u\to v\) adds one occurrence each of \(uv\) and \(vu\), without changing any non-alternating cyclic length-three count. Indeed, all old length-three windows remain present, and the only two newly introduced windows are \(uvu\) and \(vuv\). In particular the number of occurrences of \(012\) is unchanged. This operation permits increasing any selected reciprocal-pair parameter without destroying a difference in the \(012\) count between two realizations.

**4. Zero-circulation singleton classes.** With exactly one positive parameter, the necklace is the alternating two-letter cycle and is unique. With exactly two positive parameters, the support is a two-edge path on three labeled vertices. Every cyclic Euler tour consists of excursions along the two incident directed two-cycles from their common vertex. The necklaces therefore correspond bijectively to cyclic binary arrangements of \(x\) excursions of one kind and \(y\) of the other. There is only one such arrangement if the smaller parameter is \(1\); if both are at least \(2\), grouping the first kind together versus separating it yields two distinct cyclic arrangements (for instance, an arrangement with one versus two cyclic changes between kinds). With all three parameters positive, the two length-six base words \(010212\) and \(012102\) have identical directed digram profiles with each reciprocal-pair count equal to \(1\), but their \(012\) counts are \(0\) and \(1\). Apply the two-switch observation to add the remaining desired reciprocal pairs in both words. The resulting necklaces remain distinct. This proves exactly the zero-circulation cases stated.

**5. Nonzero-circulation singleton classes.** Fix positive circulation along \(0\to1\to2\to0\); relabeling and reversal handle the other orientation and choices of reciprocal edge. If there are no reciprocal pairs, the necklace is the repeated directed three-cycle. If there is exactly one positive reciprocal-pair parameter, assume it is \(x=p>0\) on \(01\), and the circulation is \(t>0\). In any realization, between successive occurrences of the symbol \(2\), one must traverse \(2\to0\), then make \(k\ge0\) repetitions of \(0\to1\to0\), then finish with \(0\to1\to2\). Thus the necklace corresponds exactly to a cyclic \(t\)-tuple \((k_1,\ldots,k_t)\) of nonnegative integers summing to \(p\). There is just one such cyclic tuple when \(t=1\) or \(p=1\). When both exceed \(1\), putting all \(p\) detours in one block versus distributing at least one detour to another block gives inequivalent necklaces.

If at least two reciprocal-pair parameters are positive, rotate the labels so that they include \(01\) and \(12\). For every \(t\ge1\), the words
\[
A_t=(012)^{t-1}0101212,
\qquad B_t=(012)^{t-1}0121012
\]
have equal directed digram profiles, with \(x=y=1\), \(z=0\), and circulation \(t\). Direct cyclic inspection gives \(N_{012}(A_t)=t\) and \(N_{012}(B_t)=t+1\); thus they are not rotations. Adding any remaining reciprocal pairs to both via the two-switch operation preserves this distinction. No such profile is uniquely reconstructible. Combining all cases completes the individual classification.

**6. Counting singleton profiles.** At zero circulation, the single-pair cases contribute \(3z^2/(1-z^2)\); the two-positive-pair cases contribute \(3(2z^4/(1-z^2)-z^4)\). At positive circulation, pure oriented triangles contribute \(2z^3/(1-z^3)\). Exactly one positive reciprocal pair contributes
\[
6\left(\frac{z^5}{1-z^2}+\frac{z^5}{1-z^3}-z^5\right),
\]
because we must have either \(t=1\) or the positive reciprocal count \(p=1\), subtracting their intersection once. Adding these disjoint classes gives the announced rational generating function. Coefficient extraction gives the six residue classes from \(n=6\) onward. The rational generating functions have poles at primitive third roots of unity and at \(-1\); therefore their quasipolynomial periods cannot be smaller than \(\operatorname{lcm}(2,3)=6\). The singleton count remains at most \(15\), whereas \(C_n\) grows cubically, proving the ambiguity-density statement.

## Verification

The standalone `verify.py` enumerates every labeled cyclic proper-coloring word through length \(16\), deduplicates by actual rotation, groups its six directed digram counts, and tests both the number of profiles and the singleton rule against direct fiber sizes. It additionally enumerates the balanced parameter tuples through length \(100\), comparing both formulas. This test checks \(131070\) indexed words, \(506\) observed profile classes, and \(127\) observed singleton classes over lengths \(2\) through \(16\). Expected output:

```text
VERIFY_OK cyclic_words_checked=131070 profile_classes_checked=506 singleton_classes_checked=127 lengths=2..16 flow_lengths=1..100
EXAMPLES [(2, 3, 3), (3, 2, 2), (4, 6, 6), (5, 6, 6), (6, 12, 11), (7, 12, 6), (8, 21, 15), (9, 22, 8), (10, 33, 9), (11, 36, 12), (12, 50, 11), (13, 54, 6), (14, 72, 15), (15, 78, 8), (16, 99, 9)]
```

Run `python3 verify.py` from the directory containing this document and the verifier. Finite enumeration corroborates the theorem, while the six proof steps above establish all lengths.

## Relationship to prior work

The balanced-transition-matrix viewpoint is classical: Jacquet, Knessl, and Szpankowski count unrestricted Markov types asymptotically, while Kiah, Puleo, and Milenkovic develop constrained de Bruijn-profile enumeration and Ehrhart asymptotics. The latter explicitly considers forbidden local substrings but does not state this **loopless ternary cyclic** exact finite generating function or classify all singleton necklace fibers. Yehezkeally, Bar-Lev, Marcovich, and Yaakobi investigate generalized substring reconstruction and code rates under longer, partially overlapping reads, without this fixed length-two constrained spectrum. Wei, Schwartz, and Ge investigate noisy substring reconstruction, again without this individual-profile theorem. Those general techniques motivate the setting and are not claimed as original. The present contribution is the explicit realizability/singleton structure and its all-length exact enumeration for this particular constraint.

## Limitations

The result concerns exactly three labeled symbols, cyclic directed reads of length two, and a prohibition on repeated adjacent symbols. No conclusion is claimed for larger alphabets, read lengths, missing/noisy reads, linear words, or necklace equivalence under reversal. The zero-error capacity here is a count of distinct deterministic observations, not an error-correcting rate for a noisy sequencing experiment. Equivalence with a differently presented prior specialized classification remains possible; the comparisons do not constitute a literature-completeness proof. The finite verifier cannot establish the infinite theorem on its own. Independent external validation has not been performed.

## References

1. P. Jacquet, C. Knessl, and W. Szpankowski, *Counting Markov Types*, DMTCS Proceedings AM (2010), DOI: 10.46298/dmtcs.2768. https://dmtcs.episciences.org/articles/2768
2. H. M. Kiah, G. J. Puleo, and O. Milenkovic, *Codes for DNA Sequence Profiles*, ISIT (2016); lawful author manuscript: https://personal.ntu.edu.sg/hmkiah/docs/papers/DNA_seq_profile_ISIT.pdf
3. Y. Yehezkeally, D. Bar-Lev, S. Marcovich, and E. Yaakobi, *Generalized Unique Reconstruction from Substrings*, first public arXiv version October 10, 2022, arXiv:2210.04471. https://arxiv.org/abs/2210.04471
4. H. Wei, M. Schwartz, and G. Ge, *Reconstruction from Noisy Substrings*, first public December 8, 2023, arXiv:2312.04790. https://arxiv.org/abs/2312.04790
