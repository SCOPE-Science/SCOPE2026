# Lie complexity of periodic binary words with two unequal marker gaps

## Finding

For every pair of integers \(1\le b<d\), set
\[
U_{b,d}=(0\,1^b\,0\,1^d)^\omega,\qquad p=b+d+2,\qquad m=\min\{d,2b+1\}.
\]
Here \(U_{b,d}\) is a one-sided infinite binary word, \(p\) is the length of its primitive period, and a *Lie class of length* \(n\ge1\) is a cyclic-conjugacy class of length-\(n\) factors of \(U_{b,d}\) for which **all** cyclic rotations occur as contiguous factors. Write \(L_{b,d}(n)\) for the number of these classes.

**Complete classification.** All Lie classes, represented by their lexicographically least words, are exactly the following whenever the displayed condition holds:

1. \(0\), only for \(n=1\);
2. \(1^n\), for \(1\le n\le d\);
3. \(01^{n-1}\), for \(2\le n\le m+1\);
4. \((01^b)^2\), only for \(n=2b+2\);
5. \((01^b01^d)^{n/p}\), for positive multiples \(n\) of \(p\).

Each listed class is distinct whenever present. Equivalently, for **every** integer \(n\ge1\),
\[
\boxed{L_{b,d}(n)=\mathbf 1_{\{n=1\}}+\mathbf1_{\{1\le n\le d\}}+\mathbf1_{\{2\le n\le m+1\}}+\mathbf1_{\{n=2b+2\}}+\mathbf1_{\{p\mid n\}}.}
\]
Consequently the ordinary generating function is
\[
\boxed{\sum_{n\ge1}L_{b,d}(n)z^n=z+\frac{z(1-z^d)}{1-z}+\frac{z^2(1-z^m)}{1-z}+z^{2b+2}+\frac{z^p}{1-z^p}.}
\]

**Transition and sharp first-period mass.** Define the *first-period Lie mass* by \(S(b,d)=\sum_{n=1}^{p}L_{b,d}(n)\), which counts all exceptional short-length classes together with the first appearance of the eventual periodic class. Then
\[
S(b,d)=d+3+\min\{d,2b+1\}.
\]
The maximal value of \(L_{b,d}(n)\) over \(n\ge1\) is \(3\) if and only if \(d\ge2b+2\), and otherwise it is \(2\). In the three-class regime the unique length with three classes is \(n=2b+2\).

For each fixed primitive period length \(p\ge5\), among all positive unequal gaps \(1\le b<d\) with \(b+d+2=p\),
\[
\boxed{\max S(b,d)=\left\lfloor\frac{4p}{3}\right\rfloor+1.}
\]
The maximizing shorter gap is uniquely \(b=1\) when \(p=5\). When \(p\ge6\), put \(q=\lfloor(p-3)/3\rfloor\); the maximizing choices are \(b=q\), and **also** \(b=q+1\) when \(p\equiv2\pmod3\) (in which case \(p\ge8\)). The larger gap is uniquely determined by \(d=p-b-2\).

## Assumptions and scope

Only \(1\le b<d\) and \(n\ge1\) are assumed; no asymptotic limit or probabilistic model is involved. Each class is counted once, independently of the number of occurrences and of its number of distinct rotations. The empty factor is excluded. The notation \(\mathbf1_{\{P\}}\) is \(1\) when statement \(P\) holds and \(0\) otherwise. The word order is \(0<1\). Equality \(b=d\) is excluded because then the four-run display is not a primitive period: the word has period \(b+1\), so the stated formula need not apply.

## Proof

**1. Primitive period and phase uniqueness.** The finite period block \(v=01^b01^d\) contains exactly two zeros. If it were a proper power, the number of repeated copies would be two, and each would contain one zero; its two cyclic zero-to-zero gaps would therefore be equal. This contradicts \(b<d\). Hence its least period is \(p\). Its \(p\) cyclic rotations are pairwise distinct. The length-\(p\) factor beginning at a particular phase therefore identifies that phase uniquely.

**2. Lengths at least \(p\).** If \(n=p\), all \(p\) length-\(p\) factors are the cyclic rotations of \(v\), giving exactly one Lie class. For \(n>p\), let \(x\) be a length-\(n\) factor with all its cyclic rotations present. Write \(x_j\) for the rotation by \(j\) positions. Each \(x_j\) is a factor at some phase \(t_j\in\{0,\ldots,p-1\}\). The first \(p\) symbols of \(x_{j+1}\) are the symbols numbered \(1,\ldots,p\) of \(x_j\), since \(n>p\). They are the length-\(p\) periodic factor at phase \(t_j+1\). Uniqueness of phases forces \(t_{j+1}\equiv t_j+1\pmod p\). As \(x_n=x_0\), uniqueness again yields \(p\mid n\). Conversely if \(p\mid n\), every factor of length \(n\) is a power of one of the rotations of \(v\), and its whole conjugacy class is present. There is exactly one such class. This proves the final indicator for all \(n\ge p\), including \(n=p\).

