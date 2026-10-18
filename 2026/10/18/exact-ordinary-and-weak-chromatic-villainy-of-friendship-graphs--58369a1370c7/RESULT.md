# Exact ordinary and weak chromatic villainy of friendship graphs

## Finding

For every integer \(k\ge1\), write \(F_k=K_1\vee(kK_2)\) for the friendship graph of \(k\) edge-disjoint triangles with one common hub. The ordinary chromatic villainy and weak chromatic villainy (using three named colours) are exactly

\[
B(F_k)=\begin{cases}0,&k=1,\\ k+1,&k\ge2,\end{cases}
\qquad
B_{\mathrm w}(F_k)=\begin{cases}0,&k=1,\\k,&k=2,3,\\k+1,&k\ge4.\end{cases}
\]

More strongly, every admissible disturbed colouring has an **exact linear-time repair-distance formula**. For \(k\ge2\), label the twice-repeated colours \(A,B\) and the singleton colour \(C\). If \(w\) has multiplicities \((k,k,1)\), let \(t=w(v_*)\) be its hub colour and let \((a_i,b_i)\) be the colours on the \(i\)-th outer edge. For a possible target hub colour \(h\in\{A,B,C\}\), put

\[
\alpha_h(w)={\bf1}_{\{t=h\}}+\sum_{i=1}^k g_h(a_i,b_i),\qquad
 g_h(a,b)=\begin{cases}
 0,&a=b=h,\\
 2,&a\ne b\text{ and }a,b\ne h,\\
 1,&\text{otherwise}.
 \end{cases}
\]

Then the exact minimum number of changed vertices under count-preserving and unrestricted (weak) repair is, respectively,

\[
d_{\mathrm{ord}}(w)=2k+1-\alpha_C(w),\qquad
  d_{\mathrm w}(w)=2k+1-\max_{h\in\{A,B,C\}}\alpha_h(w).
\]

These distances count changed vertex labels between the disturbed source and the final proper colouring, not recolouring operations along an intermediate path.

## Assumptions and scope

All graphs are finite, simple and undirected. A proper colouring uses the minimum possible number \(\chi(F_k)=3\) of *named* colours. An admissible disturbance is any permutation of the colours of a proper three-colouring on the vertex set. The ordinary repair must preserve each named colour multiplicity; a weak repair may alter the multiplicities but must retain the same palette of three colours. Ordinary and weak villainy maximize these respective minimum Hamming distances over all admissible disturbances. The theorem includes the special case \(F_1=K_3\). No claims are made for generalized windmills with larger clique blades.

For \(k\ge2\), every proper three-colouring gives the hub one colour, and every outer edge has the other two colours, one of each. Consequently all proper three-colourings have multiplicity multiset \((k,k,1)\), and the singleton colour determines the hub under ordinary repair. This assertion fails to single out a colour when \(k=1\), which is why that case is separated.

## Proof

**Exact local repair formula.** Fix a target hub colour \(h\). Each of the \(k\) outer edges must use exactly the two other named colours. These decisions are independent between edges. For a disturbed edge with source colours \((a,b)\), the maximum possible number of retained colours is zero when \(a=b=h\); it is two when \(a,b\) are distinct and both different from \(h\); it is one in every other case. Together with the hub contribution \({\bf1}_{\{t=h\}}\), this proves that the maximum global number of retained colours is \(\alpha_h(w)\). Each target obtained in this way is proper. Varying \(h\) gives the weak formula. For \(k\ge2\), ordinary repair requires \(h=C\), and every resulting target then automatically has exactly \(k\) vertices of colour \(A\), \(k\) of colour \(B\), and one of colour \(C\). This proves the ordinary formula as well.

**Universal bound.** Every outer edge of a source with profile \((k,k,1)\) contains a colour other than \(C\), since only one vertex overall is coloured \(C\). Therefore \(g_C(a_i,b_i)\ge1\) for each edge, so \(\alpha_C(w)\ge k\). Hence \(d_{\mathrm{ord}}(w)\le k+1\), and \(d_{\mathrm w}(w)\le d_{\mathrm{ord}}(w)\le k+1\).

**Witnesses for ordinary repair and for all large weak repairs.** For even \(k\ge2\), choose hub colour \(A\) and let the outer-edge source pairs be one \((A,C)\), followed by \((k-2)/2\) copies of \((A,A)\) and \(k/2\) copies of \((B,B)\). This source has profile \((k,k,1)\). It satisfies

\[
\alpha_C=k,\qquad \alpha_A=2+k/2,\qquad \alpha_B=1+k/2.
\]

For odd \(k\ge3\), take hub colour \(A\), one \((B,C)\) edge, and \((k-1)/2\) copies each of \((A,A)\) and \((B,B)\). Then

\[
\alpha_C=k,\qquad \alpha_A=(k+5)/2,\qquad \alpha_B=(k+1)/2.
\]

In both cases \(d_{\mathrm{ord}}=k+1\). For even \(k\ge4\) and odd \(k\ge5\), each displayed agreement count is at most \(k\), while \(\alpha_C=k\). Hence these witnesses attain \(d_{\mathrm w}=k+1\). Together with the universal bound, this establishes both main formulas for \(k\ge4\) and the ordinary formula for \(k\ge2\).

