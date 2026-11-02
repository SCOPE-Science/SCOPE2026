# Asymptotic rigidity and the shifted size law for bipartite Yang–Baxter solutions

## Finding

Write \(B(n)\) for the number of isomorphism classes of bipartite set-theoretic Yang–Baxter solutions on an \(n\)-element set, in the sense of Militaru [1]. All logarithms are natural. As \(n\to\infty\),

\[
\boxed{\displaystyle
\log B(n)=\frac{n^2}{4}(\log n-\log 2-1)
+\frac{n^2}{16\log n}
+O\!\left(\frac{n^2}{(\log n)^2}\right).}
\]

More precisely, the orbit counts have the asymptotically free weighted sum

\[
\boxed{\displaystyle
B(n)\sim\sum_{m=2}^{n-2}\frac{(m!)^{n-m-1}}{(n-m)!}.}
\]

For a uniformly sampled isomorphism class, the probability of a split solution tends to zero. Every nonsplit class has a canonically defined permutation block \(Z\) [1], and its size \(M_n=|Z|\) satisfies

\[
\boxed{\displaystyle
M_n=\frac n2+\frac{n}{4\log n}
+o_{\mathbb P}\!\left(\frac{n}{\log n}\right).}
\]

Equivalently, for each fixed \(\varepsilon>0\), the proportion of classes with
\(|M_n-n/2-n/(4\log n)|>\varepsilon n/\log n\) tends to zero. In addition,

\[
\boxed{\displaystyle
\mathbb P\bigl(\operatorname{Aut}(X,r)=\{1\}\bigr)\longrightarrow1.}
\]

Thus almost all isomorphism classes in this newly defined algebraic family are rigid, while the canonical permutation block is slightly larger than half the underlying set. The coefficient \(1/16\) in the logarithmic asymptotic is a consequence of that size bias; it is not visible in a fixed balanced-partition estimate.

## Assumptions and scope

For finite disjoint sets \(Y,Z\) and permutations \(g_y\in S_Z\) indexed by \(y\in Y\), let \(X=Y\sqcup Z\). Define a braid solution \(R_g\) to be the identity on \(Y^2\cup Z^2\), with

\[
R_g(y,z)=(g_y(z),y),\qquad
R_g(z,y)=(y,g_y^{-1}(z)).
\]

The associated Yang–Baxter solution is \(r_g=\tau_X\circ R_g\), where \(\tau_X\) flips the two entries. A datum is split if every \(g_y\) is the identity. The cited classification [1, Theorem 2.12 and Corollary 2.13] shows that a nonsplit isomorphism class has a unique value \(m=|Z|\), that \(k=|Y|=n-m\), and that such classes correspond to orbits of \(S_m\) acting by conjugation on \(k\)-element multisets of \(S_m\), excluding the all-identity multiset.

Here \(B(n)\) counts isomorphism classes, **not labeled solutions**. The probability statements use the uniform probability measure on these \(B(n)\) distinct classes. The asymptotic statements concern positive integers \(n\to\infty\); no other types of Yang–Baxter solution are being counted.

## Proof

### 1. Exact orbit model and coarse exponential bounds

Set \(G=S_m\), \(N=|G|=m!\), and \(k=n-m\). Let \(o(m,k)\) denote the conjugation-orbit count of multisets of cardinality \(k\) in \(G\). The finite classification in [1] yields

\[
B(n)=\left\lfloor\frac n2\right\rfloor+1
+\sum_{m=2}^{n}\bigl(o(m,n-m)-1\bigr). \tag{1}
\]

The total number of such multisets is
\(T_{m,k}=\binom{N+k-1}{k}\). Orbit sizes lie between \(1\) and \(N\), hence

\[
\frac{T_{m,k}}{N}\le o(m,k)\le T_{m,k}.\tag{2}
\]

Uniformly when \(m\) is between \(n/3\) and \(2n/3\), Stirling's formula and \(k=O(n)\) imply

\[
\log T_{m,k}
=k\log(m!)-\log(k!)+O(k^2/m!)
=m(n-m)(\log m-1)+O(n\log n).\tag{3}
\]

In particular, both bounds in (2) have the same logarithm to error \(O(n\log n)\). Put

\[
F_n(m)=m(n-m)(\log m-1).\tag{4}
\]

Outside the interval \([n/3,2n/3]\), the crude estimate
\(T_{m,k}\le(N+k)^k\) gives

\[
\log o(m,k)
\le (n-m)m\log n+n\log(n+1)
\le\left(\frac29+o(1)\right)n^2\log n.\tag{5}
\]

The middle value \(m=\lfloor n/2\rfloor\) gives at least
\(\exp((1/4+o(1))n^2\log n)\) orbits. Thus the excluded ranges and the \(O(n)\) split and subtraction terms contribute a negligible fraction of \(B(n)\).

