# Sharp Riesz conditioning for consecutive triples on finite cycles

## Finding

Let \(N\ge3\) be an integer, let \(E=\{0,1,2\}\subset\mathbb Z_N\), and for each three-element frequency set \(B\subset\mathbb Z_N\) form the square exponential synthesis matrix
\[
V_B=(e^{2\pi i kb/N})_{k\in E,\,b\in B}.
\]
Write \(\rho_N(B)=\lambda_{\max}(V_B^*V_B)/\lambda_{\min}(V_B^*V_B)\). Every such matrix is invertible. **The exact minimizing frequency sets are precisely those whose three positive cyclic gaps differ by at most one**. Thus, if \(N=3q+r\), \(r\in\{0,1,2\}\), the gaps are a permutation of \((q,q,q)\) for \(r=0\), \((q,q,q+1)\) for \(r=1\), or \((q,q+1,q+1)\) for \(r=2\).

There are exactly \(N/3\) distinct minimizing unordered sets if \(3\mid N\), and exactly \(N\) otherwise. For \(3\mid N\) the minimum is \(1\). For \(3\nmid N\), put
\[
q=\lfloor N/3\rfloor,\quad
 a=1+2\cos(2\pi q/N),\qquad
 b=1+2\cos(2\pi(q+1)/N).
\]
Then \(a>0>b\), and the exact minimum is
\[
\rho(E)=\begin{cases}
 (3-b)/(3+b/2-\sqrt{b^2/4+2a^2}),&N\equiv1\pmod3,\\
 (3+a/2+\sqrt{a^2/4+2b^2})/(3-a),&N\equiv2\pmod3.
\end{cases}
\]
The bounds are for the squared spectral condition number, which is the best exponential Riesz ratio. They make no assertion about arbitrary subsets other than this fixed consecutive triple.

## Assumptions and scope

All statements quantify over every integer \(N\ge3\) and every unordered \(B\subset\mathbb Z_N\) with \(|B|=3\). A *cyclic gap triple* is the ordered list of positive successive differences after writing representatives \(0\le b_1<b_2<b_3<N\): \((b_2-b_1,b_3-b_2,N+b_1-b_3)\). Different starting points rotate this triple. The Riesz ratio is the largest divided by the smallest **eigenvalue** of the positive Gram matrix, not the unsquared matrix condition number. All phase factors have absolute value one. The setting is finite cyclic Fourier analysis; no continuous interpolation or nonuniform weights are assumed.

## Proof

**1. Exact Gram matrix.** Multiply column \(b\) of \(V_B\) by \(e^{-2\pi ib/N}\); this does not change singular values and changes that column into \((e^{-2\pi ib/N},1,e^{2\pi ib/N})^T\). Consequently its Gram matrix \(G\) is real symmetric, with diagonal \(3\) and off-diagonal
\[
g(d)=1+2\cos(2\pi d/N),\qquad g(N-d)=g(d).
\]
The columns are a Vandermonde system in three distinct roots of unity and are independent. Put \(x=2\pi/N\) and \(q=\lfloor N/3\rfloor\). If \(3\mid N\), gaps \((q,q,q)\) give \(G=3I\), hence the minimal ratio \(1\); equality forces each off-diagonal to vanish, so all pair differences are multiples of \(N/3\) and the same balanced triples are the only minimizers.

**2. Balanced spectra and their eigenvalues.** Suppose \(3\nmid N\), and write \(a=g(q)>0\), \(b=g(q+1)<0\). If \(N\equiv1\pmod3\), balanced triples have off-diagonals \((a,a,b)\). Their eigenvalues are
\[
3-b,\qquad 3+b/2\pm\sqrt{b^2/4+2a^2}.
\]
In this congruence class \(|b|\ge a\), so the first eigenvalue is largest. If \(N\equiv2\pmod3\), balanced triples have off-diagonals \((b,b,a)\); their eigenvalues are
\[
3-a,\qquad 3+a/2\pm\sqrt{a^2/4+2b^2}.
\]
Here \(a\ge|b|\), so the first is smallest. Both inequalities follow from the exact half-angle identities below; equality of magnitudes occurs at \(N=4\) only. The formulas for \(\rho(E)\) follow.

