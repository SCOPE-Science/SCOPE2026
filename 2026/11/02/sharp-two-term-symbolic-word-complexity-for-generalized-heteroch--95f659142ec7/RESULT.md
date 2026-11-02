# Sharp two-term symbolic-word complexity for generalized heterochaos baker maps

## Finding

For every integer \(m\ge 2\) and every \(0<a<1/m\), let \(A_m(n)\) be the number of distinct admissible length-\(n\) itineraries of the generalized two-dimensional heterochaos baker map, in its natural \(2m\)-rectangle alphabet, and put \(A_m(0)=1\). This is independent of \(a\). Define the unique formal power series \(g_m(t)\) with zero constant term solving
\[
g_m(t)=t+mt\,g_m(t)^2,
\qquad
 g_m(t)=\frac{1-\sqrt{1-4mt^2}}{2mt}.
\]
Then the exact ordinary generating function is
\[
\boxed{\sum_{n\ge0}A_m(n)t^n
 =\frac{1-g_m(t)}{(1-(m+1)t)(1-mg_m(t))}.}
\]
Its sharp two-term asymptotic is
\[
\boxed{A_m(n)=(m+1)^n\left(\frac{(m-1)^2}{m(m+1)}n+\frac{m+1}{m}\right)
 +O_m\!\left(\frac{(2\sqrt m)^n}{n^{3/2}}\right).}
\]
The error statement concerns \(n\to\infty\); it is not a claim of an explicit universal numerical error bound for small \(n\). In the original four-symbol case \(m=2\),
\[
 A_2(n)=3^n\left(\frac n6+\frac32\right)
 +O\!\left(\frac{(2\sqrt2)^n}{n^{3/2}}\right),
\qquad
\frac{A_2(n)}{A_2(n-1)}=3+\frac3n+O(n^{-2}).
\]
In particular, the asymptotic ratio proposed from numerical evidence in the original heterochaos paper follows with a quantitative justification. This is not a new claim for the already known entropy \(\log(m+1)\).

## Assumptions and scope

Fix \(m\ge2\), \(a\in(0,1/m)\), and \((u,v)\in[0,1]^2\). The fully branched base map is
\[
\tau_a(u)=\begin{cases}
(u-(i-1)a)/a,& (i-1)a\le u<ia,\quad 1\le i\le m,\\
(u-ma)/(1-ma),&ma\le u\le1.
\end{cases}
\]
The skew map has branches
\[
 F_a(u,v)=\begin{cases}
(\tau_a(u),(v+i-1)/m),& (i-1)a\le u<ia,\quad 1\le i\le m,\\
(\tau_a(u),mv-j+1),&ma\le u\le1,\ (j-1)/m\le v<j/m,\quad 1\le j\le m.
\end{cases}
\]
The first kind is labeled \(\alpha_i\) and the second \(\beta_j\). An admissible word is a finite label string realized by a point whose first \(n\) iterates lie in the corresponding branch interiors; the same finite-word language is obtained from the standard closure of the coding space. Boundary ties do not affect the finite-word count. The source's coding theorem identifies the language with the \(m\)-bracket Dyck shift: an \(\alpha_i\) pushes type \(i\), and a \(\beta_j\) must match the most recent unmatched push if there is one; when there is none, any \(j\) is permitted. We also verify this finite-word rule directly from the affine branches.

## Proof

**1. An exact skeleton enumeration.** Replace each \(\beta_j\) by a single unlabeled pop \(B\), retaining the \(m\) labeled pushes. For a skeleton \(w\) of length \(n\), let \(S_k(w)\) be the number of \(B\)'s minus the number of pushes among the first \(k\) symbols, \(S_0=0\), and set \(H_n(w)=\max_{0\le k\le n}S_k(w)\). Reading a word from left to right, every pop with an unmatched push must equal that push's label. A pop with no unmatched push can have any of \(m\) labels, independently. Such free pops occur precisely when \(S_k\) makes a new strict record, and their number is \(H_n\). Consequently the number of admissible typings above a fixed skeleton is exactly \(m^{H_n(w)}\), so
\[
 A_m(n)=\sum_{w\in\{\alpha_1,\ldots,\alpha_m,B\}^n}m^{H_n(w)}.
\]
This is a bijective count: a mismatched typed pop is forbidden, while every nonmismatched finite word is realized. Indeed, any prescribed base-branch skeleton gives a nonempty open interval of base coordinates, because every base branch maps onto the whole interval. The vertical affine dynamics encodes an \(m\)-ary stack. A finite consistent specification imposes finitely many digit constraints, leaving a nonempty open vertical cylinder after avoiding finitely many partition boundaries. Thus no formal word counted above is spurious.

**2. First-passage generating function.** Make the skeleton uniformly random, giving each push \(\alpha_i\) probability \(1/(m+1)\) and the generic pop \(B\) probability \(1/(m+1)\). Then \(S_k\) is a walk with upward probability \(p=1/(m+1)\) and downward probability \(q=m/(m+1)\). Let \(\tau_r\) be the first time this walk reaches level \(r\), with \(\tau_r=\infty\) if not reached, and let \(f(z)=\mathbb E[z^{\tau_1};\tau_1<\infty]\). First-step decomposition gives
\[
 f(z)=pz+qz f(z)^2,
 \qquad f(0)=0.
\]
Translation invariance and the strong Markov property imply \(\mathbb E[z^{\tau_r};\tau_r<\infty]=f(z)^r\), for every positive integer \(r\). The identity
\[
 m^{H_n}=1+(m-1)\sum_{r=1}^{\infty}m^{r-1}\mathbf1_{\{\tau_r\le n\}}
\]
therefore yields, initially as formal power series,
\[
 U(z):=\sum_{n\ge0}\frac{A_m(n)}{(m+1)^n}z^n
 =\frac{1}{1-z}\left(1+(m-1)\sum_{r\ge1}m^{r-1}f(z)^r\right)
 =\frac{1-f(z)}{(1-z)(1-mf(z))}.
\]
Substitution \(z=(m+1)t\) and \(g_m(t)=f((m+1)t)\) proves the displayed exact generating function.

