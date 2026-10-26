# Three-marker border correlation: a local gap law and its exact distribution

## Finding
Let \(w\) be a directed binary circular word with exactly three occurrences of \(1\) and \(m\ge0\) occurrences of \(0\). Its three cyclic zero-gap lengths are \(a,b,c\ge0\), up to cyclic permutation. For each occurrence of \(1\), write \(L\) for the number of consecutive zeros immediately preceding that marker and \(R\) for the number immediately following it. Then the complete set of unbordered linear rotations is determined **locally** at each marker:

* If \(L>R\), exactly the rotation starting at that marker is unbordered.
* If \(R>L\), exactly the rotation starting at the first zero following that marker is unbordered.
* If \(L=R\), neither boundary rotation is unbordered.

Every other rotation is bordered. Consequently the number \(U(w)\) of **distinct** unbordered conjugates is
\[
 U(w)={\bf1}_{a\ne b}+{\bf1}_{b\ne c}+{\bf1}_{c\ne a}
 =\begin{cases}0& a=b=c,\\2&\text{exactly two gaps equal},\\3&\text{all gaps distinct}.\end{cases}
\]
In particular, three is the sharp upper bound throughout this fixed-content family (including arbitrarily large circumferences).

Let \(C_j(m)\) count directed necklaces (rotation classes, *not* identifying reversal) having three ones, \(m\) zeros, and \(j\) distinct unbordered conjugates. With \(B_m=\binom{m+2}{2}\), \(P_m=\lfloor m/2\rfloor+1\) and \(\delta_m={\bf1}_{3\mid m}\), the **complete distribution** is
\[
 C_0(m)=\delta_m,\qquad C_2(m)=P_m-\delta_m,\qquad
 C_3(m)=\frac{B_m-3P_m+2\delta_m}{3};
\]
all other \(C_j(m)\) vanish. Equivalently,
\[
\sum_{m\ge0}\sum_j C_j(m)x^my^j=
 \frac{1}{1-x^3}
 +y^2\left(\frac{1}{(1-x)(1-x^2)}-\frac{1}{1-x^3}\right)
 +\frac{y^3}{3}\left(\frac{1}{(1-x)^3}-\frac{3}{(1-x)(1-x^2)}+\frac{2}{1-x^3}\right).
\]
For a uniformly random length-\(m+3\) **linear** binary word containing exactly three ones, the expectation is exactly
\[
 \mathbb E[U]=3\left(1-\frac{\lfloor m/2\rfloor+1}{\binom{m+2}{2}}\right),
\]
and \(\Pr(U=3)\to1\) as \(m\to\infty\). The classification, not just its mean, holds at every finite length.

## Assumptions and scope
A nonempty proper border of a finite word \(v\) is a common prefix and suffix of lengths \(1\le\ell<|v|\). A word is *unbordered* if it has none. A conjugate is any cyclic shift, and distinct rotations are counted as distinct words only when their strings differ. The alphabet is exactly \(\{0,1\}\), circular direction is retained, and the word has exactly three ones; zero gaps may vanish. All assertions hold for every integer \(m\ge0\), including the constant word \(111\). A word containing four ones need not obey the local law.

## Proof
**Lemma 1 (marker-start test).** For arbitrary integers \(a,b,c\ge0\), the word
\[v=1\,0^a1\,0^b1\,0^c\]
is unbordered if and only if \(c>a\).

If \(c\le a\), the nonempty word \(1\,0^c\) is both a prefix and a proper suffix of \(v\), so \(v\) is bordered. Conversely suppose \(c>a\) and a proper border exists. Since the border begins with \(1\), its terminal copy starts at one of the two later ones (the first one would give the entire word). If it begins at the last one, the border is exactly \(1\,0^c\), not a prefix because \(c>a\). If it begins at the middle one, the border is \(1\,0^b1\,0^c\). Equality with the prefix forces the two internal zero gaps to agree, \(a=b\), and then forces \(c\le b=a\) for the prefix to contain the terminating \(c\) zeros after its second one. This contradicts \(c>a\). No border exists. Notice that this checks borders of **all** possible lengths, including overlapping ones.

**Lemma 2 (zero-run-start test).** If \(a\ge1\), then
\[u=0^a1\,0^b1\,0^c1\]
is unbordered if and only if \(a>c\). Indeed, reversing \(u\) gives \(1\,0^c1\,0^b1\,0^a\); reversal preserves existence of borders, so Lemma 1 applies.

