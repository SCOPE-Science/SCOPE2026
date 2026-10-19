# Regular-element census and exponential rarity in finite partition-preserving transformation monoids

## Finding

Let \(X=B_1\sqcup\cdots\sqcup B_m\) be a finite set partitioned into labeled, nonempty blocks of sizes \(n_i=|B_i|\geq1\). Write \(T(X,\mathcal P)\) for the monoid of all maps \(f:X\to X\) sending each source block into some (possibly different) block. Let \(\operatorname{Reg}(T)\) denote the set of von Neumann regular elements, namely maps \(f\) for which \(fgf=f\) for some \(g\in T\).

For positive integers \(a,s\), define
\[
U(a,s)=s!\left\{\begin{matrix}a\\s\end{matrix}\right\}
=\sum_{r=0}^{s}(-1)^r\binom sr(s-r)^a,
\]
with \(U(a,s)=0\) when \(s>a\). For any block-index map \(\tau:\{1,\ldots,m\}\to\{1,\ldots,m\}\) and target index \(j\in\operatorname{im}\tau\), put \(I_j=\tau^{-1}(j)\), \(N_j=\sum_{i\in I_j}n_i\), and
\[
C_j(\tau)=\sum_{s=1}^{n_j}\binom{n_j}{s}
\left[s^{N_j}-\prod_{i\in I_j}\bigl(s^{n_i}-U(n_i,s)\bigr)\right].
\]
Then the exact number of regular elements of the entire monoid (not merely its block-surjective submonoid) is
\[
\boxed{\ |\operatorname{Reg}(T(X,\mathcal P))|
 =\sum_{\tau:[m]\to[m]}\prod_{j\in\operatorname{im}\tau}C_j(\tau).\ }
\tag{1}
\]
Formula (1) applies to arbitrary nonuniform block sizes and requires only nonnegative integer arithmetic.

For a uniform partition of \(m\) blocks of size \(n\), corresponding to the transformation wreath product \(T_n\wr T_m\), define \(c_n(0)=1\), and, for every \(k\geq1\),
\[
c_n(k)=\sum_{s=1}^{n}\binom ns\left[s^{nk}
 -\bigl(s^n-U(n,s)\bigr)^k\right],\qquad
A_n(z)=\sum_{k\geq0}\frac{c_n(k)}{k!}z^k.
\]
Thus
\[
\boxed{\ |\operatorname{Reg}(T_n\wr T_m)|=m!\,[z^m]A_n(z)^m.\ }
\tag{2}
\]
The exponential generating function is explicitly a finite sum of exponentials:
\[
A_n(z)=1+\sum_{s=1}^{n}\binom ns\left(e^{s^nz}-e^{(s^n-U(n,s))z}\right).
\tag{3}
\]

