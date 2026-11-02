# Complete preimage spectra of a Frobenius-perturbed square over quadratic finite fields

## Finding

For every odd prime power \(q\), write \(K=\mathbb F_{q^2}\), and define \(F:K\to K\) by \(F(x)=x^2+x^q\). For each integer \(r\ge 0\), let \(N_r\) denote the number of \(y\in K\) for which \(F(x)=y\) has exactly \(r\) distinct solutions \(x\in K\). Put \(m=q+1\) and \(g=\gcd(3,m)\). There are no fibers larger than four, and the complete distribution is

\[
\begin{aligned}
N_0&=\frac{3(q^2-1)}8,\\
N_1&=\frac{2q^2+q+5-2g}6,\\
N_2&=\frac{(q-1)^2}4+g-1,\\
N_3&=\frac{q+1-2g}2,\\
N_4&=\frac{q^2-4q-5+8g}{24}.
\end{aligned}
\]

Consequently,
\[
|F(K)|=\frac{5q^2+3}8.
\]

The total image size is independent of \(g\), while the multiplicities of fibers of sizes one through four retain a cubic-residue distinction.

## Assumptions and scope

The field \(\mathbb F_q\) has arbitrary **odd** characteristic, including \(3\); \(K/\mathbb F_q\) is its unique quadratic extension. Exponents use the \(q\)-power Frobenius on \(K\), so \(x^{q^2}=x\). Define the norm-one group \(U=\{u\in K^\times:u^{q+1}=1\}\), which is cyclic of order \(m=q+1\). The quantity \(g\) is the number of solutions of \(u^3=1\) in \(U\). The counts \(N_r\) classify **targets**, not elements in the domain.

## Proof

**1. No fiber has five points.** Suppose \(F(x)=y\). Then \(x^q=y-x^2\); raise to the \(q\)-th power and use \(x^{q^2}=x\):
\[
x=y^q-(y-x^2)^2.
\]
Thus every preimage is a root of the monic quartic
\[
P_y(X)=X^4-2yX^2+X+y^2-y^q.
\]
It has at most four distinct roots. Also, if a fiber has four points, their sum is zero, since the cubic coefficient vanishes.

**2. Exact ordered collision pairs.** For distinct \(x,z\in K\), set \(h=x-z\ne0\). The equality \(F(x)=F(z)\) is equivalent to
\[
x+z=-h^{q-1}.
\]
Since the characteristic is odd, \(h\) gives exactly one ordered solution pair,
\[
x=\frac{h-h^{q-1}}2,\qquad z=\frac{-h-h^{q-1}}2.
\]
Conversely the displayed pair has the claimed difference and common image. Hence the number of ordered distinct collision pairs is exactly \(q^2-1\):
\[
\sum_{r=0}^4 r(r-1)N_r=q^2-1.
\tag{1}
\]

**3. Parametrize triples using the norm-one group.** Let \(x,y,z\) be pairwise distinct preimages of one target, and set
\[
\alpha=x+y,\quad \beta=x+z,\quad \gamma=y+z.
\]
By the pair relation above, \(\alpha,\beta,\gamma\in U\), and they are pairwise distinct. Since \(\beta-\gamma=x-y\), we have
\[
-\alpha=(\beta-\gamma)^{q-1}=-\frac1{\beta\gamma},
\]
using \(u^q=u^{-1}\) for \(u\in U\). Therefore \(\alpha\beta\gamma=1\).

Conversely, any ordered pairwise distinct \(\alpha,\beta,\gamma\in U\) with product one gives
\[
x=\frac{\alpha+\beta-\gamma}2,\quad
y=\frac{\alpha+\gamma-\beta}2,\quad
z=\frac{\beta+\gamma-\alpha}2.
\]
Their differences are nonzero, and their pairwise sums are \(\alpha,\beta,\gamma\). For example, since \(x-y=\beta-\gamma\) and \(\alpha\beta\gamma=1\), we have \[(x-y)^{q-1}=-1/(\beta\gamma)=-\alpha=-(x+y).\] The same computation for the other two pairs proves that all three points share one image. This is a bijection between ordered distinct preimage triples and ordered distinct product-one triples in \(U\).

There are \(m^2\) ordered product-one triples without the distinctness condition. Each equality of two coordinates occurs in \(m\) triples; all three equality events intersect in exactly \(g\) triples (solutions of \(u^3=1\)). By inclusion-exclusion the number of distinct-coordinate triples is
\[
T=m^2-3m+2g=6N_3+24N_4.
\tag{2}
\]

