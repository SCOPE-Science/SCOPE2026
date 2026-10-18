# Exact \(p\)-strong Roman domination of complete tripartite graphs with three defender regimes
## Finding
For integers \(a,b,c\ge2\) and \(p\ge3\), let \(G=K_{a,b,c}\), \(N=a+b+c\), and \((n_1,n_2,n_3)=(a,b,c)\). Define
\[
\begin{aligned}
W_1&=\min_{1\le i\le3}\left(n_i+\left\lceil\frac{N-n_i}{p}\right\rceil\right),\\
W_2&=\min_{1\le i<j\le3}\left(2+\left\lceil\frac{N-n_i-1}{p}\right\rceil+\left\lceil\frac{N-n_j-1}{p}\right\rceil\right),\\
W_3&=\min_{1\le i<j\le3}\left(3+\left\lceil\frac{N-n_i-2}{p}\right\rceil+\left\lceil\frac{N-n_j-2}{p}\right\rceil\right).
\end{aligned}
\]
Then
\[
\boxed{\gamma_{\mathrm{StR}}^p(K_{a,b,c})=\min\{W_1,W_2,W_3\}.}
\]
All three values are attained by explicit configurations described in the proof. The third type is essential: for every \(a\ge4\), setting \(p=2a-2\) gives
\[
\boxed{\gamma_{\mathrm{StR}}^{2a-2}(K_{a,a,a})=5,}
\]
with exactly \(3a^3\) minimum functions: choose two of the three parts and put label \(2\) at one vertex of each; put label \(1\) at one vertex in the remaining part and zero elsewhere.

## Assumptions and scope
A \(p\)-strong Roman dominating function on a finite graph \(G\) of maximum degree \(\Delta\) is a mapping
\[
f:V(G)\longrightarrow\{0,1,\ldots,1+\lceil\Delta/p\rceil\}
\]
such that, for every vertex \(v\) with \(f(v)=0\), there is a neighbor \(u\in N(v)\) with
\[
f(u)\ge1+\left\lceil\frac{|N(u)\cap Z|}{p}\right\rceil,\qquad Z=\{w:f(w)=0\}.
\]
Its weight is \(w(f)=\sum_v f(v)\), and \(\gamma_{\mathrm{StR}}^p(G)\) is the minimum weight. All three part sizes are at least two. These are ordinary \(p\)-strong Roman functions, with **no** total-support restriction; \(p\) is the capacity divisor, not the \(k\)-strong Roman game parameter.

## Proof
Write the three parts as \(V_i\), let \(s_i\) be the number of positively labelled vertices in \(V_i\), and put \(z_i=n_i-s_i\), \(z=\sum_i z_i\). A *defender* is a positive vertex \(u\in V_i\) satisfying the defensive inequality; its weight above the baseline label \(1\) is at least \(\lceil(z-z_i)/p\rceil\). A defender in \(V_i\) protects every zero outside \(V_i\), but none inside it. If there are no zeros, then the weight is at least \(N\), which is at least \(W_1\).

**One-defender-part lower bound.** Suppose all defenders belong to a single part \(V_i\). Because a zero in \(V_i\) could not be protected, \(z_i=0\), so \(s_i=n_i\). Let \(t=s_j+s_k\ge0\) be the positive count outside \(V_i\). A defender in \(V_i\) then sees exactly \(N-n_i-t\) zeros, and hence
\[
w(f)\ge n_i+t+\left\lceil\frac{N-n_i-t}{p}\right\rceil\ge n_i+\left\lceil\frac{N-n_i}{p}\right\rceil\ge W_1.
\]
The second inequality follows because increasing the positive count by one can decrease a ceiling by at most one.

**Two-defender-part lower bound.** Suppose defenders exist in distinct parts \(V_i,V_j\), and call the remaining part \(V_k\). Choose one defender from each. Their positive-label excesses and the baseline for all positive vertices yield
\[
w(f)\ge s_i+s_j+s_k+\left\lceil\frac{n_j-s_j+n_k-s_k}{p}\right\rceil+\left\lceil\frac{n_i-s_i+n_k-s_k}{p}\right\rceil.
\]
Increasing either \(s_i\) or \(s_j\) by one increases the baseline by one and can decrease at most one displayed ceiling by one. Consequently, for a lower bound these counts may be replaced by \(s_i=s_j=1\). With \(t=s_k\ge0\), this gives
\[
w(f)\ge F_{ij}(t):=2+t+\left\lceil\frac{N-n_i-1-t}{p}\right\rceil+\left\lceil\frac{N-n_j-1-t}{p}\right\rceil.
\]
For every integer \(t\ge2\) and \(p\ge3\), \(2\lceil t/p\rceil\le t\). Indeed this holds at \(t=2,3\), and for \(t\ge4\) follows by writing \(t=3q+r\), \(0\le r\le2\), and checking the three residues. Each ceiling falls by at most \(\lceil t/p\rceil\) when its argument is reduced by \(t\). Therefore \(F_{ij}(t)\ge F_{ij}(0)\) for \(t\ge2\). If \(t=1\), the lower bound is exactly \(F_{ij}(1)\). Thus
\[
w(f)\ge\min\{F_{ij}(0),F_{ij}(1)\}\ge\min\{W_2,W_3\}.
\]
Since every zero has a defender and at least one such defender exists whenever zeros exist, these two cases exhaust all feasible functions.

