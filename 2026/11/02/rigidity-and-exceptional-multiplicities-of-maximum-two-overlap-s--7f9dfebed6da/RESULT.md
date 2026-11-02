# Rigidity and exceptional multiplicities of maximum two-overlap synchronization codes

## Finding
Let \(\Sigma\) be a *labeled* alphabet of cardinality \(q\ge2\). A code \(\mathcal C\subseteq\Sigma^n\) is \((1,2)\)-overlap-free if no suffix of length one or two of any codeword equals a prefix of the same length of any (possibly identical) codeword. We count distinct sets of codewords, without identifying symbol permutations or reversal.

**Theorem.** For every \(n\ge4\), the number \(N_q(n)\) of codes having maximum possible size is independent of \(n\), and equals
\[
N_q(n)=\begin{cases}
4,&q=2,\\
6,&q=3,\\
44,&q=4,\\
140,&q=5,\\
2\binom q{\lfloor(q+1)/3\rfloor},&q\ge6.
\end{cases}
\]
For \(q\ge6\), **every** maximum code has one of just two rectangular forms
\[
 A\,\Sigma^{n-3}B^2\quad\text{or}\quad B^2\Sigma^{n-3}A,
\]
where \(A\sqcup B=\Sigma\), \(|A|=\lfloor(q+1)/3\rfloor\), and \(B\) is its complement. For \(q=4,5\) further genuinely nonrectangular maximum codes exist, as parametrized below.

The known optimum cardinality \(q^{n-3}a(q-a)^2\), \(a=\lfloor(q+1)/3\rfloor\), is used only as context; we also derive the optimizer classification directly from elementary bounds.

## Assumptions and scope
An overlap is forbidden in both directions, including a word overlapping itself. The minimum blocklength is four so prefix and suffix two-letter blocks occupy disjoint positions. Alphabet symbols are labeled. All claims are for integer \(q\ge2\), \(n\ge4\). Let \(A,B\) be nonempty disjoint subsets whose union is \(\Sigma\). For \(T\subseteq A\times B\), define
\[
\mathcal C(A,B,T)=[(A\times A)\cup T]\,\Sigma^{n-4}\,[(B\times B)\cup((A\times B)\setminus T)].
\]
The bracketed objects are two-letter word sets, so juxtaposition means concatenation. Put \(a=|A|\), \(b=|B|=q-a\), and \(t=|T|\).

All maximum codes equal \(\mathcal C(A,B,T)\), and the complete admissible parameter list is
\[
\begin{array}{c|l}
q & (a,t)\\\hline
2&(1,0),(1,1)\\
3&(1,2),(2,0)\\
4&(1,3),(2,2),(3,0)\\
5&(2,5),(2,6),(3,0),(3,1)\\
q\ge6&(a_q,a_q(q-a_q)),(q-a_q,0),\quad a_q=\lfloor(q+1)/3\rfloor.
\end{array}
\]
Every permitted \(A\) and every permitted subset \(T\) produces a distinct optimal code. The nonrectangular cases are \((a,t)=(2,2)\) at \(q=4\) and \((2,5),(3,1)\) at \(q=5\).

## Proof
**1. Saturation of prefix–suffix pairs.** Given any nonempty overlap-free code \(\mathcal C\), let \(A\) be the alphabet symbols appearing in first position and \(B\) those in last position. The length-one rule forces \(A\cap B=\varnothing\); neither set is empty. Write \(P\subseteq\Sigma^2\) for observed two-letter prefixes and \(S\subseteq\Sigma^2\) for observed two-letter suffixes. The length-two rule is equivalent to \(P\cap S=\varnothing\). Thus every codeword is in \(P\Sigma^{n-4}S\); this whole product is itself overlap-free because the one-letter ends lie in disjoint \(A,B\) and \(P\cap S=\varnothing\). If \(\mathcal C\) has maximum cardinality, then it equals the whole product (otherwise a new word can be added).

