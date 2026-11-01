# Three-direction dihedral Radon tomography: exact nullities, singular spectra, and optimal weights

## Finding

For every integer \(n\ge3\), write the dihedral group of order \(2n\) as
\[
G_n=\langle r,s\mid r^n=s^2=1,\ srs=r^{-1}\rangle.
\]
For any \(a\in\{1,\ldots,n-1\}\), consider the three maximal cyclic subgroups
\[
H_0=\langle r\rangle,\qquad H_1=\langle s\rangle,\qquad H_2=\langle sr^a\rangle.
\]
For a subgroup \(H\), define the *unnormalized* coset-sum transform \((R_Hf)(gH)=\sum_{h\in H}f(gh)\), taking one row for each distinct left coset. Equip the domain and each row space with counting-measure Euclidean norms. Put \(R_a=(R_{H_0},R_{H_1},R_{H_2})\).

**Exact injectivity and defect.** For \(d=\gcd(a,n)\),
\[
\boxed{\dim\ker R_a=d-1.}
\]
Consequently, among maximal-cyclic-subgroup directions, three is the smallest number allowing injectivity, and these particular three directions determine every function on \(G_n\) precisely when \(\gcd(a,n)=1\). The transform has \(2n+2\) measurements, with two redundant linear relations in the injective case.

**Complete weighted spectrum.** Assign positive weights \(\alpha,\beta,\gamma\) to the squared measurements from \(H_0,H_1,H_2\), respectively, and define
\[
T_a=\alpha R_{H_0}^*R_{H_0}+\beta R_{H_1}^*R_{H_1}+\gamma R_{H_2}^*R_{H_2},\qquad b=\beta+\gamma.
\]
Its eigenvalues, counted with multiplicity, are \(n\alpha+2b\), \(n\alpha\), and, for \(k=1,\ldots,n-1\), the two numbers
\[
 b\pm\bigl|\beta+\gamma\exp(2\pi i ka/n)\bigr|,
\]
**interpreted with the following nonduplicating multiplicity convention:** for \(1\le k\le\lfloor(n-1)/2\rfloor\), each sign occurs twice, and when \(n\) is even the remaining \(k=n/2\) contributes each sign once. These \(2n\) values give the entire spectrum.

**Sharp stability.** When \(a\) is coprime to \(n\), the unweighted singular-value condition number is
\[
\boxed{\kappa_2(R_a)=\sqrt{\frac{n+4}{2-2\cos(\pi/n)}}\sim\frac{n^{3/2}}{\pi}.}
\]
Among all positive scalar weights applied uniformly within each of the three direction families, the **unique minimizer up to common scaling** is
\[
\boxed{\beta=\gamma,\qquad n\alpha=(\beta+\gamma)(1-\cos(\pi/n)).}
\]
The sharp optimally weighted condition number is
\[
\boxed{\kappa_{\mathrm{opt}}^2=1+\frac{2}{1-\cos(\pi/n)},\qquad
\kappa_{\mathrm{opt}}\sim\frac{2n}{\pi}.}
\]
Thus appropriate direction weighting improves the growth order of the condition number from \(n^{3/2}\) to \(n\), while preserving injectivity.

## Assumptions and scope

All functions are arbitrary complex functions on the finite group \(G_n\). The subgroup coordinates are fixed as above; left cosets are taken as *distinct sets*, not counted repeatedly by parametrizations. Each coset sum is unnormalized. The weight parameter \(\alpha\) multiplies the squared norm of the two rotation-coset measurements, while \(\beta\) and \(\gamma\) multiply the squared norms of the \(n\) coset measurements in each reflection direction. All weights are strictly positive. The spectral and nullity formulas hold for noncoprime \(a\), whereas finite condition numbers and their optimization require \(\gcd(a,n)=1\). No claim is made about independently weighting individual cosets or about noncyclic line families.

## Proof

**1. Coset normal identity.** For every subgroup \(H\le G_n\), counting each left coset once gives
\[
(R_H^*R_Hf)(x)=\sum_{h\in H}f(xh).
\]
Writing \(C_H=R_H^*R_H\), the normal operator is \(T_a=\alpha C_{H_0}+\beta C_{H_1}+\gamma C_{H_2}\). Note that \(C_{H_0}\) sends every rotation to the total rotation sum and every reflection to the total reflection sum, while \(C_{H_1}=I+Q_s\) and \(C_{H_2}=I+Q_{sr^a}\), with \((Q_hf)(x)=f(xh)\).

**2. Discrete Fourier blocks.** Set \(u_j=f(r^j)\), \(v_j=f(sr^j)\), for indices \(j\in\mathbb Z/n\mathbb Z\). Right multiplication gives \(r^js=sr^{-j}\), \(r^j sr^a=sr^{a-j}\), and the analogous relations interchanging \(u\) and \(v\). Taking the ordinary unitary \(n\)-point Fourier transform in the index \(j\), the constant modes span an invariant two-dimensional block with eigenvalues \(n\alpha+2b\) and \(n\alpha\). The remaining frequency modes pair \(\widehat u_k\) with \(\widehat v_{-k}\) and have Hermitian blocks
\[
B_k=\begin{pmatrix}
b&\beta+\gamma\exp(-2\pi i ka/n)\\
\beta+\gamma\exp(2\pi i ka/n)&b
\end{pmatrix},\qquad k=1,\ldots,n-1.
\]
Each block has eigenvalues \(b\pm|\beta+\gamma e^{2\pi i ka/n}|\). The Fourier pairing \(k\leftrightarrow n-k\) yields the multiplicities stated above. There are exactly \(2n\) eigenvalues, so no sectors have been omitted. Equivalently, one may list a single eigenvalue from each sign at every nonzero \(k\), giving the same multiset.

