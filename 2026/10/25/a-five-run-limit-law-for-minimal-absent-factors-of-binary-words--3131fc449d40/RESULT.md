# A five-run limit law for minimal absent factors of binary words

## Finding
For a finite binary word, a **minimal absent factor** is a nonempty binary string that does not occur as a contiguous factor although each of its proper factors occurs. Every factor in this statement is contiguous, not a scattered subsequence.

Fix positive integers \(a,b,c,d,e\) and the five-run word
\[
w=0^a1^b0^c1^d0^e,\qquad n=a+b+c+d+e.
\]
Write \(N(w)\) for the number of its distinct minimal absent factors. Put \(T=\max\{c,\min(a,e)\}\) and \(M=\max\{b,d\}\). Then there is an integer \(R(w)\) such that
\[
N(w)=T+M-1-|\{b,d\}|+R(w),\qquad 0\le R(w)\le208.
\]
In particular, the error is absolutely bounded, independently of all five run lengths. The entire growing part consists of explicit three-run minimal absent factors.

Choose \((a,b,c,d,e)\) uniformly among all positive five-part compositions of \(n\). Define \(N_n=N(w)\). Let \((A,B,C,D,E)\) be a uniform point of the simplex \(\{(x_1,\ldots,x_5):x_i\ge0,\sum_i x_i=1\}\), equivalently Dirichlet\((1,1,1,1,1)\). Then
\[
\frac{N_n}{n}\;\xrightarrow{\mathrm{d}}\; Z=\max\{C,\min(A,E)\}+\max(B,D).
\]
All moments converge, and specifically
\[
\mathbb E[N_n]=\frac{8}{15}n+O(1).
\]
The displayed Dirichlet functional specifies the *full* nondegenerate limiting law, not merely its mean. Its two summands record the competing patterns \(101\) and \(010\).

## Assumptions and scope
The alphabet is exactly \(\{0,1\}\); all run lengths are positive. Minimality is by deletion of a single end character (equivalently, by occurrence of every proper contiguous factor). A uniformly sampled five-run word beginning with zero means a uniform positive composition of \(n\), not a uniform unrestricted binary word or an independent geometric-run model. Its sample size is \(\binom{n-1}{4}\), with \(n\ge5\). Complementing all bits leaves the count unchanged, so the starting symbol is immaterial.

The constants in the bounded remainder are intentionally conservative. The theorem neither asserts an exact finite-length formula for \(R(w)\) nor a rate of convergence for the law.

## Proof
**1. Exact type-three contribution.** Classify minimal absent factors by the five disjoint run-length-encoding types of Akagi–Okabe–Mieno–Nakashima–Inenaga [1, Section 2]. A type-three minimal absent word starts and ends with singleton runs and has one nonempty middle run; in the binary alphabet it is necessarily \(01^k0\) or \(10^k1\), with \(k\ge1\).

For \(01^k0\), the proper prefix \(01^k\) and proper suffix \(1^k0\) both occur precisely when \(1\le k\le M\). An entire \(01^k0\) occurs precisely when \(k=b\) or \(k=d\), because the one-run must be traversed from its preceding zero to its following zero. Therefore the number of type-three minimal absent factors of this orientation is exactly \(M-|\{b,d\}|\).

For \(10^k1\), the proper prefix \(10^k\) occurs exactly when \(k\le\max(c,e)\), and the proper suffix \(0^k1\) exactly when \(k\le\max(a,c)\). Both occur precisely when
\[
1\le k\le \min\{\max(c,e),\max(a,c)\}=T.
\]
The whole \(10^k1\) occurs exactly for \(k=c\), since the only zero-run between two one-runs has length \(c\). Because \(c\le T\), this gives exactly \(T-1\) type-three minimal absent words. Their union has cardinality \(T+M-1-|\{b,d\}|\), with no overlap between orientations.

**2. Uniform bound for all other types.** For run-length-encoded words with \(m\) maximal constant runs, [1, Lemmas 1, 2, 4 and 5, including the proof of Lemma 5] bounds non-type-three minimal absent words using the run structure. In the present setting \(m=5\), both letters are present, the types are disjoint, and the bounds specialize as follows: at most two type-one unary words, at most two type-two words, at most \(2m=10\) type-five words, and at most \([2(2m-3)]^2=196\) type-four words. The total is at most \(2+2+10+196=210\). Here \(01\) and \(10\) both occur, so there are in fact *no* type-two missing bigrams; removing that unused allowance gives \(R(w)\le208\). Every term is nonnegative, giving the claimed exact decomposition with \(0\le R\le208\). This step deliberately credits, and does not claim to rediscover, the established RLE upper-bound lemmas.

