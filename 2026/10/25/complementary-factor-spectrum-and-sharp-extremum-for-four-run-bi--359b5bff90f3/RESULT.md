# Complementary-factor spectrum and sharp extremum for four-run binary words

## Finding

For every quadruple of positive integers \(a,b,c,d\), put \(w=0^a1^b0^c1^d\) and \(n=a+b+c+d\). Let \(\mathcal F(w)\) be the set of its distinct nonempty **contiguous** factors, and let \(\overline{x}\) denote bitwise complementation. Define
\[
C(w)=|\{x\in\mathcal F(w):\overline{x}\in\mathcal F(w)\}|.
\]
Each member of a complementary pair is counted, so \(C(w)\) is even. Set
\[
\begin{aligned}
m&=\min\{\max(a,c),\max(b,d)\},\\
p&=\min(a,b),\quad q=\min(b,c),\quad r=\min(c,d),\\
h&=\min(a,b,c)\min(b,c,d).
\end{aligned}
\]
Then the exact complementary-factor count is
\[
\boxed{C(w)=2\bigl(m+pq+qr-h+\mathbf1_{\{b=c\}}pr\bigr).}
\]
More strongly, the polynomial that records the number of complementary factors at each length is given explicitly in the proof.

Let \(M_4(n)\) be the largest \(C(w)\) over length-\(n\) binary words with exactly four constant runs (equivalently, up to bit complementation, over the above quadruples). Then
\[
\boxed{M_4(5)=6,\qquad M_4(n)=2t(n-2t+1),\quad t=\left\lceil\frac n4\right\rceil,\ n=4\ \text{or}\ n\ge6.}
\]
For every \(n=4\) or \(n\ge6\), equality holds **exactly** for
\[
\boxed{b=c=t,\qquad 1\le a,d\le t,\qquad a+d=n-2t.}
\]
For \(n=5\), the two maximizing quadruples are \((1,1,1,2)\) and \((2,1,1,1)\). In particular,
\[
M_4(n)=\frac{n^2}{4}+\frac n2+O(1),
\]
whereas every four-run word with unequal interior run lengths \(b\ne c\) satisfies \(C(w)\le n^2/4\). The additive linear advantage of the extremizers therefore requires the **exact equality** of the two interior run lengths.

## Assumptions and scope

All four runs are nonempty; the word is linear, not circular. Factors are contiguous substrings, not scattered subsequences. Factor strings rather than their positions are counted. Complements must occur somewhere in the same word, not necessarily adjacent to their partners; complementary factors are counted twice, not once per unordered pair. No claim is made about words having five or more runs. The alphabet is exactly \(\{0,1\}\).

## Proof

**Classification and full length spectrum.** Define
\[
P_w(z)=\sum_{\ell\ge1}\#\{x\in\mathcal F(w):|x|=\ell,\ \overline{x}\in\mathcal F(w)\}\,z^\ell.
\]
For integers \(i,j\ge1\) let
\[
Q=\{(i,j): i\le b,\ j\le c,\ \bigl[(i\le a\ \text{and}\ j\le b)\ \text{or}\ (i\le c\ \text{and}\ j\le d)\bigr]\}.
\]
Then
\[
\boxed{\begin{aligned}
P_w(z)={}&2\sum_{k=1}^{m}z^k
+2\sum_{(i,j)\in Q}z^{i+j}\\
&+2\mathbf1_{\{b=c\}}
\sum_{i=1}^{p}\sum_{j=1}^{r}z^{b+i+j}.
\end{aligned}}
\]
To prove this, classify a nonempty factor by its number of constant runs. A one-run factor can appear together with its complement precisely for its length at most \(m\), giving the first summand. A two-run factor of type \(0^i1^j\) occurs either across the first \(01\) boundary (requiring \(i\le a,j\le b\)) or across the last \(01\) boundary (requiring \(i\le c,j\le d\)). Its complement \(1^i0^j\) occurs across the unique \(10\) boundary precisely when \(i\le b,j\le c\). Thus exactly the parameter pairs in \(Q\) contribute the two complementary strings \(0^i1^j\) and \(1^i0^j\).

A three-run factor with orientation \(010\) is \(0^i1^b0^j\), with \(1\le i\le a\) and \(1\le j\le c\); its complement \(1^i0^b1^j\) occurs as a three-run factor if and only if the entire interior zero-run has length \(c=b\), and \(i\le b,j\le d\). This produces the third summand. Any four-run factor starts with zero and ends with one, whereas its complement starts with one and ends with zero; a four-run factor of the latter orientation cannot occur in \(w\). Longer-run factors do not exist. The three displayed classes are disjoint, proving the polynomial.

The set \(Q\) is the union of the integer rectangles \([1,p]\times[1,q]\) and \([1,q]\times[1,r]\), whose intersection has \(\min(p,q)\min(q,r)=h\) points. Evaluating \(P_w(1)\) gives the count formula.

