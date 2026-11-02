# Sparse repetition is the exact zero-growth boundary for two moving dyadic holes

## Finding

Let \(T:[0,1)\to[0,1)\) be doubling modulo one and alternate, according to an arbitrary prescribed binary sequence \(\omega=(\omega_j)_{j\ge0}\), between the two dyadic holes
\[
H_0=[0,1/4),\qquad H_1=[3/4,1).
\]
For each integer \(n\ge1\), let \(S_n(\omega)\) be the initial states surviving the tests \(T^j(x)\notin H_{\omega_j}\) for \(0\le j<n\). Define the repetition (or failure-of-alternation) count
\[
d_n(\omega)=\#\{0\le j<n-1:\omega_j=\omega_{j+1}\},\qquad k_n=d_n+1.
\]
Let \(N_n(\omega)\) count the legal binary itineraries of length \(n+1\) passing the first \(n\) tests. Then, for **every** deterministic schedule and every \(n\ge1\),
\[
|S_n(\omega)|_{\mathrm{Leb}}=\frac{N_n(\omega)}{2^{n+1}},\qquad
2^{1+\lceil d_n/2\rceil}\le N_n(\omega)\le2\left(1+\frac{n}{d_n+1}\right)^{d_n+1}.
\tag{1}
\]
Here \(|\cdot|_{\mathrm{Leb}}\) denotes Lebesgue measure, not cardinality. In particular, if
\[
h^+(\omega)=\limsup_{n\to\infty}\frac{\log N_n(\omega)}{n},\qquad
h^-(\omega)=\liminf_{n\to\infty}\frac{\log N_n(\omega)}{n},
\]
then the exact two-sided critical criteria are
\[
h^+(\omega)=0\quad\Longleftrightarrow\quad\lim_{n\to\infty}\frac{d_n(\omega)}n=0,
\qquad
h^-(\omega)=0\quad\Longleftrightarrow\quad\liminf_{n\to\infty}\frac{d_n(\omega)}n=0.
\tag{2}
\]
Thus the largest possible lower exponential escape rate, \(\log2\), occurs **exactly** for schedules whose deviations from perfect alternation have zero asymptotic density. More explicitly,
\[
\liminf_{n\to\infty}-\frac1n\log|S_n(\omega)|_{\mathrm{Leb}}=\log2-h^+(\omega).
\]
For the perfectly alternating schedule \(\omega_j=j\bmod2\), one has the exact all-time law
\[
N_n=n+2,\qquad |S_n|_{\mathrm{Leb}}=\frac{n+2}{2^{n+1}}.
\tag{3}
\]
Its infinite survivor has only countably many points and has zero entropy under the two-step map. In contrast, either fixed hole alone has \(N_n=F_{n+3}\), with \(F_0=0,F_1=1\), and entropy \(\log\varphi>0\), where \(\varphi=(1+\sqrt5)/2\). Hence two individually positive-entropy open systems can have zero survivor growth under switching.

## Assumptions and scope

The hole selected at step \(j\) is removed **before** the update from \(j\) to \(j+1\). No probability law, stationarity, periodicity, or frequency limit is assumed for \(\omega\). Lebesgue initial data are used to define survival probabilities. The word-count criterion is a statement about prefix growth for a prescribed nonautonomous schedule, **not** an assertion that arbitrary schedules define a single autonomous subshift or that their word-count limits always exist. Natural logarithms are used.

Every number in \([0,1)\) has a chosen binary expansion that is not eventually all ones, resolving the dyadic ambiguity. The holes above are precisely the binary cylinders \(00\) and \(11\). The excluded ambiguous endpoints have Lebesgue measure zero; the finite word counts and escape probabilities are exact. Each legal finite itinerary extends to an infinite legal sequence because each transition matrix below has a nonzero row for each starting symbol.

## Proof

**1. Coding and exact survival mass.** Write the doubling-map binary digits as \(b_0b_1b_2\ldots\). At time \(j\), escaping through \(H_0\) is equivalent to \(b_jb_{j+1}=00\), and through \(H_1\) to \(b_jb_{j+1}=11\). Allowed consecutive-bit transitions therefore have matrices
\[
A=\begin{pmatrix}0&1\\1&1\end{pmatrix},\qquad
B=\begin{pmatrix}1&1\\1&0\end{pmatrix}.
\]
With \(M_0=A,M_1=B\), column vector \(\mathbf1=(1,1)^{\mathsf T}\), and \(P_n=M_{\omega_0}\cdots M_{\omega_{n-1}}\), the exact finite count is \(N_n=\mathbf1^{\mathsf T}P_n\mathbf1\). Every legal \((n+1)\)-bit cylinder has Lebesgue measure \(2^{-n-1}\), proving the first identity of (1).

