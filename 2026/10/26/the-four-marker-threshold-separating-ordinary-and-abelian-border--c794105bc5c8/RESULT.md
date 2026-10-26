# The four-marker threshold separating ordinary and Abelian borders

## Finding

A finite binary word has an **ordinary border** if a nonempty proper prefix is identical to a suffix of the same length; it has an **Abelian border** if a nonempty proper prefix and equally long suffix have equal numbers of each symbol. Denote by \(\lvert w\rvert_1\) the number of ones.

**Sharp sparse rigidity.** Every binary word \(w\) with \(\min(\lvert w\rvert_0,\lvert w\rvert_1)\leq 3\) is ordinarily bordered if and only if it is Abelian bordered. Four occurrences of each symbol are necessary and sufficient for a binary word to be ordinarily unbordered but Abelian bordered; the shortest such words have length eight.

**Complete first-exceptional-layer classification.** Let \(\lvert w\rvert_1=4\). A word that is ordinarily unbordered but Abelian bordered must begin and end with different bits. If it begins with zero and ends with one, write it uniquely as
\[
w=0^a1\,0^b1\,0^c1\,0^d1,
\qquad a\geq1,\quad b,c,d\geq0.
\]
Then it has this property **if and only if**
\[
a>d,\qquad a+b\leq c+d,\qquad b\neq d. \tag{1}
\]
All remaining exceptional words with four ones are reversals of these words; the two families are disjoint. Equivalently, the first family admits a unique parametrization
\[
a=d+e,\qquad c=b+e+f,\qquad e\geq1,\ f\geq0,\ b,d\geq0,\ b\neq d. \tag{2}
\]
If \(B_n\) counts all binary words of length \(n\) containing exactly four ones that are ordinarily unbordered but Abelian bordered, then
\[
\boxed{\sum_{n\geq0}B_nz^n=\frac{4z^8}{(1-z)(1-z^2)^2(1-z^4)}.} \tag{3}
\]
In particular, \(B_n=0\) for \(n<8\), and \((B_8,B_9,\ldots,B_{22})=(4,4,12,12,28,28,52,52,88,88,136,136,200,200,280)\). Moreover,
\[
B_n=\frac{n^3}{24}+O(n^2),\qquad \frac{B_n}{\binom n4}=\frac1n+O(n^{-2})
\]
as \(n\to\infty\).

## Assumptions and scope

Words are finite strings over the labeled binary alphabet \(\{0,1\}\), with ordinary (not cyclic) prefixes and suffixes. Both notions exclude the empty and entire-word borders. Reversal and bit complementation preserve both border properties, but only reversal preserves the fixed weight-four composition for arbitrary length. Equations (1)–(3) are for exactly four ones; the rigidity statement allows either symbol to be sparse. The generating variable counts total length, not the number of zeros.

## Proof

**Short-border reduction.** Any ordinarily bordered word has a border of length at most half its length: if a border has length \(h>n/2\), the period \(p=n-h\) yields a shorter nonempty border of length \(h-p=2h-n\); iterate. An Abelian border of length \(h>n/2\) likewise implies one of length \(n-h\): equality of the Parikh vectors of length-\(h\) prefix and suffix is equivalent, after subtracting both from the entire-word Parikh vector, to equality for the complementary length-\(n-h\) prefix and suffix. Hence both can be tested using disjoint prefix/suffix blocks of length at most \(\lfloor n/2\rfloor\).

**At most three ones.** If the first and last bits agree, the one-bit ordinary border exists. Otherwise reversal lets us assume the first bit is zero and the final bit one. Let \(a\geq1\) be the leading zero run and \(d\geq0\) the zero run immediately preceding the final one. If \(a\leq d\), the word has the literal border \(0^a1\). Suppose \(a>d\). For every disjoint prefix/suffix pair of length \(j\) before the prefix reaches its first one, the prefix has zero ones and the suffix at least one. Once the prefix reaches its first one (at \(j=a+1\)), the suffix has already reached the penultimate one (at \(j=d+2\leq a+1\)), if a penultimate one exists. In a word with at most three ones, disjoint prefix and suffix cannot both have at least two ones. Thus the suffix has strictly more ones for every \(j\leq\lfloor n/2\rfloor\); if only one one exists, the prefix never reaches it in that range. No Abelian border exists. Complementation gives the same conclusion for at most three zeros. Ordinary bordering always implies Abelian bordering, finishing the equivalence.

**Four ones and the Abelian condition.** Again an exceptional word has different end bits; reverse it if necessary to arrange first zero and last one, and use the four-gap form displayed above. If \(a\leq d\), there is a literal border, so require \(a>d\). For the remaining words, a disjoint prefix/suffix pair can have equal positive one counts only when each has exactly two ones. Indeed, before the first left one the prefix has zero versus at least one on the right, and when the first left one arrives the right block has already seen two ones; with only four ones overall, equal counts then require two on each side. The prefix first has two ones at length \(a+b+2\). The suffix has precisely two ones at this length if and only if \(a+b+2\leq d+c+2\), or \(a+b\leq c+d\). This condition also guarantees \(a+b+2\leq\lfloor n/2\rfloor\), so it is both necessary and sufficient for an Abelian border when \(a>d\).

