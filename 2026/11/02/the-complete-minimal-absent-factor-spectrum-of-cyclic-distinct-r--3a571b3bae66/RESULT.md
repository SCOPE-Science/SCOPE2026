# The complete minimal-absent-factor spectrum of cyclic distinct-run powers

## Finding

Let \(q\ge3\), let \(a_0,\ldots,a_{q-1}\) be distinct letters, let \(r_0,\ldots,r_{q-1}\ge1\), and let \(k\ge2\). Put \(P=a_0^{r_0}\cdots a_{q-1}^{r_{q-1}}\), \(p=\sum_i r_i\), and \(T=P^k\). All indices below are taken modulo \(q\). A *minimal absent factor* is a nonempty word absent as a contiguous factor of \(T\) whose every proper contiguous factor occurs in \(T\).

The complete set \(\operatorname{MAW}(T)\) is the following disjoint union:

\[
\begin{aligned}
\mathcal B&=\{a_i a_j:0\le i,j<q,\ j\not\equiv i,i+1\pmod q\},\\
\mathcal R&=\{a_i^{r_i+1}:0\le i<q\},\\
\mathcal I&=\{a_{i-1}a_i^t a_{i+1}:0\le i<q,\ 1\le t<r_i\},\\
\mathcal E&=\{a_{q-1}P^{k-1}a_0\}.
\end{aligned}
\]

Consequently the number of minimal absent factors is independent of the repetition count \(k\):

\[
\boxed{|\operatorname{MAW}(T)|=q(q-2)+p+1.}
\]

More precisely, their exact length enumerator is

\[
\boxed{\sum_{u\in\operatorname{MAW}(T)}z^{|u|}=
q(q-2)z^2+\sum_{i=0}^{q-1}\left(z^{r_i+1}+\sum_{t=1}^{r_i-1}z^{t+2}\right)+z^{(k-1)p+2}.}
\]

All members except the final one are invariant under increasing \(k\) beyond two; exactly one absent factor changes, and its length increases by \(p\) per additional copy. This is a statement about *contiguous* absent factors, not absent scattered subsequences or circular factors.

## Assumptions and scope

The alphabet is precisely \(\Sigma=\{a_0,\ldots,a_{q-1}\}\), with all labels pairwise distinct. The order of labels and the positive run lengths are arbitrary. The condition \(q\ge3\) is essential to this family description; the binary case is not asserted. A factor is contiguous. Both endpoints of the linear input \(P^k\) are meaningful: factors of its associated infinite circular word form a different language. The zero-length word is a factor by convention but never a minimal absent factor because every alphabet letter occurs.

## Proof

**1. All local obstructions and no others in the infinite periodic language.** Let \(L\) be the collection of finite factors of the two-sided infinite periodic word \(\cdots PPP\cdots\). Within this word, different neighboring letters can only form one of the directed transitions \(a_i a_{i+1}\). Every run of \(a_i\) has length \(r_i\), and every run strictly inside a factor spanning at least three runs has its full length \(r_i\).

Each word in \(\mathcal B\) is absent from \(L\), but its letters occur. Each \(a_i^{r_i+1}\) in \(\mathcal R\) is absent with its proper prefix and suffix of length \(r_i\) present. Each \(a_{i-1}a_i^t a_{i+1}\) with \(1\le t<r_i\) is absent because the two indicated run boundaries in \(L\) must enclose exactly \(r_i\) copies of \(a_i\); its proper prefix occurs at the start of an \(a_i\)-run and its proper suffix at the end of such a run. Thus all of \(\mathcal B\cup\mathcal R\cup\mathcal I\) are minimal absent factors of \(L\).

Conversely, consider a finite word avoiding these three families. Its run labels must follow the directed cyclic order, since any different-letter pair not following the order lies in \(\mathcal B\). Each run has length at most its prescribed \(r_i\), since otherwise it contains a member of \(\mathcal R\). Each *internal* run has length exactly \(r_i\), since a shorter one would yield a factor \(a_{i-1}a_i^t a_{i+1}\in\mathcal I\). The first and final runs, if any, may be partial. This is precisely the form of a factor of \(\cdots PPP\cdots\), including words having only one or two runs. Thus these are **all** minimal absent factors of \(L\).

**2. Short periodic factors always occur in the finite power.** The length of \(T\) is \(n=kp\). Any factor of \(L\) of length at most \(n-p+1\) may be started at a representative position among the first \(p\) positions of \(T\); it then finishes by position \(n\). Therefore it occurs in \(T\).

Suppose now that \(u\) is a minimal absent factor of \(T\) not belonging to the three local families. Such a word cannot contain any of the local minimal absent factors as a proper factor; hence it avoids the local families entirely and, by step 1, belongs to \(L\). Since it is absent in \(T\), its length \(m\) satisfies \(m\ge n-p+2\).

