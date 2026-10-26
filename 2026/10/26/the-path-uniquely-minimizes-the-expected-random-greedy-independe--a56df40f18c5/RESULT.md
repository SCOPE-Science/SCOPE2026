# The path uniquely minimizes the expected random-greedy independent set among trees

## Finding
For any integer \(n\ge4\), a uniformly random ordering of the vertices of an \(n\)-vertex tree is processed greedily, accepting a vertex precisely when none of its already accepted neighbours is present. Let \(m(T)\) denote the expected number accepted. Then
\[
T\not\cong P_n\quad\Longrightarrow\quad m(T)>m(P_n).
\]
The non-strict path-minimality theorem is due to Krivelevich, Mészáros, Michaeli and Shikhelman [1]. The present claim establishes the strict equality classification anticipated (but not proved) in their Section 8.

## Assumptions and scope
Graphs are finite, simple, undirected trees; the vertex order is uniformly random, independent of everything else. Let \(P_0\) denote the empty graph and define \(\alpha_k=m(P_k)\) for integers \(k\ge0\). Given a tree \(T\), set
\[
\nu(T)=\sum_{v\in V(T)}\sum_{C\in\operatorname{comp}(T-N[v])}\alpha_{|V(C)|}.
\]
Here \(N[v]\) is the closed neighbourhood; an empty sum is zero. A *proper KC-transformation* moves all branches incident to an endpoint of a bare path to its other endpoint, without moving the edge of that path; both endpoints must be non-leaves. The established facts used from [1, Section 8] are: (i) every \(n\)-vertex tree is reachable from \(P_n\) by successive proper KC-transformations; (ii) \(\nu\) is nondecreasing along each such transformation (Theorem 8.3); (iii) \(m(T)\ge 1+\nu(T)/n\), with equality when \(T=P_n\); (iv) the path sequence \(\alpha\) is subadditive (Lemma 8.1), and the interior KC sum appearing below is nonnegative (Lemma 8.2). These are cited inputs, not new independent proofs.

## Proof
**1. Strict path subadditivity apart from one equality.** For positive integers \(r,s\), put \(h(r,s)=\alpha_r+\alpha_s-\alpha_{r+s}\). We prove
\[
h(r,s)\ge0,\qquad h(r,s)=0\iff(r,s)=(2,2).
\]
From [1, equation (11)],
\[
\alpha_k=\sum_{j=0}^{k-1}\frac{(-2)^j(k-j)}{(j+1)!},\qquad
\alpha_{k+1}-\alpha_k=\sum_{j=0}^{k}\frac{(-2)^j}{(j+1)!}.
\]
Thus \(h(1,s)>0\) for all \(s\ge1\): the displayed difference is strictly below \(1=\alpha_1\), by pairing successive terms of the decreasing alternating series after the initial terms \(1-1\). The values
\[
\alpha_2=1,\quad\alpha_3=5/3,\quad\alpha_4=2,\quad
\alpha_5=37/15,\quad\alpha_6=26/9
\]
give \(h(2,2)=0\), \(h(2,3)=1/5>0\), \(h(2,4)=1/9>0\), and \(h(3,3)=4/9>0\).

For all \(k\ge4\), write
\[
\alpha_k=ck+d+e_k,\quad c=(1-e^{-2})/2,\quad d=(1-3e^{-2})/2,
\quad |e_k|\le\frac{2^{k+1}}{(k+2)!}\le\frac2{45}.
\]
Indeed, subtracting the infinite extension of the finite series gives an alternating tail whose terms, indexed by \(j\ge1\), have magnitudes \(2^{k+j}j/(k+j+1)!\) decreasing in \(j\). Since \(e^2>6\), \(d>1/4\); therefore when \(r,s\ge4\),
\[
h(r,s)\ge d-3(2/45)>0.
\]
If \(r=3\) and \(s\ge4\), then \(h(3,s)\ge 5/3-3c-2(2/45)>7/90>0\), using \(c<1/2\). If \(r=2\) and \(s\ge5\), then
\[
h(2,s)\ge1-2c-2\frac{2^{s+1}}{(s+2)!}
\ge e^{-2}-\frac{128}{5040}>0.
\]
The remaining pairs follow by symmetry from the explicitly checked small cases. This proves the strictness classification.