If a letter \(z\) belonged to neither \(A\) nor \(B\), then \((z,z)\notin S\) because every suffix pair ends in \(B\), and \(z\notin B\). Adjoining the words \((z,z)\Sigma^{n-4}S\) would strictly enlarge the code without introducing an overlap, contradicting maximality. Therefore \(A\sqcup B=\Sigma\).

Every pair in \(A\times A\) may be adjoined to \(P\) without meeting \(S\), because suffix pairs end in \(B\). By maximality all such pairs are in \(P\); similarly \(B\times B\subseteq S\). The only eligible pairs for both sides are \(A\times B\), and each must appear in exactly one of \(P,S\), else adjoining it to either side strictly enlarges the code. Hence \(P=(A\times A)\cup T\) and \(S=(B\times B)\cup((A\times B)\setminus T)\) for a unique \(T\). Conversely every displayed triple defines an overlap-free code. Its cardinality is
\[
|\mathcal C(A,B,T)|=q^{n-4}(a^2+t)(b^2+ab-t).
\tag{1}
\]
Because its first-letter set is exactly \(A\) and last-letter set exactly \(B\), the triple \((A,B,T)\) is uniquely recoverable from the code: no double-counting is possible.

**2. Optimization and rigidity for \(q\ge6\).** Reversing all codewords exchanges \((a,t)\) with \((b,ab-t)\), so assume \(a\le b\). Set \(u=ab-t\). The unscaled objective in (1) is
\[
F_q(a,u)=(aq-u)(b^2+u)=aqb^2+u(aq-b^2)-u^2,
\quad 0\le u\le ab.
\tag{2}
\]
Let \(\rho=(3-\sqrt5)/2\). If \(a/q\le\rho\), then \(aq-b^2\le0\); thus \(F_q(a,u)\le aqb^2\), with equality only at \(u=0\). The cubic \(a(q-a)^2\), considered for integer \(a\in[1,q-1]\), has a **unique** maximizer \(a_q=\lfloor(q+1)/3\rfloor\): its real derivative has sign given by \(q-3a\), while comparison of the neighboring integer candidates gives differences \(k\) when \(q=3k+1\), and \(k+1\) when \(q=3k+2\). For \(q\ge6\), \(a_q/q\le\rho\), so the code with \(a=a_q,u=0\) exists and has the candidate objective \(M_q=q a_q(q-a_q)^2\).

If instead \(\rho<a/q\le1/2\), the unconstrained quadratic maximum from (2) gives
\[
F_q(a,u)\le\tfrac14(q^2-ab)^2=\tfrac{q^4}{4}(1-x+x^2)^2\le\rho^2q^4,
\quad x=a/q.
\tag{3}
\]
The last inequality follows because \(1-x+x^2\) decreases on \([\rho,1/2]\), and \(1-\rho+\rho^2=2\rho\). Writing \(a_q=q/3+\delta\), where \(|\delta|\le1/3\), yields the exact identity
\[
M_q=\frac4{27}q^4-q^2\delta^2+q\delta^3
\ge q^4\left(\frac4{27}-\frac1{9q^2}-\frac1{27q^3}\right).
\tag{4}
\]
For \(q\ge8\), the factor in parentheses is at least \(2023/13824\), and
\[
\frac{2023}{13824}>\frac{73}{500}>\rho^2=\frac{7-3\sqrt5}{2}.
\]
The right inequality follows from \(\sqrt5>559/250\). Thus the interior case (3) is strictly suboptimal for every \(q\ge8\). For \(q=6\), only \(a=3\) has \(aq-b^2>0\) in the reduced range; its quadratic reaches at most \(182<M_6=192\). For \(q=7\), only \(a=3\) does; its quadratic reaches at most \(342<M_7=350\). Therefore every maximum for \(q\ge6\) has \(a=a_q,u=0\) or its reversal, with no other possibilities.