**3. The endpoint obstruction is unique.** Since \(k\ge2\), both the proper prefix \(v=u[1..m-1]\) and the proper suffix \(w=u[2..m]\) have length at least \(p+1\). Every periodic factor of this length contains a transition between two distinct letters, and the ordered transition determines a unique phase modulo \(p\), because each directed pair \(a_i a_{i+1}\) appears only once per period. Hence any occurrence of \(v\) in \(T\) that could be extended by one position to the right would extend to the same next letter as \(u\), contradicting that \(u\) is absent. Since \(v\) does occur by minimality, it must be the length-\((m-1)\) suffix of \(T\). Symmetrically, \(w\) must be the length-\((m-1)\) prefix of \(T\).

It follows that \(u[2..m-1]\) is both a prefix and suffix of \(T\), hence is a border of length \(m-2\). Because the first and last letters of \(P\) are distinct, \(P\) is unbordered and has shortest period \(p\). Also \(T=P^k\) has shortest period \(p\): any period smaller than \(p\) would restrict to a period of \(P\). Therefore every proper border of \(T\) has length at most \(n-p\), so \(m-2\le n-p\). Combined with \(m\ge n-p+2\), this forces \(m=n-p+2\), and the border must be exactly \(P^{k-1}\). The letters immediately preceding the terminal border and following the initial border are \(a_{q-1}\) and \(a_0\), respectively. Hence necessarily \(u=a_{q-1}P^{k-1}a_0\).

This word is indeed minimal absent: its proper prefix \(a_{q-1}P^{k-1}\) begins at the last position of the first copy of \(P\) and ends at the end of \(T\), while its proper suffix \(P^{k-1}a_0\) occurs at the start of \(T\). It cannot occur in \(T\), since its first transition \(a_{q-1}a_0\) forces its start at the final letter of some copy of \(P\), no earlier than position \(p\), and its length \((k-1)p+2\) would extend beyond position \(kp\).

**4. Disjointness and enumeration.** The three local families have distinct structural forms: a forbidden unequal bigram, a pure-letter overrun, and a word with two successive distinct-letter transitions. They are pairwise disjoint and their maximum length is less than \(p+2\), whereas the unique endpoint word has length \((k-1)p+2\ge p+2\). Their sizes are respectively \(q(q-2)\), \(q\), and \(\sum_i(r_i-1)=p-q\), plus one. Summing proves the count and recording the exact lengths gives the displayed polynomial. \(\square\)

## Verification

`verify.py` provides an independent literal factor-language implementation. It generates every distinct factor of each test input; computes minimal absent factors by combining occurring left and right one-letter extensions around an occurring interior (plus absent bigrams); and compares the resulting **sets of words** to the four claimed families. It also checks the exact count. Run `python3 verify.py` with Python 3 standard library. The completed test comprises 147 parameter cases and 2,104 actual minimal absent words, with \(q=3,4,5,6\), several run-length profiles, and repetition counts including \(k=2,3,4\). These finite tests corroborate the theorem but are not its proof.

For example, if \(P=\texttt{aaabbc}\) and \(k=2\), the ten minimal absent factors consist of three non-successor unequal bigrams, three pure-letter overflows, three incomplete-interior-run words, and the endpoint word \(\texttt{caaabbca}\).

## Relationship to prior work

Fici, Restivo and Rizzo (arXiv:1707.04450, 2017) treat the minimal forbidden factors of circular words and prove their relation to length-bounded minimal forbidden factors of the doubled period; they also enumerate the special circular word with all symbols distinct. Charalampopoulos and coauthors (arXiv:1806.02718, 2018) extend minimal-absent-word algorithms and sequence comparisons to circular words. Akagi and coauthors (arXiv:2202.13591, 2022) study minimal absent words under run-length encoding and obtain general structural categories and output-sensitive algorithms. Those general results motivate the present family, but the inspected statements do not give the exact all-run-length linear-power antidictionary, its length distribution, or its one-moving-endpoint law. The all-singleton circular core is consistent with the earlier distinct-symbol circular example, not independently new.

## Limitations

The theorem applies only to powers \(P^k\) of a block with each of at least three symbols occupying exactly one run. It does not assert a similar formula for repeated symbols appearing in separated runs, arbitrary primitive periods, binary blocks, \(k=1\), or the circular factor language alone. No independent scientific audit of the new derivation has been performed. The literature comparison cannot exclude every unindexed equivalent formulation.

## References

1. G. Fici, A. Restivo, L. Rizzo, *Minimal Forbidden Factors of Circular Words*, arXiv:1707.04450 (first submitted 14 July 2017). https://arxiv.org/abs/1707.04450
2. P. Charalampopoulos, M. Crochemore, G. Fici, R. Mercaş, S. P. Pissis, *Alignment-free sequence comparison using absent words*, arXiv:1806.02718 (submitted 7 June 2018). https://arxiv.org/html/1806.02718v1
3. T. Akagi, K. Okabe, T. Mieno, Y. Nakashima, S. Inenaga, *Minimal Absent Words on Run-Length Encoded Strings*, arXiv:2202.13591 (submitted 28 February 2022). https://arxiv.org/abs/2202.13591
