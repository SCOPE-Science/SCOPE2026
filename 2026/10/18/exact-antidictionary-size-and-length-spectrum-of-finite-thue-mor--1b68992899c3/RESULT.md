# Exact antidictionary size and length spectrum of finite Thue–Morse words

## Finding

For every integer \(m\ge3\), the length-\(2^m\) Thue–Morse word \(T_m=\varphi^m(0)\), where \(\varphi(0)=01\) and \(\varphi(1)=10\), has exactly \(4m-5\) **minimal absent contiguous factors** (its binary antidictionary). The complete length spectrum is:

- exactly two minimal absent words of length \(3\);
- exactly four of each length \(3\cdot2^j+2\), for each integer \(0\le j\le m-4\) (an empty range when \(m=3\));
- exactly five of length \(2^{m-2}+2\);
- zero at every other length.

In particular, the finite antidictionary has logarithmic size in the word length and the five longest missing words are a boundary phenomenon absent from the infinite-word antidictionary.

## Assumptions and scope

All words are over \(\{0,1\}\). A *factor* means a contiguous substring, not a scattered subsequence or a cyclic factor. A word \(z\) is minimal absent from \(w\) if it does not occur as a factor of \(w\), but every proper contiguous factor does; for \(|z|\ge2\) it is enough to require its length-\(|z|-1\) prefix and suffix to occur. The infinite fixed point \(t=\lim_{m\to\infty}T_m\) is used only to classify internal forbidden extensions. The theorem is asserted for every integer \(m\ge3\), not for arbitrary prefixes or for other substitutions.

## Proof

**1. Recognizability and factor complexity of the infinite word.** Let \(p(k)\) be the number of distinct length-\(k\) factors of \(t\). There are no occurrences of \(000\) or \(111\). Every even-start length-four factor is one of \(0101,0110,1001,1010\), while the odd-start possibilities are \(1011,1100,1101,0010,0011,0100\). These lists are disjoint. Thus every factor of length at least four has a unique starting parity in \(t\). Desubstitution at even and odd starts gives, for every \(\ell\ge2\),

\[
p(2\ell)=p(\ell)+p(\ell+1),\qquad
p(2\ell+1)=2p(\ell+1).
\]

Indeed an even-start factor of length \(2\ell\) encodes exactly \(\ell\) source letters, an odd-start such factor encodes \(\ell+1\) letters, and both start parities for length \(2\ell+1\) encode \(\ell+1\) letters. The encodings are injective within each parity class by the explicit form of \(\varphi\). The bases \(p(3)=6\) and \(p(4)=10\) then give by induction, for every power of two \(R=2^r\) with \(r\ge1\),

\[
p(R+1)=3R,\qquad p(R+2)=3R+4.
\]

**2. The infinite antidictionary.** Both symbols and all four binary bigrams occur in \(t\), so its minimal absent words have length at least three. The known bispecial-factor classification of \(t\) (Radoszewski–Rytter, Fact 7 and Lemma 3) says that all nonempty bispecial factors are the words \(T_i,\overline{T_i}\) for \(i\ge0\) and \(\varphi^j(010),\varphi^j(101)\) for \(j\ge0\). Any minimal absent word \(avb\) of \(t\) with \(a,b\in\{0,1\}\) must have a bispecial interior \(v\): if \(v\) had a unique left extension, an occurrence of \(vb\) could be preceded only by \(a\), forcing \(avb\); the right-extension argument is symmetric. The fixed point is uniformly recurrent, so terminal occurrences do not create exceptions.

For interiors \(v=0\) and \(v=1\), the sole absent two-sided extensions are \(000\) and \(111\). For interiors \(T_i,\overline{T_i}\) with \(i\ge1\), all four left/right-context pairs occur: inspect \(i=1\), and apply the substitution context map described next (or Radoszewski–Rytter, Observation 5) inductively. For each \(v=010\) and \(v=101\), its actual context pairs are precisely \(\{01,10\}\), where a pair denotes the preceding and following bits. Consequently two other pairs give minimal absent words for each of the two interiors. Since every occurrence of a factor of length at least four has fixed starting parity, occurrences of \(\varphi(v)\) for these interiors correspond precisely to substituted occurrences of \(v\). Under this correspondence a context pair \((a,b)\) becomes \((1-a,b)\): the last bit of \(\varphi(a)\) is \(1-a\), and the first bit of \(\varphi(b)\) is \(b\). Thus each substitution step flips the first context bit, always leaving precisely two absent context pairs for each of \(\varphi^j(010)\) and \(\varphi^j(101)\). Their lengths are \(3\cdot2^j+2\). This exhausts the infinite antidictionary.

