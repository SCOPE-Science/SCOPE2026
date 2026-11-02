# A sharp modulo-eight distribution law for the semi-Pell sequence

## Finding

Let the positive-index semi-Pell sequence be defined by \(u(1)=1\),
\(u(2m)=u(m)\) for \(m\ge1\), and
\(u(2m+1)=2u(2m)+u(2m-1)\) for \(m\ge1\).
For each \(j\in\{1,3,5,7\}\) and integer \(N\ge1\), write
\[
C_j(N)=\#\{1\le n<N:u(n)\equiv j\pmod8\}.
\]
For every such \(j\), uniformly for integer \(N\ge1\),
\[
C_j(N)=\frac N4+O(\sqrt N),
\]
with an absolute implied constant. The exponent \(1/2\) is optimal *for each of the four residues individually*.

There is an exact dyadic counting law. For \(r\ge1\), put \(C_{r,j}=C_j(2^r)\).
Define integer sequences \((E_k)_{k\ge0}\) and \((O_k)_{k\ge0}\) by
\[
\sum_{k\ge0}E_k t^k=\frac{1+t-2t^3}{1+4t^4},\qquad
\sum_{k\ge0}O_k t^k=\frac{t+2t^2+2t^3}{1+4t^4},
\]
and \(e_r=\sum_{k=0}^{r-1}E_k\), \(o_r=\sum_{k=0}^{r-1}O_k\). Then
\[
\begin{aligned}
C_{r,1}&=(2^{r-1}+e_r)/2,&C_{r,5}&=(2^{r-1}-e_r)/2,\\
C_{r,3}&=(2^{r-1}-1+o_r)/2,&C_{r,7}&=(2^{r-1}-1-o_r)/2.
\end{aligned}
\]
In particular, for every integer \(a\ge0\), the quadruple of exact counts at \(r=4a+1\), in residue order \(1,3,5,7\), is
\[
\left(2^{4a-1}+\frac{(-4)^a}{2},\;
2^{4a-1}-\frac{(-4)^a}{2},\;
2^{4a-1}-\frac{(-4)^a}{2},\;
2^{4a-1}-1+\frac{(-4)^a}{2}\right).
\]
Thus each residue discrepancy has absolute size comparable to \(\sqrt{2^{4a+1}}\) along infinitely many dyadic cutoffs.

An additional structural classification is valid for *every* positive index. Write \(n=2^v(2m+1)\), with \(v,m\ge0\), and let \(\varepsilon_i\in\{0,1\}\) be the binary digits of \(m\) (zero beyond its leading digit). Put
\[
Q(m)\equiv\sum_{i\ge1}\varepsilon_i+\sum_{i\ge0}\varepsilon_i\varepsilon_{i+1}\pmod2.
\]
Then
\[
\boxed{u(n)\equiv1+2\varepsilon_0+4Q(m)\pmod8.}
\]
The finite sums in \(Q(m)\) describe the number of non-lowest set bits and the number of overlapping binary `11` pairs, modulo two.

## Assumptions and scope

All variables \(n,N,r,a,m,v\) are ordinary nonnegative or positive integers in the stated ranges. The congruence uses the unique odd part of \(n>0\). The value at index zero is intentionally excluded; the positive semi-Pell terms coincide with the original sequence regardless of whether a source convention defines the zero-index term as zero or one. Only the modulus eight and the four odd residue classes are addressed. All error constants are absolute; no unproved equidistribution hypothesis is used.

## Proof

**1. The lowest congruence layer.** All positive terms \(u(n)\) are odd: the even-index rule preserves the oddness of a smaller term, and the odd-index rule adds an even multiple of one term to an odd earlier term. Iterating the odd-index rule gives the exact finite identity
\[
u(2m+1)=1+2\sum_{k=1}^{m}u(k)\qquad(m\ge0).
\]
Consequently \(u(2m+1)\equiv 2m+1\pmod4\); by even-index reduction, \(u(k)\equiv\operatorname{oddpart}(k)\pmod4\) for every \(k\ge1\).

