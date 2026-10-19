# Exact optimizer multiplicities for tight Fourier sampling on prime-power cycles

## Finding
Let \(p\) be a prime, \(k\ge 1\), \(N=p^k\), and \(A\ne\varnothing\) be any subset of \(\mathbb Z/N\mathbb Z\). The unnormalized Fourier characters indexed by a set \(B\subseteq\mathbb Z/N\mathbb Z\) restrict to a tight frame on \(\mathbb C^A\) if their row Gram matrix is a scalar multiple of the identity. Define
\[
R(A)=\{v_p(a-a'):a,a'\in A,\ a\ne a'\},\qquad
J(A)=\{k-1-v:v\in R(A)\}\subseteq\{0,\dots,k-1\}.
\]
For a singleton \(A\), both sets are empty. Write \(r=|J(A)|\), and put
\[
E_p(J)=\sum_{\substack{0\le j<k\\j\notin J}}p^{|J\cap\{0,\ldots,j-1\}|},\qquad
s(J)=\begin{cases}0,&J=\{0,\ldots,k-1\},\\1+\max(\{0,\ldots,k-1\}\setminus J),&\text{otherwise}.\end{cases}
\]
Then the optimum cardinality is \(p^r\), and **all** optimal frequency sets \(B\) are exactly those whose least-significant-first base-\(p\) prefix tree has \(p\) children at every occupied node in every level \(j\in J(A)\), and exactly one child at every occupied node in every other level. In particular the exact number of distinct optimal frequency sets, with frequencies not ordered, is
\[
\boxed{M_p(A)=p^{E_p(J(A))}.}
\]
Every such optimal set has translation stabilizer \(p^{s(J(A))}\mathbb Z/N\mathbb Z\); consequently the number of frequency-translation orbits of optimizers is exactly
\[
\boxed{T_p(A)=p^{E_p(J(A))-s(J(A))}.}
\]
Both counts depend only on the set of \(p\)-adic valuations of nonzero spatial differences, not their multiplicities or locations.

## Assumptions and scope
The characters are \(\chi_b(a)=\exp(2\pi i ab/N)\), for distinct frequency indices \(b\), with counting measure on \(A\) and no frequency weights. A \(p\)-ary prefix at depth \(j\) is the residue of a frequency modulo \(p^j\); a child corresponds to choosing its digit at position \(j\), counting from position zero at the least significant digit. All counts are of subsets, not ordered lists or multiplicities. For \(|A|=1\), every singleton \(B\) is optimal, giving \(M_p(A)=N\) and \(T_p(A)=1\). If \(J(A)\) is the full level set, the unique optimizer is the whole frequency group, and both counts equal one.

For example, if \(A=\{0,p^{k-1}\}\) and \(k\ge2\), then \(J(A)=\{0\}\). There are \(p^{p(k-1)}\) distinct optimal two-character frames, and \(p^{p(k-1)-k}\) translation orbits. Thus a fixed smallest admissible frame size can coexist with rapidly growing optimizer diversity.

## Proof
Let \(\zeta=\exp(2\pi i/N)\) and \(P_B(X)=\sum_{b\in B}X^b\). The restricted Fourier evaluation matrix has row Gram entries \(P_B(\zeta^{a-a'})\). Consequently its Gram matrix is \(|B|I\) precisely when \(P_B(\zeta^d)=0\) for every nonzero spatial difference \(d\). Since \(\zeta^d\) has order \(p^{k-v_p(d)}\), this condition is equivalent to \(\Phi_{p^{j+1}}\mid P_B\) for all \(j\in J(A)\), where \(\Phi\) denotes the cyclotomic polynomial.

Fix \(j\in J(A)\). Reduce \(P_B\) modulo \(X^{p^{j+1}}-1\): the coefficient of \(X^{a+tp^j}\), for \(0\le a<p^j\) and \(0\le t<p\), is the number of frequencies whose first \(j+1\) digits agree with \(a+tp^j\). Since \(\Phi_{p^{j+1}}=1+X^{p^j}+\cdots+X^{(p-1)p^j}\), divisibility is equivalent to these \(p\) coefficients being equal for each fixed \(a\). This equivalence follows by polynomial division: after reducing degrees below \(p^{j+1}\), the quotient by the monic cyclotomic polynomial has degree below \(p^j\), so exactly the equal-coefficient vectors occur.

At each required depth \(j\), every occupied prefix has at least one descendant of each of its \(p\) child types, because the child counts are positive and equal. Therefore the number of occupied prefixes is multiplied by at least \(p\) at that level, and at least preserved elsewhere. At depth \(k\), there are \(|B|\) occupied leaves. Thus \(|B|\ge p^r\), with equality forcing exactly \(p\) children per occupied parent at all levels in \(J(A)\) and exactly one at all other levels. Conversely, a prefix tree with precisely this pattern has, at each required depth, the same number \(p^{|J(A)\cap\{j+1,\dots,k-1\}|}\) of final leaves under each child. Hence the coefficient-count equalities above hold and \(B\) is a tight frame. This proves both optimality and complete characterization of equality.

Immediately before level \(j\) the tree has \(p^{|J(A)\cap\{0,\dots,j-1\}|}\) occupied parents. If \(j\notin J(A)\), each parent independently chooses one of \(p\) child digits; if \(j\in J(A)\), the choices are forced to include all \(p\) digits. Multiplying the independent choices yields \(M_p(A)=p^{E_p(J(A))}\).

Let \(s=s(J(A))\). Every digit level \(j\ge s\) is compulsory, so each optimizer is a union of complete residue classes modulo \(p^s\), and translation by \(p^s\) stabilizes it. If \(s>0\), the level \(s-1\) is not compulsory, so every occupied prefix there has only one rather than all \(p\) children. Hence \(B\) cannot be invariant under translation by \(p^{s-1}\), which would force the entire coset \(p^{s-1}\mathbb Z/N\mathbb Z\) to be included with every occupied point. Because all subgroups of \(\mathbb Z/N\mathbb Z\) are nested, the full stabilizer is exactly \(p^s\mathbb Z/N\mathbb Z\). Each translation orbit thus has \(p^s\) members. Division of \(M_p(A)\) by \(p^s\) gives the stated orbit count, including the full-group case \(s=0\).

## Verification
The accompanying `verify.py` tests every one of the \(2^k\) possible required-level profiles, directly enumerating every nonempty frequency subset for the moduli \(2,4,8,3,9,5\). It verifies the complete mask-vanishing criterion, optimum cardinality, and exact counting formula. The arithmetic uses integers only and does not rely on floating-point Fourier cancellation. The analytic proof, not finite enumeration, establishes the theorem for arbitrary primes, exponents, and spatial subsets.

## Relationship to prior work
The minimal frequency count \(p^{|R(A)|}\), the cyclotomic Gram criterion, and one canonical optimal frequency set were already established in *Minimum tight exponential-frame size on cyclic prime-power groups*; none of those facts is claimed as new. Aihua Fan, Shilei Fan, and Ruxi Shi characterized \(p\)-homogeneous spectral sets and their spectra in \(\mathbb Z/p^k\mathbb Z\). Their Theorem 5.1 is a substantial structural precursor, and after passing to a homogeneous spatial model with the same difference valuation scales, it also explains the tree structure of extremizers. The precise extension singled out here is the **multiplicity law for optimal redundant tight-frame frequency sets for an arbitrary prescribed \(A\)** and the uniform translation-orbit count, with explicit dependence on every compulsory and free digit level. These enumerative statements were not found in the inspected results, but they are derived by combining the known frameworks with elementary branching counts.

Lam and Leung's vanishing-sums theorem supplies related root-of-unity background; their 1995 preprint does not concern optimal frame enumerations. The counting formula can be viewed as an enumerative refinement of the established spectral homogeneity theory, rather than a new characterization of spectral sets or a new proof of the minimal frame size.

## Limitations
All results concern unweighted, distinct Fourier characters on cyclic prime-power groups. This theorem does not enumerate nonminimal tight frames, weighted rules, optimal numerical conditioning beyond exact tightness, or non-prime-power cyclic groups. It is a modest exact enumerative refinement of prior p-adic homogeneity and minimum-size results; originality depends on the absence of an earlier equivalent counting formula, especially in the finite harmonic-frame and spectral-set literature.

## References
1. T. Y. Lam and K. H. Leung, *On vanishing sums for roots of unity*, arXiv:math/9511209 (first submitted 1995-11-13).
2. A. Fan, S. Fan and R. Shi, *Compact Open Spectral Sets in \(\mathbb Q_p\)*, arXiv:1511.04837 (first submitted 2015-11-16), in particular Theorem 5.1 on spectra and \(p\)-homogeneous trees.
3. *Minimum tight exponential-frame size on cyclic prime-power groups*, publicly available mathematical research record (2026), exact minimum and a canonical optimizer; https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-minimum-tight-exponential-frame-size-on-cyclic-prime-power-group--b7a941dc4a7d .