For clarity, set \(u=\pi/(3N)\), \(v=\tan u\), and \(s=a-b=a+|b|\). Algebraically,
\[
a+b=\begin{cases}
\displaystyle {2v(v+\sqrt3)(v-(2-\sqrt3))(v+2+\sqrt3)\over(1+v^2)^2},&N\equiv1\pmod3,\\
\displaystyle {2v(v-\sqrt3)(v-2-\sqrt3)(v+2-\sqrt3)\over(1+v^2)^2},&N\equiv2\pmod3.
\end{cases}
\]
The first is nonpositive for \(N\ge4\), while the second is positive for \(N\ge5\); this proves the needed comparisons. For \(N\ge7\) we moreover have \(0<a\le1\), \(0<-b\le1\), hence \(0<s\le2<3\). Every balanced \(G\) has row sum of absolute off-diagonal entries at most \(s\), so Gershgorin gives
\[
\rho_N(B_{\rm bal})\le(3+s)/(3-s).
\]

**3. All gaps shorter than \(q\) are strictly suboptimal.** If the smallest gap \(r\le q-1\) and \(N\ge7\), then \(g(r)\ge g(q-1)>s\). Indeed, the exact identity
\[
g(q-1)-s=1+2\cos(qx)(2\cos x-1)>2(1-\cos x)>0
\]
holds because \(q x\ge\pi/2\), \(q x<2\pi/3\) and \(N\ge7\). A principal two-by-two submatrix of \(G\) has eigenvalues \(3\pm g(r)\). Eigenvalue interlacing therefore yields
\[
\rho_N(B)\ge {3+g(r)\over3-g(r)}>{3+s\over3-s}\ge\rho_N(B_{\rm bal}).
\]
Every unbalanced triple for \(N\equiv1\pmod3\) has such a gap. For \(N\equiv2\pmod3\), the only remaining unbalanced type is \((q,q,q+2)\).

**4. The remaining \((q,q,q+2)\) case.** For \(N\equiv2\pmod3\) and \(N\ge11\), put \(t=-g(q+2)>0\). The unbalanced Gram matrix has off-diagonals \((a,a,-t)\), so its eigenvalues include \(3+t\), and its smallest eigenvalue is strictly below \(3-t\). We show
\[
a(t-a)>b^2.
\]
With \(v=\tan(\pi/(3N))\), direct rational trigonometric algebra gives the exact certificate
\[
a(t-a)-b^2={-4v^2(v-\sqrt3)^2\over(1+v^2)^6}\,P(v),
\]
where
\[
P(v)=v^8-8v^6-56\sqrt3v^5-22v^4+80\sqrt3v^3+112v^2+8\sqrt3v-3.
\]
For \(N\ge11\), \(0<v<1/10\): indeed \(u\le\pi/33<2/21\) and \(\tan u\le u/(1-u^2/2)<42/439<1/10\). Using \(\sqrt3<7/4\), dropping negative terms, and \(v<1/10\), we have
\[
P(v)<10^{-8}+0.14+1.12+1.4-3<0.
\]
This proves \(a(t-a)>b^2\). The balanced eigenvalue formula gives
\[
\rho_N(B_{\rm bal})\le {3+a+2b^2/a\over3-a}
<{3+t\over3-t}<\rho_N(B_{\rm unbal}),
\]
where the middle inequality follows by multiplying positive denominators and checking
\[
(3+t)(3-a)-(3-t)(3+a+2b^2/a)
=6(t-a-b^2/a)+2b^2t/a>0.
\]
This excludes the last unbalanced type in every order \(N\ge11\).