Let \(b(k)\) be one if \(\operatorname{oddpart}(k)\equiv3\pmod4\), and zero otherwise; put \(A(m)=\sum_{1\le k\le m}b(k)\). Then
\[
\sum_{k=1}^{m}u(k)\equiv m+2A(m)\pmod4,
\]
so
\[
u(2m+1)\equiv1+2m+4A(m)\pmod8.
\]
The integers \(A(m)\) obey, with \(A(0)=0\),
\[
A(2m)=A(m)+\lfloor m/2\rfloor,\qquad
A(2m+1)=A(m)+\lfloor m/2\rfloor+(m\bmod2).
\]
Indeed the even summands contribute \(A(m)\), while the odd summands congruent to three modulo four contribute exactly \(\lfloor m/2\rfloor\) through \(2m\); the last odd summand is selected precisely when \(m\) is odd.

Repeatedly removing the least significant binary digit in these relations proves by induction that
\[
A(m)\equiv\sum_{i\ge2}\varepsilon_i+\sum_{i\ge0}\varepsilon_i\varepsilon_{i+1}\pmod2.
\]
Since \(2m\equiv2\varepsilon_0+4\varepsilon_1\pmod8\), substitution yields the announced formula \(u(2m+1)\equiv1+2\varepsilon_0+4Q(m)\pmod8\). The even-index rule extends it to every positive index.

**2. Exact dyadic census.** For \(p\in\{0,1\}\), set
\[
W_p(k)=\sum_{\substack{0\le m<2^k\\\varepsilon_0=p}}(-1)^{Q(m)},
\]
interpreting the only zero-bit word when \(k=0\) as \(\varepsilon_0=0\). Write \(E_k=W_0(k)\) and \(O_k=W_1(k)\). Then \((E_0,O_0)=(1,0)\), \((E_1,O_1)=(1,1)\). For \(k=2\), fixing the lowest bit and grouping by the highest bit gives the column vectors
\[
\mathbf e_2=(1,-1)^{\mathsf T},\qquad
\mathbf o_2=(1,1)^{\mathsf T}.
\]
Appending a new most significant bit \(b\) contributes the sign \((-1)^{b(1+h)}\), where \(h\) was the previous most significant bit. Therefore, for \(k\ge2\),
\[
\mathbf e_{k+1}=T\mathbf e_k,\qquad
\mathbf o_{k+1}=T\mathbf o_k,\qquad
T=\begin{pmatrix}1&1\\-1&1\end{pmatrix},
\]
and \(E_k=(1,1)\mathbf e_k\), \(O_k=(1,1)\mathbf o_k\). Direct multiplication gives \(T^4=-4I\), so \(E_{k+4}=-4E_k\), \(O_{k+4}=-4O_k\) for \(k\ge2\). Their exact initial values are
\[
(E_0,\dots,E_5)=(1,1,0,-2,-4,-4),\qquad
(O_0,\dots,O_5)=(0,1,2,2,0,-4).
\]
These finite recurrences prove the two displayed rational generating functions as identities of formal power series.

Every \(n\) with \(1\le n<2^r\) is uniquely \(2^v(2m+1)\), with \(0\le v<r\) and \(0\le m<2^{r-v-1}\). For fixed \(k=r-v-1\), the sign imbalance between residues one and five is \(E_k\), and between three and seven is \(O_k\). Across all \(k\in\{0,\ldots,r-1\}\), the total numbers with lowest bit \(\varepsilon_0=0\) and \(\varepsilon_0=1\) are respectively \(2^{r-1}\) and \(2^{r-1}-1\). Solving the two sum-and-difference pairs yields the four exact formulas for \(C_{r,j}\).

Summing the transfer recurrences, or extracting coefficients from the rational functions, gives
\[
e_{4a+1}=(-4)^a,\qquad o_{4a+1}=1-(-4)^a\qquad(a\ge0).
\]
The explicit dyadic quadruple follows immediately.

**3. Uniform prefix discrepancy.** Fix \(p\in\{0,1\}\). We show that
\[
\sum_{\substack{0\le m<M\\m\equiv p\pmod2}}(-1)^{Q(m)}=O(\sqrt M)
\]
uniformly for integers \(M\ge1\). Partition \([0,M)\) into aligned dyadic blocks, at most one of each length \(2^k\). On an aligned block of length \(2^k\), its upper binary digits are fixed. For \(k\ge2\), their effect on the sign of a varying low word is a constant factor and possibly a sign depending on its highest bit. After fixing the lowest bit to \(p\), the signed sum is thus one of the row-vector functionals \(\pm(1,1)T^{k-2}\mathbf v_p\) or \(\pm(1,-1)T^{k-2}\mathbf v_p\), with \(\mathbf v_0=(1,-1)^{\mathsf T}\) and \(\mathbf v_1=(1,1)^{\mathsf T}\). Since \(T^{\mathsf T}T=2I\), Cauchy--Schwarz bounds each such block sum by \(2^{k/2}\). The blocks of lengths one and two satisfy the same bound directly. The sum of the geometrically increasing block bounds is \(O(\sqrt M)\).