**Complete local correspondence.** Fix one marker with preceding zero gap \(L\) and following zero gap \(R\), and denote the remaining gap \(T\). The linear rotation starting at the marker is \(1\,0^R1\,0^T1\,0^L\), which by Lemma 1 is unbordered precisely when \(L>R\). If \(R\ge1\), the rotation starting at the first zero of its following run is \(0^R1\,0^T1\,0^L1\), which by Lemma 2 is unbordered precisely when \(R>L\). When \(R=0\) that second start does not exist, but \(R>L\) is impossible since \(L\ge0\). Any other rotation starts and ends with the same symbol \(0\) or \(1\), hence has a border of length one. Every marker contributes exactly one unbordered starting position if its adjacent gaps differ, and otherwise zero.

**Distinctness.** If the three gaps are unequal in any way, the word is primitive: a nontrivial power exponent must divide its number of ones, namely three, so the only possibility would be a cube of a one-one word, forcing all three gaps equal. Thus the unbordered positions counted above represent distinct conjugates. If all gaps coincide, the word is a cube, and the local rule correctly gives zero unbordered conjugates. Summing the three marker comparisons proves the formula for \(U(w)\).

**Necklace enumeration.** Number the three gaps cyclically. There are \(B_m=\binom{m+2}{2}\) nonnegative ordered triples with sum \(m\). Exactly \(\delta_m\) are constant triples. For each repeated value \(r\in\{0,\ldots,\lfloor m/2\rfloor\}\), the third value \(m-2r\) is nonnegative; excluding the single case \(r=m/3\) when integral leaves \(P_m-\delta_m\) necklace classes with exactly two equal gaps. Each such class has three labeled presentations, as does each all-distinct class; constant triples have one. Subtracting these presentations gives \(C_3(m)=(B_m-3(P_m-\delta_m)-\delta_m)/3\). Geometric-series summation proves the generating function.

**Linear-word expectation.** Every necklace with unequal gaps has exactly \(n=m+3\) linear rotations; the equal-gap necklace, when present, has \(n/3\). Since \(\binom n3=nB_m/3\), the sum of unbordered-conjugate counts over all labeled three-one words is \(n(2C_2(m)+3C_3(m))=n(B_m-P_m)\). Dividing by \(nB_m/3\) yields the stated expectation. Moreover the probability of three unbordered conjugates is \(3C_3(m)/B_m=1-(3P_m-2\delta_m)/B_m\), which tends to one.

**Sharp scope boundary.** The primitive four-one word \(1100110\) has cyclic gaps \((0,2,0,1)\). Its initial marker is preceded by one zero and followed by zero zeros, but its rotation \(1100110\) has proper border \(110\). Thus the local comparison theorem is specific to the three-marker setting, not a general principle for arbitrarily many markers.

## Verification
Run `python3 checker.py`. The independent program constructs each cyclic word with three ones and at most thirty zeros, enumerates all distinct rotations and all proper borders, and compares them with the local formula for \(5456\) zero-gap triples. It separately checks each local lemma, enumerates the complete necklace distributions for all \(0\le m\le16\) directly from all labeled words, checks algebraic orbit counts through \(m=30\), and tests the four-marker limitation. These finite computations confirm boundaries and provide regression tests; the proof above supplies the all-length conclusion.

## Relationship to prior work
Holub and Müller (arXiv:1504.02222, first public 2015-04-09, primary subject 68R15) characterize binary words with precisely two unbordered conjugates via *fully bordered* pairs and derive a palindrome-pair condition. The present local three-gap theorem also determines every **three**-unbordered configuration and every individual unbordered starting position, and gives an exact fixed-content distribution, not supplied by their stated classification. Harju and Nowotka (2004) developed general binary border-correlation and sharp unconstrained bounds. Clokie, Gabric and Shallit (2019) give the unrestricted random-word expectation \(n u_2(n)/2^n\); our constant-weight-three expectation conditions on a sparse composition and is not obtained by that unrestricted mean. The natural coding-theoretic object is the *border-correlation trace* of each circular word, rather than just its minimum- or maximum-conjugate count.

## Limitations
No claim is made that the local law extends beyond exactly three ones or to a larger alphabet. The 2004 foundational journal article's complete text could not be inspected in this investigation; an unpublished or previously embedded equivalent specialization cannot be definitively excluded. A complete classification of the four-one case is not attempted. The result has not undergone independent mathematical audit.

## References
1. Š. Holub and M. Müller, *Fully bordered words*, arXiv:1504.02222, first public 9 April 2015. https://arxiv.org/abs/1504.02222
2. T. Harju and D. Nowotka, *Border correlation of binary words*, Journal of Combinatorial Theory, Series A 108 (2004), 331–341. https://doi.org/10.1016/j.jcta.2004.07.009
3. T. Clokie, D. Gabric and J. Shallit, *Circularly squarefree words and unbordered conjugates: a new approach*, arXiv:1904.08187 (2019). https://arxiv.org/abs/1904.08187
