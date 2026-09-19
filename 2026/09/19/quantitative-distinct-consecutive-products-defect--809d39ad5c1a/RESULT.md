# Quantitative density one for distinct consecutive products

## Statement

Let \(A\subseteq\mathbb N\) be the canonical prime-gap greedy set constructed in Przemek Chojecki, *Distinct Consecutive Products*: every prime is retained, and at each consecutive-prime gap the whole interior is retained unless doing so creates a repeated product of two distinct consecutive blocks, in which case the whole interior is rejected. Chojecki proves that all consecutive-block products in the increasing enumeration of \(A\) are distinct and that \(A\) has natural density one.

Write
\[
D(X)=\#([1,X]\setminus A).
\]
Then the same construction satisfies the following quantitative strengthening.

**Theorem.** For every fixed \(\varepsilon>0\) and \(B>0\),
\[
\boxed{
D(X)\ll_{\varepsilon,B} X^{5/6+\varepsilon}
      +X(\log X)^{-B}.
}
\]
Consequently, for every fixed \(B>0\),
\[
\boxed{D(X)\ll_B X(\log X)^{-B}.}
\]

More precisely, for every fixed
\[
\frac1{24}<\theta<\frac1{16},
\qquad \rho=\frac1{2-\theta},
\]
if a prime gap \((p,p^+)\) is called short when \(p^+-p\le p^\theta\), then the total length of short rejected gaps with right endpoint at most \(X\) is
\[
\boxed{O_\theta\!\left(X^{1/2+8\theta+o(1)}\right),}
\]
whereas, for every fixed \(B>0\), the total length of all long prime gaps with left endpoint at most \(X\) is
\[
\boxed{O_{\theta,B}\!\left(X(\log X)^{-B}\right).}
\]
Letting \(\theta\downarrow1/24\) gives the exponent \(5/6+\varepsilon\).

The consecutive-product injectivity itself is unchanged: this is a quantitative re-analysis of Chojecki's canonical set, not a new construction.

## Proof

### 1. Long gaps from the \(1/24\) almost-all short-interval theorem