**3. Pole and branch-point analysis.** The solution analytic at zero is
\[
 f(z)=\frac{1-\sqrt{1-4pqz^2}}{2qz}.
\]
For \(m\ge2\), the closest square-root branch points are \(z=\pm(m+1)/(2\sqrt m)\), both strictly farther than \(1\) from zero. At \(z=1\),
\[
 f(1)=1/m,\qquad
 f'(1)=\frac{m+1}{m(m-1)},\qquad
 f''(1)=\frac{2(m+1)(3m-1)}{m(m-1)^3}.
\]
Consequently
\[
 U(z)=\frac{(m-1)^2}{m(m+1)}\frac1{(1-z)^2}
 +\frac4{m+1}\frac1{1-z}+R(z).
\]
On its analytic branch, \(1-mf(z)\) has only the zero \(z=1\), and \(1-z\) has no other zero. After the pole terms are subtracted, \(R\) has no singularities inside the two square-root branch points and has local singular expansions beginning with a square-root term at each of them. The usual binomial-coefficient estimate for the coefficients of a square-root singularity gives
\[
 [z^n]R(z)=O_m\!\left(\left(\frac{2\sqrt m}{m+1}\right)^n n^{-3/2}\right).
\]
Since \([z^n](1-z)^{-2}=n+1\), and
\[
 \frac{(m-1)^2}{m(m+1)}+\frac4{m+1}=\frac{m+1}{m},
\]
the two-term asymptotic follows. Dividing its \(m=2\) consecutive instances gives the stated ratio expansion (the remaining error is exponentially smaller relative to the main term).

## Verification

The standalone `verify.py` runs with standard Python 3 and no dependencies. It independently (a) exhausts typed bracket words using a stack, (b) counts free-pop choices via a skeleton dynamic program, and (c) extracts coefficients directly from the formal generating-function equation. It checks agreement for \(m=2,3,4\), including every typed word through lengths \(8,6,5\), respectively, and integer generating-function coefficients through length \(12\). The output is `VERIFY_OK: 61 integer equalities; m in 2..4`. In particular the first counts for \(m=2\) are \(1,4,14,48,160,528,1720,5568,17888,57216,182080\), for lengths \(0\) through \(10\). These finite tests cross-check the combinatorics, but the all-\(m\), all-\(n\) generating function and asymptotics follow from the argument above, not from enumeration.

## Relationship to prior work

Saiki, Takahasi and Yorke [1, Appendix B, Figure 9] numerically observed the asymptotic ratio \(3+3/n\) for the original four-symbol map and conjectured entropy \(\log3\). The entropy itself, and the symbolic identification with the Dyck shift, are already known: Takahasi and Yamamoto [2, Theorem A, Section 2] prove the coding identification in the generalized family, and Saiki et al. [3, Sections 1 and 3] review this and the existing maximal-entropy theory. The present claim is restricted to the exact finite-language generating function and its sharp two-term asymptotic, including the original numerical ratio. The cited 2015 and 2021 Dyck-shift orbit-counting papers [4,5] concern *periodic points and closed orbits*, which are not interchangeable with finite admissible words. Neither those inspected sections nor the inspected model papers assert the boxed language enumerator. Their coding and entropy statements alone do not state its precise linear coefficient or additive term.

## Limitations

The formula counts symbolic words, not distinct geometric points or periodic trajectories; many points can realize the same itinerary. It is uniform in the geometric parameter \(a\) only within \(0<a<1/m\). No extension to discontinuous perturbations or arbitrary skew fibers is claimed. The combinatorial method uses standard first-passage and algebraic-function tools. Publication priority is not independently certified: a previously unindexed enumeration of Dyck-shift word complexity might subsume this precise result even though the investigated sources do not. The proof has not undergone independent validation.

## References

1. Y. Saiki, H. Takahasi, J. A. Yorke, *Piecewise-linear maps with heterogeneous chaos*, arXiv:1811.01009, first posted 2018-11-02, especially Appendix B. https://arxiv.org/abs/1811.01009
2. H. Takahasi, K. Yamamoto, *Heterochaos baker maps and the Dyck system: maximal entropy measures and a mechanism for the breakdown of entropy approachability*, arXiv:2209.04905, first posted 2022-09-11, especially Theorem A and Section 2. https://arxiv.org/abs/2209.04905
3. Y. Saiki, H. Takahasi, K. Yamamoto, J. A. Yorke, *The dynamics of the heterochaos baker maps*, arXiv:2401.00836, first posted 2024-01-01, especially Sections 1 and 3. https://arxiv.org/abs/2401.00836
4. *Estimates on the number of orbits of the Dyck shift*, Journal of Inequalities and Applications, 2015. https://doi.org/10.1186/s13660-015-0899-6
5. A. Nordin and M. S. Md Noorani, *Orbit Growth of Shift Spaces Induced by Bouquet Graphs and Dyck Shifts*, Mathematics 9 (2021), 1268. https://doi.org/10.3390/math9111268