### 2. The saddle and its first displacement

Let \(L=\log n\), \(x=m/n\), and

\[
h_L(x)=x(1-x)(L+\log x-1).
\]

Then \(F_n(m)=n^2h_L(m/n)\). On \([1/3,2/3]\),

\[
\begin{aligned}
h_L'(x)&=(1-2x)(L+\log x-1)+(1-x),\\
h_L''(x)&=-2(L+\log x-1)+\frac{1-2x}{x}-1.
\end{aligned}
\]

For all sufficiently large \(L\), the second derivative is negative with magnitude bounded above and below by positive multiples of \(L\). The unique maximizer \(x_L\) is therefore determined by \(h_L'(x_L)=0\). Taylor expansion around \(1/2\) yields

\[
x_L=\frac12+\frac{1}{4L}+O(L^{-2}),\tag{6}
\]

and

\[
\max_{x\in[1/3,2/3]}h_L(x)
=\frac14(L-\log2-1)+\frac{1}{16L}+O(L^{-2}).\tag{7}
\]

Rounding the maximizing \(nx_L\) to an integer changes \(F_n\) by only \(O(L)\). The bounds (2)–(5), the \(n\) possible summands, and (7) give the stated expansion for \(\log B(n)\), since \(O(n\log n)=o(n^2/L^2)\).

For a fixed \(\varepsilon>0\), strict concavity gives a loss of at least \(c\varepsilon^2n^2/L\) in \(F_n(m)\) for integer \(m\) outside the interval \(|m/n-x_L|\le\varepsilon/L\), for some absolute \(c>0\) when \(n\) is large. That loss dominates the \(O(n\log n)\) uncertainty in (3). Combining with (5) proves that the proportion of classes outside the interval tends to zero. Using (6) with an arbitrarily smaller fixed \(\varepsilon\) establishes the asserted \(o_{\mathbb P}(n/L)\) size law.

### 3. Nearly all orbit representatives have no symmetry

For \(m,k\to\infty\) with \(m/n\to1/2\), consider the action of
\(H=S_m\times S_k\) on ordered tuples \(G^k\). The first factor acts by simultaneous conjugation; the second permutes tuple positions. These orbits are precisely the multisets modulo conjugation. The stabilizer in \(H\) is the automorphism group of the corresponding nonsplit bipartite solution, by [1, Proposition 2.15].

Write

\[
\mathcal R_{m,k}=\frac1{N^k}
\sum_{(\beta,\sigma)\in H\setminus\{(1,1)\}}
\#\operatorname{Fix}_{G^k}(\beta,\sigma).
\tag{8}
\]

We show \(\mathcal R_{m,k}=o(1)\), uniformly whenever \(m/n\to1/2\) and \(k/n\to1/2\). If \(\beta=1\), the fixed-tuples count is \(N^{c(\sigma)}\), where \(c(\sigma)\) is the number of cycles of \(\sigma\). The standard permutation-cycle identity gives

\[
\sum_{\sigma\ne1}N^{c(\sigma)-k}
=\prod_{j=0}^{k-1}\left(1+\frac jN\right)-1
=O(k^2/N)=o(1).\tag{9}
\]

For \(\beta\ne1\), let \(C_\beta\) be its centralizer in \(G\). A permutation \(\sigma\in S_k\) with \(f\) fixed positions has at most \((k-f)/2\) other cycles, each allowing at most \(N\) choices for one representative coordinate; a fixed position requires a choice in \(C_\beta\). Consequently

\[
\#\operatorname{Fix}_{G^k}(\beta,\sigma)
\le |C_\beta|^f N^{(k-f)/2}.\tag{10}
\]

There are at most \(k^{k-f}\) permutations of \(k\) positions with exactly \(f\) fixed points. For \(m\ge5\), every nonidentity conjugacy class of \(S_m\) has at least
\(s_m=m(m-1)/2\) elements. Denoting the partition number by \(p(m)\), we obtain, for every integer \(f\ge1\),

\[
\sum_{\beta\ne1}\left(\frac{|C_\beta|}{N}\right)^f
=\sum_{\substack{\mathcal C\text{ a conjugacy class}\\\mathcal C\ne\{1\}}}
|\mathcal C|^{1-f}
\le p(m)s_m^{1-f}.\tag{11}
\]

For \(f=0\), the corresponding sum is at most \(N\). Combining (10)–(11), the contribution from all \(\beta\ne1\) to (8) is at most

\[
N\left(\frac{k}{\sqrt N}\right)^k
+p(m)s_m^{1-k}
\sum_{j=0}^{k-1}\left(\frac{ks_m}{\sqrt N}\right)^j.\tag{12}
\]

In the present regime \(k\asymp m\), \(N=m!\), and \(ks_m/\sqrt N\to0\). The geometric sum is eventually at most \(2\). Also \(p(m)\le2^{m-1}\), so each term of (12) tends to zero. Equations (9) and (12) prove the asserted uniform \(\mathcal R_{m,k}=o(1)\).

Burnside's lemma now gives the **relative** estimate

\[
 o(m,k)=\frac{N^{k-1}}{k!}\bigl(1+\mathcal R_{m,k}\bigr)
=\frac{(m!)^{k-1}}{k!}(1+o(1)).\tag{13}
\]

To infer typical rigidity, examine an individual \(H\)-orbit with stabilizer order \(d\). Its contribution to the identity term in Burnside's lemma is \(1/d\), while its aggregate contribution from nonidentity group elements is \(1-1/d\). If \(d\ge2\), this second contribution is at least \(1/2\). Therefore the fraction of the orbits of \(G^k\) with nontrivial stabilizer is at most

\[
\frac{2\mathcal R_{m,k}}{1+\mathcal R_{m,k}}=o(1).\tag{14}
\]

The size-law proved in Step 2 concentrates essentially all bipartite isomorphism classes in a regime where (13)–(14) hold uniformly. After discarding the negligible split classes, (14) proves asymptotic rigidity. Finally, (13) throughout that window, together with negligibility of other \(m\), gives the asserted asymptotic sum for \(B(n)\). This completes the proof.

## Verification

The standalone `verify.py` implements the conjugation action of \(S_m\) on itself, computes orbit lengths for every conjugator for \(2\le m\le6\), and applies exact integer generating-function dynamic programming. Together with the elementary one-element-multiset case it reconstructs the published enumeration

\[
B(1),\ldots,B(8)=1,2,3,7,17,57,305,4120.
\]

The same program computes the finite saddle of \(F_n\) at five increasing values up to \(n=10000\) and compares the three-term estimate and the scaled displacement. Execute with `python3 verify.py` from the directory containing this document. The expected final line is `VERIFY_OK`.

The infinite asymptotic statements and the typical automorphism conclusion follow from the inequalities and group actions established in the proof, not from numerical extrapolation.

## Relationship to prior work

Militaru [1] constructs, classifies and counts bipartite Yang–Baxter solutions exactly and describes their automorphism groups. In particular, equation (1), the orbit model and the stabilizer interpretation are existing results, not new claims here. The new result is the three-term large-\(n\) asymptotic, the displaced canonical block-size law, and the resulting asymptotic rigidity conclusion for **uniform isomorphism classes**.

Kaur–Prajapati–Prasad [2] study simultaneous conjugacy orbits of **ordered** tuples for a **fixed finite group** as tuple length varies. That regime neither allows \(S_m\) to grow simultaneously nor factors by permutation of the coordinates, and it does not imply this saddle or rigidity statement directly.

Sadov [3] gives general asymptotic-freeness estimates for permutation groups acting on subsets and multisets. Those general bounds provide useful context for Step 3; they do not state the bipartite Yang–Baxter solution enumerator, the explicit logarithmic correction \(1/16\), or the biased typical block size. The proof here specializes the full \(S_m\times S_k\) orbit action to obtain all three conclusions. The possibility of an equivalent implication through other literature on unlabeled permutation tuples remains a priority risk.

## Limitations

The estimate is logarithmic through the displayed error term; it is not a full multiplicative saddle-point equivalent with an evaluated leading prefactor. The probabilistic statements concern the uniform distribution on **isomorphism classes**, not on labeled Yang–Baxter maps, which can have a different bias. The result applies only to the bipartite family in [1], not to all unitary or all set-theoretic Yang–Baxter solutions. Historical priority beyond the inspected and searched sources has not been independently established.

## References

1. G. Militaru, *Bipartite solutions of the set-theoretic Yang–Baxter equation*, arXiv:2610.30845v1, first posted 22 October 2026. https://arxiv.org/html/2610.30845v1 . See Theorem 2.12, Corollary 2.13, Proposition 2.15 and Theorem 2.16.
2. D. Kaur, S. K. Prajapati, A. Prasad, *Simultaneous Conjugacy Classes as Combinatorial Invariants of Finite Groups*, arXiv:1905.07957, 2019; *Communications in Algebra* 50 (2022), 4549–4559. https://arxiv.org/abs/1905.07957 . See Sections 2 and 3.
3. S. Sadov, *On asymptotically free action of permutation groups on subsets and multisets*, arXiv:1312.6886, 2013. https://arxiv.org/abs/1312.6886 . See the introduction and general stabilizer bounds.
