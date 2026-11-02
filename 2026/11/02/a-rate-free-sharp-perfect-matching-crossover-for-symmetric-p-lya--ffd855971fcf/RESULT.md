# A rate-free sharp perfect-matching crossover for symmetric Pólya threshold graphs

## Finding

For a symmetric two-colour Pólya urn with initial red and black masses both \(R_n>0\) and same-colour reinforcement \(\Delta_n>0\), generate an \(n\)-vertex threshold graph by taking each draw as an isolated/universal creation bit, and then discard self-loops. Put
\[
\kappa_n=\frac{2R_n}{\Delta_n},\qquad \delta_n=\kappa_n^{-1}=\frac{\Delta_n}{2R_n}.
\]
For every sequence of even integers \(n\to\infty\) and every positive sequence \(\kappa_n\to\infty\), **without any condition on the ratio** \(\kappa_n/n\), the perfect-matching probability obeys the sharp, rate-free asymptotic
\[
\boxed{\Pr\{G_n\text{ has a perfect matching}\}
  \sim \sqrt{\frac{2}{\pi}}\sqrt{\frac1n+\frac1{\kappa_n}}.}
\]
Equivalently its effective system size is \(n_{\mathrm{eff}}=(n^{-1}+\kappa_n^{-1})^{-1}\). In particular, when \(\kappa_n/n\to\lambda\in(0,\infty)\),
\[
\sqrt n\,\Pr\{G_n\text{ has a perfect matching}\}
 \longrightarrow\sqrt{\frac2\pi}\sqrt{1+\lambda^{-1}}.
\]
If \(\kappa_n/n\to\infty\), this recovers the fair independent-bit \(\sqrt{2/(\pi n)}\) constant; if \(\kappa_n/n\to0\) while \(\kappa_n\to\infty\), the probability is asymptotic to \(\sqrt{2/(\pi\kappa_n)}\). The critical reinforcement scale is therefore \(\delta_n\asymp n^{-1}\).

## Assumptions and scope

All graphs are labeled, undirected and loopless for purposes of matching. For \(i<j\), the edge \(\{i,j\}\) is present exactly when the \(j\)-th red/black urn draw is red; a red draw adds a universal vertex, and a black draw adds an isolated vertex. The first draw does not influence off-diagonal edges. The urn masses and reinforcement may depend on the even graph order \(n\), are strictly positive, and are identical across colours initially. There is no assumption of independent draws. The result treats ordinary graph-theoretic perfect matchings (each vertex covered by one edge, no loops). The scaling requires both \(n\to\infty\) through even integers and \(\kappa_n\to\infty\). The exact formulas below hold for all \(n\ge2\) even and \(\kappa>0\).

For \(a>0\), write \((a)_j=a(a+1)\cdots(a+j-1)\), with \((a)_0=1\). The following finite formula, obtained by combining the previously known threshold-graph ballot criterion with the Pólya exchangeable-word law, is used as a lemma rather than claimed as an independent innovation:
\[
P_n(\kappa)=\frac{1}{(\kappa)_{n-1}}
\sum_{u=n/2}^{n-1}
\left[\binom{n-1}{u}-\binom{n-1}{u+1}\right]
(\kappa/2)_u(\kappa/2)_{n-1-u}.
\]
Here \(P_n(\kappa)\) denotes the perfect-matching probability and \(\binom{n-1}{n}=0\). The only claimed new asymptotic is the rate-free formula above; the fixed-concentration regime is distinct.

## Proof

**1. Threshold matchings as ballot paths.** Remove the first creation bit and reverse the remaining \(L=n-1\) bits. Code a universal vertex as \(+1\) and an isolated vertex as \(-1\). The threshold-graph matching criterion of Reilly and Scheinerman (2009, Theorem 5.22) says that an even-order threshold graph has a perfect matching if and only if every prefix sum of this reversed word is nonnegative. Briefly, a suffix with more isolated than universal vertices cannot match its isolated vertices to their only possible neighbours; conversely, the suffix inequalities imply Hall's condition matching all isolated vertices to later universal vertices, with the remaining even number of universal vertices matched within their clique. This argument does not use loops.

