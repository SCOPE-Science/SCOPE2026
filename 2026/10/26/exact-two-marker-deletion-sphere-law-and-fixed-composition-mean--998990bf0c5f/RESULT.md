# Exact two-marker deletion-sphere law and fixed-composition mean

## Finding
Let \(n\ge2\), \(0\le t\le n\), and \(L=n-t\). Write every binary length-\(n\) word of weight two uniquely as
\[
w=0^a1\,0^b1\,0^c,\qquad a,b,c\in\mathbb Z_{\ge0},\quad a+b+c=n-2.
\]
Let \(D_t(w)\) be the **set of distinct** length-\(L\) scattered subsequences produced by deleting exactly \(t\) letters; distinct deletion patterns producing the same output are counted once. Put \((v)_+=\max(v,0)\) and \(P_h(x)=1+x+\cdots+x^h\), for \(h\ge0\).

**Pointwise formula.** For all these parameters,
\[
|D_t(w)|=[x^t]P_a(x)P_b(x)P_c(x)
+\mathbf1_{\{t\ge1,L\ge1\}}\bigl(L-(a-t+1)_+-(b-t)_+-(c-t+1)_+\bigr)
+\mathbf1_{\{t\ge2\}}.
\tag{1}
\]
The three terms count descendants with two, one, and zero ones, respectively. The coefficient is taken to be zero when \(t>a+b+c\).

**Exact fixed-composition mean.** Set \(T_{n,t}=\sum_{w\in\{0,1\}^n:|w|_1=2}|D_t(w)|\). Then
\[
\boxed{T_{n,t}=\binom{t+2}{2}\binom{L}{2}+tL^2+\binom t2 L+\mathbf1_{\{t\ge2\}}\binom n2.}
\tag{2}
\]
Here \(\binom{L}{2}=0\) for \(L\in\{0,1\}\); the mean over the \(\binom n2\) distinct source words is exactly \(T_{n,t}/\binom n2\). Formula (2) holds **simultaneously for all lengths and every deletion count**, including \(t=0\), \(t=n-1\), and \(t=n\).

**Exact maximum at every finite length.** Write \(n-2=3q+r\), with \(q\ge0\), \(r\in\{0,1,2\}\). Select
\[
(a_*,b_*,c_*)=\begin{cases}(q,q,q),&r=0,\\(q,q+1,q),&r=1,\\(q+1,q+1,q),&r=2.\end{cases}
\]
Then for every \(0\le t\le n\), the maximum of \(|D_t(w)|\) over the fixed-weight-two family is \(|D_t(0^{a_*}1\,0^{b_*}1\,0^{c_*})|\), as computed explicitly by (1). Thus it is evaluable by a product of three finite geometric sums without optimizing over words.

**Sharp saturation threshold and extremizers.** For every integer \(t\ge1\),
\[
|D_t(w)|\le M_t:=\binom{t+2}{2}+2t+\mathbf1_{\{t\ge2\}}.
\tag{3}
\]
Equality is possible at length \(n\) if and only if \(n\ge3t+2\); for such lengths equality holds **exactly** when \(a,b,c\ge t\). There are then precisely \(\binom{n-3t}{2}\) maximizing words. At the first possible length \(3t+2\), the unique maximizer is \(0^t1\,0^t1\,0^t\). For fixed \(t\ge1\), the maximizing proportion is \(\binom{n-3t}{2}/\binom n2\), tending to one as \(n\to\infty\). The case \(t=0\) is trivial: every source has one zero-deletion descendant.

## Assumptions and scope
The alphabet is exactly \(\{0,1\}\), words are linear and labeled by their positions, the source weight is exactly two, deletion count is exact rather than up to \(t\), and only distinct resulting words are counted. No distribution on deletion patterns is asserted; the average in (2) is uniform over source words. The formulas are integer identities, not asymptotic approximations. There is no claim about unrestricted source weights, insertion spheres, intersections of two balls, or coding capacity.

