# Arbitrarily long false completeness certificates for distinct squares

## Finding
For each integer \(B\ge18\), let
\[
S_B=\sum_{j=1}^{B}j^2=\frac{B(B+1)(2B+1)}6,\qquad Q_B=S_B+2,
\]
and let \(A_B\) be the strictly increasing infinite sequence
\[
A_B=(1,2,\ldots,B,Q_B,2Q_B,3Q_B,\ldots).
\]
Call a positive integer *good* if it is a sum of the squares of one or more terms of \(A_B\), using each sequence index at most once. Then, simultaneously for every \(B\ge18\):

1. \(128\) is bad and **every** integer in \([129,B^2]\) is good.
2. All four numerical hypotheses of Fuller--Nichols (2015), Theorem 6, hold with
   \[
   (k,n,r,b,\widehat N,x)=(2,1,1,B,129,4).
   \]
3. Despite those hypotheses, infinitely many arbitrarily large integers are bad: for each \(h\ge1\),
   \[
   hQ_B-1\quad\text{is bad}.
   \]

Consequently the generalized anti-Waring threshold \(N(2,1,1,A_B)\) does **not** exist. The failed finite completeness certificate has \(B^2-128\) consecutive good numbers, an unbounded number as \(B\to\infty\). Each \(A_B\) is strictly increasing, contains \(1\), has overall gcd \(1\), and is eventually an arithmetic progression of positive natural density \(1/Q_B\). The result disproves Theorem 6 under the stated generality of arbitrary nondecreasing positive integer sequences; it does not assert that any particular numerical table in the paper is false.

## Assumptions and scope
The parameter \(B\) ranges over all integers at least \(18\). A representation uses a finite, nonempty subset of pairwise distinct indices of \(A_B\); the summands are the **squares of the sequence values**, not the sequence values themselves. All assertions about Theorem 6 refer to the four conditions printed on page 5 (followed by the continuation of its proof on page 6) of the cited 2015 article. The source's convention for \(r=1\) makes its condition-3 sum empty and equal to zero.

## Proof
**1. The finite interval.** Define the exact bitset \(T_0=1\) and inductively
\[
T_j=T_{j-1}\mathbin{\mathrm{OR}}(T_{j-1}\ll j^2),\qquad1\le j\le18,
\]
where bit position \(t\) is one precisely when \(t\) is a sum of distinct squares chosen from \(1^2,\ldots,j^2\). Exhaustively evaluating this finite recurrence gives the following complete certificate:
\[
(T_{18}\gg128)\mathbin{\mathrm{AND}}1=0,\qquad
(T_{18}\gg129)\mathbin{\mathrm{AND}}(2^{196}-1)=2^{196}-1.
\]
In particular, \(128\) is not such a sum, and every integer from \(129\) through \(18^2=324\) is. The attached independent dictionary-based subset-sum recurrence reproduces both assertions, including \(2048\) distinct reachable total values through the full prefix range.

We now show *without invoking the contested theorem* that for every integer \(m\ge18\), all integers between \(129\) and \(m^2\) are sums of distinct squares with bases at most \(m\). The verified base case is \(m=18\). Assume the assertion at \(m\) and choose
\[
m^2<t\le(m+1)^2,\qquad u=t-(m-4)^2.
\]
For \(m\ge18\),
\[
129\le8m-15=m^2+1-(m-4)^2\le u
\le10m-15=(m+1)^2-(m-4)^2\le m^2.
\]
By induction \(u\) is a sum of distinct squares with bases at most \(m\). Such a representation **cannot** use \((m-4)^2\), because otherwise
\[
t=u+(m-4)^2\ge2(m-4)^2>(m+1)^2\ge t.
\]
The strict inequality follows from \(2(m-4)^2-(m+1)^2=m^2-18m+31\ge31\). Thus appending the unused square \((m-4)^2\) represents \(t\) by distinct squares. This completes the induction. In particular, all \([129,B^2]\) are represented using bases \(1,\ldots,B\), and consequently are good for \(A_B\). Any representation of \(128\) could only involve bases at most \(11\), so the finite certificate excludes \(128\) for every \(B\ge18\).

**2. All four printed conditions.** Take \(k=2\), \(n=r=1\), \(b=B\), \(\widehat N=129\), and \(x=4\). The initial term is \(a_1=1\). For the four numbered conditions of Theorem 6, we have respectively:
\[
\widehat N=129\le B^2+1-(B-4)^2=8B-15;
\qquad a_1=1\le B-4;
\]
\[
2(m-4)^2-(m+1)^2=m^2-18m+31\ge31>0
\quad(m\ge B),
\]
and
\[
(m+1)^2-(m-4)^2=10m-15\le m^2
\quad(m\ge B).
\]
The first two follow from \(B\ge18\); the last two follow from the displayed quadratics and their monotonicity for \(m\ge18\). Thus even the numerical inequality checks succeed for every required \(m\), not merely for finitely many values.

