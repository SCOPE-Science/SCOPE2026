# Sharp digit envelopes and oscillation constants for positive Galileo sequences

## Finding
Fix an integer \(k\ge2\). A normalized positive integer Galileo sequence is a sequence \((a_n)_{n\ge1}\) of positive integers with \(a_1=1\), whose partial sums \(S_0=0\), \(S_n=\sum_{j=1}^{n}a_j\) obey \(S_{2n}=kS_n\) for every \(n\ge1\). Define the binary-to-base-\(k\) digit map
\[
L_k(0)=0,\qquad L_k(n)=\sum_{j\ge0}\varepsilon_j k^j
\quad\text{if}\quad n=\sum_{j\ge0}\varepsilon_j2^j,\ \varepsilon_j\in\{0,1\}.
\]
For \(n\ge1\) set \(r(n)=\lceil\log_2n\rceil\) and
\[
U_k(n)=k^{r(n)}-L_k(2^{r(n)}-n).
\]
(The zero-argument convention makes these formulas valid at powers of two, including \(n=1\).)

**Sharp simultaneous envelopes.** For every such sequence and every \(n\ge1\),
\[
L_k(n)\le S_n\le U_k(n).
\]
Each endpoint is achieved *simultaneously at every index* by a single normalized positive integer Galileo sequence, so these are the exact pointwise minimum and maximum of \(S_n\) over the whole family.

**Sharp growth constants.** With \(\alpha=\log_2k\), every member of the family satisfies
\[
\frac{n^{\alpha}}{k-1}\le S_n\le
\left(k-\frac1{k-1}\right)n^{\alpha}\qquad(n\ge1).
\]
Neither coefficient can be improved as a uniform coefficient over all sequences and all positive indices. More precisely, for the two extremal sequences,
\[
\liminf_{n\to\infty}\frac{L_k(n)}{n^{\alpha}}=\frac1{k-1},\qquad
\limsup_{n\to\infty}\frac{L_k(n)}{n^{\alpha}}=1,
\]
\[
\liminf_{n\to\infty}\frac{U_k(n)}{n^{\alpha}}=1,\qquad
\limsup_{n\to\infty}\frac{U_k(n)}{n^{\alpha}}=k-\frac1{k-1}.
\]
At \(k=2\), both envelopes and both constants reduce to \(S_n=n\).

## Assumptions and scope
Only \(k\in\mathbb Z\), \(k\ge2\), \(n\ge1\), positive *integer* terms and normalization \(S_1=1\) are assumed. No monotonicity of the terms \((a_n)\) is assumed. For initial term \(a_1=c\in\mathbb Z_{>0}\), multiplication of the displayed extremal constructions by \(c\) gives valid scaled bounds, although the present theorem asserts sharpness only in the normalized class. Statements about asymptotic coefficients refer to entire infinite sequences, not to finite prefixes.

## Proof
**1. Exact recursion bounds.** Any admissible \(S\) is strictly increasing by positive integer increments. Its dilation identity gives
\[
S_{2m}=kS_m,\qquad
kS_m+1\le S_{2m+1}\le kS_{m+1}-1\quad(m\ge1).
\]
The digit map satisfies \(L_k(2m)=kL_k(m)\) and \(L_k(2m+1)=kL_k(m)+1\). Strong induction therefore gives \(S_n\ge L_k(n)\), starting at \(S_1=L_k(1)=1\).

Define \(V(1)=1\) and inductively, for \(m\ge1\),
\[
V(2m)=kV(m),\qquad V(2m+1)=kV(m+1)-1.
\]
These equations determine each \(V(n)\) from a smaller index (apart from the stipulated base case). The upper recursion bound for \(S\) yields \(S_n\le V(n)\) by strong induction. The formula \(V(n)=k^{r(n)}-L_k(2^{r(n)}-n)\) follows from these same recurrences: for even \(n\), both the dyadic exponent and the reflected argument halve; for odd \(n=2m+1\ge3\), put \(r=r(n)\), \(h=2^{r-1}-(m+1)\) and observe
\[
2^r-n=2h+1,\quad L_k(2h+1)=kL_k(h)+1,
\]
so \(V(n)=kV(m+1)-1\). Thus \(V=U_k\).

**2. Both extrema really are sequences.** The digits satisfy \(L_k(n)>L_k(n-1)\) for every \(n\ge1\): incrementing a binary numeral changes a block of \(t\) trailing ones into a one in position \(t\), and the increment in its base-\(k\) interpretation is
\[
k^t-\sum_{j=0}^{t-1}k^j\ge1\quad(k\ge2).
\]
Hence \(a_n=L_k(n)-L_k(n-1)\) is positive integral, \(L_k(1)=1\), and \(L_k(2n)=kL_k(n)\). This realizes the lower envelope simultaneously.

For the upper envelope, construct positive integral terms by
\[
a_1=1,\quad a_2=k-1,\quad
(a_{2m-1},a_{2m})=(ka_m-1,1)\quad(m\ge2).
\]
Each pair sums to \(ka_m\). Summing these identities proves \(S_{2n}=kS_n\) for all \(n\). Since each even term after the second is one, \(S_{2m+1}=kS_{m+1}-1\) for \(m\ge1\). Its partial sums therefore satisfy the defining recursion for \(V\), and equal \(U_k\) at every index. This proves pointwise and simultaneous sharpness.