**5. Small orders.** At \(N=3\) the only triple is orthogonal. At \(N=4\) every triple is balanced and has ratio \(4\). At \(N=5\) the balanced \((1,2,2)\) type has eigenvalues \(5,(5-\sqrt5)/2,(3+\sqrt5)/2\), hence ratio \((5+\sqrt5)/2\); the competing \((1,1,3)\) type has eigenvalues \(5,(5+\sqrt5)/2,(3-\sqrt5)/2\), hence a strictly larger ratio. At \(N=6\) the balanced basis is orthogonal. At \(N=8\), the only extra type not excluded by Step 3 is \((2,2,4)\), which has eigenvalues \(1,4,4\) and ratio \(4\); the balanced ratio \((7+\sqrt{25-16\sqrt2})/4<3\). Orders \(N=7,9,10\) are covered by Steps 1–3. Thus all \(N\ge3\) are settled.

**6. Enumeration of equality sets.** A balanced triple for \(3\mid N\) is one coset of the order-three subgroup, giving \(N/3\) sets. Otherwise its unique cyclic gap of the exceptional length has one starting vertex; translating this vertex freely gives exactly \(N\) distinct balanced unordered triples. Steps 3–5 give strict exclusion of all other types. This proves both the value and complete equality classification.

## Verification

Running `python checker.py` (Python 3 with SymPy and NumPy installed) verifies all three exact rational half-angle identities using symbolic algebra. It independently enumerates all three-element frequency sets of \(\mathbb Z_N\) for each \(3\le N\le70\), computes Gram eigenvalues, and checks that the minimizing sets and their cardinalities are exactly those asserted. The checker prints `CHECK_PASS exact_symbolic_identites=3 cyclic_orders=3..70` on successful completion. These finite spectral computations corroborate the theorem; Steps 1–6 above, including the explicit uniform polynomial inequality, prove the statement for every order.

## Relationship to prior work

Ferguson, Mayeli, and Sothanaphan introduced quantitative spectrality and the Riesz ratio in finite abelian groups; their general framework does not state the exact optimum or full extremizer enumeration for the consecutive three-point set in every cyclic group. Berman and Feuer classify perfect conditioning for a different Vandermonde interpolation design in which a continuous scale parameter may be varied; they do not determine the best imperfect Riesz ratio on a fixed finite cyclic Fourier grid. Kunis, Nagel, and Strotmann give broad separated-node stability estimates, and Kunis–Nagel give bounds for nearly colliding pairs. Neither gives the exact three-point discrete minimax classification and multiplicities asserted here. The result refines, but does not follow from, the established observation that equally spaced nodes give a perfectly conditioned matrix whenever the cyclic order is divisible by three.

## Limitations

The theorem treats exactly three consecutive sampling sites and three distinct integer-grid frequencies. It does not optimize frames with extra frequencies, nonconsecutive spatial supports, continuous node locations, or noncyclic groups. Symbolic and numerical checks are supporting verification rather than proofs for infinitely many orders. The literature comparison is based on the material inspected and is not an independent originality certification; an equivalent older specialized conditioning result may exist.

## References

1. S. Ferguson, A. Mayeli, N. Sothanaphan, *Riesz bases of exponentials and multi-tiling in finite abelian groups*, arXiv:1904.04487 (first public 2019-04-09), Sections 3–5.
2. L. Berman and A. Feuer, *On perfect conditioning of Vandermonde matrices on the unit circle*, Electronic Journal of Linear Algebra 16 (2007), DOI 10.13001/1081-3810.1190.
3. S. Kunis, D. Nagel, A. Strotmann, *Multivariate Vandermonde matrices with separated nodes on the unit circle are stable*, arXiv:2103.08167 (2021).
4. S. Kunis and D. Nagel, *On the condition number of Vandermonde matrices with pairs of nearly-colliding nodes*, arXiv:1812.08645 (2018).
