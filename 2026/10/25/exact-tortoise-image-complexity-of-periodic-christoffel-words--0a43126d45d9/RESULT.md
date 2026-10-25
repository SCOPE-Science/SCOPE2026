# Exact tortoise-image complexity of periodic Christoffel words

## Finding
Let \(q\ge2\), \(1\le p<q\), and \(\gcd(p,q)=1\). Define the infinite periodic lower mechanical word \(x=x_0x_1\cdots\) by
\[
x_i=\left\lfloor\frac{(i+1)p}{q}\right\rfloor-\left\lfloor\frac{ip}{q}\right\rfloor\quad(i\ge0).
\]
It is the periodic repetition of a primitive binary Christoffel word with \(p\) ones in a period of length \(q\). For a binary finite word \(u\), define \(T(u)\) by deleting its first occurrence of \(1\) and appending \(1\) to the right; set \(T(0^n)=0^n\) and \(T(\epsilon)=\epsilon\). Define \(R_{p,q}(n)\) as the number of distinct \(T\)-images among the length-\(n\) factors of \(x\).

Put \(h=\lfloor(q-1)/p\rfloor\). Then, for every integer \(n\ge1\),
\[
\boxed{R_{p,q}(n)=\begin{cases}
n+1-\min\{n-1,h\},&1\le n<q,\\
\min\{q,n-h\},&n\ge q.
\end{cases}}
\]
Moreover \(R_{p,q}(0)=1\). In particular, the tortoise images eventually distinguish all \(q\) cyclic factors, and the *exact first length of permanent injectivity* is \(q+h\). At the period boundary the count is \(R_{p,q}(q)=q-h\), while \(R_{p,q}(q-1)=q-h\) if \(p>1\), and \(R_{1,q}(q-1)=2\), \(R_{1,q}(q)=1\) if \(p=1\).

## Assumptions and scope
The alphabet is ordered \(0<1\), factors are contiguous, and the one-step tortoise map is the binary restriction of the Defant–Kravitz operator. The word is the *lower mechanical* periodic coding, with rational reduced slope \(p/q\); changing its phase or cyclically rotating its primitive period does not change its factor language. The assertion is for all positive lengths, including lengths beyond the period. No irrational-slope statement is claimed here.

## Proof
Write \(\alpha=p/q\). For \(t\in[0,1)\), let
\[
b_i(t)=\lfloor t+(i+1)\alpha\rfloor-\lfloor t+i\alpha\rfloor,
\qquad B_n(t)=b_0(t)\cdots b_{n-1}(t).
\]
The orbit of \(t=0\) under addition of \(\alpha\) modulo one visits all \(q\) grid points \(0,1/q,\ldots,(q-1)/q\), since \(p\) and \(q\) are coprime. The factors of \(x\) of length \(n\) are precisely the values of \(B_n(t)\) on the open cells cut out by the distinct discontinuities \(t_j=\{-j\alpha\}\) with \(0\le j\le n\). To see the endpoint convention, the floor coding is right-continuous, so each grid endpoint yields the adjacent cell's word on its right. For \(n<q\), there are \(n+1\) cells; for \(n\ge q\), all \(q\) grid endpoints occur and there are \(q\) cells.

**Transition lemma.** Sort these cells by increasing \(t\). At an internal boundary \(t_j\) with \(1\le j<q\), the earliest changes in the length-\(n\) binary word are at coordinates \(j-1,j\), when both exist: the block \(01\) changes to \(10\). Indeed the term \(\lfloor t+j\alpha\rfloor\) increases by one, raising coordinate \(j-1\) and lowering coordinate \(j\); no earlier floor term changes. If \(j=n<q\), only the last coordinate changes, from \(0\) to \(1\). For \(n\ge q\), subsequent simultaneous jumps occur at floor indices \(j+q,j+2q,\ldots\), hence at the corresponding pairs of coordinates \(j+q-1,j+q\), etc. The first changed coordinate remains \(j-1\). In every case the factor words strictly increase lexicographically along the ordered cells. Therefore all cell words are distinct, establishing the factor counts given above.

**Image transition lemma.** The images under \(T\) of these cell words are *nondecreasing* lexicographically. For a transition \(P01S\to P10S\), if \(P\) contains a \(1\), its first \(1\) is unchanged, and deletion followed by appending preserves the first changed comparison: the image strictly increases. If \(P\) consists entirely of zeros, both words lose the respective \(1\) displayed in the swap, leaving the same \(P0S1\), provided there is no further change in \(S\). A terminal change \(P0\to P1\) always strictly increases the image: either both words delete a common earlier \(1\), or \(P=0^{n-1}\) and the images are \(0^n\) and \(0^{n-1}1\). In the periodic case, after deletion of the initial swapped \(1\), the first subsequent simultaneous jump at floor index \(j+q\) creates a strict increase as soon as its first changed coordinate \(j+q-1\) enters the length-\(n\) factor. Thus an internal boundary indexed by \(j\) is an equality between neighboring \(T\)-images exactly when the prefix before coordinate \(j-1\) has no \(1\), and (when \(n\ge q\)) also \(n<q+j\).

