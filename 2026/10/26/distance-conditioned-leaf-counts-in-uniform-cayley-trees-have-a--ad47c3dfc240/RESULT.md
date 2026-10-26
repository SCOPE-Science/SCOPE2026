# Distance-conditioned leaf counts in uniform Cayley trees have a cubic-scale peak

## Finding

Let \(T_n\) be uniformly distributed over all \(n^{n-2}\) labeled trees on \(\{1,\ldots,n\}\), with integer \(n\ge4\). Let \(L_n\) be its number of **unrooted** leaves (vertices of degree one), and let \(D_n\) be the graph distance between two fixed distinct labels. For every integer \(1\le k\le n-1\), write \(F_n(k)=\mathbb E[L_n\mid D_n=k]\) and \(r_n=(n-1)/n\). Then

\[
\boxed{F_n(k)=r_n^{n-k-2}\left(n-k+1-\frac{2}{k+1}\right).}
\]

In particular, for every \(n\ge4\), conditioning the marked pair to be adjacent does **not** change the expected leaf count:

\[
\boxed{F_n(1)=\mathbb E L_n=n r_n^{n-2}.}
\]

For \(1\le k\le n-2\), the exact successive difference is

\[
\boxed{F_n(k+1)-F_n(k)
=\frac{2r_n^{n-k-3}}{n(k+1)(k+2)}\left(n-\frac{(k+2)(k^2+1)}2\right).}
\]

Define \(N_k=(k+2)(k^2+1)/2\) and \(a_n=\min\{k\ge1:N_k\ge n\}\). The regression is strictly increasing up to its peak and strictly decreasing thereafter. If \(n\ne N_{a_n}\), its **unique** maximizing distance is \(a_n\); if \(n=N_{a_n}\), precisely the adjacent distances \(a_n\) and \(a_n+1\) maximize it. The two-point plateaux occur exactly at the infinite family \(n=N_k\), \(k\ge2\); in particular, \(n=10,25,51,\ldots\). The peak is much shorter than a typical marked-vertex separation:

\[
\boxed{a_n=(2n)^{1/3}+O(1).}
\]

Two further asymptotic consequences quantify the size of this effect. With \(\mu_n=\mathbb E L_n\),

\[
\boxed{\max_k F_n(k)-\mu_n
=\frac1e\left(1-3\,2^{-1/3}n^{-1/3}+O(n^{-2/3})\right).}
\]

If integers \(k_n\) satisfy \(k_n/\sqrt n\to x\in(0,\infty)\), then

\[
\boxed{F_n(k_n)-\mu_n\longrightarrow e^{-1}(1-x^2/2).}
\]

Thus the *maximizing* conditioning distance has cubic-root scale, while the positive-versus-negative mean displacement has a square-root-scale asymptotic boundary at \(x=\sqrt2\). The second statement is a limit profile, not an assertion of an exact finite-size crossing at \(\sqrt{2n}\).

## Assumptions and scope

All trees are simple, undirected, connected, and uniformly labeled; the two marked labels are fixed and distinct. Every \(k\in\{1,\ldots,n-1\}\) has positive probability. A leaf always means **degree one**, not zero outdegree of a rooted tree. Empty powers in the forest count are understood algebraically; the extreme case \(k=n-1\) gives \(F_n(n-1)=2\). The principal finite-size classification assumes \(n\ge4\); at \(n=3\), the leaf count is constant and there is no strict peak.

## Proof

**1. Rooted-forest enumeration.** On a complete labeled graph of order \(m\) with a designated set of \(s\in\{1,\ldots,m\}\) roots, the number of spanning forests having exactly one root in each component equals \(s m^{m-s-1}\). To independently establish this classical identity, use the all-minors matrix-tree theorem: deleting the designated root rows and columns from the Laplacian \(mI-J\) leaves \(mI_{m-s}-J_{m-s}\), with eigenvalue \(s\) once and eigenvalue \(m\) of multiplicity \(m-s-1\). For \(m=s\), the forest is empty and the formula gives one. This proves the count at all boundary values.