**2. Every first proper KC move from a path strictly raises \(\nu\).** Let \(P_n\) be a path and choose two non-leaf vertices \(x,y\), separated by \(\ell\ge1\) edges. Removing the segment between them leaves pendant path arms of lengths \(a,b\ge1\). The proper KC transformation produces a three-arm spider with arm lengths \(a,b,\ell\), with the common branch vertex at \(x\). Directly inspecting the components of the closed-neighbourhood deletions gives the exact difference
\[
\begin{split}
\nu(KC(P_n;x,y))-\nu(P_n)
={}&h(a,\ell)+h(b,\ell)\\
&+\sum_{j=1}^{\ell-1}
[\alpha_{a+b+j}+\alpha_j-\alpha_{a+j}-\alpha_{b+j}].
\end{split}
\]
The first two terms are the contributions from the vertices immediately outside the two endpoints of the former bare segment: they account for splitting one path component into two; the other exterior vertices contribute zero. The interior sum is exactly the bare-path KC expression in the proof of Theorem 8.4 of [1]. It is nonnegative by [1, Lemma 8.2]. By Step 1 the first two terms are both positive unless \(a=b=\ell=2\). In that single exceptional case, the first interior summand is
\[
\alpha_5+\alpha_1-2\alpha_3=37/15+1-10/3=2/15>0.
\]
Consequently every proper KC transformation of a path strictly increases \(\nu\).

**3. Propagation to all nonpath trees.** By the KC tree poset result [1, Section 8.1], every nonpath \(n\)-vertex tree \(T\) lies at the end of a chain of proper KC-transformations beginning with \(P_n\). Step 2 makes its first step strictly increase \(\nu\), while [1, Theorem 8.3] makes every subsequent step nondecreasing. Hence \(\nu(T)>\nu(P_n)\). Finally [1, equations (10), (12)] imply
\[
m(T)\ge1+\frac{\nu(T)}n>1+\frac{\nu(P_n)}n=m(P_n).
\]
This proves unique minimization. For \(n\le3\), only one unlabelled tree exists; the statement is therefore formulated for \(n\ge4\).

## Verification
The attached `verify.py` recomputes \(\alpha_k\) by exact rational first-arrival recurrence and checks the displayed spider identity and strictness for every \(1\le a,b,\ell\le5\) using independent graph-component deletion, verifies the strict subadditivity gap over \(1\le r,s\le80\), and confirms the exact exceptional interior value. Finite computation supplements, but does not replace, the proof for all orders.

## Relationship to prior work
Krivelevich, Mészáros, Michaeli and Shikhelman [1] proved the non-strict path lower bound, KC monotonicity of \(\nu\), the path mean formula, and the needed nonnegative interior sum. Their Section 8 explicitly notes that their proof does not yield uniqueness. The present argument isolates strictness at the first KC step from the path and proves the only possible subadditivity equality cannot prevent that strictness. None of [1]'s non-strict assertions is presented as new.

## Limitations
The proof concerns expected size only, not stochastic domination of complete greedy-size distributions, nor strict monotonicity of expected greedy size under arbitrary proper KC transformations. Historical-priority uncertainty remains: independently rediscovered uniqueness or equivalent strictness may exist outside searched and inspected material. No independent audit has been performed.

## References
[1] M. Krivelevich, T. Mészáros, P. Michaeli, C. Shikhelman, *Greedy maximal independent sets via local limits*, arXiv:1907.07216 (initial version 2019-07-16), especially Sections 8.1–8.2, Theorems 1.4, 8.3–8.4 and Lemmas 8.1–8.2; published in *Random Structures & Algorithms* 64 (2024), 986–1015, doi:10.1002/rsa.21200.
