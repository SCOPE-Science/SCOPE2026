# Parity-corrected Apéry thresholds for halves of consecutive numerical semigroups

## Finding

Let \(a\ge5\) be odd and let \(3\le k\le a-2\) be integers. Define
\[
S_{a,k}=\langle a,a+1,\ldots,a+k\rangle,\qquad
T_{a,k}=\{n\in\mathbb N_0:2n\in S_{a,k}\}.
\]
Set \(t=\lceil(a-1)/k\rceil\) and \(q=a-1-(t-1)k\), so \(1\le q\le k\). For every \(0\le j<a\), put
\[
e_j=\lceil j/k\rceil,\qquad
L_j=e_j+\mathbf{1}_{e_j\not\equiv j\pmod2}.
\]
Then the complete Apéry set relative to the (not necessarily minimal) semigroup element \(a\) is
\[
\operatorname{Ap}(T_{a,k},a)=\left\{\frac{j+aL_j}{2}:0\le j<a\right\}.
\]
Consequently the Frobenius number is exactly
\[
F(T_{a,k})=\begin{cases}
(at-1)/2,&t\text{ odd},\\
at/2-1,&t\text{ even and }q\ge2,\\
(a(t-1)-1)/2,&t\text{ even and }q=1.
\end{cases}
\]
The genus is
\[
g(T_{a,k})=\frac{kt(t-1)+2tq-(t-1)(k\bmod2)-(q\bmod2)}4.
\]
The genus expression is recorded for completeness; an earlier publication gives general genus expressions for arithmetic-progression quotients. The Frobenius trichotomy and residuewise threshold description are the focus here.

## Assumptions and scope

All semigroups are additive submonoids of \(\mathbb N_0\). The genus counts nonnegative gaps; the Frobenius number is their largest member. For \(b\in T\), \(\operatorname{Ap}(T,b)=\{x\in T:x-b\notin T\}\); \(b\) need not be the multiplicity. Here \(a\in T_{a,k}\), because \(2a\in S_{a,k}\). The hypotheses are exactly odd \(a\ge5\), all integer \(k\) between \(3\) and \(a-2\), and quotient divisor \(2\). The defining generators are consecutive, not a general nonunit-step arithmetic progression. All formulas are exact and quantify over every such pair.

## Proof

**1. Exact residue thresholds of the original semigroup.** A sum of \(m\) generators in the interval \(\{a,a+1,\ldots,a+k\}\) is any integer between \(am\) and \((a+k)m\), inclusive. In particular, for any \(N\ge0\),
\[
N\in S_{a,k}\ \Longleftrightarrow\
\left\lceil\frac N{a+k}\right\rceil\le
\left\lfloor\frac Na\right\rfloor.
\]
For \(0\le j<a\), let \(e_j=\lceil j/k\rceil\), with \(e_0=0\). The least member of \(S_{a,k}\) congruent to \(j\pmod a\) is
\[
w_j=j+ae_j.
\]
Indeed \(w_j\) is realized with exactly \(e_j\) generators, whose increments above \(a\) sum to \(j\). If \(j+ah<w_j\), then \(h<e_j\). A putative representation has at most \(h\) summands (since each is at least \(a\)), but requires total increment at least \(j>kh\), impossible. Since \(a\in S_{a,k}\), all larger numbers of this residue by integer multiples of \(a\) belong to \(S_{a,k}\). Hence, for \(h\ge0\),
\[
j+ah\in S_{a,k}\ \Longleftrightarrow\ h\ge e_j.
\]

**2. Parity lift and Apéry set.** Because \(a\) is odd, multiplication by \(2\) permutes residues modulo \(a\). Fix a residue \(r\pmod a\), take \(0\le r<a\), and write \(2r=j+a\varepsilon\), where \(0\le j<a\) and \(\varepsilon\in\{0,1\}\). Parity gives \(\varepsilon\equiv j\pmod2\). Every nonnegative integer of this residue is \(x=r+ah\) for \(h\ge0\), and
\[
x\in T_{a,k}\ \Longleftrightarrow\
2x=j+a(\varepsilon+2h)\in S_{a,k}
\ \Longleftrightarrow\ \varepsilon+2h\ge e_j.
\]
Thus the least permitted exponent \(\varepsilon+2h\) is the least integer \(\ge e_j\) having parity \(j\), namely \(L_j\). The corresponding element of \(T_{a,k}\) is \((j+aL_j)/2\). As \(j\) runs through all residues modulo \(a\), so do these values, proving the stated Apéry formula (including \(j=0\)).