## Proof
**1. Retaining both ones.** Any descendant with two ones uniquely specifies retained zero gaps \((i,j,k)\) with \(0\le i\le a\), \(0\le j\le b\), \(0\le k\le c\) and \(i+j+k=L-2\). Equivalently, the deleted-zero gaps form \((a-i,b-j,c-k)\) with total \(t\). Hence their exact count is \([x^t]P_aP_bP_c\).

**2. Retaining exactly one one.** Assume \(1\le t\le n-1\), so \(L\ge1\), and index a weight-one output by its unique one's position \(i\in\{0,\dots,L-1\}\), measured as the number of zeros preceding it. Retaining the first source one yields exactly
\[
I_1=[\max(0,a-t+1),\min(a,L-1)]\cap\mathbb Z,
\]
whereas retaining the second yields exactly
\[
I_2=[\max(0,a+b-t+1),\min(a+b,L-1)]\cap\mathbb Z.
\]
Indeed, one of the \(t\) deletions removes the other one and the remaining \(t-1\) deletions remove zeros. The uncovered points in \(\{0,\ldots,L-1\}\) occur only before \(I_1\), between \(I_1\) and \(I_2\), or after \(I_2\). Their respective counts are exactly \((a-t+1)_+\), \((b-t)_+\), and \((c-t+1)_+\). Thus \(|I_1\cup I_2|=L-(a-t+1)_+-(b-t)_+-(c-t+1)_+\). For \(t=0\) or \(L=0\), no weight-one output exists.

**3. Retaining no ones.** The only weight-zero output is \(0^L\), obtainable precisely when at least the two marked positions can be deleted, i.e. \(t\ge2\). This includes \(L=0\), when the output is the empty word. These three disjoint output weights prove (1).

**4. Sum over all sources.** There are \(\binom n2\) source gap triples \((a,b,c)\). To count source/descendant pairs of output weight two, choose the three deleted-zero counts summing to \(t\), in \(\binom{t+2}{2}\) ways, and the three surviving-zero counts summing to \(L-2\), in \(\binom L2\) ways (zero if \(L<2\)). Their coordinatewise sums recover the unique source gap triple; hence this product counts pairs without multiplicity.

For output weight one, the interval-complement description in step 2 gives, for \(t\ge1\), the total
\[
\binom n2 L-2\binom{L+1}{3}-\binom L3=tL^2+\binom t2 L.
\]
To justify the subtractions directly, the sum over all \(a+b+c=n-2\) of \((a-t+1)_+\) (and likewise for \(c\)) is \(\binom{L+1}{3}\); the sum of \((b-t)_+\) is \(\binom L3\), by setting the corresponding gap above its threshold and applying the elementary composition sum \(\sum_{u=0}^m(u+1)(m-u+1)=\binom{m+3}{3}\). The displayed equality follows by substituting \(n=t+L\); its right-hand side also equals zero at \(t=0\), handling that boundary separately. For output weight zero, every source contributes one if \(t\ge2\). Summing the three output-weight classes proves (2).

**5. Exact finite-length maximum.** If two zero gaps satisfy \(u\ge v+2\), transferring one zero from the longer to the shorter changes their polynomial product by
\[
P_{u-1}(x)P_{v+1}(x)-P_u(x)P_v(x)=x^{v+1}+x^{v+2}+\cdots+x^{u-1},
\]
which has nonnegative coefficients. Multiplication by the third gap polynomial shows the two-one term cannot decrease. For the one-one term, let the three deficit thresholds be \(t-1,t,t-1\); decreasing a longer gap by one and increasing a shorter gap by one cannot increase the sum of their positive-part deficits. Explicitly, a new positive unit at a threshold \(\theta_v\in\{t-1,t\}\) requires \(v\ge\theta_v\), hence \(u\ge v+2\ge t+1\), so an old positive unit is simultaneously removed at threshold \(\theta_u\le t\). The zero-one term is constant. Iterating such transfers reaches gaps differing pairwise by at most one and does not decrease (1).

