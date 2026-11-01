# Complete exponential spectra of the dyadic parabola

## Finding

For an integer \(k\ge 1\), put \(N=2^k\), \(B=2^{k-1}\), and \(R=\mathbb Z/N\mathbb Z\). Let
\[
E_k=\{(x,x^2):x\in R\}\subset R^2.
\]
For \((u,v)\in R^2\), consider the normalized restriction of the additive character to \(E_k\):
\[
\phi_{u,v}(x)=N^{-1/2}\exp\!\left(\frac{2\pi i(ux+vx^2)}{N}\right).
\]
A set \(\Lambda\subset R^2\) of cardinality \(N\) is an exponential spectrum (these characters are an orthonormal basis of \(\ell^2(E_k)\)) **if and only if** the following construction holds.

Choose a function \(f:\mathbb Z/B\mathbb Z\to\mathbb Z/B\mathbb Z\) that is **dyadically 1-Lipschitz**, namely
\[
 a\equiv a'\pmod{2^j}\ \Longrightarrow\ f(a)\equiv f(a')\pmod{2^j}
 \quad(0\le j\le k-1).
\]
For every \(a\in\mathbb Z/B\mathbb Z\), choose independently one of four terminal pairs in \(R^2\):
\[
\begin{aligned}
H_{a,0}&=\{(a,f(a)),(a+B,f(a))\},\\
H_{a,1}&=\{(a,f(a)+B),(a+B,f(a)+B)\},\\
V_{a,0}&=\{(a,f(a)),(a,f(a)+B)\},\\
V_{a,1}&=\{(a+B,f(a)),(a+B,f(a)+B)\}.
\end{aligned}
\]
All additions in the displayed ordered pairs are interpreted modulo \(N\); \(a\) and \(f(a)\) stand for their unique representatives from \(0\) to \(B-1\). Let \(\Lambda\) be the union of these \(B\) chosen pairs. Every spectrum is produced **once and only once** by this construction. The number of distinct unordered frequency sets (without quotienting by translation or any other equivalence) is consequently
\[
\boxed{\mathcal N_k=2^{2^{k+1}-2}.}
\]
Thus the exact counts for \(k=1,2,3\) are respectively \(4\), \(64\), and \(16{,}384\). In contrast with the previously classified odd-prime-power parabola, dyadic spectra need not be single-valued graphs over the first frequency coordinate: the vertical terminal pairs are essential.

## Assumptions and scope

The ambient finite abelian group is \(R^2\), with its standard perfect character pairing. Frequencies in different residue classes in \(R^2\) are counted as distinct even if their restrictions to \(E_k\) agree; the definition of a spectrum requires exactly \(N\) **distinct ambient frequencies** and mutual orthogonality after restriction. The claim holds for every integer \(k\ge1\), including \(k=1\), when \(B=1\) and the function \(f\) is unique. The theorem classifies spectra of this specific quadratic graph, not spectra of every dyadic spectral set or affine equivalence classes of spectra.

## Proof

**1. Quadratic character-sum zero criterion.** For \(u,v\in R\), put
\[
 S_k(u,v)=\sum_{x\bmod 2^k}\exp\!\left(\frac{2\pi i(ux+vx^2)}{2^k}\right).
\]
Suppose \((u,v)\ne(0,0)\) and set \(t=\min(\nu_2(u),\nu_2(v))<k\), with \(\nu_2(0)=k\). After dividing the two coefficients by \(2^t\), write \((U,V)\) modulo \(2^m\), where \(m=k-t\); at least one of \(U,V\) is odd. Periodicity gives \(S_k(u,v)=2^t S_m(U,V)\). We establish
\[
\boxed{S_k(u,v)=0\ \Longleftrightarrow\
\begin{cases}
U+V\equiv1\pmod2,&m=1,\\
U\equiv1\pmod2,&m\ge2.
\end{cases}}
\]
When \(m=1\), the identity \(x^2=x\pmod2\) gives \(S_1(U,V)=1+(-1)^{U+V}\). When \(m\ge2\) and \(U\) is odd, translating \(x\) by \(2^{m-1}\) leaves the quadratic term unchanged and multiplies the linear exponential by \(-1\). Hence the sum is zero, independently of \(V\).

For the converse at \(m\ge2\), if \(U\) is even, primitivity forces \(V\) odd. Expanding the squared modulus and substituting \(h=x-y\) gives
\[
|S_m(U,V)|^2=\sum_{h\bmod 2^m}
 e^{2\pi i(Vh^2+Uh)/2^m}\sum_{y\bmod2^m}e^{2\pi i(2Vhy)/2^m}.
\]
The inner sum equals \(2^m\) precisely for \(h=0\) or \(h=2^{m-1}\), and is zero otherwise. Both surviving phases are \(1\), since \(U\) is even and \(m\ge2\). It follows that \(\lvert S_m(U,V)\rvert^2=2^{m+1}>0\). This proves the criterion with no unverified Gauss-sum cases.

**2. Translation into binary branching.** The inner product of two normalized characters, at distinct frequencies \((u,v)\) and \((u',v')\), is \(N^{-1}S_k(u-u',v-v')\). Write the two coordinates of each frequency in their \(k\)-bit expansions. If the two frequencies first differ in *any* coordinate at bit position \(j<k-1\), the zero criterion requires that their first-coordinate bits at \(j\) differ. If they first differ only at the highest position \(j=k-1\), the criterion instead requires that their pair of highest bits have Hamming distance exactly one. These conditions are both necessary and sufficient for mutual orthogonality.