**Removing ordinary borders.** In any disjoint ordinary border the numbers of ones on each side are equal and at most two. Zero-one borders cannot occur because the end bits differ. The unique possible border containing one one is \(0^a1\), impossible when \(a>d\). A border with two ones must be exactly \(0^a1\,0^b1\), and occurs precisely when \(b=d\) and \(a\leq c\). Under the Abelian condition \(a+b\leq c+d\), the condition \(b=d\) automatically implies \(a\leq c\). Therefore within the Abelian-bordered range a literal border exists exactly when \(b=d\). This proves (1). Substituting \(e=a-d\geq1\) and \(f=c-b-e\geq0\) yields (2).

**Enumeration.** The two possible opposite endpoint orders contribute equally by reversal. In the zero-first order, a word specified by (2) contains \(m=2e+2b+2d+f\) zeros and four ones. Its generating series by total length is
\[
 z^4\frac{z^2}{1-z^2}\frac1{1-z}
 \left(\frac1{(1-z^2)^2}-\frac1{1-z^4}\right)
 =\frac{2z^8}{(1-z)(1-z^2)^2(1-z^4)}.
\]
Multiplying by two proves (3). Near \(z=1\), the rational function in (3) has principal part \(1/[4(1-z)^4]\), while all other poles contribute at most a quadratic-order coefficient term. Hence \(B_n=n^3/24+O(n^2)\). Finally \(\binom n4=n^4/24+O(n^3)\) proves the ratio estimate. The word \(00110101\) meets (1), showing sharpness at length eight.

## Verification

The standalone, standard-library-only `checker.py` independently tests ordinary borders by direct prefix/suffix equality and Abelian borders by incremental prefix/suffix counts. It checks equality of the two border properties for all \(36{,}455\) binary words of length at most \(30\) containing zero to three ones; checks the complete gap criterion and coefficient counts on all \(80{,}730\) weight-four words of lengths \(4\) through \(26\); and compares an independent coefficient expansion of (3) with an independent parameter-count sum through length \(120\). Run `python3 checker.py`. These finite tests supplement, but do not replace, the proof for unrestricted length.

## Relationship to prior work

Rampersad, Rigo and Salimov (2013) introduce a lattice-path description and enumerate all binary Abelian-unbordered words by length; the expanded Goč–Rampersad–Rigo–Salimov version (2014) gives the corresponding Motzkin-path characterization. Christodoulakis, Christou, Crochemore and Iliopoulos (2014) study minimal Abelian-border lengths and global counting bounds. Blanchet-Sadri, Chen and Hawes (2017) derive the complete all-words distribution by shortest Abelian border length. Charlier, Harju, Puzynina and Zamboni (2016) study bounded Abelian-unbordered factors and infinite-word periodicity. In particular, the eight-letter example \(00110101\) was already known as an ordinarily unbordered, Abelian-bordered example; its existence is **not** claimed here as new. The claim here is the all-length sparse threshold, complete weight-four mixed-border classification, and its rational generating series. The cited global enumerations by Abelian-border status or minimal length do not supply an enumeration of the joint condition involving absence of literal borders, and no directly covering statement was located in the inspected texts.

## Limitations

The exact exceptional-family formula covers binary weight-four words, not every weight or alphabet. No claim is made that the general distinction between ordinary and Abelian borders is new; nor does a targeted literature search establish absolute historical priority. The full text of the 2014 Christodoulakis et al. article could not be accessed, leaving a specific priority risk. Counts concern linear words, not necklace equivalence classes. No independent mathematical audit has been performed.

## References

1. N. Rampersad, M. Rigo and P. Salimov, *On the Number of Abelian Bordered Words*, Developments in Language Theory, LNCS 7907 (2013), 420–432, DOI: `10.1007/978-3-642-38771-5_37`; proceedings published 2013-06-12.
2. D. Goč, N. Rampersad, M. Rigo and P. Salimov, *On the Number of Abelian Bordered Words (with an Example of Automatic Theorem-Proving)*, International Journal of Foundations of Computer Science 25 (2014), 1097–1110, DOI: `10.1142/S0129054114400267`; accessible author-version text `https://scispace.com/pdf/on-the-number-of-abelian-bordered-words-with-an-example-of-43gdbru0k3.pdf`.
3. M. Christodoulakis, M. Christou, M. Crochemore and C. S. Iliopoulos, *Abelian borders in binary words*, Discrete Applied Mathematics 171 (2014), 141–146, DOI: `10.1016/j.dam.2014.02.012`.
4. É. Charlier, T. Harju, S. Puzynina and L. Q. Zamboni, *Abelian bordered factors and periodicity*, European Journal of Combinatorics 51 (2016), 407–418, DOI: `10.1016/j.ejc.2015.07.003`.
5. F. Blanchet-Sadri, K. Chen and K. Hawes, *Dyck Words, Lattice Paths, and Abelian Borders*, EPTCS 252 (2017), 56–70, `https://arxiv.org/abs/1708.06461`.