**2. Reflection and exact urn probabilities.** Conditional on the number \(U\) of \(+1\) bits in this length-\(L\) word, exchangeability makes the word uniform. For \(U=u\ge n/2\), the reflection principle counts precisely
\[
N_{L,u}=\binom Lu-\binom L{u+1}
\]
nonnegative-prefix words; if \(u<n/2\), the count vanishes. A specified word with \(u\) red and \(L-u\) black draws has probability \((\kappa/2)_u(\kappa/2)_{L-u}/(\kappa)_L\), by the Pólya urn law. Summing yields the displayed exact finite formula.

**3. Reduce the ballot event to an absolute endpoint moment.** Put \(K=2U-L\), which has odd integer values and a distribution symmetric about zero. For \(K>0\), the fraction of words with nonnegative prefixes is exactly
\[
\frac{N_{L,U}}{\binom LU}=\frac{2(K+1)}{n+K+1}.
\]
Consequently,
\[
P_n(\kappa)=\mathbb E\left[\frac{2(K+1)}{n+K+1}\mathbf1_{\{K>0\}}\right].
\]
Since \(\mathbb E K_+=\mathbb E|K|/2\), simple algebra, including the boundary \(K=1\), gives the explicit error control
\[
\left|P_n(\kappa)-\frac{\mathbb E|K|}{n}\right|
\le\frac2n+\frac{2\mathbb E K^2+2\mathbb E|K|}{n^2}.
\]
The inequality follows by subtracting \(2K/n\) on \(\{K>0\}\), combining numerators to obtain \(2[n-K(K+1)]/[n(n+K+1)]\), and bounding the absolute value using \(K\ge1\).

**4. Exact endpoint variance.** De Finetti's representation for the symmetric Pólya urn gives a mixing variable \(\Theta\sim\operatorname{Beta}(\kappa/2,\kappa/2)\). Conditional on \(\Theta\), all \(L\) signs are independent and \(+1\) has probability \(\Theta\). Therefore \(\mathbb EK=0\) and the exact variance is
\[
\sigma_{n,\kappa}^{2}:=\mathbb EK^2
=L+\frac{L(L-1)}{\kappa+1}.
\]
This includes the correlation contribution from all \(\binom L2\) distinct pairs of urn draws.

**5. Triangular-array central limit theorem for every reinforcement rate.** Suppose \(n\to\infty\) and \(\kappa=\kappa_n\to\infty\). Write \(m=2\Theta-1\) and, conditionally on \(\Theta\), let \(\xi_i\in\{-1,1\}\) be the independent draw signs. The gamma representation of a Beta variable and the gamma central limit theorem show
\[
A_n:=\sqrt{\kappa+1}\,m\ \Rightarrow\ N(0,1).
\]
Set \(B_n=L^{-1/2}\sum_{i=1}^{L}(\xi_i-m)\). Its conditional characteristic function tends to \(\exp(-t^2/2)\) in probability for every fixed real \(t\): the conditional variables are uniformly bounded, their conditional variance is \(1-m^2\to1\) in probability, and the third-order characteristic-function error is \(O_t(L^{-1/2})\) uniformly in the latent parameter. Bounded convergence of these conditional characteristic functions shows the **joint** limit \((A_n,B_n)\Rightarrow(Z_1,Z_2)\) for independent standard normals \(Z_1,Z_2\).

Now
\[
\frac K{\sigma_{n,\kappa}}
=c_nA_n+d_nB_n,\quad
c_n=\frac L{\sigma_{n,\kappa}\sqrt{\kappa+1}},\quad
 d_n=\frac{\sqrt L}{\sigma_{n,\kappa}}.
\]
Both coefficients are bounded and nonnegative, and
\[
c_n^2+d_n^2=1+\frac{L}{(\kappa+1)\sigma_{n,\kappa}^{2}}
\longrightarrow1.
\]
Every subsequence therefore has a further subsequence along which these coefficients converge to \((c,d)\) with \(c^2+d^2=1\). Its limit \(cZ_1+dZ_2\) is standard normal; the subsequence principle proves \(K/\sigma_{n,\kappa}\Rightarrow N(0,1)\) for **arbitrary** relative growth of \(n\) and \(\kappa\). Since \(\mathbb E(K/\sigma_{n,\kappa})^2=1\), the absolute values are uniformly integrable. Hence
\[
\frac{\mathbb E|K|}{\sigma_{n,\kappa}}\longrightarrow\sqrt{2/\pi}.
\]