**3. Lengths below \(p\): zero and one zero.** Any length-\(n<p\) factor contains at most two zeros. There is no adjacent pair \(00\). The all-zero class occurs only for \(n=1\), while \(1^n\) occurs precisely for \(n\le d\). For a factor with exactly one zero, the class representative must be \(01^j\) for \(j=n-1\ge1\). Such a factor can occur only when \(j\le d\). Every conjugate can be written \(1^k01^{j-k}\), \(0\le k\le j\). Around the two zeros in \(U_{b,d}\), the numbers of available ones to the left and right are respectively \((d,b)\) and \((b,d)\). Under \(j\le d\), a conjugate occurs precisely if \(k\le b\) or \(k\ge j-b\). These two integer intervals cover all \(k\in[0,j]\) exactly when \(j\le2b+1\). Thus the one-zero class exists precisely for \(1\le j\le\min(d,2b+1)=m\).

**4. Lengths below \(p\): two zeros.** If a two-zero factor has all cyclic conjugates, both gaps of ones between its zeros on the *circle* must be positive; otherwise a conjugate would contain forbidden \(00\). Its class therefore has a representative \(01^s01^t\) with \(s,t\ge1\). The rotations beginning at either zero contain a complete adjacent zero-to-zero gap, so both \(s\) and \(t\) must be members of \(\{b,d\}\), the only actual complete gaps. The possibilities \((b,d)\) and \((d,b)\) have length exactly \(p\), and \((d,d)\) has length greater than \(p\). Thus for \(n<p\) only \((s,t)=(b,b)\) remains, at \(n=2b+2\). Conversely every conjugate of \((01^b)^2\) occurs across the short \(b\)-gap, with its remaining \(b\) ones furnished by portions of the adjacent long \(d\)-gaps. This is possible because \(d>b\). There are no other short Lie classes. Together with Steps 2–3 this proves the complete list.

**5. Counts, generating series, and transition.** The five mutually distinct families in the classification contribute their five indicator functions. Their sums over \(n\ge1\) are the five geometric terms displayed above. The terms whose lengths are at most \(p\) contribute respectively \(1,d,m,1,1\), so \(S=d+m+3\). For \(n>1\) and \(n<p\), only the pure-ones, one-zero, and exceptional two-zero classes can coexist; they do so exactly at \(n=2b+2\) when \(2b+2\le d\). Otherwise at most two coexist, while \(L(1)=2\). This proves the transition and the uniqueness of the three-class length.

**6. Sharp fixed-period optimization.** Fix \(p\ge5\), and substitute \(d=p-2-b\). The admissible integers satisfy \(1\le b<(p-2)/2\). On the side \(b\le(p-3)/3\) we have
\[
S=p+b+2,
\]
which strictly increases with \(b\). On the side \(b\ge(p-3)/3\) we have
\[
S=2p-2b-1,
\]
which strictly decreases with \(b\). Comparing the two admissible integers nearest the breakpoint, and treating the smallest admissible period \(p=5\) directly, yields \(\lfloor4p/3\rfloor+1\). Equality is attained precisely by the values of \(b\) stated in the finding (the two sides tie exactly when \(p\equiv2\pmod3\), except that \(p=5\) has only one admissible pair). This proves every assertion.

## Verification

The accompanying standalone \(\texttt{verify_lie.py}\) independently generates all cyclic length-\(n\) factors of the primitive period, groups them by lexicographically least cyclic rotation, and retains a class only when every rotation occurs. It compares the **complete actual class sets** with the five explicit families for \(1\le b<d\), \(b\le19\), \(d\le27\), across lengths through \(3p+4\): \(28{,}766\) complete comparisons. It additionally checks every fixed-period maximizer and maximum for \(5\le p\le99\), plus first-period mass and the three-class threshold for \(b\le39\), \(d\le49\). Its successful output is \(\texttt{VERIFY\_OK complete\_necklace\_sets=28766 sharp\_length\_extrema=5..99 exact\_mass=true peak\_transition=true}\). These finite checks corroborate, but do not replace, the universal proof above.

## Relationship to prior work

Bell and Shallit introduced Lie complexity, proved general bounds and studied automatic/morphic examples [1]. Their fully consulted publicly available preprint (including the definition, the general bounds and Examples 7.1–7.6) does not state the exact two-gap periodic spectrum or the first-period extremum above. De Luca and Fici established an exact formula for *aperiodic Sturmian words* [2]; our family consists of **periodic** words, mostly outside the balanced/Sturmian setting, and the stated formula in [2] does not entail the present family-wise spectrum. Cassaigne, Fici, Sciortino and Zamboni studied **cyclic complexity**, which counts a conjugacy class when *at least one* representative occurs [3], rather than requiring *every* rotation; their results do not imply this Lie classification. The present statement is a direct exact classification for a primitive period with two unequal return gaps, not an assertion about all periodic binary words.

## Limitations

The result does not cover equal gaps, periods with more than two zero markers, general eventually periodic sequences, or exact Lie complexity for arbitrary morphic words. It includes no claim of independent external verification. The novelty comparison cannot exclude a mathematically equivalent specialization in literature not found or indexed, and it should be interpreted as best-knowledge originality rather than a proof of uniqueness.

## References

[1] Jason P. Bell and Jeffrey Shallit, *Lie complexity of words*, arXiv:2102.03821, publicly submitted February 7, 2021. https://arxiv.org/abs/2102.03821

[2] Alessandro De Luca and Gabriele Fici, *On the Lie complexity of Sturmian words*, arXiv:2206.00995, publicly submitted June 2, 2022. https://arxiv.org/abs/2206.00995

[3] Julien Cassaigne, Gabriele Fici, Marinella Sciortino and Luca Q. Zamboni, *Cyclic Complexity of Words*, arXiv:1402.5843, publicly submitted February 24, 2014. https://arxiv.org/abs/1402.5843