**2. Condition on the whole connecting path.** Fix a specific simple path of \(k\) edges from label 1 to label 2, including its \(k-1\) ordered interior vertices. Every tree containing this path is uniquely obtained by attaching a rooted forest to its \(k+1\) path vertices; there are

\[
(k+1)n^{n-k-2}
\]

such extensions. If the first endpoint is required to be a leaf, delete it and count the remaining extensions on \(n-1\) vertices rooted at the other \(k\) path vertices. There are \(k(n-1)^{n-k-2}\), so each endpoint has conditional leaf probability

\[
\frac{k}{k+1}\left(\frac{n-1}n\right)^{n-k-2}.
\]

Each interior path vertex has degree at least two. For a fixed vertex outside the path, requiring it to be a leaf allows deletion of that vertex, leaving a rooted forest on \(n-1\) vertices with the same \(k+1\) roots, followed by \(n-1\) choices of its attachment neighbor. This gives \((k+1)(n-1)^{n-k-2}\) extensions and conditional leaf probability \(r_n^{n-k-2}\). There are \(n-k-1\) outside vertices. Summing the leaf probabilities yields

\[
F_n(k)=r_n^{n-k-2}\left(\frac{2k}{k+1}+n-k-1\right)
=r_n^{n-k-2}\left(n-k+1-\frac2{k+1}\right).
\]

The count does not depend on the identities of intermediate path vertices. Therefore it remains valid after conditioning only on \(D_n=k\), rather than on the full path. The Prüfer code gives \(\Pr(v\text{ is a leaf})=r_n^{n-2}\), proving \(\mu_n=n r_n^{n-2}\) and the exact adjacency cancellation \(F_n(1)=\mu_n\).

**3. Strict unimodality and exceptional plateaux.** Put \(g_n(k)=n-k+1-2/(k+1)\). From \(r_n=(n-1)/n\),

\[
F_n(k+1)-F_n(k)
=r_n^{n-k-3}[g_n(k+1)-r_n g_n(k)]
=\frac{r_n^{n-k-3}}{n(k+1)(k+2)}
\left[2(n-k-2)-(k-1)(k+1)(k+2)\right].
\]

The square bracket equals \(2(n-N_k)\). The numbers \(N_k\) grow strictly with positive integer \(k\); \(N_1=3<n\) and \(N_{n-2}>n\) for \(n\ge4\). Hence the successive differences switch sign once, with a possible single zero. Since \(N_k\) is an integer for every positive integer \(k\), equality occurs precisely at \(n=N_k\). Their strict growth gives exactly the maximizing ranks claimed. Since \(N_k=k^3/2+O(k^2)\), the threshold definition yields \(a_n=(2n)^{1/3}+O(1)\).

**4. Asymptotic displacement and its two scales.** An exact expression convenient for expansion is

\[
F_n(k)-\mu_n
=\mu_n\left[r_n^{-k}\left(1-\frac{k-1+2/(k+1)}n\right)-1\right],
\qquad \mu_n=n r_n^{n-2}=n/e+O(1).
\]

For \(k=O(n^{1/3})\), use \(-\log r_n=1/n+1/(2n^2)+O(n^{-3})\) and Taylor's formula uniformly to obtain

\[
F_n(k)-\mu_n
=e^{-1}\left(1-\frac{2}{k+1}-\frac{k^2}{2n}
+O\left(\frac{k+1}{n}+\frac{k^3+1}{n^2}\right)\right).
\]

At \(k=a_n=(2n)^{1/3}+O(1)\), the error is \(O(n^{-2/3})\). Also \(2/(a_n+1)=2^{2/3}n^{-1/3}+O(n^{-2/3})\), and \(a_n^2/(2n)=2^{-1/3}n^{-1/3}+O(n^{-2/3})\). This proves the asserted maximum-uplift expansion.

