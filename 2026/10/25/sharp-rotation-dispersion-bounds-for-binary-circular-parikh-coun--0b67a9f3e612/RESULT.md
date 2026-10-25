# Sharp rotation-dispersion bounds for binary circular Parikh counts

## Finding
For any integers \(a,b\ge 1\), let \(n=a+b\), \(d=\gcd(a,b)\), and \(N=n/d\). For a binary word \(w\) of length \(n\) with exactly \(a\) zeros and \(b\) ones, let \(w^{(k)}\) be its cyclic left rotation by \(k\) positions, where \(0\le k<n\). Let \(F_k\) count the *scattered* occurrences of \(01\) in \(w^{(k)}\), that is, the index pairs \(i<j\) with the letters \(0,1\) respectively. The rotation profile has mean \(\overline F=ab/2\). Its population variance
\[
V(w)=\frac1n\sum_{k=0}^{n-1}\left(F_k-\frac{ab}{2}\right)^2
\]
satisfies the sharp two-sided bounds
\[
\boxed{\frac{d^2(N^2-1)}{12}\ \le\ V(w)\ \le\ \frac{ab(ab+2)}{12}}.
\]
Equality on the left holds **if and only if** \(w\) is *circularly balanced*: among all cyclic factors of any fixed length, the numbers of ones differ by at most one. Equivalently, its circular word is a power of a primitive Christoffel word, with exactly \(d\) repeats; all left minimizers lie in the same rotation orbit. Equality on the right holds **if and only if** the ones occupy a single circular interval, equivalently \(w\) is a rotation of \(0^a1^b\). These criteria include \(a=1\) or \(b=1\), when the bounds coincide. Thus the second moment, unlike the first, distinguishes the maximally balanced and the maximally clustered configurations.

## Assumptions and scope
All words are indexed from \(0\), and the circular factors include wraparound factors of lengths \(1\) through \(n\). A scattered occurrence of \(01\) is an ordered pair of distinct positions in a *linear* representative, not an adjacent occurrence and not an equivalence class of circular pairs. Every positional rotation is used in the mean and variance, including repeated representatives for nonprimitive words. The variance is the population variance with divisor \(n\), not the sample variance with divisor \(n-1\). Nothing is asserted for higher alphabets or other scattered patterns.

## Proof
**1. Cyclic increments and mean.** Write \(x_k\in\{0,1\}\) for the letter at position \(k\) of \(w\), extended periodically, and let \(F_k\) be as above. Moving the first letter to the end removes exactly \(b\) scattered \(01\) pairs if that letter is \(0\), or adds exactly \(a\) if it is \(1\). Hence
\[
F_{k+1}-F_k=nx_k-b\qquad(k\bmod n).
\]
To compute the mean directly, let \(J=\sum_{j:x_j=1}j\), with positions indexed from \(0\). Each one at position \(j\) has \(j\) earlier letters, of which exactly its rank among the ones are also ones. Hence \(F_0=J-b(b-1)/2\). Meanwhile, \(\sum_{k=0}^{n-1}\sum_{i<k}x_i=b(n-1)-J\). Summing the increment formula gives \(\sum_kF_k=nF_0+n[b(n-1)-J]-bn(n-1)/2=nab/2\). Therefore \(\overline F=ab/2\).

**2. A quadratic identity.** For each position \(i\), define the length-\(n\) vector \(h^{(i)}\) by
\[
h^{(i)}_k=n\mathbf1_{i<k}-k\qquad(0\le k<n).
\]
The previous increment formula implies \(F_k-F_0=\sum_{i:x_i=1}h^{(i)}_k\). The \(n\) values of \(h^{(i)}\) are \(n\) consecutive integers, so \(\operatorname{Var}(h^{(i)})=(n^2-1)/12\). For \(i<j\), the difference \(h^{(i)}-h^{(j)}\) is \(n\) at precisely \(j-i\) positions and \(0\) elsewhere. Its variance is \((j-i)(n-j+i)\). The elementary covariance identity \(2\operatorname{Cov}(U,V)=\operatorname{Var}(U)+\operatorname{Var}(V)-\operatorname{Var}(U-V)\) consequently yields
\[
\boxed{V(w)=\frac{b^2(n^2-1)}{12}-\sum_{\substack{i<j\\x_i=x_j=1}}(j-i)(n-j+i).}\tag{1}
\]
In particular, the pairwise term is independent of where the linear representative starts because the product of complementary circular distances is unchanged.

