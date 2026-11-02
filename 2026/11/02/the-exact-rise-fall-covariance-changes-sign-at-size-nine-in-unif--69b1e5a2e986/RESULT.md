# The exact rise–fall covariance changes sign at size nine in uniform compositions

## Finding

Let \(R_n\) count strict rises and \(D_n\) count strict falls between consecutive parts of a uniformly sampled ordinary composition of \(n\). Their covariance is exactly zero for \(n=1,2\), negative for \(3\le n\le8\), and positive for every \(n\ge9\). The sign changes exactly once among the nontrivial sizes. An explicit exact expression is

\[
\operatorname{Cov}(R_n,D_n)=\frac{231n-1975}{15876}
+\frac1{2^n}\left(\frac{4(-1)^n n}{27}-\frac{7(-1)^n}{81}+\frac13+\frac{2p_n}{147}\right)
-\frac4{81\,4^n},
\tag{1}
\]
where \(p_n=13\) if \(n\equiv0\pmod3\), \(p_n=-2\) if \(n\equiv1\pmod3\), and \(p_n=-11\) if \(n\equiv2\pmod3\). In particular,
\[
\operatorname{Cov}(R_n,D_n)=\frac{11n}{756}-\frac{1975}{15876}+O(n\,2^{-n}).
\]
The precise boundary values are \(\operatorname{Cov}(R_8,D_8)=-49/16384\) and \(\operatorname{Cov}(R_9,D_9)=335/65536\).

## Assumptions and scope

For every integer \(n\ge1\), an *ordinary composition* of \(n\) is a finite nonempty ordered tuple of positive integers \((a_1,\ldots,a_k)\) summing to \(n\). All \(2^{n-1}\) such compositions have equal probability. A strict rise occurs at a position \(i\) with \(a_i<a_{i+1}\); a strict fall occurs where \(a_i>a_{i+1}\); equal neighboring parts count as neither. The variables \(R_n\) and \(D_n\) count these events. This is an exact finite-size theorem, not a conditional-on-number-of-parts result. It makes no claim for nonuniform composition models or restricted allowed part sizes.

## Proof

Write \(S(x)=x/(1-x)\) for the generating function of one positive part and \(G(x)=1/(1-S(x))=(1-x)/(1-2x)\) for any (possibly empty) sequence of positive parts. Mark a strict rise with two consecutive parts. Its weight generating function is
\[
U(x)=\sum_{1\le a<b}x^{a+b}=\frac{x^3}{(1-x)(1-x^2)}.
\]
There are arbitrary sequences before and after a distinguished rise, so with \(A_n=\sum_\sigma R_n(\sigma)\), summed over all compositions of \(n\),
\[
P(x)=\sum_{n\ge1}A_n x^n=G(x)^2 U(x)
=\frac{x^3}{(1+x)(1-2x)^2}.\tag{2}
\]

For the mixed moment, mark one rise and one fall. They cannot be the same adjacent comparison. If their positions share a part, they form either a peak \(a<b>c\) or a valley \(a>b<c\). Their respective weight series are
\[
H(x)=\sum_{b\ge2}x^b\left(\sum_{a=1}^{b-1}x^a\right)^2
=\frac{x^2}{(1-x)^2}\left(\frac{x^2}{1-x}-\frac{2x^3}{1-x^2}+\frac{x^4}{1-x^3}\right),
\]
\[
V(x)=\sum_{b\ge1}x^b\left(\sum_{a>b}x^a\right)^2
=\frac{x^5}{(1-x)^2(1-x^3)}.
\]
If the two comparisons are disjoint, their marked two-part blocks are separated by an arbitrary part sequence. There are two possible orders of the marked rise and fall. Thus, letting \(B_n=\sum_\sigma R_n(\sigma)D_n(\sigma)\),
\[
Q(x)=\sum_{n\ge1} B_nx^n
=G(x)^2\big(H(x)+V(x)\big)+2G(x)^3U(x)^2
=\frac{x^4(1+x^2-2x^3-2x^4)}{(1-x)(1+x)^2(1-2x)^3(1+x+x^2)}.\tag{3}
\]
Every ordered marked rise–fall pair is counted exactly once in one of these cases. Distinguishing a peak from a valley is essential: their generating functions differ.

