# Complete palindromic-factor distribution for binary circles with three markers

## Finding

Let a **binary necklace** be a nonempty binary circular word, identified under rotation but not reversal or letter complementation. If the necklace \(w\) has length \(n\), a **circular factor** is the length-\(j\) word seen at one of its \(n\) starting positions, following the specified cyclic direction, for \(1\le j\le n\). Let \(P(w)\) count **distinct nonempty palindromic circular factors**, not occurrences.

Every binary necklace with exactly three ones has a presentation
\[
w=1\,0^a1\,0^b1\,0^c,\qquad a,b,c\in\mathbb Z_{\ge0}.
\]
Let \(r\le s\le t\) be the sorted zero gaps \(a,b,c\), and let \(m=r+s+t=n-3\). Then the number of distinct palindromes is exactly
\[
P(w)=\begin{cases}
3r+\lfloor r/2\rfloor+3,&r=s=t,\\
t+3r+\lfloor t/2\rfloor+4,&r=s<t,\\
r+3t+\lfloor r/2\rfloor+4,&r<s=t,\\
t+2s+2r+4,&r<s<t.
\end{cases}
\tag{1}
\]

Let \(A_{m,p}\) be the number of binary necklaces with exactly three ones, exactly \(m\) zeros, and exactly \(p\) distinct nonempty palindromic circular factors. The following **rational bivariate generating function gives every coefficient**, for all \(m\ge0\) and \(p\ge0\):
\[
\begin{aligned}
F(x,y)&=\sum_{m,p\ge0}A_{m,p}x^m y^p\\
&=\frac{y^3+x^3y^6}{1-x^6y^7}
+\frac{xy^5+2x^2y^7+x^4y^{10}+2x^5y^{11}}{(1-x^6y^9)(1-x^2y^3)}\\
&\qquad+\frac{2x^3y^8}{(1-x^3y^5)(1-x^2y^3)(1-xy)}.
\end{aligned}
\tag{2}
\]
All generating-function identities are formal power-series identities with integer coefficients. The variable \(x\) counts zeros; the variable \(y\) counts distinct palindromic factors.

There is also a limiting law. Choose uniformly from the rotation classes with exactly three ones and \(m\) zeros, and write \(X_m=P(w)/m\) for \(m\ge1\). Then \(X_m\) converges in distribution to \(X\), with
\[
\Pr\{X\le u\}=\begin{cases}
0,&u<1,\\
3(u-1)^2,&1\le u\le3/2,\\
3(u-1)^2-3(2u-3)^2,&3/2\le u\le5/3,\\
1,&u\ge5/3.
\end{cases}
\tag{3}
\]
In particular, \(\lim_{m\to\infty}\mathbb E[X_m]=25/18\).

## Assumptions and scope

The alphabet is precisely \(\{0,1\}\), and the number of ones is exactly three. An occurrence crossing the chosen representation boundary is included if its length is at most the circumference \(n\). Palindromes are counted as distinct *strings*, even if they occur at several starting positions. A necklace and its reversal are not identified, although their palindrome inventories agree. Periodic necklaces, including \(111\), are included. No assertion is made for a different number of ones, for unrestricted factor lengths in the bi-infinite periodic extension, or for palindromic subsequences.

## Proof

**Step 1: classify every palindrome.** Write the directed cyclic zero gaps as \((a,b,c)\). There are only four possibilities for the number of ones in a circular factor because the circle contains three ones. Palindromes containing zero ones are \(0^j\) with \(1\le j\le t\), giving \(t\) strings. Those containing one one are exactly \(0^i1\,0^i\); the maximum feasible \(i\) among the three possible centers is the middle gap \(s\), so there are \(s+1\) strings.