**3. Sharp upper bound and rigidity.** List the \(b\) positions containing ones in circular order. Let \(g_1,\ldots,g_b\) be the positive cyclic gaps between consecutive such positions. Their sum is \(n\). For \(1\le i<j\le b\), write \(s_{ij}=g_i+\cdots+g_{j-1}\). The pair sum in (1) becomes
\[
\Phi(g_1,\ldots,g_b)=\sum_{i<j}s_{ij}(n-s_{ij}).
\]
This is a concave quadratic function of the real gaps on the simplex \(g_i\ge1\), \(\sum g_i=n\). If \(b\ge2\), it is *strictly* concave on that simplex: for every nonzero feasible tangent vector \(v\) its second directional derivative is \(-2\sum_{i<j}(v_i+\cdots+v_{j-1})^2<0\), since vanishing of all partial sums first forces \(v_1=\cdots=v_{b-1}=0\), and then \(v_b=0\). Thus its minimum occurs only at vertices of the simplex. Every vertex has one gap \(n-b+1=a+1\) and all others equal to \(1\), precisely the configuration with all ones consecutive around the circle. For \(b=1\) that conclusion is automatic. For \(w=0^a1^b\), the counts along successive rotations are the multiset
\[
\{ab,(a-1)b,\ldots,b,0,a,2a,\ldots,(b-1)a\}.
\]
Summing their squares and subtracting \((ab/2)^2\) gives \(V(w)=ab(ab+2)/12\). This proves the upper bound and its equality characterization.

**4. Sharp lower bound.** The increment equation also gives the modular congruence \(F_k\equiv F_0+ka\pmod n\). Since \(d=\gcd(a,n)\), every \(F_k\) is congruent to \(F_0\pmod d\). Partition the indices \(0,\ldots,n-1\) into the \(d\) consecutive blocks of length \(N=n/d\). Within each block the residues \(F_k\pmod n\) are pairwise distinct: if \(a(k-\ell)\) is divisible by \(n\), then \(N\mid(k-\ell)\). Therefore the \(N\) integers in each block, after subtracting \(F_0\) and dividing by \(d\), are distinct. Any \(N\) distinct integers have population variance at least \((N^2-1)/12\), with equality exactly for \(N\) consecutive integers: when their sorted values are \(y_1<\cdots<y_N\), the pairwise-variance identity and \(y_j-y_i\ge j-i\) give the lower bound and its equality case. Consequently each block has variance at least \(d^2(N^2-1)/12\). The law of total variance over the \(d\) equal-sized blocks proves the claimed overall lower bound. Equality forces all blocks to have the same mean and the same \(N\)-term consecutive arithmetic progression with difference \(d\). Equivalently, the entire rotation profile takes each of \(N\) consecutive \(d\)-spaced values exactly \(d\) times, and its range is \(n-d\).

For any two rotations \(k\) and \(k+\ell\), the increment equation gives
\[
F_{k+\ell}-F_k=n\,t_{k,\ell}-b\ell,
\]
where \(t_{k,\ell}\) is the number of ones in the corresponding circular factor of length \(\ell\). If equality in the lower bound holds, the range of the profile is \(n-d<n\). Thus \(\lvert t_{k,\ell}-b\ell/n\rvert<1\), and integrality forces every length-\(\ell\) circular factor to have either \(\lfloor b\ell/n\rfloor\) or \(\lceil b\ell/n\rceil\) ones. This is exactly circular balance.

