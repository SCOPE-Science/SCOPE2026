# A nonseparable nontiling Gabor window over every odd prime field of order at least five
## Finding
For every prime \(p\ge 5\), write \(\omega=e^{2\pi i/p}\) and define phases \(q_m\) on \(\mathbb F_p\) by \(q_{-2}=\omega\), \(q_{-1}=\omega^{-1}\), and \(q_m=1\) otherwise. Define
\[
h(x)=\frac1p\sum_{m\in\mathbb F_p}q_m\omega^{mx},\qquad g(x,y)=p^{-1/2}h(x-y^2).
\]
With translation set \(A=\mathbb F_p\times\{0\}\) and modulation set \(B=\{0\}\times\mathbb F_p\), the Gabor system
\[
\mathcal G(g,A,B)=\{g((x,y)-(a,0))\omega^{by}:a,b\in\mathbb F_p\}
\]
is an orthonormal basis of \(L^2(\mathbb F_p^2)\). Its support is
\[
E=\{(x,y)\in\mathbb F_p^2:x-y^2\ne1\},\qquad |E|=p(p-1).
\]
The same window simultaneously has all six features asked for in the finite-prime-field Gabor-window question of Iosevich, Kolountzakis, Lyubarskii, Mayeli and Pakianathan: \(g\) is not a product of one-variable functions, \(g\) is not positive, \(|g|\) is not a constant multiple of an indicator, \(|\widehat g|\) is not a constant multiple of an indicator, \(|E|\ne|B|\), and \(E\) does not tile \(\mathbb F_p^2\).

## Assumptions and scope
All groups use counting measure. The normalized one-dimensional Fourier transform is
\[
\widehat h(m)=p^{-1}\sum_{x\in\mathbb F_p}h(x)\omega^{-mx},
\]
and the normalized two-dimensional transform is
\[
\widehat g(m,n)=p^{-2}\sum_{x,y\in\mathbb F_p}g(x,y)\omega^{-mx-ny}.
\]
The claim is only for primes \(p\ge5\). No assertion is made for \(p=2\) or \(p=3\), and no classification of all such windows is claimed.

