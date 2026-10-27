# Sharp entropy gap for periodically switching binary-cylinder holes

## Finding
Fix an integer \(p\geq1\). At time \(i\), remove one dyadic interval of length \(1/4\) from the doubling map \(T(x)=2x\pmod1\), using a \(p\)-periodic schedule. Write the forbidden two-bit word at phase \(i\) as \(w_i=a_ic_i\), with \(a_i,c_i\in\{0,1\}\), and indices taken modulo \(p\). Define the **defect count**
\[
k=\#\{i\in\{0,\ldots,p-1\}:c_i=a_{i+1}\}.
\]
Let \(h\) denote the survivor's topological entropy **per one iteration**, and \(\gamma\) the Lebesgue escape rate, so that \(\gamma=\log 2-h\). Put
\[
r_p=\frac{p+\sqrt{p^2+4}}2.
\]

**Sharp periodic-hole dichotomy.** For every \(p\) and every one of the \(4^p\) schedules:

1. \(h=0\) if and only if \(k=0\). These are exactly \(2^p\) schedules. Their finite-time Lebesgue survival probability, after avoiding holes at times \(0,\ldots,n-1\), is **exactly**
\[
\Pr(\text{survive }n\text{ tests})=\frac{n+2}{2^{n+1}}\qquad(n\geq0).
\]
The two-sided phase-labelled survivor has exactly two periodic orbits for the time-\(p\) map; every other two-sided orbit is a one-transition connection between them. Its time-\(p\) dynamical zeta function is \((1-z)^{-2}\).

2. If \(k\geq1\), then the time-\(p\) survivor transition graph is primitive and
\[
\boxed{\quad h\geq\frac{\log r_p}{p}>0,\qquad
\gamma\leq\log2-\frac{\log r_p}{p}.\quad}
\]
**Equality holds if and only if \(k=1\).** Exactly \(p2^p\) schedules attain the smallest positive entropy. Their time-\(p\) dynamical zeta function is
\[
\zeta(z)=\frac1{1-pz-z^2}.
\]
In particular, no period-\(p\) schedule has an escape rate strictly between \(\log2-(\log r_p)/p\) and \(\log2\). The minimum positive survivor Hausdorff dimension is \((\log r_p)/(p\log2)\); zero-defect survivors have dimension zero.

For orientation, at \(p=2\) the sixteen schedules split into four with entropy zero, eight with entropy \(\frac12\log(1+\sqrt2)\), and four with entropy \(\log((1+\sqrt5)/2)\). The corresponding time-two zeta functions are \((1-z)^{-2}\), \((1-2z-z^2)^{-1}\), and \((1-3z+z^2)^{-1}\).

## Assumptions and scope
Represent each \(x\in[0,1)\) by its canonical binary expansion, terminating with zeros at dyadic rationals. Define the half-open dyadic cylinders \(H_{00}=[0,1/4)\), \(H_{01}=[1/4,1/2)\), \(H_{10}=[1/2,3/4)\), and \(H_{11}=[3/4,1)\). At time \(i\), the hole is \(H_{w_{i\bmod p}}\). The closed symbolic survivor consists of binary sequences \((b_j)_{j\geq0}\) avoiding \(b_jb_{j+1}=w_{j\bmod p}\) at every \(j\). Its two-sided extension is invariant under the \(p\)-fold shift. Topological entropy \(h\) is normalized per original doubling-map time step, not per \(p\)-block. The zeta function refers to the two-sided, phase-zero survivor under the \(p\)-fold shift. Endpoint identifications in the interval model form a countable set and do not affect entropy, Lebesgue escape probabilities, or Hausdorff dimension. The periodic-orbit statement is for the symbolic system, avoiding ambiguity at dyadic endpoints.