Among these balanced triples the coefficient term is symmetric in gap order. The one-one deficit is minimized by placing one of the larger gaps in the middle when \(r>0\). Indeed, for \(r=1\), moving the sole length-\(q+1\) gap from an outer position to the middle changes the deficit by the negative of \((v+1)_++(v-1)_+-2(v)_+\) with \(v=q-t+1\); this quantity is zero except at \(v=0\), where it is one. The same comparison, interchanging which gap is smaller, applies when \(r=2\). This proves that the displayed canonical triple realizes an exact maximum. No assertion that it is the only maximizer is required for this finite-length statement.

**6. Saturation.** The coefficient term is at most \(\binom{t+2}{2}\), because every deletion allocation of \(t\) zeros among three gaps is counted at most once. Equality requires all three allocations \((t,0,0)\), \((0,t,0)\), and \((0,0,t)\) to be available, hence \(a,b,c\ge t\), and that condition also suffices. The one-one term is at most \(2t\), because it is the union of two integer intervals each of length at most \(t\). When all three gaps are at least \(t\), each interval has length \(t\), and the two are disjoint since \(b\ge t\). The zero-one term is fixed. Thus (3) is sharp precisely for \(a,b,c\ge t\). The composition count for triples satisfying this is \(\binom{n-3t}{2}\), proving all remaining assertions.

## Verification
The standalone file `check.py` uses one method to enumerate deletion outputs as sets of surviving-position subsequences, and a separate method to compute (1) by bounded gap-polynomial convolution and the interval deficit. It compares all parameters at lengths \(2\) through \(12\), including \(t=0\), full deletion, and the empty output. It then checks (2) by summation for those lengths and tests the balanced finite-length maximum and the complete saturation-classifier for lengths through \(54\). On execution it reports 3,003 direct comparisons and 1,101,870 finite maximum-classification instances. These are finite consistency checks; the all-length results rely on steps 1–6 above. Reproduce with `python3 check.py` using only the Python standard library.

## Relationship to prior work
Levenshtein's 1965/1966 work introduced foundational deletion-sphere bounds in terms of runs; it does not supply the present fixed-weight-two all-radius mean. Hirschberg and Regnier analyzed the maximum and average size over *unrestricted* source words, which is a different averaging measure. Mercier, Khabbazian and Bhargava developed general deletion-subsequence counting methods and explicit small-radius formulas; their full 2008 text was not available for a direct exact-formula comparison. Liron and Langberg proved, in Lemma II.7 of their 2012 preprint, that certain run-balancing operations increase the number of deletion descendants. That stronger general monotonicity anticipates and can imply the balancing part of step 5; balancing alone is **not** a novelty claim. The substantive contribution assessed here is the combined exact gap-dependent all-radius law and the conditional fixed-weight-two mean in (2), with its sharp high-radius saturation and precisely counted extreme plateau. None of the inspected accessible primary texts presents that conditional mean as an all-parameter identity.

## Limitations
The source weight is fixed at exactly two; neither the formulas nor the constant saturation bound extend automatically to arbitrary weight. Only uniform sampling of source words is averaged, not random deletion positions. The proof is elementary and self-contained, but priority remains uncertain because some relevant older papers, notably Mercier–Khabbazian–Bhargava (2008), were available only at abstract/bibliographic level. These access limits are not evidence that an equivalent theorem is absent. A separate independent validation has not been performed.

## References
1. V. I. Levenshtein, *Binary codes capable of correcting deletions, insertions, and reversals*, Soviet Physics Doklady 10 (1966), 707–710 (Russian original 1965).
2. D. S. Hirschberg and M. Regnier, *Tight Bounds on the Number of String Subsequences*, Journal of Discrete Algorithms 1 (2000), 123–132. Author-hosted full text: https://www.ics.uci.edu/~dan/pubs/JDA.pdf .
3. H. Mercier, M. Khabbazian and V. K. Bhargava, *On the Number of Subsequences When Deleting Symbols From a String*, IEEE Transactions on Information Theory 54 (2008), 3279–3285. DOI: https://doi.org/10.1109/TIT.2008.924730 .
4. Y. Liron and M. Langberg, *A characterization of the number of subsequences obtained via the deletion channel*, first public arXiv version 2012-02-08. https://arxiv.org/abs/1202.1644 . In particular, inspect Lemma II.7 and Sections III–IV for the distinct, more general run-balancing and balanced-run bounds.
