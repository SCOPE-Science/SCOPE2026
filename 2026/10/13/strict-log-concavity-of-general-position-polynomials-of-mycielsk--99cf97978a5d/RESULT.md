# Strict log-concavity of general-position polynomials of Mycielskian complete graphs

## Finding
Let \(M_n=\mathcal M(K_n)\) be the standard Mycielskian of the complete graph on \(n\ge2\) vertices. Its general-position polynomial \(\Psi_n(z)=\sum_{S\text{ in general position}}z^{|S|}\), including the empty set, is
\[
\boxed{\Psi_n(z)=(2+z)(1+z)^n-1+nz\bigl((1+z)^{n-1}-1\bigr)+2nz^2+n^2z^3.}
\]
Writing \(\Psi_n(z)=\sum_{k=0}^{n+1}a_{n,k}z^k\), **every coefficient is positive and the finite sequence is strictly log-concave**:
\[
 a_{n,k}^{\,2}>a_{n,k-1}a_{n,k+1}\quad(1\le k\le n).
\]
In particular the coefficients are unimodal. The earlier determination of the general-position number \(n+1\), including its unique maximizing set for \(n\ge3\), is not a new result here; the contribution is the full cardinality enumerator and its strict log-concavity.

## Assumptions and scope
All graphs are finite, simple and undirected. The original vertices of \(M_n\) are \(v_1,\ldots,v_n\), the twin vertices are \(v'_1,\ldots,v'_n\), and the root is \(w\). All originals are pairwise adjacent, the twins form an independent set, \(v_i\sim v'_j\) precisely for \(i\ne j\), and \(w\) is adjacent precisely to the twins. A vertex set is in general position when no three of its elements occur on a common shortest path. The theorem covers all integers \(n\ge2\), with no asymptotic assumptions; no assertion is made for \(n=1\).

## Proof
**1. Geodesics and induced clusters.** For \(n\ge2\), every two distinct vertices of \(M_n\) have distance one or two. Indeed, different originals are adjacent; an original and its own twin have a two-edge path through another original; an original and another twin are adjacent; two twins share neighbor \(w\); and an original reaches \(w\) through a twin of another index. Since \(M_n\) has diameter two, a selected triple lies on a shortest path exactly when it induces a three-vertex path with nonadjacent ends. Thus a set is in general position if and only if its induced subgraph is a disjoint union of complete graphs (a cluster graph). This is a special case of the classical characterization of graph general-position sets, but it also follows immediately from the preceding distance-two argument.

**2. Classification and enumeration.** For a chosen set \(S\), let \(A\subseteq[n]\) index the selected originals, and \(B\subseteq[n]\) the selected twins. First suppose \(w\notin S\). If \(A=\varnothing\), then \(B\) is unrestricted. If \(A=\{i\}\), at most one selected twin may have an index other than \(i\), while twin \(i\) may be chosen independently. If \(|A|\ge2\), no twin whose index belongs to \(A\) is allowed (it would make a three-vertex induced path with two originals), and at most one twin with index outside \(A\) is allowed (two such twins and an original form an induced path). Conversely, each of these configurations induces disjoint cliques. The generating polynomial for these sets is therefore
\[
(1+z)^n+nz(1+z)(1+(n-1)z)
+\sum_{a=2}^{n}\binom na z^a(1+(n-a)z).
\]
Now suppose \(w\in S\). Because \(w\) is adjacent to every twin, at most one twin may be selected. With no twin, any subset of originals is allowed. With twin \(i\), any selected original must have index \(i\), since \(v_j,v'_i,w\) induces a path for \(j\ne i\). These and only these possibilities yield
\[
z(1+z)^n+nz^2(1+z).
\]
Adding the two cases and using \((n-a)\binom na=n\binom{n-1}a\) gives the boxed polynomial.

**3. Coefficients.** Direct coefficient extraction gives
\[
 a_{n,0}=1,\qquad a_{n,1}=2n+1,\qquad
 a_{n,2}=n(2n+1),\qquad
 a_{n,3}=\frac{n(5n^2-6n+7)}6.
\]
For \(4\le k\le n+1\), there is a more useful expression
\[
 a_{n,k}=\binom{n+1}{k}w_{n,k},\qquad
 w_{n,k}=2+\frac{k(n-k)}{n+1}.
\]
This includes the terminal value \(a_{n,n+1}=1\). All these values are positive, since \(w_{n,k}\ge1\) on \(0\le k\le n+1\). We use the usual convention that coefficients outside \(0\le k\le n+1\) are zero.

**4. Strict log-concavity.** The binomial sequence \(\binom{n+1}{k}\) is strictly log-concave at each interior index. The weights \(w_{n,k}\) are positive and strictly concave, because
\[
 2w_{n,k}-w_{n,k-1}-w_{n,k+1}=\frac2{n+1}>0.
\]
Positive concavity implies strict log-concavity: the arithmetic-geometric mean inequality gives \(w_{n,k}^{\,2}>w_{n,k-1}w_{n,k+1}\). Multiplication of positive log-concave sequences preserves log-concavity. Hence the desired strict inequalities hold at every index \(5\le k\le n\). The four boundary comparisons are checked exactly, using
\[
 a_{n,4}=\frac{n(n-1)(n-2)(3n-7)}{12},\qquad
 a_{n,5}=\frac{n(n-1)(n-2)(n-3)(7n-23)}{120},
\]
where these expressions are zero when their index exceeds the degree (the \(a_{n,5}\) formula is needed only for \(n\ge3\)). The resulting differences are
\[
\begin{aligned}
a_{n,1}^2-a_{n,0}a_{n,2}&=(n+1)(2n+1),\\
a_{n,2}^2-a_{n,1}a_{n,3}&=\frac{n(2n+1)(7n^2+12n-7)}6,\\
a_{n,3}^2-a_{n,2}a_{n,4}&=\frac{n^2(7n^4+27n^3-8n^2-81n+91)}{36},\\
a_{n,4}^2-a_{n,3}a_{n,5}&=\frac{n^2(n-1)(n-2)(10n^4-83n^3+307n^2-433n+7)}{720}.
\end{aligned}
\]
The first two are strictly positive for \(n\ge2\). For the third, put \(t=n-2\ge0\); its parenthesized quartic becomes \(7t^4+83t^3+322t^2+435t+225>0\). The fourth inequality is relevant for \(n\ge4\); putting \(t=n-3\ge1\), its quartic becomes \(10t^4+37t^3+100t^2+248t+40>0\). For \(n=2\), the coefficient sequence is \((1,5,10,5)\), which is strictly log-concave. Thus all interior coefficients satisfy the required strict inequalities for every \(n\ge2\). \(\square\)

## Verification
The accompanying standard-library program `verify.py` constructs graph distances by independent breadth-first searches, tests all vertex subsets for forbidden shortest-path triples for \(2\le n\le8\) (\(174752\) subsets in all), and compares with the closed formula. It also checks the exact coefficient and strict log-concavity inequalities through \(n=250\). Run `python3 verify.py`; its captured output is `verify_output.txt`. These are finite checks only; the proof above supplies the infinite classification and inequalities.

## Relationship to prior work
Thomas, Chandran, Tuite and Di Stefano [1] established general-position properties of Mycielskian graphs, including \(\operatorname{gp}(M_n)=n+1\) and uniqueness of the maximum set for \(n\ge3\) (their Corollary 2), as well as general MGP-partition conditions. Those results are fully acknowledged. Iršič, Klavžar, Rus and Tuite [2] introduced the general-position polynomial and studied unimodality for other families. Roy, Klavžar and Lakshmanan [3] considered Mycielskians primarily in terms of extremal general-position and visibility parameters. The survey [4] discusses both strands. None of these inspected sources states the above full cardinality enumerator or its strict log-concavity. The broader MGP-partition characterization is compatible with the cases here, but does not itself assert this coefficient formula or these inequalities.

## Limitations
The result applies to one Mycielskian application to complete graphs, not to iterated Mycielskians or arbitrary base graphs. The strict log-concavity conclusion is not a claim of real-rootedness. Literature checking cannot exclude an equivalent unindexed enumeration or a reformulation in induced-cluster polynomial terminology. Independent validation has not been performed.

## References
[1] E. J. Thomas, U. Chandran S. V., J. Tuite, G. Di Stefano, *On the General Position Number of Mycielskian Graphs*, arXiv:2203.08170, first posted 2022-03-15, later Discrete Applied Mathematics 353 (2024), 29–43. https://arxiv.org/abs/2203.08170

[2] V. Iršič, S. Klavžar, G. Rus, J. Tuite, *General Position Polynomials*, arXiv:2401.05696, first posted 2024-01-11, Results in Mathematics 79 (2024), article 110. https://arxiv.org/abs/2401.05696

[3] D. Roy, S. Klavžar, A. Lakshmanan S., *Mutual-visibility and general position in double graphs and in Mycielskians*, arXiv:2403.05120, first posted 2024-03-08. https://arxiv.org/abs/2403.05120

[4] J. Tuite et al., *The General Position Problem: A Survey*, arXiv:2501.19385, 2025 and subsequent revisions. https://arxiv.org/abs/2501.19385