Runbo Li's *Primes in almost all short intervals III*, Theorem 1.1, proves that for every sufficiently small \(\eta_0>0\), all but
\[
O\!\left(Y(\log Y)^{-C}\right)
\]
integers \(n\in[Y,2Y]\) have a prime in
\[
[n-n^{1/24+\eta_0},n],
\]
with an arbitrarily strong fixed logarithmic saving (by choosing the theorem's logarithmic parameter sufficiently large).

Fix \(\theta>1/24\), and choose \(\eta=1/24+\eta_0<\theta\). Consider a prime gap \((p,p^+)\) with \(Y\le p<2Y\) and length \(g=p^+-p>p^\theta\). By Bertrand's postulate, \(p^+<4Y\). Apart from \(O(Y^\eta)\) integers near the left endpoint, every integer \(n\in(p,p^+)\) satisfies
\[
[n-n^\eta,n]\subset(p,p^+),
\]
so such \(n\) is exceptional for Li's theorem. Since \(\eta<\theta\), for large \(Y\) this supplies at least \(g/2\) exceptional integers per long gap. The supplied sets from distinct prime gaps are disjoint. Applying Li's theorem on the dyadic ranges covering \([Y,4Y]\) gives, for every fixed \(B>0\),
\[
\sum_{\substack{Y\le p<2Y\\p^+-p>p^\theta}}(p^+-p)
\ll_{\theta,B}Y(\log Y)^{-B}.
\]
A dyadic summation, treating the lowest scales by disjointness, yields
\[
\sum_{\substack{p\le X\\p^+-p>p^\theta}}(p^+-p)
\ll_{\theta,B}X(\log X)^{-B}.
\]
This improves the qualitative long-gap contribution used in the density-one proof.

### 2. Raw short rejected gaps

Chojecki's canonical-witness reduction shows that a raw rejected gap has a witness
\[
\prod_{i=0}^{r-1}(x-i)=\prod_{j=0}^{s-1}(y+j),
\qquad r>s\ge1.
\]
For a short child below scale \(X\), one has \(s\le X^\theta\) and
\[
r\le L=\lceil X^\theta\log_2 X\rceil.
\]
Chojecki's uniform split-product curve estimate bounds, for fixed \((r,s)\), the number of possible \((x,y)\) by
\[
O\!\left(X^{1/2}(r^3\log X+r^4)\right).
\]
Summing over \(s<r\le L\) therefore gives
\[
\#\{\text{raw short rejected gaps with right endpoint}\le X\}
=O\!\left(X^{R+o(1)}\right),
\qquad
R=\frac12+6\theta.
\]
The published choice \(\theta=1/20\) gives \(R=4/5\); here \(\theta\) is kept symbolic.

### 3. Re-optimizing the witness forest

The proofs of Chojecki's branch/contraction and equal-chain lemmas are algebraic in \(\theta\). For a short child at scale \(Z\), they give:

- at most \(Z^{3\theta+o(1)}\) children from a fixed rejected parent;
- across an unequal short-to-short edge, the parent scale contracts to \(O(Z^\rho)\), where \(\rho=(2-\theta)^{-1}\);
- at most \(Z^{1-\rho+o(1)}\) possible long parents of a short child;
- an equal edge cannot go from a long parent to a short child;
- after an unequal edge, an equal chain contributes at most \(Z^{\theta+o(1)}\) possible endpoints.

Consider first a path originating at a raw short gap and containing exactly \(t\ge0\) unequal edges after maximal equal strings are compressed. Including the terminal-gap length, the exponent of \(X\) is
\[
E_t
=R\rho^t+
  \frac{4\theta(1-\rho^t)}{1-\rho}
  +\theta\rho^t+\theta.
\]
Collecting the \(\rho^t\) term gives coefficient
\[
C_{\rm raw}
=R+\theta-\frac{4\theta}{1-\rho}
=\frac{6\theta^2+3\theta-1}{2(\theta-1)}.
\]
For \(1/24<\theta<1/16\), this is positive. Hence \(E_t\) decreases with \(t\), and its maximum is
\[
E_0=R+2\theta=\frac12+8\theta.
\]

For paths whose backward trace stops at a long parent, with \(t\ge1\) including the first long-to-short unequal edge, the corresponding exponent is
\[
L_t
=(1-\rho)\rho^{t-1}
 +\frac{4\theta(1-\rho^t)}{1-\rho}
 +\theta.
\]
Its \(\rho^{t-1}\) coefficient is
\[
C_{\rm long}
=(1-\rho)-\frac{4\theta\rho}{1-\rho}
=\frac{5\theta^2-10\theta+1}{(\theta-2)(\theta-1)},
\]
again positive throughout \((1/24,1/16)\). Thus \(L_t\) is maximal at \(t=1\), where
\[
L_1=1-\rho+5\theta.
\]
Moreover
\[
E_0-L_1
=\frac{\theta(6\theta-13)}{2(\theta-2)}>0
\]
for this range of \(\theta\). The raw-root paths therefore dominate.

As in Chojecki's proof, repeated scale contraction implies only \(O(\log\log X)\) unequal steps, and summing over intermediate dyadic scales contributes only \(X^{o(1)}\). Hence
\[
\sum_{\substack{v\text{ short rejected}\\x(v)\le X}}d(v)
=O_\theta\!\left(X^{1/2+8\theta+o(1)}\right).
\]

### 4. The defect bound

The complement of \(A\), apart from the integer \(1\), is exactly the union of the interiors of rejected prime gaps. A rejected gap meeting \([1,X]\) has right endpoint \(O(X)\) by Bertrand's postulate. Combining the short- and long-gap estimates gives
\[
D(X)
\ll_{\theta,B}
X^{1/2+8\theta+o(1)}+X(\log X)^{-B}.
\]
Given \(\varepsilon>0\), choose \(\theta=1/24+\delta\) with \(\delta>0\) sufficiently small; then \(1/2+8\theta<5/6+\varepsilon\), and the \(o(1)\) term can be absorbed into the remaining margin. This proves
\[
D(X)\ll_{\varepsilon,B}X^{5/6+\varepsilon}+X(\log X)^{-B}.
\]
For a prescribed fixed \(B\), choose any fixed \(\varepsilon<1/6\); then the polynomial term is eventually dominated by \(X(\log X)^{-B}\), giving the super-logarithmic density-one bound.

## Relation to prior work and originality

Chojecki's theorem proves the same canonical set has density one. Its quantitative short-gap estimate is
\[
O(X^{9/10+o(1)}),
\]
coming from the fixed choice \(\theta=1/20\), while the final theorem is stated only as \(D(X)=o(X)\). Li's later/current public manuscript supplies the stronger almost-all prime-interval exponent \(1/24\). Combining that input with a symbolic re-optimization of the witness forest lowers the structured short-gap loss exponent from \(9/10\) to every exponent above \(5/6\), and retaining Li's arbitrary logarithmic exceptional-set saving yields the global super-logarithmic defect bound.

To the best of our knowledge, searches for the problem under “distinct consecutive products”, “consecutive block products”, the Erdős--Graham formulation, the exponents \(9/10\), \(5/6\), and applications of the \(1/24\) almost-all short-interval theorem did not locate a prior statement of these quantitative bounds. Public summaries and a public reconstruction/formalization of the density-one theorem located during the literature check state the density-one conclusion but did not surface the present defect estimates. The motivating preprint and Li's newest short-interval manuscript are recent, so unindexed concurrent work remains a material originality risk.

## Limitations

The result quantifies Chojecki's particular canonical greedy set; it does not prove that \(5/6\) is an optimal short-gap exponent, nor does it give a polynomial upper bound for the full defect \(D(X)\). The long-gap term is controlled only by an arbitrarily strong fixed logarithmic saving, so the strongest unconditional global statement here is \(D(X)\ll_B X(\log X)^{-B}\) for each fixed \(B\). No lower bound for the defect is asserted. The proof also inherits the cited uniform integral-point estimate and Li's almost-all short-interval theorem.

## Reproducibility

`artifacts/verify_exponents.py` symbolically checks the forest exponents, their monotonicity coefficients, the comparison between the raw-root and long-parent branches, and the limiting value \(E_0=5/6\) at \(\theta=1/24\). `artifacts/verification.txt` records its deterministic output. The script is auxiliary; the proof above is the mathematical argument.

## References

1. P. Chojecki, *Distinct Consecutive Products*, arXiv:2609.17543.
2. R. Li, *Primes in almost all short intervals III*, public manuscript, https://runbolicarey.com/assets/downloads/Primes_in_almost_all_short_intervals_III.pdf.
3. W. Castryck, R. Cluckers, P. Dittmann, K. H. Nguyen, *The dimension growth conjecture, polynomial in the degree and without logarithmic factors*, Algebra & Number Theory 14 (2020), 2261--2294.