For \(k/\sqrt n\to x>0\), expanding the same exact expression through relative order \(1/n\) instead gives

\[
r_n^{-k}\left(1-\frac{k-1+2/(k+1)}{n}\right)-1
=\frac{1-k^2/(2n)}n+o(n^{-1}),
\]

which, together with \(\mu_n/n\to e^{-1}\), proves the limiting displacement. All limits are taken along admissible integer distances; no finite experiment is substituted for any asymptotic argument.

## Verification

Execute `python verify_cayley_leaf_distance.py` using standard Python. This standalone checker independently enumerates all Prüfer codes for \(n=2,\ldots,8\) and directly measures leaves and marked distance. It compares conditional means, path probabilities, endpoint leaves, and off-path leaf probabilities to the analytic formulas as exact rational numbers. It also checks the discrete-difference identity and peak classification for dimensions through \(150\), the exceptional tie locations for \(k=2,\ldots,29\), and representative square-root-scale numerical limits. The checker reports **44,755** passing assertions. Exhaustive enumeration of these small orders and finite asymptotic probes are checks, not proofs for all sizes.

## Relationship to prior work

The classical Cayley and rooted-forest enumeration is given, for example, in Pitman's *Coalescent random forests*, especially Section 2 and its formula for a designated root set. The enumeration itself is not claimed as new. Entringer, Meir, Moon, and Székely's study of random-tree Wiener indices relates tree path distances to global statistics but does not give a conditional leaf regression. Neininger's study of Wiener indices treats global path-length and distance moments in different random-tree families, not this finite conditional leaf profile.

An independently published finite law for the degree of a **marked endpoint** given the distance to another endpoint shows that endpoint degrees decrease stochastically with the distance. That law contains the endpoint leaf probability used here, but not the *other* leaves, whose decreasing contribution changes the regression into a unimodal curve. Its main conclusions neither imply this cubic-root maximizing-distance law by specialization nor determine the exceptional double peaks. The new conclusion requires counting the off-path leaves and comparing the two terms. Berzunza Ojeda and Janson's distance-profile paper also studies leaf-biased trees, but its inspected Sections 6–8 concern marked vertices, edges, leaves, and asymptotic distributions, not the exact conditioning on the distance between two arbitrary marked labels.

## Limitations

This classification is for unweighted **uniform Cayley** trees only. It does not cover simply generated trees with arbitrary weights, random recursive trees, or binary search trees. The theorem gives a conditional expectation, not stochastic monotonicity of the full leaf-count distribution. The \(\sqrt n\)-scale claim is a limiting *mean* displacement; the exact location of its finite-sample baseline crossing is not asserted. Earlier enumeration papers could contain an implicit equivalent after additional differentiation or conditioning. An independent priority audit has not been performed.

## References

1. J. Pitman, *Coalescent random forests*, University of California, Berkeley, Statistics Technical Report 457, publicly dated 1996-09-01. https://statistics.berkeley.edu/tech-reports/457 .
2. R. C. Entringer, A. Meir, J. W. Moon, and L. A. Székely, *On the Wiener index of trees from certain families*, Australasian Journal of Combinatorics 10 (1994), 211–224, full text at https://scispace.com/pdf/on-the-wiener-index-of-trees-from-certain-families-4vmfpkb2xt.pdf . Precise initial public day not established.
3. R. Neininger, *The Wiener index of random trees*, Combinatorics, Probability and Computing 11 (2002), 587–597. https://www.math.uni-frankfurt.de/~neiningr/w-ind.pdf .
4. G. Berzunza Ojeda and S. Janson, *The distance profile of rooted and unrooted simply generated trees*, first preprint 2020-09-01, Combinatorics, Probability and Computing 31 (2022), 368–410. https://arxiv.org/abs/2009.00572 .
5. *Exact negative regression between endpoint degree and distance in a uniform Cayley tree*, published mathematical finding, identifier d9ddfb06a9ae (2026). Closely related but distinct endpoint-only conditional law.