**6. Transfer the exact absolute-moment limit to matching.** Let \(r_n=(n^{-1}+\kappa_n^{-1})^{1/2}\). The exact variance gives \(\sigma_{n,\kappa_n}/n\sim r_n\), with no assumption on the ratio \(\kappa_n/n\), and \(r_n\to0\). The Step 3 error is \(O(r_n^2)=o(r_n)\): use \(\mathbb E K^2=\sigma_{n,\kappa_n}^{2}\), \(\mathbb E|K|\le\sigma_{n,\kappa_n}\), and \(n^{-1}\le r_n^2\). Combining with Step 5 yields \(P_n(\kappa_n)\sim\sqrt{2/\pi}\,r_n\), as claimed.

## Verification

The self-contained standard-library program `verify.py` performs independent finite graph matching by bitmask dynamic programming, exhaustively compares that condition with the reversed ballot rule for even orders \(2,4,6,8,10\), and checks the beta-urn probability via two independently implemented finite sums at five rational symmetric Beta parameters. It also verifies the reflection identity over all even orders through \(248\), and compares exact beta-binomial probabilities with the sharp asymptotic across three graph sizes and four reinforcement regimes. There are \(8620\) successful finite assertions; the recorded output is in `VERIFIER_OUTPUT.txt`. These computations corroborate the finite lemma and numerical behaviour, but they do not establish an infinite-dimensional limit. The full analytic argument is above.

## Relationship to prior work

Yu, Alajaji and Gharesifard (2026) introduce the Pólya threshold-graph process and establish its urn word probabilities, vertex degrees, Laplacian spectrum and consensus dynamics; matching is not treated. Reilly and Scheinerman (2009, Theorems 5.22–5.23) establish the exact deterministic matching/ballot criterion and the independent-fair-bit matching probability, including its \(\sqrt{2/(\pi n)}\) asymptotic. Both are used explicitly, not claimed as new. Antal, Ben-Naim and Krapivsky (2010) study first passages and eventual ties for Pólya urns, with scaling of initial colour imbalance; their inspected statements do not give the growing finite-horizon, symmetric matching crossover. Schulte-Geers and Stadje (2014) study all-time maximal urn percentages and the Beta mixing representation, including a related \(1-\log2\) fixed-parameter value. The present claim is specifically the sharp, **rate-free** joint growing-graph/vanishing-reinforcement scaling in Step 6, not the underlying ballot count, exchangeability, or fixed-concentration boundary.

## Limitations

The result requires equal initial colour masses and even graph order. It concerns only existence probability of a perfect matching in the loopless projection, not matching counts, Hamiltonicity, or graph dynamics. No asymptotic claim is made when \(\kappa_n\) remains bounded. The exact finite sum is derived from published structural and urn identities and is not independently novel. The assessed originality is provisional: unindexed ballot/urn boundary-crossing results may imply the rate-free asymptotic. Independent verification and definitive historical-priority assessment have not been performed.

## References

- Jinghan Yu, Fady Alajaji, and Bahman Gharesifard, *Pólya Threshold Graphs*, arXiv:2603.18452v1 (March 19, 2026). https://arxiv.org/pdf/2603.18452
- Elizabeth Perez Reilly and Edward R. Scheinerman, *Random Threshold Graphs*, Electronic Journal of Combinatorics 16 (2009), #R130, Theorems 5.22–5.23. https://www.combinatorics.org/ojs/index.php/eljc/article/download/v16i1r130/pdf/
- Tibor Antal, E. Ben-Naim, and P. L. Krapivsky, *First Passage Properties of the Pólya Urn Process*, arXiv:1005.0867v1 (2010). https://arxiv.org/pdf/1005.0867
- Ernst Schulte-Geers and Wolfgang Stadje, *Maximal Percentages in Pólya's Urn*, arXiv:1401.1805v4 (2014). https://arxiv.org/pdf/1401.1805