**2. Upper bound for any switching schedule.** Cut the length-\(n\) hole schedule immediately after each occurrence of two consecutive equal symbols. This divides it into exactly \(k=d_n+1\) maximal alternating blocks of lengths \(\ell_1,\ldots,\ell_k\), whose sum is \(n\). Direct multiplication gives
\[
AB=\begin{pmatrix}1&0\\2&1\end{pmatrix},\qquad
BA=\begin{pmatrix}1&2\\0&1\end{pmatrix}.
\]
Since \((AB)^r=\bigl(\begin{smallmatrix}1&0\\2r&1\end{smallmatrix}\bigr)\) and \((BA)^r=\bigl(\begin{smallmatrix}1&2r\\0&1\end{smallmatrix}\bigr)\), every alternating-block product of length \(\ell\ge1\) has maximal row-sum norm exactly \(\ell+1\) (including odd lengths, by multiplying once more by \(A\) or \(B\)). Submultiplicativity yields
\[
N_n\le2\|P_n\|_\infty\le2\prod_{i=1}^{k}(\ell_i+1)
\le2\left(1+\frac{n}{k}\right)^k,
\]
where the last step is arithmetic--geometric mean. This is the upper bound of (1).

**3. Lower bound.** Divide the schedule into maximal constant runs. In a constant run of length \(r\), select \(\lfloor r/2\rfloor\) disjoint adjacent equal-symbol pairs. The total number \(q\) of such pairs satisfies \(q\ge d_n/2\), because a run of length \(r\) contributes \(r-1\) to \(d_n\), and \(\lfloor r/2\rfloor\ge(r-1)/2\). Both \(A\mathbf1\) and \(B\mathbf1\) dominate \(\mathbf1\) coordinatewise, whereas
\[
A^2\mathbf1=(2,3)^{\mathsf T}\ge2\mathbf1,\qquad
B^2\mathbf1=(3,2)^{\mathsf T}\ge2\mathbf1.
\]
All matrices have nonnegative entries. Reading the disjoint pairs and remaining single-letter factors from the right therefore gives \(P_n\mathbf1\ge2^q\mathbf1\) and \(N_n\ge2^{1+q}\ge2^{1+\lceil d_n/2\rceil}\), as claimed.

**4. Zero-growth equivalences.** Put \(t_n=(d_n+1)/n\). The two bounds imply
\[
\frac{\log2}{n}\left(1+\frac{d_n}{2}\right)
\le\frac{\log N_n}{n}
\le\frac{\log2}{n}+t_n\log(1+1/t_n).
\]
Since \(t\log(1+1/t)\to0\) as \(t\downarrow0\), vanishing upper density of repeated adjacent choices implies \(h^+=0\). Conversely if \(h^+=0\), the lower bound forces \(d_n/n\to0\). The same two inequalities along subsequences establish the liminf equivalence. The survival-mass identity then converts prefix growth into the asserted escape formula.

**5. Alternating and static comparison.** When \(\omega_j=j\bmod2\), make the reversible time-dependent digit change \(z_j=b_j\oplus(j\bmod2)\), where \(\oplus\) is addition modulo two. At every time, the one forbidden pair becomes \(z_jz_{j+1}=01\). Consequently legal words are exactly the \(n+2\) weakly nonincreasing binary words of length \(n+1\), proving (3). Infinite legal transformed strings are \(1^m0^\infty\) for \(m\ge0\) together with \(1^\infty\). All their original digit sequences are eventually alternating, so the infinite survivor is countable and every orbit is eventually on the period-two doubling orbit \(\{1/3,2/3\}\). For a constant hole, the usual two-state Fibonacci recurrence gives \(N_n=F_{n+3}\) and the indicated positive growth rate.

## Verification

Run `python3 verify_switch.py` using standard Python 3. The checker independently enumerates all binary words for all \(2^n\) schedules with \(1\le n\le11\), compares the counts with the transfer-matrix formula, checks both bounds by exact integer arithmetic, verifies the alternating count, and checks the four small matrix identities. Additional length-\(100\), \(250\), and \(500\) schedules with sparse defects are consistency checks only. The calculations pass. The infinite-rate and countability assertions are proved above, not inferred from these finite computations.