**3. Limit distribution.** A uniform positive five-part composition divided by \(n\) converges to the uniform distribution on the four-dimensional probability simplex. This follows directly by Riemann sums on the lattice \(\{(a,b,c,d,e)/n:a,b,c,d,e\ge1,\sum a=n\}\). The map
\[
F(x_1,x_2,x_3,x_4,x_5)=\max\{x_3,\min(x_1,x_5)\}+\max(x_2,x_4)
\]
is continuous and bounded on that simplex. By Step 2, \(|N_n/n-F(a/n,b/n,c/n,d/n,e/n)|\le(1+|\{b,d\}|+208)/n\le211/n\). The continuous mapping theorem therefore gives the stated distributional convergence. Uniform boundedness of \(N_n/n\) follows from the same estimate, hence every fixed moment converges.

**4. Mean.** If \(X=(A,B,C,D,E)\) has the uniform-simplex distribution, then for any \(j\) different designated coordinates and \(t\ge0\),
\[
\Pr(X_{i_1}>t,\ldots,X_{i_j}>t)=(1-jt)_+^4,
\]
where \(s_+=\max(s,0)\). Integrating this survival function gives
\[
\mathbb E\min(X_{i_1},\ldots,X_{i_j})=\frac{1}{5j}.
\]
Use \(\max(u,v)=u+v-\min(u,v)\) to obtain
\[
\begin{aligned}
\mathbb E\max(C,\min(A,E))&=\frac15+\frac1{10}-\frac1{15}=\frac7{30},\\
\mathbb E\max(B,D)&=\frac25-\frac1{10}=\frac3{10}.
\end{aligned}
\]
Their sum is \(\frac8{15}\). The bounded remainder in Step 2 and the \(O(n^{-1})\) Riemann-sum discrepancy for piecewise-linear functions on a fixed rational simplex yield \(\mathbb E N_n=\frac8{15}n+O(1)\). Alternatively, the error term follows by partitioning the simplex into finitely many rational polytopes on which \(F\) is affine; the lattice-sum over each such polytope differs from its volume integral by \(O(n^{-1})\) after normalization.

## Verification
The standalone `verify.py` constructs all distinct contiguous factors independently and, for every length-two-or-more candidate \(xuy\), checks exact minimal absence by the occurrence of \(xu\) and \(uy\) and nonoccurrence of \(xuy\). It verifies the explicit two bridge families and the conservative non-bridge bound for every five-tuple with run lengths from one through five, a total of \(5^5=3125\) cases. It also checks the rational moment identities independently using exact rational arithmetic. Run `python verify.py` using Python 3.9 or later; no third-party packages are required. These finite tests are error detection; the uniform infinite bound relies on the published proved RLE lemmas and the preceding derivation.

## Relationship to prior work
Akagi, Okabe, Mieno, Nakashima and Inenaga [1] introduced a general five-type decomposition and bounded all types except the unbounded middle bridge type in terms of the RLE size. Their results are essential to Step 2 and permit deterministic enumeration of the growing type-three family. The new assertion here is the limit distribution and its precise rational first moment for a *uniformly composed five-run binary word*, obtained by isolating its two competing bridge mechanisms; no general improvement of their deterministic algorithm is claimed.

Aurell, Innocenti and Zhou [2] studied statistical bulk/tail behavior of minimal absent words in genome-like sequences, not the positive-composition five-run ensemble. Fici, Restivo and Rizzo [3] studied minimal absent factors of circular words; their factor model differs from the linear five-run model used here. The exact run-model law stated above was not located in the inspected sources, but equivalence elsewhere remains possible.

## Limitations
Only five-run binary words under the specified uniform-composition distribution are addressed. The remainder bound \(208\) is not sharp. The complete distribution is specified by a Dirichlet functional rather than a simplified piecewise-polynomial density. Independent scientific review remains outstanding, and the literature search cannot establish universal priority. The statistical genome article [2] was accessible by abstract, not full text; no full-text noncoverage conclusion is drawn about it.

## References
[1] T. Akagi, K. Okabe, T. Mieno, Y. Nakashima and S. Inenaga, *Minimal Absent Words on Run-Length Encoded Strings*, arXiv:2202.13591, first submitted 2022-02-28. Full text inspected, Sections 1–5 and proof of Lemmas 4–5. https://arxiv.org/abs/2202.13591

[2] E. Aurell, N. Innocenti and H.-J. Zhou, *The Bulk and The Tail of Minimal Absent Words in Genome Sequences*, arXiv:1509.05188 (2015). Abstract inspected; full text unavailable during this comparison. https://arxiv.org/abs/1509.05188

[3] G. Fici, A. Restivo and L. Rizzo, *Minimal Forbidden Factors of Circular Words*, arXiv:1707.04450, first posted 2017-07. Accessible HTML inspected, introduction and main circular-word results. https://arxiv.org/abs/1707.04450
