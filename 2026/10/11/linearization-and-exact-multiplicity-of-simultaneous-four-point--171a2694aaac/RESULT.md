# Linearization and exact multiplicity of simultaneous four-point Walsh spectra

## Finding

For every integer \(d\ge2\), every nonempty finite family \(\mathcal A=(A_1,\dots,A_s)\) of four-element subsets of \(V=\mathbb F_2^d\) has the following exact simultaneous Fourier-spectrum law. Let
\[
Z=\{u\in V\setminus\{0\}:\ \sum_{a\in A_i}(-1)^{a\cdot u}=0\text{ for every }i\},
\quad
T=\#\{W\le V:\dim W=2,\ W\setminus\{0\}\subseteq Z\}.
\]
Put \(L=\sum_i\operatorname{span}\{a-a':a,a'\in A_i\}\), \(I=L^\perp\), and \(h=\dim I=d-\dim L\). Then the numbers of common orthogonal four-character spectra that are affine planes and that are affine-independent four-point sets are respectively
\[
N_{\mathrm{plane}}=2^{d-2}T,
\qquad N_{\mathrm{ind}}=2^{d-2}(2^h-1)T,
\]
so their total number is exactly
\[
\boxed{N_{\mathrm{total}}=2^{d+h-2}T.}
\]
In particular, a family possesses a common spectrum if and only if it possesses a common *affine-plane* spectrum. If \(T>0\), the affine-plane fraction is exactly \(2^{-h}\); if the joint direction space equals \(V\), all common spectra are affine planes.

There is a three-set obstruction in \(\mathbb F_2^3\): define \(e_1,e_2,e_3\) to be the standard basis and
\[
A_1=\{0,e_1,e_2,e_1+e_2\},\quad
A_2=\{0,e_1,e_3,e_1+e_3\},\quad
A_3=\{0,e_1,e_2+e_3,e_1+e_2+e_3\}.
\]
Every pair has exactly four common spectra, whereas the triple has none.

## Assumptions and scope

All vector spaces, orthogonal complements, dimensions, and additions are over \(\mathbb F_2\). A frequency \(b\in V\) represents the Walsh character \(\chi_b(a)=(-1)^{a\cdot b}\). A four-element frequency set \(B\subset V\) is a **spectrum** of \(A_i\) precisely when the four restrictions \(\{\chi_b|_{A_i}:b\in B\}\) form an orthogonal basis of complex-valued functions on \(A_i\) under counting measure. A **common spectrum** is one frequency set that is a spectrum for every member of the family. Members of the family may repeat or be translates of one another; the family must be nonempty. The theorem is about orthogonal character bases, not arbitrary invertible Riesz bases.

Every four-point set of \(V\) has affine dimension two or three. Affine dimension two means a coset of a two-dimensional vector subspace; affine dimension three means an affine-independent quadruple. The arithmetic parameter \(h\) is the dimension of the annihilator of all differences within the given time sets.

## Proof

