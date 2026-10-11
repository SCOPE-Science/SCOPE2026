# A rigorous four-fifths non-frame obstruction for an even rational Gabor window

## Finding

For the even rational window
\[
g(x)=\frac{x^2-1}{(x^2+1)(x^2+4)(x^2+9)},\qquad x\in\mathbb R,
\]
there exists a real number \(\beta_*\in(3/20,7/20)\) for which the Gabor family
\[
\mathcal G(g,\alpha_*,\beta_*)
=\{e^{2\pi i\beta_*\ell x}g(x-\alpha_*k):k,\ell\in\mathbb Z\},
\qquad \alpha_*:=\frac4{5\beta_*},
\]
is **not** a frame for \(L^2(\mathbb R)\). Thus the conjectured non-frame phenomenon at rational density \(\alpha_*\beta_*=4/5\) holds for the first case beyond the previously proved indices \(1,2,3\).

More precisely, the continuous real determinant \(D(\beta)\) defined below obeys the rigorously certified inequalities
\[
2.1035\times10^{-6}<D(3/20)<2.1036\times10^{-6},
\]
\[
-5.6824\times10^{-6}<D(7/20)<-5.6823\times10^{-6}.
\]
The intermediate value theorem then gives the required singular lattice fiber. The cited source already developed a parity-based rank reduction and reported numerical evidence at density \(4/5\); the contribution here is a *rigorous sign certificate* and the consequent proved non-frame statement for that first unresolved index, not a new general rank-reduction principle.

## Assumptions and scope

The system uses time translations \(T_{\alpha k}g(x)=g(x-\alpha k)\), modulations \(M_{\beta\ell}g(x)=e^{2\pi i\beta\ell x}g(x)\), and the usual frame definition on the complex Hilbert space \(L^2(\mathbb R)\). The fixed window is real, even, continuous, and satisfies \(g(x)=O(|x|^{-4})\). The conclusion is **existence** of at least one non-frame lattice at product \(4/5\), not non-frame behavior for every lattice having that product.

## Proof

**1. The rank test in the time-domain fibers.** Fix \(\beta>0\) and put \(\alpha=4/(5\beta)\). Folding the modulation coefficients across the period \(1/\beta\) and applying the Fourier-series Parseval identity gives
\[
\sum_{k,\ell\in\mathbb Z}|\langle f,M_{\beta\ell}T_{\alpha k}g\rangle|^2
=\frac1\beta\int_0^{1/\beta}
\sum_{k\in\mathbb Z}\left|\sum_{n\in\mathbb Z} f(x+n/\beta)\overline{g(x+n/\beta-\alpha k)}\right|^2\,dx.
\]
Write \(k=t+5m\), where \(0\le t\le4\), so \(\alpha(t+5m)=\alpha t+4m/\beta\). A Fourier series over the residue classes \(n=j+4m\), \(0\le j\le3\), therefore fibers the analysis operator into a continuous \(4\times5\) matrix. At the specific fiber \(x=0\) and frequency \(\theta=0\), its entries are
\[
M_{j,t}(\beta)=\sum_{m\in\mathbb Z}
 g\!\left(\frac{j+4m-4t/5}{\beta}\right),
\qquad 0\le j\le3,\quad0\le t\le4.
\]
The series is locally uniformly convergent in fiber parameters because the window decays to fourth order. If this matrix has rank below \(4\) at any \(\beta>0\), continuity forces arbitrarily small singular values on neighborhoods of positive fiber measure, contradicting a uniform positive lower Gabor frame bound. No assumption that a single zero-measure fiber alone violates a frame inequality is used: continuity supplies the essential-infimum contradiction.

**2. The even-symmetry block.** Define the continuous, even, \(4\)-periodic function
\[
h_\beta(u)=\sum_{m\in\mathbb Z}g\!\left(\frac{u+4m}{\beta}\right).
\]
Then \(M_{j,t}=h_\beta(j-4t/5)\), and
\(M_{4-j,5-t}=M_{j,t}\) with both indices interpreted cyclically. Reflection decomposes the \(4\)-dimensional row space into even and odd parts of dimensions \(3\) and \(1\), and the \(5\)-dimensional column space into corresponding parts of dimensions \(3\) and \(2\). On the even parts, using row vectors \(e_0,e_2,e_1+e_3\) and column vectors \(f_0,f_1+f_4,f_2+f_3\), the matrix is, up to invertible basis-normalization factors,
\[
B(\beta)=\begin{pmatrix}
h(0)&2h(4/5)&2h(8/5)\\
h(2)&2h(6/5)&2h(2/5)\\
2h(1)&2[h(1/5)+h(9/5)]&2[h(3/5)+h(7/5)]
\end{pmatrix},\qquad h=h_\beta.
\]
(The chosen column coordinates are obtained by applying the original matrix to the summed column basis vectors; row coordinates use the displayed sums.) Put \(D(\beta)=\det B(\beta)\). If \(D(\beta)=0\), the even block has rank at most \(2\), while the odd block has rank at most \(1\), hence \(\operatorname{rank}M(\beta)\le3<4\).

