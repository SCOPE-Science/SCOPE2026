# Fibonacci return-gap spectra and an infinite-mean limit law for the Baum–Sweet word

## Finding

Let \(b\) be the Baum–Sweet binary word, with \(b(0)=1\) and, for each positive integer \(n\), \(b(n)=1\) exactly when every maximal block of zeros in its standard base-two expansion has even length. For \(N\geq1\), write \(S_N=\{0\leq n<2^N:b(n)=1\}\), in increasing order, and let \(G_N(d)\) count adjacent elements of \(S_N\) whose difference is \(d\). Thus a gap of \(d\) corresponds to the return factor \(10^{d-1}\).

Set \(F_0=0\), \(F_1=1\), \(F_{j+2}=F_{j+1}+F_j\), and for \(j\geq2\) set
\[
h_j=2^{j-2}+\begin{cases}2,&j\text{ even},\\1,&j\text{ odd}.\end{cases}
\]
For every \(N\geq1\), the **entire** finite return-gap multiplicity spectrum is
\[
|S_N|=F_{N+2},\qquad
G_N(1)=\left\lceil\frac N2\right\rceil,\qquad
G_N(2)=\left\lfloor\frac N2\right\rfloor,
\]
and, for all integers \(d\geq3\),
\[
G_N(d)=\sum_{j=2}^{N-1}\mathbf1_{\{d=h_j\}}\bigl(F_{N-j+2}-1\bigr).
\]
The sum is empty when \(N\leq2\). The two distinct indices \(j=2,3\) both contribute the same gap \(h_2=h_3=3\); all later values \(h_j\) are strictly increasing. In particular, the complete set of return lengths in the infinite word is \(\{1,2,3\}\cup\{h_j:j\geq4\}\).

Let \(\varphi=(1+\sqrt5)/2\), and choose a consecutive pair uniformly among the \(F_{N+2}-1\) pairs in \(S_N\). Its gap converges in distribution on the positive integers to the probability law
\[
\mu(1)=\mu(2)=0,\quad \mu(3)=\varphi^{-1},\quad
\mu(h_j)=\varphi^{-j}\quad(j\geq4),
\]
with zero mass elsewhere. For \(j\geq4\), its exact tail is \(\mu([h_j,\infty))=\varphi^{2-j}\). This limiting law has **infinite expectation**, although each finite-window distribution has finite mean; in fact the latter mean is
\[
\frac{2^N-1}{F_{N+2}-1}\sim \frac{\sqrt5}{\varphi^2}\left(\frac2\varphi\right)^N.
\]

## Assumptions and scope

Indices start at zero. Binary expansions of positive integers have no leading zeros; \(0\) is declared to have word value one. The interval \([0,2^N)\) includes its left endpoint and excludes its right endpoint. Only adjacent **selected indices inside this interval** are counted, not the gap across its right endpoint. Limits concern counting frequencies of consecutive selected-index gaps as \(N\to\infty\), not densities of ones in the ambient integer line. All formulas apply for every integer \(N\geq1\) and every positive integer gap \(d\).

## Proof

**1. Binary suffix languages.** For \(\ell\geq0\), let \(T_\ell\) be the integers represented by **exactly** \(\ell\) binary digits from the regular language \((1\mid00)^*\); digits may begin with a pair \(00\) but not with a single zero. In particular \(T_0=\{0\}\) represents the empty word and \(T_1=\{1\}\). Sorting by value and splitting by the initial token gives, for \(\ell\geq2\), the disjoint, ordered union
\[
T_\ell=T_{\ell-2}\;\dot\cup\;\bigl(2^{\ell-1}+T_{\ell-1}\bigr).
\]
Consequently \(|T_\ell|=F_{\ell+1}\). Its smallest element is zero when \(\ell\) is even and one when \(\ell\) is odd; its largest is \(2^\ell-1\). The two ordered pieces above are separated by a unique bridge of length
\[
(2^{\ell-1}+\min T_{\ell-1})-(2^{\ell-2}-1)
=2^{\ell-2}+1+\min T_{\ell-1}=h_\ell.
\]
Every adjacent difference within \(T_\ell\) is therefore inherited from \(T_{\ell-1}\) or \(T_{\ell-2}\), or is this one bridge.

**2. Tracking bridges rather than only numerical gaps.** Fix \(j\geq2\). Distinguish bridges by their generation \(j\), including the coincidence \(h_2=h_3\). The number \(M_\ell(j)\) of inherited bridges of type \(j\) in \(T_\ell\) is zero for \(\ell<j\), equals one at \(\ell=j\), and subsequently satisfies
\[
M_\ell(j)=M_{\ell-1}(j)+M_{\ell-2}(j).
\]
It follows inductively that \(M_\ell(j)=F_{\ell-j+1}\) for \(\ell\geq j\). All internal gaps are accounted for by these labeled bridges.

