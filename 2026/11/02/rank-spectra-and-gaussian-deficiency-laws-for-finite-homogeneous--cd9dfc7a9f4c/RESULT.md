# Rank spectra and Gaussian deficiency laws for finite homogeneous graph partial automorphisms

## Finding

Let \(\operatorname{PAut}(G)\) denote the inverse monoid of isomorphisms between vertex-induced subgraphs of a finite undirected simple graph \(G\). Define its rank polynomial by
\[
R_G(z)=\sum_{f\in\operatorname{PAut}(G)}z^{|\operatorname{dom}(f)|}.
\]
Every nonempty finite homogeneous graph has an explicit rank polynomial as follows. The unique graph with no vertices, if included in the convention, has the single empty partial automorphism and thus \(R_{\varnothing}(z)=1\). For positive integers \(t,n\), define \(G_{t,n}=tK_n\), the disjoint union of \(t\) cliques of order \(n\), and
\[
B_n(z)=\sum_{j=0}^n\binom{n}{j}^{\!2}j!z^j.
\]
Then
\[
\boxed{R_{G_{t,n}}(z)=R_{\overline{G_{t,n}}}(z)=\sum_{s=0}^t\binom ts\frac{t!}{(t-s)!}(B_n(z)-1)^s.}
\]
The remaining two graphs in the finite homogeneous classification are self-complementary and have
\[
\boxed{R_{C_5}(z)=1+25z+100z^2+100z^3+50z^4+10z^5,}
\]
\[
\boxed{R_{L(K_{3,3})}(z)=1+81z+1296z^2+5616z^3+9072z^4+9072z^5+6048z^6+2592z^7+648z^8+72z^9.}
\]
Thus the complete rank profile is specified for every finite homogeneous simple graph, including the exceptional nine-vertex rook graph, whose partial-automorphism monoid has exactly \(34{,}498\) elements.

For fixed \(t\ge1\), let \(f_n\) be uniform on \(\operatorname{PAut}(tK_n)\), let \(D_n=tn-|\operatorname{dom}(f_n)|\), and keep \(t\) fixed while \(n\to\infty\). Then
\[
\boxed{\frac{D_n-t\sqrt n}{n^{1/4}}\ \Rightarrow\ \mathcal N(0,t/2),}
\]
and
\[
\boxed{|\operatorname{PAut}(tK_n)|\sim\frac{t!(n!)^t\exp(2t\sqrt n-t/2)}{(2\sqrt\pi)^t n^{t/4}}.}
\]
These statements hold unchanged for the complement graphs \(\overline{tK_n}\).

## Assumptions and scope

Apart from the explicitly handled zero-vertex graph, graphs are nonempty, finite, simple, undirected, and **homogeneous** in the induced-subgraph sense: each isomorphism between two vertex-induced subgraphs extends to a graph automorphism. The classification of Gardiner, independently of Golfand and Klin, states that each such graph or its complement is a disjoint union of equal-sized complete graphs, the pentagon, or the line graph of \(K_{3,3}\). The formula includes \(t=1\) and \(n=1\), and counts the empty partial map as rank zero. The central-limit and size-asymptotic statements require fixed \(t\), integer \(n\to\infty\), and uniform sampling from all distinct partial maps, **not** uniform restrictions of full automorphisms.

## Proof

**1. Component enumeration.** In a disjoint union of complete graphs, the nonempty intersection of a domain with each source component must map bijectively to an equally sized subset of precisely one target component; two distinct occupied source components must map to distinct target components, because they contain no edges between them. Conversely every such part assignment and every set of componentwise partial bijections gives an induced-subgraph isomorphism. If precisely \(s\) of the \(t\) source components are occupied, choose them in \(\binom ts\) ways, inject them into distinct target components in \((t)_s=t!/(t-s)!\) ways, and for each source component choose a nonempty partial bijection, counted by \(B_n(z)-1\). This proves the displayed polynomial. Complementing both domain and image induced edge relations preserves precisely the same partial maps, so \(R_G=R_{\overline G}\).

**2. Exceptional graphs.** Homogeneity implies that for an arbitrary subset \(S\subseteq V(G)\), the number of distinct partial automorphisms with domain exactly \(S\) is \(|\operatorname{Aut}(G)|/|\operatorname{Aut}(G)_{(S)}|\), with the pointwise stabilizer in the denominator. Hence
\[
[z^k]R_G(z)=\sum_{\substack{S\subseteq V(G)\\|S|=k}}\frac{|\operatorname{Aut}(G)|}{|\operatorname{Aut}(G)_{(S)}|}.
\]
For \(C_5\), the full group is dihedral of order \(10\); the resulting coefficients are \((1,25,100,100,50,10)\). For \(L(K_{3,3})\), regard vertices as pairs in \(\{0,1,2\}^2\) adjacent when they agree in one coordinate. Its full group consists of independent permutations of the three row and column labels, with optional coordinate interchange, and has order \(2(3!)^2=72\). Directly evaluating the displayed finite sum gives \((1,81,1296,5616,9072,9072,6048,2592,648,72)\). The attached independent verifier instead classifies every induced-subgraph isomorphism type, counts its automorphisms, and independently checks both stabilizer formulas; the exceptional counts are not inferred solely from a black-box group order.