**3. A finite closed form for the determinant.** The partial fraction identity is exact:
\[
g(x)=-\frac1{12(x^2+1)}+\frac1{3(x^2+4)}-\frac1{4(x^2+9)}.
\]
The classical periodic Cauchy summation formula gives
\[
h_\beta(u)=\frac{\pi\beta}{4}\sum_{a=1}^3\frac{c_a}{a}
\frac{1-t_a^2}{1+t_a^2-2t_a\cos(\pi u/2)},
\quad (c_1,c_2,c_3)=(-1/12,1/3,-1/4),\quad
t_a=e^{-\pi a\beta/2}.
\]
For completeness, that formula follows from the absolutely convergent Fourier series of the period-\(4\) sum of \(((u/\beta)^2+a^2)^{-1}\), or from the standard hyperbolic-cotangent partial-fraction identity. All denominators are strictly positive for \(\beta>0\) since \(0<t_a<1\); hence \(D\) is real and continuous.

**4. Exact rational sign enclosures and conclusion.** The accompanying standalone script `verify_gabor_4_5.py` evaluates the above expression using **exact rational interval arithmetic**, not a floating-point tolerance test. It bounds \(\pi\) through Machin's identity \(\pi=16\arctan(1/5)-4\arctan(1/239)\) and rational alternating arctangent-series truncations. It encloses the positive-argument exponential and cosine factors by terminating Taylor series with analytically bounded next terms and Lipschitz correction for the tiny enclosure of \(\pi\). All subsequent arithmetic uses rational outward enclosures on a decimal grid of size \(10^{-32}\). The script asserts the two strict rational determinant intervals stated above. These inequalities, together with continuity, imply \(D(\beta_*)=0\) for some \(\beta_*\in(3/20,7/20)\). Steps 1–2 then exclude a Gabor frame at \((\alpha_*,\beta_*)\).

## Verification

Run `python3 verify_gabor_4_5.py` using only the Python standard library. It verifies each strict rational determinant enclosure and prints `CERTIFIED` only after both assertions succeed. The proof of the unbounded-dimensional non-frame assertion is the analytic fiber-rank argument; a finite scan of lattice parameters or truncated Zak sums cannot replace that argument. Independent approximate cross-checks put a root near \(\beta\approx0.1995761259\), but neither its uniqueness nor the decimal approximation is needed by the theorem.

## Relationship to prior work

R. Ghosh, *Gabor Frame Regions and Non-Frame Obstructions for an even Rational Window* (arXiv:2609.19232v1, first public version September 16, 2026), studies **this exact window**. Its Theorem 1.4 proves non-frame lattices for products \(1/3,1/2,2/3,3/4\); Conjecture 4.1 proposes an obstruction at every \(p/(p+1)\); and Section 4.1 presents numerical, not rigorous, determinant sign evidence for \(2\le p\le200\). In particular it does **not** supply a proved \(4/5\) example. Its symmetry reduction is acknowledged rather than claimed as new. The present certificate establishes the first remaining natural case \(p=4\) with no generalization to all \(p\).

The earlier Ghosh preprint *Gabor Frame for a Rational Window with Symmetric Poles* (arXiv:2608.10568, version 2) treats the **different odd window** \(x/((x^2+1)(x^2+4))\); its parity obstruction does not imply a result for the current even generator. Published related work on Gaussian-derivative Gabor lattices and on finite-field Gabor systems concerns different windows or settings, and does not imply the specific rational-window fiber singularity here.

## Limitations

Only existence at the single rational density \(4/5\) is proved. The proof neither classifies all obstruction parameters nor asserts that the root is unique, nor resolves the full conjecture for any \(p>4\). The numerical location of the root is contextual, not certified as an isolated/unique root. Previously published numerical observations do not themselves constitute the analytic sign proof. An equivalent proof may exist in unindexed literature; independent external validation has not been performed.

## References

1. R. Ghosh, *Gabor Frame Regions and Non-Frame Obstructions for an even Rational Window*, arXiv:2609.19232v1 (publicly posted 2026-09-16), especially Theorem 1.4 and Sections 4 and 4.1. https://arxiv.org/abs/2609.19232
2. R. Ghosh, *Gabor Frame for a Rational Window with Symmetric Poles*, arXiv:2608.10568v2 (2026), an odd-window comparator. https://arxiv.org/abs/2608.10568
3. K. Gröchenig, *Foundations of Time-Frequency Analysis*, Birkhäuser, 2001 (fiberization and Gabor-frame background).