**1. Fourier-zero criterion.** For \(b\ne b'\), the inner product of the character restrictions on \(A_i\) is
\[
\sum_{a\in A_i}\chi_b(a)\overline{\chi_{b'}(a)}
=\sum_{a\in A_i}(-1)^{a\cdot(b+b')}.
\]
Thus a four-point frequency set is a common spectrum exactly when its six pairwise differences are in \(Z\). If it is an affine plane \(b+W\), these differences are precisely the three nonzero vectors of \(W\), giving \(2^{d-2}T\) plane spectra.

**2. The missing seventh direction is always annihilating.** Suppose instead that \(B=b+\{0,x,y,z\}\), with \(x,y,z\) linearly independent. Write \(H=\operatorname{span}\{x,y,z\}\) and \(t=x+y+z\). The six pairwise differences of \(B\) are exactly \(H\setminus\{0,t\}\), all in \(Z\). We show \(t\in I\).

Fix one \(A_i\). It is either an affine plane \(a+\{0,u,v,u+v\}\), with independent \(u,v\), or an affine-independent quadruple \(a+\{0,u,v,w\}\), with independent \(u,v,w\). In the plane case its Fourier transform is
\[
(-1)^{a\cdot n}(1+(-1)^{u\cdot n})(1+(-1)^{v\cdot n}),
\]
so \(Z\) avoids the kernel of the linear evaluation map \(n\mapsto(n\cdot u,n\cdot v)\). This map has rank at most two on the three-dimensional space \(H\). Its kernel on \(H\) is nonzero but cannot contain any of the six allowed pairwise differences, hence the kernel is exactly \(\{0,t\}\) and \(t\) annihilates \(u,v\).

In the independent case the transform is
\[
(-1)^{a\cdot n}\bigl(1+(-1)^{u\cdot n}+(-1)^{v\cdot n}+(-1)^{w\cdot n}\bigr).
\]
It vanishes exactly when the triple \((n\cdot u,n\cdot v,n\cdot w)\) has Hamming weight two. All six pairwise differences have even-weight evaluation triples, and they span \(H\); therefore the evaluation map from \(H\) takes values in the two-dimensional even-weight plane of \(\mathbb F_2^3\). Its kernel is nonzero. As above, none of the six nonzero differences can be in the kernel, so its kernel is \(\{0,t\}\). Therefore \(t\) annihilates \(u,v,w\). Since this holds for every \(A_i\), \(t\in L^\perp=I\). In fact \(t\ne0\) and \(t\notin Z\), because any character trivial on all the differences of a four-point set has Fourier sum of modulus four.

**3. Conversely, classification of nonplane spectra.** Let \(W\) be any admissible two-dimensional frequency subspace and \(0\ne t\in I\). Because every nonzero element of \(I\) is outside \(Z\), necessarily \(W\cap\langle t\rangle=\{0\}\). Put \(H=W\oplus\langle t\rangle\). Translating a common Fourier-zero frequency by \(t\) multiplies each \(A_i\)-transform by the constant sign \((-1)^{a_i^0\cdot t}\), where \(a_i^0\in A_i\) is arbitrary, so \(H\setminus\{0,t\}\subseteq Z\). Therefore **every** affine-independent four-point subset of any coset of \(H\) whose four-point sum is \(t\) is a common spectrum.

Conversely, step 2 shows that every nonplane common spectrum lies in this construction, with its unique \(H\) and \(t\). For a fixed pair \((H,t)\), there are exactly four complementary two-dimensional subspaces \(W\) of \(\langle t\rangle\) in \(H\), all admissible. Thus the number of such pairs is \(T(2^h-1)/4\). In each coset of \(H\), exactly eight affine-independent unordered quadruples have four-point sum \(t\): among the \(\binom84=70\) four-subsets of a three-dimensional binary affine space, fourteen are affine planes and the remaining 56 are equally distributed by their nonzero four-point sums across the seven nonzero directions. There are \(2^{d-3}\) cosets. Hence
\[
N_{\mathrm{ind}}=\frac{T(2^h-1)}4\cdot8\cdot2^{d-3}=2^{d-2}(2^h-1)T.
\]
For \(d=2\), the independent case is empty and the formula still holds because \(h=0\). Combining with step 1 proves the complete count and the existence and rigidity consequences.

**4. Sharp simultaneous obstruction.** For the displayed three time planes in \(\mathbb F_2^3\), write \(n_j=n\cdot e_j\). Their common Fourier zeros require \(n_1=1\) or, respectively, \(n_2=1\), \(n_3=1\), and \(n_2+n_3=1\). A two-dimensional frequency subspace \(W\) would have to have exactly one nonzero vector \(t\) with \(t_1=0\), and that vector would have to satisfy \(t_2=t_3=t_2+t_3=1\), a contradiction. Thus \(T=0\) for the triple. For each pair, exactly two admissible frequency planes \(W\) occur, giving \(2^{3-2}\cdot2=4\) common spectra; the joint direction span of each pair is all of \(\mathbb F_2^3\), so the nonplane contribution is zero. This gives the asserted three-set obstruction.

## Verification

The standalone `checker.cpp` uses exact integer Walsh sums and independent pairwise-difference tests. Compile with `g++ -std=c++17 -O3 -Wall -Wextra checker.cpp -o checker` and execute `./checker`. It exhaustively checks all individual four-point sets in dimensions two, three, and four; every unordered pair of four-point sets in dimension three; 700 fixed-seed four-dimensional multiset families; and all seven nonempty subfamilies of the three-plane obstruction. It separately enumerates the two-dimensional admissible subspaces, computes the annihilator cardinality, and partitions directly enumerated common spectra into plane and independent types. The successful run reported `CHECK_PASS families=5013` together with the obstruction counts \(16,16,4,16,4,4,0\) in nonempty-subfamily bit-mask order. The universally quantified proof above, not finite enumeration, establishes the theorem in every dimension and for arbitrarily large finite families.

## Relationship to prior work

Ferguson, Mayeli, and Sothanaphan, *Riesz bases of exponentials and multi-tiling in finite abelian groups*, arXiv:1904.04487, Section 7.1, explicitly formulate simultaneous exponential bases and give a three-family obstruction for two-point sets. Their framework concerns general invertible Riesz bases; it does not state this orthogonal four-point linearization, the formula for the number of spectra, or this four-point obstruction. Kiss, D. Matolcsi, M. Matolcsi, and Somlai, *Tiling and weak tiling in* \((\mathbb Z_p)^d\), arXiv:2212.05513, develops spectrality and tiling through Fourier-zero and positive-definite-function methods, rather than counting common four-point spectra. The exact pair-versus-triple distinction here is for simultaneous **orthogonal** bases, not a counterexample to existence of general Riesz bases.

## Limitations

This theorem applies to four-point time sets in binary vector spaces and to orthogonal Walsh-character spectra; it does not assert an analogous count for other cardinalities, odd prime fields, or arbitrary exponential Riesz bases. The checker exhausts specified small cases but is not a universal certificate. An independent audit has not been performed, and an equivalent older statement under universal-spectrum or Hadamard terminology cannot be categorically excluded by the literature examined.

## References

1. S. Ferguson, A. Mayeli, and N. Sothanaphan, *Riesz bases of exponentials and multi-tiling in finite abelian groups*, arXiv:1904.04487, first posted 2019-04-09, https://arxiv.org/abs/1904.04487 ; full text https://arxiv.org/html/1904.04487v6 .
2. G. Kiss, D. Matolcsi, M. Matolcsi, and G. Somlai, *Tiling and weak tiling in* \((\mathbb Z_p)^d\), arXiv:2212.05513, first posted 2022-12-11, https://arxiv.org/html/2212.05513v1 .
3. M. N. Kolountzakis and M. Matolcsi, *Complex Hadamard matrices and the spectral set conjecture*, arXiv:math/0411512 (2004), https://arxiv.org/abs/math/0411512 ; reviewed abstract only, not full text.
