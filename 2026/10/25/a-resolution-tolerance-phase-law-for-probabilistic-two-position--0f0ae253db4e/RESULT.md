# A resolution–tolerance phase law for probabilistic two-position composite-DNA GC constraints

## Finding

For a positive integer \(k\geq2\), a resolution-\(k\) composite DNA symbol is a four-tuple of nonnegative integers \((a,c,g,t)\) summing to \(k\). Its synthesized base is sampled independently at each position, with probabilities \(a/k,c/k,g/k,t/k\). Let \(C_k(\varepsilon)\) be the number of bits per composite symbol obtainable from arbitrarily long sequences for which, in **every pair of adjacent positions**, the probability that precisely one synthesized base is G or C is at least \(1-\varepsilon\). No other constraints are imposed.

For \(0\leq\varepsilon<1/2\), put
\[
W_k(m)=\sum_{i=0}^{m}(i+1)(k-i+1)
=\frac{(m+1)(m+2)(3k+3-2m)}6.
\]
Then the exact finite-resolution capacity obeys the uniform bounds
\[
\boxed{\ W_k(\lfloor k\varepsilon/2\rfloor)
\leq 2^{C_k(\varepsilon)}
\leq W_k(\lfloor k\varepsilon\rfloor).\ }
\]
In particular, for **all** \(k\geq2\) and \(0\leq\varepsilon<1/2\),
\[
\boxed{\ \frac{k}{24}(1+k\varepsilon)^2
\leq 2^{C_k(\varepsilon)}
\leq 2k(1+k\varepsilon)^2.\ }
\]
Consequently, the bounded-error resolution law is
\[
C_k(\varepsilon)=\log_2 k+2\log_2(1+k\varepsilon)+O(1),
\]
with an absolute implied constant, uniform in \(k\) and \(\varepsilon\) in the indicated range. In particular, for any fixed \(c>0\) and \(\alpha>0\), with \(\varepsilon_k=c k^{-\alpha}\),
\[
\boxed{\ \lim_{k\to\infty}\frac{C_k(\varepsilon_k)}{\log_2 k}
=3-2\min\{\alpha,1\}.\ }
\]
For any fixed \(0<c<1/2\), the ratio also tends to \(3\) when \(\varepsilon_k=c\).

There is an **exact onset threshold**: for every \(k\geq2\) and \(0\leq\varepsilon<1/k\),
\[
2^{C_k(\varepsilon)}=k+1.
\]
At \(\varepsilon=1/k\), for every \(k\geq3\),
\[
\boxed{\ 2^{C_k(1/k)}
=\frac{k+1+\sqrt{(k+1)(9k+1)}}2.\ }
\]
Thus the gain in capacity at the first nonzero tolerance threshold approaches exactly **one bit per composite symbol** as \(k\to\infty\).

## Assumptions and scope

The synthesis choices at different positions are independent; the constraint is imposed separately at every adjacent pair, not on the probability of simultaneous success across the whole strand. Every composite symbol is distinguished by its full four-tuple; distinct A/T or G/C compositions with the same total GC probability remain distinct alphabet symbols. This is the exact-balanced case of a window of length two, with accepted synthesized GC count exactly one. Logarithms in capacity are base two. Capacity is a blocklength asymptotic at each fixed \(k,\varepsilon\), followed where stated by a separate resolution limit \(k\to\infty\). The scope excludes \(\varepsilon\geq1/2\), supplementary biochemical constraints, and any error-correction or sequencing model.

## Proof

**1. GC-bin reduction and exact transfer capacity.** A symbol's GC-bin is \(i=c+g\), with \(0\leq i\leq k\); exactly
\[
b_i=(i+1)(k-i+1)
\]
distinct composite symbols occupy bin \(i\). For adjacent bins \(i,j\), the probability of a valid synthesized pair is
\[
s_k(i,j)=\frac{i(k-j)+(k-i)j}{k^2}.
\]
Define the nonnegative \((k+1)\)-by-\((k+1)\) matrix
\[
T_{ij}=b_j\,\mathbf1\{s_k(i,j)\geq1-\varepsilon\}.
\]
The number of allowed length-\(n\) composite sequences is \(\sum_i b_i (T^{n-1}\mathbf1)_i\). Its exponential growth is the spectral radius \(\rho(T)\): the initial and terminal vectors are strictly positive, so the maximum nonnegative irreducible component contributes to this scalar at its own spectral rate. Hence \(2^{C_k(\varepsilon)}=\rho(T)\). Alternatively, this is the fixed-parameter transfer-matrix principle already present in the cited probabilistic GC coding literature; the results below are new quantitative analysis of its resolution-dependent matrices.

**2. Allowed transitions lie in narrow opposite tails.** When \(\varepsilon<1/2\), bins lying on the same side of \(k/2\) cannot be adjacent in an admissible pair, because the probability of exactly one GC draw is at most \(1/2\). Write the lower bin probability as \(p=i/k\leq1/2\), the upper as \(1-h=j/k\geq1/2\), with \(0\leq h\leq1/2\). Their failure probability is
\[
f(p,h)=p+h-2ph.
\]
Since \(f(p,h)\geq p\) and \(f(p,h)\geq h\), an admissible transition must have \(i\leq\lfloor k\varepsilon\rfloor\) on the lower side and \(j\geq k-\lfloor k\varepsilon\rfloor\) on the upper side. Every row sum of \(T\) is therefore at most \(W_k(\lfloor k\varepsilon\rfloor)\), proving the spectral upper bound.

