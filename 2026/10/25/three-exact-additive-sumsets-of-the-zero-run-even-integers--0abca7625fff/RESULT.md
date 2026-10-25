# Three exact additive sumsets of the zero-run-even integers

## Finding

Let \(A\) consist of \(0\) and the positive integers whose ordinary base-two expansions have no maximal run of zeros of odd length. This set is OEIS A060142: the positive elements coincide with the 1-positions of the Baum–Sweet sequence OEIS A086747. The two OEIS sequences differ at zero, and \(0\in A\) is part of the theorem’s definition. Then

\[
A+A=\mathbb N_0,\qquad A+2A=\mathbb N_0,\qquad
A+4A=\mathbb N_0\setminus\{n:n\equiv2\pmod4\}.
\]

Here \(A+cA=\{a+cb:a,b\in A\}\), and \(\mathbb N_0=\{0,1,2,\ldots\}\). In particular, this zero-density set is an additive basis of **optimal order two**, since \(2\notin A\). Moreover, for every integer \(k\ge0\),

\[
\#(A\cap[0,2^k))=F_{k+2},\qquad F_0=0,\ F_1=1,\ F_{j+2}=F_{j+1}+F_j.
\]

Consequently the dyadic counting growth exponent is \(\log_2((1+\sqrt5)/2)\), strictly less than one. This counting law supplies standard sparsity context; the additive sumset identities are the new focus.

## Assumptions and scope

All variables denoting members of \(A\) are nonnegative integers. The binary expansion has no leading zeros; the binary expansion of \(0\) is the one-character word `0`, whose single zero-run would otherwise be odd. We explicitly include \(0\), as in OEIS A060142 (or the alternative Baum–Sweet initial-value convention \(a(0)=1\)); OEIS A086747 currently uses \(a(0)=0\). The zero-run condition applies only to positive integers. Empty sums are not used. Equality of sets is equality for every nonnegative integer, not asymptotic coverage.

## Proof

**Binary decomposition.** A positive allowed binary word starts with `1` and, after that initial `1`, is uniquely a concatenation of tiles `1` and `00`. Splitting on the least significant bits gives the disjoint identity

\[
A=4A\;\sqcup\;(8A+1)\;\sqcup\;(4A+3).
\tag{1}
\]

Indeed, allowed words end either in `00`, in `01` with the `0` run having even length (then the final suffix is `001`, or the whole word is `1`), or in `11` (with `1` itself covered as \(8\cdot0+1\)). Formally, all nonzero allowed words with final digit `1` either end in `11` or have their final `1` preceded by at least two zeros; removing the final `001` preserves admissibility. Conversely, appending `00`, `001`, or `11` to admissible prefixes with leading zeros interpreted carefully gives the three progressions; the two special short strings `1`, `11` are directly included. This also follows mechanically by inspecting the final runs. Specifically, the equivalences are \(4m\in A\iff m\in A\), \(8m+1\in A\iff m\in A\), \(4m+3\in A\iff m\in A\). The remaining residue class \(2\pmod4\) and class \(5\pmod8\) never belong to \(A\).

**Simultaneous strong induction.** Write \(X(n)\) for \(n\in A+A\) and \(Y(n)\) for \(n\in A+2A\). They both hold at \(n=0\). Suppose both hold for every smaller index. The recurrences are constructive; lowercase \(a,b\) in the following arguments always belong to \(A\) by the induction hypothesis.

For \(X(n)\):

* If \(n=4m\), choose \(m=a+b\); then \(n=4a+4b\).
* If \(n=4m+1\), choose \(m=a+2b\); then \(n=4a+(8b+1)\).
* If \(n=4m+2\) with \(m\ge1\), choose \(m-1=a+b\); then \(n=(4a+3)+(4b+3)\). For \(n=2\), use \(1+1\).
* If \(n=4m+3\), choose \(m=a+b\); then \(n=4a+(4b+3)\).

For \(Y(n)\):

* If \(n=4m\), choose \(m=a+2b\); then \(n=4a+2(4b)\).
* If \(n=4m+3\), choose \(m=a+2b\); then \(n=(4a+3)+2(4b)\).
* If \(n=4m+2\) with \(m\ge1\), choose \(m-1=a+2b\); then \(n=4a+2(4b+3)\). For \(n=2\), use \(0+2\cdot1\).
* If \(n=8r+1\), choose \(r=a+b\); then \(n=(8a+1)+2(4b)\).
* If \(n=8r+5\) with \(r\ge1\), choose \(2r-1=a+2b\); then \(n=(4a+3)+2(4b+3)\). For \(n=5\), use \(3+2\cdot1\).

Every invoked index is strictly smaller than \(n\), and every displayed summand belongs to \(A\) by (1). Thus both \(X(n)\) and \(Y(n)\) hold for all \(n\ge0\).

**The fourth dilate.** By (1), every element of \(A\) is congruent to \(0\), \(1\), or \(3\) modulo \(4\), so no element of \(A+4A\) is \(2\pmod4\). Conversely, with \(m=a+b\) or \(m=a+2b\) supplied by the preceding identities:

\[
4m=(4a)+4b,\quad 4m+3=(4a+3)+4b,
\quad 4m+1=(8b+1)+4a.
\]

The first two formulas use \(m=a+b\), and the third uses \(m=a+2b\); all summands belong to \(A\). This proves exact equality.

**Counting.** A positive allowed binary word of length \(\ell\) consists of a leading `1` followed by tilings of \(\ell-1\) positions with tiles of length one (`1`) and two (`00`). There are exactly \(F_\ell\) such words. Counting positive lengths from \(1\) through \(k\) and adding zero gives \(1+\sum_{\ell=1}^kF_\ell=F_{k+2}\). Since \(F_{k+2}=\Theta(\varphi^k)\) with \(\varphi=(1+\sqrt5)/2<2\), the set has zero natural density.

## Verification

The standalone `verify.py` separately checks the zero-run definition against (1) for integers through \(50{,}000\); constructs and directly validates both inductive representations through the same range; verifies the mixed-dilate formula and brute-force coverage through \(4{,}096\); and checks the dyadic Fibonacci formula through \(k=14\). Every assertion passes. These finite checks supplement, but do not replace, the universal arguments above.

## Relationship to prior work

Dekking's *Sumsets and fixed points of substitutions* (first public version 11 May 2021) motivates determining exact two-fold sumsets of supports of morphic/automatic sequences and establishes other examples (Fibonacci, Thue–Morse, von Neumann, sums of squares). Its inspected sections do not present the zero-run-even integer set or the three equalities above. The zero-run-even integer set (OEIS A060142), its known Fibonacci-type distribution, and the Baum–Sweet digit rule are standard; the proposed contribution is the exact additive representation and its first two natural dilation variants, not automaticity or the known Fibonacci growth.

## Limitations

The set equations cover only additive coefficients \(1,2,4\) and make no assertion for arbitrary dilations. The original 2021 methodology might imply some identities indirectly; the theorem's priority has not been independently established. Finite verification alone would not show the infinite claim, which is instead proved by (1) and strong induction.

## References

1. F. Michel Dekking, *Sumsets and fixed points of substitutions*, arXiv:2105.04959 (first public 11 May 2021); *Proceedings of the American Mathematical Society, Series B* **9** (2022), 393–403, doi:10.1090/bproc/132.
2. OEIS A060142, the zero-run-even integer set including zero, with generating rule \(0\in A\), \(x\mapsto2x+1\), \(x\mapsto4x\).
3. OEIS A086747, Baum–Sweet sequence with \(a(0)=0\) as currently recorded, and discussion of the alternative initial value.
