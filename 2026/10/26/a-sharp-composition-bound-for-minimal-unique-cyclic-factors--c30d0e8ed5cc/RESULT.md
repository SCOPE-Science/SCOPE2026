# A sharp composition bound for minimal unique cyclic factors

## Finding

Let \(w\) be a directed cyclic word of length \(n\ge 2\) over a finite alphabet \(\Sigma\). A *cyclic factor* of length \(\ell\), for \(1\le\ell\le n\), is read clockwise from one of the \(n\) starting positions, allowing wraparound. Occurrences are counted at starting positions, even when cyclic rotations agree. A factor is *minimal unique* if it occurs at exactly one starting position and every proper contiguous factor occurs at least twice. Let \(n_a\) be the number of occurrences of letter \(a\), and let \(M_a(w)\) count distinct minimal unique cyclic factors beginning with \(a\). Then

\[
M_a(w)\le\min\{n_a,n-n_a\},\qquad
|\mathcal M(w)|\le \sum_{a\in\Sigma}\min\{n_a,n-n_a\}.
\]

In particular, for a binary cyclic word with exactly \(k\) ones,
\[
|\mathcal M(w)|\le 2\min\{k,n-k\}.
\]
This coefficient is sharp at arbitrarily large lengths: each cyclic de Bruijn word of order \(r\ge1\) over a \(q\)-symbol alphabet, \(q\ge2\), has exactly \(q^r\) minimal unique cyclic factors and attains equality in the alphabet-composition bound. All its minimal unique factors have length \(r\).

## Assumptions and scope

The finite alphabet may have letters absent from the given word; these have \(n_a=0\) and contribute zero. Reading orientation is fixed. Distinct minimal unique factors are counted as words rather than as rotations or reversal classes; uniqueness of their occurrence makes this count equal to their number of starts. Cyclic factors have lengths between one and the full circumference, and a factor of length zero is not considered. A length-one factor is minimal unique precisely when its letter appears once. In all other cases, minimality is equivalent to requiring both the immediate proper prefix and the immediate proper suffix to occur at least twice. The bound is valid even for a periodic cyclic word, where multiple starts can produce the same full-length factor.

## Proof

**Non-nesting.** Distinct minimal unique cyclic factors cannot be proper prefix-comparable. If \(u\) were a proper prefix of \(v\), uniqueness of \(u\) would contradict the fact that every proper factor of the minimal unique word \(v\) repeats. Thus at most one minimal unique factor starts at any one position. In particular, \(M_a(w)\le n_a\).

**Injecting into contrasting letters.** Fix a letter \(a\). If \(M_a(w)=0\), there is nothing to prove. Suppose some minimal unique factor beginning in \(a\) is the single letter \(a\). Then \(n_a=1\), and no longer factor beginning with \(a\) can be minimal unique; hence \(M_a(w)=1\le n-n_a\), since \(n\ge2\).

Otherwise, every minimal unique factor beginning with \(a\) has length at least two and may be written \(u=av\) with \(v\) nonempty. Let \(s\) be the unique start of \(u\), indexed modulo \(n\). Its proper suffix \(v\) occurs at \(s+1\) and, by minimality, also at some start \(t\not\equiv s+1\pmod n\). Let \(p=t-1\pmod n\) be the position immediately preceding this second occurrence. The symbol at \(p\) is not \(a\): otherwise \(av=u\) would begin at \(p\ne s\), contradicting uniqueness of \(u\). Assign the contrasting position \(p\) to \(u\).

This assignment is injective even if an arbitrary second occurrence is selected for each suffix. Indeed, if distinct minimal unique factors \(u=av\) and \(u'=av'\) were assigned the same position \(p\), then \(v,v'\) would both begin at the single position \(p+1\), and so one would be a prefix of the other. It would follow that \(av\) and \(av'\) are proper prefix-comparable, contrary to non-nesting. Consequently, the \(M_a(w)\) minimal unique factors can be injected into the \(n-n_a\) positions whose letters are different from \(a\). Thus \(M_a(w)\le n-n_a\), proving the first assertion after combining both bounds. Summing over letters gives the second assertion and the stated binary specialization.

**Sharpness at infinitely many lengths.** Fix \(q\ge2\) and \(r\ge1\), and take a cyclic de Bruijn sequence of order \(r\): every \(q\)-ary length-\(r\) word appears as a cyclic factor exactly once. Its circumference is \(n=q^r\). Each shorter word of length \(\ell<r\) appears \(q^{r-\ell}\ge2\) times, since it extends to that many different length-\(r\) words. Therefore every length-\(r\) cyclic factor is minimal unique. No longer factor is minimal unique, because its initial length-\(r\) factor would already be unique; no shorter factor is unique. There are exactly \(q^r=n\) minimal unique factors. Each letter occurs \(q^{r-1}\) times, and \(n_a\le n-n_a\) because \(q\ge2\); hence the sum of the alphabet-composition bounds equals \(n\). In the binary case, \(k=2^{r-1}\), so equality reads \(|\mathcal M(w)|=2k=n\). This proves sharpness for unbounded lengths.

## Verification

The standalone program `cyclic_mus_verify.py` independently computes all cyclic factor occurrence multiplicities by direct enumeration. It exhaustively tests the per-letter and total bounds for binary words of lengths \(2\) through \(15\), ternary words of lengths \(2\) through \(8\), and four-letter words of lengths \(2\) through \(6\): altogether \(80{,}825\) cyclic word instances. It constructs and checks de Bruijn cycles in binary orders \(1\) through \(6\) and ternary orders \(1\) through \(4\). Run with `python3 cyclic_mus_verify.py`. The mathematical proof, not these finite tests, establishes the all-length claims.

## Relationship to prior work

Ilie and Smyth introduced minimal unique substrings (also called minimum unique substrings) and related them to maximal repeats, and Pei, Wu, and Yeh discussed the non-nesting property in the linear-string setting. The present result takes cyclic occurrence multiplicity as its object and bounds minimal unique factors separately by the number of matching and nonmatching alphabet positions. The conclusion is a composition-sensitive count; it is not a rephrasing of the general bound of at most one minimal unique substring per starting position. The standard de Bruijn property supplies the sharpness witnesses. Related work on string attractors, absent factors and short-read spectra concerns different invariants.

## Limitations

There is no claim that every composition can attain equality or that the bound classifies all equality cases. The output is a cardinality theorem for complete cyclic words, not a linear-window counting formula. The bibliography establishes relevant definitions and methods; it does not constitute an exhaustive priority certification. The complete text of the 2011 paper was not available through the accessible sources, leaving possible historical overlap as an explicit limitation. Finite checks cannot substitute for the written injection proof.

## References

1. L. Ilie and W. F. Smyth, "Minimum Unique Substrings and Maximum Repeats," *Fundamenta Informaticae* **110** (2011), 183–195, DOI: 10.3233/FI-2011-536; publisher records first public online date as 2011-01-01.
2. J. Pei, W. Wu, and M.-Y. Yeh, "On Shortest Unique Substring Queries," IEEE ICDE (2013), author-hosted PDF at https://www.cs.sfu.ca/~jpei/publications/Shortest%20Unique%20Substring%20Queries%20ICDE13.pdf.
3. Crochemore and Rytter, *Jewels of Stringology*, reference on minimal unique factors and de Bruijn examples; see https://125-problems.univ-eiffel.fr/problem59.php.