**3. Local rank-deficiency law.** Let \(T_n=B_n(1)\). A uniform partial permutation of an \(n\)-set has deficiency \(J_n=n-r\) distributed by
\[
\Pr(J_n=j)=\frac{\binom nj/j!}{L_n(-1)},\qquad 0\le j\le n,
\]
where the ordinary Laguerre polynomial obeys \(T_n=n!L_n(-1)\). Indeed, \(\binom nj^2(n-j)!=n!\binom nj/j!\). For \(w_{n,j}=\binom nj/j!\),
\[
\frac{w_{n,j+1}}{w_{n,j}}=\frac{n-j}{(j+1)^2}.
\]
This ratio decreases strictly in \(j\), making the weights log-concave and concentrating them near \(\sqrt n\). For fixed real \(x\), with \(j=\lfloor\sqrt n+xn^{1/4}\rfloor\), summing logarithms of these consecutive ratios yields
\[
\log\frac{w_{n,j}}{w_{n,\lfloor\sqrt n\rfloor}}=-x^2+o(1),
\]
uniformly for \(x\) in compact intervals. Outside a fixed compact window, the decreasing ratios imply Gaussian-type upper tails, uniformly after sending the compact-window radius to infinity: for \(|j-\sqrt n|\le\tfrac12\sqrt n\), the sum of logarithmic ratios is bounded above by \(O(n^{-1/2})-c(j-\sqrt n)^2/\sqrt n\) for a fixed \(c>0\); beyond that interval, geometric decay follows by the same monotonicity. Summing the central weights as a Riemann sum therefore gives \(\sum_jw_{n,j}\sim w_{n,\lfloor\sqrt n\rfloor}\sqrt{\pi}\,n^{1/4}\) and
\[
\frac{J_n-\sqrt n}{n^{1/4}}\Rightarrow\mathcal N(0,1/2).
\]

**4. Transfer from partial permutations.** In the component enumeration of Step 1, the term for \(s=t\) has size \(t!(T_n-1)^t\), while the sum of all terms with \(s<t\) is \(O_t(T_n^{t-1})\). Since \(T_n\to\infty\), a uniform partial automorphism occupies all \(t\) source components with probability \(1-O_t(T_n^{-1})\). Conditioned on this event, its \(t\) local partial bijections are independent and uniform among nonempty partial bijections. Removing the nonempty conditioning changes their joint law by at most \(O_t(T_n^{-1})\) in total variation. Consequently \(D_n\), up to a negligible total-variation error, is the sum of \(t\) independent copies of \(J_n\). The preceding local central limit theorem, with \(t\) fixed, yields the stated Gaussian limit.

Finally, the classical fixed-argument Laguerre asymptotic is
\[
L_n(-1)\sim\frac{\exp(2\sqrt n-1/2)}{2\sqrt\pi\,n^{1/4}}.
\]
Combining \(T_n=n!L_n(-1)\) with the dominating \(s=t\) term gives the claimed total-size asymptotic. This last analytic estimate is a classical Laguerre fact, not independently asserted as new.

## Verification

The standalone file `verify.py` reconstructs induced-subgraph isomorphism types by explicit permutations and sums the square of the number of induced occurrences times the type's automorphism count. It independently compares the resulting rank profiles against the component formula for nine small parameter pairs, for both graph and complement, and against direct automorphism-group stabilizer sums for both exceptional graphs. It prints `VERIFY_OK` on success. Tests include the rook-graph coefficient vector through rank nine and count \(34{,}498\). These finite experiments check arithmetic and small cases; the statements for all sizes and the Gaussian convergence follow from the preceding arguments, not from the tests.

## Relationship to prior work

The concept of the partial-graph-automorphism inverse monoid and its Green relations is developed by Jajcay, Jajcayová, Szakács and Szendrei, *Inverse monoids of partial graph automorphisms* (first available September 12, 2018). Their publicly available abstract describes structural characterization, not a homogeneous-graph rank profile. The full paper could not be inspected in this comparison; this creates a publication-priority risk. Fernandes and Paulista, *On the monoid of partial isometries of a finite star graph* (March 10, 2022), study graph-related transformation monoids, Green relations, presentations and cardinalities; a full accessible text was inspected, but its star-isometry object does not provide the rank spectra claimed here. Gardiner's classification and its later survey formulation are the pre-existing classification used in Step 2. The partial-permutation coefficients \(\binom nj^2j!\), the Laguerre identity and its asymptotic are established prior mathematics. Moreover, the exact \(C_5\) values follow from the previously available complete cycle rank enumeration; **they are included only to complete the homogeneous classification and are not claimed individually novel**.

## Limitations

The enumeration and Gaussian law use induced-subgraph partial automorphisms, not graph-metric partial isometries, and the limit keeps the number of clique components fixed. This calculation does not cover arbitrary, nonhomogeneous graphs. The main scientific novelty claim is a best-knowledge combination of the complete finite homogeneous-graph rank profiles and the induced Gaussian rank-deficiency law; no assertion of global bibliographic priority is made. General inverse-semigroup formulas or a specialized analysis in a full paper not accessible here could imply portions of the result. No independent mathematical audit has been performed.

## References

1. R. Jajcay, T. Jajcayová, N. Szakács and M. B. Szendrei, *Inverse monoids of partial graph automorphisms*, arXiv:1809.04422 (initial public posting September 12, 2018), https://arxiv.org/abs/1809.04422 .
2. V. H. Fernandes and T. Paulista, *On the monoid of partial isometries of a finite star graph*, arXiv:2203.05504 (March 10, 2022), https://arxiv.org/abs/2203.05504 .
3. A. Gardiner, *Homogeneous graphs*, Journal of Combinatorial Theory Series B 20 (1976), 94–102.
4. H. D. Macpherson, *A survey of homogeneous structures*, January 14, 2011, Theorem 2.2.4.
5. OEIS A002720, partial-permutation total counts \(\sum_{j=0}^n\binom nj^2j!\) (pre-existing).
