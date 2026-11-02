# Catalan composition law and Gaussian universality index for Dyck words

## Finding

Write \(\mathcal D_n\) for the set of Dyck words of semilength \(n\) on \(\{0,1\}\), with \(0\) an opening and \(1\) a closing parenthesis. For any word \(w\), let \(\iota(w)\) be the largest integer \(k\ge0\) such that **every** binary word of length \(k\) is an order-preserving scattered subsequence of \(w\). Put \(a_{n,k}=|\{w\in\mathcal D_n:\iota(w)=k\}|\), and take \(\mathcal D_0=\{\varepsilon\}\). Let \(C(t)=\sum_{j\ge0}\frac{1}{j+1}\binom{2j}{j}t^j\) be the Catalan generating function.

**Complete joint enumeration.** As a formal power series in \(t\), with polynomial coefficients in \(u\),

\[
\boxed{\sum_{n\ge0}\sum_{k=0}^n a_{n,k}t^n u^k
=C\!\left(\frac{tu(1-tu)}{1-t}\right).}
\]

Equivalently, with \(z\) marking the number of completed greedy arches and \(x\) the defect \(n-k\),

\[
\boxed{\sum_{k,d\ge0}a_{k+d,k}z^k x^d
=C\!\left(\frac{z(1-z)}{1-x}\right).}
\]

In particular, for \(1\le k\le n\), writing \(d=n-k\) and \(C_j=\binom{2j}{j}/(j+1)\), an exact finite coefficient formula is

\[
a_{n,k}=\sum_{j=\lceil k/2\rceil}^{k}(-1)^{k-j}C_j
\binom{j}{k-j}\binom{j+d-1}{d}.
\]

Here \(a_{0,0}=1\), while \(a_{n,0}=0\) for \(n>0\). For example, \(a_{n,n}=1\) for all \(n\ge0\); for \(n\ge2\), \(a_{n,n-1}=2^{n-1}-1\); and for \(n\ge4\),

\[
a_{n,n-2}=\left(\binom n2-1\right)2^{n-4}.
\]

**Macroscopic regime.** If \(W_n\) is uniform on \(\mathcal D_n\), then

\[
\mathbb E\,\iota(W_n)=\frac23n+O(1),\qquad
\operatorname{Var}(\iota(W_n))=\frac4{27}n+O(1),
\]

and, as \(n\to\infty\),

\[
\frac{\iota(W_n)-2n/3}{\sqrt{4n/27}}
\ \xrightarrow{\mathrm{d}}\ \mathcal N(0,1).
\]

The algebraic joint law, its finite coefficient expression and the Gaussian limit form a single enumeration theorem for the same statistic.

## Assumptions and scope

A Dyck word of semilength \(n\) contains exactly \(n\) zeros and \(n\) ones and every prefix has at least as many zeros as ones. Distinct indexed words are counted separately, with no rotation, reversal, complement, or tree-isomorphism quotient. The subsequence alphabet is the full binary alphabet even for the empty word, whose universality index is zero. The generating-function equations are formal; the probabilistic limit refers to uniform Dyck words, not Dyck factors of an infinite automatic sequence. Binomial coefficients outside their ordinary nonnegative range are zero.

## Proof

**1. Greedy arch decomposition.** The standard arch-factorization theorem says that \(\iota(w)\) equals the number of successive shortest prefixes containing both letters, removing each completed prefix and repeating; what remains is unary (or empty). For a binary alphabet each completed arch is uniquely \(0^{s+1}1\) or \(1^{s+1}0\), with \(s\ge0\). The former increases the parentheses height by \(s\), the latter decreases it by \(s\). Within a \(1^{s+1}0\) arch the height reaches its minimum immediately before the terminal zero, so such an arch starting at height \(h\) is admissible exactly when \(h-s\ge1\). A \(0^{s+1}1\) arch is admissible at any nonnegative height. The two zero-displacement arches \(01\) and \(10\) are distinct; only \(01\) is allowed at height zero.

The unfinished suffix of a nonempty Dyck word, if nonempty, consists entirely of ones, because every nonempty Dyck word ends in a one. If the completed arches end at height \(h\), that suffix must be exactly \(1^h\). Conversely, any finite sequence of the arches satisfying the height restrictions, followed by this forced suffix, constructs a unique Dyck word and recovers exactly its greedy decomposition. (At zero height the empty suffix is allowed.)