**3. Capacity bound and rigidity.** Organize an orthogonal set into the cells defined by the first \(j\) low bits of both coordinates, for \(j=0,\ldots,k-1\). Within any occupied cell at depth \(j<k-1\), at most two of the four immediate child cells can be occupied: any two occupied children must have distinct first-coordinate bits. For \(j=k-1\), at most two of the four possible top-bit completions can belong to an orthogonal set, and when two are chosen they must form an edge of the four-vertex binary square. Induction therefore bounds the population of each depth-\(j\) cell by \(2^{k-j}\), and in particular bounds the entire orthogonal set by \(N\).

An exponential spectrum has exactly \(N\) elements and hence attains equality at every cell on this branching tree. Consequently every occupied cell has **exactly two** occupied children. Up to depth \(k-1\), the two lower-coordinate children have different first-coordinate bits. Thus there is exactly one occupied joint low-bit prefix for each prefix of the first coordinate. In particular the occupied residue classes modulo \(B\) are precisely \((a,f(a))\) for a unique function \(f\), and prefix consistency shows that \(f\) is 1-Lipschitz. At the final bit each occupied cell has two completions differing in exactly one coordinate, hence one of the four displayed terminal pairs. Conversely, any 1-Lipschitz \(f\) and any choices of terminal edges obey the character-sum zero criterion for every pair, giving \(N\) mutually orthogonal unit vectors, which form a basis.

**4. Counting distinct frequency sets.** Write the values of \(f\) in binary. The output bit at position \(j\), for \(0\le j\le k-2\), may be specified independently for each input residue class modulo \(2^{j+1}\), and only for those classes. There are \(2^{2^{j+1}}\) choices at that position, so
\[
 \#\{f\}=2^{\sum_{j=0}^{k-2}2^{j+1}}=2^{2^k-2}.
\]
Each of the \(B=2^{k-1}\) terminal cells independently allows four distinct edges, supplying another \(4^B=2^{2^k}\) choices. The low residue classes uniquely recover \(f\), and the two top-bit points uniquely recover each edge, so no overcounting occurs. Their product is \(2^{2^{k+1}-2}\), as claimed.

## Verification

The standalone Python 3 checker `check_dyadic_spectra.py` uses exact cyclotomic reduction modulo \(X^{2^{k-1}}+1\) to determine zeros of the character sums without floating-point tolerances. It compares all \(N^2\) frequency differences against the criterion for every \(k\) from \(1\) through \(6\). It generates and checks all \(4\), \(64\), and \(16{,}384\) predicted spectra for \(k=1,2,3\), and separately enumerates all candidate spectral sets for \(k=1,2\) to confirm completeness. Reproduce using `python3 check_dyadic_spectra.py` with standard-library Python 3. The theorem for unrestricted \(k\) follows from the proof, not the finite verification.

## Relationship to prior work

The published classification *Complete exponential spectra of the parabola over odd prime-power rings* establishes a graph-of-strict-contraction characterization and exact count for **odd** primes only; it explicitly excludes characteristic two. The present theorem covers that previously excluded dyadic family and produces a different branching geometry, with horizontal and vertical terminal pairs and a 1-Lipschitz rather than strictly contracting lower map. This is not an implication of the odd-prime theorem, because its crucial completion-of-squares argument requires that two be invertible.

Iosevich and Koh treat extension estimates and Gauss-sum analysis on nondegenerate finite-field quadratic surfaces; their hypotheses and conclusion differ from a complete basis-partner classification on two-adic residue rings. Cai, Chen, Lipton, and Lu discuss exact exponential-sum evaluation, an existing ingredient rather than the claimed classification. Fan, Fan, and Shi characterize spectral sets in one-dimensional cyclic prime-power rings and in the \(p\)-adic field; this does not directly classify all ambient frequency partners of the two-coordinate quadratic graph. The full texts of the odd-prime classification and the two cited accessible mathematical papers were compared to the statement, not merely their titles. The result does not claim novelty of classical quadratic Gauss-sum formulas.

## Limitations

The family is restricted to powers of two and the graph of the squaring map in two coordinates. It does not classify spectra up to natural symmetries, nor does it cover general polynomial graphs or odd-prime-power analogues (addressed in prior literature). Frequency sets, not distinct restricted functional bases modulo ambient-frequency coincidences, are counted. The absence of a directly matching theorem in the searches and inspected sources is not proof of priority; equivalent earlier descriptions in Hadamard-matrix or residue-ring literature remain possible. Independent mathematical validation has not been performed.

## References

- Alex Iosevich and Doowon Koh, *Extension theorems for the Fourier transform associated with non-degenerate quadratic surfaces in vector spaces over finite fields*, arXiv:0804.4505v1, first public 2008-04-28, https://arxiv.org/abs/0804.4505.
- Jin-Yi Cai, Xi Chen, Richard Lipton, and Pinyan Lu, *On Tractable Exponential Sums*, arXiv:1005.2632v1, first public 2010-05-14, https://arxiv.org/abs/1005.2632.
- Aihua Fan, Shilei Fan, and Ruxi Shi, *Compact Open Spectral Sets in \(\mathbb Q_p\)*, arXiv:1511.04837v1, first public 2015-11-16, https://arxiv.org/abs/1511.04837.
- *Complete exponential spectra of the parabola over odd prime-power rings*, published mathematical research record, 2026, https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-complete-exponential-spectra-of-the-parabola-over-odd-prime-powe--2cf08dd7e325.
