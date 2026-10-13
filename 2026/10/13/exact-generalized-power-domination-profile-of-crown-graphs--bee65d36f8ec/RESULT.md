# Exact generalized power-domination profile of crown graphs
## Finding
Let \(n\ge 3\) and \(k\ge 1\). Write
\[
\operatorname{Cr}_n=K_{n,n}-\{a_i b_i:1\le i\le n\}
\]
with bipartition \(A=\{a_1,\ldots,a_n\}\) and \(B=\{b_1,\ldots,b_n\}\). For \(S\subseteq V(\operatorname{Cr}_n)\), set
\[
s_A=|S\cap A|,\qquad s_B=|S\cap B|,\qquad h=\max\{1,n-k-1\}.
\]
Under the standard \(k\)-power-domination process, \(S\) is \(k\)-power dominating if and only if
\[
(s_A\ge1\text{ and }s_B\ge1)\quad\text{or}\quad(s_B=0\text{ and }s_A\ge h)\quad\text{or}\quad(s_A=0\text{ and }s_B\ge h).
\]
Therefore the cardinality enumerator of all \(k\)-power-dominating sets is
\[
\mathcal P_k(\operatorname{Cr}_n;x)=\big((1+x)^n-1\big)^2+2\sum_{t=h}^n\binom nt x^t.
\]
In particular,
\[
\gamma_{P,k}(\operatorname{Cr}_n)=
\begin{cases}
1,&k\ge n-2,\\
2,&1\le k\le n-3.
\end{cases}
\]
The number of minimum \(k\)-power-dominating sets is \(2n\) when \(k\ge n-2\), is \(\binom{2n}{2}\) when \(k=n-3\), and is \(n^2\) when \(1\le k\le n-4\).

## Assumptions and scope
The graph is finite, simple, and \(n\ge3\). The propagation convention is the standard generalized power-domination rule: first observe \(N[S]\); then repeatedly, if an observed vertex has at most \(k\) unobserved neighbors, observe all of those neighbors. The empty set is not power dominating. No statement is made for alternative propagation conventions.

The earliest verified public source for this generalized parameter is the National Taiwan University preprint *Generalized power domination of graphs*, dated 10 July 2011. Power domination is classified under primary MSC \(05C69\) in the closely related SIAM treatment of generalized power domination.

## Proof
Suppose first that \(S\) meets both sides. After the initial domination step, an \(A\)-vertex \(a_i\) can remain unobserved only when the selected \(B\)-vertices consist solely of \(b_i\) and \(a_i\notin S\). Hence at most one vertex of \(A\) is unobserved. By symmetry, at most one vertex of \(B\) is unobserved. If anything remains unobserved, choose on the opposite side an observed vertex whose deleted matched nonedge is not the remaining vertex; such a vertex exists because \(n\ge3\). It then has exactly one unobserved neighbor, so the process finishes for every \(k\ge1\). Thus every mixed set is \(k\)-power dominating.

Now let \(S\subseteq A\) with \(t=|S|\). If \(t\ge2\), every vertex of \(B\) is observed in the domination step. Put \(r=n-t\), the number of unobserved \(A\)-vertices. If \(r=0\), the graph is already observed. If \(1\le r\le k+1\), choose an unobserved \(a_j\). The observed vertex \(b_j\) is nonadjacent to \(a_j\) and has exactly \(r-1\le k\) unobserved neighbors, so it observes all other unobserved \(A\)-vertices. One unobserved \(A\)-vertex remains, and an observed \(B\)-vertex with a different index observes it. Hence \(S\) succeeds.

If instead \(r\ge k+2\), then every observed \(b_j\) has at least \(r-1\ge k+1\) unobserved neighbors, while observed vertices of \(A\) have no unobserved neighbors on their own side and all their \(B\)-neighbors are already observed. No propagation can occur, so \(S\) fails.

For \(t=1\), say \(S=\{a_i\}\), the domination step observes \(a_i\) and all of \(B\setminus\{b_i\}\). Every observed \(b_j\) with \(j\ne i\) has exactly \(n-2\) unobserved neighbors. Thus the singleton succeeds exactly when \(k\ge n-2\); after the first such propagation, the remaining two vertices are observed by two further legal propagations. This is exactly the threshold \(t\ge\max\{1,n-k-1\}\). The case \(S\subseteq B\) is symmetric, proving the classification.