**3. A complete factor cutoff for each finite iterate.** Fix \(m\ge3\) and set \(R=2^{m-2}\). Every length-\(R+1\) factor of \(T_m\) occurs exactly once. For the base \(m=3\), the six length-three factors of \(01101001\) are pairwise distinct. In the induction from \(m-1\) to \(m\), suppose two equal factors have length \(R+1=2r+1\), where \(r=2^{m-3}\). The parity-recognizability argument of step 1 makes their initial positions have the same parity. Desubstituting the two occurrences produces equal length-\(r+1\) factors of \(T_{m-1}\), contradicting inductive uniqueness unless the starting positions coincide. Thus the \(2^m-R=3R\) possible length-\(R+1\) windows are all distinct. Since \(T_m\) is a prefix of \(t\) and \(p(R+1)=3R\), every infinite factor of length \(R+1\) occurs in \(T_m\). Hence the same is true of all shorter infinite factors.

Every length-\(R+2\) window of \(T_m\) is also unique because each has a unique prefix of length \(R+1\). There are \(2^m-(R+2)+1=3R-1\) such windows, whereas \(t\) has \(p(R+2)=3R+4\) factors of that length. Exactly five infinite factors of length \(R+2\) are missing from \(T_m\). Their length-\(R+1\) prefixes and suffixes all occur in \(T_m\), so all five are minimal absent words.

**4. Exhaustion and count.** No minimal absent word of length greater than \(R+2\) exists: its length-\(R+1\) interior would be forced to occur twice by the present longest proper prefix and suffix, contradicting the uniqueness of such factors. At every length at most \(R+1\), the factor sets of \(T_m\) and \(t\) agree, hence so do their minimal absent words. The infinite lengths in this range are \(3\) and \(3\cdot2^j+2\) exactly for \(0\le j\le m-4\). The boundary length \(R+2\) coincides with none of these, because \(3\cdot2^j\) is not a power of two. Therefore the total is \(2+4(m-3)+5=4m-5\), with the stated exact spectrum. \(\square\)

## Verification

The accompanying standalone `VERIFY.py` reconstructs \(T_m\), enumerates **all** factors and minimal absent words independently for every \(3\le m\le9\), and checks the complete predicted length spectra and the unique-factor cutoff. It also verifies infinite-context families through six substitution levels in a longer iterate. Running `python3 VERIFY.py` produces `VERIFY_OK`. These finite checks supplement, but do not replace, the all-ranks proof.

## Relationship to prior work

Radoszewski and Rytter (2012; first available online 15 January 2011), *On the Structure of Compacted Subword Graphs of Thue–Morse Words and Their Applications*, prove the relevant bispecial-factor classification and structural properties of the finite and infinite compacted subword graphs. Their results substantially underlie step 2. The inspected paper does not explicitly state the above finite minimal-absent-factor count, its complete length spectrum, or the five longest boundary words. Barton et al. (2014) establish a general linear-time method for computing minimal absent words of an arbitrary finite input; a generic algorithm does not itself supply this closed formula. The potential derivability of the theorem from earlier complete factor-graph descriptions is a remaining originality risk.

## Limitations

The result addresses dyadic substitution iterates only. No assertion of the novelty of the known infinite forbidden-extension description is made. The closed finite count and boundary-length spectrum have not been independently audited; a derivation in unindexed literature or in full graph descriptions not formulated in these terms remains possible. No computational check proves the infinite theorem.

## References

1. J. Radoszewski and W. Rytter, *On the Structure of Compacted Subword Graphs of Thue–Morse Words and Their Applications*, Journal of Discrete Algorithms 11 (2012), 15–24. DOI: 10.1016/j.jda.2011.01.001. Author-hosted full text: https://duch.mimuw.edu.pl/~rytter/TEACHING/TEKSTY/thue.pdf.
2. C. Barton et al., *Linear-time computation of minimal absent words using suffix array*, BMC Bioinformatics 15 (2014), 388. DOI: 10.1186/s12859-014-0388-9; https://link.springer.com/article/10.1186/s12859-014-0388-9.
