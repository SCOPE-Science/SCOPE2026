# Strict likelihood-ratio ordering of same-part distances in complete-bipartite uniform spanning trees

## Finding

Fix integers \(a>b\ge 2\). Sample a uniform spanning tree of the simple complete bipartite graph \(K_{a,b}\), with vertex classes \(A\) and \(B\). Write \(J_A=D_A/2\) and \(J_B=D_B/2\), where \(D_A\) and \(D_B\) are the tree distances between fixed distinct vertices in \(A\) and \(B\), respectively. The laws are marginal; no coupling is assumed.

**Theorem.** \(J_B<_{\mathrm{lr}}J_A\): the ratio \(\Pr(J_A=j)/\Pr(J_B=j)\) is strictly increasing on their common positive support \(1\le j\le b-1\), and \(\Pr(J_A=b)>0=\Pr(J_B=b)\). In particular \(\Pr(J_A\ge j)>\Pr(J_B\ge j)\) for every integer \(2\le j\le b\), and \(\mathbb E\phi(D_A)>\mathbb E\phi(D_B)\) for every strictly increasing real function \(\phi\). If \(a=b\ge2\), the two laws coincide by symmetry.

## Known distance law used in the proof

For integers \(a\ge2,b\ge1\), put \(M=\min(a-1,b)\). The same-part tail for endpoints in the part of size \(a\) is
\[
S_A(j)=\Pr(J_A\ge j)=\prod_{i=1}^{j-1}\frac{(a-i-1)(b-i)}{ab},\qquad 1\le j\le M+1,
\]
with empty product \(1\) and zero tail for \(j>M+1\). The mass is \(S_A(j)-S_A(j+1)\). These formulas follow from the prescribed-tree inclusion theorem of Ge and Dong and are recorded explicitly in *A complete one-crossing law for marked distances in bipartite uniform spanning trees*. For completeness, a path with \(j+1\) vertices of \(A\) and \(j\) of \(B\) has inclusion probability \([ab-(a-j-1)(b-j)]/(a^j b^{j+1})\). For two fixed endpoints there are \((a-2)_{\underline{j-1}}(b)_{\underline j}\) such paths, where \((x)_{\underline k}\) is the falling factorial. Their inclusion events are disjoint because a tree has a unique path between its endpoints. The sum is the difference of the displayed successive products, and the last product vanishes at \(M+1\). The \(B\)-law uses exchanged class sizes when \(b\ge2\).

## Proof of the ordering

Set \(C_j=j(a+b-j-1)\) and \(p_A(j)=\Pr(J_A=j)\), \(p_B(j)=\Pr(J_B=j)\). Subtracting successive tails gives \(p_A(j)=S_A(j)(C_j+b)/(ab)\) and \(p_B(j)=S_B(j)(C_j+a)/(ab)\). Thus on the common support,
\[
\frac{p_A(j)}{p_B(j)}=
\left[\prod_{i=1}^{j-1}\frac{(a-i-1)(b-i)}{(b-i-1)(a-i)}\right]\frac{C_j+b}{C_j+a}.
\]
For each adjacent comparison \(1\le j\le b-2\), the newly appended factor has positive denominator and numerator exceeding it by \(a-b\). The last quotient increases strictly, since it increases in \(C_j\) and \(C_{j+1}-C_j=a+b-2j-2>0\) in this range. At \(j=b\), only the larger class has positive mass. This proves the stated strict order, including \(b=2\), where the common support is a single point and strictness comes from the extra positive mass.

For \(2\le j\le b\), the upper-tail probability at \(j\) is strictly larger on the \(A\)-side: each existing product factor for \(A\) exceeds the corresponding factor for \(B\) when the latter is positive, and the \(B\)-tail at \(b\) is zero while the \(A\)-tail is positive. Summation by parts gives the strict expectation inequality. The likelihood-ratio theorem gives more than tail order: even after restriction to a common distance window, the odds of one specified higher distance versus one lower distance in the common support are larger for endpoints in the larger class.

## Verification and scope

The unchanged `verify.py` checks both the known laws and the strict adjacent likelihood-ratio minors with rational arithmetic for \(2\le a\le30, 1\le b\le30\) (the latter where \(a>b\ge2\)). It separately enumerates spanning trees on \(K_{a,b}\) for \(2\le a,b\le4\). For instance on \(K_{4,3}\) the masses are \((2/3,11/36,1/36)\) versus \((3/4,1/4,0)\), with increasing common-support ratios \(8/9<11/9\). Finite checks illustrate the all-size argument; they do not prove it. The theorem concerns the uniform spanning-tree law, not a minimum or nonuniform weighted spanning tree or a general bipartite host.

## Relationship to prior work

Ge–Dong, Theorem 1.4, and Dong–Ge, Theorem 4, give respectively the prescribed-tree and more general prescribed-forest counts. The exact individual mass and tail formulas are prior and are not part of the originality claim. *A complete one-crossing law for marked distances in bipartite uniform spanning trees* explicitly gives those laws and proves a stochastic comparison across **different** complete bipartite hosts of fixed total size when the marked part is at least as large as its complement. That theorem neither compares anchor classes within one unbalanced host nor asserts likelihood-ratio order. The present contribution is only the strict within-host cross-class likelihood-ratio theorem. Equivalent priority elsewhere has not been ruled out.

## References

- J. Ge and F. Dong, *Spanning trees in complete bipartite graphs and resistance distance in nearly complete bipartite graphs*, Theorem 1.4, https://arxiv.org/abs/1904.07766.
- F. Dong and J. Ge, *Counting spanning trees in a complete bipartite graph which contain a given spanning forest*, Theorem 4, https://arxiv.org/abs/2103.05294.
- *A complete one-crossing law for marked distances in bipartite uniform spanning trees*, https://github.com/Resultary/2026/blob/main/2026/10/26/SCOPE-a-complete-one-crossing-law-for-marked-distances-in-bipartite-un--50939acd9f27/RESULT.md.
