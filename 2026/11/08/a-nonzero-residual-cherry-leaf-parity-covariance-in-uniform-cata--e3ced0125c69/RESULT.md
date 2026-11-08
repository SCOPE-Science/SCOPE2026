# A nonzero residual cherry–leaf-parity covariance in uniform Catalan trees

## Finding
Let \(T_n\) be uniform among rooted ordered full binary trees with exactly \(n\) internal vertices (hence \(n+1\) leaves). Define the signed leaf-depth imbalance and the number of cherries by
\[
\Delta_n=\sum_{\ell\text{ leaf}}(-1)^{\operatorname{depth}(\ell)},\qquad
H_n=\#\{\text{internal vertices with two leaf children}\}.
\]
Then the unnormalized covariance has the nonzero finite limit
\[
\boxed{\lim_{n\to\infty}\operatorname{Cov}(\Delta_n,H_n)=\frac{3}{32}.}
\]
Although each of the two variances is of linear order, their correlation is of smaller, inverse-linear order:
\[
\boxed{\lim_{n\to\infty}n\operatorname{Corr}(\Delta_n,H_n)=\frac{1}{2\sqrt2}.}
\]
Here correlation is defined for \(n\ge3\). Finite-size signs need not agree with the positive limit: the exact covariances at \(n=3,4,5,6\) are respectively \(24/25,-24/49,4/7,-12/121\).

## Assumptions and scope
A full binary tree has either zero children (a leaf) or exactly two *ordered* children at each vertex. An isolated leaf has size zero, depth zero and no cherries. A tree of size \(n\) has \(C_n=\binom{2n}{n}/(n+1)\) equally likely shapes. The root has depth zero. All assertions concern the uniform **ordered** tree model, not coalescent, uniform leaf-labelled phylogenetic, or random binary-search trees. The limit uses integer \(n\to\infty\).

## Proof
Write \(d(T)=\sum_{\ell}(-1)^{\operatorname{depth}(\ell)}\) and \(h(T)\) for the two statistics, and set
\[
F(z;u,v)=\sum_{T}z^{|T|}u^{d(T)}v^{h(T)}.
\]
This is well-defined as a formal \(z\)-series with finite Laurent-polynomial coefficients in \(u\). The one-leaf tree contributes \(u\). At an internal root each child subtree's leaf depths increase by one, reversing its signed imbalance. The root becomes a cherry only when both children are leaves. Therefore
\[
F(z;u,v)=u+z\bigl(F(z;u^{-1},v)^2+(v-1)u^{-2}\bigr).\tag{1}
\]
Set \(s=\sqrt{1-4z}\), with \(s(0)=1\). At \(u=v=1\), (1) yields \(C(z)=2/(1+s)\). At \(u=1\) with \(v\) free, the cherry enumerator is
\[
G(z,v)=\frac{1-\sqrt{1-4z-4z^2(v-1)}}{2z}.
\]
In particular, with derivatives evaluated at \(u=v=1\),
\[
B(z):=F_v=\frac z s,\qquad
M(z):=F_u=\frac1{2-s},
\]
and, by differentiating \(M(z,v)=\bigl[1-2z(v-1)\bigr]/\bigl[1+2zG(z,v)\bigr]\),
\[
J(z):=F_{uv}=-\frac{2z}{2-s}-\frac{2z^2}{s(2-s)^2}.\tag{2}
\]
Consequently, the three exact expectations are \(\mathbb E\Delta_n=[z^n]M/C_n\), \(\mathbb E H_n=[z^n]B/C_n\), and \(\mathbb E(\Delta_nH_n)=[z^n]J/C_n\). In particular,
\[
\mathbb E H_n=\frac{n(n+1)}{2(2n-1)}\quad(n\ge1).
\]

