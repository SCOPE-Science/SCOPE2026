# Dimension-six bifurcation of closest product states for complementary Dicke cats

## Finding
For every integer \(n\ge 4\), let \(\lvert D_n^{(k)}\rangle\) be the normalized symmetric \(n\)-qubit Dicke state with \(k\) excitations, and consider the balanced complementary-excitation state
\[
\lvert\Psi_n\rangle=\frac{\lvert D_n^{(1)}\rangle+\lvert D_n^{(n-1)}\rangle}{\sqrt2}.
\]
Its geometric product overlap is \(\Lambda_n^2=\max_{\lvert v_1\rangle,\ldots,\lvert v_n\rangle}\bigl|\langle v_1\otimes\cdots\otimes v_n\mid\Psi_n\rangle\bigr|^2\), and geometric entanglement is \(E_G=1-\Lambda_n^2\).

The exact global optimizer exhibits a sharp transition at six qubits. For \(n=4,5\),
\[
\Lambda_n^2=\frac{n}{2^{n-1}},
\]
and all nearest product states are the \(n-2\) distinct rays \(\lvert u(1/2,2\pi j/(n-2))\rangle^{\otimes n}\), with \(0\le j<n-2\). For every \(n\ge6\), there is a *unique* \(t_n>0\) solving
\[
(n-2)\tanh\!\left(\frac{n-2}{2}t_n\right)=n\tanh(t_n),
\]
and the exact \(2(n-2)\) nearest product rays are
\[
\lvert u(x_n^{\pm},2\pi j/(n-2))\rangle^{\otimes n},\qquad
x_n^{\pm}=\frac{1\pm\tanh(t_n)}2,\quad 0\le j<n-2,
\]
where \(\lvert u(x,\phi)\rangle=\sqrt{1-x}\lvert0\rangle+e^{i\phi}\sqrt{x}\lvert1\rangle\). The overlap is exactly
\[
\Lambda_n^2=\frac{n}{2^{n-1}}\frac{\cosh^2((n-2)t_n/2)}{\cosh^n(t_n)}\qquad(n\ge6).
\]
In particular, \(x_6^{\pm}=(1\pm1/\sqrt3)/2\), \(\Lambda_6^2=2/9\), and
\[
\lim_{n\to\infty}\Lambda_n^2=\frac1{2e},\qquad
\lim_{n\to\infty}E_G(\Psi_n)=1-\frac1{2e}.
\]

## Assumptions and scope
The Hilbert space is \((\mathbb C^2)^{\otimes n}\). Each \(\lvert D_n^{(k)}\rangle\) is the uniform normalized superposition of computational basis strings with exactly \(k\) ones; the two terms defining \(\lvert\Psi_n\rangle\) are orthogonal for \(n\ge4\), making the state normalized. Local product factors may be arbitrary complex normalized vectors, with product states identified up to overall scalar phase. The geometric measure here is \(1-\Lambda_n^2\), not its logarithmic convention.

## Proof
**Reduction to a single qubit.** The symmetry theorem of Hübener–Kleinmann–Wei–González-Guillén–Gühne (arXiv:0905.4822, Lemma 1) establishes that, for \(n\ge3\), *every* optimal complex product vector for a nonzero symmetric pure state has proportional local factors. Thus it is enough to maximize over \(\lvert u(x,\phi)\rangle^{\otimes n}\), with \(0\le x\le1\) and \(\phi\) modulo \(2\pi\). Directly expanding the two Dicke contributions gives
\[
\left|\langle u(x,\phi)^{\otimes n}\mid\Psi_n\rangle\right|^2
=\frac n2\left|\sqrt{x}(1-x)^{(n-1)/2}e^{-i\phi}+x^{(n-1)/2}\sqrt{1-x}\,e^{-i(n-1)\phi}\right|^2.
\]
The endpoints have zero overlap. For each interior \(x\), both summands are positive in modulus, so equality in the triangle inequality holds exactly when \((n-2)\phi\equiv0\pmod{2\pi}\). The maximum at that \(x\) is
\[
F_n(x)=\frac n2\left(\sqrt{x}(1-x)^{(n-1)/2}+x^{(n-1)/2}\sqrt{1-x}\right)^2.
\]

**Global extrema.** Substitute \(x=e^t/(e^t+e^{-t})=(1+\tanh t)/2\) for \(t\in\mathbb R\). The exact identity
\[
F_n(x(t))=\frac{n}{2^{n-1}}\frac{\cosh^2(at)}{\cosh^n(t)},\qquad a=\frac{n-2}{2},
\]
shows evenness in \(t\); its logarithmic derivative is
\[
\frac{d}{dt}\log F_n(x(t))=(n-2)\tanh(at)-n\tanh t.
\]
For \(t>0\) and \(a>1\), the ratio \(R_a(t)=\tanh(at)/\tanh t\) decreases *strictly* from \(a\) to \(1\), since
\[
\frac{d}{dt}\log R_a(t)=\frac{2a}{\sinh(2at)}-\frac2{\sinh(2t)}<0.
\]
Here the inequality is the strict convexity inequality \(\sinh(2at)>a\sinh(2t)\). If \(n=4\), then \(a=1\) and the logarithmic derivative is \(-2\tanh t<0\) on \(t>0\). For \(n=5\), the initial value of \((n-2)R_a(t)\) is \(9/2<5\), so the derivative is again strictly negative. Thus \(t=0\) alone maximizes when \(n=4,5\). For integers \(n\ge6\), the initial value \((n-2)a=(n-2)^2/2\) is strictly above \(n\), whereas the terminal limit \(n-2\) is strictly below \(n\). Strict monotonicity provides exactly one crossing \(t_n>0\), with positive derivative before it and negative derivative after it. Therefore precisely \(\pm t_n\) globally maximize; phase alignment yields the stated complete list of product rays. There are no non-symmetric product optimizers by the cited symmetry theorem.

