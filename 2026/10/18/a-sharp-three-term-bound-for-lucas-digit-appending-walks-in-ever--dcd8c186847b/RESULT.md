# A sharp three-term bound for Lucas digit-appending walks in every base

## Finding

Let \(L_0=2\), \(L_1=1\), and \(L_{n+2}=L_{n+1}+L_n\). In an integer base \(b\ge2\), a *one-digit-appending Lucas walk* is a strictly increasing finite sequence of distinct positive Lucas values \(a_0,a_1,\ldots,a_{h-1}\) such that, for each successive pair, there is a digit \(d\in\{0,1,\ldots,b-1\}\) with \(a_{i+1}=b a_i+d\).

**Theorem.** Every such walk, in every base, has at most three terms (two appending transitions). This bound is sharp for infinitely many bases: if \(k\ge3\) is odd, then in base \(b=L_k\) there is the walk \(1\to L_k\to L_{2k}\), with appended digits \(0,2\), since \(L_{2k}=L_k^2+2\).

There is also an exact structural classification above the initial exceptional values. Whenever a three-term walk begins at \(L_x\) with \(x\ge2\), it has **precisely** the form
\[
L_x\longrightarrow L_{x+k}\longrightarrow L_{x+2k},\qquad
b=L_k,\qquad 3\le x<k,\quad x,k\text{ odd},
\]
with appended digits \(L_{k-x}\) and \(L_x\), respectively. Conversely, every pair of odd integers \(x,k\) satisfying \(3\le x<k\) gives a valid three-term walk in base \(L_k\). Here *three-term* means three values, not three transitions.

## Assumptions and scope

The Lucas values are taken as a set of positive integers, with the small values ordered as \(1,2,3,4,7,11,\ldots\); although \(L_0=2>L_1=1\), a walk is ordered by increasing *value*. From index \(2\) onward, the Lucas sequence is strictly increasing. The base stays fixed throughout each walk. Leading zeros in a *single appended digit* are permitted (digit \(0\)); no digit replacement, insertion at the left, or block of multiple digits is allowed. The result holds for every integer base \(b\ge2\), with no upper bound on the starting value or the base.

## Proof

**1. Adjacent index jumps must coincide.** Consider two consecutive appending transitions starting at \(L_x\) for \(x\ge2\). They give positive integers \(k,\ell\) and a base \(b\ge2\) with
\[
L_{x+k}=bL_x+d_1,\qquad
L_{x+k+\ell}=bL_{x+k}+d_2,\qquad 0\le d_1,d_2<b.
\]
Write \(a=L_x\), \(c=L_{x+k}\), \(u=c/a\), and \(v=L_{x+k+\ell}/c\). Since \(a\ge3\) and \(c\ge4\), the appending inequalities imply
\[
\frac{3}{4}\le\frac{a}{a+1}<\frac{v}{u}<1+\frac1c\le\frac54<\frac43.\tag{1}
\]
Indeed \(b\le u<b(1+1/a)\) and \(b\le v<b(1+1/c)\). The usual addition identity for Lucas and Fibonacci numbers, where \(F_0=0,F_1=1,F_{j+2}=F_{j+1}+F_j\), is
\[
\frac{L_{m+j}}{L_m}=F_{j+1}+F_j\frac{L_{m-1}}{L_m}.\tag{2}
\]
For \(m\ge2\), the ratio \(L_{m-1}/L_m\) belongs to \([1/3,3/4]\); for \(m\ge3\) it belongs to \([4/7,3/4]\). These claims follow from \(L_1/L_2=1/3\), \(L_2/L_3=3/4\), \(L_3/L_4=4/7\), and the recurrence \(r_{m+1}=1/(1+r_m)\), whose invariant intervals are the displayed ones.

If \(\ell\ge k+1\), identity (2) implies
\[
v\ge F_{k+2}+\tfrac47F_{k+1},\qquad
u\le F_{k+1}+\tfrac34F_k.
\]
The difference between three times the former lower bound and four times the latter upper bound equals \(\tfrac57F_{k+1}>0\). Thus \(v/u>4/3\), contrary to (1). If \(\ell\le k-1\), necessarily \(k\ge2\), and (2) gives
\[
v\le F_k+\tfrac34F_{k-1},\qquad
u\ge F_{k+1}+\tfrac13F_k.
\]
Four times the first right side equals three times the second, by \(F_{k+1}=F_k+F_{k-1}\). Consequently \(v/u\le3/4\), again contradicting (1). We conclude that \(\ell=k\).

**2. Determine the base and parity.** The standard Lucas product identity is
\[
L_{r+s}=L_rL_s-(-1)^sL_{r-s}\qquad(r\ge s\ge0).\tag{3}
\]
Taking \(r=x+k\) and \(s=k\) gives \(L_{x+2k}=L_kL_{x+k}-(-1)^kL_x\). Let \(q=L_k-b\). Hence the digit in the second transition is
\[
d_2=q c-(-1)^k a.\tag{4}
\]
If \(k\) is odd, then \(d_2=qc+a\). Since \(c\ge ba\) and \(a\ge3\), a positive \(q\) makes \(d_2\ge c+a>b\), while a negative \(q\) makes \(d_2\le a-c<0\). Thus \(q=0\), giving \(b=L_k\) and \(d_2=a<b\). In particular \(L_x<b=L_k\), so monotonicity forces \(x<k\).