For the limit, expand the functions from (2) at their unique dominant singularity \(z=1/4\):
\[
M=\frac12+\frac{s}{4}+\frac{s^2}{8}+\frac{s^3}{16}+O(s^4),\qquad
J=-\frac{1}{32s}-\frac9{32}-\frac{11s}{128}+O(s^2).
\]
The omitted analytic (even-power) pieces have no singular contribution at \(1/4\); subsequent odd powers give the stated remainder terms. The only other potential denominator zero, \(2-s=0\), lies at \(z=-3/4\). Standard binomial-coefficient extraction applies. For \(n\ge2\), exact identities include
\[
\frac{[z^n]s^{-1}}{C_n}=n+1,\qquad
\frac{[z^n]s}{C_n}=-\frac{n+1}{2n-1},\qquad
\frac{[z^n]s^3}{C_n}=\frac{3(n+1)}{(2n-1)(2n-3)}.
\]
It follows, retaining terms needed after multiplication by the order-\(n\) cherry mean, that
\[
\begin{aligned}
\mathbb E\Delta_n&=-\frac18-\frac{9}{64n}+O(n^{-2}),\\
\mathbb E H_n&=\frac n4+\frac38+O(n^{-1}),\\
\mathbb E(\Delta_nH_n)&=-\frac n{32}+\frac3{256}+O(n^{-1}).
\end{aligned}
\]
Subtracting the product of means cancels the order-\(n\) terms and gives \(3/32+O(n^{-1})\).

For the correlation, differentiating (1) twice in \(u\) gives
\[
P(z):=F_{uu}\big|_{1,1}=\frac{2zM(z)^2+4zC(z)M(z)}s=\frac{9}{8s}+O(1).
\]
As \(\mathbb E\Delta_n^2=([z^n](P+M))/C_n\), this implies
\[
\operatorname{Var}(\Delta_n)=\frac98n+O(1).
\]
Twice differentiating \(G(z,v)\) gives \(G_{vv}(z,1)=2z^3s^{-3}\). Coefficient extraction yields, for \(n\ge3\),
\[
\operatorname{Var}(H_n)=\frac{n(n-2)(n-1)(n+1)}{2(2n-3)(2n-1)^2}=\frac n{16}+O(1).
\]
Dividing the covariance by the product of standard deviations now proves the asserted limit \(n\operatorname{Corr}(\Delta_n,H_n)\to1/(2\sqrt2)\). The exact small-\(n\) examples follow from the same coefficient formulas. This completes the proof.

## Verification
Run `python3 check.py` from the directory containing that file; Python's standard library is the only dependency. The verifier exhaustively enumerates all ordered full binary tree shapes with up to nine internal vertices and compares their signed leaf sums, cherry sums, and mixed sums with a separate recursive count. It also compares the formal-derivative recurrences, Catalan coefficients, and exact cherry coefficients through size 100, and checks specified small covariances. It reports `CHECKS_PASS 640` when successful. These finite checks corroborate the identities but do not replace the all-size generating-function proof or singularity analysis.

## Relationship to prior work
Janson's 2005 paper proves depth-residue normal limits for conditioned Galton–Watson trees, including the binary-tree setting. His result supplies relevant context for the *marginal* parity fluctuation and does not state the cherry–parity mixed covariance or its residual constant. The Catalan cherry enumerator is classical; its generating polynomial is tabulated in OEIS A068763 and linked to Flajolet–Sedgewick's *Analytic Combinatorics*. Equation (1) and its mixed derivative isolate the interaction between local cherries and global parity; neither marginal statement determines the order-one covariance after cancellation of order-\(n\) contributions. These comparisons do not certify absence of an equivalent statement in all earlier tree-enumeration literature.

## Limitations
This is a one-model, two-statistic covariance result. It does not claim a joint central limit theorem, universality beyond ordered full binary trees, or a general sign classification for all finite sizes. Earlier multivariate tree enumerations may contain equivalent coefficient identities implicitly; this historical-priority risk has not been eliminated. Independent mathematical validation has not been performed.

## References
1. S. Janson, *Congruence properties of depths in some random trees*, publicly available 2005-09-21, https://arxiv.org/abs/math/0509471 .
2. P. Flajolet and R. Sedgewick, *Analytic Combinatorics*, Cambridge University Press, 2009, https://algo.inria.fr/flajolet/Publications/AnaCombi/anacombi.html .
3. OEIS A068763, cherry-refined Catalan enumeration, https://oeis.org/A068763 .
