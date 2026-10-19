# The complete mixed parabola–quartic convolution spectrum over odd finite fields

## Finding

Let \(F=\mathbb F_q\) be any finite field of characteristic at least five. Consider the parabola and quartic graph
\[
A=\{(t,t^2):t\in F\},\qquad B=\{(u,u^4):u\in F\}\subset F^2.
\]
For \((s,y)\in F^2\), let \(r(s,y)\) count the ordered representations \((s,y)=a+b\) with \(a\in A\) and \(b\in B\). Let \(N_j=\#\{(s,y):r(s,y)=j\}\). The only possible multiplicities are \(j=0,1,2,3,4\), and **all five exact counts** are as follows. Write \(\chi:F\to\{-1,0,1\}\) for the quadratic character with \(\chi(0)=0\), and put \(\alpha=\chi(2)\), \(\beta=\chi(-2)\), \(\gamma=\chi(-6)\):
\[
\begin{aligned}
N_0&=\frac{3q^2-2q+1-\alpha q-\beta}{8},\\
N_1&=\frac{2q^2+3q-5+2\alpha q-2\gamma}{6},\\
N_2&=\frac{q^2-2q+7-\alpha q+3\beta+4\gamma}{4},\\
N_3&=\frac{q-3-2\beta-2\gamma}{2},\\
N_4&=\frac{q^2-6q+11+\alpha q+9\beta+8\gamma}{24}.
\end{aligned}
\]
In particular,
\[
|A+B|=\frac{5q^2+2q-1+\alpha q+\beta}{8},\qquad
\sum_{s,y}r(s,y)^2=2q^2-q.
\]
There are no four-representation targets over \(\mathbb F_5\); at least one such target exists in **every eligible finite field of order \(q\ge7\)**. Thus the first fourfold fiber occurs over \(\mathbb F_7\), where \((N_0,N_1,N_2,N_3,N_4)=(16,21,9,2,1)\).

## Assumptions and scope

The sums and products are in \(F\), which may have arbitrary extension degree. Ordered representations count the ordered choice of the parabola point followed by the quartic point, not unordered pairs from one common set. Both curves contain the origin and have exactly \(q\) distinct points. All formulas use counting measure; the final Fourier identity uses the **unnormalized** additive Fourier transform. The characteristic restriction ensures that \(2\), \(3\), and \(4\) are nonzero, and that a quartic has at most four distinct roots.

## Proof

**Reduction to quartic root counts.** The first coordinate of a representation forces \(t=s-u\). Hence \(r(s,y)\) is the number of roots in \(F\) of
\[
H_{s,y}(X)=X^4+X^2-2sX+(s^2-y).
\]
In particular, \(0\le r\le4\). Write \(S_k=\sum_{s,y}\binom{r(s,y)}{k}\) for \(k=1,2,3,4\). Then \(S_k=\sum_{j=k}^4\binom jk N_j\).

**The first two factorial moments.** Every \((t,u)\in F^2\) gives one representation at exactly one target, so \(S_1=q^2\). If two distinct roots \(u\ne v\) of \(H_{s,y}\) share their target, subtracting their equations gives
\[
2s=u^3+u^2v+uv^2+v^3+u+v.
\]
This determines \(s\) uniquely and then determines \(y\). Every unordered pair of distinct field elements therefore belongs to exactly one common target, whence \(S_2=\binom q2\).

**An exact quadratic-form count.** For later use, let \(Q_m\) be a nondegenerate quadratic form in \(m\) variables over \(F\), with matrix determinant \(d\) modulo squares. For \(c\ne0\), the standard Gauss-sum computation gives
\[
\#\{x\in F^2:Q_2(x)=c\}=q-\chi(-d),\qquad
\#\{x\in F^3:Q_3(x)=c\}=q^2+\chi(-cd)q.
\]
Indeed, Fourier-invert the indicator of \(Q_m(x)=c\); diagonalizing \(Q_m\) makes the nontrivial Fourier coefficients products of quadratic Gauss sums. The Gauss identities \(G(\psi)^2=\chi(-1)q\) and \(\sum_{t\ne0}\chi(t)\psi(ct)=\chi(c)G(\psi)\) yield both stated formulas. No numerical approximation is involved.

**Three-root fibers.** For any three roots \(u,v,w\) of a depressed monic quartic with fixed quadratic coefficient \(1\), the fourth root in the algebraic closure equals \(-u-v-w\). Vieta's formula for the second symmetric sum therefore gives
\[
Q(u,v,w):=u^2+v^2+w^2+uv+uw+vw=-1.
\]
Conversely, any three *distinct* elements obeying this identity uniquely determine \(s\) and \(y\) for which all are roots: take \(s\) from the third elementary symmetric sum of the four roots and \(s^2-y\) from their product. The matrix of \(Q\) has determinant \(1/2\), so the number of all ordered triples (repetitions allowed) satisfying \(Q=-1\) is \(q^2+\alpha q\). For a specified equality between two variables, the residual binary form has determinant \(2\), hence has \(q-\beta\) solutions. The all-equal triples satisfy \(6u^2=-1\), with \(1+\gamma\) solutions. Inclusion–exclusion gives the number of ordered triples with distinct entries,
\[
D_3=q^2+\alpha q-3(q-\beta)+2(1+\gamma)
=q^2+(\alpha-3)q+2+3\beta+2\gamma.
\]
Each three-element subset of roots can be ordered six ways, so \(S_3=D_3/6\).

**Four-root fibers.** Four *distinct* roots \(u_1,u_2,u_3,u_4\) form the full root set of some \(H_{s,y}\) if and only if
\[
\sum_{i=1}^4u_i=0,\qquad\sum_{i=1}^4u_i^2=-2.
\]
The equivalence uses the missing cubic coefficient and the fixed quadratic coefficient \(1\); the lower coefficients uniquely determine \(s,y\). Eliminate \(u_4=-u_1-u_2-u_3\). The remaining condition is again \(Q(u_1,u_2,u_3)=-1\), giving \(q^2+\alpha q\) ordered quadruples before distinctness is imposed.

Apply the partition-lattice inclusion–exclusion sieve to their equality patterns. There are six partitions of type \((2,1,1)\), each contributing \(-(q-\beta)\), three partitions of type \((2,2)\), each contributing \(+(1+\beta)\), and four partitions of type \((3,1)\), each contributing \(+2(1+\gamma)\). These subsidiary equations are, respectively, a binary form of determinant \(2\), the equation \(u^2=-1/2\), and the equation \(u^2=-1/6\). The all-equal pattern is impossible, because \(4u=0\) forces \(u=0\), inconsistent with the nonzero quadratic sum. Hence the number of ordered all-distinct quadruples is
\[
\begin{aligned}
D_4&=q^2+\alpha q-6(q-\beta)+3(1+\beta)+8(1+\gamma)\\
&=q^2+(\alpha-6)q+11+9\beta+8\gamma.
\end{aligned}
\]
Every fourfold target corresponds to exactly one unordered root set, so \(N_4=D_4/24\) and \(S_4=N_4\).

**Inversion and consequences.** Invert the triangular system
\[
S_k=\sum_{j=k}^4\binom jkN_j\quad(k=1,2,3,4),\qquad\sum_{j=0}^4N_j=q^2.
\]
Substituting \(S_1=q^2\), \(S_2=q(q-1)/2\), \(S_3=D_3/6\), and \(S_4=D_4/24\) yields exactly the five displayed formulas. In particular, \(\sum r^2=S_1+2S_2=2q^2-q\), and \(|A+B|=q^2-N_0\). For \(q=5\), the \(N_4\) formula gives zero. At \(q=7\) it gives one. For \(q\ge11\), the bound \(\alpha,\beta,\gamma\ge-1\) yields \(24N_4\ge q^2-7q-6>0\). There is no intermediate eligible field size between \(5\) and \(7\), so the claimed sharp onset follows.

## Verification

Run the self-contained standard-library script `verify.py` with Python 3, in the same directory as this file. It independently evaluates every target's exact root multiplicity using finite-field arithmetic and compares the five resulting counts with the formulas, checks all four moment identities, and reports one line per field. `verification_output.txt` records the reproduced output. Tested fields are \(\mathbb F_p\) for thirteen primes \(p\in\{5,7,11,13,17,19,23,29,31,37,41,43,47\}\), together with \(\mathbb F_{25}\), \(\mathbb F_{49}\), and \(\mathbb F_{121}\). The verification samples do not substitute for the proof over all eligible finite fields.

With \(\widehat{h}(\xi)=\sum_{x\in F^2}h(x)\overline{\psi(\langle x,\xi\rangle)}\), the Parseval identity also gives the exact mixed fourth Fourier moment
\[
q^{-2}\sum_{\xi\in F^2}|\widehat{1_A}(\xi)|^2|\widehat{1_B}(\xi)|^2=2q^2-q,
\]
which is distinct from an unrestricted sharp bilinear extension norm.

## Relationship to prior work

The sharp finite-field extension framework of González-Riquelme and Oliveira e Silva motivates examining exact convolution fibers. Its stated extremal theorems concern self-convolution of particular quadratic surfaces and the parabola's sixth moment, rather than this mixed parabola–quartic count. Nguyen's two-moment subset-sum theorem supplies an important nearby counting framework; its displayed exact Theorem 2.11 evaluates the **zero** first and second moment target, whereas the distinct-four-root component here has prescribed moments \((0,-2)\). The later work of Lai–Marino–Robinson–Wan provides an algorithm for higher-moment subset-sum *existence*, not this complete Fourier-convolution multiplicity histogram. Published quartic self-energy and fifth-power self-convolution calculations likewise have different objects and do not imply the five counts here. Possible other explicit nonzero-target moment-subset formulas remain an originality risk.

## Limitations

The theorem concerns **unweighted**, ordered mixed convolution only, not sharp operator norms for arbitrary complex weights and not the individual locations of each multiplicity class. The displayed formulas depend on the three quadratic characters but do not enumerate each target within a class. Characteristic \(2\) or \(3\) requires different analysis. There is no claim of independent validation or of uniqueness among all published but possibly unindexed equivalent classifications.

## References

1. C. González-Riquelme and D. Oliveira e Silva, *Sharp extension inequalities on finite fields*, arXiv:2405.16647 (initial public preprint 26 May 2024), https://arxiv.org/pdf/2405.16647.
2. J. Nguyen, *Higher Moments Subset Sum Problem over Finite Fields*, doctoral dissertation, University of California, Irvine (2019), https://escholarship.org/uc/item/2cr0w697.
3. T. Lai, A. Marino, A. Robinson and D. Wan, *Moment subset sums over finite fields*, arXiv:1910.05894 (2019), https://arxiv.org/pdf/1910.05894.
