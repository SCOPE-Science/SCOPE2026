# Weight-resolved cyclic three-gram capacity with a forbidden triple

## Finding

Let \(n\ge1\), let \(0\le w\le n\), and observe an oriented cyclic binary word through the **multiset with multiplicities** of its \(n\) cyclic contiguous length-three factors. Restrict the source to words with exactly \(w\) occurrences of \(1\) and **no cyclic occurrence of \(111\)**. Denote by \(C_{n,w}\) the number of distinct observable three-gram profiles. Then \(C_{n,0}=1\) and for \(w\ge1\),

\[
 C_{n,w}=\sum_{y=0}^{\lfloor w/2\rfloor}\left(\max\{0,\min(w-y,n-2w+y)\}+\mathbf 1_{\{n=2w-y\}}\right).
\]

These values are the exact largest zero-error code sizes at fixed length and weight when a received output consists solely of the unordered, multiplicity-preserving collection of oriented cyclic triples. An explicit representative can be constructed for every realizable profile.

The complete bivariate generating function, with \(G(z,u)=\sum_{n\ge1}\sum_{w=0}^n C_{n,w}z^nu^w\), is

\[
G(z,u)=\frac z{1-z}+\frac1{(1-uz^2)(1-u^2z^3)}-1
+\frac z{(1-z)^2}\left(\frac1{(1-uz^2)(1-u^2z^3)}-\frac1{(1-uz^3)(1-u^2z^4)}\right).
\]

For every fixed \(w\ge2\), a saturation transition occurs **exactly** at \(n=3w\): for all \(n\ge3w\),

\[
 C_{n,w}=\bigl(\lfloor w/2\rfloor+1\bigr)w-\frac{\lfloor w/2\rfloor(\lfloor w/2\rfloor+1)}2,
\]

whereas at \(n=3w-1\) the count is smaller by exactly one. For \(w=1\) the plateau is attained already at \(n=2\).

If \(w_n=\lfloor\alpha n\rfloor\) with \(0\le\alpha\le1\), then \(C_{n,w_n}=n^2f(\alpha)+O(n)\), where

\[
f(\alpha)=\begin{cases}
3\alpha^2/8,&0\le\alpha\le1/3,\\
(-15\alpha^2+12\alpha-2)/8,&1/3\le\alpha\le1/2,\\
(2-3\alpha)^2/8,&1/2\le\alpha\le2/3,\\
0,&2/3\le\alpha\le1.
\end{cases}
\]

Summing over weights, \(C_n=\sum_w C_{n,w}\) has generating function

\[
\sum_{n\ge1}C_nz^n=\frac z{1-z}+\frac1{(1-z^2)(1-z^3)}-1+\frac{z^3}{(1-z)^2(1-z^3)(1-z^4)}.
\]

It is a cubic quasipolynomial of **exact least period \(12\)**, with \(C_n=n^3/72+O(n^2)\).

## Assumptions and scope

A cyclic word is indexed modulo \(n\). The length-three factors start at all \(n\) positions, even if \(n=1\) or \(n=2\), in which case their indices wrap and repeat. The forbidden triple \(111\) is interpreted with the same cyclic indexing. Words identified by rotation give the same profile. Reversal is **not** imposed as an equivalence, and triples such as \(001\) and \(100\) are formally distinct coordinates (although their counts are forced equal here). The output has no positional labels, but each ordered triple and its multiplicity is observed exactly; no read noise, deletion or erasure is allowed. Binary weight counts occurrences of symbol \(1\).

## Proof

**Run-parameter bijection.** For a mixed cyclic word (both symbols occur), cyclically decompose it into alternating positive one-runs and zero-runs. Since \(111\) is forbidden, every one-run has length one or two. Let \(a\) be the number of singleton one-runs, \(y\) the number of double one-runs, and \(t=a+y\) the number of both sorts of runs. Among the \(t\) zero-runs, let \(x\) have length at least two and \(t-x\) have length one. Set \(b\) equal to the sum over the long zero-runs of their lengths minus two; hence \(b\ge0\), and necessarily \(x=0\Rightarrow b=0\).

In lexicographic coordinate order \((000,001,010,011,100,101,110,111)\), the observed profile is exactly

\[
 (b,x,a,y,x,t-x,y,0).
\]

Indeed, each long zero-run contributes one \(001\), one \(100\), and its excess length to \(000\). Each singleton one-run contributes one \(010\), each double one-run contributes one \(011\) and one \(110\), and every zero-run of length one contributes one \(101\). Thus \(a,y,x,b\) can be recovered uniquely from the observation.

Conversely, take any integers \(a,y\ge0\) with \(t=a+y\ge1\), \(0\le x\le t\), and \(b\ge0\), subject to \(x=0\Rightarrow b=0\). Form \(y\) one-runs of length two and \(a\) of length one in arbitrary cyclic order; give \(x\) zero-runs initial length two and the rest length one; if \(x>0\), add all \(b\) extra zeros to the first long zero-run. Alternating these runs constructs a cyclic word with precisely that profile and no \(111\). Consequently the parametrization is necessary and sufficient; two different quadruples cannot give the same profile. The only non-mixed allowable word is the all-zero word, which gives one further profile at each positive length and weight zero. The all-one cyclic words are forbidden, including at length one or two.

**Fixed weight.** For mixed words,

\[
w=a+2y,\qquad t=w-y,\qquad n=2w-y+x+b.
\]

Hence \(0\le y\le\lfloor w/2\rfloor\). If \(x=0\), then \(b=0\), so this contributes one profile exactly when \(n=2w-y\). Otherwise \(x\) can be any integer from \(1\) through \(\min(w-y,n-2w+y)\), with nonnegative \(b\) determined. Summing gives the coefficient formula. Choosing a single codeword for each profile attains the stated maximum, whereas no two codewords with identical observations can both belong to a zero-error code.