**3. Exceptional small alphabets and enumeration.** Directly evaluating the finitely many integers \(1\le a\le q-1\), \(0\le t\le a(q-a)\) in (1) for \(q=2,3,4,5\) gives exactly the listed maximizing pairs; the corresponding optimal objectives are respectively \(2,12,36,90\). For fixed \((a,t)\), there are \(\binom qa\) choices of the labeled first-letter class \(A\), and independently \(\binom{a(q-a)}t\) choices of \(T\). Hence
\[
N_q(n)=\sum_{(a,t)\text{ optimizing}}\binom qa\binom{a(q-a)}t.
\tag{5}
\]
The totals are \(4,6,44,140\). For \(q\ge6\) the two optimizing patterns each contribute \(\binom q{a_q}\), giving the stated formula. No step depends on \(n\) beyond its being at least four. \(\square\)

## Verification
The standalone `verify_direct.cpp` independently enumerates every possible two-letter prefix set \(P\subseteq\Sigma^2\) for \(q=2,3,4,5\), computes the largest compatible suffix set, and counts optimal labeled codebooks **without assuming** the \((A,B,T)\) parameterization. It obtains maximum sizes \(2,12,36,90\) and extremizer counts \(4,6,44,140\). The separate `verify_parametric.py` enumerates all \((a,t)\) through \(q=35\), checks all optimizing pairs against the theorem and the independently described classification, and reproduces the counts. Both files use standard C++17 / Python 3 and need no data downloads. `verification_output.txt` records their actual outputs. Finite runs are corroboration; the proof above establishes the unbounded alphabet and blocklength ranges.

## Relationship to prior work
Cai, Wang, and Feng proved the **maximum size** of \((1,2)\)-overlap-free codes, not an explicit all-alphabet enumeration of every optimum; the size formula is reproduced in Stanovnik's later article. Stanovnik's 2024 preprint characterizes **inclusion-maximal** restricted-overlap codes generally, but that does not directly give this optimizer rigidity, the exact counts, or the two exceptional alphabet sizes. Yang and Ding's 2025-publicized, 2026-volume article develops overlap-free constructions, non-expandability, and generating functions, but not the theorem here. The 2024 paper on maximum *non-overlapping* codes concerns all overlap lengths \(1,\ldots,n-1\), not just lengths one and two. A mathematical-research database record on length-five non-overlapping codes similarly does not cover this distinct restriction.

## Limitations
The optimum-cardinality formula predates this result and is not presented as original. The new contributions are classification, rigidity threshold, exceptional cases, and complete count of labeled extremizers. We do not classify suboptimal or merely inclusion-maximal codes. The theorem is restricted to forbidden overlap lengths one and two with blocklength at least four; no inference for full non-overlapping codes or longer forbidden overlaps is made. Priority against all possible unindexed treatments, including derivations implicit in the 2023 size proof, has not been independently established.

## References
1. Q. Cai, X. Wang, T. Feng, “Constructions and Bounds for q-Ary (1,k)-Overlap-Free Codes,” *IEEE Transactions on Information Theory* 70 (2024), 4439–4444, doi:10.1109/TIT.2023.3319010 (first public 2023).
2. L. Stanovnik, “Codes with restricted overlaps: expandability, constructions, and bounds,” arXiv:2411.02899 (first public 2024-11-05), doi:10.1007/s12190-025-02441-z. Full article: https://link.springer.com/article/10.1007/s12190-025-02441-z.
3. H. Yang, Y. Ding, “Q-Ary (t1,t2)-Overlap-Free Codes,” *IEICE Transactions on Fundamentals* E109-A (2026), 757–762, first public online 2025-09-22, doi:10.1587/transfun.2025EAL2050. https://globals.ieice.org/en_transactions/fundamentals/10.1587/transfun.2025EAL2050/_f.
4. L. Stanovnik, M. Moškon, M. Mraz, “In search of maximum non-overlapping codes,” *Designs, Codes and Cryptography* 92 (2024), 1299–1326, doi:10.1007/s10623-023-01344-z.