Therefore, for each of the four residues, among odd integers \(2m+1\) with \(0\le m<M\), the count is \(M/4+O(\sqrt M)\). Separating positive even and odd indices in \([1,2M)\) gives
\[
C_j(2M)=C_j(M)+\frac M4+O(\sqrt M).
\]
The additional term for \(C_j(2M+1)\) differs from \(C_j(2M)\) by at most one. Iterating these two relations down the binary expansion of \(N\) gives \(C_j(N)=N/4+O(\sqrt N)\), since the accumulated errors form a convergent geometric sum at successive halved scales.

**4. Sharpness.** At \(N=2^{4a+1}\), the four exact formulas show errors from \(N/4\) of respectively \((-4)^a/2\), \(-(-4)^a/2\), \(-(-4)^a/2\), and \((-4)^a/2-1\). For each fixed residue these have size asymptotic to \(4^a/2\), a positive constant multiple of \(\sqrt N\). Thus no exponent smaller than \(1/2\) can replace the exponent in the uniform error bound for any of the four residues.

## Verification

Run the self-contained Python standard-library script `python3 verify.py` from the directory containing this document. It reconstructs 65,535 positive terms using the original recurrence, checks 32,768 odd-index mod-eight binary formulas, confirms the odd-part reduction, compares all sixteen dyadic census sizes from \(r=1\) through \(r=16\), and checks the rational coefficients and \(T^4=-4I\). The expected final status is `VERIFY_OK`.

These finite checks do not prove the infinite conclusion. That conclusion is obtained from the exact binary recursion, the transfer-matrix identities, and the aligned-block Cauchy--Schwarz estimate above.

## Relationship to prior work

Keith and Munagi introduced binary-composition interpretations for the semi-Pell sequence and proved its modulo-four behavior at odd arguments in arXiv:1912.11148v1, Theorem 2. Their later treatment of semi-m-Pell compositions (Online Journal of Analytic Combinatorics, 2023, Theorem 6) classifies the positive sequence modulo four, not modulo eight. Ballantine and Beck (arXiv:2303.11493v1, Section 6) give further partition interpretations and connect the lowest congruence layer to paperfolding. The OEIS entry A129095 records the sequence and related counting tables. These are the starting identities; the new statement is the complete next-layer digital formula, every dyadic residue count, the all-cutoff density law, and its separately sharp square-root fluctuation.

The quadratic sign \((-1)^{Q(m)}\) belongs to the generalized Rudin--Shapiro family, for which transfer-matrix square-root bounds are a standard mechanism. That general mechanism does not itself identify the semi-Pell residues or give the exact census above. Searches of named-object aliases and the closest primary texts did not reveal these particular conclusions. This does not establish absolute priority.

## Limitations

Only modulus eight is classified. The theorem makes no claim about distributions modulo higher powers of two, dependence of adjacent residues, or a limiting law for the full integer values. The discrepancy exponent is optimal, but the exact best global implied constants are not determined. Priority is subject to unindexed work and to any more general digital-residue theorem not located in the inspected material. Verification is internal and no independent scientific audit has been performed.

## References

1. William J. Keith and Augustine O. Munagi, *Binary Compositions and Semi-Pell Compositions*, arXiv:1912.11148v1, first posted 2019-12-23. https://arxiv.org/html/1912.11148v1
2. Cristina Ballantine and George Beck, *Partitions enumerated by self-similar sequences*, arXiv:2303.11493v1, first posted 2023-03-20, especially Section 6. https://arxiv.org/html/2303.11493
3. William J. Keith and Augustine O. Munagi, *Power compositions and semi-Pell compositions*, Online Journal of Analytic Combinatorics 18 (2023), paper 2. https://combinatorialpress.com/article/ojac/vol18/276.pdf
4. OEIS Foundation, A129095, *Semi-Pell numbers*, and A129096, the odd-index subsequence. https://oeis.org/A129095
