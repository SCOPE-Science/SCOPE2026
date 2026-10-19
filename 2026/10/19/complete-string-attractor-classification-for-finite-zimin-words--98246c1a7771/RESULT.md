# Complete string-attractor classification for finite Zimin words

## Finding

For each integer \(n\ge1\), define the Zimin word recursively by
\[
Z_1=1,\qquad Z_{n+1}=Z_n(n+1)Z_n.
\]
Thus \(Z_2=121\), \(Z_3=1213121\), and \(|Z_n|=2^n-1\).

A **string attractor** for a finite word \(w\) is a set \(\Gamma\) of positions such that every nonempty contiguous factor of \(w\) has *some* occurrence whose interval intersects \(\Gamma\). Let \(E_{n,j}\) be the set of positions occupied by the symbol \(j\) in \(Z_n\). Then, for every \(n\ge1\) and every position subset \(\Gamma\),
\[
\boxed{\Gamma\text{ is a string attractor of }Z_n
\quad\Longleftrightarrow\quad
\Gamma\cap E_{n,j}\ne\varnothing\quad(1\le j\le n).}
\]
In other words, *the complete family of attractors is determined by symbol coverage alone*. The factor-occurrence constraints do not impose any additional restrictions.

The number \(A_n(s)\) of attractors of each size is specified by the exact generating polynomial
\[
\boxed{\sum_{s=0}^{2^n-1} A_n(s)t^s
=\prod_{j=1}^{n}\big((1+t)^{2^{n-j}}-1\big).}
\]
Consequently, the minimum attractor size is \(\gamma(Z_n)=n\). Every inclusion-minimal attractor is minimum-size, consisting of one arbitrarily chosen position of each symbol. The number of these attractors is
\[
\boxed{A_n(n)=\prod_{j=1}^{n}2^{n-j}=2^{n(n-1)/2}.}
\]
The total number of attractors, without a size restriction, is
\[
\boxed{\sum_s A_n(s)=\prod_{j=1}^{n}(2^{2^{n-j}}-1).}
\]
For orders \(n=1,2,3,4,5,6\), the minimum-attractor multiplicities are respectively \(1,2,8,64,1024,32768\). These integers are familiar in other contexts; their interpretation as optimal Zimin-word attractors is the mathematical assertion here.

## Assumptions and scope

All positions use **one-based indexing**. The alphabet of \(Z_n\) is precisely \(\{1,\ldots,n\}\) with literal distinct symbols, not variables subsequently substituted by nonempty words. Factors are ordinary nonempty **contiguous** substrings, not scattered subsequences, and occurrences are wholly within the finite linear word \(Z_n\). A factor is covered when at least one of its occurrences intersects a chosen position. The empty position set is allowed as a candidate but is not an attractor for a nonempty word. The theorem holds for every \(n\ge1\), including the one-letter base case.

## Proof

**1. Ruler representation and symbol classes.** For \(i\ge1\), write \(\nu_2(i)\) for the exponent of two dividing \(i\). Recursion on \(n\) gives the exact formula
\[
Z_n[i]=1+\nu_2(i),\qquad 1\le i\le2^n-1.
\]
Indeed, on the left half this is the formula for \(Z_{n-1}\). At the central index \(i=2^{n-1}\), its value is \(n\). On the right half, writing \(i=2^{n-1}+q\) for \(1\le q<2^{n-1}\), the valuation satisfies \(\nu_2(i)=\nu_2(q)\). Hence
\[
E_{n,j}=\{(2h+1)2^{j-1}:0\le h<2^{n-j}\},
\qquad |E_{n,j}|=2^{n-j}.
\]

**2. Every factor has a unique largest symbol.** Let \(f=Z_n[a..b]\) be any nonempty occurrence, and let \(j\) be its largest letter. Suppose that two positions \(p<q\) of this interval had letter \(j\). Such positions are congruent to \(2^{j-1}\) modulo \(2^j\). Therefore \(q-p\ge2^j\), and the position \(p+2^{j-1}\), strictly between them, is a multiple of \(2^j\), hence carries a letter at least \(j+1\). This contradicts the definition of \(j\). Thus \(f\) contains exactly one occurrence of its largest letter; denote its position by \(p\).

**3. Uniform centered neighborhoods.** Fix any \(j\in\{1,\ldots,n\}\) and an arbitrary occurrence position \(q\in E_{n,j}\). Put \(R_j=2^{j-1}-1\). The interval \([q-R_j,q+R_j]\) lies within \([1,2^n-1]\), since \(2^{j-1}\le q\le2^n-2^{j-1}\). For each integer \(d\) with \(0<|d|<2^{j-1}\), the strict valuation inequality \(\nu_2(d)<j-1=\nu_2(q)\) yields
\[
\nu_2(q+d)=\nu_2(d).
\]
The central symbol equals \(j\) and every symbol at a nonzero offset \(d\) equals \(1+\nu_2(|d|)\), independent of the chosen center \(q\). In particular, all length-\(2^j-1\) neighborhoods centered at occurrences of \(j\) are identical and equal to \(Z_j\).