**Matching constructions.** For \(W_1\), fix a minimizing part \(V_i\); assign label \(1+\lceil(N-n_i)/p\rceil\) to one vertex there, label \(1\) to the other \(n_i-1\) vertices there, and zero elsewhere. For \(W_2\), fix minimizing distinct parts \(V_i,V_j\), choose one vertex in each, assign respectively \(1+\lceil(N-n_i-1)/p\rceil\) and \(1+\lceil(N-n_j-1)/p\rceil\), and zero elsewhere. For \(W_3\), choose one vertex each in \(V_i,V_j\) and one vertex in \(V_k\); give the first two vertices labels \(1+\lceil(N-n_i-2)/p\rceil\), \(1+\lceil(N-n_j-2)/p\rceil\), and the third label \(1\). The zero vertices in \(V_i\), \(V_j\), and \(V_k\) are all defended by a selected vertex in a different part. All labels remain within \(1+\lceil\Delta/p\rceil\), where \(\Delta=N-\min_i n_i\). This proves equality.

**Sharp third-mode census.** Put \((n_1,n_2,n_3)=(a,a,a)\), \(a\ge4\), \(p=2a-2\). Direct substitution gives \(W_1=a+2\), \(W_2=6\), and \(W_3=5\). For an optimum function of weight five, defenders cannot lie in only one part, since then the first lower bound is at least \(a+2\ge6\). Pick two defender parts. Because every defender sees at least one zero neighbor, each defender has label at least two. Thus a weight-five function has either two positive vertices of labels \((3,2)\), or three positive vertices of labels \((2,2,1)\) (the case of two defenders each of label \(2\) and an additional positive label \(1\)). With only two positive vertices, both defenders see \(2a-1>p\) zeros, so each would need label at least three: impossible at total weight five. For a \((2,2,1)\) function the two label-two defenders must lie in distinct parts; each must see at most \(p=2a-2\) zeros, forcing the label-one vertex to lie in the third part. Conversely this arrangement works. There are \(\binom32 a^3=3a^3\) possibilities, giving the classification.

## Verification
The standard-library verifier `VERIFIER.py` independently evaluates the original vertexwise domination predicate for all label assignments in ten small graph/parameter cases. It compares the computed minimum weight to the theorem (763,975 assignments). It also checks all candidate labelings of weight at most five for the sharp balanced family with \(a=4,5,6,7\), including exact counts, and performs 97 further integer threshold checks through \(a=100\). Run `python3 VERIFIER.py` to reproduce the output recorded in `VERIFIER_OUTPUT.txt`. These finite calculations do not substitute for the preceding proof.

## Relationship to prior work
Valenzuela-Tripodoro and collaborators introduced \(p\)-strong Roman domination and determined values for several families, including complete bipartite graphs, in their 2024 paper. The inspected complete-text preprint does not present this exact three-part formula or its three-regime sharp family. The classical strong Roman case (divisor \(2\)) has a known exact complete multipartite formula; it does not determine the \(p\ge3\) values. Total strong Roman domination adds a separate condition on positive support and is a different optimization, as is the \(k\)-strong Roman game model. The lower-bound proof here addresses the simultaneous competition between two defender parts and the capacity cost saved by an auxiliary positive vertex.

## Limitations
The theorem assumes exactly three nonempty parts of size at least two and \(p\ge3\). It does not establish the same three-term formula for two-part graphs, singleton parts, or more than three parts. The complete minimum-function enumeration is proved only for the explicitly stated balanced sharp family, not arbitrary part sizes. Bibliographic uniqueness is not certified and independent expert review has not been performed.

## References
1. J. C. Valenzuela-Tripodoro, M. A. Mateos-Camacho, M. Cera, R. M. Casablanca and M. P. Álvarez-Ruiz, “p-Strong Roman Domination in Graphs,” *WSEAS Transactions on Mathematics* 23 (2024), 1005–1017, DOI:10.37394/23206.2024.23.104; complete open version arXiv:2501.10140.
2. M. P. Álvarez-Ruiz, I. G. Yero, T. Mediavilla-Gradolph, S. M. Sheikholeslami and J. C. Valenzuela, “On the strong Roman domination number of graphs,” *Discrete Applied Mathematics* 231 (2017), 44–59, DOI:10.1016/j.dam.2016.12.013.
3. S. Nazari-Moghaddam, M. Soroudi, S. M. Sheikholeslami and I. G. Yero, “On the total and strong version for Roman dominating functions in graphs,” arXiv:1912.01093.