The condition on the prefix can be evaluated arithmetically. For \(1\le j<q\), the number of ones in its first \(j-1\) coordinates at either side of \(t_j\) is
\[
\lfloor t_j+(j-1)\alpha\rfloor-\lfloor t_j\rfloor
=\lfloor\lceil j\alpha\rceil-\alpha\rfloor=\lfloor j\alpha\rfloor.
\]
Here \(j\alpha\) is not integral because \(j<q\) and the fraction is reduced, and \(\lceil j\alpha\rceil-\alpha\) lies strictly between \(\lfloor j\alpha\rfloor\) and \(\lfloor j\alpha\rfloor+1\). Consequently this prefix is all zero precisely for \(jp<q\), or equivalently \(1\le j\le h=\lfloor(q-1)/p\rfloor\).

If \(1\le n<q\), there are \(n+1\) ordered factors. Of their \(n\) adjacent boundaries, the boundary indexed by \(j=n\) is strictly increasing, while precisely \(\min\{n-1,h\}\) among \(1\le j<n\) identify neighboring tortoise images. Since the image list is nondecreasing, every fiber occupies consecutive cells; hence the number of distinct images is
\[
(n+1)-\min\{n-1,h\}.
\]

If \(n\ge q\), there are \(q\) ordered factors. The internal boundaries are indexed by \(j=1,\ldots,q-1\). Exactly the indices \(1\le j\le h\) for which \(j>n-q\) still identify neighboring images. The number of equal adjacent image pairs is therefore
\[
\max\{0,h-(n-q)\}.
\]
Again consecutive-fiber monotonicity gives
\[
R_{p,q}(n)=q-\max\{0,h-(n-q)\}=\min\{q,n-h\}.
\]
This also proves injectivity for \(n\ge q+h\), and noninjectivity for \(n=q+h-1\), proving the sharp threshold. The empty factor gives the remaining value \(R_{p,q}(0)=1\). \(\square\)

## Verification
The standalone script `check.py` independently constructs each primitive period using integer-floor arithmetic, enumerates all cyclic factors, applies the binary tortoise map directly, and compares the exact image counts to the formula. It checks all \(773\) coprime pairs \(1\le p<q\le50\) and \(52{,}813\) factor-image enumerations, including lengths beyond the period. The recorded output is in `check_output.txt`. A second independent script `boundary_check.py` enumerates rational rotation cells directly and verifies the required lexicographic monotonicity and all 48,807 boundary-identification decisions; its output is in `boundary_output.txt`. All integer operations are exact. This finite check tests instances; the proof above establishes the theorem for arbitrary coprime parameters and every length.

## Relationship to prior work
Defant and Kravitz introduced hare and tortoise stack-sorting maps on finite words. Campbell and Rampersad subsequently introduced tortoise complexity on factor languages and identified Sturmian generalizations as an open direction, proving results for paperfolding and Thue–Morse. Existing irrational-Sturmian one-pass formulas do not cover rational periodic Christoffel languages, for which the number of factors stops at \(q\) and the image count undergoes a distinct boundary/recovery regime; notably, the \(p=1\) family has a genuine one-step drop at \(n=q\). The present exact rational-phase formula follows instead by tracking repeat discontinuities at indices separated by \(q\).

## Limitations
Only one application of tortoise, periodic lower mechanical binary words and reduced rational slopes are covered. The theorem does not compute hare images or iterated tortoise images, nor assert a new result for irrational slopes. Indexing or unlocated prior work might contain an equivalent rational-slope classification; no independent scientific audit has been performed.

## References
1. C. Defant and N. Kravitz, *Stack-sorting for words*, Australasian Journal of Combinatorics **77** (2020), 51–68; initial arXiv preprint 1809.09158 (2018), https://arxiv.org/abs/1809.09158.
2. J. M. Campbell and N. Rampersad, *Subword enumeration up to stack-sorting equivalence*, arXiv:2604.25811v2 (2026), original submission 2026-04-28, https://arxiv.org/abs/2604.25811.
3. M. Lothaire, *Algebraic Combinatorics on Words*, Cambridge University Press (2002), standard background on mechanical, Sturmian, and Christoffel words.
