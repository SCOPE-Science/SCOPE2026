# The exact sharp gap for complex Schatten-four Schur idempotents

## Finding

Let \(I,J\) be finite or countable sets and \(S_4(I,J)\) the complex Schatten-four class of operators from \(\ell_2(J)\) to \(\ell_2(I)\). For a zero-one array \(E=(e_{ij})_{i\in I,j\in J}\), suppose its entrywise Schur projection \(T_E(A)=(e_{ij}a_{ij})\) is bounded on \(S_4(I,J)\). Set \(\tau\) equal to the unique positive root of
\[
 \tau^3+4\tau^2+3\tau-1=0,
\]
and put
\[
 \kappa=\left(1+\frac{\tau(3\tau+4)}{(1+\tau)^4(\tau^2+4\tau+2)}\right)^{1/4}
 =1.0375410061056345\ldots .
\]
Then
\[
 \boxed{\ \|T_E\|=0,\quad \|T_E\|=1,\quad\text{or}\quad\|T_E\|\ge\kappa.\ }
\]
The positive gap is *sharp*: \(\kappa\) is attained by the \(2\times2\) triangle Schur mask \(\Delta=\left(\begin{smallmatrix}1&1\\1&0\end{smallmatrix}\right)\). In particular, \((1,\kappa)\) contains no norm of a complex Schatten-four zero-one Schur projection. The exact gap is \(\kappa-1=0.0375410061056345\ldots\).

## Assumptions and scope

The scalar field is \(\mathbb C\), the Schatten exponent is exactly \(4\), and both matrix index sets are finite or countable. The norm is the *ordinary* induced \(S_4\)-operator norm, not a completely bounded norm. The zero-one condition makes \(T_E\) an idempotent. For countable index sets, only bounded Schur projections are in scope. A zero multiplier has norm zero.

## Proof

**Step 1: a complete two-by-two reduction.** For any complex \(A=\left(\begin{smallmatrix}a&z\\w&b\end{smallmatrix}\right)\), the two singular values satisfy
\[
 \|A\|_4^4=(|a|^2+|b|^2+|z|^2+|w|^2)^2-2|ab-zw|^2.
\]
Write \(\alpha=|a|\), \(\beta=|b|\), \(s=|z|^2+|w|^2\), and \(r=|zw|\). Necessarily \(s\ge2r\). The fourth power of the numerator for \(T_\Delta\) is
\[
 N=(\alpha^2+s)^2-2r^2,
\]
while the fourth power of the denominator is at least
\[
 D_0=N+\beta^4+2s\beta^2-4\alpha\beta r.
\]
Equality is attainable by choosing the phase of \(ab\) opposite that of \(zw\). Let \(K\ge1\) denote the supremum of the norm ratios for *balanced* entries \(|z|=|w|\) and this adverse phase. At the smallest admissible \(s=2r\), the definition of \(K\) gives \(K^4D_0-N\ge0\). For fixed \(\alpha,\beta,r\), the expression
\[
 (K^4-1)\big((\alpha^2+s)^2-2r^2\big)
 +K^4(\beta^4+2s\beta^2-4\alpha\beta r)
\]
is nondecreasing for \(s\ge2r\), so every complex \(A\) has ratio at most \(K\). If \(r=0\), then \(\|T_\Delta A\|_4\le\|A\|_4\) directly from the same formula. Conversely, balanced complex matrices with adverse phase are included in the full domain. Therefore \(\|T_\Delta\|=K\).

Scaling balanced nonzero off-diagonal entries to modulus one and adjusting diagonal and row/column phases reduces this supremum to real matrices \(\left(\begin{smallmatrix}a&1\\1&b\end{smallmatrix}\right)\) with \(a,b\in\mathbb R\). Their fourth-power ratio is
\[
 R(a,b)=\frac{a^4+4a^2+2}{a^4+b^4+4(a^2+b^2+ab)+2}.
\]
For each fixed real \(a\), the denominator is strictly convex in \(b\) and its unique minimizer solves \(b^3+2b+a=0\). Parameterize \(a=-b^3-2b\), and let \(t=b^2\ge0\). Direct expansion gives
\[
 R(-b^3-2b,b)=1+\frac{t(3t+4)}{(1+t)^4(t^2+4t+2)}.
\]
Differentiation shows its derivative has the sign of \(1-3t-4t^2-t^3\) for \(t>0\). The cubic \(t^3+4t^2+3t-1\) is strictly increasing on \([0,\infty)\), starts negative, and tends to infinity, so its unique positive zero \(\tau\) is the unique global maximum. At \(t=0\) and in the limit \(t\to\infty\) the ratio equals one. Hence \(\|T_\Delta\|_4=\kappa\), with an explicit maximizing matrix obtained by taking \(b=\sqrt\tau\), \(a=-b^3-2b\), and \(z=w=1\).

