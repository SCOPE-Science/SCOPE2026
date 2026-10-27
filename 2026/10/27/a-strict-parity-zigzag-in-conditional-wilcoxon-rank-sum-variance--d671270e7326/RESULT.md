# A strict parity zigzag in conditional Wilcoxon rank-sum variance given two-sample runs

## Finding

Let a binary word be chosen uniformly among the \(\binom{a+b}{a}\) words with \(a\ge1\) symbols \(1\) and \(b\ge1\) symbols \(0\). Define \(R\) to be the number of maximal contiguous constant-symbol blocks, and \(U=\#\{(i,j):i<j,\,w_i=1,\,w_j=0\}\). The latter is a Mann–Whitney two-sample statistic, or an affine reversal of the Wilcoxon rank sum, when sample labels are read in increasing pooled-rank order.

For every attainable number \(r\) of runs, \(\mathbb E[U\mid R=r]=ab/2\). Let \(V_r=\operatorname{Var}(U\mid R=r)\). For every admissible \(2k\),
\[
V_{2k}=\frac{ab\bigl(2abk+4ab-(a+b)k^2-(a+b)k+2(a+b)+k^2-k\bigr)}{12k(k+1)}.
\]
For every admissible \(2k+1\), define
\[
W(a,b,k)=\frac{ab\bigl(2ab-(a+b)k+a-3b+k-1\bigr)}{12(k+1)},
\qquad V_{2k+1}=\frac{(a-k)W(a,b,k)+(b-k)W(b,a,k)}{a+b-2k}.
\]
For every pair of attainable even run counts separated by two, \(V_{2k}>V_{2k+2}\). Every attainable odd run count is a strict local minimum relative to either existing adjacent even run count: whenever all three exist,
\[
V_{2k}>V_{2k+1}<V_{2k+2}.
\]
In particular, \(\operatorname{Cov}(R,U)=0\) without independence, and conditioning on a run count produces a strict parity-dependent variance zigzag. For example, with \(a=b=3\), the conditional variances for \(r=2,3,4,5,6\) are respectively \(81/4,9/4,25/4,1/4,9/4\).

## Assumptions and scope

The underlying null law is uniform on fixed-content binary words. Positive integers \(a,b\) are unrestricted. An attainable even run count is \(2k\) with \(1\le k\le\min(a,b)\); an attainable odd run count is \(2k+1\) with \(1\le k\le\min(a,b)\) and \(a+b>2k\). Zero-probability conditioning events are excluded. In the odd formula any term whose start-symbol orientation is infeasible has coefficient zero. All variances are ordinary conditional population variances, without asymptotic approximation.

## Proof

Reversal of a word preserves \(R\) and maps \(U\) to \(ab-U\). Therefore \(\mathbb E[U\mid R=r]=ab/2\) for every admissible \(r\), whence \(\operatorname{Cov}(R,U)=0\).

**Run-composition lemma.** Condition on the first symbol, and suppose there are \(u\) runs of ones and \(v\) runs of zeros. Their run lengths are independent uniform positive compositions \(A=(A_1,\ldots,A_u)\) of \(a\) and \(B=(B_1,\ldots,B_v)\) of \(b\): each ordered pair of length vectors defines a unique word. For any uniform positive composition of \(c\) into \(d\) parts, the coordinate mean is \(c/d\) and covariance matrix is
\[
\frac{c(c-d)}{d(d+1)}P_d,\qquad P_d=I_d-\frac{\mathbf 1_d\mathbf 1_d^\mathsf T}{d}.
\]
One proof writes the composition as \(1\) plus a uniform weak composition of \(c-d\), whose symmetric Dirichlet–multinomial counting law has covariance \(c(c-d)P_d/(d(d+1))\). Alternatively, it follows by evaluating the elementary first and second factorial moments under stars-and-bars counting. This formula also holds when \(d=1\) or \(c=d\), since then the composition is deterministic.

For a word starting with \(1\), put \(M_{ij}=\mathbf1_{\{i\le j\}}\); for a word starting with \(0\), put \(M_{ij}=\mathbf1_{\{i<j\}}\), with indices respectively over the one-runs and zero-runs. In either orientation \(U=A^\mathsf T M B\). Set \(s_A=a(a-u)/(u(u+1))\), \(s_B=b(b-v)/(v(v+1))\). Independence and the covariance lemma give the exact matrix identity
\[
\operatorname{Var}(U\mid u,v,\text{orientation})=s_As_B\|P_uMP_v\|_F^2+s_A(b/v)^2\|P_uM\mathbf1_v\|^2+s_B(a/u)^2\|P_vM^\mathsf T\mathbf1_u\|^2.
\]
This follows by centering \(A,B\), expanding their bilinear form, and observing that the linear terms and centered bilinear term are pairwise uncorrelated. No independence of the coordinates within each composition is used.

**Even run counts.** For \(R=2k\), both orientations have \(u=v=k\) and equal probability. The starting-one matrix is the upper triangular all-one matrix, and the starting-zero matrix is its strict upper-triangular counterpart. For either one,
\[
\|P_kMP_k\|_F^2=(k^2-1)/12,\qquad \|P_kM\mathbf1_k\|^2=\|P_kM^\mathsf T\mathbf1_k\|^2=k(k^2-1)/12.
\]
The conditional means in the two orientations are \(ab(k+1)/(2k)\) and \(ab(k-1)/(2k)\). Apply the law of total variance, adding the between-orientation variance \((ab/(2k))^2\). Simplification gives the formula for \(V_{2k}\).

**Odd run counts.** For \(R=2k+1\), the starting-one orientation has \((u,v)=(k+1,k)\), and the starting-zero orientation has \((u,v)=(k,k+1)\). Both orientation-specific means are \(ab/2\). In the first orientation the rectangular staircase matrix satisfies
\[
\|P_{k+1}MP_k\|_F^2=(k-1)(k+2)/12,\quad
\|P_{k+1}M\mathbf1_k\|^2=k(k+1)(k+2)/12,\quad
\|P_kM^\mathsf T\mathbf1_{k+1}\|^2=k(k^2-1)/12.
\]
Substituting into the bilinear variance identity yields exactly \(W(a,b,k)\). Interchanging symbols yields \(W(b,a,k)\) for the second orientation. The numbers of words in the two cases are
\[
\binom{a-1}{k}\binom{b-1}{k-1},\qquad
\binom{a-1}{k-1}\binom{b-1}{k},
\]
so their conditional probabilities are \((a-k)/(a+b-2k)\) and \((b-k)/(a+b-2k)\). Since the component means agree, averaging gives \(V_{2k+1}\).

**Strict parity comparisons.** Algebraic subtraction of the displayed rational expressions gives
\[
V_{2k}-V_{2k+1}
=\frac{ab(a+b)\bigl(2ab-(a+b)k+(a+b)-2k\bigr)}{6k(k+1)(a+b-2k)}.
\]
When the odd count is attainable, put \(x=a-k\ge0\), \(y=b-k\ge0\), \(x+y>0\). The parenthesized factor equals \((k+1)(x+y)+2xy>0\).

Whenever the next even count exists, write \(x=a-k-1\ge0\), \(y=b-k-1\ge0\). Then
\[
V_{2k+2}-V_{2k+1}
=\frac{ab\,\Phi_k(x,y)}{6(k+1)(k+2)(a+b-2k)},
\]
where
\[
\Phi_k(x,y)=k^2(x+y+2)+4kxy+6k(x+y)+8k+x^2y+xy^2+10xy+8(x+y)+8>0.
\]
Finally,
\[
V_{2k}-V_{2k+2}
=\frac{ab\bigl(abk+4ab+2a+2b-k\bigr)}{6k(k+1)(k+2)}>0.
\]
The last numerator is positive since the admissibility of \(2k+2\) implies \(a,b\ge k+1\). These differences prove all assertions, including strictness and boundary cases.

## Verification

The standalone `verify.py` exhaustively generates every binary word for each \(1\le a,b\le8\), groups by attainable run counts, computes conditional moments as exact rational numbers, and compares them to every asserted formula and strict inequality. It passes 1,340 assertions. As a separate exact algebra check, the three displayed variance differences simplify to the stated expressions. Finite enumeration verifies examples and implementation but is not used to infer the universal theorem; the proof above covers all positive \(a,b\).

## Relationship to prior work

Conger and Viswanath study multiset-permutation inversion and descent marginals and their normal approximation, not conditional rank-sum variance at a fixed number of constant-symbol runs. Bhattacharya describes Wald–Wolfowitz and rank-based two-sample statistics in a broad asymptotic framework, not this finite conditional variance profile. Krattenthaler enumerates lattice paths by turns, whereas the present statistic is the enclosed area/inversion count jointly conditioned on turns. Classical Gaussian-binomial descriptions encode inversion marginal distributions but do not by themselves specify the conditional parity inequalities. Works on run-based statistical process control use runs of signaling events or chart run lengths, distinct from fixing the number of pooled binary-label blocks. The full older literature on joint area–turn enumeration could contain equivalent formulas; no claim of exhaustive historical priority is made.

## Limitations

The finding concerns the uniform, fixed-content two-sample rank null, not arbitrary dependent labels, tied pooled observations, nonuniform random words, or the full joint distribution of \((R,U)\). Exact zero covariance is not independence. Classical joint area–turn generating functions may lead indirectly to these expressions; a genuinely stronger previously published result would supersede the novelty claim. Some relevant older publisher full texts were not accessible for complete comparison. Independent mathematical assessment has not been performed.

## References

1. M. Conger and D. Viswanath, *Normal approximations for descents and inversions of permutations of multisets*, arXiv:math/0508242 (first submitted 2005-08-14), https://arxiv.org/abs/math/0508242.
2. B. B. Bhattacharya, *A General Asymptotic Framework for Distribution-Free Graph-Based Two-Sample Tests*, arXiv:1508.07530 (2015), https://arxiv.org/abs/1508.07530.
3. C. Krattenthaler, *The Enumeration of Lattice Paths With Respect to Their Number of Turns* (1997), https://www.mat.univie.ac.at/~kratt/artikel/turnsurv.pdf.
4. B. R. Handa and S. G. Mohanty, *On q-Binomial Coefficients and Some Statistical Applications*, SIAM Journal on Mathematical Analysis (1980), DOI:10.1137/0511090.
5. N. Balakrishnan, I. S. Triantafyllou, and M. V. Koutras, *Nonparametric control charts based on runs and Wilcoxon-type rank-sum statistics*, Journal of Statistical Planning and Inference (2009), DOI:10.1016/j.jspi.2009.02.013.
