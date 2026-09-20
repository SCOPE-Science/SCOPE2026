# Same-model review

## Result reviewed

**Accelerated filtrations break arbitrary-filtration entropy–growth implications**

The reviewed claims are:

1. every infinite-dimensional affine algebra admits the accelerated finite-dimensional filtrations
   \[
   V_0=0,\qquad V_n=U^{b^n}\quad(b\ge2)
   \]
   with algebraic entropy at least \(\log b\);
2. for \(k[x]\), the entropy of this filtration is exactly \(\log b\), although \(\operatorname{GKdim}k[x]=1\) and its intrinsic growth is polynomial;
3. this gives direct counterexamples to the arbitrary-finite-dimensional-filtration formulations of Theorems 3.7, 3.9 and 3.14 of arXiv:2609.18144v1, and to the analogous arbitrary-filtered module implication;
4. intrinsic growth is always bounded above by the growth measured by an arbitrary exhaustive filtration, and equality is restored when that filtration is linearly upper-controlled by a standard filtration.

## Correctness review

### Filtration check

For \(n,m\ge1\),
\[
b^n+b^m\le b^{n+m}
\]
when \(b\ge2\). Therefore
\[
U^{b^n}U^{b^m}\subseteq U^{b^n+b^m}\subseteq U^{b^{n+m}}.
\]
The filtration is finite-dimensional because \(U\) is finite-dimensional, and exhaustive because \(U\) generates \(A\).

### Entropy lower bound

If \(A\) is infinite-dimensional and \(1\in U\), no equality \(U^r=U^{r+1}\) can occur: such an equality would make all subsequent powers equal and force \(A=U^r\) finite-dimensional. Hence dimension rises by at least one at every integer step, giving
\[
\dim U^{b^n}-\dim U^{b^{n-1}}\ge b^n-b^{n-1}.
\]
Taking the entropy limsup yields \(h_{\rm alg}\ge\log b\).

For \(k[x]\), the chosen space has dimension \(b^n+1\), so
\[
\dim(V_n/V_{n-1})=(b-1)b^{n-1},
\]
and the entropy is exactly \(\log b\). This is incompatible with any assertion that positive entropy for an arbitrary finite-dimensional filtration forces infinite GK dimension or exponential intrinsic growth.

### Growth-comparison repair

For an arbitrary exhaustive filtration, a finite generating space \(U\) is contained in some \(V_s\), whence
\[
U^n\subseteq V_{sn}.
\]
This proves the one-sided growth comparison.

If also \(V_n\subseteq U^{an+c}\) for large \(n\), the reverse coarse comparison follows. For positive entropy, infinitely many filtration quotients are exponentially large. Their inclusion in \(U^{an+c}\) gives a positive exponential lower rate along a subsequence. Since
\[
\dim U^{r+s}\le(\dim U^r)(\dim U^s),
\]
Fekete's lemma makes \(\log\dim U^r/r\) converge; the subsequence lower bound therefore forces a positive limit, which is equivalent to exponential intrinsic growth.

For modules, the same upper linear control converts exponentially large filtered pieces along a subsequence into values of the standard module growth function whose logarithms are linear in the radius; division by \(\log r\) then forces infinite GK dimension.

### Adversarial checks

- The use of \(V_0=0\) causes no multiplicativity issue.
- The inequality \(b^n+b^m\le b^{n+m}\) includes the boundary case \(b=2,n=m=1\).
- The strictness of every \(U^r\subset U^{r+1}\) uses \(1\in U\), which is stated.
- The exact polynomial-ring computation does not depend on characteristic.
- The correction is restricted to arbitrary filtrations; it does not infer failure of separately proved graded or standard-filtration results.

**Correctness: PASS.**

## Originality review

The 2024 paper by Bock et al. was checked because it introduced the filtered algebraic entropy used by the 2026 source. It explicitly observes that entropy depends on the filtration, proves that linear reindexing \(W_n=V_{kn}\) multiplies a pre-existing entropy by \(k\), and notes that a nonzero entropy can therefore be enlarged. It also proves persistence of zero entropy under several restricted changes, including linear reindexing and standard filtrations. Those facts are prior art and are not claimed as new here.

The present contribution uses exponential rather than linear reindexing. It shows that even an algebra whose standard entropy is zero, such as \(k[x]\), can acquire positive entropy under a valid finite-dimensional filtration. Targeted searches for the source arXiv identifier, exponential/accelerated filtration reindexing, polynomial-algebra positive filtered entropy, and corrections to the September 2026 preprint did not reveal a published correction or the same counterexample-and-repair package.

The source preprint is extremely recent, so a concurrent observation or subsequent revision remains a substantial originality risk. The full text of Krause–Lenagan's book proposition cited by the source was not directly inspected. This does not affect correctness because the counterexample addresses the theorem exactly as stated in arXiv:2609.18144v1, but it limits any claim about how the source's citation should have been formulated.

**Originality: PASS, to the best of our knowledge.**

## Value review

The counterexample is elementary but affects several central arbitrary-filtration implications in a new paper: equality of intrinsic and filtration growth, positive-entropy forcing infinite GK dimension, and positive-entropy forcing exponential growth. The universal acceleration theorem identifies the mechanism rather than giving only an isolated example, while the linear-control proposition supplies a usable corrected hypothesis.

The distinction is also conceptually useful: algebraic entropy is an invariant of a filtered algebra, and without quantitative comparison of the filtration index to word length it cannot diagnose the intrinsic growth type of the underlying affine algebra.

**Value: PASS.**

## Scientific limitations

- No claim is made that filtration dependence itself is new.
- No claim is made that standard-filtration or graded results in arXiv:2609.18144v1 fail merely because the arbitrary-filtration statements fail.
- The source is v1 of a preprint submitted on 16 September 2026 and may be revised.
- Originality is necessarily qualified by the very short interval since that submission and by the uninspected full text of the cited Krause–Lenagan proposition.

Same-model review: passed. Independent audit: not yet performed.