**Step 2: the universal gap.** Call a zero-one array *triangle-free* when it has no \(2\times2\) subarray with exactly three ones. If it is not triangle-free, row and column compressions isolate such a subarray; permutations identify its Schur multiplier with \(T_\Delta\). Since multiplication on either side by coordinate projections is Schatten-four contractive, \(\|T_E\|\ge\|T_\Delta\|=\kappa\).

If a zero-one array is triangle-free, any two nonzero rows whose sets of one-positions overlap have exactly the same support: differing supports would exhibit a three-one subarray. Thus its support splits into disjoint all-one rectangles \(R_k\times C_k\), where the \(R_k\)'s are mutually disjoint and likewise the \(C_k\)'s. With corresponding orthogonal coordinate projections \(P_k,Q_k\),
\[
 T_E(A)=\sum_k P_k A Q_k.
\]
For finitely many blocks, first compress to the unions of their row and column supports, then average \(U_\varepsilon A V_\varepsilon\) over independent signs \(\varepsilon_k\), where the two diagonal unitaries use the *same* sign on \(R_k\) and \(C_k\). Cross-block terms cancel and the displayed block sum remains. Unitary invariance and compression contractivity give \(\|T_E(A)\|_4\le\|A\|_4\). Truncating to finitely many coordinate blocks and taking the Schatten-four limit gives the same inequality on countable sets. Every nonzero mask fixes some matrix unit, hence its norm equals one. The zero mask has norm zero. This proves the trichotomy and sharpness. \(\square\)

## Verification

The accompanying `verify.py` is a standalone Python standard-library verifier. Execute `python3 verify.py`. It checks two integer polynomial identities using 27 evaluation points (more than their degree bound of 12), exhausts all zero-one masks of sizes \(2\times2\), \(2\times3\), and \(3\times3\) for the triangle/block criterion, evaluates the maximizing witness and algebraic root, and tests the sharp bound on 25,000 reproducible random complex \(2\times2\) inputs. The finite tests are corroboration; Steps 1 and 2 are analytic proofs over all admissible matrices and index sets.

## Relationship to prior work

Banks and Harcharras (2004) established a nonzero gap above one for noncontractive idempotent Schur multipliers in general non-Hilbert Schatten classes and identified the two-by-two triangle mask as its sharp obstruction. They explicitly left the *precise* triangle-mask multiplier norm open for \(2<p<\infty\). The present result settles its exact value at \(p=4\) and thereby determines the sharp gap for that exponent. Doust and Gillespie (2005) treated boundedness classes and contraction of disjoint rectangular blocks, rather than the exact triangle-mask Schatten-four norm. Levene (2013) computed norm gaps for Schur multipliers acting on bounded-operator spaces; these are the \(p=\infty\) rather than \(p=4\) norms. These comparisons concern statements and their implications, not just titles.

## Limitations

No formula is claimed for other Schatten exponents or for completely bounded multiplier norms. This is a single-class sharp quantitative result, not a general solution to the original variable-exponent question. Published-source comparison cannot exclude an equivalent calculation under different notation; the related early work on random zero-one matrix norms was available only through abstracts in this inspection.

## References

1. W. D. Banks and A. Harcharras, “On the norm of an idempotent Schur multiplier on the Schatten class,” *Proceedings of the American Mathematical Society* **132** (2004), 2121–2125. DOI: `10.1090/S0002-9939-04-07340-X`. Publicly available electronically February 6, 2004; particularly Lemmas 1–3 and the discussion on page 2123.
2. I. Doust and T. A. Gillespie, “Schur multiplier projections on the von Neumann–Schatten classes,” *Journal of Operator Theory* **53** (2005), 251–272. Lawful author preprint: `https://web.maths.unsw.edu.au/~iand/Papers/Schur/schurcpjotf.pdf`.
3. R. H. Levene, “Norms of idempotent Schur multipliers,” arXiv:`1302.4849` (2013), particularly the introduction and Theorem 1.1 (bounded-operator norms).
4. I. Doust, “Norms of 0-1 matrices in \(C_p\),” *Geometric Analysis and Applications* **39** (2001), 50–55. Bibliographic/abstract-level comparison only.