## Proof
**1. Exact finite-state model.** For a forbidden word \(w=ab\), let \(A_w\) be the binary \(2\times2\) matrix with \((u,v)\) entry equal to \(1\) unless \((u,v)=(a,b)\). Paths through the matrices \(A_{w_0},\ldots,A_{w_{p-1}}\), repeated periodically, are precisely the admissible binary strings. If \(M=A_{w_0}\cdots A_{w_{p-1}}\), then the number of allowed strings of length \(n+1\) is \((1,1)A_{w_0}\cdots A_{w_{n-1}}(1,1)^{\mathsf T}\). All four individual matrices are unimodular and have neither zero row nor zero column. Periodic transfer-matrix growth gives \(h=(\log\rho(M))/p\), and the fair-Bernoulli dyadic partition gives \(\gamma=\log2-h\).

**2. Time-dependent binary gauge.** Write \(w_i=a_ic_i\) and replace each observed bit by \(y_i=b_i\mathbin{\mathrm{xor}}a_{i\bmod p}\). The forbidden transition in gauge coordinates begins with zero. It ends with one if \(c_i\ne a_{i+1}\), and with zero if \(c_i=a_{i+1}\). Thus the transformed phase matrix is respectively
\[
L=\begin{pmatrix}1&0\\1&1\end{pmatrix},\qquad
F=\begin{pmatrix}0&1\\1&1\end{pmatrix}.
\]
Writing \(Q_i\) for the identity or swap according to \(a_i\), we have \(Q_iA_{w_i}Q_{i+1}\in\{L,F\}\). Since \(Q_p=Q_0\), the original monodromy is similar to a product of exactly \(p-k\) matrices \(L\) and \(k\) matrices \(F\), in the original cyclic order.