**4. Recenter any factor on any occurrence of its largest letter.** Return to the factor \(Z_n[a..b]\) of maximum letter \(j\) and its unique \(j\)-position \(p\). We claim
\[
0\le p-a<2^{j-1},\qquad 0\le b-p<2^{j-1}.
\]
If \(a\le p-2^{j-1}\), then the position \(p-2^{j-1}\) is within the factor and within the finite word, is a multiple of \(2^j\), and thus has a symbol exceeding \(j\). The same reasoning holds to the right, using \(p+2^{j-1}\). This contradiction establishes the strict inequalities. Consequently \(f\) lies entirely in the common centered neighborhood from Step 3. For every \(q\in E_{n,j}\), the interval
\[
[q-(p-a),\ q+(b-p)]
\]
is inside \(Z_n\), has the same letter sequence \(f\), and contains \(q\). This is the key factor-recentering lemma.

**5. Attractor equivalence.** Necessity: if \(\Gamma\) is an attractor, then the length-one factor consisting of \(j\) must be covered, which requires \(\Gamma\cap E_{n,j}\ne\varnothing\). This holds for every \(j\).

Sufficiency: suppose that \(\Gamma\) meets each symbol class. Choose any factor \(f\) and put \(j=\max(f)\). Choose \(q\in\Gamma\cap E_{n,j}\). By Step 4, \(f\) has an occurrence crossing \(q\); hence it is covered. This works for every nonempty factor, proving \(\Gamma\) is an attractor.

**6. Enumeration and minimality.** The position classes \(E_{n,j}\) partition the \(2^n-1\) positions and have sizes \(2^{n-j}\). For each symbol, a valid attractor chooses an arbitrary nonempty subset of its positions. Its size generating polynomial is therefore \((1+t)^{2^{n-j}}-1\), and choices for distinct symbols are independent. Multiplication gives the stated generating polynomial. The smallest exponent is \(n\), with coefficient \(\prod_j2^{n-j}=2^{n(n-1)/2}\). An attractor containing more than one occurrence of a letter is not inclusion-minimal: deleting one such occurrence preserves the condition in Step 5. Conversely, deleting any position from a set containing exactly one occurrence per letter destroys the corresponding length-one coverage. The inclusion-minimal and minimum-cardinality families therefore agree. Evaluating the polynomial at \(t=1\) gives the total number of attractors. All assertions follow. \(\square\)

## Verification

The accompanying standalone `verify.py` constructs \(Z_n\) in two independent ways (recursive concatenation and binary valuations); verifies every centered occurrence neighborhood through order eight; and independently builds coverage masks from all contiguous factor occurrences. It exhaustively compares the attractor property against coverage of every symbol for **all** \(32,906\) subsets over orders one through four. It also verifies all \(33,867\) minimum-size candidate sets over orders one through six, plus eighty pseudorandom higher-order minimum candidates. Its successful output is documented in `VERIFICATION.md`. These finite computations corroborate the proof but do not replace its universally quantified argument.

## Relationship to prior work

Głowinski and Rytter [1] study the recursive Zimin words and compressed **ranked pattern matching** within them. The factor-maximum and ruler structure used in this proof is elementary in that older setting; the present result does not claim to invent it. Prezza [2] introduced string attractors as factor-occurrence hitting sets and proved their connection to compressed-string representations. The generic attractor definition and alphabet-size lower bound are established background, not new findings. More recent work by Banbara and collaborators [3] completely characterizes minimum string attractors of **Fibonacci, period-doubling, and Thue–Morse** words. Its inspected theorems concern different word families and do not yield this complete Zimin attractor polynomial. Béaur, Gheeraert, and Hellouin de Menibus [4] focus on bi-infinite attractors, whereas the present statement is for finite recursively built Zimin words.

The contribution claimed here is specifically the equivalence between attractorhood and coverage of every letter for every finite Zimin word, together with the resulting classification of **all** valid attractors and their cardinality generating polynomial. The numeric coefficients of the optimal-attractor sequence occur elsewhere under unrelated combinatorial interpretations.

## Limitations

This theorem is for literal Zimin words with a growing alphabet and **finite linear** factor occurrences. It does not assert the same characterization for words obtained by substituting strings for Zimin variables, for binary encodings of the growing alphabet, for arbitrary Zimin-word prefixes, or for cyclic factors. The multiplicity counts distinct position subsets, not equivalence classes under symmetry. The result does not directly quantify the storage cost of a compressed index on a fixed alphabet. Exhaustive checks were finite; the all-order conclusion comes from the symbolic proof. The mathematical argument is offered for independent examination and has not undergone an independent scientific audit.

## References

1. Radosław Głowinski and Wojciech Rytter, *Compressed Pattern-Matching with Ranked Variables in Zimin Words*, arXiv:1307.1560, first submitted July 5, 2013. https://arxiv.org/abs/1307.1560
2. Nicola Prezza, *String Attractors*, arXiv:1709.05314, first submitted September 15, 2017. https://arxiv.org/html/1709.05314v2
3. Mutsunori Banbara, Hideo Bannai, Peaker Guo, Dominik Köppl, Takuya Mieno, and Yoshio Okamoto, *The Smallest String Attractors of Fibonacci, Period-Doubling, and Thue–Morse Words*, arXiv:2602.16152, initially submitted February 2026, revised October 12, 2026. https://arxiv.org/html/2602.16152
4. Pierre Béaur, France Gheeraert, and Benjamin Hellouin de Menibus, *String attractors and bi-infinite words*, arXiv:2403.13449, first submitted March 20, 2024. https://arxiv.org/html/2403.13449v1
