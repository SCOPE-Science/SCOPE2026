# Exact arithmetic Fourier frame spectrum and sharp stability on primitive words

## Finding
For integers \(n,q\ge2\), let \(\mathcal P_{n,q}\) consist of words in \((\mathbb Z/q\mathbb Z)^n\) whose least positive cyclic-shift period is \(n\). Sample \(\mathcal P_{n,q}\) uniformly. Restrict the constant \(1\) and the first-coordinate Fourier band \(\chi_{a,j}(x)=\exp(2\pi i a x_j/q)\), for \(1\le a<q\) and \(j\in\mathbb Z/n\mathbb Z\), to this sample space. Their probability-normalized Gram matrix has eigenvalue \(1\) on the constant function and, for every \(a\ne0\), eigenvalues
\[
\boxed{\lambda_{n,q}(k)=\frac{\displaystyle\sum_{d\mid\gcd(n,k)}\mu(d)\,d\,q^{n/d}}{\displaystyle\sum_{d\mid n}\mu(d)q^{n/d}}},\qquad k\in\mathbb Z/n\mathbb Z.
\]
Here \(\gcd(n,0)=n\), and \(\mu\) is the number-theoretic Möbius function. For an exact spectral-level description, put \(R=\operatorname{rad}(n)\) and let \(S\) range over subsets of the distinct prime divisors of \(n\). Set
\[
B_n(S)=\sum_{d\mid\prod_{p\in S}p}\mu(d)dq^{n/d},\quad
P_{n,q}=\sum_{d\mid n}\mu(d)q^{n/d}.
\]
The eigenvalue \(B_n(S)/P_{n,q}\) appears with multiplicity
\[
(q-1)\frac nR\prod_{p\mid n,\,p\notin S}(p-1).
\]
Coincident levels have their multiplicities added. In particular the smallest eigenvalue is \(B_n(\{p:p\mid n\})/P_{n,q}\), attained at frequency \(k=0\), and the largest is \(q^n/P_{n,q}\), attained exactly when \(\gcd(n,k)=1\). The restricted Fourier family is linearly independent except when \((q,n)=(2,2)\), where it has exactly one dependency.

For all other \((q,n)\), the exact squared singular-value condition number is
\[
\boxed{\kappa_{n,q}^2=\frac{q^n}{\sum_{d\mid n}\mu(d)dq^{n/d}}\le4},
\]
with **equality only at** \((q,n)=(2,3)\). The constant eigenvalue \(1\) lies between the two displayed extreme eigenvalues, so including the constant does not alter this condition number. For fixed \(q\), the frame becomes asymptotically tight as \(n\to\infty\); the spectral deviation is bounded by a constant times \(n\log n\,q^{-n/2}\).

## Assumptions and scope
A cyclic-shift period \(t\) satisfies \(x_{j+t}=x_j\) at every position, with indices reduced modulo \(n\); “primitive” or “aperiodic” here means least cyclic-shift period exactly \(n\), **not** border-free/unbordered words. The alphabet is the cyclic group \(\mathbb Z/q\mathbb Z\); \(q\) need not be prime. Let \(N_{n,q}=|\mathcal P_{n,q}|=P_{n,q}>0\). The inner product is \(\langle f,g\rangle=N_{n,q}^{-1}\sum_{x\in\mathcal P_{n,q}} f(x)\overline{g(x)}\). The input family contains \(1+n(q-1)\) functions, all orthonormal in the ambient uniform product measure. Multiplicities in the theorem refer to this input family, not to cyclic necklaces quotienting by rotation; uniform rooted primitive words and uniform necklaces equipped with an independent uniformly random root give identical sampling laws. The singular-value condition number is the ratio of largest to smallest nonzero singular values only in the injective cases specified.

