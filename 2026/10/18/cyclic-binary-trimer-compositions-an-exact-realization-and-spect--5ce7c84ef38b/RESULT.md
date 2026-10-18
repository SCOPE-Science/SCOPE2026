# Cyclic binary trimer compositions: an exact realization and spectrum theorem

## Finding

For every integer \(n\geq1\), let \(w=w_0\cdots w_{n-1}\) be a binary word, with indices interpreted modulo \(n\). For \(j\in\{0,1,2,3\}\), define \(c_j(w)\) to be the number of positions \(i\in\{0,\ldots,n-1\}\) for which \(w_i+w_{i+1}+w_{i+2}=j\). The *cyclic trimer-composition spectrum* is \(C(w)=(c_0,c_1,c_2,c_3)\), which retains multiplicities of the four unordered three-symbol compositions, but not the ordering within individual windows. Repeated positions in windows are counted in the natural periodic extension for \(n=1,2\).

**Exact realization theorem.** A nonnegative integer quadruple \((a,p,q,d)\) of positive total \(n=a+p+q+d\) occurs as \(C(w)\) if and only if one of the following disjoint alternatives holds:

1. \(p=q=0\) and \((a,d)\) is \((n,0)\) or \((0,n)\).
2. \(p+q>0\), \(p\equiv q\pmod 3\), \(a>0\Longrightarrow p\geq2\), and \(d>0\Longrightarrow q\geq2\).