**3. Lower digit growth.** Put \(\alpha=\log_2 k\ge1\). For each binary expansion, superadditivity of \(x\mapsto x^{\alpha}\) on nonnegative arguments gives
\[
L_k(n)=\sum_{j:\varepsilon_j=1}(2^j)^{\alpha}\le n^{\alpha}.
\]
Conversely, prove \(n^{\alpha}\le(k-1)L_k(n)\) by induction, using \(n=2^r+t\), \(0\le t<2^r\). The increasing function \(u\mapsto(2^r+u)^{\alpha}-u^{\alpha}\) satisfies
\[
(2^r+t)^{\alpha}-t^{\alpha}\le(2^{r+1})^{\alpha}-(2^r)^{\alpha}=(k-1)k^r.
\]
Apply the induction hypothesis to \(t\) and use \(L_k(n)=k^r+L_k(t)\). Equality \(L_k(2^r)=k^r\) gives the upper oscillation endpoint. The all-ones binary inputs obey
\[
L_k(2^r-1)=\frac{k^r-1}{k-1},
\]
which gives the lower oscillation endpoint.

**4. Upper digit growth.** First \(U_k(n)\ge n^{\alpha}\) follows inductively from its even and odd recurrences. For odd indices, use
\[
U_k(2m+1)=kU_k(m+1)-1\ge(2m+2)^{\alpha}-1\ge(2m+1)^{\alpha},
\]
because \(\alpha\ge1\). For the upper bound, let \(r=r(n)\) and \(x=(2^r-n)/2^r\in[0,1/2)\). The lower estimate on \(L_k\) yields
\[
\frac{U_k(n)}{n^{\alpha}}\le
F(x):=\frac{1-x^{\alpha}/(k-1)}{(1-x)^{\alpha}}.
\]
Direct differentiation for \(0<x<1/2\) gives
\[
F'(x)=\frac{\alpha\bigl(1-x^{\alpha-1}/(k-1)\bigr)}{(1-x)^{\alpha+1}}\ge0.
\]
The limiting value at \(x=1/2\) is \(F(1/2)=k-1/(k-1)\), proving the universal upper coefficient. Powers \(n=2^r\) give \(U_k(n)/n^{\alpha}=1\). The indices \(n=2^r+1\) satisfy
\[
U_k(2^r+1)=k^{r+1}-\frac{k^r-1}{k-1},
\]
so their normalized ratios tend to \(k-1/(k-1)\). All four oscillation claims, including the degenerate \(k=2\) case, follow.

## Verification
The accompanying standalone \(verify.py\) builds the two extremal sequences from their positive integer splitting recurrences and tests their digit formulas, the dilation identity, and exact pointwise inequalities for \(2\le k\le17\), \(1\le n\le2000\). It also exhaustively enumerates admissible positive splits for three small finite horizons and checks every resulting prefix against both claimed extrema. Running \(python verify.py\) reports 32,000 deterministic checks and 54,300 exhaustive-prefix comparisons, followed by `verification: PASS`. These computations are finite sanity checks; the general proof is the induction and calculus argument above.

## Relationship to prior work
Cheah and Treeby (arXiv:2604.20889, first posted 2026-04-19; primary MSC 11B37) establish the binary-tree parameterization of all positive Galileo sequences (their Theorem 5) and nonsharp two-sided power bounds for *monotone* integer sequences (their Theorem 12). The present result optimizes over **all** normalized positive integer sequences, without monotonicity, and identifies exact digit-wise pointwise minima and maxima and their best global asymptotic constants. Their parameterization is the closest structural predecessor; it is not claimed to be new here. Earlier work of May (1972), Zeitlin (1975), and Eğecioğlu (2017) concerns Galileo recurrences and examples. The binary-to-base-\(k\) digit map is classical as a Cantor-integer construction; the novelty asserted here is its simultaneous *sharp extremal role* for the dilation-constrained family and the exact two-sided oscillation constants, not the digit map by itself.

## Limitations
The theorem does not classify which values strictly between the two envelopes can occur at a fixed index. It does not assert independent review, priority certification, or a corresponding result for noninteger or nonpositive terms. Some older literature (especially May and Zeitlin) could not be materially read in full; implicit earlier coverage of the extremal interpretation remains a residual originality risk. The numerical verification only covers its indicated finite ranges.

## References
1. W. Cheah and D. Treeby, *Structure and Growth of Galileo Sequences*, arXiv:2604.20889, first submitted 2026-04-19, https://arxiv.org/abs/2604.20889.
2. K. O. May, *Galileo sequences, a good dangling problem*, American Mathematical Monthly 79 (1972), 67–69, DOI: 10.2307/2978135.
3. D. Zeitlin, *A family of Galileo sequences*, American Mathematical Monthly 82 (1975), 819–822, DOI: 10.2307/2319798.
4. Ö. Eğecioğlu, *A note on iterated Galileo sequences*, Discrete Mathematics, Algorithms and Applications 9 (2017), 1750015, DOI: 10.1142/S179383091750015X.