## Proof
**Period sieve and two-point moments.** For a divisor \(d\mid n\), let \(U_d\) be the words obtained by repeating a block of length \(n/d\) exactly \(d\) times. Thus \(|U_d|=q^{n/d}\), and pointwise inclusion–exclusion yields \(\mathbf1_{\mathcal P_{n,q}}=\sum_{d\mid n}\mu(d)\mathbf1_{U_d}\). Summing gives \(N_{n,q}=P_{n,q}\). For \(a,b\in\{1,\dots,q-1\}\) and positions \(i,j\), character orthogonality on every independent block symbol yields
\[
\sum_{x\in U_d}\chi_{a,i}(x)\overline{\chi_{b,j}(x)}
=\mathbf1_{a=b}\,\mathbf1_{n/d\mid(i-j)}q^{n/d}.
\]
For a nontrivial character, its individual mean vanishes on every \(U_d\), so it is orthogonal to the constant after sieving. Different nonzero character labels are orthogonal as well. Consequently the Gram matrix is the orthogonal direct sum of \(1\) and \(q-1\) identical \(n\)-by-\(n\) circulants, each with lag kernel
\[
C(h)=\frac1{P_{n,q}}\sum_{\substack{d\mid n\\n/d\mid h}}\mu(d)q^{n/d}.
\]
The cyclic Fourier transform of \(\mathbf1_{n/d\mid h}\) is \(d\mathbf1_{d\mid k}\). This proves the boxed eigenvalue formula. The prime-divisor set of \(\gcd(n,k)\) determines each eigenvalue; counting the residues \(k\) with that exact set gives \(n/R\prod_{p\notin S}(p-1)\), proving the stated multiplicities.

**The extremal-frequency ordering.** For any integer \(m\ge1\) and any set \(S\) of primes dividing \(m\), define \(B_m(S)=\sum_{d\mid\prod_{p\in S}p}\mu(d)dq^{m/d}\). Consider the words of length \(m\) avoiding all repetition events \(U_p\) for \(p\in S\), and put \(T(x)=\sum_{j=0}^{m-1}\exp(2\pi i x_j/q)\). Character orthogonality, period-event intersections, and inclusion–exclusion give the **nonnegative sum-of-squares identity**
\[
\boxed{mB_m(S)=\sum_{x\notin\bigcup_{p\in S}U_p}|T(x)|^2\ge0}.
\]
Indeed, on \(U_d\) the word repeats its independent \(m/d\)-symbol block \(d\) times; summing \(|T|^2\) over this set gives \(mdq^{m/d}\). Whenever \(p\mid m\) but \(p\notin S\), the Möbius sum splits as
\[
B_m(S)-B_m(S\cup\{p\})=pB_{m/p}(S)\ge0.
\]
Thus the spectral numerator decreases whenever additional prime divisors are imposed. It is largest at \(S=\varnothing\), with value \(q^n\), and smallest at the full prime set. The maximum is strict whenever \(S\ne\varnothing\): the first decrease on adjoining any prime is \(pq^{n/p}>0\). The nonnegative sum of squares is strictly positive whenever \(m\ge3\), because a word with one exceptional letter is primitive and has \(|T|\ge m-2>0\). At \(m=2\), positivity holds for \(q\ge3\) using the two distinct symbols \(0,1\), whose character values do not sum to zero, and also for \(S=\varnothing\). Exactly at \((m,q,S)=(2,2,\{2\})\), the sum vanishes. Therefore the full Gram is injective precisely outside \((n,q)=(2,2)\), with one zero Fourier level at that exceptional pair.

**Uniform sharp bound.** The sum-of-squares identity and a union bound applied to the nonnegative summands imply
\[
B_n(\{p:p\mid n\})\ge q^n-\sum_{p\mid n}p q^{n/p}.
\]
For \(n\ge3\), write \(E(n,q)=\sum_{p\mid n}p q^{-n(1-1/p)}\). It decreases in \(q\), so \(E(n,q)\le E(n,2)\). If \(n\) is prime, \(E(n,2)=n2^{1-n}\le3/4\), with equality only at \(n=3\). For composite \(n=4,6,8\), the values are respectively \(1/2,7/16,1/8\). For every composite \(n\ge9\), each prime divisor is at most \(n/2\), and their number at most \(\log_2 n\); hence
\[
E(n,2)\le\frac{n\log_2n}{2^{n/2+1}}<\frac34.
\]
The upper bound on the right is decreasing for real \(n\ge8\), and equals \(3/4\) at \(n=8\). Thus \(B_n\ge q^n/4\), with the only possible equality at \((n,q)=(3,2)\). There \(B_3=2\) and \(q^n=8\), so equality really holds. For \(n=2\) and \(q\ge3\), the denominator is \(q^2-2q\), and \(\kappa^2=q/(q-2)\le3\). Finally the constant eigenvalue lies between the nonconstant extremes: the trace of each circulant is \(n\) since \(C(0)=1\), so the average nonconstant eigenvalue equals \(1\). This completes the sharp condition-number proof.