Let \(U\) be the sum of \(s\) over rising arches and \(D\) the sum over falling arches. The height after all arches is \(h=U-D\). With \(k\) completed arches the total word length is \(2k+U+D+h=2k+2U\). Hence its semilength satisfies the fundamental **defect identity**

\[
\boxed{n-\iota(w)=U.}
\]

Thus positive increments in the arch-height path, not the number of returns or peaks of the original Dyck path, mark the defect.

**2. Exact arch-height equations.** Let \(F_h(z,x)\), for \(h\ge0\), count all admissible sequences of future arches from height \(h\), followed by the uniquely determined all-one closing suffix; mark each arch by \(z\) and each positive height increment \(s\) by \(x^s\). For \(h\ge1\), a first arch can be either of two level arches, an upward jump of arbitrary size, or a downward jump to any positive height. Therefore

\[
F_h=1+z\left(2F_h+\sum_{s\ge1}x^sF_{h+s}
+\sum_{j=1}^{h-1}F_j\right),\qquad h\ge1,
\]

while

\[
F_0=1+z\left(F_0+\sum_{s\ge1}x^sF_s\right).
\]

These equations have unique solutions as formal power series in \(z\) with coefficients in \(\mathbb Q[[x]]\): the coefficient of each positive power of \(z\) depends only on coefficients of smaller \(z\)-degree. The constant term is one at every height.

Set \(F_h=(r-1)r^{h-1}/z\) for \(h\ge1\), where \(r(0,x)=1\). Substitution into the first recurrence yields

\[
1=z\left(2+\frac{xr}{1-xr}+\frac{1}{r-1}\right),
\]

or, after clearing denominators,

\[
\boxed{x(1-z)r^2-(1+x-2z)r+(1-z)=0.}
\]

The branch with \(r(0,x)=1\) exists uniquely as a formal \(z\)-series over \(\mathbb Q[[x]]\); furthermore \((r-1)/z\) is a power series with constant term one, so the substitution is valid. The height-zero equation gives

\[
F_0=\frac{1-x}{(1-z)(1-xr)}.
\]

Solving the quadratic using the same branch, and simplifying the discriminant

\[
(1+x-2z)^2-4x(1-z)^2=(1-x)\bigl(1-x-4z(1-z)\bigr),
\]

produces

\[
F_0=\frac{2}{1+\sqrt{1-4z(1-z)/(1-x)}}
=C\!\left(\frac{z(1-z)}{1-x}\right).
\]

By the defect identity, \(F_0\) is precisely the joint generating function asserted above. Substituting \(z=tu\) and \(x=t\) gives the semilength/index form. Expanding \(C\) and using the binomial theorem twice yields the finite coefficient formula. Coefficients at fixed defects one and two come from

\[
[x]F_0=\frac{z}{(1-z)(1-2z)},\qquad
[x^2]F_0=\frac{z(1-z)}{(1-2z)^3}.
\]

The zero-defect case has \([x^0]F_0=1/(1-z)\). At \(u=1\), the joint law specializes to \(C(t)\), recovering the ordinary Catalan count.

**3. Gaussian limit.** Put \(T(t,u)=tu(1-tu)/(1-t)\), so the bivariate generating function is \(C(T(t,u))\). Uniformly for complex \(u\) sufficiently close to one, its unique dominant singularity in \(t\) is the analytic solution near \(1/4\) to \(4T(t,u)=1\):

\[
\rho(u)=\frac{4u+1-\sqrt{8u+1}}{8u^2},\qquad \rho(1)=\frac14.
\]

The other root of this quadratic and the possible pole of \(T\) remain near \(t=1\), so they do not interfere locally. Since the Catalan square-root singularity is nondegenerate, with \(c(u)=4\rho(u)\partial_tT(\rho(u),u)\) analytic and \(c(1)=1\), uniform singularity transfer gives

\[
[t^n]C(T(t,u))=\frac{\sqrt{c(u)}}{\sqrt\pi}
\rho(u)^{-n}n^{-3/2}(1+O(n^{-1})),
\]

