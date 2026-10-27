# A sharp ninefold birth-horizon for degree–leaf covariance in plane increasing trees

## Finding
Let \(T_n\) be a uniformly random plane increasing tree on birth labels \(1,\dots,n\). For a fixed nonroot label \(j\ge 2\), write \(D_{j,n}\) for the number of children of vertex \(j\), and \(L_n\) for the total number of leaves. For every integer \(n\ge j\), put
\[
 a_{j,n}=\prod_{k=j}^{n-1}\frac{2k}{2k-1},\qquad
 b_{j,n}=\prod_{k=j}^{n-1}\frac{2k-2}{2k-1}
 =\frac{j-1}{n-1}a_{j,n},
\]
where empty products equal \(1\). Then the **exact mixed covariance** is
\[
 \boxed{\operatorname{Cov}(D_{j,n},L_n)=\frac{a_{j,n}-1}{3}+b_{j,n}-1.}
\]
It equals zero when \(n=j\). At every later tree size, its sign has the following sharp classification:
\[
 \boxed{\operatorname{Cov}(D_{j,n},L_n)<0\quad(j<n\le 9j-4),\qquad
 \operatorname{Cov}(D_{j,n},L_n)>0\quad(n\ge 9j-3).}
\]
Thus **the first positive covariance occurs at exactly \(n=9j-3\)** for every nonroot birth label \(j\ge2\); no later-size zero occurs. For instance, vertex \(j=2\) changes from negative at \(n=14\) to positive at \(n=15\). In the simultaneous regime \(j\to\infty\) and \(n/j\to t\ge1\),
\[
 \operatorname{Cov}(D_{j,n},L_n)\longrightarrow
 \frac{(\sqrt t-1)(\sqrt t-3)}{3\sqrt t}.
\]
The limit independently exhibits the crossover at the ratio \(t=9\).

## Assumptions and scope
A plane increasing tree is a rooted tree with ordered children and strictly increasing labels along root-to-vertex paths. At size \(n\), the new vertex \(n+1\) chooses uniformly among the \(2n-1\) insertion gaps. Conditional on the tree, a vertex with \(d\) children is chosen as parent with probability \((d+1)/(2n-1)\). This growth makes all \((2n-3)!!\) plane increasing trees on \(n\) labels equiprobable. The root label \(j=1\) is excluded from the exact threshold statement: the proof starts from the marked nonroot vertex's deterministic birth state. Degree means **outdegree** throughout, not total undirected graph degree. All expectations and covariances concern this single probability model, without conditioning on tree shape.

## Proof
Let \(W_n=D_{j,n}+1\), and let \(B_n\) indicate that vertex \(j\) is still a leaf. At its birth, \(W_j=B_j=1\) deterministically, while \(L_j\) is random. Write \(g_n=2n-1\) and \(\mathcal F_n\) for the growth history. If \(I_j\) indicates attachment to vertex \(j\), and \(I_\ell\) attachment to **some leaf**, then
\[
 W_{n+1}=W_n+I_j,\quad L_{n+1}=L_n+1-I_\ell,
\]
\[
 \mathbb E(I_j\mid\mathcal F_n)=\frac{W_n}{g_n},\quad
 \mathbb E(I_\ell\mid\mathcal F_n)=\frac{L_n}{g_n},\quad
 \mathbb E(I_jI_\ell\mid\mathcal F_n)=\frac{B_n}{g_n}.
\]
The last equality uses that a leaf has exactly one attachment gap. Hence, writing \(a_n=\mathbb EW_n\), \(b_n=\mathbb EB_n\),
\[
 a_{n+1}=a_n\frac{2n}{2n-1},\qquad
 b_{n+1}=b_n\frac{2n-2}{2n-1},\qquad
 \mathbb EL_n=\frac{2n-1}{3}\quad(n\ge2).
\]
Multiplying the two update equations gives the conditional product identity
\[
 \mathbb E(W_{n+1}L_{n+1}\mid\mathcal F_n)
 =W_nL_n+W_n+\frac{W_n-B_n}{2n-1}.
\]
Taking expectations and subtracting marginal means yields
\[
 C_{n+1}-C_n=\frac{a_n/3-b_n}{2n-1}
 =\frac{b_n(n-3j+2)}{3(j-1)(2n-1)},
 \qquad C_n=\operatorname{Cov}(W_n,L_n).
\]
The products satisfy \(a_{n+1}-a_n=a_n/(2n-1)\), and \(b_{n+1}-b_n=-b_n/(2n-1)\). Since \(C_j=0\), telescoping produces
\[
 C_n=\frac{a_n-1}{3}+b_n-1.
\]
The finite difference is negative at first, vanishes at \(n=3j-2\), and is positive thereafter. Therefore, to establish the first positive size, it suffices to check the signs at the two successive sizes \(9j-4\) and \(9j-3\).