**3. Joining the binary-length shells.** The positive elements of \(S_N\) with standard binary length \(L\), for \(1\leq L\leq N\), are precisely \(2^{L-1}+T_{L-1}\). Along with the isolated element zero, these shells appear in increasing order. The boundary gap from shell length \(L\) to the next shell is \(1+\min T_L\), for \(0\leq L<N\), where shell zero denotes \(\{0\}\). Thus \(L\) even contributes a gap of one and \(L\) odd contributes a gap of two. The counts are exactly \(\lceil N/2\rceil\) and \(\lfloor N/2\rfloor\). For each bridge type \(j\), the internal shell contributions sum to
\[
\sum_{\ell=j}^{N-1}F_{\ell-j+1}=F_{N-j+2}-1.
\]
The shell sizes give \(|S_N|=1+\sum_{\ell=0}^{N-1}F_{\ell+1}=F_{N+2}\). Distinct bridge types are aggregated when their numerical gaps coincide, proving the complete formula.

**4. Limiting law and mean.** For each fixed \(j\geq2\), Binet's Fibonacci asymptotic gives
\[
\lim_{N\to\infty}\frac{F_{N-j+2}-1}{F_{N+2}-1}=\varphi^{-j}.
\]
The boundary gaps have limiting frequency zero. Because \(\sum_{j=2}^\infty\varphi^{-j}=1\), the pointwise limits exhaust the total probability mass, so the probability measures converge (indeed, in total variation) on the countable set of positive integers. The duplicate values \(h_2=h_3=3\) combine to \(\varphi^{-2}+\varphi^{-3}=\varphi^{-1}\). For \(j\geq4\), summing the geometric tail gives \(\sum_{i=j}^\infty\varphi^{-i}=\varphi^{2-j}\). Since \(h_j\geq2^{j-2}\) and \(2/\varphi>1\), the series \(\sum_{j\geq4}h_j\varphi^{-j}\) diverges: the limit law has infinite mean. Finally \(\min S_N=0\), \(\max S_N=2^N-1\), so the sum of all consecutive gaps is \(2^N-1\). Division by the exact number \(F_{N+2}-1\) of gaps, followed by Binet's formula, gives the stated finite means and asymptotic.

## Verification

The standalone `verify.py` independently constructs the Baum–Sweet support by testing the lengths of **all actual runs of zero digits** in ordinary binary expansions. For each \(1\leq N\leq18\), it directly enumerates all \(2^N\) integers, forms every adjacent difference, compares its complete multiset against the Fibonacci formula, verifies the number of support elements, and checks that the total gap length telescopes to \(2^N-1\). Executing `python3 verify.py` prints `VERIFY_OK`. This finite test is an independent check of instances; the proof above establishes all exponents.

## Relationship to prior work

The Baum–Sweet word and its automatic description originate in Baum and Sweet (1976) and are surveyed by Allouche (1993). OEIS A060142 records exactly its one-position set, as a self-generated integer sequence. OEIS A219608 is the odd subsequence of A060142, and OEIS A219609 explicitly tabulates half of its consecutive differences. Since the odd elements of A060142 are exactly twice all its elements plus one, A219609 is **exactly the already-tabulated complete consecutive-gap sequence**. Neither the gap sequence nor its initial terms are asserted to be new here. The claim is the uniform **Fibonacci formula for the multiplicity of every gap at every binary cutoff**, together with the exact limiting distribution, its power-geometric tail and infinite mean. The inspected sequence records give a definition, finite tables, and elementary subsequence identities, but do not state these quantitative theorems. The Allouche survey discusses the automaton, not the all-scale gap histogram. A general gap theorem for automatic sequences does not give this exact distribution. Kimberling's (2000) differently-generated set uses the rules \(x\mapsto2x\) and \(x\mapsto4x-1\), rather than the A060142 rules \(x\mapsto2x+1\) and \(x\mapsto4x\), so its Beatty-rank theorem does not cover the present statement.

## Limitations

The convergence is at dyadic cutoffs and is normalized by the number of selected-index gaps, not by the integer length of the observation window. No general law for arbitrary real cutoffs is asserted. The exact gap **sequence** is already known from OEIS A219609, and an uncatalogued existing derivation of the frequency formula or limit distribution remains a possible originality risk. The proof uses elementary regular-language recurrences and requires no assertion about uniqueness of a literature search. It is not an independent formal verification.

## References

1. L. E. Baum and M. M. Sweet, *Continued Fractions of Algebraic Power Series in Characteristic 2*, Annals of Mathematics 103 (1976), 593–610.
2. J.-P. Allouche, *Finite automata and arithmetic* (1993), https://www.mat.univie.ac.at/~slc/opapers/s30allouche.pdf.
3. C. Kimberling, OEIS A060142, *Ordered set S defined by these rules*, https://oeis.org/A060142 (created 2001-03-05).
4. R. Zumkeller, OEIS A219608, *Odd terms in A060142*, https://oeis.org/A219608 (2012).
5. R. Zumkeller, OEIS A219609, *Half of first differences of A219608*, https://oeis.org/A219609 (2012); see the listed 10,000-entry gap table.
6. C. Kimberling, *A Self-Generating Set and the Golden Mean*, Journal of Integer Sequences 3 (2000), Article 00.2.8, https://cs.uwaterloo.ca/journals/JIS/VOL3/goldentext.html (a different generating rule).