**Generating function.** The contributions from the all-zero word are \(z/(1-z)\). For mixed words with \(x=0\), the weight and length sums are \(\sum_{a,y\ge0;(a,y)\ne(0,0)}(uz^2)^a(u^2z^3)^y\). For \(x>0\), write \(t=a+y\), sum \(z^x\) from \(x=1\) to \(t\), and independently sum \(z^b\) over nonnegative \(b\). Using \(\sum_{x=1}^t z^x=z(1-z^t)/(1-z)\) proves the displayed bivariate rational function. Setting \(u=1\), then simplifying the difference of the two bracket terms, gives the univariate generating function.

**Saturation and density.** If \(n\ge3w\), then for every \(0\le y\le\lfloor w/2\rfloor\) one has \(n-2w+y\ge w-y\), so the number of positive choices of \(x\) is \(w-y\), with no \(x=0\) exception. Their sum is the displayed plateau. At \(n=3w-1\), only \(y=0\) loses one choice; for \(w\ge2\), no exception replaces it. To establish the earliest plateau, observe that for \(n<3w\) the \(y=0\) term falls short of its plateau value (by at least one), and at \(n=2w\) the one boundary contribution cannot compensate when \(w\ge2\); all other summands are bounded above by their plateau counts. For \(w=1\), direct substitution gives the stated exception.

For \(\alpha=w/n\) and \(\beta=y/n\), the positive-choice summand is \(n\max\{0,\min(\alpha-\beta,1-2\alpha+\beta)\}\). The nonzero range is \(\max(0,2\alpha-1)\le\beta\le\alpha/2\). Summing on a mesh of size \(1/n\) and noting that the indicator contributions total at most \(O(n)\) gives a uniform \(O(n)\) Riemann-sum error. Integrating the two intersecting affine branches, with their transition at \(\beta=(3\alpha-1)/2\), gives exactly the stated three nonzero quadratic pieces.

Finally the univariate rational generating function has a fourth-order pole at \(z=1\), with leading principal part \(1/[12(1-z)^4]\); hence \(C_n=n^3/72+O(n^2)\). Its other poles have orders dividing four or three, so the coefficient sequence is a quasipolynomial of period dividing twelve. The primitive fourth-root poles are noncancelling because only the last summand is singular there. At a primitive cube root \(\zeta\), the coefficient of \((1-z^3)^{-1}\) equals \(1/(1-\zeta^2)+1/(1-\zeta)^3\); the two terms have unequal absolute values \(1/\sqrt3\) and \(1/(3\sqrt3)\), and therefore cannot cancel. Thus any coefficient quasipolynomial period is divisible by both three and four, proving exact least period twelve.

## Verification

Run `python3 verify.py` with Python 3.9 or later. The verifier independently enumerates all cyclic binary indexed words of lengths \(1\) through \(16\), groups profiles by length and weight, and compares every group cardinality with the closed formula. It also constructs a realizing word for each enumerated parameter profile through length \(70\), checks the eight observed coordinates, and compares the formula with a direct truncation of the bivariate rational series. It checks the exact saturation boundary at weights \(2\) through \(39\). A successful replay emits `VERIFY_OK`. These finite computations corroborate, but do not replace, the all-length proof above.

## Relationship to prior work

Kiah, Puleo and Milenkovic [1] study DNA sequence profile codes through restricted de Bruijn graphs and Ehrhart theory. Their general quasipolynomial/asymptotic theorems motivate considering profile classes, but do not explicitly determine this forbidden-triple, weight-resolved **cyclic** coefficient formula. Their discussion states that specialized forbidden-triple families are outside the analyzed scope. Chee and coauthors [2] study maximal run-length-limited de Bruijn sequences and enumerate legal words and necklaces, which are different from distinct multiplicity-profile classes. Shen and coauthors [3] count forbidden-factor-avoiding **source words** using the cluster method, not their images under a three-gram-multiset observation. No equivalence with the present explicit weight-resolved profile result was established by these comparisons.

## Limitations

The result assumes a complete exact spectrum of cyclic oriented length-three factors; it does not give a reconstruction algorithm for the original word, individual fiber sizes, an error-correcting distance, noisy sequencing capacity, or conclusions for general forbidden patterns, alphabets, or read lengths. The observation classes can contain many distinct necklaces, so the code size is achieved only by choosing one representative per class. Relevant general constrained Markov-type enumerations could conceivably contain the present formula implicitly; an exhaustive historical uniqueness claim is not made. The verifier is finite, whereas the proof establishes all lengths and weights.

## References

1. H. M. Kiah, G. J. Puleo, and O. Milenkovic, *Codes for DNA Sequence Profiles*, arXiv:1502.00517 (first public 2015-02-02), https://arxiv.org/html/1502.00517v1. See Sections 2-4, particularly the restricted de Bruijn/Ehrhart treatment and discussion of excluded specialized forbidden substrings.
2. Y. M. Chee, T. Etzion, T. L. Nguyen, D. H. Ta, V. D. Tran, and V. K. Vu, *Maximum Length RLL Sequences in de Bruijn Graph*, arXiv:2403.01454 (first public 2024-03-03), https://arxiv.org/abs/2403.01454. See Sections 1 and 4 for the distinct-window and necklace-count objectives.
3. Y. Shen, C. Shangguan, Z. Lin, and G. Ge, *Constrained coding upper bounds via Goulden-Jackson cluster theorem*, arXiv:2407.16449 (first public 2024-07-23), https://arxiv.org/abs/2407.16449. See Section 1 and the definition of the full constrained source-word count.
