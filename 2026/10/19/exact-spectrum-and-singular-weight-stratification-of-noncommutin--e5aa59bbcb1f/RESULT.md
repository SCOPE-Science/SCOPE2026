# Exact spectrum and singular-weight stratification of noncommuting three-tap Heisenberg convolution

## Finding
Let \(p\) be an odd prime, \(n\ge1\), and \(g,h\) noncommuting elements of the finite exponent-\(p\) Heisenberg group \(H\) of order \(p^{2n+1}\). For all \(a,b,c\in\mathbb C\), not all zero, define \(T=aI+bL_g+cL_h\) on \(\mathbb C[H]\), where \(L_gf(x)=f(g^{-1}x)\). Set \(\zeta=e^{2\pi i/p}\). Then its full characteristic polynomial is
\[
\chi_T(\lambda)=\prod_{r,s\in\mathbb F_p}(\lambda-a-b\zeta^r-c\zeta^s)^{p^{2n-2}}
\left((\lambda-a)^p-b^p-c^p\right)^{(p-1)p^{2n-1}}.
\]
Moreover, with \(Z=\#\{(r,s)\in\mathbb F_p^2:a+b\zeta^r+c\zeta^s=0\}\) and \(F=a^p+b^p+c^p\), its **geometric** nullity is exactly
\[
\dim_{\mathbb C}\ker T=p^{2n-2}Z+(p-1)p^{2n-1}\mathbf1_{\{F=0\}}.
\]
The operator is invertible exactly when \(Z=0\) and \(F\ne0\). If \(abc\ne0\), then \(Z\in\{0,1,2\}\); if exactly two coefficients are nonzero, \(Z\in\{0,p\}\), while with exactly one nonzero coefficient \(Z=0\). For the unweighted filter \(a=b=c=1\), the operator is invertible for every \(p\ge5\), whereas for \(p=3\) its nullity is \(2p^{2n-2}\).

The two kinds of singularities can occur separately or together. For instance \((a,b,c)=(-2,1,1)\) has \(Z=1,F\ne0\); \((1,1,-2^{1/p})\), with the positive real \(p\)-th root, has \(Z=0,F=0\); and for every \(p\ge5\), \((1,\omega,\omega^2)\), where \(\omega\) is a primitive complex cube root, has \(Z=1,F=0\). For the latter case no other resonance occurs, since two circles intersect in at most two points and the putative second equilateral solution would require a nontrivial cubic root to be a \(p\)-th root.

## Assumptions and scope
Let \(V=\mathbb F_p^{2n}\) have a nondegenerate alternating form \(\Omega\). We use \(H=V\times\mathbb F_p\) with multiplication \((v,t)(w,s)=(v+w,t+s+\Omega(v,w)/2)\). The commutator of elements projecting to \(v,w\) is \((0,\Omega(v,w))\). Thus the hypothesis that \(g,h\) do not commute is precisely \(\Omega(\bar g,\bar h)\ne0\). The formula is independent of the central coordinates of \(g,h\), since every element has order dividing \(p\). No assumption of nonzero individual coefficients is needed beyond \((a,b,c)\ne(0,0,0)\). All spectral multiplicities count **algebraic** multiplicity; the nullity formula separately counts geometric multiplicity. They may differ on nilpotent blocks.

## Proof
**(1) One-dimensional blocks.** The abelianization is \(H/[H,H]\cong V\). It has \(p^{2n}\) unitary characters, each occurring once in the regular representation. Since \(\bar g,\bar h\) are linearly independent, their evaluations cover all \((\zeta^r,\zeta^s)\in\mu_p^2\), each with multiplicity \(p^{2n-2}\). This gives exactly the displayed linear factors and contributes \(p^{2n-2}Z\) to the geometric nullity.

**(2) Nonabelian blocks.** There are exactly \(p-1\) remaining inequivalent irreducible representations, one per nontrivial central character, all of dimension \(p^n\). Each appears \(p^n\) times in the regular representation (finite Stone–von Neumann theory). In each such representation, let \(U=\rho(g)\) and \(W=\rho(h)\). They obey \(U^p=W^p=I\) and \(UW=\xi WU\), with \(\xi\) a primitive \(p\)-th root. Symplectic orthogonal decomposition of the pair's nondegenerate plane reduces \((U,W)\) to \(p^{n-1}\) copies of the standard \(p\)-dimensional clock–shift pair, possibly multiplied by \(p\)-th roots (which do not change the calculation).

**(3) Exact clock–shift characteristic polynomial.** For a standard pair, the quantum binomial theorem at a primitive \(p\)-th root gives \((bU+cW)^p=(b^p+c^p)I\). For every \(1\le j<p\), every monomial appearing in \((bU+cW)^j\) is proportional to \(U^uW^v\) with \(u,v\ge0\) and \(u+v=j\). At least one of \(u,v\) is nonzero modulo \(p\), and the trace of this Weyl monomial is zero. Thus \(\operatorname{tr}(bU+cW)^j=0\) for all \(1\le j<p\). Newton's identities, together with the \(p\)-th-power identity, imply that its characteristic polynomial is \(\lambda^p-b^p-c^p\), including the degenerate case \(b^p+c^p=0\). Shifting by \(aI\), each irreducible copy contributes \((\lambda-a)^p-b^p-c^p\). Counting \(p-1\) central characters and both the internal and regular multiplicities gives exponent \((p-1)p^{2n-1}\).

**(4) Geometric kernel of a singular clock–shift block.** When \(F=a^p+b^p+c^p=0\), the \(p\)-dimensional block is singular. It has exactly one-dimensional kernel: if \(b\ne0\), represent \(U\) as the cyclic shift and \(W\) as the diagonal modulation. The kernel equations form a nondegenerate first-order recurrence determining all coordinates from any one coordinate, so nullity is at most one; singularity gives equality. If \(b=0\), then \(c\ne0\), and \(W\) has \(p\) distinct diagonal eigenvalues, exactly one of which cancels \(a\). This yields \((p-1)p^{2n-1}\) extra kernel dimensions. If \(F\ne0\), all nonabelian blocks are invertible. Summing proves the formula.

**(5) Sharp phase-resonance bound.** For \(abc\ne0\), the equation \(b\zeta^r+c\zeta^s=-a\) places \(b\zeta^r\) at the intersection of circles of respective radii \(|b|\) around \(0\) and \(|c|\) around \(-a\). Their centers differ because \(a\ne0\), hence there are at most two intersections. If exactly one coefficient vanishes, a root-of-unity ratio either fixes one coordinate (leaving \(p\) choices for the other) or has no solutions. If two coefficients vanish, no solution occurs. For \(a=b=c=1\), three \(p\)-th roots can sum to zero only at angles separated by \(120\) degrees; since \(p\) is prime, this happens exactly at \(p=3\), with two ordered solutions. In this equal-weight case \(F=3\ne0\).

The examples in the first section follow directly. For the nonabelian-only example, any phase equation would give \(2^{1/p}\in\mathbb Q(\zeta)\); this is impossible because \([\mathbb Q(2^{1/p}):\mathbb Q]=p\), by Eisenstein, whereas \([\mathbb Q(\zeta):\mathbb Q]=p-1\).

## Verification
The supplied standalone Python program `verification/check.py` constructs the complete regular-convolution matrices of \(H_3(p)\) for \(p\in\{3,5,7\}\) in finite characteristics \(\ell\) with \(\ell\equiv1\pmod{3p}\), using exact modular Gaussian elimination. It checks 15 weighted cases against the predicted nullity, including invertible, purely abelian, purely nonabelian, and simultaneous weight strata. The script reports `VERIFY_OK`. Finite-characteristic tests are independent algebraic checks for these samples only, not substitutes for the characteristic-zero proof for all \(p,n\).

## Relationship to prior work
The finite Stone–von Neumann theorem and Heisenberg representations are standard; Gurevich–Hadani supply a precise finite-field representation framework. Arezoomand–Taeri prove a general factorization of characteristic polynomials of Cayley-type operators into irreducible representation blocks. The present result evaluates the noncommuting weighted three-tap blocks, classifies their **geometric** kernels even at multiple-root boundaries, and provides the complete weight-dependent singular locus for every odd prime and every Heisenberg dimension. Its specific spectrum/nullity formula is not asserted by either cited work. Related abelian sparse-convolution results cannot account for the independent nonabelian Fermat term.

## Limitations
This theorem assumes odd prime characteristic, exponent-\(p\) Heisenberg groups, and a genuinely noncommuting generator pair. It does not classify the commuting-pair regime, larger supports, arbitrary finite nilpotent groups, or condition numbers. Algebraic and geometric multiplicities differ when \(a=0\) and \(b^p+c^p=0\); the formula above deliberately uses geometric nullity. Full historical priority has not been independently certified, and an unrecognized equivalent formulation in older quantum-torus literature remains possible.

## References
1. S. Gurevich and R. Hadani, *Quantization of symplectic vector spaces over finite fields*, arXiv:0705.4556, first public 31 May 2007. https://arxiv.org/abs/0705.4556
2. M. Arezoomand and B. Taeri, *On the Characteristic Polynomial of n-Cayley Digraphs*, Electronic Journal of Combinatorics 20(3), P57 (2013), DOI:10.37236/3105. https://www.combinatorics.org/ojs/index.php/eljc/article/download/v20i3p57/pdf/