**3. A complete bipartite admissible subgraph.** Put \(m=\lfloor k\varepsilon/2\rfloor\). Every pair between lower bins \(0,\ldots,m\) and upper bins \(k-m,\ldots,k\) satisfies \(f(p,h)\leq p+h\leq\varepsilon\). The corresponding induced transfer matrix contains both directions of a complete bipartite weighted graph. Its weighted total on each side is \(W_k(m)\), by symmetry \(b_i=b_{k-i}\). Its spectral radius is exactly \(W_k(m)\). Monotonicity of the spectral radius for nonnegative matrices proves the lower bound.

**4. Uniform estimates and the singular scaling law.** The closed form of \(W_k(m)\) follows by summing \((i+1)(k-i+1)\). As \(m\leq\lfloor k/4\rfloor\) in the lower bound, direct summation gives \(W_k(m)\geq3k(m+1)^2/8\). Also \(\lfloor k\varepsilon/2\rfloor+1\geq(1+k\varepsilon)/3\). Therefore the lower spectral bound is at least \(k(1+k\varepsilon)^2/24\). For the upper bound, \(W_k(m)\leq(k+1)(m+1)^2\leq2k(1+k\varepsilon)^2\). Taking logarithms proves the uniform approximation. Substituting \(\varepsilon_k=c k^{-\alpha}\) yields \(1+2(1-\alpha)_+=3-2\min\{\alpha,1\}\) as the coefficient of \(\log_2 k\). Fixed \(c\in(0,1/2)\) yields coefficient \(3\).

**5. First tolerance jump.** If \(\varepsilon<1/k\), the tail restriction in step 2 leaves only the two extreme bins \(0,k\), joined in both directions; each has multiplicity \(k+1\), so \(\rho(T)=k+1\). If \(k\geq3\) and \(\varepsilon=1/k\), direct substitution into \(f\) shows the only admissible pairs of distinct bins are \((0,k),(0,k-1),(1,k)\) and reversals. The pair \((1,k-1)\) has failure \(2/k-2/k^2>1/k\). Symmetrizing \(T\) with diagonal bin weights gives a four-vertex weighted path whose outer edge weights are \(\sqrt{2k(k+1)}\) and whose middle edge weight is \(k+1\); unused bins are isolated. The largest eigenvalue of this path is the positive root of
\[
\lambda^2-(k+1)\lambda-2k(k+1)=0,
\]
which is the asserted formula. Dividing by \(k+1\) shows the onset growth-factor ratio tends to \(2\), hence the capacity jump tends to \(\log_2 2=1\) bit.

## Verification

`composite_resolution_verify.py` is a standalone Python 3 script using exact rational arithmetic for transition admissibility, directly enumerating composite symbols and all valid short words, checking the weighted transfer recurrence, confirming the tail formula and complete-bipartite witnesses for resolutions 2 through 60, and numerically checking the first-jump spectral identity. Run `python3 composite_resolution_verify.py` from the directory containing this document and script; the expected final line begins `VERIFY_OK`. These finite checks corroborate the proof but do not themselves justify its all-parameter quantifiers. The proof's induction-free inequalities and explicit four-vertex spectral calculation do that.

## Relationship to prior work

Bodur, Walter, and Wachter-Zeh (2026) introduced the \(\varepsilon\)-probabilistic composite-DNA GC framework and the general finite-state capacity formula for fixed constraint parameters. The present result takes their exact-balanced two-position case and proves **uniform, resolution-dependent** lower and upper capacity bounds, the associated continuum of scaling exponents under shrinking tolerance, and a closed-form first jump. These quantitative two-parameter laws are not asserted by the general matrix representation alone, nor in the material inspected from that paper. Nguyen and coauthors (2025) instead require every synthesized realization to satisfy the constraints, which is a different deterministic model. No priority claim is made for the general spectral method or for ordinary composite-symbol bin counting.

## Limitations

The quantitative asymptotics concern the smallest even balanced window, not longer windows or wider GC bands. No uniform estimate is claimed beyond \(\varepsilon<1/2\). At \(k=2\) the first-threshold formula in the fourth displayed box is inapplicable because middle bins coincide; the universal bounds and zero-tolerance statement do apply. The result measures combinatorial constraint capacity, not synthesis fidelity after sequencing or a code's error-correction performance. The closest motivating paper contains the general matrix formulation, and an independently discovered/unindexed scaling analysis could create an originality overlap; novelty is limited to the explicit uniform quantitative conclusions established here.

## References

1. H. Bodur, F. Walter, and A. Wachter-Zeh, *Probabilistic GC-Constraints for Composite DNA*, arXiv:2610.09998v1, first public 2026-10-07, https://arxiv.org/abs/2610.09998.
2. T. T. Nguyen, C. Wang, K. Cai, Y. Zhang, and Z. Yakhini, *Constrained Coding for Composite DNA: Channel Capacity and Efficient Constructions*, arXiv:2501.10645v1, first public 2025-01-18, https://arxiv.org/abs/2501.10645.