**3. Exact kernel and minimality.** Since the weights are positive, a nonconstant block has a zero eigenvalue exactly when \(e^{2\pi i ka/n}=1\), i.e. \(n\mid ka\). There are exactly \(d-1\) such nonzero residue classes \(k\). The two constant eigenvalues are positive. This proves the nullity law. A single reflection direction has an alternating-function kernel, and with rotation direction plus just one reflection direction every nonzero-frequency block remains singular. With two reflection directions but without the rotation direction, the function equal to \(+1\) on rotations and \(-1\) on reflections belongs to the kernel. Thus fewer than three maximal directions never suffice. If \(d=1\), all \(2n\) columns are independent, while the \(2n+2\) output rows have two linear dependencies because the total of each direction's coset sums equals the group total.

**4. Unweighted conditioning.** For \(\alpha=\beta=\gamma=1\) and coprime \(a\), multiplication by \(a\) permutes the nonzero residues modulo \(n\). The largest absolute cosine factor is \(\cos(\pi/n)\). Consequently the smallest eigenvalue is \(\delta=2-2\cos(\pi/n)\), and the largest is the constant-mode eigenvalue \(n+4\). Their square-root ratio is the stated condition number.

**5. Optimal direction weights.** Fix coprime \(a\), write \(A=n\alpha\), and put
\[
R=\sqrt{b^2-4\beta\gamma\sin^2(\pi/n)},\qquad \delta=b-R>0.
\]
The largest eigenvalue is always \(A+2b\), since \(b+R\le2b\), and the smallest is \(\min\{A,\delta\}\). Therefore
\[
\kappa_2(T_a^{1/2})^2=\frac{A+2b}{\min\{A,\delta\}}.
\]
For fixed positive \(\beta,\gamma\), this expression strictly decreases for \(A<\delta\) and strictly increases for \(A>\delta\), so its unique optimum is \(A=\delta\), with value \(1+2b/\delta\). With \(b\) fixed, \(\delta=b-\sqrt{b^2-4\beta\gamma\sin^2(\pi/n)}\) is uniquely maximized when \(\beta\gamma\) is maximal, i.e. \(\beta=\gamma=b/2\). Then \(R=b\cos(\pi/n)\), giving the unique optimal ratios and sharp value. Standard sine and cosine expansions give the stated asymptotics.

## Verification

The included `checker.py` constructs all coset-incidence matrices directly from the multiplication law and compares their normal-matrix spectra against independently evaluated Fourier-block formulas. It performs exact modular-rank comparisons for every \(n=3,\ldots,26\) and every \(1\le a<n\), plus full Gram eigenvalue and unequal-weight comparisons. In the executed environment, the checker passed 648 exact modular ranks, 858 spectral comparisons, 84 proper-subfamily rank tests, and 189 unequal-weight comparisons. Command: `python checker.py` after installing `numpy` as specified in `requirements.txt`. These finite checks do not replace the all-\(n\) proof above.

## Relationship to prior work

Ilmavirta's *On Radon transforms on finite groups* (first arXiv submission 2014-11-14), especially Proposition 5.1 and Section 7.3, proves injectivity for the full cyclic-subgroup Radon transform on dihedral groups and introduces a maximal-geodesic variant. Its explicit inversion uses **all \(n\) reflection directions**, not the two reflection directions studied here. The limited-direction nullity law, the complete singular spectrum, and the optimal three-family weighting do not follow from the statement of that result without a separate spectral analysis. The cyclic-convolution methods in Fill's work provide useful background but concern abelian moving averages rather than these noncommutative coset projections. Separate published results on projective cyclic-grid tomography and generalized-dihedral three-tap convolution concern different transforms and do not directly imply this theorem.

## Limitations

Only three selected maximal cyclic subgroup families are treated; a subset of rows within any one family is not optimized. The weighted optimum is restricted to a single positive scalar per full family, not arbitrary row-by-row or matrix weights. The result concerns the Euclidean counting-measure condition number for unnormalized sums; a different output normalization changes the numerical weight convention. The new deductions have no independent mathematical audit. Earlier equivalent treatments in specialized finite tomography or weighted cycle-spectral literature cannot be excluded solely by the bounded source comparison.

## References

1. J. Ilmavirta, *On Radon transforms on finite groups*, arXiv:1411.3829, first submitted 2014-11-14. https://arxiv.org/abs/1411.3829 . In particular Proposition 5.1 and Section 7.3.
2. J. A. Fill, *The Radon Transform on \(\mathbb Z_n\)*, SIAM Journal on Discrete Mathematics, 1989, DOI:10.1137/0402023. https://doi.org/10.1137/0402023 .
3. *Sharp scalar-view conditioning and a smallest-prime barrier for projective cyclic Radon transforms*, published research record, 2026-10-11, identifier `58911b2d31f1` (full published result text inspected).
4. *Complete three-tap Fourier-rank census on elementary generalized dihedral groups*, published research record, 2026-10-11, identifier `7d6c365ba4ff` (full published result text inspected).