**Asymptotic tightness.** The same divisor bound gives \(0\le 1-B_n/q^n\le E(n,q)\le(n\log_2 n/2)q^{-n/2}\) for composite \(n\), with the prime case even smaller. The lower and upper Gram levels therefore both converge to \(1\), yielding the stated estimate for the spectral deviation and condition number as \(n\to\infty\) with \(q\) fixed.

## Verification
The standalone `checker.py` independently enumerates small primitive-word spaces, counts equal-letter pairs to obtain exact cross-moments, and compares exact characteristic polynomials with the predicted divisor-indexed spectrum. Successful replay produced 24 complete enumerated parameter instances, 115 exact pair-moment comparisons, 24 exact spectral-polynomial comparisons, and 1,071 larger arithmetic parameter checks. Run `python checker.py` from this directory (Python 3 and SymPy). The finite tests corroborate but do not replace the period-sieve, positivity, and global-inequality proofs.

## Relationship to prior work
Murray's *Möbius Polynomials* (arXiv:1312.3848v1) proves the counting formula \(P_{n,q}\) for primitive cyclic words. The present result uses that established count but also computes every pairwise coordinate-character moment, the full spatial Gram spectrum, exact multiplicities and the sharp uniform conditioning constant, none of which are asserted there. Duzhin and Pasechnik (arXiv:1304.2563v1) study group actions on aperiodic binary necklaces, a different invariant. The paper by Rukhin and Volkovich uses “aperiodic words” to mean **unbordered patterns** and studies frequencies of occurrences in an independent random text; that different notion and sampling law cannot imply this theorem. Previously published harmonic-sampling classifications for fixed Hamming shells work on a different support and have a forced shell-constraint kernel, whereas the primitive-word sample is injective almost everywhere. Fourier sampling on **unit residues** modulo a cyclic order is likewise different from sampling coordinate characters on primitive words.

## Limitations
No classification is claimed for higher-degree Fourier bands, nonuniform distributions on primitive words, or alphabets with additional coordinate-dependent constraints. Exact spectral coincidences beyond the stated multiplicity-addition rule are not classified. Historical duplication risk remains from literature expressing primitive-necklace autocorrelations or their Fourier transforms in equivalent notation; the inspected sources did not establish the complete theorem, but the literature survey is not an exhaustive novelty certificate. The independent mathematical audit has not been performed.

## References
1. Will Murray, *Möbius Polynomials*, arXiv:1312.3848v1, submitted 2013-12-13, Sections 1 and 3, https://arxiv.org/html/1312.3848v1.
2. S. Duzhin and D. Pasechnik, *Automorphisms of necklaces and sandpile groups*, arXiv:1304.2563v1, submitted 2013-04-09, https://arxiv.org/abs/1304.2563.
3. A. L. Rukhin and Z. Volkovich, *Testing randomness via aperiodic words*, J. Statist. Comput. Simulation 78 (2008), 1131–1142, https://www.nist.gov/publications/testing-randomness-aperiodic-words (terminology and different covariance problem).
4. *Exact q-ary Hamming-shell Fourier concentration and the arithmetic tightness criterion*, publicly available mathematical research note, https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-exact-q-ary-hamming-shell-fourier-concentration-and-the-arithmet--89a15e26e594.
5. *Consecutive Fourier bands minimize primitive-row frame potential at every modulus*, publicly available mathematical research note, https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-consecutive-fourier-bands-minimize-primitive-row-frame-potential--d824c1a982ba.