Set \(q=j-1\ge1\), \(m=n-1\ge q\), and \(r_h=(2h)!!/(2h-1)!!\) for integer \(h\ge1\). Since \(a_{j,n}=r_m/r_q\),
\[
 C_n=\frac43\bigl(F(q,m)-1\bigr),\qquad
 F(q,m)=\frac{r_m}{r_q}\frac{m+3q}{4m}.
\]
For \(k\in\{4,5\}\) define \(f_q(k)=F(q,9q+k)\). One obtains the exact ratio
\[
 \frac{f_{q+1}(k)}{f_q(k)}=
 \prod_{s=1}^{9}\frac{2(9q+k+s)}{2(9q+k+s)-1}
 \cdot\frac{2q+1}{2q+2}\cdot
 \frac{12q+12+k}{9q+9+k}\cdot\frac{9q+k}{12q+k}.
\]
After subtracting \(1\), canceling factors, and collecting terms, the numerator for \(k=4\) is
\[
 P_4(q)=3(30233088q^6+185807520q^5+467376480q^4+
 615684240q^3+447870672q^2+170561415q+26566925),
\]
with positive denominator
\[
 (3q+1)(6q+5)(6q+7)(18q+11)(18q+13)(18q+17)(18q+19)(18q+23)(18q+25).
\]
For \(k=5\), the numerator is \(-P_5(q)\) with
\[
 P_5(q)=816293376q^8+6258249216q^7+20236013568q^6+
 35761124160q^5+37291355424q^4+22945309344q^3+
 7719297192q^2+1101181470q+2977975,
\]
and strictly positive denominator
\[
 (2q+3)(6q+5)(6q+7)(12q+5)(18q+11)(18q+13)
 (18q+17)(18q+19)(18q+23)(18q+25).
\]
The certificate is a direct rational-function identity; `checker.py` checks its expanded numerator/denominator coefficient signs. Consequently \(f_q(4)\) is strictly increasing in integer \(q\ge1\), and \(f_q(5)\) is strictly decreasing. Wallis's product asymptotic \(r_h\sim\sqrt{\pi h}\) yields \(f_q(4),f_q(5)\to1\) as \(q\to\infty\). Therefore
\[
 f_q(4)<1<f_q(5)\quad\text{for every integer }q\ge1.
\]
For an independent base-case check, \(f_1(4)=16777216/16900975<1\) and \(f_1(5)=2097152/2064825>1\). Since the covariance is increasing at and beyond these locations, the two strict inequalities and the finite-difference sign prove the complete threshold classification. Finally, \(r_m/r_q\to\sqrt t\) and \(b_{j,n}\to1/\sqrt t\) whenever \(j\to\infty\), \(n/j\to t\ge1\), proving the limit.

## Verification
The standalone `checker.py` tests the rational certificate by symbolic exact expansion and positivity of every polynomial coefficient. Independent rational dynamic programming tracks the joint distribution of the total leaf count, marked-vertex attachment weight, and the marked-vertex leaf indicator; 512 exact moment/probability assertions passed. Direct rational sign checks passed for every \(2\le j\le99\) at all relevant sizes through and beyond the crossover. The exact polynomial inequalities and telescoping argument—not finite enumeration—prove the theorem for all admissible labels and sizes. Run `python checker.py` with Python 3 and SymPy installed.

## Relationship to prior work
Mahmoud, Smythe and Szymański (1993) supply the uniform-gap PORT growth rule and establish global leaf means and variances, fixed-root marginal outdegree means, and branch-leaf laws; their sections 2–8 do not state the covariance between a fixed nonroot birth label's outdegree and the total leaf count, nor the ninefold sign threshold. Zhang (arXiv:1706.02441; first public June 8, 2017) derives fixed-label degree marginals and moments, not the mixed degree–leaf covariance. Bóna and Pittel (arXiv:2108.04989; first public August 11, 2021) study ranks (including leaves) of random vertices and asymptotic independence of uniformly sampled vertex ranks, not this fixed-birth-label dependence. In **unordered uniform recursive trees** a previously recorded root-degree/leaf covariance has a different sign law and a different attachment kernel; it cannot imply the present PORT theorem. The source comparisons are about implications of statements, not mere title overlap.

## Limitations
The result is specific to uniform plane increasing trees, nonroot birth labels, and covariance with **all** leaves. It does not establish stochastic dependence beyond second moments, a central limit theorem, or a corresponding threshold for root outdegree or other attachment rules. Historical priority has residual uncertainty beyond the full texts and published-result records inspected; independent assessment is not yet performed. The asymptotic expression assumes both labels and size diverge at a finite fixed ratio \(t\ge1\).

## References
1. H. M. Mahmoud, R. T. Smythe, J. Szymański, *On the Structure of Random Plane-Oriented Recursive Trees and Their Branches*, Random Structures & Algorithms **4** (1993), 151–176. DOI: `10.1002/rsa.3240040204`.
2. P. Zhang, *On several properties of plane-oriented recursive trees*, arXiv:`1706.02441` (first public June 8, 2017), later in *Probability in the Engineering and Informational Sciences*.
3. M. Bóna and B. Pittel, *Random increasing plane trees: asymptotic enumeration of vertices by distance from leaves*, arXiv:`2108.04989` (first public August 11, 2021).