## Relationship to prior work

Kong, Sun and Wang, *Open dynamical systems with a moving hole* (first posted 2025-05-05), develop general moving-cylinder dimension theory and matrix-product methods **under the hypothesis that the base is at least three**. Their final remarks explicitly identify binary base two as excluded because a connecting-word argument fails there. Their results give a general context for moving holes but do not assert criterion (2) or the sharp bounds (1) in this binary case. The newer work of Kong, Li, Ma and Simon (2026) extends the framework to inhomogeneous iterated-function systems while retaining a base-at-least-three hypothesis for the corresponding main dimension theorem. A previously established exact prefix-count formula for arbitrary moving binary-bigram holes in bases at least three is complementary; its matrix bookkeeping is not claimed as a new invention here. The present result isolates the **singular two-symbol case** and establishes its all-schedule zero-growth boundary.

Manada, Annou, Yamauchi, Morita and Ota (first public 2025-10-14) give capacity formulas for **periodic** forbidden-word schedules. Those cover the periodic subcase in principle; the alternating periodic example above is an illustration, not a claim of priority for periodic capacity calculations. The new criterion concerns **arbitrary, including nonperiodic**, schedules and supplies quantitative uniform finite-time bounds. Nan (2026) develops random open-map thermodynamic formalism under hypotheses for invariant random measures; this is distinct from the pointwise all-schedule critical criterion here. Livorati, Georgiou, Dettmann and Leonel (2013/2014) analyze oscillating/breathing time-dependent holes, but not the present binary symbolic degeneracy. Sturman and Thiffeault (2017/2019) analyze Lyapunov exponents for random products of positive shear matrices, which are related to products of the unipotent blocks \(AB\) and \(BA\), but their stochastic assumptions and average-growth bounds do not give the present deterministic all-schedule equivalence.

## Limitations

The result applies only to the doubling map, the two specified complementary length-two cylinders, and binary switching schedules. It does not establish a corresponding criterion for larger alphabets, higher-order cylinders, or arbitrary moving intervals. For irregular schedules, the exponential growth limit need not exist; this theorem uses limsup and liminf explicitly. The entropy of a perfectly alternating periodic system is already accessible from periodic finite-type theory, so novelty is claimed only for the complete arbitrary-schedule criterion and its uniform quantitative proof. Priority against unindexed work on the same exceptional matrix products remains open to independent literature review. The checks included in the package are finite consistency checks, not infinite proof certificates.

## References

1. D. Kong, B. Sun, Z. Wang, *Open dynamical systems with a moving hole*, arXiv:2505.02336, version 1 posted 2025-05-05; full version 2: https://arxiv.org/html/2505.02336v2, especially Theorem 1.1 and Section 7(i).
2. D. Kong, K. Li, C.-Y. Ma, K. Simon, *Open dynamics with a moving hole: inhomogeneous IFS and exponential separation condition*, arXiv:2610.31128v1, posted 2026-10-22, https://arxiv.org/html/2610.31128v1, especially Theorem 1.1 and Remark 1.2.
3. A. Manada, N. Annou, R. Yamauchi, H. Morita, T. Ota, *The Capacities of Periodic-Finite-Type Shifts from the Perspective of the Forbidden-Word Length*, public 2025-10-14, DOI:10.1587/transfun.2025EAP1099, https://www.jstage.jst.go.jp/article/transfun/advpub/0/advpub_2025EAP1099/_pdf.
4. C. Nan, *Invariant and conditionally invariant measures for random open interval maps with countably many branches*, arXiv:2603.19586, posted 2026-03-20, https://arxiv.org/abs/2603.19586.
5. A. L. P. Livorati, O. Georgiou, C. P. Dettmann, E. D. Leonel, *Escape through a time-dependent hole in the doubling map*, arXiv:1312.7030, first posted 2013-12-25, https://arxiv.org/abs/1312.7030.
6. R. Sturman, J.-L. Thiffeault, *Lyapunov exponents for the random product of two shears*, arXiv:1706.03398, posted 2017-06-11, https://arxiv.org/abs/1706.03398; journal full text https://link.springer.com/article/10.1007/s00332-018-9497-3.