The enumerator follows by disjoint counting. Mixed sets contribute \(\big((1+x)^n-1\big)^2\). One-sided sets on either side have sizes \(t\ge h\), contributing \(2\sum_{t=h}^n\binom nt x^t\). The minimum-size statements and their multiplicities follow from the lowest nonzero coefficient: singletons are possible exactly when \(h=1\); when \(h=2\), every two-vertex set works; when \(h\ge3\), exactly the \(n^2\) mixed pairs are minimum.

## Verification
A standalone exhaustive checker independently simulates the generalized observation process and compares it with the theorem for every subset of \(\operatorname{Cr}_n\), for \(3\le n\le8\) and every \(1\le k\le n\). It tests \(669888\) subset/parameter instances, checks every coefficient of the stated enumerator, and checks the minimum value and number of minimizers in all \(33\) parameter pairs. It also verifies explicitly that \(\{a_1,b_2\}\) power dominates \(\operatorname{Cr}_5\) for \(k=1\). The computation is finite verification only; the proof above establishes the theorem for all stated parameters.

Reproduction: run `python verification.py`. The expected final line is recorded in `verification_output.txt`.

## Relationship to prior work
Chang, Dorbec, Montassier, and Raspaud introduced \(k\)-power domination as a common generalization of domination and ordinary power domination. Dorbec, Henning, Löwenstein, Montassier, and Raspaud later proved an upper bound for connected \(k+2\)-regular graphs; for the slice \(k=n-3\), that bound is consistent with the value \(2\) obtained here but does not classify the sets or give the full parameter profile.

Chandrasekaran and Sulthana's 2019 article *k-Power Domination of Crown Graph* uses the standard crown object \(K_{n,n}\) with the perfect matching removed. The publisher-indexed text states Theorem 1 as \(\gamma_{P,k}\ge n-k\) for \(n\ge k+2\), and its algorithm reports equality \(\gamma_{P,k}=n-k\). Under the standard generalized propagation rule used here, this is false. For example, \(S=\{a_1,b_2\}\) is a power-dominating set of \(\operatorname{Cr}_5\) for \(k=1\), so \(\gamma_{P,1}\le2\), whereas \(n-k=4\). The theorem above replaces that scalar assertion by an all-set classification and exact enumerator.

Brimkov, Patel, Suriyanarayana, and Teich introduced the power-domination polynomial as the enumerator of all ordinary power-dominating sets. Their searchable full text contains no crown-graph treatment; `crown` has no occurrence, and `complete bipartite` appears in preliminaries rather than a crown-family formula. A 2025 full-text survey/application paper on power-domination polynomials likewise contains no occurrence of `crown` or `complete bipartite` in its power-domination family list; its Section 3.2 treats complete, path, cycle, wheel, star, windmill, friendship, cone, fan, and related families.

## Limitations
The 2019 publisher PDF is protected by an interactive verification layer in direct retrieval. The scientific comparison above therefore relies on the publisher-indexed extraction, which exposes the crown definition, Theorem 1, its proof text, and the algorithm output, but not on a page-by-page local copy of the entire three-page article. The retained theorem does not require that article for correctness. The claim of contradiction is specifically relative to the standard generalized \(k\)-power-domination rule stated in the assumptions.

The exhaustive computation covers only \(3\le n\le8\) and \(1\le k\le n\); it is not used as an infinite proof. No independent audit has been performed.

## References
1. G. J. Chang, P. Dorbec, M. Montassier, and A. Raspaud, *Generalized power domination of graphs*, National Taiwan University preprint 2011-07, dated 10 July 2011; Discrete Applied Mathematics 160 (2012), 1691–1698. DOI: 10.1016/j.dam.2012.03.007.
2. P. Dorbec, M. A. Henning, C. Löwenstein, M. Montassier, and A. Raspaud, *Generalized Power Domination in Regular Graphs*, SIAM Journal on Discrete Mathematics 27(3) (2013), 1559–1574. DOI: 10.1137/120891356. Primary MSC: 05C69.
3. S. Chandrasekaran and A. Sulthana, *k-Power Domination of Crown Graph*, International Journal of Applied Engineering Research 14(13) (2019), 3066–3068. Publisher file: https://www.ripublication.com/ijaer19/ijaerv14n13_11.pdf.
4. B. Brimkov, R. Patel, V. Suriyanarayana, and A. Teich, *Power domination polynomials of graphs*, arXiv:1805.10984 (2018).
5. G. Kuriachan and A. Parthiban, *On Graph Entropy Measures Based on the Number of Dominating and Power Dominating Sets*, Malaysian Journal of Mathematical Sciences 19(1) (2025), 269–287. DOI: 10.47836/mjms.19.1.14.