**3. Infinite modular obstruction.** A sum of squares drawn from the initial block \(1,\ldots,B\) lies in \([0,S_B]\). Every term later in \(A_B\) is divisible by \(Q_B\), hence its square is zero modulo \(Q_B\). Therefore every representable integer has residue modulo \(Q_B\) belonging to \(\{0,1,\ldots,S_B\}\). But \(S_B=Q_B-2\), so residue \(Q_B-1\) is omitted. In particular every \(hQ_B-1\), \(h\ge1\), is bad, proving there can be no eventual threshold.

The initial parameter \(B=18\) gives \(S_{18}=2109\), \(Q_{18}=2111\), and the explicit sequence \((1,2,\ldots,18,2111,4222,6333,\ldots)\). All \(129\) through \(324\) are good, but \(2110,4221,6332,\ldots\) are bad.

**4. Why the source's induction does not apply.** On page 6 of the 2015 article, the argument attempts to conclude from the badness of \(t\) and goodness of \(t-(m-x)^k\) that the latter representation necessarily contains the term \((m-x)^k\). Such an implication is justified when \(m-x\) is an eligible value of the sequence, but the published hypotheses do not require that. For \(A_B\), most integers \(m-4>B\) are not sequence values. The proof's additive extension step is therefore unavailable. A sufficient additional hypothesis to validate that step is that every integer \(m-x\), \(m\ge b\), occurs among the eligible sequence entries. This supplementary condition is not claimed necessary and does not automatically extend the theorem to sparse sequences such as primes.

## Verification
The accompanying standalone \(verify.py\) executes two independent exact finite subset-sum algorithms (large-integer bitsets and a dictionary of explicit witnesses). Both agree for all totals through \(2109\), exclude \(128\), and cover the complete interval \(129\) through \(324\). It also checks the four certificate inequalities at the appropriate endpoints for \(18\le B\le400\), and illustrates the infinite modular argument with sample moduli and indices. The proof above, rather than tests at bounded \(B\), establishes all quantified claims.

To reproduce: \(\texttt{python3 verify.py}\). No external packages are required.

## Relationship to prior work
Fuller, Prier and Vasconi (2014), Theorem 2.2, give a completeness certificate for the **unrestricted ordinary sequence of positive integers**. Their argument validly appends a square whose base is known to be available. Fuller and Nichols (2015), Theorem 6, extend the wording to **arbitrary nondecreasing positive integer sequences**, but the transition does not retain the availability premise. Their Table 1 already lists the numerical triple \((\widehat N,x,b)=(129,4,18)\) in the unrestricted case. The present construction keeps those successful local checks unchanged while modifying only the infinite tail of admissible bases.

LeVan and Prier (2017) study bounds for the ordinary anti-Waring number and do not state a theorem covering arbitrary sequences with the claimed implication. The standard known value \(N(2,1)=129\) for all positive-integer square bases is compatible with this finding. The discrepancy concerns the **generalized sufficiency theorem**, not the original classical anti-Waring result or a demonstration that any tabulated numerical threshold is numerically wrong.

## Limitations
The construction disproves the printed general theorem and produces an infinite family of witnesses. It does not classify all sequences for which a finite completeness certificate is sound; the additional full-tail-availability condition is only sufficient, not characterized as optimal. The analysis does not independently check any claimed threshold for primes or fixed residue progressions. A literature search did not locate an earlier explicit correction, but an unlocated erratum or equivalent argument remains possible. Independent mathematical validation has not been performed.

## References
1. C. Fuller and R. H. Nichols, Jr., *Generalized Anti-Waring Numbers*, **Journal of Integer Sequences** 18 (2015), Article 15.10.5, Theorem 6 and Tables 1--6. Published 2015-09-24. https://www.maths.tcd.ie/EMIS/journals/JIS/VOL18/Fuller/fuller2.pdf
2. C. Fuller, D. R. Prier and K. A. Vasconi, *New Results on an Anti-Waring Problem*, **Involve** 7 (2014), 239--244, Theorems 2.1--2.2. https://msp.org/involve/2014/7-2/involve-v7-n2-p09-p.pdf
3. P. LeVan and D. Prier, *Improved Bounds on the Anti-Waring Number*, **Journal of Integer Sequences** 20 (2017), Article 17.8.7. https://cs.uwaterloo.ca/journals/JIS/VOL20/Prier/prier3.pdf
4. OEIS A001661, *Largest number not the sum of distinct positive n-th powers* (background on the classical square case). https://oeis.org/A001661