**Small weak cases.** Suppose \(k\in\{2,3\}\) and the source hub is \(C\). The ordinary target with hub \(C\) retains that vertex and at least one colour on each outer edge. Therefore some weak target retains at least \(k+1\) vertices. If the source hub differs from \(C\), exchange the names \(A,B\) if needed to take hub \(A\).

For \(k=2\), if the source edge containing the unique \(C\) is \((A,C)\), the other edge is \((B,B)\); a target with hub \(A\) retains at least three vertices. If the \(C\)-edge is \((B,C)\), the other edge is \((A,B)\); a target with hub \(C\) retains three vertices. Thus every source has weak cost at most \(2\).

For \(k=3\), if the \(C\)-edge is \((A,C)\), the other edges must be \((A,B)\) and \((B,B)\); hub \(C\) retains four vertices. If the \(C\)-edge is \((B,C)\), the remaining edges are either \((A,B),(A,B)\), when hub \(C\) retains five vertices, or \((A,A),(B,B)\), when hub \(A\) retains four vertices. Thus every source has weak cost at most \(3\). The two explicit witnesses above attain weak costs \(2\) and \(3\) in these cases, respectively. Therefore the small weak values are sharp.

Finally, \(F_1=K_3\) is complete, so every permutation of the three distinct colours is already proper and both values equal zero. This proves every assertion.

## Verification

The accompanying standalone Python program `verify.py` uses exact integer arithmetic. It independently enumerates all \(3\cdot2^k\) properly coloured targets and all distinct source words of multiplicities \((k,k,1)\), checking the local agreement formula against direct Hamming distances for every \(1\le k\le6\). At \(k=1\) all three colour multiplicities are one, and the separate complete-graph rule is used. It also checks the construction witnesses for \(2\le k\le18\), including explicit proper-target enumeration through \(k=8\). The reported global values are \((B,B_{\mathrm w})=(0,0),(3,2),(4,3),(5,5),(6,6),(7,7)\) for \(k=1,2,3,4,5,6\), respectively. These finite checks corroborate but are not used to prove the all-\(k\) theorem.

To replay, place `verify.py` alongside this document and run `python verify.py` using Python 3 with only its standard library. It prints `ALL_TESTS_PASSED` on success. All proof steps above are elementary and independent of program output.

## Relationship to prior work

Chromatic villainy and its weak variant were introduced by Clark et al. [1], who determine values for connected bipartite graphs and discuss other graph classes, as does the later classification of villainy two [2]. The two October 2026 preprints [3,4] motivate profile-based repair and respectively treat odd cycles, complete multipartite graphs, extremal values at fixed order and chromatic number, and disjoint unions with general composition algorithms. Their stated results do not evaluate the connected, noncomplete-multipartite family \(K_1\vee(kK_2)\): its triangles share a hub, and removing the hub gives a matching, but taking a join is not the disjoint-union operation to which [4] applies.

The exact per-source formula here is a direct local maximization over target hub colours, while the global classification includes a sharp small-order transition between strict ordinary-versus-weak inequality and equality. This is not claimed to improve a general algorithm from [4]. The original 2018 thesis [5] concerns paths, cycles and complete multipartite graphs; its full text was unavailable for inspection, so the comparison to that thesis is only partial.

## Limitations

The new formula concerns friendship graphs, not all triangular cacti, arbitrary joins or general windmills. The result is an exact worst-case Hamming-distance statement, not a claim about the number of recolouring operations along proper intermediate colourings. The finite verification checks only the indicated sizes; the unrestricted parameter statement follows solely from the displayed proof. Literature searches found no covering theorem under the tested terminology, but this is not a proof of bibliographic uniqueness. The cited 2018 thesis could not be inspected in full, and unindexed equivalent treatments remain possible. Independent mathematical audit has not been performed.

## References

1. S. A. Clark, J. E. Holliday, S. Holliday, P. D. Johnson Jr., J. E. Trimm, R. R. Rubalcaba, and M. Walsh, *Chromatic Villainy in Graphs*, Congressus Numerantium **182** (2006), 171–182. Public author-hosted transcription: https://www.researchgate.net/publication/265812808_Chromatic_villainy_in_graphs
2. S. Jahanbekam and M.-R. Lin, *Characterization of Graphs with Villainy 2*, arXiv:2103.05816v1 (2021), https://arxiv.org/html/2103.05816v1
3. J. Jiang, Y. Jiang, Y. Li, L. Wang, and A. Zhang, *Exact and extremal values of chromatic villainy*, arXiv:2610.13580v1 (first public 9 October 2026), https://arxiv.org/html/2610.13580v1
4. J. Jiang, Y. Jiang, Y. Li, L. Wang, and A. Zhang, *Disjoint unions and fixed-parameter algorithms for chromatic villainy*, arXiv:2610.13556v1 (first public 9 October 2026), https://arxiv.org/html/2610.13556v1
5. A. Raleigh, *The Chromatic Villainy of Complete Multipartite Graphs*, M.S. thesis, Rochester Institute of Technology (2018), https://repository.rit.edu/theses/9889/