**4. Identify exactly which triples extend to four points.** Given such a triple, let \(w=-(x+y+z)\), the only possible fourth root distinct from \(x,y,z\) by Step 1. Note that
\[
w-x=-(\alpha+\beta),\qquad w+x=-\gamma.
\]
If \(\alpha+\beta\ne0\), then
\[
(w-x)^{q-1}=(\alpha+\beta)^{q-1}=\frac1{\alpha\beta}=\gamma=-(w+x),
\]
so \(F(w)=F(x)\). The analogous equalities hold for \(y,z\). Thus, if none of \(\alpha,\beta,\gamma\) are opposite, \(w\) is a new fourth preimage. If one pair is opposite, \(w\) coincides with one of the existing points; no distinct fourth preimage can exist by the quartic. Since the three coordinates are distinct, at most one opposite pair occurs.

Count bad ordered triples with \(\alpha=-\beta\). Their product condition forces \(\gamma=-\alpha^{-2}\). This coordinate is distinct from \(\alpha\) and \(-\alpha\) precisely when \(\alpha^3\ne-1\) and \(\alpha^3\ne1\). The two excluded equations each have \(g\) solutions in \(U\), and the solutions are disjoint in odd characteristic. Hence there are \(m-2g\) possibilities for this designated opposite pair, and \(3(m-2g)\) bad ordered triples altogether. Every size-three fiber accounts for \(3!=6\) bad triples, while size-four fibers account for none. Therefore
\[
6N_3=3(m-2g),\qquad N_3=\frac{m-2g}2.
\]
Substitute into (2):
\[
N_4=\frac{m^2-6m+8g}{24}.
\]

**5. Recover the remaining counts.** From (1),
\[
N_2=\frac{q^2-1-6N_3-12N_4}2
=\frac{(q-1)^2}4+g-1.
\]
The mass identity \(\sum rN_r=q^2\) gives \(N_1=q^2-2N_2-3N_3-4N_4\). Finally \(\sum N_r=q^2\) gives \(N_0=N_2+2N_3+3N_4\). Substitution yields the stated formulae and \(q^2-N_0=(5q^2+3)/8\). All counts are integers because the argument counts finite sets directly. \(\square\)

## Verification

The standalone \(\texttt{verify.py}\) exhaustively evaluates \(F\) using two-field-element coordinates \(x=u+v\sqrt d\), for a nonsquare \(d\in\mathbb F_q\). In these coordinates,
\[
F(x)=(u^2+dv^2+u)+(2u-1)v\sqrt d.
\]
The program constructs \(\mathbb F_q\) directly for prime \(q\), and as a quadratic extension of the prime field for tested square orders. It counts every target multiplicity and compares all five categories with the formulas, independently of the collision-pair and triple proof. Run \(\texttt{python verify.py}\) using Python 3. The executed check covered 19 odd prime-power field sizes (including \(9,25,49\)), 19,859 domain elements, and all corresponding target fibers; no mismatch occurred. Finite tests are corroboration, not the proof of the unrestricted theorem.

## Relationship to prior work

Mullen--Wan--Wang (arXiv:1210.8119) prove general upper bounds for multivariate finite-field polynomial value sets; their Theorem 2.1 is not an exact spectrum for this quadratic-extension map. Qin--Hong (arXiv:1303.2229) give criteria and constructions for permutation polynomials involving linearized and trace expressions; their main results do not state the nonpermutation fiber multiplicities calculated here. Both are relevant context, not assertions of novelty by themselves. Exact-expression, coordinate-equivalence, and value-set searches did not locate a dominating result, but this absence is not a proof of novelty.

## Limitations

The classification is specific to \(F(x)=x^2+x^q\) on quadratic extensions in odd characteristic. It does not describe all polynomial maps of comparable degree, provide individual preimage lists for each target, or assert analogous formulas in characteristic two. Broader historical literature on finite-field polynomial-map fiber distributions may contain an equivalent reformulation not identified by the searches. Independent verification has not been performed.

## References

1. Gary L. Mullen, Daqing Wan, and Qiang Wang, *Value sets of polynomial maps over finite fields*, arXiv:1210.8119v1 (first posted 2012-10-30), https://arxiv.org/html/1210.8119v1.
2. Xiaoer Qin and Shaofang Hong, *Constructing permutation polynomials over finite fields*, arXiv:1303.2229 (first posted 2013-03-09), https://arxiv.org/pdf/1303.2229.