Furthermore, for each *fixed* block size \(n\geq2\), the proportion of regular elements among the \(m^m n^{nm}\) total elements decreases exponentially in \(m\). Put \(B_n(z)=A_n(z/n^n)\). There is a unique \(t_n>0\) such that
\[
\frac{t_n B_n'(t_n)}{B_n(t_n)}=1.
\]
Define
\[
v_n=t_n\left.\frac{d}{dt}\left(\frac{tB_n'(t)}{B_n(t)}\right)\right|_{t=t_n}>0,
\qquad \rho_n=\frac{B_n(t_n)}{e\,t_n}.
\]
Then \(0<\rho_n<1\) and
\[
\boxed{\quad
\frac{|\operatorname{Reg}(T_n\wr T_m)|}{m^m n^{nm}}
\sim\frac{\rho_n^m}{\sqrt{v_n}}
\quad(m\to\infty,\ n\geq2\text{ fixed}).\quad}
\tag{4}
\]
For \(n=1\) the entire monoid is regular and the proportion equals one. For \(n=2\),
\[
B_2(z)=e^z-e^{z/2}+2e^{z/4}-1,
\qquad \rho_2\approx0.969592013730826.
\]

## Assumptions and scope

The sets, partitions and maps are finite. Blocks are nonempty and distinguishable as subsets of a specified labeled ground set; there is no quotient by relabeling. Composition is ordinary transformation composition (the equation \(fgf=f\) is orientation-independent). A map in \(T(X,\mathcal P)\) is **not** required to map any source block onto an entire target block. The exact formulas hold for every \(m\geq1\) and all positive block sizes. The asymptotic is only asserted with \(n\geq2\) fixed while \(m\) tends to infinity.

## Proof

**1. Regularity criterion (known).** Fix an element \(f\in T(X,\mathcal P)\), let its induced block map be \(\tau\), and for each occupied target block \(B_j\) define \(A_j=(\operatorname{im}f)\cap B_j=\bigcup_{i\in I_j}f(B_i)\). We claim that \(f\) is regular precisely when, for each \(j\in\operatorname{im}\tau\), at least one \(i\in I_j\) satisfies \(f(B_i)=A_j\). This is the finite case of the published regularity characterization of Pei, restated in Sarkar--Singh (2023), Proposition 3.4. For completeness, the direct argument is as follows. If \(fgf=f\), then for every \(y\in A_j\), \(f(g(y))=y\), while \(g(B_j)\) lies in one source block, say \(B_i\). It follows that \(A_j\subseteq f(B_i)\subseteq A_j\) and necessarily \(i\in I_j\). Conversely, choose such an \(i\) for each occupied \(j\). Define \(g\) on \(A_j\) by choosing preimages in \(B_i\), and extend it arbitrarily over all of \(B_j\) into \(B_i\). For unoccupied blocks choose any target block and send their points there. The resulting map preserves the partition and is an inner inverse for \(f\).

**2. Count at one occupied target.** Fix \(\tau\) and an occupied target \(j\). The union \(A_j\) is a uniquely determined nonempty subset of \(B_j\), say with cardinality \(s\). Choose it in \(\binom{n_j}s\) ways. Across all source blocks \(i\in I_j\) there are \(s^{N_j}\) tuples of maps with their images contained in \(A_j\). Exactly \(s^{n_i}-U(n_i,s)\) maps from \(B_i\) into \(A_j\) fail to be onto \(A_j\). Thus the product subtracted in \(C_j(\tau)\) counts tuples for which **none** is onto. Every surviving tuple has at least one onto component and consequently has union exactly \(A_j\), so each is counted exactly once. The choices at distinct targets are independent; multiply over occupied \(j\), then sum over all \(m^m\) induced maps \(\tau\). This proves (1).

**3. Uniform exponential generating function.** With uniform block size, a target with \(k\geq1\) labeled source blocks contributes \(c_n(k)\); a target with none contributes the empty-factor value \(c_n(0)=1\). The multinomial theorem yields
\[
\sum_{\substack{k_1,\dots,k_m\geq0\\k_1+\cdots+k_m=m}}
\frac{m!}{k_1!\cdots k_m!}\prod_{j=1}^{m}c_n(k_j)
=m![z^m]A_n(z)^m,
\]
proving (2). Summation of the exponential series over all \(k\geq1\) gives (3).

**4. Exponential rarity and the constant.** For \(k\geq1\) set \(p_k=c_n(k)/n^{nk}\), and set \(p_0=1\). These coefficients are probabilities of the known regularity condition for \(k\) independently uniform block maps into a given target. They satisfy \(0<p_k\leq1\); \(p_1=1\), and \(p_2<1\) when \(n\geq2\): two constant maps with distinct values provide a counterexample to the regularity condition. Accordingly
\[
B_n(z)=\sum_{k\geq0}p_k\frac{z^k}{k!},
\qquad B_n(1)<e.
\]
From (3), the \(s=n\) term has positive leading exponential \(e^z\) in \(B_n(z)\); every other exponential has exponent less than one, since \(n!<n^n\) for \(n\geq2\), and \(s<n\) has \((s/n)^n<1\). Thus \(B_n(t)\sim e^t\) and \(tB_n'(t)/B_n(t)\sim t\) as \(t\to\infty\).

For \(t>0\), assign probabilities \(\mathbb P_t(K=k)=p_k t^k/(k!B_n(t))\). Its mean is \(\mu(t)=tB_n'(t)/B_n(t)\), and \(t\mu'(t)=\operatorname{Var}_t K>0\) because the support contains zero and one. Since \(\mu(t)\to0\) as \(t\downarrow0\) and \(\mu(t)\to\infty\) as \(t\to\infty\), there is a unique \(t_n\) with mean one, and its variance is \(v_n>0\).

For independent copies \(K_1,\dots,K_m\) under \(\mathbb P_{t_n}\), coefficient extraction gives
\[
[z^m]B_n(z)^m
=B_n(t_n)^m t_n^{-m}
\,\mathbb P_{t_n}(K_1+\cdots+K_m=m).
\]
The law has span one (it assigns positive mass to every integer \(k\geq0\)), finite moments of every order, and positive finite variance. The standard aperiodic lattice local central limit theorem, or its elementary characteristic-function proof, therefore gives
\[
\mathbb P_{t_n}(K_1+\cdots+K_m=m)
\sim(2\pi m v_n)^{-1/2}.
\]
Dividing (2) by \(m^m n^{nm}\) and applying Stirling's formula proves (4). Finally \(B_n(t)/t\) has its unique global minimum at \(t_n\), because the logarithmic derivative has the sign of \(\mu(t)-1\). Hence
\[
0<\rho_n=\frac{B_n(t_n)}{et_n}\leq\frac{B_n(1)}e<1.
\]
When \(n=1\), \(B_1(z)=e^z\), as expected for the full transformation monoid on \(m\) points.

## Verification

The accompanying independent finite checker `verify.py` reconstructs maps block by block; computes each count from (1); independently enumerates the regularity property directly from image unions; exhaustively searches all possible inner inverses when the entire monoid has at most 500 elements; checks selected positive and negative instances by direct inner-inverse search in larger cases; and checks the independent exponential-generating-function recurrence for uniform partitions. All enumerated tests passed. Exact illustrative counts (regular/total) are \((1,2):13/15\), \((2,2):60/64\), \((2,3):351/455\), \((1,1,2):78/96\), \((1,2,2):341/405\), \((2,2,2):1566/1728\), and \((3,2,1):2004/3024\). Small finite checks supplement, and do not replace, the general counting and asymptotic proofs.

## Relationship to prior work

Lu (2026) studies generation and rank of iterated transformation wreath products, motivating the uniform case; its principal results are not counts of regular elements. Pei (2005) and Sarkar--Singh (2023, Proposition 3.4) already characterize regular elements of the **whole** partition-preserving transformation monoid. This characterization is credited and used explicitly; it is not asserted to be new here. Sarkar--Singh (2020), Section 6.3, gives a count of regular elements of the **different submonoid** \(\Gamma(X,\mathcal P)\), whose individual source-block maps are surjective onto whole blocks. The present new contribution is the full-monoid nonuniform formula (1), uniform generating function (2)--(3), and explicit exponential-rarity asymptotic (4).

## Limitations

Originality has been assessed against accessible primary literature and mathematical finding records, but an older equivalent finite-enumeration formula or asymptotic under a different notation cannot be excluded. The logarithmic-exponential rate is specified implicitly by a unique positive saddle point rather than by elementary radicals. The theorem concerns finite partitions only. No independently conducted audit or independent validation is claimed.

## References

1. Jiaping Lu, *Generation of Iterated Wreath Products Constructed from Full Transformation Monoids and Symmetric Groups*, arXiv:2609.20521v1 (first public September 17, 2026), https://arxiv.org/abs/2609.20521.
2. Mosarof Sarkar and Shubh N. Singh, *Semigroups of transformations whose characters belong to a given semigroup*, arXiv:2310.19414v1 (2023), especially Proposition 3.4, https://arxiv.org/html/2310.19414v1.
3. Mosarof Sarkar and Shubh N. Singh, *Regular, Unit-regular, and Idempotent elements of semigroups of transformations that preserve a partition*, arXiv:2010.14033v1 (2020), especially Section 6.3 on \(\Gamma(X,\mathcal P)\), https://arxiv.org/abs/2010.14033.
4. H. Pei, *Regularity and Green's relations for semigroups of transformations that preserve an equivalence* (2005), regularity criterion as cited and reproduced in Reference 2.
5. Classical aperiodic lattice local central limit theorem, applied to an explicitly defined positive lattice distribution with analytic probability generating function.