uniformly in a complex neighborhood of \(u=1\). Consequently the probability generating functions for \(\iota(W_n)\) satisfy the standard analytic quasi-powers hypotheses. The logarithmic mean and variance slopes are

\[
-\left.\left(u\frac{d}{du}\right)\log\rho(u)\right|_{u=1}=\frac23,
\qquad
-\left.\left(u\frac{d}{du}\right)^2\log\rho(u)\right|_{u=1}=\frac4{27}>0.
\]

The quasi-powers central-limit theorem proves the stated normal limit and the first two moment estimates. The derivatives can also be checked directly from \(4u^2\rho^2-(4u+1)\rho+1=0\), giving \(\rho'(1)=-1/6\) and \(\rho''(1)=13/54\).

## Verification

The included dependency-free `verify.py` enumerates all 290,512 Dyck words with semilength at most 12, computes universality indices directly, and compares their distributions with the Catalan coefficient formula. Independently it counts arch-height paths with bounded defect using a transition dynamic program, checks every cell with at most 18 arches and defect at most 8, verifies both near-maximal closed forms through semilength 64, and checks the singularity derivative constants by exact rational arithmetic. It returns `VERIFY_OK` (390 grouped assertions). These checks are finite evidence, not a substitute for the full formal-series and analytic proof.

## Relationship to prior work

Schnoebelen and Veron (2023) establish arch factorization and related algorithms for arbitrary words; Adamson (2023) and Adamson et al. (2023) count subsequence-universal words under unconstrained or regular-language assumptions. Mol, Rampersad, and Shallit (2023) investigate *Dyck factors occurring inside automatic sequences*, rather than all Dyck words indexed by their scattered-subsequence universality. These results provide the natural context, not the displayed joint Catalan composition or Gaussian law.

A closely related pre-existing Dyck arch-defect result already supplies a uniform **fixed-defect** finite-matrix rationality theorem and explicit formulas for defects zero through three. The small-defect formulas here are confirmations and are **not presented as new**. The statement proved here is different in scope: one algebraic expression jointly enumerates **all** indices and defects without a defect-dependent matrix and gives the growing-index normal limit with exact slopes. Fixed-defect rationality by itself neither states this global composition nor supplies the large-defect asymptotics. The equivalence of the present formula to every individual coefficient obtained from a previous matrix is expected because both count the same Dyck statistic; the new contribution is the uniform closed evaluation and probabilistic regime. Whether an equivalent all-defect identity is implicit in more general lattice-path results remains a literature risk.

## Limitations

The formula counts the ordinary Dyck language, not other Catalan encodings with an unrelated pathwise statistic. Normality is for a uniformly chosen Dyck word, not for arbitrary restricted or nonuniform sources. The theorem does not claim a local limit, a large-deviation principle, or independent validation. Prior literature and database searches cannot establish universal uniqueness; a stronger, unlocated generating-function theorem could subsume it. The proof requires the usual analytic quasi-powers result for the probabilistic corollary; no finite experiment establishes that limit.

## References

[1] Ph. Schnoebelen and J. Veron, *On Arch Factorization and Subword Universality for Words and Compressed Words*, arXiv:2304.11932 (first posted 2023-04-24), https://arxiv.org/abs/2304.11932.

[2] D. Adamson, *Ranking and Unranking k-subsequence universal words*, arXiv:2304.04583 (first posted 2023-04-10), https://arxiv.org/abs/2304.04583.

[3] L. Mol, N. Rampersad, and J. Shallit, *Dyck Words, Pattern Avoidance, and Automatic Sequences*, arXiv:2301.06145 (first posted 2023-01-15), https://arxiv.org/abs/2301.06145.

[4] D. Adamson, P. Fleischmann, A. Huch, T. Koß, F. Manea, and D. Nowotka, *k-Universality of Regular Languages*, arXiv:2311.10658 (first posted 2023-11-17), https://arxiv.org/abs/2311.10658.

[5] P. Flajolet and R. Sedgewick, *Analytic Combinatorics*, Cambridge University Press, 2009, Chapters VI and IX (standard singularity transfer and quasi-powers arguments).