**Sharp extremal bound when \(b=c\).** Write \(b=c=t\). Put \(A=\min(a,t)\), \(D=\min(d,t)\). The two-run rectangle union has size \(t(A+D)-AD\); the three-run contribution has size \(AD\). The one-run contribution has size \(\max(t,\min(a,d))\). Hence
\[
\frac{C(w)}2=\max\{t,\min(a,d)\}+t\bigl(\min(a,t)+\min(d,t)\bigr).
\]
This is at most \(t(1+a+d)=t(n-2t+1)\), with equality if and only if \(a,d\le t\): if at least one is at most \(t\), the maximum term is exactly \(t\) and equality in the remaining estimate requires both outer runs at most \(t\); if both exceed \(t\), writing \(a=t+x,d=t+y\) with positive integers \(x,y\) leaves a strictly positive deficit \(t(x+y)-\min(x,y)\).

The concave integer quadratic \(t(n+1-2t)\) is maximized at an integer nearest \((n+1)/4\). In every residue class, \(t_*=\lceil n/4\rceil\) is a maximizing integer; when \(n\equiv1\pmod4\), the only other maximizing integer is \(t_*-1\), but its outer-run sum \(n-2(t_*-1)>2(t_*-1)\) makes equality impossible. For \(n=4\) and all \(n\ge6\), the condition \(2\le n-2t_*\le2t_*\) guarantees the existence of positive \(a,d\le t_*\) with the required sum. Thus these and only these quadruples attain the stated upper bound within \(b=c\).

**Unequal interior runs cannot maximize.** By reversal followed by complementation, which preserves \(C\), it suffices to treat \(b<c\). Put \(t=b\), \(A=\min(a,t)\), and \(D=\min(c,d)\). The two-run pair count is \(t(A+D)-A\min(D,t)\). If \(d\ge t\), then \(D\ge t\), so this count is \(tD\), while the one-run pair count is at most \(d\). As \(a\ge1\) and \(c\ge t+1\), one has \(d\le n-2(t+1)\). Therefore
\[
\frac{C(w)}2\le(t+1)d\le(t+1)\bigl(n-2(t+1)\bigr)\le\frac{n^2}{8},
\]
where the last inequality is an identity after completing the square. If instead \(d<t\), the one-run pair count is \(t\), and the two-run count is at most \(t(a+d)\), giving
\[
\frac{C(w)}2\le t(1+a+d)\le t(n-2t)\le\frac{n^2}{8}.
\]
The case \(b>c\) follows by the same reversal-complement symmetry. Hence every \(b\ne c\) obeys \(C(w)\le n^2/4\).

For \(n\ge6\), the attainable equality-case value \(2t_*(n-2t_*+1)\) exceeds \(n^2/4\), since \(t_*\) is within \(1/2\) of \((n+1)/4\), whence
\[
t_*(n-2t_*+1)\ge\frac{(n+1)^2}{8}-\frac12>\frac{n^2}{8}.
\]
This excludes all unequal-interior-run quadruples from the maximum and completes the equality classification. The cases \(n=4,5\) follow by inspecting the respectively one and four positive compositions into four parts.

## Verification

The accompanying self-contained Python program `verify.py` directly constructs sets of **distinct** contiguous factors, complements each factor, and compares every length coefficient against the classification for all \(7^4=2401\) positive quadruples with run lengths at most seven. It independently checks the exact finite-length maxima and every equality-case quadruple for every \(n\) from \(4\) to \(64\). The recorded result is `VERIFY_OK exhaustive_length_spectra=2401 extremal_lengths=4..64 (61)`.

The proof above is uniform in all positive run lengths; exhaustive finite checks are supplementary, not a proof of the unbounded statement. Run `python3 verify.py` without dependencies.

## Relationship to prior work

Currie, Dvořáková, Ochem, Opočenská, Rampersad and Shallit introduce complementary-factor avoidance classes and study the number of complemented factor **strings** in infinite words, together with repetition thresholds and associated complexity questions. Their 2022 preprint (published in 2025) motivates this finite fixed-run enumerative problem. Their results concern different quantifiers and objects: infinitely recurring pattern avoidance and critical exponents rather than a sharp extremum over all positive four-run compositions at a prescribed length. The present proof is self-contained and does not derive its polynomial or equality cases from those results.

Sawada, Stevens and Williams study complement-free constrained de Bruijn cycles, where a specified length is represented by exactly one of each complementary pair. The circular construction and its factor-set coverage problem differ from the present linear bounded-run simultaneous-occurrence count.

## Limitations

The result applies only to exactly four runs. It counts occurrences by distinct factor string rather than positions and does not handle scattered subsequences. It gives a sharp maximum but not the complete distribution of \(C(w)\) over all four-part compositions. An equivalent formulation in literature not discovered by the stated searches remains possible; the related prior work should be considered in any independent novelty assessment. No independent audit or external validation is claimed.

## References

1. J. Currie, Ľ. Dvořáková, P. Ochem, D. Opočenská, N. Rampersad, and J. Shallit, *Complement Avoidance in Binary Words*, arXiv:2209.09598 (first public 2022-09-20), https://arxiv.org/html/2209.09598v2 ; *Electronic Journal of Combinatorics* 32(4), #P4.24 (2025), DOI 10.37236/11555.
2. J. Sawada, B. Stevens, and A. Williams, *De Bruijn Sequences for the Binary Strings with Maximum Density*, WALCOM 2011, LNCS 6552, 182–190, DOI 10.1007/978-3-642-19094-0_19.