Partial fractions (or direct coefficient extraction from (2) and (3)) yield, for all \(n\ge1\),
\[
A_n=\frac{2^n(3n-5)}{36}-\frac{(-1)^n}{9},
\tag{4}
\]
\[
B_n=2^n\left(\frac{(n+1)(n+2)}{72}-\frac{61(n+1)}{756}+\frac{155}{5292}\right)
+\frac{(-1)^n(2n+1)}{54}+\frac16+\frac{p_n}{147}.\tag{5}
\]
The three-periodic \(p_n\) comes from \((13-2x-11x^2)/(1-x^3)\). Reversal of compositions gives \(\mathbb E R_n=\mathbb E D_n=A_n/2^{n-1}\). Also \(\mathbb E[R_nD_n]=B_n/2^{n-1}\). Substitution into the definition of covariance gives (1).

It remains to prove the sign **for every size**, rather than infer it from a finite calculation. Exact substitution gives zero at \(n=1,2\), and at \(n=3,4,5,6,7,8\) respectively gives
\[
-\frac1{16},\quad-\frac1{64},\quad-\frac{17}{256},\quad-\frac{17}{1024},\quad-\frac{113}{4096},\quad-\frac{49}{16384}.
\]
For \(n\ge9\), since \(|p_n|\le13\), the absolute value of the two correction terms in (1) is bounded by
\[
E_n=\frac1{2^n}\left(\frac{4n}{27}+\frac7{81}+\frac{26}{147}+\frac13\right)+\frac4{81\,4^n}.
\]
The positive linear term is \(L_n=(231n-1975)/15876\). The sequence \(L_n\) is strictly increasing, while \(E_n\) is strictly decreasing for all \(n\ge9\). At the endpoint, \(L_9=26/3969\) and \(E_9=326843/86704128\), so \(L_9-E_9=723407/260112384>0\). Hence \(L_n>E_n\) for every \(n\ge9\), proving strict positivity without assuming the sign from computation. Finally, the correction in (1) is \(O(n\,2^{-n})\), giving the stated asymptotic law. \(\square\)

## Verification

The standalone standard-library Python program `verify.py` computes coefficients independently using integer rational-function recurrences, checks formulas (4), (5), and (1) for sizes \(1\le n\le240\), exhaustively enumerates all compositions for \(1\le n\le13\), and checks the exact sign bound. It passed 1,218 exact assertions. The infinite-size sign theorem follows from the displayed monotone bound, not the finite test range. To replay, run `python3 verify.py`.

## Relationship to prior work

Heubach and Mansour (2003) established a general joint generating function marking rises, levels, drops, and part count for compositions; that earlier result determines all rise–fall mixed moments in principle and is **not claimed to be new here**. Their explicit ordinary-composition specialization and Chinn–Grimaldi–Heubach's earlier work give marginal rise and fall counts. Brennan and Knopfmacher (2009) determine one-sided ascent moments and asymptotic behavior. Bender and Canfield (2005) establish general asymptotic normality for locally restricted compositions with covariance matrices of linear scale. Kong's work on rise/fall distributions of random sequences also gives broader joint enumeration machinery. The contribution assessed here is the **exact all-size sign boundary, its explicit exponentially controlled formula, and its direct three-pattern proof**. The full joint enumerators can in principle be differentiated to recover the covariance; however, the inspected results do not state or prove the strict negative-to-positive transition at \(n=9\). This priority assessment is not independent certification.

## Limitations

This is a derived structural inequality about a special marginal of a known broader joint distribution, not a new general rise–fall enumerator or multivariate limit theorem. The claim relies on elementary symbolic identities verified by independent coefficient checks; the displayed proof, not a finite experiment, is the infinite-range evidence. Literature priority could be affected by older specific moment-product computations not inspected in full, especially the 2003 Fibonacci Quarterly paper of Chinn, Grimaldi, and Heubach, or other applications of the complete 2003 joint generating function. No independent mathematical audit was performed.

## References

- S. Heubach and T. Mansour, *Counting rises, levels, and drops in compositions*, arXiv:math/0310197 (first posted 14 October 2003). https://arxiv.org/abs/math/0310197
- E. A. Bender and E. R. Canfield, *Locally Restricted Compositions I. Restricted Adjacent Differences*, Electronic Journal of Combinatorics **12** (2005), R57. https://www.combinatorics.org/ojs/index.php/eljc/article/view/v12i1r57
- C. Brennan and A. Knopfmacher, *The distribution of ascents of size d or more in compositions*, DMTCS **11** (2009), 1–10. https://dmtcs.episciences.org/en/articles/462
- Y. Kong, *Joint distribution of rises, falls, and number of runs in random sequences*, arXiv:2405.01748 (2024 open manuscript of earlier published work). https://arxiv.org/abs/2405.01748