A palindrome containing exactly two ones must contain two consecutive ones and has the form \(0^i1\,0^g1\,0^i\), where \(g\) is their intervening cyclic gap and \(0\le i\le\min\{g',g''\}\), with \(g',g''\) the two other cyclic gaps. Two choices give the same string exactly when both \(g\) and \(i\) agree. Hence the number of two-one palindromes is
\[
T_2=\sum_{g\in\{a,b,c\}_{\mathrm{distinct}}}
\bigl(1+\min\{\text{the other two gap lengths}\}\bigr),
\]
where for repeated gap values any occurrence may be used: the associated pair of remaining gaps has the same minimum. Evaluating this sum gives, respectively for the four cases in (1),
\[
T_2=r+1,\quad 2r+2,\quad r+t+2,\quad 2r+s+3.
\]

A palindrome containing all three ones has its central one flanked by two *equal* cyclic zero gaps \(g\); it is \(0^i1\,0^g1\,0^g1\,0^i\). The remaining gap \(h\) supplies both outer arms, so \(0\le i\le\lfloor h/2\rfloor\). If all three gaps are equal the same strings occur from each center and are counted once. Thus the count is \(\lfloor r/2\rfloor+1\) if all gaps are equal, \(\lfloor t/2\rfloor+1\) if the two smaller gaps agree, \(\lfloor r/2\rfloor+1\) if the two larger gaps agree, and zero if all are different. The four disjoint groups contain different numbers of ones, so adding them proves (1). Each displayed factor has length at most \(n\); conversely every length-at-most-\(n\) palindrome fits one of the four groups. This establishes necessity and sufficiency, including zero-gap boundaries.

**Step 2: count rotation classes.** For three gaps the ordered triple is defined only up to cyclic rotation. A sorted triple with three distinct entries gives exactly two directed necklaces (the two possible cyclic orders); a sorted triple with a repeated entry gives exactly one. This remains true for the periodic all-equal case.

For \(r<s<t\) write \(r=i\), \(s=i+j+1\), \(t=i+j+k+2\), where \(i,j,k\ge0\). Then \(m=3i+2j+k+3\), \(P=5i+3j+k+8\), and the rotation-class multiplicity is two. Its generating function is the last summand of (2).

For \(r=s<t\), write \(r=i\), \(t=i+d+1\). Here \(m=3i+d+1\) and \(P=4i+d+5+\lfloor(i+d+1)/2\rfloor\). Splitting \(i=2u+v\) and \(d=2h+z\) with \(v,z\in\{0,1\}\) produces
\[
\frac{xy^5+x^2y^7+x^4y^{10}+x^5y^{11}}{(1-x^6y^9)(1-x^2y^3)}.
\]
For \(r<s=t\), write \(r=i\), \(s=t=i+d+1\). Then \(m=3i+2d+2\) and \(P=4i+3d+7+\lfloor i/2\rfloor\), giving
\[
\frac{x^2y^7+x^5y^{11}}{(1-x^6y^9)(1-x^2y^3)}.
\]
Finally, the all-equal gaps \(r=s=t=i\) give \(m=3i\), \(P=3i+\lfloor i/2\rfloor+3\), hence the first summand of (2). Adding these mutually exclusive cases proves (2).

**Step 3: limiting law.** Among gap triples with fixed sum \(m\), the triples having a repeated entry form only \(O(m)\) choices; the total number of necklaces is \(\Theta(m^2)\). For the remaining triples (1) says \(P=2m-t+4\). Normalizing the ordered gaps by \(m\) gives the uniform distribution on the simplex \(\{(v_1,v_2,v_3):v_i\ge0,\sum v_i=1\}\) in the limit: this is the elementary Riemann-sum limit for nonnegative integer triples. The difference between uniformly sampled ordered triples and uniformly sampled necklaces vanishes because at most an \(O(1/m)\) fraction have repeated gaps. Consequently \(X_m\) converges to \(2-M\), with \(M=\max(V_1,V_2,V_3)\) for a uniformly sampled simplex point.

Inclusion-exclusion on \(V_i>v\) yields
\[
\Pr\{M>v\}=3(1-v)_+^2-3(1-2v)_+^2+(1-3v)_+^2,
\]
where \(z_+=\max\{z,0\}\). Substituting \(v=2-u\) proves (3). Also
\[
\mathbb E[M]=\sum_{j=1}^{3}(-1)^{j+1}\binom3j\frac1{3j}=\frac{11}{18},
\]
so \(\mathbb E[X]=2-11/18=25/18\). Uniform boundedness of \(X_m\) follows directly from (1), and therefore the expectations converge as stated.

## Verification

Run `python3 checker.py` with Python 3 and no external dependencies. The independent direct enumerator constructs all cyclic factors and tests palindrome equality as strings. It compares entire palindrome sets with the structural inventory for 8,000 labeled zero-gap triples, then compares the bivariate generating-function coefficients with direct sorted-gap counting through \(m=50\). Finally, independent explicit rotational equivalence classes through length \(17\) reproduce the corresponding coefficient rows. Successful replay prints three `PASS` lines. These are finite tests; the proof above establishes the infinite statements.

## Relationship to prior work

Simpson (2014) established the general bound \(P(w)<5n/3\) for circular words and gave nearly sharp examples, including the constructions cited in the OEIS record. Those general bounds and specific near-extremal examples are **not claimed as new**. OEIS A247000 records maximum counts across all binary circles, with dated examples. The distinguishing statement here is a complete *individual three-marker inventory* and the **joint all-length distribution by number of zeros and distinct palindromes**, given by (2), together with its limiting law. A general maximum-value sequence does not determine coefficients indexed simultaneously by fixed composition and palindrome count.

The full text of Simpson (2014), especially the relevant near-extremal constructions, could not be independently inspected. The publicly accessible abstract and the OEIS page do not state (1) or (2), but their silence does not rule out equivalent results elsewhere in the full article. Any earlier covering theorem would supersede the claimed originality.

## Limitations

This is a fixed-composition, fixed-alphabet result. It does not improve Simpson's general upper bound, assert a new maximum for all binary circles, or identify first discovery of the near-extremal three-one examples. The limiting law concerns uniformly chosen **necklaces**, not uniformly chosen binary strings of the same length. The priority comparison is limited by inaccessible full text of the 2014 primary paper and by possible alternate terminology; scientific verification of (1)–(3) does not resolve historical priority. No independent mathematical audit has been performed.

## References

1. Jamie Simpson, *Palindromes in circular words*, Theoretical Computer Science **550** (2014), 66–78, DOI: 10.1016/j.tcs.2014.07.012. Public abstract: https://researchportal.murdoch.edu.au/esploro/outputs/journalArticle/Palindromes-in-circular-words/991005543823107891
2. N. J. A. Sloane et al., OEIS A247000, *Maximal number of palindromes in a circular binary word of length n*, initial record dated September 15, 2014: https://oeis.org/A247000