Conversely, circular balance forces every length-\(\ell\) factor count into those two adjacent integers (their average over all starts is \(b\ell/n\)). Thus \(\lvert F_{k+\ell}-F_k\rvert<n\) for any two rotations, and all these differences are multiples of \(d\). Hence the profile range is at most \(n-d\). Since each consecutive block of \(N\) rotations has \(N\) distinct residues modulo \(n\) and all values lie on the same \(d\)-spaced lattice, the range is *exactly* \(n-d\), with the same \(N\) levels each repeated \(d\) times. The lower bound is therefore attained. Such words exist explicitly: set
\[
x_k=\left\lfloor\frac{(k+1)b}{n}\right\rfloor-\left\lfloor\frac{kb}{n}\right\rfloor\quad(0\le k<n),
\]
which gives \(b\) ones and satisfies circular balance by telescoping floors. The standard characterization of circularly balanced binary words identifies their unique rotation orbit with the \(d\)-fold power of the primitive Christoffel word of composition \((a/d,b/d)\). This completes the proof.

## Verification
A dependency-free Python verifier is supplied as `verify.py`. Execute `python verify.py 14`. It independently enumerates all \(32{,}738\) nonconstant binary words of lengths \(2\) through \(14\); explicitly recounts scattered \(01\) pairs in every rotation; checks both exact inequalities, both equality characterizations using direct factor counts, the universal mean, and identity (1). This exhaustive finite test is a regression check, **not** the proof for unrestricted \(a,b\).

## Relationship to prior work
Poovanandran, Simpson and Teh (2021), *Counting Subwords in Circular Words and Their Parikh Matrices*, introduce the averaged circular Parikh matrix. Their Theorem 4.11 proves the universal binary mean \(ab/2\), which is explicitly treated as prior work here. The new result characterizes the **second moment** over individual rotations and both sharp extremizers. Vesti (2015), building on Jenkinson (2009), studies majorization of **base-2 numerical rotation orbits** and identifies balanced and single-block words as extrema for different statistics. Neither its numerical orbit observable nor its cited majorization inequalities state or immediately imply the present scattered-subsequence variance identities. De Luca and Fici (2022 preprint; later version 2024) study balanced/Christoffel words and their counts, supplying context for the equality structure, but not this dispersion invariant. All are acknowledged without asserting that absence from searches proves novelty.

## Limitations
The alphabet must be binary, both letter counts positive, and all \(n\) positional rotations must be counted with multiplicity. The measure is a single scalar variance, not a complete reconstruction of the circular word: distinct nonequivalent necklaces can share its value. Existing majorization theories may admit a reinterpretation or an unindexed corollary recovering some of these bounds; complete exclusion of such literature is not claimed. The mathematical statements above have unrestricted finite-length proofs, while the code tests only the stated finite range.

## References
1. G. Poovanandran, J. Simpson, W. C. Teh, *Counting Subwords in Circular Words and Their Parikh Matrices*, arXiv:2110.14858v1, first publicly posted 2021-10-28, in particular Theorem 4.11. https://arxiv.org/abs/2110.14858
2. J. Vesti, *The most unbalanced words \(0^{q-p}1^p\) and majorization*, arXiv:1501.00871v2 (2015), especially §§1–2. https://arxiv.org/abs/1501.00871
3. A. De Luca, G. Fici, *Some Results on Digital Segments and Balanced Words*, arXiv:2211.09417v3 (first posted 2022), especially §2 on Christoffel words. https://arxiv.org/abs/2211.09417
4. O. Jenkinson, *Balanced Words and Majorization*, Discrete Mathematics, Algorithms and Applications 1(4) (2009), 463–484, doi:10.1142/S179383090900035X (abstract and statement compared via citation in [2]; full text not inspected).