## Proof
Fourier inversion gives \(\widehat h(m)=q_m/p\), so \(|\widehat h(m)|=1/p\) for every \(m\). Plancherel therefore yields, for every \(a,a'\in\mathbb F_p\),
\[
\sum_x h(x-a)\overline{h(x-a')}=\frac1p\sum_m\omega^{m(a'-a)}=\mathbf 1_{a=a'}.
\]
Consequently
\[
\langle g_{a,b},g_{a',b'}\rangle
=\frac1p\sum_y\omega^{(b-b')y}\sum_x h(x-a-y^2)\overline{h(x-a'-y^2)}
=\mathbf 1_{a=a'}\mathbf 1_{b=b'}.
\]
There are \(p^2\) atoms in the \(p^2\)-dimensional space, hence they form an orthonormal basis.

It remains to identify the support. Put \(\phi_{-2}=1\), \(\phi_{-1}=-1\), and \(\phi_m=0\) otherwise. Then
\[
ph(x)=\sum_{m\in\mathbb F_p}\omega^{xm+\phi_m}.
\]
If this sum vanishes, let \(c_j\) count the occurrences of residue \(j\) among the exponents \(xm+\phi_m\), and set \(P(T)=\sum_{j=0}^{p-1}c_jT^j\). Since \(P(\omega)=0\), the minimal polynomial \(1+T+\cdots+T^{p-1}\) divides \(P\). Both have degree at most \(p-1\), while \(\sum_jc_j=p\), so every \(c_j=1\). Thus the exponent map must be a permutation of \(\mathbb F_p\).

For \(x\ne0\), the unchanged indices contribute every residue except \(-2x\) and \(-x\); the two changed values are \(-2x+1\) and \(-x-1\). Neither changed value can equal its corresponding omitted value, so permutation forces the cross-match
\[
-2x+1=-x,\qquad -x-1=-2x,
\]
which is equivalent to \(x=1\). For \(x=0\) the exponent map is not a permutation when \(p\ge5\). Hence \(h\) has the unique zero \(x=1\), proving the displayed formula for \(E\).

Since \(|E|=p(p-1)\) does not divide \(p^2\), \(E\) cannot tile \(\mathbb F_p^2\); also \(|E|\ne|B|=p\). The rows \(y=0\) and \(y=1\) of \(g\) omit different \(x\)-coordinates, namely \(1\) and \(2\), while every row is nonzero. A product \(u(x)v(y)\) with all rows nonzero would have the same \(x\)-support in every row, so \(g\) is not a product of one-variable functions.

The window is not positive. If \(h\) were real-valued, Fourier symmetry would require \(q_{-m}=\overline{q_m}\). At \(m=1\) this would say \(\omega^{-1}=1\), a contradiction.

The modulus is not constant on \(E\). Indeed \(\|h\|_2=1\) and \(h\) has \(p-1\) nonzero entries, so constant nonzero modulus would have to equal \(1/\sqrt{p-1}\). But
\[
|h(0)|=\frac{p-2+2\cos(2\pi/p)}p>\frac{p-2}p>\frac1{\sqrt{p-1}}
\]
for \(p\ge5\).

Finally, direct substitution gives
\[
\widehat g(m,n)=q_m p^{-5/2}\sum_{y\in\mathbb F_p}\omega^{-my^2-ny}.
\]
For \(m=0\), the inner sum is \(p\) when \(n=0\) and \(0\) otherwise. For \(m\ne0\), its squared modulus is \(p\): after expanding the square, the invertible change of variables \(u=y-z\), \(v=y+z\) makes the \(v\)-sum vanish unless \(u=0\). Therefore
\[
|\widehat g(m,n)|=
\begin{cases}
p^{-3/2},&(m,n)=(0,0),\\
0,&m=0,\ n\ne0,\\
p^{-2},&m\ne0.
\end{cases}
\]
There are two distinct nonzero Fourier magnitudes, so \(|\widehat g|\) is not a constant multiple of an indicator.

## Verification
The accompanying `verify.py` independently reconstructs the phase sequence and window for \(p\in\{5,7,11,13,17,19,23\}\). It checks the unique-zero combinatorics, the flat one-dimensional Fourier magnitude, every translation inner product, the complete \(p^2\)-atom Gabor Gram matrix, the support size, variation of \(|g|\), nonreality, and the stated two-dimensional Fourier-magnitude formula. Running the packaged file produces the stored `verification_output.txt` line `VERIFY_OK primes=5,7,11,13,17,19,23 atom_systems=1543`.

The computation is a finite consistency check only. The theorem for every prime \(p\ge5\) follows from the analytic proof above, including the cyclotomic minimal-polynomial argument and the quadratic Gauss-sum magnitude calculation.

## Relationship to prior work
Iosevich, Kolountzakis, Lyubarskii, Mayeli and Pakianathan study separable Gabor orthonormal bases on \(L^2(\mathbb F_p^d)\). Their Theorem 1.7 constructs windows for which neither \(|g|\) nor \(|\widehat g|\) is an indicator multiple, but their construction is a product of one-variable functions and has full support. At the end of the paper they explicitly ask whether one window can simultaneously be nonproduct, nonpositive, nonconstant-modulus in time and frequency, have \(|E|\ne|B|\), and have nontiling support. The construction above supplies such a window uniformly for every \(p\ge5\).

Zhou's discrete-Gabor work gives a later structural classification of allowable time-frequency support sets in cyclic finite-dimensional systems and, in the prime case, a necessity theorem for those support sets. Its ambient system is \(\mathbb C^n\) with time-frequency set in \(\mathbb Z_n^2\), whereas the present claim concerns a separable system on \(L^2(\mathbb F_p^2)\) and the geometry of the window's spatial support. Zhou's 2024 paper explicitly distinguishes these two settings. The inspected sources do not state the construction above or an implication that supplies all six requested properties.

## Limitations
This result is an existence theorem, not a classification. It does not determine whether analogous constructions exist for \(p=2\) or \(p=3\), nor does it classify nontiling Gabor windows for larger dimensions or nonprime fields. The originality assessment is based on the cited primary papers, later directly related work, targeted literature and semantic-index searches; it cannot exclude an unindexed or differently phrased construction.

## References
1. A. Iosevich, M. Kolountzakis, Yu. Lyubarskii, A. Mayeli, J. Pakianathan, *On Gabor orthonormal bases over finite prime fields*, arXiv:1712.09120, first posted 25 December 2017; DOI 10.1112/blms.12426.
2. W. Zhou, *On the construction of discrete orthonormal Gabor bases on finite dimensional spaces*, Applied and Computational Harmonic Analysis 55 (2021), 270–281; DOI 10.1016/j.acha.2021.06.001. The article was available online 7 June 2021 and lists MSC 42C15 first.
3. W. Zhou, *A Fuglede type conjecture for discrete Gabor bases*, Banach Journal of Mathematical Analysis 18 (2024), Article 51; DOI 10.1007/s43037-024-00361-x.
4. C. Frederick, A. Mayeli, *A characterization of Gabor Riesz bases with separable time-frequency shifts*, arXiv:2202.06343. This paper treats continuous \(\mathbb R^d\) Riesz Gabor systems generated by characteristic functions and does not imply the finite-field construction above.