**3. Zero-defect rigidity.** If \(k=0\), all forbidden transitions in the gauge are \(01\), so a surviving one-sided gauge string has the form a (possibly empty or infinite) string of ones followed by zeros. Exactly \(n+2\) length-\(n+1\) prefixes are possible. Multiplying their dyadic cylinder measure \(2^{-(n+1)}\) proves the asserted survival formula. The transfer product is \(L^p=\begin{psmallmatrix}1&0\\p&1\end{psmallmatrix}\), with spectral radius one. In the bi-infinite gauge, all paths are the two constant sequences or a single descending step at some integer position; the two constant sequences give all periodic points of the time-\(p\) map, and \(\#\operatorname{Fix}(\sigma^{pm})=2\) for every \(m\geq1\). The zeta function is \(\exp(\sum_{m\geq1}2z^m/m)=(1-z)^{-2}\).

**4. Strict positivity and sharp minimization.** Every product containing \(F\) has both off-diagonal entries positive and its bottom-right entry positive: begin with \(L^a\), multiply by the first \(F\), and verify inductively that subsequent right multiplication by \(L\) or \(F\) preserves these properties. Hence each such product is a primitive nonnegative matrix. In any cyclic product with at least two occurrences of \(F\), a cyclic rotation exposes a subword \(FL^aF\), for some integer \(a\geq0\). The exact identity
\[
FL^aF-L^{a+1}F=\begin{pmatrix}1&a\\0&0\end{pmatrix}\ne0
\]
shows that replacing that subword by \(L^{a+1}F\) weakly decreases every matrix entry, strictly somewhere, while preserving word length and reducing the number of \(F\)'s by one. Nonnegative unimodular matrices on the two sides preserve a nonzero positive difference. Both old and new products are primitive, so strict Perron–Frobenius comparison yields a strictly smaller spectral radius. Cyclic rotation preserves spectral radius because the factors are invertible. Iterating produces a word with exactly one \(F\); every such word is cyclically conjugate to \(FL^{p-1}\). The latter is
\[
FL^{p-1}=\begin{pmatrix}p-1&1\\p&1\end{pmatrix},
\qquad \det(FL^{p-1})=-1,\qquad\operatorname{tr}(FL^{p-1})=p.
\]
Its Perron root is precisely \(r_p\), the positive root of \(\lambda^2-p\lambda-1=0\). Consequently all \(k\geq1\) products have spectral radius at least \(r_p>1\), and strict inequality holds when \(k\geq2\). This proves both the zero-entropy equivalence and the sharp gap and equality classification.

**5. Schedule multiplicities and periodic points.** Choose the \(p\) first bits \(a_i\) freely. For each prescribed defect subset \(D\subseteq\{0,\ldots,p-1\}\), the second bits are uniquely fixed by \(c_i=a_{i+1}\) for \(i\in D\) and \(c_i=1-a_{i+1}\) otherwise. Therefore exactly \(2^p\binom pk\) labelled schedules have \(k\) defects. The \(p\)-step labelled graph has adjacency matrix \(M\) and exactly \(\operatorname{tr}(M^m)\) fixed points for its \(m\)-th iterate. Hence its Artin–Mazur zeta function is \(1/\det(I-zM)\). In the one-defect case, the matrix above gives \((1-pz-z^2)^{-1}\). Primitivity when \(k\geq1\) also gives uniqueness of the time-\(p\) measure of maximal entropy. For \(k=0\) the only invariant probabilities are mixtures of the two constant gauge sequences. Standard graph-directed dyadic cylinder dimension bounds give \(\dim_H=h/\log2\) for the forward survivor: the primitive case uses the Perron growth of its dyadic cylinders, while the countable zero-defect case has dimension zero.

## Verification
Run `python3 verify.py`. This standalone standard-library checker independently constructs all sixteen original transition choices and their integer monodromies, then checks every schedule of periods \(1\) through \(7\), altogether \(21{,}844\) schedules. It confirms their gauge conjugacies, determinants, exact zero- and one-defect characteristic polynomials, schedule multiplicities, and numerically separates the two-or-more-defect Perron roots from the sharp bound. For periods at most three, it additionally compares transfer counts with direct enumeration of every binary prefix through nine positions and directly counts periodic points through ten positions, checking their equality to traces of monodromy powers. These finite checks do not prove the all-period result; the explicit matrix comparison and gauge argument above do.

## Relationship to prior work
Livorati, Georgiou, Dettmann and Leonel, *Escape through a time-dependent hole in the doubling map* (arXiv:1312.7030, first posted 2013-12-25), investigate moving and breathing holes through numerical transfer/Ulam approximations and overlap corrections. Their specified oscillatory-boundary family and escape-rate estimates do not state the present sharp discrete-cylinder classification or its \(p\)-dependent first-positive-entropy gap. Cheriyath and Agarwal, *Subshifts of Finite Type with a Hole* (arXiv:1905.11767, first posted 2019-05-28), study time-independent unions of forbidden cylinders through correlation polynomials and Perron theory; those static-hole statements do not give a classification of periodically changing single cylinders. General transfer-matrix and Perron–Frobenius principles are used here, not claimed as new. A complete implication comparison against unindexed periodic-forbidden-word work remains a historical-priority limitation.

## Limitations
The theorem requires a binary doubling map and a single half-open length-\(1/4\) cylinder at each phase. For multiple cylinders, longer forbidden words, nonperiodic schedules, and nonuniform initial distributions, no analogous gap is asserted. The elementary lower-bound argument is specific to the two matrices arising after the binary gauge. Reported originality is conditional on searched and inspected sources; the known general transfer-matrix formalism makes historical priority for an equivalent specialization a residual risk. No independent audit has been performed.

## References
1. A. L. P. Livorati, O. Georgiou, C. P. Dettmann and E. D. Leonel, *Escape through a time-dependent hole in the doubling map*, arXiv:1312.7030, first submitted 2013-12-25, https://arxiv.org/abs/1312.7030 .
2. H. Cheriyath and N. Agarwal, *Subshifts of Finite Type with a Hole*, arXiv:1905.11767, first submitted 2019-05-28, https://arxiv.org/abs/1905.11767 .
3. L. A. Bunimovich and A. Yurchenko, *Where to place a hole to achieve a maximal escape rate*, Israel Journal of Mathematics 182 (2011), 229–252. Background on static binary holes.