If \(k\) is even, then \(d_2=qc-a\). A nonpositive \(q\) makes the digit negative. For positive \(q\), \(d_2\ge c-a\). For every \(x\ge2\) and \(k\ge2\), the difference \(L_{x+k}-L_x\) is increasing in \(x\), since successive differences increase by \(L_{x+k-1}-L_{x-1}>0\). Its minimum is \(L_{k+2}-L_2=L_{k+1}+L_k-3\ge L_k\). Hence \(d_2\ge L_k>b\), impossible. Therefore \(k\) is odd and \(b=L_k\).

Applying (3) with \(r=k\), \(s=x<k\) yields
\[
d_1=L_{x+k}-L_kL_x=-(-1)^xL_{k-x}.\tag{5}
\]
The nonnegative digit condition forces \(x\) odd. Since \(x\ge2\), this means \(x\ge3\); also \(k>x\), so \(k\ge5\). Equations (4) and (5) give the claimed digits. Conversely, for all such odd \(x,k\), equations (3)–(5) show that \(L_{x+k}=L_kL_x+L_{k-x}\) and \(L_{x+2k}=L_kL_{x+k}+L_x\), with both digits strictly between \(0\) and \(L_k\). This proves the classification.

**3. Exclude four-term walks.** Suppose \(a\to c\to e\to f\) were a four-term walk. If \(c\ge3\), the classification applied to its last three terms would imply \(c<b\); the first transition yields \(c=ba+d\ge b\), a contradiction. The only remaining case is \(c=2\), since the Lucas values are positive and strictly increase along the walk. Then necessarily \(a=1\), \(b=2\), and \(d=0\). The next Lucas value in \([2c,2(c+1))=[4,6)\) is \(e=4\), but there is no Lucas value in \([8,10)\), so no fourth term exists.

**4. Sharpness for infinitely many bases.** For each odd integer \(k\ge3\), \(L_k\ge4\) and (3) with \(r=s=k\) gives \(L_{2k}=L_k^2-2(-1)^k=L_k^2+2\). Hence \(1\to L_k\to L_{2k}\) is a valid three-term walk in base \(b=L_k\). These bases are distinct and unbounded. Combining this construction with Step 3 proves sharpness.

## Verification

The independent-of-proof arithmetic checker `verify.py`, executable with `python3 verify.py`, exhaustively constructs all appending edges between the first \(220\) indexed Lucas numbers for integer bases \(2\) through \(2000\). It checks every represented three-term walk for the absence of a fourth term, verifies the structural classification for three-term walks beginning at value at least \(3\), checks explicit infinite-family identities at \(561\) finite parameter pairs, and independently tests the index-gap obstruction over \(3036\) parameter triples. Its finite tests are consistency checks only; Steps 1–4 prove the unrestricted theorem.

## Relationship to prior work

Miller, Peng, Popescu, and Wattanawanichkul studied right digit-appending walks on the *Fibonacci* numbers in base ten and proved a two-term maximum for that setting [1]. Kominers later established general-base finite bounds for Fibonacci walks, and a qualitative extension to first-kind Lucas sequences \(U_n(P,Q)\) [2]. The classical Lucas numbers in this finding are the *second-kind companion* \(V_n(1,-1)\), whose initial conditions differ from Fibonacci's. In particular, [2, Theorem 4.2] is explicitly stated for \(U_n\), not for this companion \(V_n\); its general logarithmic-type bounds also do not imply a sharp base-independent constant or the displayed exact three-term classification. Earlier number-sequence walk studies [3] concern other arithmetic families. These differences are mathematical scope distinctions, not assertions that every possible prior formulation has been ruled out.

## Limitations

The theorem concerns exactly one appended base-\(b\) digit per transition; appending multiple digits, left extensions, digit edits, and general companion Lucas sequences \(V_n(P,Q)\) are not treated. The numerical verifier does not certify the infinite argument. No exhaustive priority search of all unpublished or unindexed work is possible, and independent mathematical review remains outstanding.

## References

[1] S. J. Miller, F. Peng, T. Popescu, and N. Wattanawanichkul, *Walking to Infinity on the Fibonacci Sequence*, arXiv:2204.08138 (first public 2022-04-18), https://arxiv.org/abs/2204.08138 .

[2] S. D. Kominers, *Uniform Bounds for Digit-Appending Fibonacci Walks*, arXiv:2512.06446v1 (2025-12-06), especially Sections 3–4, https://arxiv.org/abs/2512.06446 .

[3] S. J. Miller et al., *Walking to Infinity Along Some Number Theory Sequences*, arXiv:2010.14932 (2020-10-28), https://arxiv.org/abs/2010.14932 .