**Threshold and limit.** For \(n=6\), writing \(z=\tanh t\) reduces \(4\tanh(2t)=6\tanh t\) to \(z^2=1/3\). Substitution gives the stated exact overlap \(2/9\), strictly above the equatorial value \(6/32=3/16\).

For the limit, write \(A=\sqrt{x}(1-x)^{(n-1)/2}\) and \(B=x^{(n-1)/2}\sqrt{1-x}\). On \(0\le x\le1/2\),
\[
A^2\le\frac1n(1-1/n)^{n-1},\qquad B^2\le2^{-n}.
\]
These follow by maximizing \(x(1-x)^{n-1}\) at \(x=1/n\), and bounding \(x^{n-2}\le2^{-(n-2)}\). Thus, for that half-interval,
\[
F_n(x)\le\frac12\left((1-1/n)^{(n-1)/2}+\sqrt n\,2^{-n/2}\right)^2.
\]
The complementary half is identical by the symmetry \(F_n(x)=F_n(1-x)\). The upper bound tends to \(1/(2e)\); the test point \(x=1/n\) provides \(\Lambda_n^2\ge\tfrac12(1-1/n)^{n-1}\), which has the same limit. This completes the proof.

## Verification
Run `python3 verify.py` in the directory containing this document and that standalone file. The verifier expands tensor coefficients directly for \(4\le n\le8\), compares the analytical overlap formula, solves the stationary equation by bisection for finite test sizes, compares sampled latitudes, checks the exact six-qubit constant numerically against the rational \(2/9\), and tests the predicted asymptotic limit at larger finite dimensions. Its expected message is `VERIFY_OK direct_tensor_n=4..8 grid_n=4..16 special_n6=2/9 asymptotic_n=25,80,200`. These are finite corroborations; global uniqueness and the limit are proved analytically above.

## Relationship to prior work
Baguette–Bastin–Martin (arXiv:1407.1738, Sec. II A) identify the entire family of balanced complementary-Dicke superpositions as maximally mixed on one qubit, and study geometric entanglement in general, but their explicit classification covers four qubits rather than the all-dimension nearest-product branch count or the six-qubit transition. Hübener and coauthors (arXiv:0905.4822) prove the symmetric-product optimizer theorem used above. Chen–Xu–Zhu (arXiv:0911.1493, Sec. II A) give a general one-variable optimization recipe for arbitrary symmetric states with nonnegative Dicke coefficients; this supplies the known reduction but does not state the present solved bifurcation and its optimizer count. Aulbach–Markham–Murao (arXiv:1003.5643) study the broader geometry of symmetric closest-product points; Blasone–Dell'Anno–De Siena–Illuminati (arXiv:0712.4085) investigate geometric entanglement of symmetric superpositions of W and GHZ states, a distinct two-component family. No assertion of mathematical priority is implied by these comparisons.

## Limitations
This theorem applies to the equal-phase, equal-weight one-excitation and one-hole symmetric Dicke superposition for all integer \(n\ge4\). It does not determine corresponding thresholds for unequal amplitudes, other excitation indices, nonsymmetric states, mixed-state convex roofs, or alternative entanglement measures. The exact maximizer for \(n\ge6\) is specified by a unique transcendental root, rather than elementary closed forms for arbitrary \(n\). General positive-Dicke-state optimization methods exist in prior work, and an equivalent unstated or differently formulated specialization remains a literature-priority risk. Independent external verification has not been performed.

## References
- D. Baguette, T. Bastin and J. Martin, *Multiqubit symmetric states with maximally mixed one-qubit reductions*, arXiv:1407.1738 (first public 7 July 2014), Secs. II and IV.
- R. Hübener, M. Kleinmann, T.-C. Wei, C. González-Guillén and O. Gühne, *The geometric measure of entanglement for symmetric states*, arXiv:0905.4822 (2009), Lemma 1.
- L. Chen, A. Xu and H. Zhu, *Geometric measure of entanglement for pure multipartite states*, arXiv:0911.1493 (2009), Sec. II A.
- M. Aulbach, D. Markham and M. Murao, *The maximally entangled symmetric state in terms of the geometric measure*, arXiv:1003.5643 (2010).
- M. Blasone, F. Dell'Anno, S. De Siena and F. Illuminati, *Hierarchies of geometric entanglement*, arXiv:0712.4085 (2007), Sec. III C.