**3. Exact maximum.** Write \(b=a-1=(t-1)k+q\). For \(j\) in a block \((m-1)k<j\le mk\), the value \(e_j=m\), except the final block is truncated at \(b\). Therefore \(L_j\le t\) on every earlier block, and \(L_j\le t+1\) on the final block. If \(t\) is odd, \(b\) is even so \(L_b=t+1\). It is the largest \(L\)-level and largest \(j\) on that level; the maximum of \(j+aL_j\) is \(b+a(t+1)\). If \(t\) is even and \(q\ge2\), \(b-1\) is odd in the final block, so \(L_{b-1}=t+1\), while \(L_b=t\). It is the largest \(j\) reaching level \(t+1\), and maximizes \(j+aL_j\). If \(t\) is even and \(q=1\), the final block comprises only \(j=b\), which matches the parity of \(t\); hence all \(L_j\le t\), with the maximum \(j+aL_j=b+at\). Applying Selmer's standard identity \(F(T)=\max\operatorname{Ap}(T,a)-a\) yields the three displayed formulas. In all cases the maximizer is unique.

**4. Exact genus.** Selmer's genus identity, together with \(\sum_{j=0}^{a-1}j=a(a-1)/2\), gives
\[
g(T_{a,k})=\frac12\sum_{j=0}^{a-1}L_j-\frac{a-1}{4}.
\]
The \(t-1\) complete blocks each have length \(k\), and the last has length \(q\). Therefore
\[
\sum_{j=0}^{a-1} e_j=\frac{kt(t-1)}2+tq.
\]
Each complete block has exactly \(\lfloor k/2\rfloor\) positions where \(j\) and \(e_j\) have different parity; the final block has exactly \(\lfloor q/2\rfloor\) such positions. For odd \(k\), the initial position of each block has matching parity; for even \(k\), parity alternates evenly. Thus
\[
\sum_{j=0}^{a-1}(L_j-e_j)=(t-1)\lfloor k/2\rfloor+\lfloor q/2\rfloor.
\]
Substitute \(a-1=(t-1)k+q\), simplify \(2\lfloor u/2\rfloor=u-(u\bmod2)\), and obtain the genus formula.

**5. Boundary interpretation.** The same original Apéry thresholds give \(F(S_{a,k})=at-1\). Consequently
\[
F(T_{a,k})=\left\lfloor\frac{F(S_{a,k})}{2}\right\rfloor
\]
except precisely when \(t\) is even and \(q=1\), in which case the quotient Frobenius number is smaller by \((a-1)/2\). This is an exact classification of the exceptional boundary, not a uniform equality assumed in advance.

## Verification

An independent executable Python 3 checker, `check.py`, uses the interval-membership criterion for \(2x\in S_{a,k}\), separately from the symbolic Apéry predictions. It exhaustively compares the formulas for all odd \(a\in[5,119]\) and all \(3\le k\le a-2\). The recorded replay passed 3,364 parameter pairs, 844,484 membership comparisons, and 273,586 Apéry-minimality comparisons. For each pair it independently counts gaps, finds their maximum, and checks every predicted Apéry element. Run using `python3 check.py` in the package directory. Finite tests do not prove the universal statement; Steps 1–5 do.

## Relationship to prior work

Adeniran, Butler, Defant, Gao, Harris, Hettle, Liang, Nam and Volk (2018), especially their concluding open problem, ask for Frobenius and genus formulas for quotients of truncated arithmetic-progression semigroups. Their worked cases concern shorter or complete progressions, or quotient divisors dividing the multiplicity, not the odd-multiplicity half of a genuine intermediate consecutive interval. Feihu Liu (2023) studies an encompassing arithmetic-progression setting but explicitly assumes that the quotient divisor divides the initial generator; our divisor \(2\) does not divide odd \(a\). Lee and Nam (2024) give genus expressions for arithmetic-progression quotients, so our genus identity is not asserted to be a new genus classification. The present Apéry and Frobenius identities resolve the natural nondivisible half-quotient subcase with a sharp, piecewise parity anomaly. General generating-function techniques for quotient semigroups likewise exist (Liu, 2023), but the explicit parity-boundary trichotomy is not stated in the inspected relevant published results.

## Limitations

The scope is an explicit subfamily, not the full arbitrary-step or arbitrary-divisor open problem. The self-review analysis and finite checker do not constitute independent audit or formal certification. The full 2024 Lee–Nam paper was not accessible in the available literature pathway; only its abstract and publisher first-page preview were inspected. An implicit Frobenius deduction there or in other unindexed literature remains a residual originality risk. No optimality claim beyond the exact mathematical equalities is made.

## References

1. A. Adeniran et al., *On the Genus of a Quotient of a Numerical Semigroup* (first public preprint September 25, 2018), arXiv:1809.09360v1; https://arxiv.org/abs/1809.09360 .
2. F. Liu, *On Quotients of Numerical Semigroups for Almost Arithmetic Progressions* (December 11, 2023), arXiv:2312.06096v1; https://arxiv.org/abs/2312.06096 .
3. K. Lee and H. Nam, *The Genus of a Quotient of Several Types of Numerical Semigroups*, International Journal of Number Theory 20 (2024), 1809–1831, DOI 10.1142/S1793042124500891; published online April 5, 2024.
4. F. Liu, *Generating Functions for the Quotients of Numerical Semigroups* (December 18, 2023), arXiv:2312.10889v1; https://arxiv.org/abs/2312.10889 .