Let \(N(n)=\#\{C(w):w\in\{0,1\}^n\}\). Then the complete ordinary generating function is

\[
\boxed{\sum_{n\geq1}N(n)z^n=\frac{z(2-3z+z^2-2z^3+5z^4-2z^5-z^6+z^7)}{(1-z)^4(1+z+z^2)}.}
\]

In particular, \(N(1)=2\), \(N(2)=3\), and for every \(n\geq3\),

\[
\boxed{N(n)=\frac{n^3-6n^2+39n-26+8\epsilon_n}{18},\qquad
\epsilon_n=\begin{cases}1&n\equiv0\pmod3,\\-1&n\equiv1\pmod3,\\0&n\equiv2\pmod3.\end{cases}}
\]

Consequently \(N(n)=n^3/18+O(n^2)\), the exact eventual quasipolynomial period is three, and

\[
\boxed{\lim_{n\to\infty}\frac{N(n)}{\binom{n+3}{3}}=\frac13.}
\]

The maximum number of length-\(n\) binary words having pairwise different cyclic trimer-composition spectra is exactly \(N(n)\): one representative from each nonempty observation class is optimal.

## Assumptions and scope

The alphabet is the two labeled symbols \(0,1\); the observation is a *cyclic* multiset of **exactly** length-three substring compositions, and contains neither ordered three-grams nor shorter-factor counts. Every starting position contributes one observation, including on periodic words and at \(n=1,2\). Distinct output quadruples are counted, not distinct input necklaces. There are no stochastic hypotheses in the realization or counting statements.

## Proof

**1. Cyclic run decomposition.** For a word containing both symbols, let \(r\geq1\) be the number of cyclic zero-runs, also the number of one-runs. Write \(s_0,s_1\in\{0,\ldots,r\}\) for the numbers of zero-runs and one-runs of length one. An all-zero trimer is centered inside a zero-run of length at least three; similarly for all-one trimers. Directly inspecting run boundaries, the two mixed-trimer counts satisfy

\[
p=2(r-s_0)+s_1,\qquad q=2(r-s_1)+s_0.
\]

Indeed, each zero-run of length at least two provides one \(100\) and one \(001\) trimer, and each singleton one-run provides one \(010\) trimer; the other formula exchanges zeros and ones. These identities remain valid for the alternating length-two word because its length-three windows are taken cyclically. The all-zero and all-one counts are

\[
a=\sum_{\text{zero-runs }R}(\lvert R\rvert-2)_+,\qquad d=\sum_{\text{one-runs }R}(\lvert R\rvert-2)_+.
\]

Subtracting the mixed-trimer identities gives \(p-q=3(s_1-s_0)\). If \(a>0\), some zero-run has length at least three and contributes two weight-one trimers, so \(p\geq2\). Similarly \(d>0\) forces \(q\geq2\). The asserted conditions are therefore necessary. If a word uses only one symbol, its profile is one of the two pure profiles in alternative 1.

**2. Constructing every permitted profile.** Suppose \(p+q>0\) and the conditions in alternative 2 hold. Define the positive integers

\[
A=\frac{2p+q}{3},\qquad B=\frac{p+2q}{3},\qquad
r=\left\lceil\frac{\max(A,B)}2\right\rceil.
\]

Congruence makes \(A,B\) integers. The identities \(2A-B=p\geq0\) and \(2B-A=q\geq0\) imply \(\max(A,B)\leq2\min(A,B)\), hence \(r\leq A,B\). Set \(s_0=2r-A\) and \(s_1=2r-B\); these are integers between zero and \(r\). Moreover \(a>0\) implies \(r\leq A-1\): if \(B>A\), this follows from \(2A-B=p\geq2\); otherwise \(A\geq2\) follows from \(p\geq2\) and \(p\equiv q\pmod3\), and then \(\lceil A/2\rceil\leq A-1\). Symmetrically, \(d>0\) implies \(r\leq B-1\).

Choose \(s_0\) singleton zero-runs and \(r-s_0=A-r\) zero-runs initially of length two. If \(a>0\), the latter number is positive, so distribute \(a\) extra zeros arbitrarily among those nonsingleton runs; if \(a=0\), add nothing. Do the same with one-runs using \(s_1\), \(r-s_1\), and \(d\). Interleave the resulting \(r\) zero-runs and \(r\) one-runs cyclically. The identities in step 1 give precisely \((a,p,q,d)\). Its length is \(A+B+a+d=p+q+a+d=n\). This proves sufficiency and the complete realization theorem, including all boundary cases.

**3. Counting the feasible profiles.** For a fixed mixed count \(p\), the number of possibilities for \(a\), enumerated by its contribution to length, is \(K_p(z)=1\) for \(p\in\{0,1\}\), and \(K_p(z)=1/(1-z)\) for \(p\geq2\). The same applies to \(q,d\). Thus

\[
\sum_{n\geq1}N(n)z^n=\frac{2z}{1-z}
+\sum_{\substack{p,q\geq0,\ p\equiv q\ (\mathrm{mod}\ 3)\\ p+q>0}}
 z^{p+q}K_p(z)K_q(z).
\]

To evaluate this sum use

\[
S(z)=\sum_{p\equiv q\ (\mathrm{mod}\ 3)}z^{p+q}
=\frac{1+z^2+z^4}{(1-z^3)^2},\qquad
T(z)=\sum_{\substack{p\leq1\\p\equiv q\ (\mathrm{mod}\ 3)}}z^{p+q}
=\frac{1+z^2}{1-z^3}.
\]

Since \(K_p=(1-z)^{-1}(1-z\mathbf{1}_{p\leq1})\), summing over the three common residue classes, and removing the \((p,q)=(0,0)\) term, yields

\[
\sum_{n\geq1}N(n)z^n=\frac{2z}{1-z}-1+
\frac{S(z)-2zT(z)+z^2(1+z^2)}{(1-z)^2}.
\]

Elementary rational simplification gives the stated generating function. The partial-fraction identity is

\[
\frac{2z}{1-z}-1+\frac{S(z)-2zT(z)+z^2(1+z^2)}{(1-z)^2}
=1+2z+z^2+\frac{4}{9(1+z+z^2)}
-\frac4{1-z}+\frac{32}{9(1-z)^2}-\frac4{3(1-z)^3}+\frac1{3(1-z)^4}.
\]

The series \(1/(1+z+z^2)=(1-z)/(1-z^3)\) has coefficients periodically \(1,-1,0\). Extracting coefficients proves both initial values and the exact quasipolynomial. The nonzero residue-class term proves that its least eventual period is exactly three. The pole at \(z=1\) has leading term \((3(1-z)^4)^{-1}\), which gives \(N(n)=n^3/18+O(n^2)\). The total number of arbitrary nonnegative four-entry histograms with sum \(n\) is \(\binom{n+3}{3}\), giving the fraction \(1/3\). Selecting one representative of each attainable profile and applying the pigeonhole principle proves the zero-error code assertion.

## Verification

A standalone standard-library Python checker, `verify.py`, provides two logically different finite tests: direct enumeration of all binary words for \(1\leq n\leq16\), and an independent de Bruijn-state dynamic program enumerating cyclic triple windows for \(1\leq n\leq48\). Both compare complete *sets* of attainable quadruples with the realization conditions, then compare their cardinalities with exact coefficient extraction. The tested cardinalities for lengths \(1\) through \(18\) are \(2,3,4,5,8,12,16,23,32,42,56,73,92,116,144,175,212,254\). These are finite checks; the universal claims follow from steps 1–3 of the proof.

Reproduce by running `python3 verify.py` in the directory containing the embedded files. No nonstandard Python packages are required.

## Relationship to prior work

Ye and Elishco [1] introduce length-limited **linear** substring-composition observations and develop constructive reconstruction codes, but their Section VIII does not give a cyclic fixed-trimer composition realizability classification or an enumeration of its image. Gupta and Mahdavifar [2] address the full, **linear** multiset of substring compositions and reconstruction algorithms, likewise not this observation space. Ota and Manada [3] study reconstruction of a circular binary word from **ordered** substring frequencies and minimal absent words; their criterion concerns uniquely reconstructing a particular word and assumes primitive circular input, not counting the image of the orientation-forgetting length-three composition map over all circular words. The present result distinguishes these models rather than treating a reconstruction theorem as an enumeration theorem.

## Limitations

The theorem is for binary alphabets, cyclic windows of exactly length three, and noiseless observations. It does not count the sizes of individual fibers, give efficient encoders selecting representatives, or generalize the four-coordinate formula to longer windows or larger alphabets. The independent dynamic-program and exhaustive checks are finite corroborations, not a substitute for the combinatorial proof. An equivalent enumeration outside the inspected literature remains possible; no external independent validation has been performed.

## References

[1] Z. Ye and O. Elishco, *Reconstruction of a Single String from a Part of its Composition Multiset*, arXiv:2208.14963 (first public version, 2022-08-31), https://arxiv.org/abs/2208.14963. Relevant material: Section VIII.

[2] U. Gupta and H. Mahdavifar, *A New Algebraic Approach for String Reconstruction from Substring Compositions*, arXiv:2201.09955 (2022), https://arxiv.org/abs/2201.09955. Relevant material: Sections I–IV.

[3] T. Ota and A. Manada, *A Reconstruction of Circular Binary String Using Substrings and Minimal Absent Words*, IEICE Transactions on Fundamentals E107-A (2024), 409–416, DOI:10.1587/transfun.2023TAP0015, https://doi.org/10.1587/transfun.2023TAP0015. Relevant material: Sections 2–5.
